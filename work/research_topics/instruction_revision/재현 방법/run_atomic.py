"""Launch each paired R8 trajectory with freshly initialized policy and simulator processes."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone

from inside import artifacts, write_json


PACKET = Path(__file__).resolve().parent
POLICY = Path('/opt/resteer/third_party/openpi')
SIM_PYTHON = '/opt/resteer/.venv/bin/python'


def utc():
    return datetime.now(timezone.utc).isoformat()


def run_path(out, arm, repeat):
    name = f'{arm}_{repeat}'
    serve = [sys.executable, str(POLICY/'scripts/serve_policy.py'), '--port', '8000',
             'policy:checkpoint', '--policy.config=pi05_libero', '--policy.dir=/data/checkpoints/pi05_libero']
    with (out/'logs'/f'{name}_server.log').open('w') as server_log:
        server = subprocess.Popen(serve, cwd='/opt/resteer', stdout=server_log, stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic() + 420
            while server.poll() is None:
                try:
                    with socket.create_connection(('127.0.0.1', 8000), timeout=1):
                        break
                except OSError:
                    if time.monotonic() >= deadline:
                        raise TimeoutError(f'{name} server startup')
                    time.sleep(1)
            else:
                raise RuntimeError(f'{name} server exited with {server.returncode}')
            with (out/'logs'/f'{name}_sim.log').open('w') as sim_log:
                subprocess.run([SIM_PYTHON, str(PACKET/'atomic_control.py'), str(out), arm, str(repeat)],
                               cwd='/opt/resteer', stdout=sim_log, stderr=subprocess.STDOUT,
                               timeout=1200, check=True)
        finally:
            if server.poll() is None:
                server.terminate()
                try:
                    server.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    server.kill()
                    server.wait()


def main(out):
    if not Path('/.dockerenv').is_file():
        raise RuntimeError('Use the local Docker launcher')
    spec = json.loads((PACKET/'ATOMIC_CONTROL.json').read_text())
    latest = Path('/prior/LATEST').read_text().strip()
    if not latest or Path(latest).name != latest:
        raise ValueError('Invalid qualification directory')
    prior = Path('/prior')/latest
    qualification = json.loads((prior/'runtime_manifest.json').read_text())
    if (qualification['status'] != 'PASS_IO_ONLY' or qualification['image_id'] != os.environ['REVISION_IMAGE_ID']
            or qualification['resteer_revision'] != spec['source_commit']
            or qualification['openpi_revision'] != spec['openpi_commit']):
        raise ValueError('Qualify the selected image and checkpoint with the smoke stage first')
    out.mkdir(parents=True, exist_ok=False)
    (out/'frames').mkdir()
    (out/'logs').mkdir()
    (out/'smoke').mkdir()
    for filename in ('runtime_manifest.json', 'native_result.json', 'policy_observations.npz'):
        shutil.copyfile(prior/filename, out/'smoke'/filename)
    shutil.copyfile(PACKET/'ATOMIC_CONTROL.json', out/'protocol.json')
    report = {'status':'STARTED', 'started_at':utc(), 'image_id':qualification['image_id'],
              'qualification':latest, 'paths':[], 'executed_sha256':{
                  f: hashlib.sha256((PACKET/f).read_bytes()).hexdigest()
                  for f in ('ATOMIC_CONTROL.json','atomic_control.py','run_atomic.py','inside.py')}}
    try:
        checked = artifacts(download=False)['files']
        if (checked != qualification['artifacts']['files'] or
                checked != json.loads(Path('/data/VERIFIED_ARTIFACTS.json').read_text())['files']):
            raise ValueError('Qualification and rollout checkpoint bytes differ')
        for repeat in range(1,spec['repetitions']+1):
            for arm in spec['arms']:
                entry = {'arm':arm['arm'], 'repeat':repeat, 'started_at':utc()}
                report['paths'].append(entry)
                write_json(out/'run.json', report)
                print(f"Starting {arm['arm']} repetition {repeat}", flush=True)
                run_path(out, arm['arm'], repeat)
                entry['finished_at'] = utc()
                print(f"Completed {arm['arm']} repetition {repeat}", flush=True)
        report['status'] = 'COMPLETED'
    except Exception as error:
        report.update(status='FAILED', error=f'{type(error).__name__}: {error}')
        raise
    finally:
        report['finished_at'] = utc()
        write_json(out/'run.json', report)


if __name__ == '__main__':
    main(Path(sys.argv[1]))
