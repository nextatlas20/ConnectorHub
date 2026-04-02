# orion-relay

## Overview

Relays Orion event envelopes to subscriber webhooks with at-least-once delivery.

## Configuration

`ORION_RELAY_ENDPOINT` is required. `ORION_MAX_INFLIGHT` defaults to 64 concurrent
deliveries.

## Failure modes

A subscriber returning 5xx is retried with exponential backoff for five minutes,
then the envelope is copied to the parked topic.
