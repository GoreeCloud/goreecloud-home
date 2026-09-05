# GoreeCloud Home Storage and Migration Contract

`0.1.0-dev.4` uses one local SQLite database authority with two explicit schema ledgers.

## Home state schema

`schema_migrations` remains at version 5:

1. event journal,
2. durable Home/Room/Device plus desired/reported state,
3. device availability,
4. optimistic desired/reported state revisions,
5. persistent adapter registry/lifecycle.

The original event-only Development database and pre-registry adapter references retain their tested forward migration paths.

## Automation storage schema

`automation_schema_migrations` is independent and currently at version 1. It creates persistent scenes, schedules, automations and automation run history in the same SQLite database. This allows automation persistence to evolve without falsely renumbering or redefining the established Home state-schema contract.

`HomeAutomationEngine` restores definitions on startup and validates Home ownership, device/capability references, scenes and schedules before use. Schedule duplicate-occurrence keys and execution history survive restart.

Home state mutations issued by scenes/automations share the same database transaction and journal. Failed automation action attempts roll back their desired-state mutations before a separate failed run result is recorded.

This remains Development migration evidence only. Everkeep integration, encrypted-at-rest policy, production backup/restore, downgrade/rollback acceptance, multi-controller replication and long-term event/history retention remain incomplete.
