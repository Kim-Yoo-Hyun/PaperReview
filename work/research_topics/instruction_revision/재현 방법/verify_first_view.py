"""Verify the first-query intervention, score the physical paths and compare dispatched blocks."""
import argparse
from io import BytesIO
import json
from pathlib import Path

import numpy as np
from PIL import Image

from run_bottle_xy import partners
from run_first_view import inputs, protocol
from verify_atomic import CAMERAS, read, sha
from verify_command_cross import score_path
from verify_layouts import check_saved_replays, unpack
from verify_r1 import check_calibration, prefix_signature, verify


BOWL = 'BOWL_AND_PROTECTED_BOTTLE'
BOTTLE = 'BOTTLE_TRANSPORT'


def classify(selections):
    if selections['11-11'] != [BOWL]*2 or selections['19-19'] != [BOTTLE]*2:
        return 'OWN_CONTROLS_NOT_REPRODUCED'
    a,b = selections['11-19'],selections['19-11']
    if len(set(a)) != 1 or len(set(b)) != 1 or 'OTHER' in (a[0],b[0]):
        return 'MIXED_OR_OTHER_CROSSED_OUTCOMES'
    return {(BOTTLE,BOWL):'FIRST_QUERY_SWITCHES_BOTH_DIRECTIONS',
            (BOWL,BOTTLE):'NEITHER_ENDPOINT_SWITCHES',
            (BOTTLE,BOTTLE):'ONLY_PHYSICAL_11_SWITCHES_TO_BOTTLE',
            (BOWL,BOWL):'ONLY_PHYSICAL_19_SWITCHES_TO_BOWL'}[a[0],b[0]]


def received(folder, name, tape, spec, prefix, model_at=None):
    records = [json.loads(line) for line in (folder/f'{name}_receipts.jsonl').read_text().splitlines()]
    expected_ticks = [0,*range(spec['switch'],spec['horizon'],spec['replan_controls'])]
    queries,live = tape['queries'],tape['live_camera_sha256']
    assert len(records) == len(live) == len(expected_ticks) == 61
    assert [q['completed_controls'] for q in queries] == expected_ticks
    assert live[:2] == [q['rgb_sha256'] for q in prefix['queries']]
    assert queries[1]['proprioception'] == prefix['queries'][1]['proprioception']
    keys = [records[0]['rng_before']]
    assert keys[0] == [0,spec['policy_rng_seed']]
    for idx,(record,q,actual) in enumerate(zip(records,queries,live)):
        expected = spec['first_view']['rgb_sha256'] if idx == 1 else actual
        prompt = spec['source_prompt'] if idx == 0 else spec['arms'][tape['arm']]
        override = (model_at or {}).get(idx,{})
        assert q['rgb_sha256'] == expected and record['rgb_sha256'] == override.get('rgb_sha256',expected)
        assert record['prompt'] == q['prompt'] == prompt
        assert record['proprioception'] == q['proprioception'] and len(q['proprioception']) == 8
        assert record['actions_sha256'] == sha(np.asarray(override.get('reply',q['reply']),dtype='<f8').tobytes())
        assert record['rng_before'] == keys[-1] and len(record['rng_after']) == 2
        keys.append(record['rng_after'])
    assert len(set(map(tuple,keys))) == len(keys)
    assert expected_ticks[2] == 7
    block = [row['dispatched'] for row in tape['rows'][2:7]]
    assert block == queries[1]['reply'][:5]
    return keys,np.array(block)


def contact(tape, spec, limits):
    scored = score_path(tape,dict(spec=spec,limits=limits))
    robot = set(tape['bottle_geometry']['robot'])
    bowl = set(tape['geometry']['contact_geoms']['bowl'].values())
    rows = [tape['initial_readout'],*tape['rows']]
    bowl_tick = next((i for i,row in enumerate(rows) if partners(row,'bowl',bowl) & robot),None)
    bottle_tick = scored['first_robot_contact']
    touches = {obj:tick for obj,tick in [('bowl',bowl_tick),('bottle',bottle_tick)] if tick is not None}
    first_tick = min(touches.values(),default=None)
    return dict(scored, first_robot_bowl_contact=bowl_tick, first_robot_bottle_contact=bottle_tick,
                first_object_contact_tick=first_tick, first_objects=[obj for obj,tick in touches.items() if tick == first_tick])


def action_difference(block, reference):
    delta = np.abs(block-reference)
    return {'exact':bool(np.array_equal(block,reference)), 'translation_max_abs':float(delta[:,:3].max()),
            'rotation_max_abs':float(delta[:,3:6].max()), 'gripper_max_abs':float(delta[:,6].max())}


def assessment(out):
    design,cells,previous = inputs()
    assert read(out/'study.json') == design
    run,gates,controls = (read(out/name) for name in ('run.json','gates.json','controls.json'))
    assert run['status'] == 'COMPLETED' and run['jax_memory_fraction'] == '0.50'
    assert gates['started_at'] < gates['frozen_at'] == run['frozen_at'] < run['finished_at']
    sources = out/'executed_sources'
    assert run['input_sha256'] == {f.name:sha(f.read_bytes()) for f in sources.iterdir()}
    runtime = read(out/'runtime_manifest.json')
    assert runtime['image_id'] == run['image_id'] == previous['image_id']
    assert runtime['artifacts']['files'] == previous['artifacts']['files']
    assert list(gates['prefixes']) == [f'{p}-{d}' for p,d in design['cells']]
    if (out/'execution-log-index.json').exists():
        combined = (out/'execution.log').read_bytes()
        index = read(out/'execution-log-index.json')
        expected = {f'seed-{p}-{d}/logs/B_{r}_{role}.log' for p,d in design['cells']
                    for r in design['repeats'] for role in ('sim','server')}
        assert set(index) == expected
        offset = 0
        for item in index.values():
            assert item['offset'] == offset
            offset += item['bytes']
            assert sha(combined[item['offset']:offset]) == item['sha256']
        assert offset == len(combined)
    layouts,blocks,selections = {},{},{}
    schedule = None
    previous_end = gates['frozen_at']
    for physical,donor in design['cells']:
        key = f'{physical}-{donor}'
        folder = out/f'seed-{key}'
        host = cells[physical]
        spec = protocol(design,cells,physical,donor)
        for filename in ('prefix.json','calibration.json'):
            assert (folder/filename).read_bytes() == host['raw'][filename]
        assert gates['prefixes'][key] == dict(eligible=True,prefix_sha256=spec['source_replay']['file_sha256'])
        assert read(folder/'runtime_manifest.json') == runtime
        cell_run = read(folder/'run.json')
        assert cell_run['input_sha256'] == run['input_sha256'] and cell_run['frozen_at'] == run['frozen_at']
        assert previous_end < cell_run['paths'][0]['started_at'] < cell_run['finished_at'] <= run['finished_at']
        previous_end = cell_run['finished_at']
        if physical == donor:
            assert cell_run['finished_at'] < controls['checked_at']
        else:
            assert controls['checked_at'] < cell_run['paths'][0]['started_at']
        raw_score = verify(folder,None,expected_spec=spec)
        assert all(raw_score['exact_prefix_across_all'].values()) and all(raw_score['pre_eligible'])
        assert raw_score['post_revision_token_counts'] == {'B_1':[22],'B_2':[22]} and raw_score['source_tokens'] == 20
        original_tokens = json.loads(host['raw']['tokens_before.json'])['records']
        assert read(folder/'tokens_before.json')['records'] == {k:original_tokens[k] for k in ('source','B')}
        limits,_ = check_calibration(read(folder/'calibration.json'),spec)
        paths = {}
        for repeat in design['repeats']:
            name = f'B_{repeat}'
            tape = read(folder/f'{name}.json')
            assert tape['control_hz'] == design['hz'] and len(tape['rows']) == design['controls']
            assert prefix_signature(tape,2,5) == prefix_signature(host['prefix'],2,5)
            keys,block = received(folder,name,tape,spec,host['prefix'])
            if schedule is None:
                schedule = keys
            assert keys == schedule
            blocks[key,name] = block
            paths[name] = contact(tape,spec,limits)
            assert paths[name]['joint_at_300'] == raw_score['per_path'][name]['bottle']['goal_and_compliance']
        layouts[key] = {'policy_controls':raw_score['policy_controls'],'model_queries':raw_score['model_queries'],
                        'exact_restarts':raw_score['exact_restarts']['B'],'translation_tolerance_mm':limits[0]*1000,
                        'rotation_tolerance_deg':raw_score['rotation_tolerance_degrees'],'paths':paths}
        selections[key] = [path['selection'] for path in paths.values()]
        if physical == donor:
            assert controls['selections'][str(physical)] == selections[key]
    compares = {}
    for physical,donor in design['cells']:
        if physical != donor:
            key = f'{physical}-{donor}'
            compares[key] = {name:{target:action_difference(blocks[key,name],blocks[f'{pos}-{pos}',name])
                                   for target,pos in [('own',physical),('donor',donor)]}
                             for name in layouts[key]['paths']}
    changed = {}
    for camera in CAMERAS:
        pair = []
        for pos in (11,19):
            with Image.open(BytesIO(cells[pos]['images'][camera])) as img:
                pair.append(np.array(img))
        changed[camera] = int(np.any(pair[0] != pair[1], axis=-1).sum())
    assert all(changed.values())
    return {'decision':classify(selections),'selection_by_cell':selections,'eligible_layouts':list(layouts),'layouts':layouts,
            'first_five_commands_compared_to_same_repeat_own_controls':compares,
            'changed_branch_pixels_of_50176':changed,'branch_proprioception':cells[11]['prefix']['queries'][1]['proprioception'],
            'source_tokens':20,'revised_tokens':22,'verified_native_replies_and_inputs':sum(v['model_queries'] for v in layouts.values()),
            'matching_rng_transitions_per_restart':len(schedule)-1,'branch_rng_before':schedule[1],
            'branch_rng_after':schedule[2],'rollout_controls':sum(v['policy_controls'] for v in layouts.values()),
            'independent_scenes':1,'restarts_per_cell':2}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    args = parser.parse_args()
    with unpack(args.run) as folder:
        result = assessment(folder)
        check_saved_replays(args.run,result)
    print(json.dumps(result,indent=2,allow_nan=False))
