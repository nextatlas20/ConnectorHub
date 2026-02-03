# kepler-sink

## Overview

Writes normalized telemetry batches into the Kepler warehouse.

## Configuration

`KEPLER_DSN` is required. `KEPLER_BATCH_SIZE` defaults to 500 records.

## Failure modes

Transient warehouse errors are retried three times; an exhausted batch is
parked in the `kepler_dead_letter` queue.
