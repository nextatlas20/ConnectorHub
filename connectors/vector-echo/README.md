# vector-echo

## Overview

Echoes embedding vectors back to callers and records them for drift analysis.

## Configuration

`VECTOR_ECHO_ENDPOINT` is required. `VECTOR_ECHO_DIM` defaults to 384.

## Failure modes

Malformed vectors are rejected with 422 and counted in the `vector_echo_rejected`
metric.
