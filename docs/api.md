# GoreeCloud Home API v1 — Development Foundation

Current routes remain read-only local diagnostics:

- `GET /livez` — process liveness.
- `GET /readyz` — shared SQLite authority and expected schema readiness.
- `GET /api/v1/status` — bounded lifecycle metadata and aggregate Home/Room/Device/adapter/availability/lifecycle counts plus storage and contract versions.

The status response deliberately omits household state values, state revisions, adapter reasons, device/room names, event payloads, credentials, and identities.

No HTTP write/control route is implemented in `0.1.0-dev.3`. Internal Home Core state methods now support optimistic `expected_revision` checks, but those methods are not network authorization boundaries. Future network writes require GoreeCloud Identity, Wardveil Security, explicit scopes, and documented conflict semantics.

Current contract versions: API `v1`, capability `1.0`, device availability `1.0`, state revision `1.0`, adapter lifecycle `1.0`, SQLite schema `5`.
