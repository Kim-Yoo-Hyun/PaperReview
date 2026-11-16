#!/bin/sh
# Only the selected computer's local Docker. No host Python/package/asset installation.
set -eu
task_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task=gap-retrieval-a1
image=python:3.11.14-slim-bookworm@sha256:65a93d69fa75478d554f4ad27c85c1e69fa184956261b4301ebaf6dbb0a3543d
volume=paper-retrieval-a1-assets
mode=${1:-help}
case "$mode" in
  help|-h|--help)
    printf '%s\n' 'Usage: sh "work/research_topics/context_retrieval/재현 방법/resume_assets.sh" {check|audit|preview|clean}' \
      'audit: verify the 12.8 MB pinned demo archive in Docker; JSON report on stdout.' \
      'preview: emit selected first/last frames as base64 JSON; do not redirect to the repository.' \
      'clean: remove this task-owned temporary volume; preserve pre-existing images.' \
      'No weights, embedding, simulator, training or policy inference is run.'
    exit 0 ;;
  check|audit|preview|clean) ;;
  *) printf 'Unknown mode: %s\n' "$mode" >&2; exit 2 ;;
esac
if [ -n "${DOCKER_CONTEXT:-}" ]; then
  endpoint=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
elif [ -n "${DOCKER_HOST:-}" ]; then
  endpoint=$DOCKER_HOST
else
  endpoint=$(docker context inspect "$(docker context show)" --format '{{.Endpoints.docker.Host}}')
fi
case "$endpoint" in unix://*|npipe://*) ;; *) printf '%s\n' 'Local Docker endpoint required.' >&2; exit 3 ;; esac
d() (unset DOCKER_CONTEXT DOCKER_HOST; docker --host "$endpoint" "$@")
platform=$(d version --format '{{.Server.Os}}/{{.Server.Arch}}')
case "$platform" in linux/amd64|linux/arm64) ;; *) printf 'Unsupported native platform: %s\n' "$platform" >&2; exit 3 ;; esac
if [ "$mode" = check ]; then
  d info --format '{"architecture":"{{.Architecture}}","memory_bytes":{{.MemTotal}},"cpus":{{.NCPU}},"runtimes":"{{range $key,$value := .Runtimes}}{{$key}} {{end}}"}'
  exit 0
fi
if [ "$mode" = clean ]; then
  if d volume inspect "$volume" >/dev/null 2>&1; then
    [ "$(d volume inspect --format '{{index .Labels "paperreview.task"}}' "$volume")" = "$task" ] || exit 4
    d volume rm "$volume"
  fi
  exit 0
fi
if ! d volume inspect "$volume" >/dev/null 2>&1; then
  d volume create --label "paperreview.task=$task" "$volume" >/dev/null
fi
[ "$(d volume inspect --format '{{index .Labels "paperreview.task"}}' "$volume")" = "$task" ] || exit 4
d image inspect "$image" >/dev/null 2>&1 || d pull --platform "$platform" "$image" >&2
image_id=$(d image inspect --format '{{.Id}}' "$image")
name=paper-retrieval-a1-"$mode"-$$
cleanup() {
  owner=$(d inspect --format '{{index .Config.Labels "paperreview.task"}}' "$name" 2>/dev/null || true)
  if [ "$owner" = "$task" ]; then d rm -f "$name" >/dev/null; fi
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
set --
if [ "$mode" = preview ]; then set -- --preview; fi
d run --rm --pull never --name "$name" --label "paperreview.task=$task" \
  --platform "$platform" --read-only --cap-drop ALL --security-opt no-new-privileges \
  --memory 512m --cpus 2 --pids-limit 64 \
  --env "RETRIEVAL_AUDIT_IMAGE_ID=$image_id" \
  --mount "type=bind,src=$task_dir,dst=/audit,readonly" \
  --mount "type=volume,src=$volume,dst=/scratch" \
  --entrypoint python "$image" -B /audit/asset_audit.py "$@"
