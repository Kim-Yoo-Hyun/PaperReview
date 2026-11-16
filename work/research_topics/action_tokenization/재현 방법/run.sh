#!/bin/sh
set -eu
TASK_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TASK_IMAGE=paper-gap-codec1:20261103
TASK_CONTEXT=$(docker context show)
# DOCKER_CONTEXT takes precedence over DOCKER_HOST in the Docker CLI.
if [ -n "${DOCKER_CONTEXT:-}" ]; then
  TASK_ENDPOINT=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
else
  TASK_ENDPOINT=${DOCKER_HOST:-$(docker context inspect "$TASK_CONTEXT" --format '{{.Endpoints.docker.Host}}')}
fi
case "$TASK_ENDPOINT" in unix://*) ;; *) echo 'Local Docker socket required' >&2; exit 3;; esac
# Bind every operation to the endpoint we checked, even with conflicting env vars.
task_docker() {
  (unset DOCKER_CONTEXT DOCKER_HOST; docker --host "$TASK_ENDPOINT" "$@")
}
task_docker info --format 'Docker {{.ServerVersion}} {{.OSType}}/{{.Architecture}} CPUs={{.NCPU}} RAM={{.MemTotal}}'
case "${1:-check}" in
  check) ;;
  build) task_docker build --label org.openai.task=gap-codec1-20261103 -t "$TASK_IMAGE" "$TASK_DIR" ;;
  run|suffix)
    TASK_MODE=$1
    TASK_DEFAULT=verified
    if [ "$TASK_MODE" = suffix ]; then TASK_DEFAULT=suffix_verified; fi
    TASK_OUT=${2:-"$TASK_DIR/results/$TASK_DEFAULT"}
    TASK_SCRIPT=probe.py
    if [ "$TASK_MODE" = suffix ]; then TASK_SCRIPT=suffix_probe.py; fi
    mkdir -p "$TASK_OUT"
    TASK_OUT=$(CDPATH= cd -- "$TASK_OUT" && pwd)
    if [ -e "$TASK_OUT/results.json" ]; then echo 'Use a new output directory; existing evidence preserved' >&2; exit 4; fi
    task_docker run --rm --pull=never --label org.openai.task=gap-codec1-20261103 \
      --cpus 2 --memory 3g --pids-limit 128 --cap-drop ALL --security-opt no-new-privileges \
      --read-only --tmpfs /tmp:rw,size=536870912 \
      -e HF_HOME=/tmp/hf -e HOME=/tmp \
      -v "$TASK_DIR:/app:ro" -v "$TASK_OUT:/output:rw" --entrypoint python "$TASK_IMAGE" -B "/app/$TASK_SCRIPT"
    ;;
  cleanup)
    TASK_LABEL=$(task_docker image inspect "$TASK_IMAGE" --format '{{index .Config.Labels "org.openai.task"}}')
    [ "$TASK_LABEL" = gap-codec1-20261103 ] || exit 5
    task_docker image rm "$TASK_IMAGE"
    ;;
  *) echo 'Usage: sh run.sh check|build|run|suffix [new-output-dir]|cleanup' >&2; exit 2;;
esac
