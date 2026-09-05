# GoreeCloud Home — Development User Manual

## Scope

This manual covers the `0.1.0-dev.1` Home Core foundation only. It is not a consumer smart-home setup guide and does not claim hardware compatibility.

## Requirements

- Python 3.12+
- a writable location for the SQLite database

## Start Home Core

```bash
PYTHONPATH=src python -m goreecloud_home --database ./home.db --listen 127.0.0.1:8765
```

The service binds to loopback by default. Do not expose this Development runtime directly to an untrusted network.

## Health endpoints

```bash
curl http://127.0.0.1:8765/livez
curl http://127.0.0.1:8765/readyz
curl http://127.0.0.1:8765/api/v1/status
```

The current HTTP API has no write/device-control endpoints.

## Run tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Current limitations

No Matter/Thread, Zigbee, Z-Wave, MQTT, BLE, physical device control, automation execution, production authentication, remote access, Home client UI or production deployment is implemented yet.