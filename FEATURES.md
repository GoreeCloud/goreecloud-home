# GoreeCloud Home — Features

## Implemented in 0.1.0-dev.3

- **Implemented:** Home/Room/Device domain registry with durable SQLite restoration.
- **Implemented:** one atomic SQLite authority for current state and the durable event journal.
- **Implemented:** schema migrations through version 5, including prior Development database compatibility paths.
- **Implemented:** protocol-neutral Capability Contract v1 and runtime parity validation.
- **Implemented:** desired and reported state separation with persistent optimistic revisions.
- **Implemented:** stale-write conflict detection using explicit expected revisions.
- **Implemented:** Device Availability Contract v1 with persistent transitions/observations.
- **Implemented:** Adapter Lifecycle Contract v1 with persistent registration and lifecycle transitions.
- **Implemented:** devices naming an adapter require a registered adapter record.
- **Implemented:** bounded read-only loopback liveness/readiness/status endpoints.
- **Implemented:** automated domain, migration, persistence, adapter, revision and contract tests.
- **Implemented:** GoreeCloud Platform Contract v0.2 declaration.

## Planned next

- **Planned:** persistent scenes and scene activation.
- **Planned:** declarative automation triggers, conditions and actions.
- **Planned:** schedules, deterministic local execution, execution history, retries and loop prevention.
- **Planned:** Matter/Thread adapter, commissioning and interoperability validation.
- **Planned:** local LAN, MQTT, Zigbee, Z-Wave and BLE adapters.
- **Blocked:** Glaze UI Home client and application acceptance.
- **Blocked:** GoreeCloud Identity, Wardveil Security, Privacy Shield, Everkeep, Manager and Mesh runtime integrations/acceptance.
- **Planned:** remote access, notifications, cameras/media, energy, GoreeCloud Location presence and bounded GoreeCloud AI/voice integration after required security/privacy contracts.
