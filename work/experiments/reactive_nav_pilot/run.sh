#!/usr/bin/env bash
set -euo pipefail
task_dir="$(cd "$(dirname "$0")" && pwd)"
contract_dir="$(cd "$task_dir/../reactive_nav_contract" && pwd)"
endpoint="$(docker context inspect --format '{{.Endpoints.docker.Host}}')"
if [[ -n "${DOCKER_HOST:-}" ]]; then endpoint="$DOCKER_HOST"; fi
case "$endpoint" in unix://*) ;; *) echo 'Only local Docker unix sockets allowed.' >&2; exit 2;; esac
image_id='sha256:ec14bd72a90f89cb6f3c4b263bb35a81de7977dffb2e5a2cb7e96946f1545ebb'
docker image inspect "$image_id" >/dev/null
result_dir="${2:-$task_dir/results/replay}"
mkdir -p "$result_dir"
result_dir="$(cd "$result_dir" && pwd)"
case "${1:-run}" in
  run)
    if [[ -e "$result_dir/FROZEN_RUN.json" ]]; then echo 'Choose fresh output directory.' >&2; exit 2; fi
    docker image inspect "$image_id" > "$result_dir/docker_image.json"
    docker version --format '{{json .}}' > "$result_dir/docker_version.json"
    docker run --rm --label org.openai.task=gap-p4-reactive-nav-pilot \
      --network none --read-only --cpus 2 --memory 512m --pids-limit 128 \
      --cap-drop ALL --security-opt no-new-privileges --tmpfs /tmp:rw,size=16m \
      --mount "type=bind,source=$task_dir,target=/app,readonly" \
      --mount "type=bind,source=$contract_dir,target=/contract,readonly" \
      --mount "type=bind,source=$result_dir,target=/output" \
      "$image_id" sh -c 'python -B pilot.py --output /output && python -B analyse.py --output /output'
    ;;
  *) echo 'Usage: bash run.sh run [fresh_output_directory]' >&2; exit 2;;
esac
