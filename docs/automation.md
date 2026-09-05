# GoreeCloud Home Automation Contract v1

`0.1.0-dev.4` introduces a bounded GoreeCloud-owned automation foundation. It does not execute arbitrary source code, shell commands, templates, or third-party scripting languages.

## Persistence boundary

`HomeAutomationEngine` shares Home Core's SQLite authority and durable event journal but maintains a separate `automation_schema_migrations` ledger. Home state schema remains version 5; automation storage begins at version 1. Scenes, schedules, automations and execution history are restored and re-validated against current Home ownership, devices, capabilities, scenes and schedules.

## Definitions

Scenes contain ordered `set_desired` actions only. Automations contain one declarative trigger, up to 16 conditions, and up to 32 ordered actions. Automation actions are limited to `set_desired` and `activate_scene`.

Automation Contract v1 supports manual, reported-state-equals, availability-equals and schedule triggers. Conditions support desired-state-equals, reported-state-equals and availability-equals.

## Determinism and scheduling

`evaluate_trigger` runs matching enabled automations in stable automation-ID order. Actions execute in definition order. Adapter/event routing into this evaluator is not yet automatic.

Schedules define hour, minute, weekdays, enabled state and a durable last-fired occurrence key. Evaluation requires a caller-supplied timezone-aware datetime, so behavior does not silently depend on host timezone. Duplicate occurrences are suppressed durably across restart. No background clock driver is implemented yet.

## Atomic execution and history

Runs record `running`, `succeeded`, `failed` or `skipped`. Successful action mutations and the successful run result commit atomically. If a later action fails, desired-state changes from that attempt are rolled back before the failed run is recorded separately. Automations may request one to three whole-run attempts.

A trigger evaluation may match at most 32 automations. Scenes and automations cannot invoke arbitrary automations, preventing recursive action graphs in this contract version.

These are trusted local Home Core semantics, not network authorization. The Development HTTP API remains read-only.
