# GoreeCloud Home Security Boundary

## Current foundation

- The Development HTTP server defaults to `127.0.0.1`.
- The HTTP surface is read-only and does not expose device registration or desired-state mutation.
- Status output contains product/lifecycle information and aggregate counts only.
- The repository contains no protocol credentials, enrollment secrets, private keys or production environment values.

## Privileged future capabilities

Locks, garage doors, gates, alarms, security modes, cameras, doorbells and comparable capabilities require stronger authorization and auditing than low-risk lighting controls. Future APIs must receive an authenticated authority context and enforce capability-specific permissions.

## Required Wardveil work

- device/controller trust
- credential and key storage boundary
- network and adapter risk controls
- privileged operation policy
- abuse/rate controls for remote surfaces
- security event audit
- integration and application acceptance

The current foundation must not be described as Wardveil-integrated or production secure.