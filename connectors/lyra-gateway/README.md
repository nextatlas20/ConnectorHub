# lyra-gateway

## Overview

Fronts the Lyra pricing service and enforces per-tenant request quotas.

## Configuration

`LYRA_GATEWAY_ENDPOINT` is required. `LYRA_QUOTA_RPS` defaults to 20 requests per
second.

## Failure modes

When the upstream is unavailable the gateway serves cached quotes for ten minutes
and then returns 503 to the caller.
