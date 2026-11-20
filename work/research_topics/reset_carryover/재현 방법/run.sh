#!/bin/sh
# Reproduce the CPU simulations in local Docker and publish one new result file.
set -eu
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ] || { [ "$#" -eq 2 ] && [ "$2" != panda ]; }; then
    echo "Usage: sh run.sh NEW_RESULT.json [panda]" >&2
    exit 2
fi
output=$1
if [ -e "$output" ]; then
    echo "Result path already exists: $output" >&2
    exit 2
fi
if [ -n "${DOCKER_CONTEXT:-}" ]; then
    endpoint=$(docker context inspect "$DOCKER_CONTEXT" --format '{{.Endpoints.docker.Host}}')
else
    endpoint=${DOCKER_HOST:-$(docker context inspect --format '{{.Endpoints.docker.Host}}')}
fi
case "$endpoint" in
    unix://*|npipe://*) ;;
    *) echo "A local Docker socket is required" >&2; exit 2 ;;
esac
docker info --format 'Docker {{.ServerVersion}} {{.OSType}}/{{.Architecture}}' >&2

source_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
scratch=$(mktemp -d "$(dirname -- "$output")/.reset-pilot.XXXXXXXX")
scratch=$(CDPATH='' cd -- "$scratch" && pwd)
cleanup() {
    rm -f "$scratch/primary" "$scratch/repeat" "$scratch/half_step" "$scratch/matched_close" "$scratch/public_door" "$scratch/bundle" "$scratch/panda.json"
    rmdir "$scratch"
}
trap cleanup EXIT
trap 'exit 1' HUP INT TERM
if [ "${2:-}" = panda ]; then
    image=registry-reset-panda:reference
    workers=${PANDA_WORKERS:-4}
    case "$workers" in 1|2|3|4) ;; *) echo "PANDA_WORKERS must be 1 to 4" >&2; exit 2 ;; esac
    docker build --platform linux/amd64 -f "$source_dir/Panda.Dockerfile" -t "$image" "$source_dir"
    docker run --rm --network none --platform linux/amd64 --cpus "$workers" --memory 5g \
        --mount "type=bind,source=$scratch,target=/out" "$image" python -u panda_eval.py /out/panda.json --workers "$workers"
    cat "$scratch/panda.json" > "$scratch/bundle"
    ln "$scratch/bundle" "$output"
    echo "Result saved to $output"
    exit 0
fi
image=registry-reset-carryover:pilot-1
docker build -t "$image" "$source_dir"
simulate() {
    docker run --rm -i --network none --read-only --cpus 1 --memory 512m --tmpfs /tmp "$@"
}
simulate "$image" run > "$scratch/primary"
simulate "$image" run > "$scratch/repeat"
cmp "$scratch/primary" "$scratch/repeat"
simulate "$image" run --timestep-ms 1 > "$scratch/half_step"
simulate "$image" run --matched-close > "$scratch/matched_close"
simulate --entrypoint python "$image" door_probe.py > "$scratch/public_door"
{
    printf '{"primary":'
    cat "$scratch/primary"
    for name in half_step matched_close public_door; do
        printf ',"%s":' "$name"
        cat "$scratch/$name"
    done
    printf '}\n'
} > "$scratch/bundle"
simulate "$image" check < "$scratch/bundle"
ln "$scratch/bundle" "$output"
echo "Result saved to $output"
