#!/bin/sh
set -eu
usage() {
    echo "Usage: sh run.sh NEW_RESULT.json [--servo-only | --scan-only]" >&2
    exit 2
}
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ] || [ -e "$1" ]; then
    usage
fi
result_path=$1
stage=${2:-}
if [ "$#" -eq 2 ]; then
    case "$stage" in
        --servo-only|--scan-only) ;;
        *) usage ;;
    esac
fi
if [ -n "${DOCKER_CONTEXT:-}" ]; then
    endpoint=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
else
    endpoint=${DOCKER_HOST:-$(docker context inspect --format '{{.Endpoints.docker.Host}}')}
fi
case "$endpoint" in
    unix://*|npipe://*) ;;
    *) echo "This experiment requires a local Docker socket" >&2; exit 2 ;;
esac
docker info --format 'Docker {{.ServerVersion}} {{.OSType}}/{{.Architecture}}' >&2
source_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
if [ -n "$stage" ] && [ ! -f "$source_dir/results.json" ]; then
    echo "A single-stage replay needs the archived 0.5 ms policy and trials in results.json" >&2
    exit 2
fi
scratch=$(mktemp -d "$(dirname -- "$1")/.assembly.XXXXXXXX")
trap 'rm -f "$scratch/first" "$scratch/repeat"; rmdir "$scratch"' EXIT
trap 'exit 1' HUP INT TERM
image=registry-assembly-recovery:pilot
docker build -t "$image" "$source_dir"
set --
if [ -f "$source_dir/results.json" ]; then
    set -- --mount "type=bind,source=$source_dir/results.json,target=/pilot-reference.json,readonly"
fi
set -- "$@" "$image"
if [ -n "$stage" ]; then
    set -- "$@" "$stage"
fi
for replica in first repeat; do
    docker run --rm --read-only --network none --cpus 1 --memory 512m --tmpfs /tmp "$@" > "$scratch/$replica"
done
cmp "$scratch/first" "$scratch/repeat"
ln "$scratch/first" "$result_path"
echo "Verified deterministic replay and saved $result_path"
