# GoreeCloud Home — Specifications

## Current checkpoint

- Product: GoreeCloud Home
- Version: 0.1.0-dev.4
- Lifecycle: Development
- Platform Contract: 0.2
- Conformance: Nonconformant
- Implementation boundary: local Home Core plus bounded companion automation engine

## Architecture

Home Core owns the local Home/Room/Device domain, protocol-neutral capabilities, desired/reported state, device availability, adapter lifecycle, versioned SQLite state and durable event journal. `HomeAutomationEngine` attaches to the same local SQLite authority/journal and owns scenes, schedules, automation definitions and execution history. Home remains independent of Internet/cloud availability for these local semantics.

## Persistence

The proven Home state-schema ledger remains at version 5. The companion automation engine maintains a separate `automation_schema_migrations` ledger at automation schema version 1 inside the same SQLite database. Automation startup restores and validates scenes, schedules and automations against current Home ownership, devices, capabilities and referenced scenes/schedules before use.

## Automation Contract v1

Machine-readable `contracts/automation.v1.json` defines supported trigger, condition, action and run-status vocabularies plus hard limits. Scenes may contain only desired-state actions. Automations may use manual, reported-state-equals, availability-equals or schedule triggers; desired/reported-state and availability conditions; and `set_desired` or `activate_scene` actions.

A trigger evaluation selects matching enabled automations in stable ID order. Actions execute in definition order. Successful multi-action state mutation and run completion are atomic. On failure, the attempt rolls back desired-state changes and records a failed run separately. One to three whole-run attempts are supported. Conditions that do not match produce a skipped history record.

Schedules persist hour/minute/weekdays and a last-fired occurrence key. Evaluation requires an explicit timezone-aware datetime and suppresses duplicate occurrences durably. No autonomous background clock driver exists yet.

Arbitrary code, shell execution, templates, recursive automation actions and unauthenticated network control are outside Automation Contract v1.

## HTTP API

The Development network API remains read-only: `/livez`, `/readyz`, and `/api/v1/status`. Internal scene/automation methods are not authorization boundaries and are not exposed as network write routes.

## Protocol and platform boundary

Matter/Thread and all other device protocols remain unimplemented/unvalidated. GoreeCloud Identity, Wardveil Security, Privacy Shield, Everkeep, Manager, Mesh and Glaze UI remain applicable but blocked/unaccepted runtime integrations.

## Next milestone work

Complete automatic local event routing into the bounded evaluator plus background schedule driving and additional time/presence semantics, then establish Matter/Thread adapter, commissioning credential, subscription and interoperability boundaries. No hardware interoperability, RC, Stable, production, security/privacy acceptance or recovery acceptance is claimed by this checkpoint.
