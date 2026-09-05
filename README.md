# GoreeCloud Home

GoreeCloud Home is an original, local-first GoreeCloud smart-home platform for private household control, automation, device interoperability, scenes, presence-aware behavior, and future secure remote access.

## Status

**Lifecycle:** Development  
**Version:** `0.1.0-dev.1`  
**Conformance:** Nonconformant / foundation in progress  
**Repository:** `GoreeCloud/goreecloud-home`

This repository currently implements the first Home Core foundation: a domain registry for homes, rooms, devices and capabilities; desired/reported state tracking; a durable SQLite event journal; and a loopback-only read-only status server. It does **not** yet implement Matter, Thread, Zigbee, Z-Wave, MQTT, BLE, production authentication, remote access, a Glaze UI client, or hardware control.

## Product identity

- Canonical product name: **GoreeCloud Home**
- Installed/launcher short name: **Home**
- Brand relationship: prefixed GoreeCloud family product
- Intended package/application suffix: `home`
- Intended canonical application identifier: `com.goreecloud.home`
- Development model: original GoreeCloud-controlled software

## Design principles

- **Local first:** core automations and device state must not require Internet or GoreeCloud cloud availability.
- **Protocol neutral:** GoreeCloud capabilities are the application model; Matter, Zigbee, Z-Wave, MQTT, BLE and vendor adapters translate at the boundary.
- **Desired vs reported state:** Home distinguishes user/system intent from device-observed reality.
- **Durable events:** important state transitions are journaled independently of GoreeCloud Mesh so offline operation remains valid.
- **Least privilege:** no unauthenticated network device-control API is exposed by the Development foundation.
- **Portable:** configuration, automations and supported user-owned data must remain exportable and recoverable.

## Current foundation

```text
Home clients (planned)
        |
   Home Core API
        |
+-------+--------------------+
|                            |
Domain Registry        Event Journal
|                            |
Home / Room / Device   durable SQLite events
|                            |
Capabilities           desired/reported state
        |
Protocol adapters (planned)
Matter/Thread | Zigbee | Z-Wave | MQTT | BLE | LAN
```

## Run the Development core

Requires Python 3.12+ and uses only the Python standard library at this stage.

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

Available Development endpoints:

- `GET /livez`
- `GET /readyz`
- `GET /api/v1/status`

The HTTP surface is intentionally read-only. Device registration and desired-state changes currently exist only as internal Home Core methods until GoreeCloud Identity, Wardveil Security and authorization boundaries are implemented.

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Repository documentation

- `SPECIFICATIONS.md` — version-coupled product and architecture specification
- `FEATURES.md` — implemented/planned capability inventory
- `BENEFITS.md` — supportable product value
- `COMPETITIVE-OBJECTIVES.md` — differentiation objectives
- `BRANDING.md` — canonical identity and presentation rules
- `USER-MANUAL.md` — Development usage guidance
- `docs/architecture.md` — architecture and protocol-boundary notes
- `docs/platform-integration-status.md` — seven Integral Platform Systems evaluation
- `docs/security.md` — security boundaries
- `docs/privacy.md` — privacy model
- `docs/recovery.md` — backup/restore/export requirements
- `docs/api.md` — current API surface

## Release boundary

A source commit, passing test run, merged pull request, or Platform Contract validation does not establish RC, Stable, production, security, privacy, recoverability, interoperability, or hardware acceptance. Those claims require separate evidence.