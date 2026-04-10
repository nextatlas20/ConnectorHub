# quill-source

## Overview

Polls the Quill export bucket and stages new objects for downstream consumers.

## Configuration

`QUILL_BUCKET` and `QUILL_PREFIX` are required. `QUILL_BATCH` defaults to 200 objects.

## Failure modes

Objects that fail checksum validation are skipped and reported to the ops channel.
