"""Docker-only asset verification and bounded orchestration; unbuilt recipe."""
import base64
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import socket
import subprocess
import sys
import time
import urllib.request
import zipfile

from packet_checks import classify_probe, verify_recipe

if not Path('/.dockerenv').exists():
    raise SystemExit('Docker only')

PLAN = json.loads(Path('/recipe/RESUME_PLAN.json').read_text())
ART = json.loads(Path('/recipe/ARTIFACTS.json').read_text())
DATA = Path('/data')
SERVER_PY = '/opt/openpi/.venv/bin/python'
SIM_PY = '/opt/sim/bin/python'


def digest(path, algorithm='sha256', git_blob=False):
    h = hashlib.new(algorithm)
    if git_blob:
        h.update(f'blob {path.stat().st_size}\0'.encode())
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def get(url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        tmp = path.with_name(path.name + '.partial')
        with urllib.request.urlopen(url, timeout=120) as src, tmp.open('wb') as dst:
            shutil.copyfileobj(src, dst)
        tmp.replace(path)


def verify_checkpoint():
    for item in ART['checkpoint']['inference_files']:
        p = DATA / 'checkpoint' / item['rfilename']
        if p.stat().st_size != item['size']:
            raise RuntimeError(f'Wrong size: {p}')
        expected = item.get('lfs', {}).get('sha256')
        actual = digest(p) if expected else digest(p, 'sha1', git_blob=True)
        if actual != (expected or item['blobId']):
            raise RuntimeError(f'Checkpoint checksum mismatch: {p}')
    normalizer = DATA / 'checkpoint' / PLAN['model']['normalizer']
    if digest(normalizer) != PLAN['model']['normalizer_sha256']:
        raise RuntimeError('Normalizer SHA256 mismatch')


def verify_sources():
    for path, key in [('/opt/vlabench', 'vlabench'), ('/opt/openpi', 'openpi'), ('/opt/rrt', 'rrt')]:
        rev = subprocess.check_output(['git', '-C', path, 'rev-parse', 'HEAD'], text=True).strip()
        if rev != PLAN['source'][key]:
            raise RuntimeError(f'Source revision mismatch: {path}')
    if digest(Path('/opt/openpi/uv.lock')) != PLAN['source']['openpi_lock_sha256']:
        raise RuntimeError('Openpi lock mismatch')
    track = Path('/opt/vlabench/VLABench/configs/evaluation/tracks/track_1_in_distribution.json')
    if digest(track) != ART['scene']['source_sha256']:
        raise RuntimeError('Public scene source mismatch')
    selected = json.loads(track.read_text())['select_fruit'][PLAN['probe']['episode_index']]
    if selected != ART['scene']['episode']:
        raise RuntimeError('Scene selector mismatch')


def verify_receipt():
    receipt = json.loads((DATA / 'asset_receipt.json').read_text())
    for relative, sha in receipt['files_sha256'].items():
        if digest(DATA / relative) != sha:
            raise RuntimeError(f'Asset changed: {relative}')
    verify_checkpoint()
    return receipt


def assets():
    verify_sources()
    if (DATA / 'asset_receipt.json').exists():
        verify_receipt()
        print('Existing sealed assets verified; no replacement.')
        return
    checkpoint = ART['checkpoint']
    for item in checkpoint['inference_files']:
        get(f"https://huggingface.co/{checkpoint['repo_id']}/resolve/{checkpoint['revision']}/{item['rfilename']}",
            DATA / 'checkpoint' / item['rfilename'])
    verify_checkpoint()
    shutil.copytree('/opt/base-assets', DATA / 'assets', dirs_exist_ok=True)
    archive_hashes = {}
    for item in ART['asset_archives']:
        archive = DATA / 'archives' / item['name']
        archive.parent.mkdir(parents=True, exist_ok=True)
        if not archive.exists():
            subprocess.run([SIM_PY, '-m', 'gdown', '--id', item['drive_id'], '-O', str(archive)], check=True)
        archive_hashes[item['name']] = digest(archive)
        with zipfile.ZipFile(archive) as z:
            root = (DATA / 'assets').resolve()
            for item_info in z.infolist():
                target = (root / item_info.filename).resolve()
                if not target.is_relative_to(root) or (item_info.external_attr >> 16) & 0o170000 == 0o120000:
                    raise RuntimeError('Unsafe archive member')
            z.extractall(root)
    # Populate exactly the upstream cache location, then validate public object metadata.
    from openpi.shared.download import maybe_download
    tokenizer = maybe_download('gs://big_vision/paligemma_tokenizer.model', gs={'token': 'anon'})
    expected_md5 = base64.b64decode(ART['tokenizer']['md5Hash']).hex()
    if tokenizer.stat().st_size != int(ART['tokenizer']['size']) or digest(tokenizer, 'md5') != expected_md5:
        raise RuntimeError('Tokenizer differs from pinned GCS metadata')
    required = ['base/default.xml', 'robots/franka_emika_panda/panda.xml']
    required += [x['xml_path'] for x in ART['scene']['episode']['task']['components']]
    # Robot base path is inspected again in native load; do not invent alternate assets.
    for relative in required:
        if not (DATA / 'assets' / relative).is_file():
            raise RuntimeError(f'Required asset missing: {relative}')
    files = {str(p.relative_to(DATA)): digest(p)
             for directory in ['assets', 'openpi-cache', 'archives']
             for p in (DATA / directory).rglob('*') if p.is_file() and not p.name.endswith('.lock')}
    receipt = {'status': 'DOWNLOADED_AND_SEALED_NOT_NATIVE_VERIFIED',
               'archive_sha256': archive_hashes, 'files_sha256': files,
               'tokenizer_generation': ART['tokenizer']['generation'],
               'checkpoint_revision': checkpoint['revision']}
    (DATA / 'asset_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'asset_files_sealed': len(files), 'archive_sha256': archive_hashes}))


def smoke():
    verify_sources()
    verify_receipt()
    runs = Path('/runs')
    if list(runs.glob('attempt-*')):
        raise RuntimeError('One bounded attempt already exists. Inspect results before changing the plan; no auto retry.')
    out = runs / 'attempt-1'
    out.mkdir()
    env = dict(os.environ, JAX_PLATFORMS='cuda', SET_RUN_DIR=str(out),
               HF_HUB_OFFLINE='1', SET_IMAGE_ID=os.environ.get('SET_IMAGE_ID', 'unknown'))
    outcome = {'stage': 'PRECHECK', 'native_rollouts_completed': 0,
               'image_id': env['SET_IMAGE_ID'], 'plan_sha256': digest(Path('/recipe/RESUME_PLAN.json')),
               'artifacts_sha256': digest(Path('/recipe/ARTIFACTS.json'))}
    server = None
    started = time.monotonic()
    try:
        gpu = subprocess.check_output(['nvidia-smi', '--query-gpu=name,uuid,driver_version,memory.total',
                                       '--format=csv,noheader'], text=True)
        outcome['gpu'] = gpu.strip()
        outcome['jax_devices'] = subprocess.check_output(
            [SERVER_PY, '-c', 'import jax; d=jax.devices(); assert d and all(x.platform=="gpu" for x in d); print(d)'],
            env=env, text=True, timeout=90).strip()
        for label, python in [('sim', SIM_PY), ('server', SERVER_PY)]:
            with (out / f'{label}-packages.txt').open('w') as f:
                subprocess.run(['uv', 'pip', 'freeze', '--python', python], stdout=f, check=True)
        shutil.copy('/recipe/sim-resolved.txt', out / 'sim-resolved.txt')
        shutil.copy('/recipe/RESUME_PLAN.json', out / 'plan.json')
        shutil.copy('/recipe/recipe_sha256.json', out / 'recipe_sha256.json')
        shutil.copy('/data/asset_receipt.json', out / 'asset_receipt.json')
        with (out / 'server.log').open('w') as log:
            server = subprocess.Popen([SERVER_PY, '/opt/openpi/scripts/serve_policy.py', '--env', 'VLABENCH',
                                       '--port', '8000', 'policy:checkpoint',
                                       '--policy.config', PLAN['model']['config'],
                                       '--policy.dir', '/data/checkpoint'],
                                      env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            while True:
                if server.poll() is not None:
                    raise RuntimeError('Policy server exited; inspect server.log')
                if time.monotonic() - started > 300:
                    raise TimeoutError('Policy startup exceeded 300 seconds')
                try:
                    with socket.create_connection(('127.0.0.1', 8000), timeout=1):
                        break
                except OSError:
                    time.sleep(1)
            outcome['stage'] = 'NATIVE_ATTEMPT'
            remaining = PLAN['probe']['wall_timeout_seconds'] - (time.monotonic() - started)
            with (out / 'client.log').open('w') as log_client:
                result = subprocess.run([SIM_PY, '/recipe/native_probe.py'], env=env, stdout=log_client,
                                        stderr=subprocess.STDOUT, timeout=max(1, remaining))
            outcome['client_exit_code'] = result.returncode
            probe = None
            if (out / 'probe.json').exists():
                probe = json.loads((out / 'probe.json').read_text())
            outcome.update(classify_probe(probe, result.returncode))
            if outcome['stage'] == 'CLIENT_FAILED':
                raise RuntimeError(outcome['failure_reason'])
    except Exception as exc:
        outcome['error'] = str(exc)
        raise
    finally:
        if server is not None and server.poll() is None:
            os.killpg(server.pid, signal.SIGTERM)
            try:
                server.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(server.pid, signal.SIGKILL)
                server.wait()
        outcome['wall_seconds'] = time.monotonic() - started
        (out / 'runtime.json').write_text(json.dumps(outcome, indent=2) + '\n')


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'verify-recipe':
        hashes = verify_recipe('/recipe', '/expected-recipe')
        print(json.dumps({'status': 'RECIPE_MATCH_ONLY', 'files_checked': len(hashes)}))
    elif mode == 'assets':
        assets()
    elif mode == 'smoke':
        smoke()
    elif mode == 'results':
        for p in sorted(Path('/runs').glob('attempt-*/*.json')):
            if p.name in {'runtime.json', 'probe.json'}:
                obj = json.loads(p.read_text())
                obj.pop('trace', None)
                print(str(p), json.dumps(obj, indent=2))
    else:
        raise SystemExit('Expected verify-recipe, assets, smoke or results')
