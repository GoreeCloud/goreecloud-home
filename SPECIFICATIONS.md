# GoreeCloud Home — Specifications

## Document status

- Product: GoreeCloud Home
- Short name: Home
- Repository: GoreeCloud/goreecloud-home
- Version: 0.1.0-dev.2
- Lifecycle: Development
- Development model: Original GoreeCloud-controlled software
- Platform Contract: 0.2
- Current implementation claim: Home Core persistence and state-contract foundation only

## 1. Purpose and product boundary

GoreeCloud Home is the native GoreeCloud smart-home platform. It is intended to combine approachable household control with deep local automation and broad interoperability while preserving privacy, portability, recoverability, offline operation and substantive GoreeCloud platform integration.

Home must not become a maintained fork, white-label deployment or architectural reskin of Home Assistant, Google Home, Apple Home/HomeKit, or another complete smart-home application. Standards-compatible foundational protocol libraries may be used when justified, but GoreeCloud owns the application-defining state model, automation model, APIs, user experience, security boundaries and lifecycle.

## 2. Product identity

Canonical name: **GoreeCloud Home**. Approved short runtime label: **Home**. Repository: `GoreeCloud/goreecloud-home`. Package/application suffix: `home`. Intended application identifier: `com.goreecloud.home`.

## 3. Local architecture

Home Core is the authoritative local domain service inside one Home Controller. Its current layers are a Home/Room/Device domain registry, versioned capability contracts, desired/reported state, device availability, a durable SQLite current-state projection and a durable event journal. The current-state projection and event journal share one SQLite transaction authority.

Home Core must not require GoreeCloud Mesh to preserve local state or, later, execute safety-relevant local automation.

## 4. Durable storage and migration

The Development database maintains `schema_migrations` and currently reaches schema version 3:

1. event journal,
2. durable Home/Room/Device and desired/reported capability state,
3. persistent device availability.

A domain state mutation and its logical event commit atomically. If journaling fails, the state change is rolled back; an event cannot remain committed without its associated state mutation. Home Core reconstructs its in-process registry from durable state at startup and re-validates ownership boundaries and capability/state contracts before readiness.

The migration path from the original `0.1.0-dev.1` event-only Development database preserves existing events and is covered by automated tests. This does not constitute production upgrade, downgrade, backup, restore or rollback acceptance.

## 5. Capability contract v1

`contracts/capabilities.v1.json` is the machine-readable initial capability contract. Runtime definitions and the committed contract must match exactly in tests. Each capability may define value kind, writable/read-only direction, numeric bounds, unit, reported enumeration and a narrower desired enumeration.

Initial definitions include `light.power`, `light.brightness`, `switch.power`, `lock.state`, `cover.position`, `thermostat.target_temperature`, `sensor.temperature`, `sensor.humidity`, `sensor.motion`, and `sensor.contact`. A protocol adapter may not introduce arbitrary unregistered capability names and thereby redefine the Home model implicitly.

Desired state is validated separately from reported state. Read-only sensors reject desired writes. Diagnostic reported values that are not valid commands remain reportable; for example, a lock may report `jammed` while desired lock state is limited to `locked` or `unlocked`.

## 6. Device availability contract v1

`contracts/device-availability.v1.json` defines `unknown`, `online`, `degraded`, and `offline` with explicit legal transitions. `unknown` is initial-only once a device reaches a known state. Same-state updates are recorded as observations rather than transitions. Availability timestamps and optional bounded reasons are persisted.

## 7. Event model

Material Home Core transitions append immutable logical events with monotonically increasing sequence identifiers. Current event families include Home creation, Room creation, device registration, desired/report state changes, availability transitions and same-state availability observations.

## 8. API boundary

Current Development HTTP routes are `GET /livez`, `GET /readyz`, and `GET /api/v1/status`. The status surface exposes only bounded product/lifecycle data, aggregate counts, aggregate availability, storage schema version and capability-contract version. It does not expose household state, event payloads, credentials or identities.

No network write/control API is implemented. Future control requires GoreeCloud Identity authorization, Wardveil Security controls, Privacy Shield review and explicit capability scopes.

## 9. Automation and protocol direction

The next core milestones are versioned adapter lifecycle/registration plus state revision/conflict semantics, followed by a GoreeCloud-owned declarative automation model for scenes, triggers, conditions, actions, schedules and execution history. Matter and Thread remain the first protocol-adapter priority, followed by local LAN, MQTT, Zigbee, Z-Wave, BLE and bounded vendor adapters.

Protocol implementations must translate into versioned GoreeCloud capability/availability contracts and may not become the canonical product state model.

## 10. Integral Platform Systems

GoreeCloud Manager, Privacy Shield, Wardveil Security, Everkeep, Glaze UI, GoreeCloud Mesh and GoreeCloud Identity are all applicable and all remain blocked/unaccepted runtime integrations at `0.1.0-dev.2`. The current persistence work is not Everkeep recovery acceptance, and the read-only status API is not Manager integration acceptance.

## 11. Security, privacy and continuity

Locks, doors, alarms, cameras, access credentials and comparable capabilities are high-risk and require stronger authorization and audit controls before network control is exposed. Reusable protocol secrets and cryptographic material must remain out of ordinary source history and status output. Local-only operation remains a valid target; cloud functionality must be additive. Home requires future tested backup, restore, export and migration for applicable user-owned configuration/state while respecting Privacy Shield policy.

## 12. Implemented state

`0.1.0-dev.2` implements validated Home/Room/Device models, shared SQLite current-state/journal authority, three migrations, restart restoration, atomic state/event transactions, capability contract v1, availability contract v1, desired/reported validation, read-only diagnostics, and automated domain/persistence/migration/contract tests.

## 13. Explicitly not implemented

Matter/Thread commissioning/fabrics, Zigbee, Z-Wave, MQTT, BLE, physical device drivers, adapter lifecycle/registration, state revision/conflict handling, automation execution, scenes, schedules, production authentication/authorization, remote access, notifications, camera/media pipelines, energy management, GoreeCloud Location presence, GoreeCloud AI/voice, Glaze UI clients, substantive Integral Platform System runtime integrations, backup/restore execution, packaging, signing, deployment, hardware acceptance, RC, Stable and production qualification remain incomplete.

Passing Development tests or Platform Contract validation does not qualify Home for production use.
