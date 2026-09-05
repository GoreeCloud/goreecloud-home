# GoreeCloud Home — Development User Manual

## Scope

This manual covers the `0.1.0-dev.3` Home Core Development checkpoint only. It is not a consumer smart-home setup guide and does not claim hardware compatibility.

## Requirements

- Python 3.12+
- a writable location for the SQLite database

## Start Home Core

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

The service binds to loopback by default. Do not expose this Development runtime directly to an untrusted network.

The database is migrated automatically to the current Development schema. The original event-only Development database layout is upgraded in place without deleting existing events. Back up Development data before experimenting with future schema changes; production-grade upgrade/rollback is not yet accepted.

## Health endpoints

```bash
curl http://127.0.0.1:8765/livez
curl http://127.0.0.1:8765/readyz
curl http://127.0.0.1:8765/api/v1/status
```

The status response includes bounded aggregate counts plus the storage schema version, capability-contract version, state-revision contract version, adapter-lifecycle contract version, and bounded adapter/availability counts. It does not expose device names, room names, desired/reported values, household identities, event payloads, or credentials.

The current HTTP API has no write/device-control endpoints.

## Contracts

- `contracts/capabilities.v1.json` — initial capability value and write-direction contract.
- `contracts/device-availability.v1.json` — device availability states and legal transitions.
- `contracts/state-revision.v1.json` — optimistic desired/reported revision and stale-write conflict semantics.
- `contracts/adapter-lifecycle.v1.json` — adapter registration and lifecycle transitions.

These are Development contracts. Incompatible changes require a new contract version rather than silently redefining existing semantics.

## Run tests

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Current limitations

No Matter/Thread, Zigbee, Z-Wave, MQTT, BLE, physical device control, automation execution, production authentication, remote access, Home client UI or production deployment is implemented yet.
