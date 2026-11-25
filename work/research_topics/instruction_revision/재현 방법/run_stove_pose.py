"""Run the geometry-qualified common-pose comparison with the native policy in Docker."""
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
from verify_stove import sha
from verify_stove_pose import BASE, PLAN, PLAN_FILE, planned


def policy_block(out, sim, subset, plan_name, log_name, *, workers=3):
    def one(entry):
        with (out/'logs'/(entry['session']+'.log')).open('w') as log:
            proc = subprocess.run([*sim,'run',entry['session']],cwd='/opt/resteer',stdout=log,stderr=subprocess.STDOUT,timeout=1200)
        if proc.returncode:
            raise RuntimeError(entry['session']+' '+(out/'logs'/(entry['session']+'.log')).read_text()[-1500:])
    path = out/(plan_name+'.json')
    write_json(path,subset)
    with server(path,out/'logs'/log_name), ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(one,subset))


def run(out):
    assert Path('/.dockerenv').is_file() and sha(BASE)==PLAN['baseline_sha256']
    out.mkdir()
    for folder in ('frames','logs','paths','receipts','sources'):
        (out/folder).mkdir()
    os.environ.update(XLA_PYTHON_CLIENT_MEM_FRACTION='0.50',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with zipfile.ZipFile(BASE) as z:
        previous = json.loads(z.read('runtime.json'))
    checkpoint = artifacts(download=False)['files']
    assert checkpoint == previous['checkpoint']
    names = [*previous['sources'],PLAN_FILE,'stove_pose_sim.py','run_stove_pose.py','verify_stove_pose.py']
    sources = {}
    for name in names:
        path = out/'sources'/name
        path.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(PACKET/name,path)
        sources[name] = sha(path)
    gpu = subprocess.check_output(['nvidia-smi','--query-gpu=name,driver_version,memory.total','--format=csv,noheader'],text=True).strip()
    write_json(out/'runtime.json',dict(started=utc(),image=os.environ['REVISION_IMAGE_ID'],gpu=gpu,
               checkpoint=checkpoint,sources=sources,baseline_sha256=sha(BASE)))
    write_json(out/'design.json',PLAN)
    sim = [SIM_PYTHON,str(PACKET/'stove_pose_sim.py'),str(out)]
    subprocess.run([*sim,'qualify'],check=True)
    lead = read(out/'qualification.json')['lead']
    if lead is None:
        print('No common physical preparation passed qualification',flush=True)
        return
    entries = planned(lead)
    write_json(out/'sessions.json',entries)
    for block in range(1,PLAN['blocks']+1):
        subset = [e for e in entries.values() if e['block']==block]
        policy_block(out,sim,subset,f'block-{block}',f'policy-{block}.log')
        print('Completed policy block',block,'paths',len(subset),flush=True)
    subprocess.run([SIM_PYTHON,str(PACKET/'verify_stove_pose.py'),str(out),'score'],check=True)
    print('Completed',utc(),flush=True)


if __name__ == '__main__':
    run(Path(sys.argv[1]))
