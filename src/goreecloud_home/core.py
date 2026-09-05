from __future__ import annotations

from copy import deepcopy
from threading import RLock
from typing import Any

from .journal import EventJournal
from .models import Device, Home, Room


class HomeCore:
    """Authoritative local in-process domain service for the Development foundation.

    Authentication and authorization are intentionally not implemented in this class.
    Network/control adapters must add GoreeCloud Identity and Wardveil enforcement before
    privileged control is exposed beyond a trusted internal boundary.
    """

    def __init__(self, journal: EventJournal) -> None:
        self.journal = journal
        self._lock = RLock()
        self._homes: dict[str, Home] = {}
        self._rooms: dict[str, Room] = {}
        self._devices: dict[str, Device] = {}

    def create_home(self, home: Home) -> None:
        with self._lock:
            if home.id in self._homes:
                raise ValueError(f"home already exists: {home.id}")
            self._homes[home.id] = home
            self.journal.append("home.created", home.id, {"name": home.name})

    def create_room(self, room: Room) -> None:
        with self._lock:
            if room.home_id not in self._homes:
                raise KeyError(f"unknown home: {room.home_id}")
            if room.id in self._rooms:
                raise ValueError(f"room already exists: {room.id}")
            self._rooms[room.id] = room
            self.journal.append(
                "room.created",
                room.id,
                {"home_id": room.home_id, "name": room.name},
            )

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
            self._devices[device.id] = deepcopy(device)
            self.journal.append(
                "device.registered",
                device.id,
                {
                    "home_id": device.home_id,
                    "room_id": device.room_id,
                    "name": device.name,
                    "capabilities": sorted(device.capabilities),
                    "adapter": device.adapter,
                },
            )

    def set_desired_state(self, device_id: str, capability: str, value: Any) -> None:
        with self._lock:
            device = self._require_device(device_id)
            device.require_capability(capability)
            device.desired_state[capability] = deepcopy(value)
            self.journal.append(
                "device.desired_state.changed",
                device.id,
                {"capability": capability, "value": value},
            )

    def set_reported_state(self, device_id: str, capability: str, value: Any) -> None:
        with self._lock:
            device = self._require_device(device_id)
            device.require_capability(capability)
            device.reported_state[capability] = deepcopy(value)
            self.journal.append(
                "device.reported_state.changed",
                device.id,
                {"capability": capability, "value": value},
            )

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return {
                "homes": len(self._homes),
                "rooms": len(self._rooms),
                "devices": len(self._devices),
                "device_state": {
                    device_id: {
                        "home_id": device.home_id,
                        "room_id": device.room_id,
                        "capabilities": sorted(device.capabilities),
                        "desired": deepcopy(device.desired_state),
                        "reported": deepcopy(device.reported_state),
                    }
                    for device_id, device in sorted(self._devices.items())
                },
            }

    def _require_device(self, device_id: str) -> Device:
        try:
            return self._devices[device_id]
        except KeyError as exc:
            raise KeyError(f"unknown device: {device_id}") from exc
