# GoreeCloud Home — Specifications

## Document status

- Product: GoreeCloud Home
- Short name: Home
- Repository: GoreeCloud/goreecloud-home
- Version: 0.1.0-dev.1
- Lifecycle: Development
- Development model: Original GoreeCloud-controlled software
- Platform Contract: 0.2
- Current implementation claim: Home Core foundation only

## 1. Purpose

GoreeCloud Home is the native GoreeCloud smart-home platform. Its goal is to combine approachable household control with deep automation and broad interoperability while preserving local operation, privacy, portability, recoverability and GoreeCloud platform integration.

Home must not be a maintained fork, white-label deployment or architectural reskin of Home Assistant, Google Home, Apple Home/HomeKit, or another complete smart-home product. Standards-compatible foundational protocol libraries may be used when justified, but GoreeCloud owns and controls the application-defining state model, automation model, user experience, APIs, security boundaries and lifecycle.

## 2. Product identity

- Canonical name: GoreeCloud Home
- Approved short runtime label: Home
- Brand relationship: prefixed GoreeCloud family product
- GoreeCloud Suite member: yes
- Repository: GoreeCloud/goreecloud-home
- Package/application suffix: home
- Intended application identifier: com.goreecloud.home

## 3. Architecture

Home is split into replaceable layers:

1. **Home Core** — authoritative local household domain state and coordination.
2. **Capability model** — protocol-neutral device capabilities.
3. **Desired/reported state model** — separates intended state from observed device state.
4. **Event journal** — durable local chronology required for offline operation, auditability and recovery.
5. **Automation engine** — planned trigger/condition/action execution with scenes and schedules.
6. **Protocol adapters** — planned Matter/Thread, Zigbee, Z-Wave, MQTT, BLE and LAN integrations.
7. **Client surfaces** — planned Glaze UI web, Android, Linux, wall-display and quick-control experiences.
8. **Platform adapters** — Manager, Privacy Shield, Wardveil Security, Everkeep, Glaze UI, Mesh and Identity.

Home Core must not require GoreeCloud Mesh to execute local automations or preserve safety-relevant local state.

## 4. Domain model

### Home

Represents one household authority boundary. A Home owns rooms and registered devices.

### Room

A user-facing placement inside one Home. Future floors and zones can group rooms without changing device ownership.

### Device

Represents a physical or virtual controllable/observable device. Each device declares a set of GoreeCloud capability identifiers.

### Capability

Protocol-neutral functional contract such as:

- `light.power`
- `light.brightness`
- `light.color`
- `light.color_temperature`
- `switch.power`
- `lock.state`
- `cover.position`
- `thermostat.mode`
- `thermostat.target_temperature`
- `sensor.temperature`
- `sensor.humidity`
- `sensor.motion`
- `sensor.contact`
- `camera.stream`
- `camera.snapshot`
- `media.playback`
- `media.volume`

Adapters translate native protocol properties into this model. Protocol-specific details that cannot be represented losslessly may be retained as adapter metadata without redefining the Home Core domain.

## 5. State model

Home maintains two distinct state classes:

- **Desired state:** what an authorized actor wants a capability to become.
- **Reported state:** what the device or adapter actually reports.

The distinction is required so Home can represent pending commands, offline devices, failed transitions, retries and conflicts without falsely reporting intent as device reality.

## 6. Event model

Material Home Core transitions append immutable logical events to a local journal. Initial events include home creation, room creation, device registration, desired-state changes and reported-state changes.

The Development journal uses SQLite and monotonically increasing sequence IDs. Future schema evolution must preserve migration and recovery paths.

## 7. Automation model — planned

The automation engine will use a GoreeCloud-owned declarative model with:

- triggers
- conditions
- actions
- scenes
- schedules
- sunrise/sunset conditions
- presence/geofence conditions through GoreeCloud Location when applicable
- rate limiting and loop prevention
- explicit authorization context
- deterministic local execution where supported
- execution history and failure reason

A future visual editor and text/YAML representation must map to the same underlying semantic model rather than becoming separate automation systems.

## 8. Protocol strategy

Planned priority:

1. Matter and Thread
2. local Wi-Fi/LAN discovery and control
3. MQTT
4. Zigbee
5. Z-Wave
6. BLE and Bluetooth proxying
7. bounded vendor adapters where necessary

Protocol libraries are foundational dependencies and must remain isolated behind GoreeCloud adapter contracts. Home must not expose protocol internals as the permanent product data model.

## 9. Hub and node model — planned

A Home should have one authoritative Home Controller at a time. Additional Home Nodes may provide radios, Thread Border Router functions, BLE proxying or other edge connectivity. Controller authority and failover must prevent split-brain state.

Supported deployment targets are planned to include dedicated hub hardware, Linux server/container/VM deployment, and development workstation operation.

## 10. API

Current Development HTTP API is loopback-oriented and read-only:

- `GET /livez`
- `GET /readyz`
- `GET /api/v1/status`

No unauthenticated device-control endpoint is part of the current public runtime surface. Future write/control APIs require GoreeCloud Identity authorization, Wardveil Security controls, Privacy Shield review and explicit capability scopes.

## 11. Integral Platform Systems

All seven systems are applicable:

- GoreeCloud Manager — health, inventory and operations visibility.
- Privacy Shield — household telemetry, camera/presence/history retention and data governance.
- Wardveil Security — device trust, privileged control, secrets, network risk and audit.
- Everkeep — configuration, automation, history-policy-aware backup, restore and export.
- Glaze UI — accessible responsive Home client experiences.
- GoreeCloud Mesh — discovery, non-safety-critical cross-product events and capability exchange.
- GoreeCloud Identity — household authentication, users, guests, sessions, roles and authorization.

At version 0.1.0-dev.1 these integrations are requirements, not implemented/accepted integrations.

## 12. Security boundaries

Locks, garage doors, alarms, cameras, access credentials and equivalent capabilities are high-risk. Future control requires explicit authorization context and elevated safeguards. Reusable protocol credentials and cryptographic material must never be committed to Git or exposed in ordinary status output.

The Development HTTP server binds to loopback by default and exposes no write/control API.

## 13. Privacy

Local-only operation must remain a valid configuration. Cloud use must be additive rather than required for core local control. Presence, camera, audio, behavioral and household-history data require explicit retention and sharing controls.

No advertising, third-party behavioral analytics or mandatory telemetry is part of the product design.

## 14. Continuity and portability

Home requires backup, restore, export and migration support for applicable configuration, rooms, devices, capability mappings, automations, scenes and user-owned state/history according to privacy policy. Recovery qualification must test restore behavior rather than merely create backups.

## 15. Current implementation

Version 0.1.0-dev.1 implements:

- validated domain identifiers and dataclasses for Home, Room and Device
- a thread-safe in-process Home Core registry
- protocol-neutral device capability identifiers
- desired and reported state maps
- durable SQLite event journal
- read-only loopback status/liveness/readiness HTTP server
- unit tests for domain invariants, state changes and event persistence
- Platform Contract v0.2 declaration
- CI foundation

## 16. Explicitly not implemented yet

Matter/Thread commissioning and fabrics; Zigbee; Z-Wave; MQTT; BLE; physical device drivers; production API authentication; household Identity integration; authorization roles; automation execution; scenes; remote access; notifications; cameras/media pipelines; energy management; GoreeCloud Location presence; GoreeCloud AI/voice; Glaze UI clients; Manager/Privacy Shield/Wardveil/Everkeep/Mesh runtime integration; backup/restore execution; packaging; deployment; signing; production acceptance; RC or Stable qualification.

## 17. Acceptance direction

Future milestones must validate exact revisions with unit/integration tests, protocol interoperability fixtures or real hardware where relevant, offline behavior, restoration, authorization, privileged action controls, privacy retention, accessibility, upgrade/rollback and release provenance.

Passing foundation tests does not qualify Home for production use.