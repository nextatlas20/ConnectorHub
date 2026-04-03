# nova-bridge

## Overview

Bridges Nova change events into the internal event bus.

## Configuration

`NOVA_BRIDGE_ENDPOINT` is required. `NOVA_BUS_TOPIC` defaults to `nova.changes`.

## Troubleshooting

Check the bridge logs for signature mismatches before paging the on-call engineer.
