#!/usr/bin/env python3
"""Host stdlib only; package installation and all probes run in local Docker."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import uuid

sys.dont_write_bytecode = True
from config import HERE, manifest, build_context


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def call(argv):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=20)
        return dict(command=argv, returncode=p.returncode, stdout=p.stdout, stderr=p.stderr)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return dict(command=argv, returncode=-1, error=str(exc))


def check(plan, output):
    record = dict(utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                  host=dict(system=platform.system(), machine=platform.machine()),
                  steps=[], native_executed=False, gpu_allocation='NOT_CHECKED')
    def finish(status):
        record['status'] = status
        save(output / 'local_check.json', record)
        return record
    def inspect(argv):
        result = call(argv)
        record['steps'].append(result)
        return result
    if not shutil.which('docker'):
        return finish('BLOCKED_DOCKER_CLI')
    if os.environ.get('DOCKER_HOST'):
        return finish('BLOCKED_DOCKER_HOST_OVERRIDE')
    context = inspect(['docker', 'context', 'show'])
    if context['returncode']:
        return finish('BLOCKED_CONTEXT')
    name = context['stdout'].strip()
    meta = inspect(['docker', 'context', 'inspect', name])
    try:
        endpoint = json.loads(meta['stdout'])[0]['Endpoints']['docker']['Host']
    except (KeyError, IndexError, ValueError):
        return finish('BLOCKED_CONTEXT_METADATA')
    record.update(context=name, endpoint=endpoint)
    if not endpoint.startswith('unix://'):
        return finish('BLOCKED_NONLOCAL_ENDPOINT')
    info = inspect(['docker', '--context', name, 'info', '--format', '{{json .}}'])
    if info['returncode']:
        return finish('BLOCKED_DAEMON')
    try:
        data = json.loads(info['stdout'])
    except ValueError:
        return finish('BLOCKED_DAEMON_METADATA')
    record['daemon'] = {k: data.get(k) for k in ('OSType', 'Architecture', 'MemTotal', 'ServerVersion')}
    if platform.system() != 'Linux' or platform.machine() not in ('x86_64', 'AMD64'):
        return finish('BLOCKED_HOST_PLATFORM')
    if data.get('OSType') != 'linux' or data.get('Architecture') not in ('x86_64', 'amd64'):
        return finish('BLOCKED_DAEMON_PLATFORM')
    if data.get('MemTotal', 0) < plan['hardware']['minimum_docker_ram_gib'] * 2**30:
        return finish('BLOCKED_DOCKER_RAM')
    return finish('LOCAL_METADATA_READY')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=('check', 'run'))
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    plan = manifest()
    output = (args.output or HERE / 'runs' / (dt.datetime.now().strftime('%Y%m%d-%H%M%S') + '-' + uuid.uuid4().hex[:6])).resolve()
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise SystemExit('Choose a new empty output directory; existing results are preserved')
    output.mkdir(parents=True, exist_ok=True)
    local = check(plan, output)
    print(local['status'], str(output), flush=True)
    if local['status'] != 'LOCAL_METADATA_READY' or args.mode == 'check':
        return 0 if local['status'] == 'LOCAL_METADATA_READY' else 3
    save(output / 'resolved_plan.json', plan)
    docker = ['docker', '--context', local['context']]
    active, stages = set(), []
    stamp = uuid.uuid4().hex[:10]
    report = dict(status='STARTED', stages=stages, scope=plan['claim_boundary'])

    def stream(argv, label):
        print(label, flush=True)
        with (output / (label + '.log')).open('w') as log:
            proc = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            try:
                for line in proc.stdout:
                    log.write(line); log.flush(); print(line, end='', flush=True)
                rc = proc.wait()
            finally:
                if proc.poll() is None:
                    proc.terminate()
                    try: proc.wait(timeout=10)
                    except subprocess.TimeoutExpired: proc.kill(); proc.wait()
        stages.append(dict(stage=label, returncode=rc))
        save(output / 'launcher_result.json', report)
        if rc:
            raise RuntimeError(label + ' failed: ' + str(rc))

    def container(image, command, label, network=False, cache=False, gpu=True):
        name = 'task-geometry-' + stamp + '-' + label
        active.add(name)
        argv = docker + ['run', '--rm', '--name', name, '--label', plan['label'],
                         '--platform', plan['platform'], '--network', 'bridge' if network else 'none',
                         '--shm-size', '2g', '-e', 'NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics',
                         '--mount', 'type=bind,src=' + str(output) + ',dst=/out']
        if gpu: argv += ['--gpus', 'all']
        if cache: argv += ['--mount', 'type=volume,src=' + plan['cache_volume'] + ',dst=/cache']
        stream(argv + [image] + command, label)
        active.discard(name)

    try:
        gpu = ('import torch,json; assert torch.cuda.is_available(); p=torch.cuda.get_device_properties(0); '
               'print(json.dumps(dict(name=p.name,memory=p.total_memory,major=p.major,cuda=torch.version.cuda))); '
               'assert p.major>=8 and p.total_memory>=' + str(plan['hardware']['minimum_gpu_vram_gib'] * 2**30) + '; '
               'assert torch.cuda.is_bf16_supported()')
        container(plan['base_image'], ['python', '-c', gpu], 'gpu')
        with tempfile.TemporaryDirectory(prefix='task-geometry-build-') as temp:
            build_context(Path(temp))
            stream(docker + ['build', '--platform', plan['platform'], '--label', plan['label'],
                             '-t', plan['image'], temp], 'build')
        container(plan['image'], ['python', 'checks.py'], 'checks', gpu=False)
        container(plan['image'], ['python', 'probe.py', 'environment', '--output', '/out'], 'environment', cache=True)
        # Verify EGL/scene before fetching eight GB of weights.
        container(plan['image'], ['python', 'probe.py', 'scene', '--output', '/out'], 'scene', cache=True)
        container(plan['image'], ['python', 'probe.py', 'fetch', '--output', '/out'], 'fetch', network=True, cache=True)
        container(plan['image'], ['python', 'probe.py', 'vla', '--output', '/out'], 'vla', cache=True)
        report['status'] = 'P0_INPUT_PATH_PASSED_NO_TASK_EFFECT_CLAIM'
        save(output / 'image_inspect.json', call(docker + ['image', 'inspect', plan['image']]))
        return 0
    except (RuntimeError, OSError, KeyboardInterrupt) as exc:
        report.update(status='STOPPED', reason=str(exc))
        return 4
    finally:
        report['cleanup'] = [call(docker + ['rm', '-f', name]) for name in sorted(active)]
        report['retained_assets'] = dict(image=plan['image'], cache_volume=plan['cache_volume'], reason='Reusable preparation; no broad prune')
        save(output / 'launcher_result.json', report)


if __name__ == '__main__':
    sys.exit(main())
