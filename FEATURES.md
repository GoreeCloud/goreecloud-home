# GoreeCloud Home — Features

Status labels: **Implemented**, **Partial**, **Planned**, **Blocked**.

## Implemented in 0.1.0-dev.1

- **Implemented:** local Home, Room and Device domain registry.
- **Implemented:** protocol-neutral capability identifiers on devices.
- **Implemented:** desired-state and reported-state separation.
- **Implemented:** durable SQLite event journal with monotonic sequence IDs.
- **Implemented:** read-only loopback liveness, readiness and bounded status endpoints.
- **Implemented:** domain/state/event unit tests and compile validation in CI.
- **Implemented:** GoreeCloud Platform Contract v0.2 manifest.

## Planned Home Core

- **Planned:** floors, zones and reusable device groups.
- **Planned:** scenes and scene activation.
- **Planned:** automation triggers, conditions and actions.
- **Planned:** schedules, sunrise/sunset and calendar-aware conditions.
- **Planned:** automation execution history, retries and loop prevention.
- **Planned:** device availability/health and adapter diagnostics.
- **Planned:** energy and utility telemetry model.
- **Planned:** multi-controller recovery and controlled Home Node model.

## Planned protocols

- **Planned:** Matter discovery and commissioning.
- **Planned:** Matter fabrics, subscriptions and device control.
- **Planned:** Thread Border Router integration.
- **Planned:** local Wi-Fi/LAN discovery and adapters.
- **Planned:** MQTT adapter.
- **Planned:** Zigbee coordinator and device adapter support.
- **Planned:** Z-Wave controller and device adapter support.
- **Planned:** BLE devices and proxy nodes.
- **Planned:** bounded vendor adapters when open/local standards are insufficient.

## Planned clients and experience

- **Blocked:** Glaze UI web/desktop Home client pending implementation and acceptance.
- **Planned:** Android client.
- **Planned:** Linux client/shell integration.
- **Planned:** tablet/wall-dashboard mode.
- **Planned:** favorites, rooms, devices, scenes and automation dashboards.
- **Planned:** visual automation editor backed by the same declarative automation model.
- **Planned:** actionable notifications and quick controls.

## Planned GoreeCloud integration

- **Blocked:** GoreeCloud Identity household auth, sessions, roles and capability scopes.
- **Blocked:** Wardveil Security privileged action, device trust, secret and risk controls.
- **Blocked:** Privacy Shield retention, telemetry, camera/presence and sharing policy enforcement.
- **Blocked:** Everkeep backup, restore, export and recovery acceptance.
- **Blocked:** GoreeCloud Manager operational registration and health consumption.
- **Blocked:** GoreeCloud Mesh capability registration and cross-product event exchange.
- **Blocked:** Glaze UI conformance and accessibility acceptance.
- **Planned:** GoreeCloud Location geofencing/presence integration.
- **Planned:** GoreeCloud AI natural-language automation assistance and bounded voice control.

## Planned device categories

Lights, switches, smart plugs, locks, garage doors, covers/blinds, fans, thermostats/HVAC, environmental sensors, motion/contact sensors, alarms, cameras, doorbells, media devices, appliances, irrigation, vacuums, energy meters and other devices that can be mapped safely into versioned GoreeCloud capabilities.