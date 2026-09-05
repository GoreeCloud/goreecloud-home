from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
import json

from .core import HomeCore


class HomeStatusServer(ThreadingHTTPServer):
    def __init__(self, address: tuple[str, int], core: HomeCore) -> None:
        self.core = core
        super().__init__(address, HomeStatusHandler)


class HomeStatusHandler(BaseHTTPRequestHandler):
    server: HomeStatusServer

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        if self.path == "/livez":
            self._json(HTTPStatus.OK, {"status": "live"})
            return
        if self.path == "/readyz":
            ready = self.server.core.journal.ready()
            self._json(
                HTTPStatus.OK if ready else HTTPStatus.SERVICE_UNAVAILABLE,
                {"status": "ready" if ready else "not-ready"},
            )
            return
        if self.path == "/api/v1/status":
            snapshot = self.server.core.snapshot()
            self._json(
                HTTPStatus.OK,
                {
                    "product": "GoreeCloud Home",
                    "version": "0.1.0-dev.1",
                    "lifecycle": "development",
                    "conformance": "nonconformant",
                    "counts": {
                        "homes": snapshot["homes"],
                        "rooms": snapshot["rooms"],
                        "devices": snapshot["devices"],
                    },
                    "control_api": "not-exposed",
                },
            )
            return
        self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def do_POST(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        self._json(
            HTTPStatus.METHOD_NOT_ALLOWED,
            {"error": "control_api_not_exposed"},
            extra_headers={"Allow": "GET"},
        )

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _json(
        self,
        status: HTTPStatus,
        payload: dict[str, Any],
        *,
        extra_headers: dict[str, str] | None = None,
    ) -> None:
        encoded = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
        self.send_response(int(status))
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        if extra_headers:
            for name, value in extra_headers.items():
                self.send_header(name, value)
        self.end_headers()
        self.wfile.write(encoded)
