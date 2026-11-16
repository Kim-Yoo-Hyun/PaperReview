#!/usr/bin/env python3
"""Host control plane only. All payload acquisition/model/simulator work uses local Docker."""
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

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'work/sources/vla_rl_gap_review_2026-11-03.json'
BASE = 'nvidia/cuda@sha256:2d205a50fefc321aca51a1d3aa46fb9a633dd2509a10e28c8bd34a6cb2027619'


def capture(argv):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=20)
        return {'argv': argv, 'exit_code': p.returncode, 'stdout': p.stdout.strip(), 'stderr': p.stderr.strip()}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'argv': argv, 'exit_code': None, 'stdout': '', 'stderr': str(exc)}


def resource_reasons(host_os, host_arch, endpoint, server, overrides):
    reasons = []
    if overrides:
        reasons.append('DOCKER_HOST/DOCKER_CONTEXT overrides must be unset; use an explicitly selected local context')
    if not endpoint.startswith('unix://'):
        reasons.append('Local Unix Docker endpoint required; SSH/TCP endpoints are outside this packet')
    if host_os != 'Linux' or host_arch not in ('x86_64', 'amd64'):
        reasons.append('Initial packet targets a local Linux x86-64 host')
    if server.get('OSType') != 'linux' or server.get('Architecture') not in ('x86_64', 'amd64'):
        reasons.append('Linux amd64 Docker daemon required')
    return reasons


def check(gpu_index=0):
    info = {'host': {'os': platform.system(), 'architecture': platform.machine()}, 'commands': []}
    info['overrides'] = [k for k in ('DOCKER_HOST', 'DOCKER_CONTEXT', 'BUILDX_BUILDER', 'BUILDKIT_HOST') if os.environ.get(k)]
    try:
        info['host']['ram_bytes'] = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    except (ValueError, OSError):
        pass
    info['repository_filesystem_free_bytes'] = shutil.disk_usage(ROOT).free
    if not shutil.which('docker'):
        return dict(info, decision='RESOURCE_UNMET', reasons=['Docker CLI unavailable'])
    # Do not contact an overridden endpoint, which could be remote.
    if info['overrides']:
        return dict(info, decision='RESOURCE_UNMET', reasons=['Unset Docker endpoint/builder overrides before checking'])
    context = capture(['docker', 'context', 'show'])
    endpoint = capture(['docker', 'context', 'inspect', '--format', '{{.Endpoints.docker.Host}}'])
    endpoint_value = endpoint['stdout']
    # Retain only an endpoint template in portable evidence.
    endpoint['stdout'] = endpoint_value.replace(str(Path.home()), '<user-home>')
    info['commands'].extend([context, endpoint])
    if endpoint['exit_code'] != 0 or not endpoint_value.startswith('unix://'):
        return dict(info, decision='RESOURCE_UNMET', reasons=['Local Unix endpoint not established; daemon not contacted'])
    raw = capture(['docker', 'info', '--format', '{{json .}}'])
    server = {}
    if raw['exit_code'] == 0:
        data = json.loads(raw['stdout'])
        server = {k: data.get(k) for k in ('OSType', 'Architecture', 'NCPU', 'MemTotal', 'ServerVersion', 'OperatingSystem')}
        server['Runtimes'] = sorted(data.get('Runtimes') or {})
    info['commands'].append({'argv': raw['argv'], 'exit_code': raw['exit_code'], 'selected_fields': server, 'stderr': raw['stderr']})
    reasons = resource_reasons(platform.system(), platform.machine(), endpoint_value, server, info['overrides'])
    if raw['exit_code'] != 0:
        reasons.append('Docker daemon unavailable')
    if not reasons:
        gpu = capture(['nvidia-smi', '--query-gpu=index,name,driver_version,memory.total,memory.free', '--format=csv,noheader,nounits'])
        info['commands'].append(gpu)
        if gpu['exit_code'] != 0 or not gpu['stdout']:
            reasons.append('Host NVIDIA GPU/driver metadata unavailable; no container download attempted')
        else:
            rows = list(csv.reader(gpu['stdout'].splitlines(), skipinitialspace=True))
            selected = [row for row in rows if row[0].strip() == str(gpu_index)]
            if len(selected) != 1:
                reasons.append('Requested NVIDIA GPU index not found')
            else:
                row = selected[0]
                try:
                    version = tuple(int(n) for n in row[2].strip().split('.'))
                    if version < (550, 54, 14):
                        reasons.append('Driver below scoped CUDA 12.4 GA target 550.54.14')
                    # Necessary lower bound only; encoder/activation/renderer headroom remains unqualified.
                    if float(row[3]) * 1024**2 <= 15082474368:
                        reasons.append('GPU total memory does not exceed one BF16 base tensor storage')
                    info['selected_gpu'] = {'index': gpu_index, 'name': row[1], 'driver': row[2],
                                            'total_mib': float(row[3]), 'free_mib': float(row[4]),
                                            'native_memory_qualified': False}
                except (ValueError, IndexError):
                    reasons.append('Could not parse selected NVIDIA GPU metadata')
    info.update(decision='RESOURCE_UNMET' if reasons else 'HOST_ELIGIBLE_CONTAINER_GPU_UNVERIFIED', reasons=reasons,
                gpu_allocation_attempted=False, cuda_or_egl_verified=False)
    return info


def fingerprint():
    h = hashlib.sha256()
    for p in [HERE / n for n in ('Dockerfile', 'requirements.txt', 'native_p0.py', 'resume.py')] + [LEDGER]:
        h.update(p.name.encode() + b'\0' + p.read_bytes())
    return h.hexdigest()


def require_fresh_image(image, packet_sha):
    r = capture(['docker', 'image', 'inspect', image, '--format', '{{index .Config.Labels "org.paperregistry.vrl.packet-sha"}}'])
    if r['exit_code'] != 0 or r['stdout'] != packet_sha:
        raise RuntimeError('Missing/stale image: run build with this packet before prepare/p0')
    r = capture(['docker', 'image', 'inspect', image, '--format', '{{.Id}}'])
    if r['exit_code'] != 0:
        raise RuntimeError(r['stderr'])
    return r['stdout']


def run_logged(argv, log_path):
    print('Executing:', json.dumps(argv, ensure_ascii=False), flush=True)
    # Preserve the exact failing stage without retrying or overwriting prior logs.
    with log_path.open('x') as log:
        p = subprocess.run(argv, stdout=log, stderr=subprocess.STDOUT)
    if p.returncode:
        raise RuntimeError(f'Exit {p.returncode}; inspect {log_path}')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase', choices=['check', 'build', 'prepare', 'p0'])
    ap.add_argument('--results', type=Path, help='New/existing result directory; phase evidence is never overwritten')
    ap.add_argument('--gpu', type=int, default=0, help='One NVIDIA device index, default 0')
    args = ap.parse_args()
    if args.gpu < 0:
        ap.error('GPU index must be nonnegative')
    report = check(args.gpu)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report['decision'] == 'RESOURCE_UNMET':
        return 3
    if args.phase == 'check':
        return 0  # Host eligibility only; never a native qualification pass.
    if not args.results:
        ap.error('--results is required for build/prepare/p0')
    results = args.results.resolve()
    if ',' in str(ROOT) or ',' in str(results):
        ap.error('Docker bind paths containing commas are not supported')
    results.mkdir(parents=True, exist_ok=True)
    evidence = results / (args.phase + '-host.json')
    if evidence.exists() or (results / (args.phase + '.json')).exists():
        ap.error('Phase evidence already exists; inspect it and choose a new result directory for a deliberate retry')
    digest = fingerprint()
    image = 'paper-vrl-p0:' + digest[:16]
    report.update(packet_sha256=digest, phase=args.phase, image=image, native_result_verified=False)
    evidence.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    try:
        if args.phase == 'build':
            # Only on an eligible local target; no numerical benchmark or policy inference.
            run_logged(['docker', 'run', '--rm', '--gpus', f'device={args.gpu}', '--network', 'none', BASE,
                        'nvidia-smi', '--query-gpu=name,driver_version,memory.total', '--format=csv'], results / 'gpu-allocation.log')
            ledger = json.loads(LEDGER.read_text())
            plan = json.loads((HERE / 'RESUME_PLAN.json').read_text())
            run_logged(['docker', 'build', '--platform', 'linux/amd64', '--label', 'org.paperregistry.task=vrl-p0',
                        '--build-arg', 'VRL_PACKET_SHA=' + digest,
                        '--build-arg', 'VRL_SOURCE_SHA=' + plan['setup_source_audit']['commit'],
                        '--build-arg', 'LIBERO_SOURCE_SHA=' + ledger['r2_review']['comparison_contract']['task']['libero_commit'],
                        '-t', image, str(HERE)], results / 'build.log')
            report['image_id'] = require_fresh_image(image, digest)
        else:
            report['image_id'] = require_fresh_image(image, digest)
            ledger_in_container = '/workspace/' + str(LEDGER.relative_to(ROOT))
            command = ['docker', 'run', '--rm', '--gpus', f'device={args.gpu}', '--shm-size', '2g',
                       '--label', 'org.paperregistry.task=vrl-p0',
                       '--mount', f'type=bind,source={ROOT},target=/workspace,readonly',
                       '--mount', f'type=bind,source={results},target=/results',
                       '--mount', 'type=volume,source=vrl_update_cache,target=/cache',
                       '-e', 'VRL_IMAGE_ID=' + report['image_id'], '-e', 'VRL_PACKET_SHA=' + digest]
            if args.phase == 'p0':
                command += ['--network', 'none', '-e', 'HF_HUB_OFFLINE=1', '-e', 'TRANSFORMERS_OFFLINE=1']
            command += [image, 'python3', '/opt/vrl/native_p0.py', args.phase, '--ledger', ledger_in_container]
            run_logged(command, results / (args.phase + '.log'))
        report['phase_exit'] = 0
    except Exception as exc:
        report.update(phase_exit=1, error=str(exc))
        print(str(exc), file=sys.stderr)
        return 1
    finally:
        evidence.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
