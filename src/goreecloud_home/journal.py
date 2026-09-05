from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from threading import RLock
from typing import Any
import json
import sqlite3


@dataclass(frozen=True, slots=True)
class Event:
    sequence: int
    event_type: str
    entity_id: str
    occurred_at: str
    payload: dict[str, Any]


class EventJournal:
    """Durable local event journal for Home Core domain transitions."""

    def __init__(self, path: str | Path) -> None:
        self.path = str(path)
        self._lock = RLock()
        self._connection = sqlite3.connect(self.path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.execute("PRAGMA foreign_keys=ON")
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                occurred_at TEXT NOT NULL,
                payload_json TEXT NOT NULL
            )
            """
        )
        self._connection.commit()

    def close(self) -> None:
        with self._lock:
            self._connection.close()

    def append(self, event_type: str, entity_id: str, payload: dict[str, Any]) -> Event:
        if not event_type or not entity_id:
            raise ValueError("event_type and entity_id are required")
        occurred_at = datetime.now(timezone.utc).isoformat()
        encoded = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        with self._lock:
            cursor = self._connection.execute(
                "INSERT INTO events(event_type, entity_id, occurred_at, payload_json) VALUES (?, ?, ?, ?)",
                (event_type, entity_id, occurred_at, encoded),
            )
            self._connection.commit()
            sequence = int(cursor.lastrowid)
        return Event(sequence, event_type, entity_id, occurred_at, json.loads(encoded))

    def list_since(self, sequence: int = 0, limit: int = 100) -> list[Event]:
        if sequence < 0:
            raise ValueError("sequence must be non-negative")
        if not 1 <= limit <= 1000:
            raise ValueError("limit must be between 1 and 1000")
        with self._lock:
            rows = self._connection.execute(
                "SELECT sequence, event_type, entity_id, occurred_at, payload_json "
                "FROM events WHERE sequence > ? ORDER BY sequence ASC LIMIT ?",
                (sequence, limit),
            ).fetchall()
        return [
            Event(
                sequence=int(row["sequence"]),
                event_type=str(row["event_type"]),
                entity_id=str(row["entity_id"]),
                occurred_at=str(row["occurred_at"]),
                payload=json.loads(str(row["payload_json"])),
            )
            for row in rows
        ]

    def ready(self) -> bool:
        with self._lock:
            row = self._connection.execute("SELECT 1 AS ok").fetchone()
        return bool(row and row["ok"] == 1)
