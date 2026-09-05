# GoreeCloud Home State Contracts

## Capability contract v1

`contracts/capabilities.v1.json` defines the first Home capability contract. Tests require semantic parity with runtime definitions. Definitions may specify name/version, value kind, writable/read-only direction, numeric bounds, unit, reported enumerations and narrower desired enumerations.

A protocol adapter may not introduce an unregistered capability string and thereby redefine Home semantics implicitly. For example, `lock.state` may report `jammed`, but desired values are limited to `locked` and `unlocked`.

## Availability contract v1

`contracts/device-availability.v1.json` defines `unknown`, `online`, `degraded`, and `offline`, plus legal transitions. `unknown` is initial-only after a known state is reached. Same-state observations update timestamp/reason and are journaled as observations rather than transitions.

## Next contract work

Adapter lifecycle/registration, command acknowledgement, state revision/conflict handling and automation execution semantics will be versioned separately.
