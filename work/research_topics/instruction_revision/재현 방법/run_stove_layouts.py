"""Run the registered standalone gates and fixed-cost transfer on LIBERO drawer layouts 2 and 3."""
from importlib.metadata import version
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

from inside import artifacts, write_json
from run_atomic import SIM_PYTHON, utc
from run_stove_pose import policy_block
from verify_atomic import PACKET, read
from verify_stove import sha
from verify_stove_layouts import DESIGN, DESIGN_FILE, check_freeze, digest, follow_plan, gate_plan


def initialize_study(out, design, extra_sources=(), *, key_count=None):
    assert Path('/.dockerenv').is_file()
    check_freeze(PACKET)
    prior=PACKET/design['parent']
    if prior.is_file():
        assert sha(prior)==design['parent_sha256']
    checkpoint=artifacts(download=False)['files']
    assert digest(checkpoint)==DESIGN['checkpoint_manifest_sha256']
    out.mkdir()
    for name in ('sources','paths','preparation','receipts','logs','frames'):
        (out/name).mkdir()
    os.environ.update(XLA_PYTHON_CLIENT_MEM_FRACTION='0.50',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    names=[DESIGN_FILE,DESIGN['starts_file'],DESIGN['preparation'],'drawer/protocol.json','drawer/stove_handoff.json',
           'drawer/task.bddl','drawer/stove.bddl','drawer/LICENSE','run_stove_layouts.py','verify_stove_layouts.py',
           'stove_layouts_sim.py','run_stove_pose.py','stove_pose_sim.py','verify_stove_pose.py','run_stove.py',
           'stove_sim.py','verify_stove.py','verify_drawer.py','drawer_sim.py','camera_extension.py','camera_server.py',
           'serve_first_view.py','run_r1.py','inside.py','atomic_control.py','resume.sh',*extra_sources]
    sources={}
    for n in names:
        target=out/'sources'/n
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(PACKET/n,target)
        sources[n]=sha(target)
    sim_versions=json.loads(subprocess.check_output([SIM_PYTHON,'-c',
        "import json,platform;from importlib.metadata import version;print(json.dumps(dict(python=platform.python_version(),mujoco=version('mujoco'),robosuite=version('robosuite'))))"],text=True))
    gpu=subprocess.check_output(['nvidia-smi','--query-gpu=name,driver_version,memory.total','--format=csv,noheader'],text=True).strip()
    commits={n:subprocess.check_output(['git','-C',r,'rev-parse','HEAD'],text=True).strip() for n,r in
             [('resteer','/opt/resteer'),('openpi','/opt/resteer/third_party/openpi')]}
    write_json(out/'runtime.json',dict(started=utc(),image=os.environ['REVISION_IMAGE_ID'],gpu=gpu,checkpoint=checkpoint,
               policy_python=platform.python_version(),jax=version('jax'),simulator=sim_versions,commits=commits,sources=sources))
    write_json(out/'design.json',design)
    command=[sys.executable,str(PACKET/'run_stove.py'),str(out),'--keys']
    if key_count is not None:
        command.append(str(key_count))
    subprocess.run(command,check=True)
    assert digest(read(out/'rng.json'))==design.get('rng_sha256',DESIGN['rng_schedule_sha256'])


def run(out):
    initialize_study(out,DESIGN)
    (out/'gates').mkdir()
    sim=[SIM_PYTHON,str(PACKET/'stove_layouts_sim.py'),str(out)]
    verify=[SIM_PYTHON,str(PACKET/'verify_stove_layouts.py'),str(out)]
    def blocks(stage,plan):
        for b in DESIGN['blocks']:
            subset=[e for e in plan.values() if e['block']==b]
            if subset:
                policy_block(out,sim,subset,f'{stage}-block-{b}',f'{stage}-policy-{b}.log')
            print(stage,'block',b,'paths',len(subset),flush=True)

    gates=gate_plan()
    write_json(out/'gate_sessions.json',gates)
    blocks('gate',gates)
    subprocess.run([*verify,'gate'],check=True)
    gate=read(out/'gate.json')
    print('Direct competence', {l:x['successes'] for l,x in gate.items()},flush=True)
    subprocess.run([*sim,'prepare'],check=True)
    plan=follow_plan(gate)
    write_json(out/'sessions.json',plan)
    blocks('continuation',plan)
    subprocess.run([*verify,'score'],check=True)
    print('Completed',utc(),flush=True)


if __name__=='__main__':
    run(Path(sys.argv[1]))
