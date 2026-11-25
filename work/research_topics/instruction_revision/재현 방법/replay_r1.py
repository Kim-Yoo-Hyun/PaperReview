"""Replay the four archived command streams in fresh simulators and localize repeat differences."""
import argparse
from contextlib import nullcontext
import hashlib
import json
from pathlib import Path
import zipfile

import numpy as np
from PIL import Image
from resteer.sim import libero as sim

from atomic_control import capture_state, geom_info, measurements
from r1_motion import BottleObserver, reset
from verify_atomic import CAMERAS, PACKET, read


def render(env,prompt):
    sim.set_camera_rendering(env,True)
    obs = sim.get_observation(env)
    sim.set_camera_rendering(env,False)
    return sim.policy_input(obs,prompt)


def difference(image,reference):
    delta = abs(image.astype(np.int16)-reference.astype(np.int16))
    return {'pixels':int(np.count_nonzero(delta.any(axis=2))),'max_channel_levels':int(delta.max())}


def replay(data,spec,image,stop_at=None):
    env = reset(spec['scene_seed'], spec.get('bottle_xy'))
    try:
        observer = BottleObserver(env)
        geometry = geom_info(env)
        groups = {k:set(v.values()) for k,v in geometry['contact_geoms'].items()}
        assert geometry == data['geometry'] and observer.geometry == data['bottle_geometry']
        rack = None
        if spec['case']=='R4':
            from r4_rack import RackObserver
            rack = RackObserver(env,spec)
            assert rack.geometry==data['rack']['geometry']
        def check_row(row,success):
            native = measurements(env,groups,success)
            native['bowl_contacts'] = [list(pair) for pair in native['bowl_contacts']]
            assert native == {k:row[k] for k in native} and row['bottle_pose'] == observer.pose()
            assert row['bottle_contacts'] == [list(pair) for pair in observer.contacts()]
            if rack is not None:
                assert rack.sample(success)==data['rack']['samples'][row.get('tick',0)]
        check_row(data['initial_readout'],env.env._check_success(return_success_dict=True))
        diffs, matches = [],{}
        def compare_observation(tick,query,record):
            assert query['observation/state'].tolist() == record['proprioception']
            for key in CAMERAS:
                digest = record['rgb_sha256'][key]
                if hashlib.sha256(query[key].tobytes()).hexdigest() != digest:
                    delta = difference(query[key],image(digest)) if image is not None else {}
                    diffs.append(dict(tick=tick,camera=key,**delta))
        def physical_query(index):
            q = data['queries'][index]
            if 'live_camera_sha256' in data:
                return dict(q, rgb_sha256=data['live_camera_sha256'][index])
            return q
        for row in data['rows'][:stop_at]:
            tick = row['tick']-1
            if row['index'] == 0:
                q = physical_query(row['query'])
                assert q['completed_controls'] == tick
                compare_observation(tick,render(env,q['prompt']),q)
                if str(tick) in data['snapshots']:
                    actual = capture_state(env)
                    matches[str(tick)] = {k:v==data['snapshots'][str(tick)][k] for k,v in actual.items()}
            _,success = sim.step(env,np.asarray(row['dispatched']))
            check_row(row,success)
        if stop_at is not None:
            index, = [i for i,q in enumerate(data['queries']) if q['completed_controls']==stop_at]
            branch = physical_query(index)
            compare_observation(stop_at,render(env,branch['prompt']),branch)
            assert not diffs and all(all(v.values()) for v in matches.values())
            return {'controls':stop_at,'state':capture_state(env),'rgb_sha256':branch['rgb_sha256'],
                    'proprioception':branch['proprioception'],'verified_earlier_snapshots':matches}
        actual = capture_state(env)
        matches['terminal'] = {k:v==data['final_state'][k] for k,v in actual.items()}
        compare_observation(spec['horizon'],render(env,spec['arms'][data['arm']]),data['final_observation'])
        result = {'actions':len(data['rows']),'native_rows_and_bottle_poses_exact':True,
                  'snapshots':matches,'rgb_differences_against_original':diffs}
        if rack is not None:
            result['rack_samples_exact'] = len(data['rack']['samples'])
        return result
    finally:
        env.close()


def compare_restarts(a,b,image):
    first_pixels = None
    for x,y in zip(a['queries'],b['queries']):
        unequal = {k:difference(image(x['rgb_sha256'][k]),image(y['rgb_sha256'][k]))
                   for k in CAMERAS if x['rgb_sha256'][k]!=y['rgb_sha256'][k]}
        if unequal:
            first_pixels = {'after_controls':x['completed_controls'],'cameras':unequal,
                            'same_proprioception':x['proprioception']==y['proprioception']}
            break
    first_row = next((x['tick'] for x,y in zip(a['rows'],b['rows']) if x!=y),None)
    first_command = next((x['tick'] for x,y in zip(a['rows'],b['rows']) if x['dispatched']!=y['dispatched']),None)
    return {'first_unequal_rgb':first_pixels,'first_unequal_raw_row':first_row,'first_unequal_command':first_command}


def main(out,archive):
    def image(digest):
        name = digest+'.png'
        with (archive.open(name) if archive else (out/'frames'/name).open('rb')) as handle:
            with Image.open(handle) as img:
                return np.asarray(img)
    paths,checks,diagnostic = {},{},{}
    spec = read(out/'protocol.json')
    arms = spec['arms']
    if spec.get('case')=='R4':
        arms = list(dict.fromkeys(p['arm'] for p in read(out/'run.json')['paths']))
    for arm in arms:
        for repeat in range(1,spec['repetitions']+1):
            name = f'{arm}_{repeat}'
            paths[name] = read(out/f'{name}.json')
            checks[name] = replay(paths[name],spec,image)
        diagnostic[arm] = compare_restarts(paths[f'{arm}_1'],paths[f'{arm}_2'],image)
    return {'policy_queries':0,'replayed_controls':sum(p['actions'] for p in checks.values()),
            'paths':checks,'original_native_restart_comparison':diagnostic}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    parser.add_argument('--prepare-donors',action='store_true')
    args = parser.parse_args()
    out = args.run
    if args.prepare_donors:
        spec = read(out/'protocol.json')
        ref = PACKET/spec['reference']['archive']
        states = {}
        with zipfile.ZipFile(ref/'frames.zip') as frames:
            def donor_image(digest):
                with frames.open(digest+'.png') as handle, Image.open(handle) as img:
                    return np.asarray(img)
            for name in sorted(set(spec['branch_donors'].values())):
                data = read(ref/name)
                states[name] = replay(data,spec,donor_image,spec['intervention_tick'])
        (out/'donor_states.json').write_text(json.dumps(states,indent=2,allow_nan=False)+'\n')
        raise SystemExit(0)
    archive = out/'frames.zip'
    with (zipfile.ZipFile(archive) if archive.exists() else nullcontext()) as frames:
        print(json.dumps(main(out,frames),indent=2))
