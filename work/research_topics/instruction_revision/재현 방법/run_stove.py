"""Run the direct stove gate followed by paired closed-loop continuations in Docker."""
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

from camera_extension import server
from inside import artifacts, write_json
from run_atomic import SIM_PYTHON, utc
from verify_atomic import PACKET, read
from verify_stove import D, DESIGN_FILE, DONORS, blocks, crossed, planned, sha


def keys(out, count=None):
    import jax
    if count is None:
        count = D['continuation_key_offset'] + D['full_budget']//D['replan_every']
    result = {}
    for seed in D['primary_seeds']:
        key = jax.random.key(seed)
        sequence = [jax.random.key_data(key).tolist()]
        for _ in range(count):
            key,_ = jax.random.split(key)
            sequence.append(jax.random.key_data(key).tolist())
        result[str(seed)] = sequence
    write_json(out/'rng.json',result)


def block(out, stage, n):
    groups = blocks(stage,n)
    name = stage+'-'+str(n)
    plan = out/(name+'.json')
    write_json(plan,[e for g in groups for e in g])
    def run_group(entries):
        for entry in entries:
            with (out/'logs'/(entry['session']+'.log')).open('w') as log:
                subprocess.run([SIM_PYTHON,str(PACKET/'stove_sim.py'),str(out),'run',entry['session']],
                               cwd='/opt/resteer',stdout=log,stderr=subprocess.STDOUT,check=True,timeout=1500)
    with server(plan,out/'logs'/(name+'.log')):
        with ThreadPoolExecutor(max_workers=3) as pool:
            list(pool.map(run_group,groups))
    print('Completed',name,sum(map(len,groups)),'paths',flush=True)


def run(out):
    assert Path('/.dockerenv').is_file() and sha(DONORS) == D['donor_sha256']
    assert sha(PACKET/'drawer/stove.bddl') == D['bddl_sha256'] and sha(PACKET/'drawer/stove_starts.json') == D['selected_starts_sha256']
    out.mkdir()
    for folder in ('paths','receipts','logs','frames','sources','crossed'):
        (out/folder).mkdir()
    os.environ.update(XLA_PYTHON_CLIENT_MEM_FRACTION='0.50', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    with zipfile.ZipFile(DONORS) as z:
        previous = json.loads(z.read('runtime.json'))
    checkpoint = artifacts(download=False)['files']
    assert checkpoint == previous['checkpoint']
    sources = {}
    for name in [DESIGN_FILE,'drawer/stove.bddl','drawer/stove_starts.json','drawer/LICENSE','drawer/protocol.json',
                 'drawer/starts.json','stove_sim.py','run_stove.py','verify_stove.py','drawer_sim.py','camera_server.py',
                 'serve_first_view.py','atomic_control.py','inside.py','run_r1.py','camera_extension.py','resume.sh']:
        copy = out/'sources'/name
        copy.parent.mkdir(exist_ok=True,parents=True)
        shutil.copyfile(PACKET/name,copy)
        sources[name] = sha(copy)
    gpu = subprocess.check_output(['nvidia-smi','--query-gpu=name,driver_version,memory.total','--format=csv,noheader'],text=True).strip()
    write_json(out/'runtime.json',dict(started_at=utc(),image=os.environ['REVISION_IMAGE_ID'],gpu=gpu,
               checkpoint=checkpoint,sources=sources,donor_archive=D['donor_sha256']))
    write_json(out/'design.json',D)
    write_json(out/'sessions.json',planned())
    subprocess.run([sys.executable,__file__,str(out),'--keys'],check=True)
    subprocess.run([SIM_PYTHON,str(PACKET/'stove_sim.py'),str(out),'qualify'],check=True)
    for n in range(1,D['blocks']+1):
        block(out,'direct',n)
    subprocess.run([SIM_PYTHON,str(PACKET/'verify_stove.py'),str(out),'gate'],check=True)
    if read(out/'gate.json')['passed']:
        for n in range(1,D['blocks']+1):
            block(out,'continuation',n)
        def fixed(name):
            with (out/'logs'/(name+'.log')).open('w') as log:
                subprocess.run([SIM_PYTHON,str(PACKET/'stove_sim.py'),str(out),'cross',name],
                               cwd='/opt/resteer',stdout=log,stderr=subprocess.STDOUT,check=True,timeout=400)
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(fixed,crossed()))
        print('Completed fixed-command crossover',flush=True)
    subprocess.run([SIM_PYTHON,str(PACKET/'verify_stove.py'),str(out),'score'],check=True)
    print('Finished',utc(),flush=True)


if __name__ == '__main__':
    if sys.argv[2:3] == ['--keys']:
        if len(sys.argv) not in (3,4):
            raise SystemExit('Expected --keys [number of splits]')
        keys(Path(sys.argv[1]), int(sys.argv[3]) if len(sys.argv)==4 else None)
    else:
        run(Path(sys.argv[1]))
