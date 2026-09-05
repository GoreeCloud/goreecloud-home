from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import re

_IDENTIFIER = re.compile(r"^[a-z0-9][a-z0-9._-]{0,127}$")
_CAPABILITY = re.compile(r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+$")


def _validate_identifier(value: str, label: str) -> str:
    if not _IDENTIFIER.fullmatch(value):
        raise ValueError(f"invalid {label}: {value!r}")
    return value


def validate_capability(value: str) -> str:
    if not _CAPABILITY.fullmatch(value):
        raise ValueError(f"invalid capability: {value!r}")
    return value


@dataclass(frozen=True, slots=True)
class Home:
    id: str
    name: str

    def __post_init__(self) -> None:
        _validate_identifier(self.id, "home id")
        if not self.name.strip():
            raise ValueError("home name must not be empty")


@dataclass(frozen=True, slots=True)
class Room:
    id: str
    home_id: str
    name: str

    def __post_init__(self) -> None:
        _validate_identifier(self.id, "room id")
        _validate_identifier(self.home_id, "home id")
        if not self.name.strip():
            raise ValueError("room name must not be empty")


@dataclass(slots=True)
class Device:
    id: str
    home_id: str
    name: str
    capabilities: frozenset[str]
    room_id: str | None = None
    adapter: str | None = None
    desired_state: dict[str, Any] = field(default_factory=dict)
    reported_state: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _validate_identifier(self.id, "device id")
        _validate_identifier(self.home_id, "home id")
        if self.room_id is not None:
            _validate_identifier(self.room_id, "room id")
        if not self.name.strip():
            raise ValueError("device name must not be empty")
        normalized = frozenset(validate_capability(item) for item in self.capabilities)
        if not normalized:
            raise ValueError("device must expose at least one capability")
        self.capabilities = normalized

    def require_capability(self, capability: str) -> None:
        validate_capability(capability)
        if capability not in self.capabilities:
            raise ValueError(f"device {self.id!r} does not expose {capability!r}")
