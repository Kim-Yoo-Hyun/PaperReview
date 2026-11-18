#!/usr/bin/env python3
"""Host stdlib orchestration only. No model/simulator import or payload download."""
import argparse
import csv
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
OWNER = 'relation-p0'
FILES = ('PLAN.json', 'Dockerfile', '.dockerignore', 'resume.py', 'probe.py', 'actor.py', 'test_contract.py')


def capture(argv, timeout=30):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return {'argv': argv, 'exit_code': p.returncode, 'stdout': p.stdout.strip(), 'stderr': p.stderr.strip()}
    except (OSError, subprocess.TimeoutExpired) as e:
        return {'argv': argv, 'exit_code': None, 'stdout': '', 'stderr': str(e)}


def fingerprint():
    h = hashlib.sha256()
    for name in FILES:
        h.update(name.encode() + b'\0' + (HERE / name).read_bytes())
    return h.hexdigest()


def check(plan, gpu):
    out = {'host': {'os': platform.system(), 'arch': platform.machine()}, 'commands': [], 'native_runs': 0}
    if any(os.environ.get(k) for k in ('DOCKER_HOST', 'DOCKER_CONTEXT', 'BUILDX_BUILDER', 'BUILDKIT_HOST', 'DOCKER_TLS_VERIFY')):
        return dict(out, status='BLOCKED_OVERRIDE', reason='Unset Docker/builder overrides; select a local Unix context')
    if not shutil.which('docker'):
        return dict(out, status='BLOCKED_CLI')
    ctx = capture(['docker', 'context', 'show'])
    out['commands'].append(ctx)
    if ctx['exit_code'] != 0:
        return dict(out, status='BLOCKED_CONTEXT')
    docker = ['docker', '--context', ctx['stdout']]
    ep = capture(['docker', 'context', 'inspect', ctx['stdout'], '--format', '{{.Endpoints.docker.Host}}'])
    out['commands'].append(ep)
    if ep['exit_code'] != 0 or not ep['stdout'].startswith('unix://'):
        return dict(out, status='BLOCKED_NONLOCAL')
    raw = capture(docker + ['info', '--format', '{{json .}}'])
    out['commands'].append({'argv': raw['argv'], 'exit_code': raw['exit_code'], 'stderr': raw['stderr']})
    out['context'] = ctx['stdout']
    if raw['exit_code'] != 0:
        return dict(out, status='BLOCKED_DAEMON', server=None, gpu=None)
    info = json.loads(raw['stdout'])
    out['server'] = {k: info.get(k) for k in ('OSType', 'Architecture', 'MemTotal', 'NCPU', 'ServerVersion')}
    if platform.system() != 'Linux' or platform.machine() not in ('x86_64', 'amd64') or info.get('Architecture') not in ('x86_64', 'amd64') or info.get('OSType') != 'linux':
        return dict(out, status='BLOCKED_PLATFORM')
    if info.get('MemTotal', 0) < plan['resources']['daemon_ram_floor_gib'] * 1024**3:
        return dict(out, status='BLOCKED_RAM')
    smi = capture(['nvidia-smi', '--query-gpu=index,uuid,name,driver_version,memory.free', '--format=csv,noheader,nounits'])
    out['commands'].append(smi)
    try:
        if smi['exit_code'] != 0:
            raise ValueError('nvidia-smi failed')
        row = next(r for r in csv.reader(smi['stdout'].splitlines(), skipinitialspace=True) if int(r[0]) == gpu)
        out['gpu'] = dict(index=gpu, uuid=row[1], name=row[2], driver=row[3], free_mib=float(row[4]))
        if float(row[4]) < plan['resources']['free_vram_floor_mib']:
            return dict(out, status='BLOCKED_VRAM')
    except (ValueError, IndexError, StopIteration):
        return dict(out, status='BLOCKED_NVIDIA')
    return dict(out, status='HOST_ELIGIBLE_CONTAINER_UNVERIFIED')


def write_report(path, obj):
    # Keep personal paths out of committed/exported diagnostics.
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2).replace(str(Path.home()), '<user-home>') + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase', choices=('check', 'build', 'control', 'prepare', 'p0', 'run'))
    ap.add_argument('--results', required=True, type=Path, help='New directory for this invocation')
    ap.add_argument('--gpu', type=int, default=0)
    ap.add_argument('--backward', action='store_true', help='Optional single gradient check, no optimizer')
    args = ap.parse_args()
    if args.gpu < 0 or ',' in str(args.results.resolve()):
        ap.error('Nonnegative GPU index and comma-free result path required')
    output = args.results.resolve()
    output.mkdir(parents=True, exist_ok=False)
    plan = json.loads((HERE / 'PLAN.json').read_text())
    report = check(plan, args.gpu)
    packet = fingerprint()
    report['packet_sha256'] = packet
    write_report(output / 'local_check.json', report)
    print(json.dumps({'status': report['status'], 'packet': packet}))
    if report['status'] != 'HOST_ELIGIBLE_CONTAINER_UNVERIFIED':
        return 3
    if args.phase == 'check':
        return 0
    docker = ['docker', '--context', report['context']]
    image = 'paper-relation-p0:' + packet[:16]
    volume = 'paper-relation-cache-' + hashlib.sha256((plan['model']['revision'] + plan['assets']['revision']).encode()).hexdigest()[:12]
    # Socket-local daemon does not by itself prove free space on its storage mount.
    disk = capture(docker + ['info', '--format', '{{.DockerRootDir}}'])
    if disk['exit_code'] != 0 or not Path(disk['stdout']).exists():
        raise RuntimeError('Cannot inspect local DockerRootDir free space; no downloads started')
    if shutil.disk_usage(disk['stdout']).free < plan['resources']['free_disk_floor_gib'] * 1024**3:
        raise RuntimeError('Insufficient Docker storage for the selected preparation floor')
    active_name = None
    commands = []
    image_identity = None

    def run_container(img, argv, network='none', cache=True, timeout=1800):
        nonlocal active_name
        active_name = 'paper-relation-' + uuid.uuid4().hex[:12]
        cmd = docker + ['run', '--rm', '--name', active_name, '--label', 'org.paperregistry.owner=' + OWNER,
                        '--gpus', 'device=' + report['gpu']['uuid'], '--network=' + network, '--shm-size=2g',
                        '--memory=32g', '--pids-limit=512', '-e', 'NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics',
                        '-e', 'RELATION_IN_DOCKER=1', '-e', 'RELATION_GPU_UUID=' + report['gpu']['uuid'],
                        '-e', 'RELATION_PACKET_SHA=' + packet,
                        '--mount', 'type=bind,src=' + str(output) + ',dst=/results']
        if cache:
            cmd += ['--mount', 'type=volume,src=' + volume + ',dst=/cache']
        cmd += [img] + argv
        commands.append(cmd)
        log_path = output / ('container-' + str(len(commands)) + '.log')
        with log_path.open('w') as log:
            subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=timeout)
        active_name = None
        return log_path

    try:
        if args.phase in ('build', 'run'):
            # The selected base image is needed by the build; verify allocation before dependency installation.
            allocation_log = run_container(plan['base_image'], ['nvidia-smi', '--query-gpu=uuid', '--format=csv,noheader'], cache=False)
            # Docker may prepend pull messages. Require exactly the selected UUID among GPU rows.
            seen = [line.strip() for line in allocation_log.read_text().splitlines() if line.strip().startswith('GPU-')]
            if seen != [report['gpu']['uuid']]:
                raise RuntimeError('GPU allocation mismatch; dependency build not started')
            cmd = docker + ['build', '--platform=linux/amd64', '--force-rm', '--build-arg', 'PACKET_SHA=' + packet,
                            '-t', image, str(HERE)]
            commands.append(cmd)
            with (output / 'build.log').open('w') as log:
                subprocess.run(cmd, env=dict(os.environ, DOCKER_BUILDKIT='0'), stdout=log, stderr=subprocess.STDOUT, check=True, timeout=7200)
        label = capture(docker + ['image', 'inspect', image, '--format', '{{index .Config.Labels "org.paperregistry.packet"}}'])
        if label['exit_code'] != 0 or label['stdout'] != packet:
            raise RuntimeError('Image missing/stale: build this packet first')
        image_identity = capture(docker + ['image', 'inspect', image, '--format', '{{json .Id}}'])
        if image_identity['exit_code'] != 0:
            raise RuntimeError('Cannot record built image ID')
        if args.phase == 'build':
            return 0
        vol = capture(docker + ['volume', 'inspect', volume, '--format', '{{index .Labels "org.paperregistry.owner"}}'])
        if vol['exit_code'] == 0 and vol['stdout'] != OWNER:
            raise RuntimeError('Refusing unrelated cache volume')
        if vol['exit_code'] != 0:
            subprocess.run(docker + ['volume', 'create', '--label', 'org.paperregistry.owner=' + OWNER, volume], check=True)
        if args.phase in ('control', 'run'):
            run_container(image, [plan['python']['actor'], '/opt/relation/test_contract.py'])
        if args.phase in ('prepare', 'run'):
            run_container(image, [plan['python']['actor'], '/opt/relation/probe.py', 'environment'])
            run_container(image, [plan['python']['actor'], '/opt/relation/probe.py', 'prepare'], network='bridge', timeout=7200)
        if args.phase in ('p0', 'run'):
            run_container(image, [plan['python']['actor'], '/opt/relation/probe.py', 'environment'])
            cmd = [plan['python']['simulator'], '/opt/relation/probe.py', 'p0']
            if args.backward:
                cmd += ['--backward']
            run_container(image, cmd, timeout=1800)
        return 0
    finally:
        # Only our unique active container; never prune user images/volumes.
        if active_name:
            subprocess.run(docker + ['rm', '-f', active_name], capture_output=True, timeout=30)
        write_report(output / 'launcher.json', {'packet': packet, 'image': image, 'image_identity': image_identity,
                                              'cache_volume': volume, 'commands': commands})


if __name__ == '__main__':
    sys.exit(main())
