"""Run the late camera-channel comparison on the eight archived gripper starts."""
import argparse
from functools import partial
import json
import os
from pathlib import Path
import subprocess
from zipfile import ZipFile

from drawer_gripper_position_starts import (BASE, HOSTS, LAYOUT, MODES, STUDIES, alternate, branch,
    checked_inputs, live_study, local_cohort, subprocess_starts, validate)
from drawer_view_duration import LIMIT, PERIOD
from drawer_width import tape_for
from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import TASK, check_archive_repeat, planned
from verify_stove import sha
from verify_stove_layouts import check_replayed_paths, replay

SCRIPT = 'drawer_camera_window.py'
DESIGN_FILE = 'drawer/drawer_camera_window.json'
DESIGN = read(PACKET / DESIGN_FILE)
CHANNELS = DESIGN['channels']
INDICES = {v:DESIGN['indices'] if cams else [] for v,cams in CHANNELS.items()}
PARENT = PACKET / DESIGN['parent']
assert set(CHANNELS) == {'self','external','wrist','both'}
assert CHANNELS['both'] == list(CAMERAS) == CHANNELS['external'] + CHANNELS['wrist']


def sessions():
    modes = [m+'.'+v for v in CHANNELS for m in HOSTS]
    entries = planned({**STUDIES[2], 'arms':list(LAYOUT)}, modes=modes)
    for entry in entries.values():
        entry['mode'],entry['view'] = entry['mode'].split('.')
        entry['layout'] = LAYOUT[entry['arm']]
    return entries


def archived_starts(out, *, install=False):
    assert sha(PARENT) == DESIGN['parent_sha256']
    donor = local_cohort(out)['donors'].relative_to(out.resolve()).as_posix()
    with ZipFile(PARENT) as z:
        names = ['clearance.json','qualification.json','camera_inputs.json',donor]
        names += [n for n in z.namelist() if n.startswith(('frames/','preparation/'))]
        assert len([n for n in names if n.startswith('preparation/')]) == len(LAYOUT)*len(MODES)
        for n in names:
            p, data = out/n, z.read(n)
            if install:
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_bytes(data)
            else:
                assert p.read_bytes() == data, n
    return checked_inputs(out, validate_fn=validate)


def run_path(out, entry, replaying):
    from drawer_camera_routing import schedule
    from drawer_location_sim import run

    arm,mode,view = entry['arm'],entry['mode'],entry['view']
    bank = read(out/'camera_inputs.json')['images'][arm]
    factory = partial(schedule,host=bank[mode],narrow=bank[alternate(mode)],channels=CHANNELS[view],
                      indices=INDICES[view],width=DESIGN['camera_width_m'])
    return run(out,entry,replay=replaying,view_factory=factory,cohort=live_study(out,LAYOUT[arm]),
               arrangements=read(out/'clearance.json')['arrangements'][arm],prepare_fn=branch)


def probe(out, arm, mode):
    from OpenGL import GL
    from atomic_control import capture_state, digest
    from drawer_camera_routing import schedule
    from drawer_location_sim import LocationCabinet
    from drawer_sim import observe, state_hash
    from middle_aperture_sim import environment, restore

    study = live_study(out,LAYOUT[arm])
    bank = read(out/'camera_inputs.json')['images'][arm]
    host = tape_for(out,arm,mode)
    wide = mode in HOSTS
    env = environment(arm, layout=study['layout'])
    try:
        scene = LocationCabinet(env)
        common = restore(env,scene,arm,out,donors_file=study['donors'])
        assert common == host['common'] and state_hash(capture_state(env)) == host['donor_physics']
        prep = branch(env,scene,common,mode,BASE['lead'],corrections=read(out/'clearance.json')['arrangements'][arm])
        assert all(host[k] == v for k,v in prep.items()) and scene.read() == host['handoff']
        narrow = bank[alternate(mode)] if wide else bank[mode]
        records = {}
        for name in CHANNELS if wide else ['self']:
            view = schedule(env,scene,host=bank[mode],narrow=narrow,channels=CHANNELS[name],
                            indices=[0],width=DESIGN['camera_width_m'])
            query,sample = observe(env,out,False,TASK['prompt'])
            view.apply(0,query,sample,[])
            assert sample['physics'] == host['first']['physics'] == state_hash(capture_state(env))
            assert sample['state'] == host['first']['state'] == query['observation/state'].tolist()
            assert {c:digest(query[c]) for c in CAMERAS} == sample['render']['sent']
            records[name] = sample['render']
        renderer = GL.glGetString(GL.GL_RENDERER).decode()
        return dict(physics=sample['physics'],state=sample['state'],renderer=renderer,views=records)
    finally:
        env.close()


def check_routing(record, native, selected):
    assert record['selected'] == selected and record['self_rgb'] == native
    assert record['exchange'] == bool(selected)
    if selected:
        assert set(record['narrow_rgb']) == set(record['narrow_changed_pixels']) == set(CAMERAS)
    else:
        assert not record['narrow_rgb'] and not record['narrow_changed_pixels']
    for cam in CAMERAS:
        if selected:
            count = record['narrow_changed_pixels'][cam]
            assert 0 <= count <= 224*224
            assert (count > 0) == (native[cam] != record['narrow_rgb'][cam])
        expected = record['narrow_rgb'][cam] if cam in selected else native[cam]
        assert record['sent'][cam] == expected
        assert record['changed_pixels'][cam] == (record['narrow_changed_pixels'][cam] if cam in selected else 0)


def check_preflight(out):
    qual, bank = archived_starts(out)
    proof = read(out/'channel_preflight.json')
    assert set(proof) == set(LAYOUT)
    for arm in LAYOUT:
        assert set(proof[arm]) == set(MODES)
        for mode,s in proof[arm].items():
            wide = mode in HOSTS
            tape = tape_for(out,arm,mode)
            assert s['physics'] == tape['first']['physics'] and s['state'] == tape['first']['state']
            assert s['renderer'] == qual['renderer'] and 'NVIDIA' in s['renderer']
            assert set(s['views']) == (set(CHANNELS) if wide else {'self'})
            native = bank['images'][arm][mode]
            for name,r in s['views'].items():
                selected = CHANNELS[name]
                check_routing(r,native,selected)
                assert r['host_after'] == s['physics'] and r['host_qpos'] == tape['handoff']['upper']['joints'][2]
                assert r['render_qpos'] == (-DESIGN['camera_width_m'] if selected else r['host_qpos'])
                if selected:
                    assert all(r['sent'][cam] == bank['images'][arm][alternate(mode)][cam] for cam in selected)
    return qual,bank,proof


def prepare(out):
    archived_starts(out, install=True)
    checks = subprocess_starts(out,'probe',MODES,script=SCRIPT)
    write_json(out/'channel_preflight.json',{a:{m:checks[a,m] for m in MODES} for a in LAYOUT})
    check_preflight(out)
    print('Restored 8 hosts and 8 narrow references, verified all 32 host camera assignments',flush=True)


def collect(out):
    from run_atomic import SIM_PYTHON, utc
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block
    from drawer_camera_window_score import score

    assert sha(PARENT) == DESIGN['parent_sha256']
    with ZipFile(PARENT) as z:
        parent_runtime = json.loads(z.read('runtime.json'))
    os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
    sources = [*parent_runtime['sources'],DESIGN_FILE,SCRIPT,'drawer_camera_routing.py','drawer_camera_window_score.py',
               'plot_drawer_camera_window.py','drawer_camera_window.sh']
    initialize_study(out,DESIGN,sources,key_count=BASE['key_offset']+TASK['extension']//PERIOD)
    run = read(out/'runtime.json')
    assert all(run[k] == parent_runtime[k] for k in ('image','gpu','checkpoint','policy_python','jax','simulator','commits'))
    sim = [SIM_PYTHON,str(PACKET/SCRIPT),str(out)]
    subprocess.run([*sim,'prepare'],check=True)
    entries = sessions()
    write_json(out/'sessions.json',entries)
    loads = []
    for block in STUDIES[2]['blocks']:
        cache = Path('/tmp/camera-window-jit')/str(block)
        assert not cache.exists()
        os.environ['JAX_COMPILATION_CACHE_DIR'] = str(cache)
        subset = [e for e in entries.values() if e['block']==block]
        loads.append(dict(block=block,cache=str(cache),empty_before_load=True,started=utc()))
        policy_block(out,sim,subset,f'block-{block}',f'policy-{block}.log',workers=5)
        loads[-1]['closed'] = utc()
        write_json(out/'loads.json',loads)
        print('Closed model load',block,'with',len(subset),'paths',flush=True)
    write_json(out/'verification.json',score(out))


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('folder',type=Path)
    ap.add_argument('stage',choices=('collect','prepare','probe','verify','run','replay'))
    ap.add_argument('items',nargs='*')
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.stage=='collect':
        collect(args.folder)
    elif args.stage=='prepare':
        prepare(args.folder)
    elif args.stage=='probe':
        print(json.dumps(probe(args.folder,*args.items)))
    elif args.items:
        name,=args.items
        assert args.stage in ('run','replay')
        result=run_path(args.folder,read(args.folder/'sessions.json')[name],args.stage=='replay')
        if result is not None:
            print(json.dumps(result))
    else:
        from drawer_camera_window_score import score
        entries=sessions()
        with unpack(args.folder) as out:
            result=score(out)
            assert result==read(args.folder/'verification.json')
            if args.stage=='replay':
                assert args.output and not args.output.exists()
                proof=replay(out,script=SCRIPT,entries=entries,workers=6)
                check_replayed_paths(out,proof,entries,{})
                write_json(args.output,proof)
            elif (args.folder/'physical_replay.json').is_file():
                proof=read(args.folder/'physical_replay.json')
                check_replayed_paths(out,proof,entries,{})
                if 'archive_repeat' in proof:
                    check_archive_repeat(args.folder,out,proof,entries)
        print('Verified',result['paths'],'camera-window paths and',result['policy_queries'],'receipts',flush=True)
