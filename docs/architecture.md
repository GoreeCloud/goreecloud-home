# GoreeCloud Home Architecture

Home Core is the authoritative smart-home domain service inside one controller. Internet connectivity and GoreeCloud cloud services are not prerequisites for local state or future local automation execution.

`0.1.0-dev.3` uses one SQLite authority for durable current state, adapter lifecycle and the event journal. Schema version 5 covers the original journal, Home/Room/Device and desired/reported state, availability, optimistic state revisions, and adapter registration/lifecycle.

Adapters are explicit registered entities. A device cannot name an adapter that Home Core does not know. Adapter lifecycle is independent of device availability: an adapter can be degraded while individual devices have their own online/degraded/offline observations.

Desired and reported state use separate monotonically increasing revisions. Optional expected-revision checks give future adapter/client writers deterministic stale-write rejection without conflating desired intent with reported device truth.

Adapters translate protocol state into versioned GoreeCloud capability, availability, and revision semantics. Matter clusters, Zigbee attributes, Z-Wave command classes, MQTT topics, or vendor schemas do not become the canonical Home model.

The next major domain work is persistent declarative scenes, automations, schedules, and execution history before Matter/Thread control is introduced.
