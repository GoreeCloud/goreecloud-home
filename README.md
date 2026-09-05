# GoreeCloud Home

GoreeCloud Home is an original, local-first GoreeCloud smart-home platform for private household control, automation, device interoperability, scenes, presence-aware behavior, and future secure remote access.

## Status

**Lifecycle:** Development  
**Version:** `0.1.0-dev.2`  
**Conformance:** Nonconformant / foundation in progress  
**Repository:** `GoreeCloud/goreecloud-home`

The current source implements the second Home Core Development checkpoint. Home/Room/Device state is persisted in the same local SQLite authority as the durable event journal, schema migrations are versioned, capability values are validated against a machine-readable v1 contract, and devices have a persistent availability state-transition model. The network surface remains deliberately read-only.

It does **not** yet implement Matter, Thread, Zigbee, Z-Wave, MQTT, BLE, physical device control, production authentication, remote access, automation execution, or a Glaze UI Home client.

## Product identity

- Canonical product name: **GoreeCloud Home**
- Installed/launcher short name: **Home**
- Brand relationship: prefixed GoreeCloud family product
- Intended package/application suffix: `home`
- Intended canonical application identifier: `com.goreecloud.home`
- Development model: original GoreeCloud-controlled software

## Design principles

- **Local first:** core state and future local automations must not require Internet or GoreeCloud cloud availability.
- **Protocol neutral:** versioned GoreeCloud capabilities are the application model; protocol adapters translate at the boundary.
- **Desired vs reported state:** Home distinguishes requested state from device-observed reality.
- **Durable authority:** domain state and its event journal share one SQLite transaction boundary.
- **Explicit availability:** device connectivity/health uses a versioned transition contract instead of ad-hoc booleans.
- **Least privilege:** no unauthenticated network device-control API is exposed by the Development foundation.
- **Portable:** configuration, automations and supported user-owned data must remain exportable and recoverable.

## Durable state

`0.1.0-dev.2` adds a migration ledger and durable Home, Room, Device, desired-state, reported-state, and availability tables. Home Core commits a domain mutation and its logical event in the same SQLite transaction. On restart, it reconstructs its in-process domain from the durable state projection and validates that restored state against current contracts.

Current schema migrations are:

1. event journal,
2. durable Home/Room/Device plus desired/reported state,
3. device availability.

The original `0.1.0-dev.1` event-only Development database is migrated without deleting existing events; this path is covered by tests.

## Capability contract v1

`contracts/capabilities.v1.json` defines the initial protocol-neutral capability semantics and is tested for exact parity with runtime definitions. It currently includes lighting, switching, lock, cover, thermostat, temperature, humidity, motion, and contact capabilities. The contract defines type, write direction, ranges, units, and enumerated values where applicable.

## Device availability contract v1

`contracts/device-availability.v1.json` defines `unknown`, `online`, `degraded`, and `offline` plus legal transitions. `unknown` is initial-only after a device reaches a known state. Repeated observations of the same state are journaled separately from actual transitions.

## Run the Development core

Requires Python 3.12+ and currently uses only the Python standard library.

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

Available Development endpoints:

- `GET /livez`
- `GET /readyz`
- `GET /api/v1/status`

The HTTP surface remains read-only. Device registration and state/availability mutations are internal Home Core methods, not authenticated network APIs.

## Tests

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

The suite covers domain invariants, desired/reported truth, capability validation, read-only capability rejection, availability transitions, event persistence, schema migration, restart restoration, machine-readable contract parity, and atomic rollback when journaling fails.

## Protocol roadmap

1. Matter and Thread
2. local Wi-Fi/LAN discovery/control
3. MQTT
4. Zigbee
5. Z-Wave
6. BLE/proxy nodes
7. bounded vendor adapters when open/local standards are insufficient

## Platform integration status

GoreeCloud Manager, Privacy Shield, Wardveil Security, Everkeep, Glaze UI, GoreeCloud Mesh and GoreeCloud Identity are all applicable and all remain **blocked/unaccepted** at this checkpoint.

## Release boundary

This is Development source. Passing tests and Platform Contract validation do not establish hardware interoperability, security/privacy acceptance, recovery acceptance, RC, Stable, deployment, or production readiness.
