# GoreeCloud Home — Features

Status labels: **Implemented**, **Partial**, **Planned**, **Blocked**.

## Implemented in 0.1.0-dev.2

- **Implemented:** local Home, Room and Device domain registry.
- **Implemented:** durable SQLite persistence for homes, rooms, devices, desired state and reported state.
- **Implemented:** versioned SQLite migration ledger through schema version 3.
- **Implemented:** atomic state-plus-event transactions inside one local SQLite authority.
- **Implemented:** restart restoration of persisted Home Core state.
- **Implemented:** protocol-neutral capability identifiers and machine-readable capability contract v1.
- **Implemented:** type/range/unit/enumeration validation for the initial capability set.
- **Implemented:** read-only capability rejection and distinct desired/reported semantics where needed.
- **Implemented:** desired-state and reported-state separation.
- **Implemented:** durable SQLite event journal with monotonic sequence IDs.
- **Implemented:** machine-readable device availability contract v1.
- **Implemented:** persistent `unknown`, `online`, `degraded`, and `offline` availability with transition validation and observation events.
- **Implemented:** bounded read-only loopback liveness, readiness and status endpoints.
- **Implemented:** automated tests for domain, persistence, migration, transaction rollback, availability, and contract parity.
- **Implemented:** GoreeCloud Platform Contract v0.2 manifest.

## Planned Home Core

- **Planned:** floors, zones and reusable device groups.
- **Planned:** state revision/conflict semantics for concurrent adapter/client activity.
- **Planned:** adapter registration and lifecycle contracts.
- **Planned:** scenes, triggers, conditions, actions and schedules.
- **Planned:** automation execution history, retries and loop prevention.
- **Planned:** energy/utility telemetry and richer device diagnostics.
- **Planned:** controlled Home Node and controller failover model.

## Planned protocols

- **Planned:** Matter discovery, commissioning, fabrics, subscriptions and device control.
- **Planned:** Thread Border Router integration.
- **Planned:** local Wi-Fi/LAN discovery and adapters.
- **Planned:** MQTT, Zigbee, Z-Wave and BLE/proxy-node adapters.
- **Planned:** bounded vendor adapters when open/local standards are insufficient.

## Planned clients and GoreeCloud integration

- **Blocked:** Glaze UI web/desktop Home client pending implementation and acceptance.
- **Blocked:** GoreeCloud Identity household authentication, sessions, roles and capability scopes.
- **Blocked:** Wardveil Security privileged-action, device-trust, secret and risk controls.
- **Blocked:** Privacy Shield retention, telemetry, camera/presence and sharing policy enforcement.
- **Blocked:** Everkeep backup, restore, export and recovery acceptance.
- **Blocked:** GoreeCloud Manager registration/health consumption.
- **Blocked:** GoreeCloud Mesh capability registration and cross-product events.
- **Planned:** Android/Linux clients, wall dashboard, actionable notifications, GoreeCloud Location presence, and bounded GoreeCloud AI/voice assistance.
