#!/bin/sh
# Repository-relative entry point; experiment dependencies stay inside Docker.
set -eu
task_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_root=$(CDPATH= cd -- "$task_dir/../../.." && pwd)
task_image=paper-registry-c3-replay:2026-10-23
task_evidence=$task_root/work/experiments/vla_rl_c3_logits/evidence
task_command=${1:-help}
case "$task_command" in
  help)
    printf '%s\n' 'Usage: sh work/experiments/portable/run.sh {check|build|replay-c3|test|clean}'
    exit 0 ;;
  check|build|replay-c3|test|clean) ;;
  *) printf '%s\n' 'Unsupported task. Native policy experiments remain HOLD; see README.md.' >&2; exit 2 ;;
esac
# Reject remote endpoints: bind mounts and user authorization refer to this computer.
if [ -n "${DOCKER_CONTEXT:-}" ]; then
  task_endpoint=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
else
  task_endpoint=${DOCKER_HOST:-$(docker context inspect --format '{{.Endpoints.docker.Host}}')}
fi
case "$task_endpoint" in unix://*|npipe://*) ;; *) printf '%s\n' 'Use a local Docker daemon on the selected computer.' >&2; exit 2 ;; esac
docker info >/dev/null
task_platform=${PAPER_REPLAY_PLATFORM:-$(docker version --format '{{.Server.Os}}/{{.Server.Arch}}')}
case "$task_platform" in linux/arm64|linux/amd64) ;; *) printf '%s\n' 'Supported image platforms: linux/arm64, linux/amd64.' >&2; exit 2 ;; esac
task_image=$task_image-${task_platform#linux/}
case "$task_command" in
  check)
    docker version --format '{{json .Server}}'
    for task_file in native_logits.npz logits_analysis.json tail_audit.json; do
      test -f "$task_evidence/$task_file" || { printf '%s\n' "Missing evidence: $task_file" >&2; exit 1; }
    done
    git -C "$task_root" status --short -- work/experiments/portable work/experiments/vla_rl_c3_logits/evidence
    printf '%s\n' 'Local prerequisites present. Dirty/untracked files above are not yet guaranteed in a clone.' ;;
  build) docker build --platform "$task_platform" --tag "$task_image" "$task_dir" ;;
  replay-c3)
    docker run --platform "$task_platform" --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges \
      --user 65534:65534 --tmpfs /tmp:rw,nosuid,size=16m \
      --mount "type=bind,src=$task_evidence,dst=/evidence,readonly" "$task_image" ;;
  test)
    docker run --platform "$task_platform" --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges \
      --user 65534:65534 --tmpfs /tmp:rw,nosuid,size=16m \
      --entrypoint python "$task_image" /opt/replay/test_replay.py ;;
  clean) docker image rm "$task_image" ;;
esac
