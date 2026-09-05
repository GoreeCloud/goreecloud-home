# GoreeCloud Home API v1 — Development Foundation

Current network routes remain read-only local diagnostics:

- `GET /livez` — process liveness.
- `GET /readyz` — Home state SQLite authority and expected Home schema readiness.
- `GET /api/v1/status` — bounded lifecycle metadata, aggregate Home/Room/Device/adapter/availability counts, Home storage schema version, and capability/state-revision/adapter/automation contract versions.

The status response deliberately omits household state values, state revisions, automation definitions/history, adapter reasons, device/room names, event payloads, credentials and identities.

No HTTP write/control route is implemented in `0.1.0-dev.4`. `HomeAutomationEngine` is a trusted local Python boundary sharing Home Core's database/journal. Its scene and automation methods are not network authorization surfaces.

Current versions: API `v1`, capability `1.0`, device availability `1.0`, state revision `1.0`, adapter lifecycle `1.0`, automation contract `1.0`, Home state schema `5`, automation storage schema `1`.
