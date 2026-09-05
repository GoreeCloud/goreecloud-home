# GoreeCloud Home — Features

## Implemented in 0.1.0-dev.4

- Durable Home/Room/Device state, desired/reported revisions, availability, adapters and event journal in the versioned Home state store.
- Home state schema remains version 5; the companion automation engine uses automation storage schema version 1 in the same SQLite authority.
- Capability, availability, state-revision, adapter-lifecycle and automation v1 contracts.
- Persistent scenes with ordered validated desired-state actions and atomic activation.
- Persistent declarative automations with manual, reported-state, availability and schedule triggers.
- Desired/reported-state and availability conditions.
- `set_desired` and `activate_scene` actions only; arbitrary code/scripts/templates are excluded.
- Persistent schedules with weekdays, hour/minute, timezone-aware caller evaluation and durable duplicate-occurrence suppression.
- Deterministic trigger matching and definition-order action execution.
- Persistent run history with running/succeeded/failed/skipped states.
- Atomic rollback on failed multi-action attempts and bounded whole-run retries (maximum 3).
- Hard limits for conditions/actions/runs per trigger to reduce accidental loops or runaway execution.
- Read-only loopback liveness/readiness/status HTTP API.
- Platform Contract v0.2 declaration and automated validation.

## Still planned or blocked

- Automatic adapter/event routing into the automation evaluator.
- Background schedule clock driver, sunrise/sunset and calendar triggers.
- Presence/geofence triggers through GoreeCloud Location.
- Matter/Thread, LAN, MQTT, Zigbee, Z-Wave and BLE protocol adapters.
- Glaze UI Home client and visual automation editor.
- GoreeCloud Identity, Wardveil Security, Privacy Shield, Everkeep, Manager and Mesh runtime integration/acceptance.
- Secure remote access, notifications, cameras/media, energy, AI/voice, hardware acceptance, RC, Stable and production qualification.
