# atlas-sink

## Overview

Streams normalized metrics into the Atlas time-series store.

## Configuration

`ATLAS_SINK_ENDPOINT` and `ATLAS_SINK_TOKEN` are required.

## Failure modes

The writer buffers up to 10,000 points while Atlas is unreachable and flushes them
on reconnect.
