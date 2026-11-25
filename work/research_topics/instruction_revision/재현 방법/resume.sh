#!/bin/sh
# Local Docker only. No host Python, dependency installation, or emulation.
set -eu
recipe_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task=instruction-revision-p0
image=paper-revision-p0:7329c159
base=ghcr.io/astral-sh/uv:0.8.22-python3.11-bookworm-slim@sha256:e59dc06793821e707e3a90234025c996eb4db2af807fdd7d9dd731d2fc678a96
data_volume=paper-revision-p0-data
run_volume=paper-revision-p0-runs
mode=${1:-help}
case "$mode" in
  help|-h|--help)
    printf '%s\n' 'Setup: check, gpu, build, assets, smoke, results' \
      'Collect: drawer-location NEW_DIR, middle-aperture-layout2 NEW_DIR' \
      'Score: verify-drawer-location DIR, verify-middle-aperture DIR, verify-stove-layouts DIR' \
      'Replay: replay-drawer-location DIR [NEW_REPORT], replay-prior-closed DIR NEW_REPORT'
    exit 0 ;;
  check|gpu|build|assets|smoke|results|drawer-location|middle-aperture-layout2|verify-drawer-location|verify-middle-aperture|verify-stove-layouts|replay-drawer-location|replay-prior-closed) ;;
  *) printf 'Unknown drawer study stage: %s\n' "$mode" >&2; exit 2 ;;
esac

if [ -n "${DOCKER_CONTEXT:-}" ]; then
  endpoint=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
elif [ -n "${DOCKER_HOST:-}" ]; then
  endpoint=$DOCKER_HOST
else
  endpoint=$(docker context inspect "$(docker context show)" --format '{{.Endpoints.docker.Host}}')
fi
case "$endpoint" in
  unix://*|npipe://*) ;;
  *) printf 'Only the selected local Docker endpoint is allowed: %s\n' "$endpoint" >&2; exit 3 ;;
esac
d() (unset DOCKER_CONTEXT DOCKER_HOST; docker --host "$endpoint" "$@")
platform=$(d version --format '{{.Server.Os}}/{{.Server.Arch}}')
printf 'Local endpoint: %s; daemon: %s\n' "$endpoint" "$platform" >&2
d info --format 'cpus={{.NCPU}} memory_bytes={{.MemTotal}} runtimes={{range $name, $_ := .Runtimes}}{{$name}} {{end}}' >&2
if [ "$platform" != linux/amd64 ]; then
  printf 'NOT_MET: linux/amd64 with NVIDIA CUDA/EGL is required; no emulation or fallback.\n' >&2
  exit 3
fi
[ "$mode" != check ] || exit 0

gpu_device=${REVISION_GPU_DEVICE:-0}
case "$gpu_device" in ''|*[!0-9]*) printf 'Select one numeric GPU index.\n' >&2; exit 2 ;; esac
container=paper-revision-p0-"$mode"-$$
cleanup() {
  owned=$(d inspect --format '{{index .Config.Labels "paperreview.task"}}' "$container" 2>/dev/null || true)
  if [ "$owned" = "$task" ]; then d rm -f "$container" >/dev/null; fi
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

gpu() {
  d image inspect "$base" >/dev/null 2>&1 || d pull --platform linux/amd64 "$base"
  d run --rm --pull never --name "$container" --label "paperreview.task=$task" \
    --network none --gpus "device=$gpu_device" \
    --env NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility \
    --entrypoint nvidia-smi "$base" \
    --query-gpu=name,uuid,driver_version,memory.total --format=csv,noheader
}
if [ "$mode" = gpu ]; then gpu; exit 0; fi
if [ "$mode" = build ]; then
  gpu
  if d image inspect "$image" >/dev/null 2>&1; then
    [ "$(d image inspect --format '{{index .Config.Labels "paperreview.task"}}' "$image")" = "$task" ] || {
      printf 'Existing image tag belongs to another task; refusing replacement.\n' >&2; exit 4;
    }
  fi
  d build --platform linux/amd64 --tag "$image" "$recipe_dir"
  d image inspect --format 'built_image={{.Id}} platform={{.Os}}/{{.Architecture}}' "$image"
  exit 0
fi

image_id=$(d image inspect --format '{{.Id}}' "$image")
[ "$(d image inspect --format '{{index .Config.Labels "paperreview.task"}}' "$image_id")" = "$task" ] || exit 4
[ "$(d image inspect --format '{{.Os}}/{{.Architecture}}' "$image_id")" = linux/amd64 ] || exit 4

sim=/opt/resteer/.venv/bin/python
policy=/opt/resteer/third_party/openpi/.venv/bin/python
case "$mode" in
  verify-drawer-location|verify-middle-aperture|verify-stove-layouts)
    [ "$#" -eq 2 ] && [ -d "$2" ] || { echo 'Supply the recorded run or archive directory.' >&2; exit 2; }
    case "$mode" in
      verify-drawer-location) verifier=drawer_location.py ;;
      verify-middle-aperture) verifier=verify_middle_aperture.py ;;
      verify-stove-layouts) verifier=verify_stove_layouts.py ;;
    esac
    run_path=$(CDPATH= cd -- "$2" && pwd)
    d run --rm --pull never --name "$container" --label "paperreview.task=$task" --network none \
      --cap-drop ALL --security-opt no-new-privileges \
      --mount "type=bind,src=$recipe_dir,dst=/packet,readonly" --mount "type=bind,src=$run_path,dst=/trial,readonly" \
      --entrypoint "$sim" "$image_id" "/packet/$verifier" /trial
    exit 0 ;;
  replay-drawer-location|replay-prior-closed)
    [ "$#" -ge 2 ] && [ "$#" -le 3 ] && [ -d "$2" ] || { echo 'Supply an existing run and optionally a new report.' >&2; exit 2; }
    run_path=$(CDPATH= cd -- "$2" && pwd)
    if [ "$mode" = replay-prior-closed ]; then
      [ "$#" -eq 3 ] || { echo 'Supply a new report path for the historical replay.' >&2; exit 2; }
      script=replay_prior_closed.py
    else
      script=drawer_location.py
    fi
    output=${3:-}
    set -- --entrypoint "$sim" "$image_id" "/packet/$script" /trial
    [ "$mode" = replay-prior-closed ] || set -- "$@" replay
    if [ -n "$output" ]; then
      [ ! -e "$output" ] || { echo 'The report path already exists.' >&2; exit 2; }
      report_dir=$(CDPATH= cd -- "$(dirname -- "$output")" && pwd)
      set -- --mount "type=bind,src=$report_dir,dst=/report" "$@" --output "/report/$(basename -- "$output")"
    fi
    d run --rm --pull never --name "$container" --label "paperreview.task=$task" --network none \
      --gpus "device=$gpu_device" --shm-size 2g --env CUDA_VISIBLE_DEVICES=0 --env MUJOCO_EGL_DEVICE_ID=0 \
      --env OMP_NUM_THREADS=1 --env OPENBLAS_NUM_THREADS=1 \
      --mount "type=bind,src=$recipe_dir,dst=/packet,readonly" --mount "type=bind,src=$run_path,dst=/trial,readonly" "$@"
    exit 0 ;;
esac

volume() {
  if ! d volume inspect "$1" >/dev/null 2>&1; then
    [ "$mode" != results ] || { printf 'No saved run volume.\n' >&2; exit 4; }
    d volume create --label "paperreview.task=$task" "$1" >/dev/null
  fi
  [ "$(d volume inspect --format '{{index .Labels "paperreview.task"}}' "$1")" = "$task" ] || {
    printf 'Volume ownership mismatch: %s\n' "$1" >&2; exit 4;
  }
}
if [ "$mode" = results ]; then
  volume "$run_volume"
  d run --rm --pull never --name "$container" --label "paperreview.task=$task" --network none \
    --mount "type=volume,src=$run_volume,dst=/runs,readonly" "$image_id" results
  exit 0
fi

volume "$data_volume"
if [ "$mode" = drawer-location ] || [ "$mode" = middle-aperture-layout2 ]; then
  [ "$#" -eq 2 ] && [ ! -e "$2" ] || { echo 'Supply a new output directory.' >&2; exit 2; }
  parent=$(CDPATH= cd -- "$(dirname -- "$2")" && pwd)
  leaf=$(basename -- "$2")
  if [ "$mode" = drawer-location ]; then
    set -- /packet/drawer_location.py "/output/$leaf" collect
  else
    set -- /packet/verify_middle_aperture.py "/output/$leaf" collect --layout 2
  fi
  d run --rm --pull never --name "$container" --label "paperreview.task=$task" --network none --hostname localhost \
    --gpus "device=$gpu_device" --shm-size 2g --env CUDA_VISIBLE_DEVICES=0 --env MUJOCO_EGL_DEVICE_ID=0 \
    --env "REVISION_IMAGE_ID=$image_id" --env JAX_COMPILATION_CACHE_DIR=/tmp/revision-jit \
    --mount "type=volume,src=$data_volume,dst=/data,readonly" --mount "type=bind,src=$recipe_dir,dst=/packet,readonly" \
    --mount "type=bind,src=$parent,dst=/output" --entrypoint "$policy" "$image_id" "$@"
  exit 0
fi
if [ "$mode" = assets ]; then
  d run --rm --pull never --name "$container" --label "paperreview.task=$task" \
    --mount "type=volume,src=$data_volume,dst=/data" "$image_id" assets
else
  volume "$run_volume"
  d run --rm --pull never --name "$container" --label "paperreview.task=$task" \
    --network none --hostname localhost --gpus "device=$gpu_device" --shm-size 2g \
    --env CUDA_VISIBLE_DEVICES=0 --env MUJOCO_EGL_DEVICE_ID=0 \
    --env "REVISION_IMAGE_ID=$image_id" \
    --mount "type=volume,src=$data_volume,dst=/data" \
    --mount "type=volume,src=$run_volume,dst=/runs" "$image_id" smoke
fi
