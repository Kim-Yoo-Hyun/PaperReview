#!/usr/bin/env bash
set -euo pipefail
task_dir="$(cd "$(dirname "$0")" && pwd)"
image_tag="paper-gap-p3:rvo-c2c46ba"
endpoint="$(docker context inspect --format '{{.Endpoints.docker.Host}}')"
if [[ -n "${DOCKER_HOST:-}" ]]; then endpoint="$DOCKER_HOST"; fi
case "$endpoint" in unix://*) ;; *) echo 'Only local Docker unix sockets are allowed.' >&2; exit 2;; esac
case "${1:-check}" in
  build)
    docker build --label org.openai.task=gap-p3-reactive-nav-contract -t "$image_tag" "$task_dir"
    ;;
  check)
    result_dir="${2:-$task_dir/results/replay}"
    mkdir -p "$result_dir"
    result_dir="$(cd "$result_dir" && pwd)"
    if [[ -e "$result_dir/contract_report.json" ]]; then
      echo 'Choose a fresh output directory to preserve previous evidence.' >&2; exit 2
    fi
    image_id="$(docker image inspect --format '{{.Id}}' "$image_tag")"
    docker image inspect "$image_id" > "$result_dir/docker_image.json"
    docker version --format '{{json .}}' > "$result_dir/docker_version.json"
    docker run --rm --label org.openai.task=gap-p3-reactive-nav-contract \
      --network none --read-only --cpus 2 --memory 512m --pids-limit 128 \
      --cap-drop ALL --security-opt no-new-privileges --tmpfs /tmp:rw,size=16m \
      --mount "type=bind,source=$task_dir,target=/app,readonly" \
      --mount "type=bind,source=$result_dir,target=/output" \
      "$image_id"
    ;;
  *) echo 'Usage: bash run.sh build | check [fresh_output_directory]' >&2; exit 2;;
esac
