#!/usr/bin/env python3
"""Host stdlib control plane only. All payloads, dependencies and native work stay in local Docker."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import uuid

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OWNER = 'paperregistry.langret-p0'
LABEL = 'org.paperregistry.langret.packet-sha'
FILES = ['langret_resume.py', 'langret_probe.py', 'langret.Dockerfile', 'langret_requirements.txt']


def capture(argv, timeout=25):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return dict(argv=argv, exit_code=p.returncode, stdout=p.stdout.strip(), stderr=p.stderr.strip())
    except (OSError, subprocess.TimeoutExpired) as exc:
        return dict(argv=argv, exit_code=None, stdout='', stderr=str(exc))


def compile_plan():
    ledger = json.loads((ROOT / 'work/sources/vla_masters_gap_scout_2026-11-12.json').read_text())
    return ledger['p0_preparation']['runtime_plan']


def fingerprint(plan):
    h = hashlib.sha256(json.dumps(plan, sort_keys=True).encode())
    for name in FILES:
        h.update(name.encode() + b'\0' + (HERE / name).read_bytes())
    return h.hexdigest()


def resource_reasons(host_os, host_arch, endpoint, server, overrides):
    reasons = []
    if overrides:
        reasons.append('Docker/builder overrides must be unset')
    if not endpoint.startswith('unix://'):
        reasons.append('Local Unix Docker endpoint required')
    if host_os != 'Linux' or host_arch not in ('x86_64', 'amd64'):
        reasons.append('Native packet requires local Linux x86-64')
    if server.get('OSType') != 'linux' or server.get('Architecture') not in ('x86_64', 'amd64'):
        reasons.append('Native packet requires Linux amd64 daemon')
    if (server.get('MemTotal') or 0) < 32 * 1024**3:
        reasons.append('Selected daemon RAM floor is 32 GiB; not a measured minimum')
    return reasons


def check(gpu):
    out = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
               host=dict(os=platform.system(), arch=platform.machine()), commands=[], native_runs=0)
    overrides = [k for k in ('DOCKER_HOST', 'DOCKER_CONTEXT', 'BUILDX_BUILDER', 'BUILDKIT_HOST', 'DOCKER_TLS_VERIFY') if os.environ.get(k)]
    if overrides or not shutil.which('docker'):
        return dict(out, decision='RESOURCE_UNMET', reasons=['Docker CLI required and overrides must be unset'])
    ctx = capture(['docker', 'context', 'show'])
    if ctx['exit_code'] != 0:
        return dict(out, decision='RESOURCE_UNMET', reasons=['Docker context unavailable'], commands=[ctx])
    ep = capture(['docker', 'context', 'inspect', ctx['stdout'], '--format', '{{.Endpoints.docker.Host}}'])
    endpoint = ep['stdout']
    ep['stdout'] = endpoint.replace(str(Path.home()), '<user-home>')
    out['commands'].extend([ctx, ep])
    if ep['exit_code'] != 0 or not endpoint.startswith('unix://'):
        return dict(out, decision='RESOURCE_UNMET', reasons=['Local endpoint not established; no daemon mutation'])
    raw = capture(['docker', '--context', ctx['stdout'], 'info', '--format', '{{json .}}'])
    server = {}
    if raw['exit_code'] == 0:
        info = json.loads(raw['stdout'])
        server = {k: info.get(k) for k in ('OSType', 'Architecture', 'MemTotal', 'NCPU', 'ServerVersion', 'OperatingSystem')}
    out['commands'].append(dict(argv=raw['argv'], exit_code=raw['exit_code'], server=server, stderr=raw['stderr']))
    reasons = resource_reasons(platform.system(), platform.machine(), endpoint, server, overrides)
    if raw['exit_code'] != 0:
        reasons.append('Docker daemon unavailable')
    if not reasons:
        info = capture(['nvidia-smi', '--query-gpu=index,uuid,name,driver_version,memory.free', '--format=csv,noheader,nounits'])
        out['commands'].append(info)
        try:
            row = next(r for r in csv.reader(info['stdout'].splitlines(), skipinitialspace=True) if int(r[0]) == gpu)
            if tuple(map(int, row[3].split('.'))) < (550, 54, 15):
                reasons.append('Driver below selected CUDA 12.4.1 target 550.54.15')
            if float(row[4]) < 24 * 1024:
                reasons.append('Selected free VRAM floor is 24 GiB; 48 GiB recommended, sufficiency unverified')
            out['gpu'] = dict(index=gpu, uuid=row[1], name=row[2], driver=row[3], free_mib=float(row[4]))
        except (ValueError, IndexError, StopIteration):
            reasons.append('Selected NVIDIA GPU metadata unavailable')
    return dict(out, context=ctx['stdout'], decision='RESOURCE_UNMET' if reasons else 'HOST_ELIGIBLE_CONTAINER_UNVERIFIED', reasons=reasons)


def require_image(docker, image, expected):
    r = capture(docker + ['image', 'inspect', image, '--format', '{{index .Config.Labels "' + LABEL + '"}}'])
    if r['exit_code'] != 0 or r['stdout'] != expected:
        raise RuntimeError('Missing/stale image. Build this exact packet first.')


def ensure_volume(docker, volume):
    r = capture(docker + ['volume', 'inspect', volume, '--format', '{{index .Labels "org.paperregistry.owner"}}'])
    if r['exit_code'] == 0:
        if r['stdout'] != OWNER:
            raise RuntimeError('Refusing unrelated existing cache volume')
    else:
        subprocess.run(docker + ['volume', 'create', '--label', 'org.paperregistry.owner=' + OWNER, volume], check=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=['check', 'build', 'prepare', 'p0'])
    p.add_argument('--results', required=True, type=Path, help='New output directory; never reuse an old run')
    p.add_argument('--gpu', type=int, default=0)
    args = p.parse_args()
    if args.gpu < 0:
        p.error('GPU index must be nonnegative')
    output = args.results.resolve()
    if ',' in str(output):
        p.error('Result path must not contain commas (Docker mount syntax)')
    output.mkdir(parents=True, exist_ok=False)
    report = check(args.gpu)
    (output / 'local_check.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    if report['decision'] == 'RESOURCE_UNMET':
        return 3
    if args.phase == 'check':
        return 0
    plan = compile_plan()
    packet = fingerprint(plan)
    plan['packet_sha256'] = packet
    docker = ['docker', '--context', report['context']]
    image = 'paper-langret-p0:' + packet[:16]
    volume = 'paper-langret-cache-' + packet[:16]
    name = 'paper-langret-' + uuid.uuid4().hex[:12]
    command = []
    try:
        if args.phase == 'build':
            # Allocate only on the compatible host; never pull a GPU image on resource failure.
            alloc = capture(docker + ['run', '--rm', '--name', name, '--label', 'org.paperregistry.owner=' + OWNER,
                                      '--gpus', 'device=' + str(args.gpu), '--network=none',
                                      plan['base_image'], 'nvidia-smi', '--query-gpu=uuid,name', '--format=csv,noheader'], timeout=180)
            (output / 'allocation.json').write_text(json.dumps(alloc, indent=2))
            if alloc['exit_code'] != 0 or report['gpu']['uuid'] not in alloc['stdout']:
                raise RuntimeError('Docker NVIDIA allocation did not match selected host GPU')
            with tempfile.TemporaryDirectory(prefix='langret-build-') as tmp:
                for f in FILES:
                    shutil.copyfile(HERE / f, Path(tmp) / f)
                (Path(tmp) / 'plan.json').write_text(json.dumps(plan, indent=2))
                command = docker + ['build', '--force-rm', '--platform', 'linux/amd64', '-f', str(Path(tmp) / 'langret.Dockerfile'),
                                    '--build-arg', 'PACKET_SHA=' + packet, '-t', image, tmp]
                with (output / 'build.log').open('w') as log:
                    subprocess.run(command, env=dict(os.environ, DOCKER_BUILDKIT='0'), stdout=log, stderr=subprocess.STDOUT, check=True, timeout=7200)
        else:
            require_image(docker, image, packet)
            ensure_volume(docker, volume)
            command = docker + ['run', '--rm', '--name', name, '--label', 'org.paperregistry.owner=' + OWNER,
                                '--gpus', 'device=' + str(args.gpu), '--read-only', '--shm-size=2g',
                                '--tmpfs', '/tmp:rw,size=4g', '--mount', 'type=volume,src=' + volume + ',dst=/cache',
                                '--mount', 'type=bind,src=' + str(output) + ',dst=/results']
            command += ['--network=none'] if args.phase == 'p0' else ['-e', 'HF_HUB_OFFLINE=0', '-e', 'TRANSFORMERS_OFFLINE=0']
            command += [image, 'python3', '/opt/langret/packet/langret_probe.py', args.phase]
            with (output / 'run.log').open('w') as log:
                subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=7200)
        identity = capture(docker + ['image', 'inspect', image, '--format', '{{json .Id}} {{json .RepoDigests}} {{json .Architecture}}'])
        (output / 'execution.json').write_text(json.dumps(dict(command=command, packet_sha256=packet, image=identity, cache_volume=volume, exit_code=0), indent=2))
        return 0
    except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
        (output / 'execution.json').write_text(json.dumps(dict(command=command, packet_sha256=packet, error=str(exc), native_success=False), indent=2))
        print(str(exc))
        return 4
    finally:
        # Only the uniquely named container made by this invocation is eligible for removal.
        own = capture(docker + ['container', 'inspect', name, '--format', '{{index .Config.Labels "org.paperregistry.owner"}}'])
        if own['exit_code'] == 0 and own['stdout'] == OWNER:
            capture(docker + ['rm', '-f', name])


if __name__ == '__main__':
    raise SystemExit(main())
