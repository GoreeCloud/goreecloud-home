from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from threading import RLock
from typing import Any

from .availability import (
    DeviceAvailability,
    normalize_availability,
    normalize_observed_at,
    normalize_reason,
    validate_availability_transition,
)
from .capabilities import CapabilityRegistry, default_capability_registry
from .journal import EventJournal
from .models import Device, Home, Room
from .storage import LATEST_SCHEMA_VERSION, SQLiteStateStore


class HomeCore:
    """Authoritative local Home domain service for the Development foundation.

    Authentication and authorization are intentionally not implemented in this class.
    Network/control adapters must add GoreeCloud Identity and Wardveil enforcement before
    privileged control is exposed beyond a trusted internal boundary.
    """

    def __init__(
        self,
        journal: EventJournal,
        *,
        capability_registry: CapabilityRegistry | None = None,
        state_store: SQLiteStateStore | None = None,
    ) -> None:
        self.journal = journal
        self.capabilities = capability_registry or default_capability_registry()
        self.state_store = state_store or SQLiteStateStore(journal.database)
        if self.state_store.database is not self.journal.database:
            raise ValueError("state store and event journal must share one database authority")
        self._lock = RLock()
        self._homes: dict[str, Home] = {}
        self._rooms: dict[str, Room] = {}
        self._devices: dict[str, Device] = {}
        self._load_persisted_state()

    def create_home(self, home: Home) -> None:
        with self._lock:
            if home.id in self._homes:
                raise ValueError(f"home already exists: {home.id}")
            with self.journal.transaction():
                self.state_store.insert_home(home)
                self.journal.append("home.created", home.id, {"name": home.name})
            self._homes[home.id] = home

    def create_room(self, room: Room) -> None:
        with self._lock:
            if room.home_id not in self._homes:
                raise KeyError(f"unknown home: {room.home_id}")
            if room.id in self._rooms:
                raise ValueError(f"room already exists: {room.id}")
            with self.journal.transaction():
                self.state_store.insert_room(room)
                self.journal.append(
                    "room.created",
                    room.id,
                    {"home_id": room.home_id, "name": room.name},
                )
            self._rooms[room.id] = room

    def register_device(self, device: Device) -> None:
        with self._lock:
            if device.home_id not in self._homes:
                raise KeyError(f"unknown home: {device.home_id}")
            if device.room_id is not None:
                room = self._rooms.get(device.room_id)
                if room is None:
                    raise KeyError(f"unknown room: {device.room_id}")
                if room.home_id != device.home_id:
                    raise ValueError("device room must belong to the same home")
            if device.id in self._devices:
                raise ValueError(f"device already exists: {device.id}")
            self._validate_device_contract(device)
            persisted = deepcopy(device)
            with self.journal.transaction():
                self.state_store.insert_device(persisted)
                self.journal.append(
                    "device.registered",
                    persisted.id,
                    {
                        "home_id": persisted.home_id,
                        "room_id": persisted.room_id,
                        "name": persisted.name,
                        "capabilities": sorted(persisted.capabilities),
                        "adapter": persisted.adapter,
                        "availability": persisted.availability.value,
                    },
                )
            self._devices[persisted.id] = persisted

    def set_desired_state(self, device_id: str, capability: str, value: Any) -> None:
        with self._lock:
            device = self._require_device(device_id)
            device.require_capability(capability)
            self.capabilities.validate_desired(capability, value)
            persisted_value = deepcopy(value)
            with self.journal.transaction():
                self.state_store.set_device_state(
                    device.id, "desired", capability, persisted_value
                )
                self.journal.append(
                    "device.desired_state.changed",
                    device.id,
                    {"capability": capability, "value": persisted_value},
                )
            device.desired_state[capability] = persisted_value

    def set_reported_state(self, device_id: str, capability: str, value: Any) -> None:
        with self._lock:
            device = self._require_device(device_id)
            device.require_capability(capability)
            self.capabilities.validate_reported(capability, value)
            persisted_value = deepcopy(value)
            with self.journal.transaction():
                self.state_store.set_device_state(
                    device.id, "reported", capability, persisted_value
                )
                self.journal.append(
                    "device.reported_state.changed",
                    device.id,
                    {"capability": capability, "value": persisted_value},
                )
            device.reported_state[capability] = persisted_value

    def observe_device_availability(
        self,
        device_id: str,
        availability: DeviceAvailability | str,
        *,
        observed_at: datetime | None = None,
        reason: str | None = None,
    ) -> None:
        with self._lock:
            device = self._require_device(device_id)
            target = normalize_availability(availability)
            validate_availability_transition(device.availability, target)
            occurred_at = normalize_observed_at(observed_at)
            normalized_reason = normalize_reason(reason)
            changed = target != device.availability
            event_type = (
                "device.availability.changed"
                if changed
                else "device.availability.observed"
            )
            payload: dict[str, Any] = {
                "availability": target.value,
                "observed_at": occurred_at,
            }
            if changed:
                payload["previous_availability"] = device.availability.value
            if normalized_reason is not None:
                payload["reason"] = normalized_reason
            with self.journal.transaction():
                self.state_store.update_availability(
                    device.id, target, occurred_at, normalized_reason
                )
                self.journal.append(event_type, device.id, payload)
            device.availability = target
            device.availability_updated_at = occurred_at
            device.availability_reason = normalized_reason

    def ready(self) -> bool:
        return (
            self.journal.ready()
            and self.state_store.schema_version == LATEST_SCHEMA_VERSION
        )

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            availability_counts = {
                availability.value: sum(
                    1
                    for device in self._devices.values()
                    if device.availability == availability
                )
                for availability in DeviceAvailability
            }
            return {
                "homes": len(self._homes),
                "rooms": len(self._rooms),
                "devices": len(self._devices),
                "storage_schema_version": self.state_store.schema_version,
                "capability_contract_version": self.capabilities.contract_version,
                "availability_counts": availability_counts,
                "device_state": {
                    device_id: {
                        "home_id": device.home_id,
                        "room_id": device.room_id,
                        "capabilities": sorted(device.capabilities),
                        "desired": deepcopy(device.desired_state),
                        "reported": deepcopy(device.reported_state),
                        "availability": device.availability.value,
                        "availability_updated_at": device.availability_updated_at,
                        "availability_reason": device.availability_reason,
                    }
                    for device_id, device in sorted(self._devices.items())
                },
            }

    def _load_persisted_state(self) -> None:
        homes, rooms, devices = self.state_store.load()
        for room in rooms.values():
            if room.home_id not in homes:
                raise RuntimeError(f"persisted room references unknown home: {room.id}")
        for device in devices.values():
            if device.home_id not in homes:
                raise RuntimeError(f"persisted device references unknown home: {device.id}")
            if device.room_id is not None:
                room = rooms.get(device.room_id)
                if room is None or room.home_id != device.home_id:
                    raise RuntimeError(
                        f"persisted device has invalid room/home boundary: {device.id}"
                    )
            self._validate_device_contract(device)
        self._homes = homes
        self._rooms = rooms
        self._devices = devices

    def _validate_device_contract(self, device: Device) -> None:
        self.capabilities.validate_device_capabilities(device.capabilities)
        for capability, value in device.desired_state.items():
            device.require_capability(capability)
            self.capabilities.validate_desired(capability, value)
        for capability, value in device.reported_state.items():
            device.require_capability(capability)
            self.capabilities.validate_reported(capability, value)

    def _require_device(self, device_id: str) -> Device:
        try:
            return self._devices[device_id]
        except KeyError as exc:
            raise KeyError(f"unknown device: {device_id}") from exc
