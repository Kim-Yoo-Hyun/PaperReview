"""Score scene 11's archived neutral-bottle actions on both physical bottle positions."""
import argparse
import json
from pathlib import Path
import zipfile

import numpy as np

from run_bottle_xy import partners
from verify_atomic import PACKET, read, sensor_flags, sha
from verify_neutral_layouts import transport_motion
from verify_r1 import bottle_scores, check_calibration


DESIGN = 'R1_COMMAND_CROSS.json'


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()


def commands_sha(rows):
    values = np.asarray([r['dispatched'] for r in rows], dtype='<f8')
    assert values.shape == (300,7) and np.isfinite(values).all()
    return sha(values.tobytes())


def source_data():
    design = read(PACKET/DESIGN)
    ref = PACKET/design['source']['archive']
    for name, expected in design['source']['sha256'].items():
        assert sha((ref/name).read_bytes()) == expected, name
    history = read(ref/'verification.json')
    assert history['decision'] == 'ONLY_SCENE_11_SWITCHED_TO_BOTTLE'
    cells = {}
    with zipfile.ZipFile(ref/'study.zip') as archive:
        image = json.loads(archive.read('runtime_manifest.json'))['image_id']
        for pos in design['positions']:
            key = f"{design['scene']}-{pos}"
            def load(name):
                return json.loads(archive.read(f'seed-{key}/{name}.json'))
            spec, prefix = load('protocol'), load('prefix')
            assert spec['scene_seed'] == design['scene'] and spec['bottle_xy_seed'] == pos
            assert spec['horizon'] == design['horizon'] and spec['switch'] == design['branch']
            assert history['layouts'][key]['qualification']['eligible']
            limits, _ = check_calibration(load('calibration'), spec)
            tapes = {}
            for rep in design['repeats']:
                tape = load(f'B_{rep}')
                assert tape['arm'] == design['wording'] == 'B' and tape['repeat'] == rep
                assert tape['status'] == 'COMPLETED' and tape['control_hz'] == design['control_hz']
                assert [r['tick'] for r in tape['rows']] == list(range(1,design['horizon']+1))
                assert commands_sha(tape['rows']) == design['command_sha256'][str(pos)][rep-1]
                assert all(q['prompt'] == spec['arms']['B'] for q in tape['queries'][1:])
                assert [r['dispatched'] for r in tape['rows'][:2]] == [r['dispatched'] for r in prefix['rows']]
                tapes[rep] = tape
            cells[pos] = dict(spec=spec,prefix=prefix,tapes=tapes,limits=limits,previous=history['layouts'][key]['paths'])
    left,right = (cells[k] for k in design['positions'])
    assert left['spec']['arms']['B'] == right['spec']['arms']['B']
    assert [r['dispatched'] for r in left['prefix']['rows']] == [r['dispatched'] for r in right['prefix']['rows']]
    return design, cells, image


def schedule(design, batch):
    positions = design['positions']
    routes = [(origin,target,rep) for origin in positions for target in positions for rep in design['repeats']]
    if batch == 'second':
        routes.reverse()
    return [r for r in routes if r[0] == r[1]] + [r for r in routes if r[0] != r[1]]


def path_id(origin, target, rep):
    return f'from-{origin}-to-{target}-B{rep}'


def physical_row(row):
    return {k:v for k,v in row.items() if k not in ('query','index')}


def check_path(trace, views, cells, origin, target, rep):
    source, receiver = cells[origin]['tapes'][rep], cells[target]
    prefix = receiver['prefix']
    assert trace['geometry'] == prefix['geometry'] and trace['bottle_geometry'] == prefix['bottle_geometry']
    assert trace['initial_readout'] == prefix['initial_readout']
    assert trace['rows'][:2] == [physical_row(r) for r in prefix['rows']]
    assert set(trace['snapshots']) == {'0','2','terminal'}
    assert all(trace['snapshots'][k] == v for k,v in prefix['snapshots'].items())
    assert [r['tick'] for r in trace['rows']] == list(range(1,301))
    assert [r['dispatched'] for r in trace['rows']] == [r['dispatched'] for r in source['rows']]
    assert [v['tick'] for v in views] == [q['completed_controls'] for q in source['queries']] + [300]
    for view, expected in zip(views[:2], prefix['queries']):
        assert view['proprioception'] == expected['proprioception'] and view['rgb_sha256'] == expected['rgb_sha256']
    if origin == target:
        assert trace['rows'] == [physical_row(r) for r in source['rows']]
        assert trace['snapshots']['terminal'] == source['final_state']
        assert all(v['proprioception'] == q['proprioception'] for v,q in zip(views,[*source['queries'],source['final_observation']]))


def score_path(trace, receiver):
    spec, limits = receiver['spec'], receiver['limits']
    geometry = trace['geometry']
    groups = {k:set(v.values()) for k,v in geometry['contact_geoms'].items()}
    size = np.asarray(geometry['cabinet_site_half_size'])
    rows = [trace['initial_readout'],*trace['rows']]
    flags = [sensor_flags(row,groups,size) for row in rows]
    goals = [f['cabinet'] for f,_ in flags]
    first_goal = next((i for i,g in enumerate(goals) if g), None)
    bowl_cabinet = [i for i,r in enumerate(rows) if partners(r,'bowl',groups['bowl']) & groups['cabinet']]
    bottle = bottle_scores(trace,spec,limits,goals[-1])
    first_robot = next(iter(bottle['bottle_robot_contact_ticks']),None)
    motion, transported = transport_motion(trace,limits[0]*1000,first_robot,first_goal)
    joint = bottle['goal_and_compliance']
    label = 'BOWL_AND_PROTECTED_BOTTLE' if joint else 'BOTTLE_TRANSPORT' if transported else 'OTHER'
    return {'selection':label,'joint_at_300':joint,'goal_at_300':goals[-1],'bottle_compliant_all':bottle['compliant_all'],
            'bowl_released_last_five':all(f['cabinet'] and not contact for f,contact in flags[-5:]),
            'first_native_goal':first_goal,'first_robot_contact':first_robot,'first_violation_tick':bottle['first_bad_state_tick'],
            'first_bowl_cabinet_contact':next(iter(bowl_cabinet),None),'bowl_cabinet_contact_at_deadline':300 in bowl_cabinet,
            'bottle_transport_signature':transported,'peak_bottle_rotation_deg':max(bottle[k]['peak_degrees'] for k in ('prefix','after_revision')),
            'motion':motion}


def assess(bundle):
    design, cells, image = source_data()
    reports, trajectories, recordings, self_rgb = {}, {}, {}, {}
    with zipfile.ZipFile(bundle) as z:
        assert z.testzip() is None and len(set(z.namelist())) == len(z.namelist())
        assert json.loads(z.read('design.json')) == design
        known = {'design.json','first.json','second.json'}
        prior_end = None
        for batch in ('first','second'):
            meta = json.loads(z.read(batch+'.json'))
            assert meta['image_id'] == image and meta['policy_queries'] == 0 and 'NVIDIA' in meta['renderer']
            assert (prior_end is None or prior_end <= meta['started_at']) and meta['started_at'] < meta['finished_at']
            prior_end = meta['finished_at']
            for name,h in meta['source_sha256'].items():
                item = 'executed_sources/'+name
                known.add(item)
                assert sha(z.read(item)) == h
            schedule_rows = schedule(design,batch)
            assert meta['order'] == [path_id(*route) for route in schedule_rows]
            assert set(meta['paths']) == set(meta['order'])
            reports[batch], trajectories[batch], recordings[batch] = {}, {}, {}
            self_rgb[batch] = {}
            for origin,target,rep in schedule_rows:
                key = path_id(origin,target,rep)
                refs = meta['paths'][key]
                items = []
                for k in ('trajectory','observations'):
                    name = 'objects/'+refs[k]+'.json'
                    known.add(name)
                    raw = z.read(name)
                    assert sha(raw) == refs[k]
                    items.append(json.loads(raw))
                trace, views = items
                check_path(trace,views,cells,origin,target,rep)
                assert commands_sha(trace['rows']) == design['command_sha256'][str(origin)][rep-1]
                score = score_path(trace,cells[target])
                if origin == target:
                    old = cells[target]['previous'][f'B_{rep}']
                    native = cells[origin]['tapes'][rep]
                    native_views = [*native['queries'],native['final_observation']]
                    self_rgb[batch][key] = [{'tick':v['tick'],'camera':cam}
                        for v,q in zip(views,native_views) for cam in v['rgb_sha256'] if v['rgb_sha256'][cam] != q['rgb_sha256'][cam]]
                    assert all(score[k] == old[k] for k in ('joint_at_300','goal_at_300','bottle_compliant_all','first_native_goal',
                               'first_robot_contact','first_violation_tick','first_bowl_cabinet_contact','bowl_cabinet_contact_at_deadline',
                               'bottle_transport_signature','bowl_released_last_five','motion'))
                reports[batch][key], trajectories[batch][key], recordings[batch][key] = score,refs['trajectory'],views
        assert set(z.namelist()) == known
    cross_a = [path_id(11,19,r) for r in design['repeats']]
    cross_b = [path_id(19,11,r) for r in design['repeats']]
    bowl,bottle = 'BOWL_AND_PROTECTED_BOTTLE','BOTTLE_TRANSPORT'
    def all_selected(keys, label):
        return all(batch[k]['selection'] == label for batch in reports.values() for k in keys)
    assert all_selected([path_id(11,11,r) for r in design['repeats']],bowl)
    assert all_selected([path_id(19,19,r) for r in design['repeats']],bottle)
    if all_selected(cross_a,bowl) and all_selected(cross_b,bottle):
        decision = 'ENDPOINT_FOLLOWS_COMMAND_STREAM_BOTH_DIRECTIONS'
    elif all_selected(cross_a,bottle) and all_selected(cross_b,bowl):
        decision = 'ENDPOINT_FOLLOWS_PHYSICAL_POSITION_BOTH_DIRECTIONS'
    else:
        decision = 'REPORT_DIRECTIONAL_OR_OTHER_OUTCOMES'
    rgb = {}
    for key, first in recordings['first'].items():
        second = recordings['second'][key]
        rgb[key] = [{'tick':a['tick'],'camera':cam} for a,b in zip(first,second) for cam in a['rgb_sha256']
                    if a['rgb_sha256'][cam] != b['rgb_sha256'][cam]]
    return {'decision':decision,'policy_queries':0,'controls_per_batch':len(trajectories['first'])*design['horizon'],
            'distinct_command_streams':len({h for reps in design['command_sha256'].values() for h in reps}),
            'physical_traces_exact_between_batches':{k:h==trajectories['second'][k] for k,h in trajectories['first'].items()},
            'rgb_differences_between_batches':rgb,'self_rgb_differences_from_native':self_rgb,'paths':reports}


def verify_folder(folder):
    checksum = folder/'SHA256SUMS'
    entries = [line.split('  ',1) for line in checksum.read_text().splitlines()]
    assert sorted(n for _,n in entries) == ['replays.zip','verification.json']
    assert all(sha((folder/n).read_bytes())==h for h,n in entries)
    result = assess(folder/'replays.zip')
    assert result == read(folder/'verification.json')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    print(json.dumps(verify_folder(parser.parse_args().folder),indent=2,allow_nan=False))
