# GoreeCloud Home — Development User Manual

This manual covers `0.1.0-dev.4` Development Home Core and its companion automation engine only.

## Start

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

The service binds to loopback by default. The Home state database remains at Development schema version 5. Initializing `HomeAutomationEngine` creates or validates automation storage schema version 1 in the same SQLite database without redefining the Home state-schema ledger.

## Diagnostics

```bash
curl http://127.0.0.1:8765/livez
curl http://127.0.0.1:8765/readyz
curl http://127.0.0.1:8765/api/v1/status
```

Status exposes bounded aggregate counts and contract/schema versions, not household state values, automation definitions, execution payloads, credentials or identities. There are no HTTP write/control endpoints.

## Automation development API

Trusted local Python callers may create Scene, Schedule and Automation definitions through `HomeAutomationEngine` and invoke scene activation, manual automation execution, trigger evaluation or schedule evaluation. Schedule evaluation requires an explicit timezone-aware datetime. Automatic adapter-event routing and a background clock driver are not implemented yet.

Execution history is durable and records succeeded, failed and skipped runs. Failed action attempts roll back desired-state mutations before failure history is written. Bounded whole-run retry attempts are supported.

## Tests

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

No Matter/Thread, Zigbee, Z-Wave, MQTT, BLE, physical-device control, production authentication, remote access or consumer Home UI is implemented yet.
