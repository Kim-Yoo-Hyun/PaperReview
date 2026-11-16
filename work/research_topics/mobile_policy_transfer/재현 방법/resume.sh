#!/bin/sh
# Host side only inspects Docker. GPU commands execute inside Docker.
# No package installation, image pull, model inference or simulator launch.
set -eu
handoff_mode=${1:-help}
case "$handoff_mode" in
  help)
    printf '%s\n' 'Usage: sh "work/research_topics/mobile_policy_transfer/재현 방법/resume.sh" {check|gpu}' \
      'check: local endpoint + daemon/platform information; not runtime qualification.' \
      'gpu: check, then nvidia-smi in HANDOFF_GPU_IMAGE (must already exist locally).' \
      'See README.md for the remaining native adapter/image work.'
    exit 0 ;;
  check|gpu) ;;
  *) printf '%s\n' 'Unknown mode; use help.' >&2; exit 2 ;;
esac
command -v docker >/dev/null 2>&1 || { printf '%s\n' 'BLOCKED: Docker CLI missing.' >&2; exit 3; }
if [ -n "${DOCKER_CONTEXT:-}" ]; then
  handoff_endpoint=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
elif [ -n "${DOCKER_HOST:-}" ]; then
  handoff_endpoint=$DOCKER_HOST
else
  handoff_endpoint=$(docker context inspect --format '{{.Endpoints.docker.Host}}')
fi
case "$handoff_endpoint" in
  unix://*|npipe://*) ;;
  *) printf '%s\n' 'BLOCKED: use the selected computer local Docker socket; remote endpoints are not allowed.' >&2; exit 2 ;;
esac
# Pin the inspected endpoint for every subsequent call, independent of env defaults.
unset DOCKER_CONTEXT DOCKER_HOST
handoff_docker() { docker --host "$handoff_endpoint" "$@"; }
handoff_docker info --format 'daemon={{.ServerVersion}} os={{.OSType}} architecture={{.Architecture}} cpus={{.NCPU}} memory_bytes={{.MemTotal}} runtimes={{json .Runtimes}}'
handoff_platform=$(handoff_docker version --format '{{.Server.Os}}/{{.Server.Arch}}')
if [ "$handoff_platform" != linux/amd64 ]; then
  printf '%s\n' "BLOCKED: current native recipe requires linux/amd64; observed $handoff_platform. No emulation fallback." >&2
  exit 3
fi
if [ "$handoff_mode" = check ]; then
  printf '%s\n' 'PLATFORM_ONLY: GPU allocation, CUDA/graphics, assets, images and native handoff remain unverified.'
  exit 0
fi
: "${HANDOFF_GPU_IMAGE:?Set an existing local image reference containing nvidia-smi; no image is pulled automatically.}"
handoff_image_id=$(handoff_docker image inspect "$HANDOFF_GPU_IMAGE" --format '{{.Id}}')
handoff_image_platform=$(handoff_docker image inspect "$handoff_image_id" --format '{{.Os}}/{{.Architecture}}')
if [ "$handoff_image_platform" != linux/amd64 ]; then
  printf '%s\n' "BLOCKED: GPU inspection image is $handoff_image_platform, expected linux/amd64." >&2
  exit 3
fi
handoff_container=paper-handoff-p0-gpu-$$
handoff_cleanup() {
  handoff_label=$(handoff_docker inspect --type=container "$handoff_container" --format '{{index .Config.Labels "paperreview.task"}}' 2>/dev/null || true)
  if [ "$handoff_label" = handoff-p0 ]; then
    handoff_docker rm -f "$handoff_container" >/dev/null 2>&1 || true
  fi
}
trap handoff_cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
printf '%s\n' "inspection_image=$handoff_image_id"
handoff_docker run --rm --pull=never --network=none --read-only \
  --cap-drop ALL --security-opt no-new-privileges \
  --name "$handoff_container" --label paperreview.task=handoff-p0 \
  --gpus all --env NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  --entrypoint nvidia-smi "$handoff_image_id" \
  --query-gpu=name,uuid,driver_version,memory.total --format=csv,noheader
printf '%s\n' 'GPU_VISIBILITY_ONLY: this is not a CUDA kernel, Vulkan render, model or handoff qualification result.'
