#!/usr/bin/env bash
set -euo pipefail
task_dir="$(cd "$(dirname "$0")" && pwd)"
endpoint="$(docker context inspect --format '{{.Endpoints.docker.Host}}')"
if [[ -n "${DOCKER_HOST:-}" ]]; then endpoint="$DOCKER_HOST"; fi
case "$endpoint" in unix://*) ;; *) echo 'Local Docker only.' >&2; exit 2;; esac
result_dir="${1:-$task_dir/results/reanalysis}"
mkdir -p "$result_dir"
result_dir="$(cd "$result_dir" && pwd)"
if [[ -e "$result_dir/analysis.json" ]]; then echo 'Choose a fresh output directory.' >&2; exit 2; fi
image_id="$(docker image inspect --format '{{.Id}}' paper-gap-p3:rvo-c2c46ba)"
docker image inspect "$image_id" > "$result_dir/docker_image.json"
docker run --rm --label org.openai.task=gap-p4-recorded-analysis \
  --network none --read-only --cpus 2 --memory 512m --pids-limit 128 \
  --cap-drop ALL --security-opt no-new-privileges --tmpfs /tmp:rw,size=32m \
  --mount "type=bind,source=$task_dir,target=/app,readonly" \
  --mount "type=bind,source=$task_dir/results/verified,target=/recorded,readonly" \
  --mount "type=bind,source=$result_dir,target=/output" \
  "$image_id" python -B replay_analysis.py
