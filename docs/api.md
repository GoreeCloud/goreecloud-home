# GoreeCloud Home API v1 — Development Foundation

Base transport: local HTTP for Development diagnostics.

## GET /livez

Returns process liveness only.

Example semantic response:

```json
{"status":"live"}
```

## GET /readyz

Checks the local event journal connection and reports bounded readiness.

## GET /api/v1/status

Returns product identity, version, lifecycle, conformance state, aggregate domain counts and the fact that the control API is not exposed.

It deliberately does not return device names, room names, desired/reported device values, event payloads, credentials or household identities.

## Writes

No HTTP write/control route is implemented in 0.1.0-dev.1. `POST` receives `405 Method Not Allowed` with `control_api_not_exposed`.

Future control APIs require GoreeCloud Identity and Wardveil authorization contracts before exposure beyond trusted internal code.