"""Fetch pinned text/metadata into Docker scratch space, without installation."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path('/tmp/c2')
ROBOFOLLOW = 'f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8'
ROBOTWIN = '6dde57155eafa3e4ebf6ad1f93a7cf7d5d41a755'
DATASET = 'bbb1e266ed585f1557773de5a3f1e3b4cd944f97'


def main():
    entries = [('dataset.txt', f'https://huggingface.co/api/datasets/AutoLab-SJTU/robofollow-data/revision/{DATASET}')]
    for p in ['README.md', 'PI05.md', 'collect.py', 'scene_sources/scene3.py', 'evaluation/scene3.py',
              'requirements-core.txt', 'protocol.yml', 'episodes.py', 'routes.py', 'runinfo.py']:
        entries.append(('sources/' + p, f'https://raw.githubusercontent.com/AutoLab-SAI-SJTU/RoboFollow/{ROBOFOLLOW}/{p}'))
    for p in ['scripts/requirements.txt', 'scripts/_install.sh']:
        entries.append(('sources/robotwin/' + p, f'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/{ROBOTWIN}/{p}'))
    evidence = []
    for target, url in entries:
        with urllib.request.urlopen(url, timeout=45) as response:
            data = response.read()
        path = ROOT / target
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        evidence.append({'relative_cache_path': target, 'url': url, 'bytes': len(data),
                         'sha256': hashlib.sha256(data).hexdigest()})
    out = ROOT / 'out'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'source_manifest.json').write_text(json.dumps({'sources': evidence,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}, indent=2) + '\n')
    print('Pinned source/metadata records:', len(evidence))


if __name__ == '__main__':
    if not Path('/.dockerenv').exists():
        raise SystemExit('Run preparation inside Docker')
    main()
