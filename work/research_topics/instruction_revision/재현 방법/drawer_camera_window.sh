#!/bin/sh
# Run or validate the late single-camera experiment on the selected local daemon.
set -eu
packet=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
sh "$packet/resume.sh" check
image=$(docker image inspect --format '{{.Id}}' paper-revision-p0:7329c159)
[ "$image" = sha256:9ca0e14cfe436930629c15681c49e8a044b73d327ee097ee8eaf780f5d7be7a7 ]
mode=${1:?Supply collect, verify or replay}
path=${2:?Supply a run or result directory}
python=/opt/resteer/.venv/bin/python
script=/packet/drawer_camera_window.py
gpu=${REVISION_GPU_DEVICE:-0}
case "$gpu" in ''|*[!0-9]*) exit 2;; esac
case "$mode" in
  collect)
    [ "$#" -eq 2 ]
    [ ! -e "$path" ]
    parent=$(CDPATH= cd -- "$(dirname -- "$path")" && pwd)
    [ "$(docker volume inspect --format '{{index .Labels "paperreview.task"}}' paper-revision-p0-data)" = instruction-revision-p0 ]
    set -- --hostname localhost --mount type=volume,src=paper-revision-p0-data,dst=/data,readonly \
      --mount "type=bind,src=$parent,dst=/runs" -e "REVISION_IMAGE_ID=$image" \
      --entrypoint /opt/resteer/third_party/openpi/.venv/bin/python "$image" "$script" "/runs/$(basename -- "$path")" collect ;;
  verify)
    [ "$#" -eq 2 ]
    run=$(CDPATH= cd -- "$path" && pwd)
    exec docker run --rm --pull never --network none --cap-drop ALL --security-opt no-new-privileges \
      --mount "type=bind,src=$packet,dst=/packet,readonly" --mount "type=bind,src=$run,dst=/trial,readonly" \
      --entrypoint "$python" "$image" "$script" /trial verify ;;
  replay)
    [ "$#" -eq 3 ]
    [ ! -e "$3" ]
    run=$(CDPATH= cd -- "$path" && pwd)
    report=$(CDPATH= cd -- "$(dirname -- "$3")" && pwd)
    set -- --mount "type=bind,src=$run,dst=/trial,readonly" --mount "type=bind,src=$report,dst=/report" \
      --entrypoint "$python" "$image" "$script" /trial replay --output "/report/$(basename -- "$3")" ;;
  *) exit 2 ;;
esac
exec docker run --rm --pull never --network none --gpus "device=$gpu" --shm-size 2g \
  -e CUDA_VISIBLE_DEVICES=0 -e MUJOCO_EGL_DEVICE_ID=0 -e OPENBLAS_NUM_THREADS=1 -e OMP_NUM_THREADS=1 \
  --mount "type=bind,src=$packet,dst=/packet,readonly" "$@"
