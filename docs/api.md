# GoreeCloud Home API v1 — Development Foundation

Current routes are read-only local diagnostics:

- `GET /livez` — process liveness.
- `GET /readyz` — shared SQLite authority and expected schema readiness.
- `GET /api/v1/status` — bounded product/version/lifecycle/conformance metadata, aggregate Home/Room/Device and availability counts, storage schema version, capability-contract version, and `control_api: not-exposed`.

The status response deliberately omits device/room names, desired/reported values, event payloads, credentials, identities, availability reasons and adapter-private data.

No HTTP write/control route is implemented in `0.1.0-dev.2`; `POST` receives `405 Method Not Allowed`. Future network control requires explicit GoreeCloud Identity and Wardveil authorization contracts.

Current contract versions: API `v1`, capability contract `1.0`, device availability contract `1.0`, SQLite schema `3`.
