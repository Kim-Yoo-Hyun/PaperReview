#!/usr/bin/env python3
"""Host control plane only; dependencies, assets, inference and checks run in local Docker."""
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
import sys
import uuid

HERE = Path(__file__).resolve().parent
OWNER = 'paperregistry.feedback-p0'
LABEL = 'org.paperregistry.feedback.packet-sha'


def capture(argv, timeout=25):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return {'argv': argv, 'exit_code': p.returncode, 'stdout': p.stdout.strip(), 'stderr': p.stderr.strip()}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'argv': argv, 'exit_code': None, 'stdout': '', 'stderr': str(exc)}


def resource_reasons(host_os, arch, endpoint, server, overrides):
    reasons = []
    if overrides:
        reasons.append('Docker endpoint/builder overrides must be unset')
    if not endpoint.startswith('unix://'):
        reasons.append('Local Unix Docker endpoint required; remote execution unsupported')
    if host_os != 'Linux' or arch not in ('x86_64', 'amd64'):
        reasons.append('This native packet targets a local Linux x86-64 NVIDIA computer')
    if server.get('OSType') != 'linux' or server.get('Architecture') not in ('amd64', 'x86_64'):
        reasons.append('Linux amd64 daemon required')
    return reasons


def check(gpu_index):
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'host': {'os': platform.system(), 'arch': platform.machine()}, 'commands': [],
              'gpu_allocation_attempted': False, 'native_model_or_simulation_run': False}
    try:
        report['host']['ram_bytes'] = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    except (ValueError, OSError):
        pass
    overrides = [k for k in ['DOCKER_HOST', 'DOCKER_CONTEXT', 'BUILDX_BUILDER', 'BUILDKIT_HOST', 'DOCKER_TLS_VERIFY'] if os.environ.get(k)]
    if overrides or not shutil.which('docker'):
        return dict(report, decision='RESOURCE_UNMET', reasons=['Unset overrides / Docker CLI required'], overrides=overrides)
    ctx = capture(['docker', 'context', 'show'])
    ep = capture(['docker', 'context', 'inspect', '--format', '{{.Endpoints.docker.Host}}'])
    endpoint = ep['stdout']
    ep['stdout'] = endpoint.replace(str(Path.home()), '<user-home>')
    report['commands'].extend([ctx, ep])
    if ctx['exit_code'] != 0 or ep['exit_code'] != 0 or not endpoint.startswith('unix://'):
        return dict(report, decision='RESOURCE_UNMET', reasons=['Local endpoint not established; daemon not contacted'])
    raw = capture(['docker', '--context', ctx['stdout'], 'info', '--format', '{{json .}}'])
    server = {}
    if raw['exit_code'] == 0:
        j = json.loads(raw['stdout'])
        server = {k: j.get(k) for k in ['OSType', 'Architecture', 'MemTotal', 'NCPU', 'ServerVersion', 'OperatingSystem']}
        server['Runtimes'] = sorted(j.get('Runtimes', {}))
    report['commands'].append({'argv': raw['argv'], 'exit_code': raw['exit_code'], 'server': server, 'stderr': raw['stderr']})
    reasons = resource_reasons(platform.system(), platform.machine(), endpoint, server, overrides)
    if raw['exit_code'] != 0:
        reasons.append('Docker daemon unavailable')
    if not reasons:
        gpu = capture(['nvidia-smi', '--query-gpu=index,name,driver_version,memory.total,memory.free', '--format=csv,noheader,nounits'])
        report['commands'].append(gpu)
        try:
            row = next(r for r in csv.reader(gpu['stdout'].splitlines(), skipinitialspace=True) if r[0] == str(gpu_index))
            if tuple(map(int, row[2].split('.'))) < (530, 30, 2):
                reasons.append('Driver below selected CUDA 12.1 GA target 530.30.02')
            # Necessary lower bound only; renderer and activations still need qualification.
            if float(row[4]) * 1024**2 <= 15082474368:
                reasons.append('Free GPU memory does not exceed BF16 actor tensor storage')
            report['selected_gpu'] = {'index': gpu_index, 'name': row[1], 'driver': row[2],
                                      'total_mib': float(row[3]), 'free_mib': float(row[4])}
        except (StopIteration, ValueError, IndexError):
            reasons.append('Selected host NVIDIA GPU/driver metadata unavailable')
    return dict(report, decision='RESOURCE_UNMET' if reasons else 'HOST_ELIGIBLE_CONTAINER_UNVERIFIED',
                reasons=reasons, context=ctx['stdout'])


def fingerprint():
    plan = json.loads((HERE / 'RESUME_PLAN.json').read_text())
    h = hashlib.sha256(json.dumps({k: plan[k] for k in ['contract', 'sources', 'environment']}, sort_keys=True).encode())
    for name in ['Dockerfile', '.dockerignore', 'requirements.txt', 'probe.py', 'resume.py']:
        h.update(name.encode() + b'\0' + (HERE / name).read_bytes())
    return h.hexdigest()


def validate_image(docker, image, expected):
    result = capture(docker + ['image', 'inspect', image, '--format', '{{index .Config.Labels "' + LABEL + '"}}'])
    if result['exit_code'] != 0 or result['stdout'] != expected:
        raise RuntimeError('Missing/stale image; run build for the current packet')


def record_image(docker, image, output):
    result = capture(docker + ['image', 'inspect', image, '--format',
                              '{{json .Id}} {{json .RepoDigests}} {{json .Os}} {{json .Architecture}}'])
    if result['exit_code'] != 0:
        raise RuntimeError('Cannot record native image identity')
    (output / 'image.json').write_text(json.dumps(result, indent=2))


def volume(docker, name):
    result = capture(docker + ['volume', 'inspect', name, '--format', '{{index .Labels "org.paperregistry.owner"}}'])
    if result['exit_code'] == 0:
        if result['stdout'] != OWNER:
            raise RuntimeError('Volume exists but is not owned by this packet')
    else:
        subprocess.run(docker + ['volume', 'create', '--label', 'org.paperregistry.owner=' + OWNER, name], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['check', 'build', 'prepare', 'p0'])
    parser.add_argument('--results', type=Path, required=True, help='New result directory for each command')
    parser.add_argument('--gpu', type=int, default=0)
    args = parser.parse_args()
    if args.gpu < 0:
        parser.error('GPU index must be nonnegative')
    output = args.results.resolve()
    output.mkdir(parents=True, exist_ok=False)
    report = check(args.gpu)
    (output / 'local_check.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    if report['decision'] == 'RESOURCE_UNMET':
        return 3  # No pull/build/download/container attempted after resource rejection.
    if args.phase == 'check':
        return 0
    packet = fingerprint()
    image = 'paper-feedback-p0:' + packet[:16]
    docker = ['docker', '--context', report['context']]
    env = dict(os.environ, DOCKER_BUILDKIT='0')  # Explicit local Engine build; never a remote buildx builder.
    commands = []
    container_name = None
    if args.phase == 'build':
        commands = docker + ['build', '--platform', 'linux/amd64', '--build-arg', 'PACKET_SHA=' + packet,
                             '-t', image, str(HERE)]
    else:
        validate_image(docker, image, packet)
        record_image(docker, image, output)
        name = 'paper-feedback-p0-' + packet[:16]
        volume(docker, name)
        container_name = 'paper-feedback-io-' + uuid.uuid4().hex[:12]
        commands = docker + ['run', '--rm', '--name', container_name, '--pull=never', '--gpus', f'device={args.gpu}',
                             '--network', 'bridge' if args.phase == 'prepare' else 'none', '--shm-size', '2g',
                             '-e', 'NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics',
                             '-e', 'FEEDBACK_PACKET_SHA=' + packet,
                             '-e', 'HF_HUB_OFFLINE=' + ('0' if args.phase == 'prepare' else '1'),
                             '--mount', f'type=volume,source={name},target=/cache',
                             '--mount', f'type=bind,source={output},target=/results',
                             image, 'python3', '/opt/feedback/packet/probe.py', args.phase]
    (output / 'command.json').write_text(json.dumps({'packet_sha': packet, 'argv': commands}, indent=2))
    try:
        with (output / 'execution.log').open('x') as log:
            completed = subprocess.run(commands, stdout=log, stderr=subprocess.STDOUT, env=env)
        if args.phase == 'build' and completed.returncode == 0:
            record_image(docker, image, output)
        (output / 'exit.json').write_text(json.dumps({'exit_code': completed.returncode, 'phase': args.phase,
                                                    'research_effect_measured': False}, indent=2))
        return completed.returncode
    finally:
        if container_name:
            # Only the uniquely named container created by this invocation is eligible for cleanup.
            capture(docker + ['container', 'rm', '-f', container_name])


if __name__ == '__main__':
    sys.exit(main())
