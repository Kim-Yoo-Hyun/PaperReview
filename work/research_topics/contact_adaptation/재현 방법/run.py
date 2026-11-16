#!/usr/bin/env python3
"""Host stdlib Docker orchestration only. Never import simulation on the host."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import uuid

HERE = Path(__file__).resolve().parent
PACKET_FILES = ('Dockerfile', '.dockerignore', 'P0_PLAN.json', 'run.py', 'probe.py', 'test_p0.py')


def fingerprint(root=HERE):
    hashes = {n: hashlib.sha256((root / n).read_bytes()).hexdigest() for n in PACKET_FILES}
    return hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest(), hashes


def local_endpoint(endpoint):
    return endpoint.startswith('unix://') and len(endpoint) > len('unix://')


def compatible(info, host_system, host_machine):
    return (host_system == 'Linux' and host_machine in ('x86_64', 'amd64')
            and info.get('OSType') == 'linux'
            and info.get('Architecture') in ('x86_64', 'amd64'))


class Launcher:
    def __init__(self, output, cache_volume='paper-contact-p0-cache-v1'):
        if not re.fullmatch(r'paper-contact-p0-[a-zA-Z0-9_.-]+', cache_volume):
            raise ValueError('Cache volume must use the paper-contact-p0- prefix')
        self.cache_volume = cache_volume
        self.output = output
        output.mkdir(parents=True, exist_ok=False)
        self.plan = json.loads((HERE / 'P0_PLAN.json').read_text())
        self.fp, self.hashes = fingerprint()
        self.image = 'paper-contact-p0:' + self.fp[:16]
        self.events = []
        self.prefix = ['docker']

    def cmd(self, args, timeout=30):
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
            event = dict(args=args, exit_code=r.returncode, stdout=r.stdout, stderr=r.stderr)
        except subprocess.TimeoutExpired:
            event = dict(args=args, exit_code=124, stdout='', stderr='process timeout')
        self.events.append(event)
        return event

    def require(self, args, timeout=30):
        r = self.cmd(args, timeout)
        if r['exit_code']:
            raise RuntimeError(f"command exit {r['exit_code']}: {r['stderr'][-1500:]}")
        return r['stdout']

    def check(self):
        # Pin a local context explicitly for ALL later Docker commands. A remote
        # DOCKER_HOST must not bypass the user's local-Docker constraint.
        env_host = os.environ.get('DOCKER_HOST', '')
        if env_host and not local_endpoint(env_host):
            raise RuntimeError('Remote DOCKER_HOST is not allowed')
        ctx = self.require(['docker', 'context', 'show']).strip()
        record = json.loads(self.require(['docker', 'context', 'inspect', ctx]))[0]
        endpoint = record['Endpoints']['docker']['Host']
        if not local_endpoint(endpoint) or (env_host and env_host != endpoint):
            raise RuntimeError('Choose one unambiguous local unix Docker context')
        self.prefix = ['docker', '--context', ctx]
        info = json.loads(self.require(self.prefix + ['info', '--format', '{{json .}}']))
        self.host = dict(system=platform.system(), machine=platform.machine(), context=ctx,
                         endpoint=endpoint, daemon_arch=info.get('Architecture'),
                         daemon_memory_bytes=info.get('MemTotal'), daemon_cpus=info.get('NCPU'),
                         daemon_version=info.get('ServerVersion'))
        if not compatible(info, platform.system(), platform.machine()):
            raise RuntimeError('Selected packet requires local Linux x86-64/NVIDIA Docker; no emulation fallback')
        # Allocation probe: no simulator or weights, at most 120 seconds.
        self.gpu = self.container(self.plan['base_image'],
                                  ['nvidia-smi', '--query-gpu=name,driver_version,memory.total',
                                   '--format=csv,noheader'], timeout=120, entrypoint='nvidia-smi',
                                  strip_first=True, mounts=False, pull='missing')
        if self.gpu['exit_code']:
            raise RuntimeError('NVIDIA allocation/device query failed; see command log')

    def container(self, image, command, timeout, entrypoint=None, strip_first=False,
                  mounts=True, network='none', pull='never'):
        name = 'paper-contact-p0-' + uuid.uuid4().hex[:12]
        args = self.prefix + ['run', '--rm', '--name', name, '--pull=' + pull,
                              '--label', 'paper.task=contact-p0', '--gpus', 'all',
                              '--network', network, '--env', 'NVIDIA_DRIVER_CAPABILITIES=compute,utility']
        if mounts:
            # Installation/assets/cache stay in image or Docker volume. Only
            # result files go to the host; the source packet is read-only.
            args += ['--mount', f'type=bind,src={HERE},dst=/packet,readonly',
                     '--mount', f'type=bind,src={self.output},dst=/results',
                     '--mount', f'type=volume,src={self.cache_volume},dst=/cache',
                     '--env', 'CONTACT_P0_FINGERPRINT=' + self.fp,
                     '--env', 'CONTACT_P0_IMAGE_ID=' + self.image_id]
        if entrypoint:
            args += ['--entrypoint', entrypoint]
        args += [image] + (command[1:] if strip_first else command)
        try:
            return self.cmd(args, timeout)
        finally:
            # Exact, task-created UUID name only. Never prune user containers.
            check = subprocess.run(self.prefix + ['inspect', '--format',
                                   '{{index .Config.Labels "paper.task"}}', name],
                                   capture_output=True, text=True, timeout=15)
            if check.returncode == 0 and check.stdout.strip() == 'contact-p0':
                self.cmd(self.prefix + ['rm', '-f', name])

    def run(self, stage):
        self.check()
        if stage == 'check':
            return
        if stage == 'build':
            self.require(self.prefix + ['build', '--platform', 'linux/amd64',
                         '--build-arg', 'PACKET_FINGERPRINT=' + self.fp,
                         '--tag', self.image, str(HERE)], timeout=3600)
            return
        image = json.loads(self.require(self.prefix + ['image', 'inspect', self.image]))[0]
        if image.get('Config', {}).get('Labels', {}).get('paper.contact.packet') != self.fp:
            raise RuntimeError('Stale image: rebuild this exact packet')
        if image.get('Architecture') != 'amd64' or image.get('Os') != 'linux':
            raise RuntimeError('Wrong native image architecture')
        self.image_id = image['Id']
        result = self.container(self.image, [stage],
                                timeout=1800, network='bridge' if stage == 'prepare' else 'none')
        if result['exit_code']:
            raise RuntimeError(f"{stage} exit {result['exit_code']}; see container output")

    def save(self, stage, error):
        record = dict(stage=stage, status='FAILED_OR_BLOCKED' if error else 'COMMAND_COMPLETE',
                      error=error, created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                      packet_fingerprint=self.fp, packet_files=self.hashes,
                      host=getattr(self, 'host', None), image=self.image, cache_volume=self.cache_volume,
                      commands=self.events, policy_queries=0, optimizer_updates=0)
        (self.output / 'launcher.json').write_text(json.dumps(record, indent=2) + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('stage', choices=['check', 'build', 'prepare', 'p0'])
    ap.add_argument('--output', type=Path, help='New result directory; never overwrite an existing run')
    ap.add_argument('--cache-volume', default='paper-contact-p0-cache-v1', help='Docker volume with paper-contact-p0- prefix')
    args = ap.parse_args()
    output = args.output or HERE / 'runs' / (dt.datetime.now().strftime('%Y%m%d_%H%M%S_') + uuid.uuid4().hex[:6])
    launcher = Launcher(output.resolve(), args.cache_volume)
    error = None
    try:
        launcher.run(args.stage)
    except Exception as exc:
        error = str(exc)
    finally:
        launcher.save(args.stage, error)
    print(json.dumps({'stage': args.stage, 'error': error, 'results': str(launcher.output)}, ensure_ascii=False))
    return 3 if error else 0


if __name__ == '__main__':
    sys.exit(main())
