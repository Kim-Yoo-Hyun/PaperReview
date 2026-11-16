#!/bin/sh
set -eu
if [ "$#" -ne 1 ]; then
    echo 'Usage: sh run_contract.sh NEW_OUTPUT_DIRECTORY' >&2
    exit 2
fi
task_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
mkdir -p -- "$1"
task_output=$(CDPATH= cd -- "$1" && pwd)
if [ -n "$(ls -A "$task_output")" ]; then
    echo 'Output directory must be empty; existing evidence is preserved.' >&2
    exit 2
fi
task_image='python:3.11.14-slim-bookworm@sha256:65a93d69fa75478d554f4ad27c85c1e69fa184956261b4301ebaf6dbb0a3543d'
task_cache=$(mktemp -d "${TMPDIR:-/tmp}/gap-n3-source.XXXXXX")
# Own temporary source directory only; never use a user-supplied cleanup path.
trap 'rm -rf -- "$task_cache"' EXIT HUP INT TERM
docker run --rm --read-only --cap-drop ALL --security-opt no-new-privileges --memory 512m --cpus 2 --pids-limit 64 \
  --tmpfs /tmp:rw,nosuid,nodev,size=64m \
  --mount "type=bind,source=$task_root,target=/app,readonly" \
  --mount "type=bind,source=$task_cache,target=/source" \
  -w /app "$task_image" python -B source_repair.py fetch /source
docker run --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges --memory 512m --cpus 2 --pids-limit 64 \
  --tmpfs /tmp:rw,nosuid,nodev,size=64m \
  --mount "type=bind,source=$task_root,target=/app,readonly" \
  --mount "type=bind,source=$task_cache,target=/source,readonly" \
  --mount "type=bind,source=$task_output,target=/output" \
  -e "N3_IMAGE_REFERENCE=$task_image" -w /app "$task_image" \
  python -B check_contract.py --source /source --output /output
