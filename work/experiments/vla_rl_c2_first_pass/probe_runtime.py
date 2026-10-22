"""Docker-only package/device gate. Does not execute a policy or simulator."""
import ctypes
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time
import urllib.request

ROOT = Path('/tmp/c2')
OUT = ROOT / 'out'
OUT.mkdir(parents=True, exist_ok=True)


def query(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    return json.loads(data), hashlib.sha256(data).hexdigest()


def main():
    report = {'platform': platform.platform(), 'machine': platform.machine(),
              'python': sys.version, 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'device_paths': {p: Path(p).exists() for p in ['/dev/nvidia0', '/dev/nvidiactl', '/dev/dri']},
              'pip_probes': [], 'pypi_releases': {}, 'checkpoint_discovery': []}
    try:
        ctypes.CDLL('libcuda.so.1')
        report['cuda_driver_library'] = 'loaded'
    except OSError as exc:
        report['cuda_driver_library'] = str(exc)
    for package in ['sapien==3.0.0b1', 'mplib==0.2.1']:
        command = [sys.executable, '-m', 'pip', 'install', '--dry-run', '--no-deps',
                   '--only-binary=:all:', '--disable-pip-version-check', package]
        start = time.monotonic()
        proc = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
        report['pip_probes'].append({'command': command, 'returncode': proc.returncode,
                                     'output': proc.stdout, 'elapsed_seconds': time.monotonic() - start})
        name, version = package.split('==')
        url = f'https://pypi.org/pypi/{name}/{version}/json'
        data, sha = query(url)
        report['pypi_releases'][package] = {'url': url, 'response_sha256': sha,
            'distribution_files': [{'filename': x['filename'], 'sha256': x['digests']['sha256'],
                                     'size': x['size'], 'packagetype': x['packagetype']} for x in data['urls']]}
        print(package, 'resolver exit', proc.returncode, flush=True)
    for url in ['https://huggingface.co/api/models?search=RoboFollow&limit=100',
                'https://huggingface.co/api/models?author=AutoLab-SJTU&limit=100',
                'https://api.github.com/repos/AutoLab-SAI-SJTU/RoboFollow/releases']:
        try:
            data, sha = query(url)
            report['checkpoint_discovery'].append({'url': url, 'response_sha256': sha,
                'results': [x.get('id', x.get('tag_name')) for x in data]})
        except Exception as exc:
            report['checkpoint_discovery'].append({'url': url, 'error': str(exc)})
    report['limitations'] = [
        'Only the reference binary package route is tested; custom source builds/CPU ports are not disproved.',
        'Checkpoint API search is discovery, not proof that no checkpoint exists anywhere.',
        'No simulator assets, neural weights, policy inference, training, or episode rollout were run.'
    ]
    (OUT / 'runtime_probe.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['machine', 'device_paths', 'cuda_driver_library', 'checkpoint_discovery']}, indent=2))


if __name__ == '__main__':
    if not Path('/.dockerenv').exists():
        raise SystemExit('Run this gate inside Docker')
    main()
