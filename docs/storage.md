# GoreeCloud Home Storage and Migration Contract

`0.1.0-dev.2` uses one SQLite database for durable current state and the logical event journal. Domain mutations execute in a transaction that includes both the state write and the event append, preventing either representation from committing alone.

The `schema_migrations` ledger currently reaches version 3: event journal; durable Home/Room/Device plus desired/reported state; and device availability. Readiness requires the expected schema version.

The original `0.1.0-dev.1` event-only database is migrated in place without deleting its existing events; automated tests cover this Development path.

At startup, Home Core restores Home/Room/Device data, desired/reported state and availability, then re-validates ownership and capability contracts. Invalid persisted state fails startup rather than being silently reinterpreted.

This is not production backup/restore acceptance. Encrypted-at-rest policy, Everkeep integration, downgrade handling, isolated restore validation, multi-controller replication, event retention/compaction and production rollback remain incomplete.
