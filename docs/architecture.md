# GoreeCloud Home Architecture

## Local authority

Home Core is the authoritative smart-home domain service inside one controller. Internet connectivity and GoreeCloud cloud services are not prerequisites for local state or future local automation execution.

```text
Clients / Automations
        |
   Home Core API
        |
+-------+--------+----------------+
|                |                |
Registry       State           Journal
|                |                |
Home/Room      desired          durable
Device         reported         events
Capability       |
        +---------+
        |
Protocol adapter boundary
Matter/Thread | Zigbee | Z-Wave | MQTT | BLE | LAN
```

## Capability boundary

Adapters translate external protocol state into versioned GoreeCloud capabilities. Home Core does not use a Matter cluster, Zigbee attribute, Z-Wave command class, MQTT topic or vendor cloud schema as its canonical product model.

## Desired and reported state

Every controllable capability may have desired and reported values. A desired value does not become reported merely because a command was issued. This supports honest offline, pending, retry and failure states.

## Durable journal

The local event journal exists independently of GoreeCloud Mesh. Mesh may later exchange cross-product events, but a Mesh outage must not erase Home history or prevent local safety-relevant behavior.

## Controller and node direction

Future deployments may contain one authoritative controller and multiple Home Nodes for radios, Thread Border Router functions or BLE proxying. Authority/failover must prevent split brain.

## Adapter isolation

Each protocol adapter will have explicit discovery, commissioning, subscription, command, credential and error boundaries. Foundational protocol dependencies must remain replaceable and may not silently define application state, authorization or user experience.