"""Independently check policy inputs, commands and native placement predicates from an R8 run."""
import argparse
from contextlib import nullcontext
import hashlib
import json
from pathlib import Path
import zipfile

import numpy as np
from PIL import Image


PACKET = Path(__file__).resolve().parent
CAMERAS = ('observation/image', 'observation/wrist_image')


def read(path):
    return json.loads(path.read_bytes())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify_run_files(out):
    manifest = out/'SHA256SUMS'
    if not manifest.is_file():
        return
    def entries(data):
        pairs = [line.split('  ', 1) for line in data.decode().splitlines()]
        by_name = {name:digest for digest,name in pairs}
        assert len(by_name)==len(pairs)
        return by_name
    current = entries(manifest.read_bytes())
    assert set(current)=={f.relative_to(out).as_posix() for f in out.rglob('*') if f.is_file() and f!=manifest}
    assert all(sha((out/name).read_bytes())==digest for name,digest in current.items())
    if 'execution-files.zip' in current:
        with zipfile.ZipFile(out/'execution-files.zip') as z:
            old = entries(z.read('original-SHA256SUMS'))
            bundled = {name for name in old if name.startswith(('logs/','executed_sources/'))}
            assert sorted(z.namelist())==sorted(bundled|{'original-SHA256SUMS'})
            assert all(sha(z.read(name))==old[name] for name in bundled)
            assert bundled.isdisjoint(current)
            assert all(current.get(n)==h for n,h in old.items() if n not in bundled)


def source_matches(name, digest, *folders):
    for folder in folders:
        path = folder/'executed_sources'/name
        if path.is_file() and sha(path.read_bytes())==digest:
            return True
        bundle = folder/'execution-files.zip'
        if bundle.is_file():
            with zipfile.ZipFile(bundle) as z:
                member = 'executed_sources/'+name
                if member in z.namelist() and sha(z.read(member))==digest:
                    return True
    path = PACKET/name
    return path.is_file() and sha(path.read_bytes())==digest


def array(value, shape):
    v = np.asarray(value)
    assert v.shape == shape and np.isfinite(v).all()
    return v


def verify_smoke(out, spec, run):
    smoke = out/'smoke'
    meta, tape = read(smoke/'runtime_manifest.json'), read(smoke/'native_result.json')
    assert meta['status'] == tape['status'] == 'PASS_IO_ONLY' and meta['native'] == tape
    assert meta['image_id'] == run['image_id'] and meta['resteer_revision'] == spec['source_commit']
    assert meta['openpi_revision'] == spec['openpi_commit']
    for filename in ('ARTIFACTS.json','native_probe.py','inside.py'):
        assert sha((PACKET/filename).read_bytes()) == meta['recipe_sha256'][filename]
    expected = read(PACKET/'ARTIFACTS.json')['files']
    files = meta['artifacts']['files']
    assert len(expected) == len(files) == 17
    for original, checked in zip(expected, files):
        assert (original['relative_path'],original['generation'],original['size']) == (
            checked['path'],checked['generation'],checked['size'])
        assert checked['crc32c_verified'] and len(bytes.fromhex(checked['sha256'])) == 32
        assert not original.get('expected_sha256') or original['expected_sha256'] == checked['sha256']
    assert tape['inference_count'] == len(tape['calls']) == 2 and tape['control_hz'] == 20
    assert tape['action_count'] == len(tape['steps']) == 7
    with np.load(smoke/'policy_observations.npz', allow_pickle=False) as images:
        for i, (call,arm) in enumerate(zip(tape['calls'],spec['arms'])):
            assert call['prompt'] == arm['prompt']
            array(call['actions'],(10,7))
            array(call['state'],(8,))
            for key in CAMERAS:
                frame = images[f"query{i}_{key.split('/')[-1]}"]
                assert frame.shape == (224,224,3) and frame.dtype == np.uint8 and np.ptp(frame) > 0
                assert sha(frame.tobytes()) == call['image_sha256'][key]
    for i, step in enumerate(tape['steps']):
        query, index = (0,i) if i < 2 else (1,i-2)
        assert (step['step'],step['call'],step['action_index']) == (i,query,index)
        assert step['prompt'] == tape['calls'][query]['prompt']
        assert step['action'] == tape['calls'][query]['actions'][index]
    return tape, {'status':tape['status'], 'model_queries':2, 'executed_controls':7,
                  'verified_assets':len(files), 'asset_bytes':sum(f['size'] for f in files)}


def sensor_flags(row, groups, size):
    pairs = [tuple(pair) for pair in row['bowl_contacts']]
    assert pairs == sorted(set(pairs))
    assert all(a <= b and (a in groups['bowl'] or b in groups['bowl']) for a,b in pairs)
    partners = {b if a in groups['bowl'] else a for a,b in pairs}
    bowl = array(row['bowl_xyz'],(3,))
    plate = array(row['plate_xyz'],(3,))
    site = array(row['cabinet_site_xyz'],(3,))
    relative = array(row['cabinet_site_mat'],(3,3)) @ (bowl-site)
    above_plate = plate[2] <= bowl[2] and np.linalg.norm(bowl[:2]-plate[:2]) < 0.1
    above_cabinet = size[2]-0.005 < relative[2] < size[2]+0.10 and (abs(relative[:2]) < size[:2]).all()
    goals = {'plate':bool(above_plate and partners & groups['plate']),
             'cabinet':bool(above_cabinet and partners & groups['cabinet'])}
    assert goals == row['goals'], (goals,row['goals'])
    return goals, bool(partners & groups['gripper'])


def intervals(values):
    spans = []
    for tick, flag in enumerate(values,1):
        if not flag:
            continue
        if spans and spans[-1][1] == tick-1:
            spans[-1][1] = tick
        else:
            spans.append([tick,tick])
    return spans


def verify_path(data, arm, rep, spec, check_image):
    assert data['status'] == 'COMPLETED' and (data['arm'],data['repeat']) == (arm['arm'],rep)
    assert data['control_hz'] == 20 and 'NVIDIA' in data['renderer']
    geom = data['geometry']
    groups = {k:set(v.values()) for k,v in geom['contact_geoms'].items()}
    assert all(groups.values()) and sum(map(len,groups.values())) == len(set.union(*groups.values()))
    size = array(geom['cabinet_site_half_size'],(3,))
    assert (size > 0).all()
    initial, initial_contact = sensor_flags(data['initial_readout'],groups,size)
    switch, period = spec['shared_source_controls'], spec['replan_controls']
    horizon = spec['policy_controls_per_path']
    query_times = [0,*range(switch,horizon,period)]
    queries, rows = data['queries'], data['rows']
    assert len(queries) == len(query_times) == spec['queries_per_path'] and len(rows) == horizon
    assert data['discarded_at_switch'] == period-switch
    for q,t in zip(queries,query_times):
        assert (q['completed_controls'],q['prompt']) == (t,spec['source_prompt'] if t < switch else arm['prompt'])
        array(q['reply'],(spec['action_horizon'],spec['action_dim']))
    for observation in [*queries,data['final_observation']]:
        array(observation['proprioception'],(8,))
        assert set(observation['rgb_sha256']) == set(CAMERAS)
        for digest in observation['rgb_sha256'].values():
            check_image(digest)
    for tick in (0,switch,horizon):
        state = data['final_state'] if tick == horizon else data['snapshots'][str(tick)]
        assert state['control_tick'] == spec['warmup_controls']+tick
        assert np.isfinite(state['integration_state']).all() and len(state['integration_state']) > 100
        assert len(bytes.fromhex(state['rng_sha256'])) == 32
        array(state['gripper_command_state'],(2,))
        array(state['controller']['goal_pos'],(3,))
    requested = arm['arm']
    other = 'cabinet' if requested == 'plate' else 'plate'
    holds, others, released, contacts = [], [], [], []
    for i,row in enumerate(rows):
        index_query = 0 if i < switch else 1+(i-switch)//period
        index_action = i-query_times[index_query]
        assert (row['tick'],row['query'],row['index']) == (i+1,index_query,index_action)
        assert row['dispatched'] == queries[index_query]['reply'][index_action]
        flags,contact = sensor_flags(row,groups,size)
        holds.append(flags[requested])
        others.append(flags[other])
        released.append(flags[requested] and not contact)
        contacts.append(contact)
    native_spans, release_spans = intervals(holds),intervals(released)
    scores = {'requested_at_deadline':holds[-1], 'other_at_deadline':others[-1],
              'released_last_five':all(released[-spec['release_window']:]),
              'first_native_tick':native_spans[0][0] if native_spans else None,
              'first_five_clear_ticks_start':next((a for a,b in release_spans if b-a+1 >= spec['release_window']),None),
              'native_intervals':native_spans, 'other_destination_intervals':intervals(others),
              'released_intervals':release_spans, 'bowl_gripper_contact_intervals':intervals(contacts),
              'terminal_agent_view':data['final_observation']['rgb_sha256'][CAMERAS[0]]}
    eligible = not (any(initial.values()) or initial_contact or holds[switch-1] or others[switch-1] or contacts[switch-1])
    return scores, eligible


def verify(out, frames_zip):
    verify_run_files(out)
    run = read(out/'run.json')
    spec = read(out/'protocol.json')
    assert run['status'] == 'COMPLETED' and spec == read(PACKET/'ATOMIC_CONTROL.json')
    for name,digest in run['executed_sha256'].items():
        assert sha((PACKET/name).read_bytes()) == digest, name
    tape, qualification = verify_smoke(out,spec,run)
    image_ids = set()

    def check_image(digest):
        if digest in image_ids:
            return
        assert len(bytes.fromhex(digest)) == 32
        name = f'{digest}.png'
        with (frames_zip.open(name) if frames_zip else (out/'frames'/name).open('rb')) as f:
            with Image.open(f) as img:
                rgb = np.asarray(img)
                assert rgb.shape == (224,224,3) and rgb.dtype == np.uint8 and np.ptp(rgb) > 0
                assert sha(rgb.tobytes()) == digest
        image_ids.add(digest)

    branches, summaries, eligibility = [], {}, []
    repeat_checks, first = {}, {}
    for rep in range(1,spec['repetitions']+1):
        for arm in spec['arms']:
            name = arm['arm']
            entry = run['paths'][len(branches)]
            assert (entry['repeat'],entry['arm']) == (rep,name) and entry['finished_at']
            data = read(out/f'{name}_{rep}.json')
            score, eligible = verify_path(data,arm,rep,spec,check_image)
            eligibility.append(eligible)
            summaries[f'{name}_{rep}'] = score
            q0, qb = data['queries'][:2]
            branches.append({'geometry':data['geometry'],'initial_readout':data['initial_readout'],
                             'snapshots':data['snapshots'],'first_query':q0,'first_two_rows':data['rows'][:2],
                             'branch_images':qb['rgb_sha256'],'branch_proprioception':qb['proprioception'],
                             'discarded_queue':q0['reply'][spec['shared_source_controls']:spec['replan_controls']]})
            comparable = {k:v for k,v in data.items() if k != 'repeat'}
            if rep == 1:
                first[name] = comparable
            else:
                repeat_checks[name] = {k:v == first[name][k] for k,v in comparable.items()}
    assert len(run['paths']) == len(branches)
    stored = set(frames_zip.namelist()) if frames_zip else {p.name for p in (out/'frames').iterdir()}
    assert stored == {f'{digest}.png' for digest in image_ids}
    if (out/'views').is_dir():
        previews = {'branch':branches[0]['branch_images'][CAMERAS[0]],
                    **{name:d['final_observation']['rgb_sha256'][CAMERAS[0]] for name,d in first.items()}}
        for name,digest in previews.items():
            with Image.open(out/'views'/f'{name}.png') as img:
                assert sha(np.asarray(img).tobytes()) == digest
    matched = {k:all(b[k] == branches[0][k] for b in branches) for k in branches[0]}
    consistent = all(all(v.values()) for v in repeat_checks.values())
    exclusive = all(v['requested_at_deadline'] and not v['other_at_deadline'] for v in summaries.values())
    decision = 'UNRESOLVED_PREFIX_OR_REPEAT'
    if all(matched.values()) and all(eligibility) and consistent:
        decision = 'BOTH_ATOMIC_TARGETS_SUPPORTED_ON_FIXTURE' if exclusive else 'ATOMIC_TARGET_MISS_ON_FIXTURE'
    smoke_input_match = [tape['calls'][i]['image_sha256'] == first['cabinet']['queries'][i]['rgb_sha256']
                         and tape['calls'][i]['state'] == first['cabinet']['queries'][i]['proprioception']
                         for i in range(2)]
    return {'decision':decision,'qualification':qualification,'scene_seed':spec['environment_seed'],
            'independent_layouts':1, 'repeated_runs':len(branches), 'control_hz':20,
            'model_queries':len(branches)*spec['queries_per_path'],
            'policy_controls':len(branches)*spec['policy_controls_per_path'],
            'warmup_controls':len(branches)*spec['warmup_controls'],
            'native_flags_recomputed':2*len(branches)*(1+spec['policy_controls_per_path']),
            'verified_unique_rgb_frames':len(image_ids),'prefix_exact_across_all_paths':matched,
            'branch_eligible_each':eligibility,'per_arm_exact_replay':repeat_checks,'path_scores':summaries,
            'separate_smoke_input_match_vs_cabinet':smoke_input_match,
            'scope':'One unconstrained R8 fixture, one checkpoint and policy key. No R1/R4 or semantic comparison.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    args = parser.parse_args()
    archive = args.run/'frames.zip'
    with (zipfile.ZipFile(archive) if archive.exists() else nullcontext()) as frames:
        print(json.dumps(verify(args.run,frames), indent=2))
