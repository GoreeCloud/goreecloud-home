# GoreeCloud Home

GoreeCloud Home is an original, local-first GoreeCloud smart-home platform for private household control, automation and standards-based device interoperability.

## Status

**Lifecycle:** Development  
**Version:** `0.1.0-dev.3`  
**Conformance:** Nonconformant  
**Repository:** `GoreeCloud/goreecloud-home`

The current Home Core persists Home/Room/Device state, desired/reported values and revisions, device availability, adapter registration/lifecycle, and a durable event journal in one versioned SQLite authority. It exposes only bounded read-only diagnostic HTTP routes.

It does **not** yet implement Matter/Thread commissioning or control, Zigbee, Z-Wave, MQTT, BLE, automation execution, production authentication/authorization, remote access, or a Glaze UI Home client.

## Core contracts

- `contracts/capabilities.v1.json` — protocol-neutral capability types, write direction, ranges, units and enumerations.
- `contracts/device-availability.v1.json` — device availability states and transitions.
- `contracts/state-revision.v1.json` — optimistic desired/reported state revisions and stale-write conflict behavior.
- `contracts/adapter-lifecycle.v1.json` — adapter registration and lifecycle state machine.

Runtime definitions and machine-readable contract files are checked for exact parity in tests.

## Durable authority

The migration ledger is currently schema version 5: event journal; durable Home/Room/Device and desired/reported state; device availability; state revisions; adapter registry/lifecycle. A state mutation and its logical event commit in the same SQLite transaction. Restart restoration re-validates domain, capability and adapter relationships before readiness.

## Run the Development core

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

Available routes are `GET /livez`, `GET /readyz`, and `GET /api/v1/status`. `POST` is rejected; no network control API is exposed.

## Tests

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

The suite covers domain boundaries, capability semantics, availability, adapter lifecycle, persistence/migration, restart restoration, atomic rollback, optimistic state conflicts, and contract parity.

## Next development

The next major implementation is a persistent GoreeCloud-owned scene/automation/schedule model with deterministic execution history. Matter and Thread remain the first protocol-adapter priority after that core model and authorization boundaries are defined.

## Platform boundary

GoreeCloud Manager, Privacy Shield, Wardveil Security, Everkeep, Glaze UI, GoreeCloud Mesh and GoreeCloud Identity are applicable but remain blocked/unaccepted runtime integrations. Passing Development tests or Platform Contract validation does not establish conformance, RC, Stable, hardware interoperability, recovery acceptance, or production readiness.
