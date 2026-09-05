# GoreeCloud Home — Specifications

## Document status

- Product: GoreeCloud Home
- Short name: Home
- Repository: GoreeCloud/goreecloud-home
- Version: 0.1.0-dev.3
- Lifecycle: Development
- Development model: Original GoreeCloud-controlled software
- Platform Contract: 0.2
- Current implementation claim: durable Home Core, state contracts and adapter-boundary foundation only

## Purpose and architecture

GoreeCloud Home is the native local-first GoreeCloud smart-home platform. Complete third-party smart-home applications may inform interoperability objectives but must not become Home's product-defining architecture, state model, automation model, UI or security boundary.

Home Core is the authoritative local domain service. It owns Home/Room/Device relationships, protocol-neutral capabilities, desired/reported state, device availability, adapter registration/lifecycle, versioned persistence and the local event journal. GoreeCloud Mesh may later exchange cross-product events but is not the authority for local state or future safety-relevant automation.

## Persistence

One SQLite authority commits current state and logical events atomically. Schema version 5 contains the event journal, Home/Room/Device and desired/reported state, device availability, optimistic state revisions, and adapter registration/lifecycle. Startup restores and validates persisted state before readiness.

Development migrations preserve the original event-only journal and promote pre-registry `0.1.0-dev.2` adapter references into explicit adapter records without claiming a known protocol. These are Development migration tests, not production upgrade/rollback acceptance.

## Capability and state contracts

`contracts/capabilities.v1.json` defines the initial versioned GoreeCloud capability set and value/write semantics. Desired state and reported state remain distinct.

`contracts/state-revision.v1.json` defines optimistic revisions for desired and reported capability state. New values start at revision 1. Expected revision 0 requires creation; an exact positive expected revision guards mutation; stale expectations raise `state_revision_conflict` and commit neither state nor event. Internal unconditional writes remain possible when no expected revision is supplied, but this does not authorize unconditional future network writes.

`contracts/device-availability.v1.json` defines device availability independently of adapter lifecycle.

## Adapter boundary

`contracts/adapter-lifecycle.v1.json` defines persistent adapter registration and `registered`, `starting`, `ready`, `degraded`, `failed`, and `stopped` lifecycle semantics. Devices that name an adapter require that adapter to be registered. Registration/lifecycle support is infrastructure only and is not evidence that Matter, Thread or any other protocol is implemented.

## API and security boundary

Current HTTP routes are read-only diagnostics: `GET /livez`, `GET /readyz`, and `GET /api/v1/status`. Network device-control writes remain unimplemented. Future writes require GoreeCloud Identity authorization, Wardveil Security enforcement, Privacy Shield review and explicit capability/revision semantics.

## Integral Platform Systems

Manager, Privacy Shield, Wardveil Security, Everkeep, Glaze UI, GoreeCloud Mesh and GoreeCloud Identity are all applicable and remain blocked/unaccepted runtime integrations at this checkpoint.

## Next major implementation

The next domain milestone is a GoreeCloud-owned persistent scene/automation/schedule model with triggers, conditions, actions, deterministic local execution and execution history. Matter and Thread remain the first protocol priority after the automation and authorization boundaries are sufficiently defined.

## Explicit limitations

No Matter/Thread commissioning or hardware control, Zigbee, Z-Wave, MQTT, BLE, automation execution, production authentication/authorization, remote access, Glaze UI client, platform-system runtime acceptance, backup/restore acceptance, packaging, signing, hardware acceptance, RC, Stable or production qualification is claimed.
