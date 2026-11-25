"""Qualify the two preselected R1 layouts, freeze their prefixes, and run each comparison."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

import numpy as np

from inside import artifacts, write_json
from run_atomic import SIM_PYTHON, utc
from run_r1 import digest, run_path
from verify_atomic import PACKET, read, sensor_flags
from verify_r1 import check_calibration, displacement, world_pose


STUDY = 'R1_LAYOUTS.json'
INPUTS = (STUDY, 'R1_RAW_UPDATE.json', 'R1_CONTROL.json', 'SEMANTIC_CASES.json', 'ATOMIC_CONTROL.json',
          'run_layouts.py', 'run_r1.py', 'run_atomic.py', 'r1_motion.py', 'atomic_control.py',
          'inside.py', 'verify_r1.py', 'verify_atomic.py')


def base_inputs():
    design = read(PACKET/STUDY)
    assert digest(PACKET/design['base']) == design['base_sha256']
    base = read(PACKET/design['base'])
    ref = PACKET/base['reference']['archive']
    for name in ('calibration.json', 'O_1.json', 'runtime_manifest.json'):
        assert digest(ref/name) == base['reference']['files'][name]
    return design, base, ref


def layout_spec(base, seed, prefix_hash=None):
    keys = ('case', 'policy', 'policy_rng_seed', 'python_hash_seed', 'calibration_seed', 'warmup_controls',
            'horizon', 'switch', 'replan_controls', 'repetitions', 'source_prompt', 'goal_key', 'arms',
            'protected_body', 'score', 'measurement', 'run_order')
    spec = {k:base[k] for k in keys}
    spec.update(layout_study=STUDY, scene_seed=seed, calibration={k:base['calibration'][k] for k in
                ('translation_m', 'world_rotation_axis', 'rotation_degrees')})
    if prefix_hash is not None:
        spec['source_replay'] = {'path':'prefix.json', 'file_sha256':prefix_hash, 'controls':spec['switch']}
    return spec


def positions(bowl, bottle):
    return {'bowl':bowl, 'bottle':bottle}


def layout_gate(cal, spec, previous):
    trial = cal['check']
    xyz = positions(trial['bowl_xyz'], trial['drift'][0]['xyz'])
    distances = {key:{obj:float(1000*np.linalg.norm(np.asarray(pos)-other[obj])) for obj,pos in xyz.items()}
                 for key,other in previous.items()}
    limit = cal['translation_m']
    distinct = all(max(items.values()) > 1000*limit for items in distances.values())
    origin = world_pose(trial['drift'][0])
    peak = np.max([displacement(origin,world_pose(pose)) for pose in trial['drift']],axis=0)
    try:
        check_calibration(cal,spec)
        monitor = True
    except AssertionError:
        monitor = False
    return {'xyz_m':xyz, 'distance_mm_from_previous':distances, 'distinct':distinct,
            'frozen_monitor_valid':monitor, 'zero_command_states':len(trial['drift']),
            'peak_zero_translation_mm':float(peak[0]*1000), 'peak_zero_rotation_deg':float(np.degrees(peak[1])),
            'layout_eligible':distinct and monitor}


def prefix_gate(folder, spec, cal):
    data = read(folder/'prefix.json')
    assert data['status']=='PREFIX_ONLY' and len(data['rows'])==spec['switch']
    first, branch = data['queries']
    assert first['completed_controls']==0 and first['prompt']==spec['source_prompt']
    assert branch['completed_controls']==spec['switch'] and 'reply' not in branch
    assert [r['dispatched'] for r in data['rows']]==first['reply'][:spec['switch']]
    assert data['initial_readout']['bottle_pose']==cal['check']['drift'][0]
    assert data['initial_readout']['bowl_xyz']==cal['check']['bowl_xyz']
    assert data['bottle_geometry']==cal['check']['geometry']
    groups = {k:set(v.values()) for k,v in data['geometry']['contact_geoms'].items()}
    size = np.asarray(data['geometry']['cabinet_site_half_size'])
    rows = [data['initial_readout'],*data['rows']]
    cleared = []
    for row in (rows[0],rows[-1]):
        flags,grasp = sensor_flags(row, groups, size)
        cleared.append(not any(flags.values()) and not grasp)
    origin = world_pose(rows[0]['bottle_pose'])
    peak = np.max([displacement(origin,world_pose(row['bottle_pose'])) for row in rows],axis=0)
    protected = bool(np.all(peak <= [cal['translation_m'],cal['rotation_rad']]))
    return {'initial_and_branch_clear':cleared, 'protected':protected, 'eligible':all(cleared) and protected,
            'prefix_sha256':digest(folder/'prefix.json')}


def calibrate_layout(folder, seed):
    from r1_motion import calibration_trial, write
    _, _, ref = base_inputs()
    cal = read(ref/'calibration.json')
    cal['check'] = calibration_trial(seed, include_layout=True)
    write(folder/'calibration.json', cal)


def run(out):
    assert Path('/.dockerenv').exists()
    # Leave room for the EGL simulator and cuBLAS workspace on the shared 32 GB card.
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    design, base, ref = base_inputs()
    out.mkdir(parents=True,exist_ok=False)
    qual = Path('/prior/LATEST').read_text().strip()
    assert Path(qual).name == qual
    runtime = Path('/prior')/qual/'runtime_manifest.json'
    meta = read(runtime)
    assert meta['status']=='PASS_IO_ONLY' and meta['image_id']==os.environ['REVISION_IMAGE_ID']
    assert meta['artifacts']['files']==read(ref/'runtime_manifest.json')['artifacts']['files']==artifacts(download=False)['files']
    shutil.copyfile(PACKET/STUDY,out/'study.json')
    shutil.copyfile(runtime,out/'runtime_manifest.json')
    hashes = {name:digest(PACKET/name) for name in INPUTS}
    sources = out/'executed_sources'
    sources.mkdir()
    for name in hashes:
        shutil.copyfile(PACKET/name,sources/name)
    original = read(ref/'O_1.json')['initial_readout']
    previous = {str(design['reference_seed']):positions(original['bowl_xyz'],original['bottle_pose']['xyz'])}
    gate = {'started_at':utc(),'jax_memory_fraction':os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'],'layouts':{},'prefixes':{}}
    for seed in design['seeds']:
        folder = out/f'seed-{seed}'
        (folder/'frames').mkdir(parents=True)
        (folder/'logs').mkdir()
        spec = layout_spec(base,seed)
        write_json(folder/'protocol.json',spec)
        subprocess.run([SIM_PYTHON,__file__,str(folder),'--calibrate',str(seed)],check=True)
        assessed = layout_gate(read(folder/'calibration.json'),spec,previous)
        gate['layouts'][str(seed)] = assessed
        if assessed['layout_eligible']:
            previous[str(seed)] = assessed['xyz_m']
        print(f"Layout {seed}: distinct={assessed['distinct']} monitor={assessed['frozen_monitor_valid']}",flush=True)
    for seed in design['seeds']:
        if not gate['layouts'][str(seed)]['layout_eligible']:
            continue
        folder = out/f'seed-{seed}'
        spec = layout_spec(base,seed)
        run_path(folder,'raw',1,mode='prefix')
        branch = prefix_gate(folder,spec,read(folder/'calibration.json'))
        gate['prefixes'][str(seed)] = branch
        if branch['eligible']:
            write_json(folder/'protocol.json',layout_spec(base,seed,branch['prefix_sha256']))
    gate['frozen_at'] = utc()
    write_json(out/'gates.json',gate)
    for seed in design['seeds']:
        if not gate['prefixes'].get(str(seed),{}).get('eligible'):
            continue
        folder = out/f'seed-{seed}'
        shutil.copyfile(runtime,folder/'runtime_manifest.json')
        runlog = {'started_at':utc(),'frozen_at':gate['frozen_at'],'image_id':meta['image_id'],'qualification':qual,
                  'input_sha256':hashes,'frozen_calibration_sha256':digest(folder/'calibration.json'),'paths':[],'status':'STARTED'}
        subprocess.run([sys.executable,str(PACKET/'run_r1.py'),'tokens',str(folder),'before'],check=True)
        for repeat,order in enumerate(base['run_order'],1):
            for arm in order:
                entry={'arm':arm,'repeat':repeat,'started_at':utc()}
                runlog['paths'].append(entry)
                write_json(folder/'run.json',runlog)
                print(f'Running seed {seed}, {arm}, repeat {repeat}',flush=True)
                run_path(folder,arm,repeat)
                entry['finished_at']=utc()
        subprocess.run([sys.executable,str(PACKET/'run_r1.py'),'tokens',str(folder),'after'],check=True)
        runlog.update(status='COMPLETED',finished_at=utc())
        write_json(folder/'run.json',runlog)
    write_json(out/'run.json',{'status':'COMPLETED','input_sha256':hashes,'finished_at':utc()})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('out',type=Path)
    parser.add_argument('--calibrate',type=int)
    args = parser.parse_args()
    if args.calibrate is None:
        run(args.out)
    else:
        calibrate_layout(args.out,args.calibrate)
