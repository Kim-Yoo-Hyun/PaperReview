"""Check the physical finger hold and paired outcomes on the two original contact states."""
import argparse
from collections import Counter
import json
from pathlib import Path
import zipfile

import numpy as np

from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_stove import D as STOVE, sha
from verify_stove_layouts import (
    DESIGN as BASE, check_freeze, check_replayed_paths, digest, replay, score_continuation,
)
from verify_stove_pose import PLAN, max_difference, preparation_metrics, summarize

DESIGN_FILE = 'drawer/stove_fingers.json'
DESIGN = read(PACKET / DESIGN_FILE)


def prep_signature(tape):
    # The rasterizer is checked separately from the physical comparison.
    return digest({**tape, 'first': {k: tape['first'][k] for k in ('state', 'physics')}})


def donor_trace(raw):
    return dict(initial=raw['initial_physics'], final=raw['final_physics'],
                start=digest([raw['common'], raw['geometry'], raw['initial']]),
                actions=[row['action'] for row in raw['rows']],
                measurements=digest([{k:v for k,v in row.items() if k!='action'} for row in raw['rows']]),
                observations=digest([[v[k] for k in ('tick','physics','state')] for v in raw['queries']]))


def source_donors(parent):
    donors = {}
    assert sha(parent) == DESIGN['parent_sha256']
    with zipfile.ZipFile(parent) as archive:
        for arm, expected in zip(DESIGN['arms'], DESIGN['donor_physics'], strict=True):
            raw = json.loads(archive.read(f'gates/{arm}.json'))
            assert raw['task'] == 'drawer' and raw['layout'] == DESIGN['layout']
            assert raw['final_physics'] == expected and raw['rows'][-1]['drawer_contact']
            assert raw['rows'][-1]['drawer_open'] and not any(row['on'] for row in raw['rows'])
            controls = {}
            for mode in BASE['modes']:
                lead = 0 if mode == 'immediate' else BASE['lead']
                tape = json.loads(archive.read(f'preparation/{arm}-{mode}-{lead}.json'))
                controls[mode] = prep_signature(tape)
            donors[arm] = dict(donor_trace(raw), preparation=controls)
    return donors


def planned():
    entries = {}
    modes = DESIGN['modes']
    for block in DESIGN['blocks']:
        group = []
        for index, arm in enumerate(DESIGN['arms']):
            for key in BASE['stove_seeds']:
                split = (index + key) % len(modes)
                for mode in modes[split:] + modes[:split]:
                    name = f'{arm}-{mode}-b{block}-s{key}'
                    lead = 0 if mode == 'immediate' else BASE['lead']
                    group.append(dict(session=name, arm=arm, layout=DESIGN['layout'], block=block, mode=mode,
                                      lead=lead, key=key, key_offset=BASE['key_offset'], source=STOVE['prompt'],
                                      queries=(BASE['budgets'][-1]-lead)//BASE['period'], receipts=f'receipts/{name}.jsonl'))
        for entry in group if block == 1 else reversed(group):
            entries[entry['session']] = entry
    return entries


def physical_metrics(out, donors):
    result = {}
    for arm in DESIGN['arms']:
        result[arm] = {}
        for mode in DESIGN['modes']:
            lead = 0 if mode == 'immediate' else BASE['lead']
            tape = read(out/'preparation'/f'{arm}-{mode}-{lead}.json')
            assert (tape['arm'], tape['mode'], tape['length']) == (arm, mode, lead)
            assert tape['donor_physics'] == donors[arm]['final']
            assert tape['start']['stove']['drawer_contact'] and tape['start']['stove']['drawer_open']
            assert tape['first']['state'][:3] == tape['handoff']['tool']['xyz']
            if mode != 'finger_hold':
                assert prep_signature(tape) == donors[arm]['preparation'][mode]
            if not lead:
                assert tape['actions'] == tape['rows'] == [] and tape['first']['physics'] == donors[arm]['final']
                continue
            target = tape['start']['tool']['fingers']
            rows = tape['rows']
            metrics = preparation_metrics(tape)
            metrics['peak_finger_from_donor_mm'] = 1000 * max(max_difference(r['tool']['fingers'],target) for r in rows)
            contacts = [i for i,r in enumerate(rows,1) if r['stove']['drawer_contact']]
            metrics.update(drawer_contact_steps=len(contacts), last_drawer_contact_step=max(contacts,default=0),
                           touching_drawer_at_handoff=tape['handoff']['stove']['drawer_contact'])
            for i, action in enumerate(tape['actions']):
                assert len(action) == (7 if i < PLAN['clear_controls'] else 8)
                assert np.isfinite(action).all() and max(map(abs,action)) <= 1
                assert action[-1] == (0 if mode == 'finger_hold' else PLAN['open_gripper'])
            if mode == 'finger_hold':
                actuator = tape['finger_actuators']
                bounds = np.asarray(actuator['ranges'])
                normalized = np.asarray(actuator['normalized_targets'])
                assert -1 <= normalized.min() <= normalized.max() <= 1
                assert np.allclose(bounds.mean(axis=1) + normalized * np.diff(bounds).ravel()/2,
                                   target, rtol=0, atol=1e-12)
                assert np.shape(actuator['applied_targets']) == (lead, 2)
                assert np.allclose(actuator['applied_targets'], target, rtol=0, atol=1e-12)
                metrics['passed_all_steps'] = metrics['passed'] and metrics['peak_finger_from_donor_mm'] <= PLAN['limits']['finger_mm']
            result[arm][mode] = metrics
    return result


def counts(outcomes, entries, deadline):
    data = {(e['arm'],e['block'],e['key'],e['mode']): outcomes[e['session']][deadline] for e in entries}
    by_mode = {mode:summarize([v for key,v in data.items() if key[-1] == mode]) for mode in DESIGN['modes']}
    paired = {}
    for left,right in [('pose',m) for m in DESIGN['modes'] if m != 'pose'] + [('finger_hold','wait')]:
        cells = Counter((v['on'],data[(*key[:-1],right)]['on']) for key,v in data.items() if key[-1] == left)
        paired[f'{left}_vs_{right}'] = dict(left_only=cells[True,False], right_only=cells[False,True],
                                            both_on=cells[True,True], both_off=cells[False,False])
    return dict(by_mode=by_mode,paired=paired)


def score(out):
    assert read(out/'design.json') == DESIGN
    sources = out/'sources'
    check_freeze(sources)
    runtime = read(out/'runtime.json')
    assert all(sha(sources/n) == h for n,h in runtime['sources'].items())
    assert digest(runtime['checkpoint']) == BASE['checkpoint_manifest_sha256']
    donors = read(sources/DESIGN['donors'])
    assert digest(donors) == DESIGN['donors_sha256']
    parent = PACKET/DESIGN['parent']
    if parent.exists():
        assert donors == source_donors(parent)
    geometry = physical_metrics(out, donors)
    assert geometry == read(out/'qualification.json')['endpoints']
    qualified = all(d['finger_hold']['passed_all_steps'] for d in geometry.values())
    entries = planned() if qualified else {}
    assert read(out/'sessions.json') == entries
    assert set(entries) == {f.stem for f in (out/'paths').glob('*.json')} == {f.stem for f in (out/'receipts').glob('*.jsonl')}
    keys = read(out/'rng.json')
    assert digest(keys) == BASE['rng_schedule_sha256']
    scores, seen = {}, set()
    preps = {}
    for n,e in entries.items():
        k = e['arm'],e['mode']
        if k not in preps:
            preps[k] = read(out/'preparation'/f"{e['arm']}-{e['mode']}-{e['lead']}.json")
        scores[n] = score_continuation(out,e,preps[k],{'last_drawer_contact':BASE['drawer_horizon']},keys,seen)
    groups = {'all':list(entries.values())}
    cells = []
    for arm in DESIGN['arms']:
        groups[arm] = [e for e in entries.values() if e['arm']==arm]
        for block in DESIGN['blocks']:
            name = f'{arm}-b{block}'
            cells.append(name)
            groups[name] = [e for e in groups[arm] if e['block']==block]
    measures = [str(h) for h in BASE['budgets']] + [f"policy_{h-BASE['lead']}" for h in BASE['budgets']]
    comparisons = {name:{h:counts(scores,group,h) for h in measures} for name,group in groups.items() if group}
    advantage = {}
    for h in map(str,BASE['budgets']):
        pairs = [comparisons[n][h]['paired']['pose_vs_finger_hold'] for n in cells] if qualified else []
        advantage[h] = bool(pairs) and all(x['left_only'] > x['right_only'] for x in pairs)
    return dict(qualified=qualified, geometry=geometry, paths=len(entries), controls=len(entries)*BASE['budgets'][-1],
                policy_queries=sum(e['queries'] for e in entries.values()), advantage_every_cell=advantage,
                comparisons=comparisons, outcomes_by_path=scores)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=['score','verify','replay'], nargs='?', default='verify')
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    with unpack(args.folder) as out:
        if args.stage == 'replay':
            proof = replay(out, script='stove_finger_sim.py', entries=read(out/'sessions.json'))
            if args.output:
                write_json(args.output,proof)
                print('Physically replayed',proof['paths'],'paths')
            else:
                print(json.dumps(proof))
        else:
            result = score(out)
            if args.stage == 'score':
                write_json(out/'verification.json',result)
            else:
                assert result == read(args.folder/'verification.json')
                proof = args.folder/'physical_replay.json'
                if proof.exists():
                    check_replayed_paths(out,read(proof),read(out/'sessions.json'),{})
            print('Qualified:',result['qualified'],'paths:',result['paths'])
