# Home Platform Integration Status

Version: 0.1.0-dev.1

| Platform system | Applicability | Current status | Foundation evidence | Required next work |
| --- | --- | --- | --- | --- |
| GoreeCloud Manager | Applicable | Blocked | `/livez`, `/readyz`, bounded status endpoint | registration, health contract consumption, acceptance |
| Privacy Shield | Applicable | Blocked | local-first privacy requirements documented | retention/sharing policy enforcement and acceptance |
| Wardveil Security | Applicable | Blocked | loopback default; no HTTP control API | device trust, privileged-action controls, secret boundary, acceptance |
| Everkeep | Applicable | Blocked | recovery/export requirements documented | backup/export implementation, isolated restore test, acceptance |
| Glaze UI | Applicable | Blocked | product UI requirements only | Home client using required Glaze baseline, accessibility/rendered acceptance |
| GoreeCloud Mesh | Applicable | Blocked | independent durable local journal and adapter boundary | capability registration, bounded events, cross-product acceptance |
| GoreeCloud Identity | Applicable | Blocked | authorization boundary documented | household auth, sessions, roles, guest access, capability scopes, acceptance |

A documented requirement or status endpoint is not substantive platform integration. All seven remain unimplemented/unaccepted for conformance purposes in this foundation.