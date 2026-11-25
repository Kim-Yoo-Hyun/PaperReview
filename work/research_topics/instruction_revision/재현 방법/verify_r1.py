"""Re-score retained bottle pose, native bowl goals, dispatch and branch matching without the simulator."""
import argparse
from contextlib import nullcontext
import json
import math
from pathlib import Path
import zipfile

import numpy as np
from PIL import Image

from verify_atomic import CAMERAS, array, intervals, read, sha, verify_path, source_matches, verify_run_files


PACKET = Path(__file__).resolve().parent


def cross_matrix(v):
    x,y,z = v
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0]])


def world_pose(data):
    p,q = array(data['xyz'],(3,)),array(data['wxyz'],(4,))
    free = array(data['free_joint'],(7,))
    matrix = array(data['rotation'],(3,3))
    assert abs(np.linalg.norm(q)-1) < 1e-9 and abs(np.linalg.norm(free[3:])-1) < 1e-9
    assert np.max(abs(p-free[:3])) < 1e-12 and abs(abs(free[3:]@q)-1) < 1e-9
    skew = cross_matrix(q[1:])
    assert np.max(abs(matrix-(np.eye(3)+2*q[0]*skew+2*skew@skew))) < 1e-9
    return p,matrix


def displacement(origin,sample):
    p0,r0 = origin
    p,r = sample
    turn = r@r0.T
    skew = turn-turn.T
    sine = 0.5*np.linalg.norm([skew[2,1],skew[0,2],skew[1,0]])
    angle = math.atan2(sine,(np.trace(turn)-1)/2)
    return [float(np.linalg.norm(p-p0)),angle]


def check_calibration(cal,spec):
    assert cal['status'] == 'FROZEN'
    limits = np.array([cal['translation_m'],cal['rotation_rad']])
    settings = spec['calibration']
    offset = np.asarray(settings['translation_m'])
    axis = np.asarray(settings['world_rotation_axis'],dtype=float)
    axis /= np.linalg.norm(axis)
    theta = math.radians(settings['rotation_degrees'])
    skew = cross_matrix(axis)
    expected_rotation = np.eye(3)+math.sin(theta)*skew+(1-math.cos(theta))*skew@skew
    scores = {}
    for role,seed in [('fit',spec['calibration_seed']),('check',spec['scene_seed'])]:
        trial = cal[role]
        assert trial['seed'] == seed and trial['control_hz'] == 20 and 'NVIDIA' in trial['renderer']
        assert trial['geometry']['world_parent'] == 0 and len(trial['drift']) == spec['horizon']+1
        ref = world_pose(trial['drift'][0])
        drift = np.max([displacement(ref,world_pose(s)) for s in trial['drift']],axis=0)
        probes = {k:world_pose(s) for k,s in trial['probes'].items()}
        assert np.max(abs(probes['translation'][0]-ref[0]-offset)) < 1e-12
        assert np.max(abs(probes['rotation'][1]@ref[1].T-expected_rotation)) < 1e-10
        assert np.max(abs(np.array(trial['probes']['sign_flip']['free_joint'][3:])+trial['drift'][0]['free_joint'][3:])) < 1e-10
        errors = {k:np.asarray(displacement(ref,v)) for k,v in probes.items()}
        assert np.max(abs(errors['translation']-[np.linalg.norm(offset),0])) < 1e-9
        assert np.max(abs(errors['rotation']-[0,theta])) < 1e-9 and np.max(errors['sign_flip']) < 1e-9
        assert (drift < limits).all()
        assert (errors['translation'] > limits).tolist() == [True,False]
        assert (errors['rotation'] > limits).tolist() == [False,True]
        if role == 'fit':
            independent = (drift+[errors['translation'][0],errors['rotation'][1]])/2
            assert np.max(abs(independent-limits)) < 5e-8
        scores[role] = {'seed':seed,'zero_command_samples':len(trial['drift']),
                        'max_drift_mm':round(float(drift[0]*1000),9),'max_drift_degrees':round(math.degrees(drift[1]),9),
                        'known_translation_mm':round(float(errors['translation'][0]*1000),9),
                        'known_rotation_degrees':round(math.degrees(errors['rotation'][1]),9),'sign_flip_invariant':True}
    return limits,scores


def bottle_scores(data,spec,limits,goal):
    rows = [data['initial_readout'],*data['rows']]
    ref = world_pose(rows[0]['bottle_pose'])
    error = np.array([displacement(ref,world_pose(s['bottle_pose'])) for s in rows])
    # State 2 is both the post-state of the preceding action and the pre-state of action 3.
    over = (error > limits).any(axis=1)
    action_bad = over[:-1] | over[1:]
    switch = spec['switch']
    def phase(start,stop):
        pos,rot = error[start:stop+1].max(axis=0)
        violating = np.flatnonzero(action_bad[start:stop])+start+1
        return {'first_action':start+1,'last_action':stop,'peak_mm':round(float(pos*1000),9),
                'peak_degrees':round(math.degrees(rot),9),'violating_action_count':len(violating),
                'first_violating_action':int(violating[0]) if len(violating) else None}
    prefix,suffix = phase(0,switch),phase(switch,spec['horizon'])
    groups = data['bottle_geometry']
    ids,robot,bowl = set(groups['bottle']),set(groups['robot']),set(data['geometry']['contact_geoms']['bowl'].values())
    assert ids and robot and ids.isdisjoint(robot|bowl) and groups['world_parent'] == 0
    hits = {'robot':[],'bowl':[]}
    for tick,row in enumerate(rows):
        pairs = list(map(tuple,row['bottle_contacts']))
        assert pairs == sorted(set(pairs)) and all(a<=b and (a in ids or b in ids) for a,b in pairs)
        targets = {b if a in ids else a for a,b in pairs}
        for name,geoms in [('robot',robot),('bowl',bowl)]:
            if targets & geoms:
                hits[name].append(tick)
        bowl_pairs = set(map(tuple,row['bowl_contacts']))
        assert {pair for pair in pairs if set(pair) & bowl} == {pair for pair in bowl_pairs if set(pair) & ids}
    bad_ticks = np.flatnonzero(over)
    return {'prefix':prefix,'after_revision':suffix,'compliant_all':not bool(np.any(over)),
            'goal_and_compliance':bool(goal and not over.any()),'first_bad_state_tick':int(bad_ticks[0]) if len(bad_ticks) else None,
            'position_violation_state_ticks':np.flatnonzero(error[:,0]>limits[0]).tolist(),
            'rotation_violation_state_ticks':np.flatnonzero(error[:,1]>limits[1]).tolist(),
            'violating_action_intervals':intervals(action_bad),
            'bottle_robot_contact_ticks':hits['robot'],'bottle_bowl_contact_ticks':hits['bowl']}


def prefix_signature(data,switch,period):
    source,branch = data['queries'][:2]
    if 'prefix_replay' in data:
        source = dict(source,reply=data['prefix_replay']['reference_reply'])
    return {'initial':data['initial_readout'],'bottle_geoms':data['bottle_geometry'],'geometry':data['geometry'],
            'native':data['snapshots'],'source_reply_and_obs':source,'first_two_actions_and_outcomes':data['rows'][:switch],
            'branch_rgb':data['live_camera_sha256'][1] if 'live_camera_sha256' in data else branch['rgb_sha256'],
            'branch_state':branch['proprioception'],
            'discarded_queue':source['reply'][switch:period]}


def verify(out,archive,protocol_file='R1_CONTROL.json',expected_spec=None):
    verify_run_files(out)
    spec,base = read(out/'protocol.json'),read(PACKET/'ATOMIC_CONTROL.json')
    assert spec == (expected_spec if expected_spec is not None else read(PACKET/protocol_file))
    reference_reply = None
    if 'source_replay' in spec:
        replay = spec['source_replay']
        reference = (out if 'layout_study' in spec else PACKET/spec['reference']['archive'])/replay['path']
        assert sha(reference.read_bytes()) == replay['file_sha256'] and replay['controls'] == spec['switch']
        reference_reply = read(reference)['queries'][0]['reply']
    run,meta = read(out/'run.json'),read(out/'runtime_manifest.json')
    assert run['status'] == 'COMPLETED' and run['image_id'] == meta['image_id'] and meta['status'] == 'PASS_IO_ONLY'
    assert meta['resteer_revision'] == base['source_commit'] and meta['openpi_revision'] == base['openpi_commit']
    assert len(meta['artifacts']['files']) == 17 and all(a['crc32c_verified'] for a in meta['artifacts']['files'])
    for name,digest in run['input_sha256'].items():
        assert source_matches(name,digest,out,out.parent,PACKET/'results/2026-11-24-r1-bottle'), name
    assert sha((out/'calibration.json').read_bytes()) == run['frozen_calibration_sha256']
    cal = read(out/'calibration.json')
    limits,calibration = check_calibration(cal,spec)
    before,after = (read(out/f'tokens_{s}.json') for s in ('before','after'))
    assert all(t['full_vs_native_ids_exact'] and t['model']==spec['policy'] for t in (before,after))
    assert before['limit'] == after['limit'] and before['discrete_state_input'] == after['discrete_state_input']
    assert set(before['records']) == {'source',*spec['arms']}
    seen_frames = set()
    def check_frame(digest):
        if digest in seen_frames:
            return
        name = digest+'.png'
        with (archive.open(name) if archive else (out/'frames'/name).open('rb')) as f:
            with Image.open(f) as img:
                pixels = np.asarray(img)
                assert pixels.shape == (224,224,3) and pixels.dtype == np.uint8 and np.ptp(pixels) > 0
                assert sha(pixels.tobytes()) == digest
        seen_frames.add(digest)
    base = dict(base,source_prompt=spec['source_prompt'])
    assert (spec['switch'],spec['replan_controls'],spec['horizon'],spec['repetitions']) == (
        base['shared_source_controls'],base['replan_controls'],base['policy_controls_per_path'],base['repetitions'])
    scores,first,repeats,prefixes,eligible = {},{},{},[],[]
    token_counts = {}
    for repeat in range(1,spec['repetitions']+1):
        order = spec['run_order'][repeat-1] if 'run_order' in spec else spec['arms']
        assert sorted(order) == sorted(spec['arms'])
        for arm in order:
            prompt = spec['arms'][arm]
            name = f'{arm}_{repeat}'
            entry = run['paths'][len(prefixes)]
            assert (entry['arm'],entry['repeat']) == (arm,repeat) and run['frozen_at'] < entry['started_at'] < entry['finished_at']
            data = read(out/f'{name}.json')
            assert data['arm'] == arm
            dispatch = data['queries']
            assert ('prefix_replay' in data) == (reference_reply is not None)
            if reference_reply is not None:
                prefix = data['prefix_replay']
                assert prefix['reference_reply'] == reference_reply and prefix['controls'] == spec['switch']
                assert (prefix['path'],prefix['file_sha256']) == (replay['path'],replay['file_sha256'])
                array(dispatch[0]['reply'],(base['action_horizon'],base['action_dim']))
                dispatch = [dict(dispatch[0],reply=reference_reply),*dispatch[1:]]
            goal,pre = verify_path(dict(data,arm='cabinet',queries=dispatch),{'arm':'cabinet','prompt':prompt},
                                   repeat,base,check_frame)
            if 'first_view' in spec:
                assert len(data['live_camera_sha256']) == len(dispatch)
                for pair in data['live_camera_sha256']:
                    assert set(pair) == set(CAMERAS)
                    for digest in pair.values():
                        check_frame(digest)
            assert data['initial_readout']['bottle_pose'] == cal['check']['drift'][0]
            bottle = bottle_scores(data,spec,limits,goal['requested_at_deadline'])
            start_clear = goal['first_five_clear_ticks_start']
            clear_tick = start_clear+base['release_window']-1 if start_clear is not None else None
            first_bad = bottle['first_bad_state_tick']
            # A descriptive reading at first released placement, separate from the fixed deadline.
            interim = {'tick':clear_tick,'compliant_through_tick':None if clear_tick is None else
                       first_bad is None or first_bad > clear_tick}
            eligible.append(pre and bottle['prefix']['violating_action_count'] == 0)
            scores[name] = {'bowl':goal,'bottle':bottle,'at_first_five_released_posthoc':interim}
            tokens = after['records'][name]
            assert len(tokens) == len(data['queries']) and all(0 < t['tokens'] <= after['limit'] for t in tokens)
            if not after['discrete_state_input']:
                expected = before['records']['source']+before['records'][arm]*(len(tokens)-1)
                assert all((a['tokens'],a['ids_sha256']) == (b['tokens'],b['ids_sha256'])
                           for a,b in zip(tokens,expected))
            token_counts[name] = list(sorted({t['tokens'] for t in tokens[1:]}))
            prefixes.append(prefix_signature(data,spec['switch'],spec['replan_controls']))
            body = {k:v for k,v in data.items() if k != 'repeat'}
            if repeat == 1:
                first[arm] = body
            else:
                repeats[arm] = body == first[arm]
    assert len(prefixes) == len(run['paths']) and set(scores) == set(after['records'])
    frame_names = set(archive.namelist()) if archive else {p.name for p in (out/'frames').iterdir()}
    assert frame_names == {digest+'.png' for digest in seen_frames}
    if (out/'views').is_dir():
        views = {k:v['final_observation']['rgb_sha256'][CAMERAS[0]] for k,v in first.items()}
        views['branch'] = prefixes[0]['branch_rgb'][CAMERAS[0]]
        for name,digest in views.items():
            with Image.open(out/'views'/f'{name}.png') as img:
                assert sha(np.asarray(img).tobytes()) == digest
    matched = {k:all(p[k] == prefixes[0][k] for p in prefixes) for k in prefixes[0]}
    if (out/'fixed_action_replay.json').is_file():
        replay = read(out/'fixed_action_replay.json')
        assert set(replay['paths']) == set(scores) and replay['policy_queries'] == 0
        assert replay['replayed_controls'] == len(prefixes)*spec['horizon']
        for path in replay['paths'].values():
            assert path['actions'] == spec['horizon'] and path['native_rows_and_bottle_poses_exact']
            assert all(all(fields.values()) for fields in path['snapshots'].values())
        for arm,diagnosis in replay['original_native_restart_comparison'].items():
            a,b = first[arm],read(out/f'{arm}_2.json')
            first_command = next((x['tick'] for x,y in zip(a['rows'],b['rows']) if x['dispatched']!=y['dispatched']),None)
            first_row = next((x['tick'] for x,y in zip(a['rows'],b['rows']) if x!=y),None)
            assert (first_command,first_row) == (diagnosis['first_unequal_command'],diagnosis['first_unequal_raw_row'])
    conditions = {arm:{'native_goal':sum(v['bowl']['requested_at_deadline'] for k,v in scores.items() if k.startswith(arm+'_')),
                       'bottle_compliance':sum(v['bottle']['compliant_all'] for k,v in scores.items() if k.startswith(arm+'_')),
                       'joint':sum(v['bottle']['goal_and_compliance'] for k,v in scores.items() if k.startswith(arm+'_')),
                       'release_final_five':sum(v['bowl']['released_last_five'] for k,v in scores.items() if k.startswith(arm+'_'))}
                  for arm in spec['arms']}
    disposition = 'UNRESOLVED_PREFIX_OR_REPEAT'
    if all(matched.values()) and all(eligible) and all(repeats.values()):
        if all(v['bottle']['compliant_all'] and not (v['bottle']['bottle_robot_contact_ticks'] or v['bottle']['bottle_bowl_contact_ticks']) for v in scores.values()):
            disposition = 'BOTH_COMPLY_WITHOUT_SAMPLED_CONTACT_LOW_CONSTRAINT_INFORMATION'
        else:
            disposition = 'VALID_PAIR_REPORT_GOAL_AND_VIOLATION_SEPARATELY'
    outcomes = {}
    for arm in spec['arms']:
        keys = [(
            s['bowl']['requested_at_deadline'],s['bowl']['first_native_tick'],s['bottle']['goal_and_compliance'],
            s['bottle']['first_bad_state_tick'],s['at_first_five_released_posthoc']['tick']
        ) for k,s in scores.items() if k.startswith(arm+'_')]
        outcomes[arm] = all(k==keys[0] for k in keys)
    return {'decision':disposition,'independent_scenes':1,'seed':spec['scene_seed'],'conditions':conditions,
            'calibration':calibration,'translation_tolerance_mm':limits[0]*1000,'rotation_tolerance_degrees':math.degrees(limits[1]),
            'exact_prefix_across_all':matched,'pre_eligible':eligible,'exact_restarts':repeats,
            'same_endpoints_first_goal_first_violation_and_first_released_window':outcomes,
            'model_queries':len(prefixes)*base['queries_per_path'],'policy_controls':len(prefixes)*spec['horizon'],
            'warmup_controls_rollouts':len(prefixes)*spec['warmup_controls'],'control_hz':20,
            'checked_pose_samples':len(prefixes)*(spec['horizon']+1),'checked_native_goal_flags':2*len(prefixes)*(spec['horizon']+1),
            'unique_rgb':len(seen_frames),'token_limit':after['limit'],'source_tokens':before['records']['source'][0]['tokens'],
            'post_revision_token_counts':token_counts,'verified_untruncated_actual_queries':sum(map(len,after['records'].values())),
            'per_path':scores,'measurement':'Poses and contacts at sampled control boundaries. Joint score uses the t0 reference throughout.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    out = parser.parse_args().run
    frames = out/'frames.zip'
    with (zipfile.ZipFile(frames) if frames.exists() else nullcontext()) as archive:
        print(json.dumps(verify(out,archive),indent=2,allow_nan=False))
