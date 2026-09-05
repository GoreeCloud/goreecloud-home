# GoreeCloud Home

GoreeCloud Home is an original, local-first GoreeCloud smart-home platform for household control, automation and standards-based device interoperability.

## Status

**Lifecycle:** Development  
**Version:** `0.1.0-dev.4`  
**Conformance:** Nonconformant  
**Repository:** `GoreeCloud/goreecloud-home`

Home Core now provides durable device/state foundations plus the first persistent declarative scene, automation, schedule and execution-history engine. It still exposes only bounded read-only diagnostic HTTP routes and does not yet control physical smart-home protocols.

## Current contracts

- Capability Contract v1
- Device Availability Contract v1
- State Revision Contract v1
- Adapter Lifecycle Contract v1
- Automation Contract v1

## Automation foundation

Scenes use ordered validated desired-state writes. Automations can use manual, reported-state, availability or schedule triggers, optional state/availability conditions, and `set_desired` / `activate_scene` actions. Definitions and execution history survive restart.

Execution is deterministic and bounded: 32 actions maximum, 16 conditions maximum, 32 automation matches per trigger, and at most three whole-run attempts. Successful action sets commit atomically; failed attempts roll back desired-state changes and are recorded in history. Arbitrary code, shell, templates and automation-to-automation actions are not supported.

Schedules are evaluated against a caller-supplied timezone-aware datetime and suppress duplicate occurrences durably. A background clock service and automatic protocol-event routing are not implemented yet.

## Run Development Home Core

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

Available routes: `GET /livez`, `GET /readyz`, `GET /api/v1/status`. The HTTP surface is intentionally read-only.

## Tests

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Next development

Complete Milestone 2 event/clock integration and additional deterministic trigger semantics, then begin Matter/Thread adapter boundaries, commissioning credential handling and interoperability fixtures. Glaze UI and substantive GoreeCloud platform integrations follow as evidence-backed workstreams.
