# GoreeCloud Home Architecture

Home Core is the authoritative smart-home domain service inside one controller. Internet connectivity and GoreeCloud cloud services are not prerequisites for local state or future local automation execution.

The Home state subsystem uses one SQLite authority at state schema version 5 for Home/Room/Device state, adapter lifecycle, availability, desired/reported revisions and the durable event journal.

`HomeAutomationEngine` is a bounded companion inside the same local Home process/domain boundary. It shares Home Core's SQLite connection and journal but evolves through a separate automation schema ledger, currently version 1. It owns scenes, schedules, automation definitions and run history without redefining the Home state-schema contract.

Desired and reported state use separate optimistic revisions. Automation actions target desired state only and continue to respect the existing capability validation boundary.

Automation Contract v1 excludes arbitrary scripts/templates and recursive automation-to-automation actions. Matching and action execution are deterministic and bounded. Successful action sets commit atomically; failed attempts roll back their desired-state changes before failure history is recorded.

Protocol adapters remain explicit registered entities. Future Matter/Thread and other adapters will translate protocol state into the existing capability/availability/revision contracts and may later feed trusted events into the automation evaluator. No protocol adapter currently implements physical device interoperability.
