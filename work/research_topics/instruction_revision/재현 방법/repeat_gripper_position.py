"""Repeat even-seed self/late pairs in a new Docker policy process and JAX cache."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile

from drawer_bowl_position import sessions
from drawer_gripper_position_starts import DESIGN, HOSTS, LAYOUT, SCRIPT, alternate
from drawer_view_duration import behavior_record, rendered_inputs
from drawer_width import tape_for
from inside import write_json
from verify_atomic import PACKET, read
from verify_middle_aperture import contact_geometry, path_outcomes
from verify_stove import sha
from verify_stove_layouts import digest


def selection():
    return {n:e for n,e in sessions().items() if e['block']==1 and e['key']%2==0 and e['view'] in ('self','late')}


def verify(out, parent):
    original = read(parent/'verification.json')['paths_by_session']
    entries = selection()
    assert read(out/'sessions.json')==entries and read(out/'repeat-plan.json')==list(entries.values())
    assert set(entries)=={p.stem for p in (out/'paths').glob('*.json')}=={p.stem for p in (out/'receipts').glob('*.jsonl')}
    keys=read(parent/'rng.json')
    qual=read(parent/'qualification.json')
    geo={int(i):contact_geometry(v) for i,v in qual['geometry'].items()}
    refs={(a,m):tape_for(parent,a,m) for a in LAYOUT for h in HOSTS for m in (h,alternate(h))}
    cases,frames={},set()
    flags,match={},Counter()
    deltas=[]
    for n,e in entries.items():
        layout,a,m=e['layout'],e['arm'],e['mode']
        t=read(out/'paths'/(n+'.json'))
        own,other=refs[a,m],refs[a,alternate(m)]
        sent,ex=rendered_inputs(t,e,own,other,geo[layout],DESIGN['exchange_indices'])
        vals,_=path_outcomes(out,e,own,geo[layout],keys,frames,sent_by_tick=sent,tape=t)
        obs=behavior_record(vals,t,ex)
        obs['first_20_sha256']=digest(obs.pop('controls'))
        obs['final_physics']=t['final_physics']
        prior=original[n]
        cases[n]=obs
        match.update({k:int(obs[k]==prior[k]) for k in ('contact','contact_tick','at15','at30','first_20_sha256','final_physics')})
        old=read(parent/'paths'/(n+'.json'))['queries'][0]
        new=t['queries'][0]
        assert new['state']==old['state'] and new['physics']==old['physics'] and new['render']['sent']==old['render']['sent']
        deltas.append(max(abs(x-y) for r,s in zip(old['reply'][:5],new['reply'][:5],strict=True) for x,y in zip(r,s,strict=True)))
        if e['view']=='self':
            late=n.replace('.self-','.late-')
            flags[n]=prior['contact']!=original[late]['contact']
    groups={}
    for layout in (2,3):
        groups[str(layout)]={}
        for m in HOSTS:
            names=[n for n in flags if entries[n]['mode']==m and entries[n]['layout']==layout]
            counts=Counter((flags[n],cases[n]['contact']!=cases[n.replace('.self-','.late-')]['contact']) for n in names)
            groups[str(layout)][m]=dict(pairs=len(names),original=sum(v for (a,b),v in counts.items() if a),
                repeat=sum(v for (a,b),v in counts.items() if b),original_only=counts[True,False],repeat_only=counts[False,True])
    return dict(paths=len(entries),queries=sum(e['queries'] for e in entries.values()),first_input_and_rng_equal=len(deltas),
                identical_first_five=sum(v==0 for v in deltas),largest_first_five_component_change=max(deltas),
                agreement=dict(match),changes=groups,paths_by_session=cases)


def collect(parent,out):
    from inside import artifacts
    from run_atomic import SIM_PYTHON
    from run_stove_pose import policy_block

    assert Path('/.dockerenv').is_file()
    runtime=read(parent/'runtime.json')
    assert os.environ['REVISION_IMAGE_ID']==runtime['image'] and artifacts(download=False)['files']==runtime['checkpoint']
    cache=Path(os.environ['JAX_COMPILATION_CACHE_DIR'])
    assert not cache.exists() or not list(cache.iterdir())
    assert all(sha(PACKET/n)==h for n,h in runtime['sources'].items())
    out.mkdir()
    for key in ('paths','logs','receipts','frames'):
        (out/key).mkdir()
    for name in ('sources','preparation','clearance.json','camera_inputs.json','qualification.json','rng.json'):
        (out/name).symlink_to((parent/name).resolve())
    entries=selection()
    assert len(entries)==64
    write_json(out/'sessions.json',entries)
    write_json(out/'environment.json',dict(image=runtime['image'],gpu=runtime['gpu'],checkpoint_sha256=digest(runtime['checkpoint']),
        fresh_cache=True,seeds=[0,2,4,6],source_sha256=sha(Path(__file__)),parent_start=runtime['started']))
    sim=[SIM_PYTHON,str(PACKET/SCRIPT),str(out)]
    os.environ.update(XLA_PYTHON_CLIENT_PREALLOCATE='false',XLA_PYTHON_CLIENT_MEM_FRACTION='0.50',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    policy_block(out,sim,list(entries.values()),'repeat-plan','policy-repeat.log',workers=5)
    write_json(out/'repeat-verification.json',verify(out,parent))


def bundle(out, destination):
    files=[out/n for n in ('sessions.json','repeat-plan.json','environment.json','repeat-verification.json','logs/policy-repeat.log')]
    for name in ('paths','receipts','frames'):
        files.extend(sorted(p for p in (out/name).iterdir() if p.is_file()))
    assert sha(Path(__file__))==read(out/'environment.json')['source_sha256']
    with ZipFile(destination,'x',compression=ZIP_DEFLATED,compresslevel=9) as z:
        for p in files:
            z.write(p,p.relative_to(out))
        z.write(Path(__file__),'sources/repeat_gripper_position.py')


def verify_bundle(parent,path):
    with tempfile.TemporaryDirectory() as tmp, ZipFile(path) as z:
        assert z.testzip() is None and all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(tmp)
        out=Path(tmp)
        assert sha(out/'sources/repeat_gripper_position.py')==read(out/'environment.json')['source_sha256']
        assert verify(out,parent)==read(out/'repeat-verification.json')


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('stage',choices=('collect','bundle','verify'))
    ap.add_argument('source',type=Path)
    ap.add_argument('destination',type=Path)
    args=ap.parse_args()
    if args.stage=='collect':
        collect(args.source,args.destination)
    elif args.stage=='bundle':
        bundle(args.source,args.destination)
    else:
        from verify_layouts import unpack
        with unpack(args.source) as parent:
            # The main verification report lives beside the ZIP.
            if not (parent/'verification.json').exists():
                shutil.copyfile(args.source/'verification.json',parent/'verification.json')
            verify_bundle(parent,args.destination)
    print('Verified 64 independent-cache self/late paths' if args.stage=='verify' else 'Completed '+args.stage,flush=True)
