# GoreeCloud Home Storage and Migration Contract

`0.1.0-dev.3` uses one SQLite database for durable current state, adapter state, and the logical event journal. Domain mutations execute in transactions that include both current-state and event writes.

The `schema_migrations` ledger currently reaches version 5:

1. event journal,
2. durable Home/Room/Device plus desired/reported state,
3. device availability,
4. optimistic desired/reported state revisions,
5. persistent adapter registry/lifecycle.

The original event-only Development database migrates forward without deleting prior events. The `0.1.0-dev.2` pre-registry adapter reference is also migrated into an explicit adapter record using protocol `unknown`, preserving the device relationship without falsely claiming a known protocol.

At startup, Home Core restores adapters, Home/Room/Device data, desired/reported values and revisions, and availability, then re-validates ownership, adapter references, and capability contracts before readiness.

This is Development migration evidence only. Everkeep integration, encrypted-at-rest policy, production backup/restore, downgrade/rollback acceptance, multi-controller replication, and long-term event retention remain incomplete.
