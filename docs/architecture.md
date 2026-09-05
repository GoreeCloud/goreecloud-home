# GoreeCloud Home Architecture

Home Core is the authoritative smart-home domain service inside one controller. Internet connectivity and GoreeCloud cloud services are not prerequisites for local state or future local automation execution.

`0.1.0-dev.2` uses one SQLite authority for a durable current-state projection and event journal. Each domain mutation and logical event commit in one transaction. Schema migration version 3 covers the event journal, Home/Room/Device plus desired/reported state, and device availability. Startup restores and validates persisted state before readiness.

Adapters translate external protocol state into versioned GoreeCloud capabilities and availability. Home Core does not use a Matter cluster, Zigbee attribute, Z-Wave command class, MQTT topic or vendor schema as its canonical model.

Desired state remains distinct from reported state, and device connectivity uses an explicit availability state machine. The local journal remains independent of GoreeCloud Mesh. Future Home Nodes may provide radios/Thread Border Router/BLE proxy functions while one controller retains household authority.

The next architecture work is adapter lifecycle/registration and state revision/conflict semantics before any network control API is exposed.
