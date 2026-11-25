"""Score drawer-to-stove trials from actuator receipts, contact geoms and the native hinge."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import statistics
import subprocess
import sys
import zipfile

import numpy as np

from inside import write_json
from verify_atomic import PACKET, read
from verify_drawer import command_sha, pixels
from verify_layouts import unpack


DESIGN_FILE = 'drawer/stove_handoff.json'
D = read(PACKET/DESIGN_FILE)
DONORS = PACKET/D['donor_archive']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archived_name(arm, block):
    return f"branch-{block}-{D['donor_pair']}-{arm}"


@lru_cache(maxsize=2)
def donor(arm):
    with zipfile.ZipFile(DONORS) as z:
        return json.loads(z.read(f'recapture/paths/{archived_name(arm,1)}.json'))


def scenario(condition):
    if condition.startswith('public-'):
        start = int(condition.split('-')[1])
        assert start in D['public_starts']
        return True, start, None, 0
    start = D['donor_public_start']
    if condition == 'layout':
        return False, start, None, 0
    arm, tick = condition.split('-')
    assert arm in ('A','B') and int(tick) in [D['primary_switch'],*D['timing_controls']]
    return False, start, arm, int(tick)


def blocks(stage, number):
    if stage == 'direct':
        groups = [[(cond,k) for k in D['direct_seeds']] for cond in
                  [*(f'public-{s}' for s in D['public_starts']),'layout']]
    else:
        assert stage == 'continuation'
        groups = []
        for tick in [D['primary_switch'],*D['timing_controls']]:
            seeds = D['primary_seeds'] if tick == D['primary_switch'] else D['timing_seeds']
            for key in seeds:
                arms = ('A','B') if key % 2 == 0 else ('B','A')
                groups.append([(f'{arm}-{tick}',key) for arm in arms])
    if number % 2 == 0:
        groups = [list(reversed(g)) for g in reversed(groups)]
    return [[dict(session=f'{stage}-{number}-{cond}-k{k}', condition=cond, key=k,
                  key_offset=0 if cond.startswith('public-') else D['continuation_key_offset'],
                  source=D['prompt'], queries=D['full_budget']//D['replan_every'], stage=stage,block=number,
                  receipts=f'receipts/{stage}-{number}-{cond}-k{k}.jsonl') for cond,k in group] for group in groups]


def planned():
    return {e['session']:e for s in ('direct','continuation') for b in range(1,D['blocks']+1)
            for g in blocks(s,b) for e in g}


def crossed():
    result = {}
    tick = D['primary_switch']
    for block in range(1,D['blocks']+1):
        for key in D['primary_seeds']:
            for src,dst in (('A','B'),('B','A')):
                name = f'cross-{block}-{src}-to-{dst}-k{key}'
                result[name] = dict(session=name,condition=f'{dst}-{tick}',key=key,block=block,
                                    motor_source=f'continuation-{block}-{src}-{tick}-k{key}')
    return result


def qualification(out):
    assert sha(DONORS) == D['donor_sha256'] and sha(PACKET/'drawer/stove.bddl') == D['bddl_sha256']
    assert sha(PACKET/'drawer/stove_starts.json') == D['selected_starts_sha256']
    assert read(out/'design.json') == D and read(out/'sessions.json') == planned()
    q = read(out/'qualification.json')
    states = q['states']
    assert set(states) == {e['condition'] for e in planned().values()}
    schedule = read(out/'rng.json')
    with zipfile.ZipFile(DONORS) as z:
        for arm in 'AB':
            t = donor(arm)
            for block in range(1,5):
                name = archived_name(arm,block)
                historical = json.loads(z.read(f'recapture/paths/{name}.json'))
                assert historical['final_physics'] == t['final_physics'] and historical['rows'] == t['rows']
                last = json.loads(z.read(f'recapture/receipts/{name}.jsonl').splitlines()[-1])
                assert last['rng_after'] == schedule['0'][D['continuation_key_offset']]
            for tick in [*D['timing_controls'],D['primary_switch']]:
                s = states[f'{arm}-{tick}']
                old, new = t['rows'][tick-1], s['initial']
                assert new['gripper_pairs'] == old['gripper_pairs'] and new['drawer_joints'] == old['joints']
                assert new['drawer_open'] and new['drawer_contact'] == (arm == 'B' and tick in (155,160))
                assert s['last_prior_drawer'] == max(i for i,r in enumerate(t['rows'][:tick],1) if r['target_contact'])
                if tick == D['primary_switch']:
                    assert s['physics'] == t['final_physics']
                elif tick % D['replan_every'] == 0:
                    assert s['physics'] == t['queries'][tick//D['replan_every']]['physics']
    assert all(not s['initial']['on'] and not s['initial']['stove_contact'] for s in states.values())
    return q, schedule


def first(rows, key):
    return next((i for i,r in enumerate(rows) if r[key]), None)


def outcome(rows, endpoint, prior, switch):
    r = rows[:endpoint+1]
    contacts = [i for i,x in enumerate(r) if x['drawer_contact']]
    last_drawer = contacts[-1] if contacts else (prior-switch if prior is not None else None)
    on = first(r,'on')
    return dict(last_drawer_relative=last_drawer, last_drawer_after=max((i for i in contacts if i>0),default=None),
                first_stove=first(r,'stove_contact'), first_button=first(r,'button_contact'), first_on=on,
                ever_on=on is not None, on=r[-1]['on'], button_and_on=r[-1]['on'] and first(r,'button_contact') is not None,
                drawer_open=r[-1]['drawer_open'], angle=r[-1]['angle'])


def check_path(out,e,q,schedule,seen_frames):
    t = read(out/'paths'/(e['session']+'.json'))
    assert (t['session'],t['condition'],t['block'],t['seed']) == (e['session'],e['condition'],e['block'],e['key'])
    start = q['states'][e['condition']]
    assert t['initial'] == start['initial'] and t['initial_physics'] == start['physics']
    wire = [json.loads(l) for l in (out/e['receipts']).read_bytes().splitlines()]
    keys = schedule[str(e['key'])]
    period = D['replan_every']
    assert len(wire) == len(t['queries']) == e['queries'] and len(t['rows']) == D['full_budget']
    for i,(sample,rec) in enumerate(zip(t['queries'],wire)):
        offset = i*period
        assert sample['tick'] == offset and rec['prompt'] == D['prompt']
        assert (rec['rgb_sha256'],rec['proprioception']) == (sample['live'],sample['state'])
        assert (rec['rng_before'],rec['rng_after']) == tuple(keys[e['key_offset']+i:e['key_offset']+i+2])
        assert np.asarray(sample['reply']).shape == (10,7) and command_sha(sample['reply']) == rec['actions_sha256']
        assert sample['reply'][:period] == [r['action'] for r in t['rows'][offset:offset+period]]
        if i == 0:
            assert (sample['physics'],sample['state']) == (start['physics'],start['state'])
            for h in sample['live'].values():
                if h not in seen_frames:
                    pixels(out,h)
                    seen_frames.add(h)
    return physical_readouts(t,e,q)


def check_contact_rows(rows,geometry):
    groups = {k:set(map(int,geometry[k])) for k in ('drawer','stove','button','gripper')}
    for r in rows:
        pairs = r['gripper_pairs']
        assert all(a in groups['gripper'] for a,b in pairs)
        for k in ('drawer','stove','button'):
            assert r[k+'_contact'] == any(b in groups[k] for a,b in pairs)
        assert r['drawer_open'] == (r['drawer_joints'][1] < -0.14)
        assert r['on'] == (r['angle'] >= D['on_angle_rad'])


def physical_readouts(t,e,q):
    start = q['states'][e['condition']]
    assert (t['session'],t['condition'],t['block'],t['seed']) == (e['session'],e['condition'],e['block'],e['key'])
    assert (t['initial'],t['initial_physics']) == (start['initial'],start['physics'])
    assert len(t['rows']) == D['full_budget']
    rows = [t['initial'],*t['rows']]
    check_contact_rows(rows,q['geometry'])
    _, _, _, switch = scenario(e['condition'])
    return {str(h):outcome(rows,h,start['last_prior_drawer'],switch) for h in (D['primary_budget'],D['full_budget'])}


def check_crosses(out,q,online):
    measurements, directions = {}, {}
    for name,e in crossed().items():
        t = read(out/'crossed'/(name+'.json'))
        base = e['motor_source']
        native = read(out/'paths'/(base+'.json'))
        assert t['motor_source'] == base and t['commands_sha256'] == command_sha([r['action'] for r in native['rows']])
        assert len(t['queries']) == len(native['queries']) and all('reply' not in s for s in t['queries'])
        assert t['queries'][0]['physics'] == q['states'][e['condition']]['physics']
        measurements[name] = physical_readouts(t,e,q)
        direction = native['condition'][0] + '_to_' + e['condition'][0]
        directions.setdefault(direction,[]).append((measurements[name],online[base]))
    assert set(measurements) == {p.stem for p in (out/'crossed').glob('*.json')}
    summary = {}
    for direction, trials in directions.items():
        stats = {}
        for budget in (D['primary_budget'],D['full_budget']):
            h = str(budget)
            pairs = [(v[h],orig[h]) for v,orig in trials]
            stats[h] = dict(summary=summarize([v for v,_ in pairs]), native_on=sum(u['on'] for _,u in pairs),
                            lost=sum(u['on'] and not v['on'] for v,u in pairs),
                            gained=sum(v['on'] and not u['on'] for v,u in pairs))
        summary[direction] = stats
    return dict(paths=len(measurements),by_direction=summary,outcomes_by_path=measurements)


def numbers(values):
    a = [v for v in values if v is not None]
    return dict(n=len(a), min=min(a), median=statistics.median(a), max=max(a)) if a else dict(n=0)


def summarize(items):
    return dict(paths=len(items), on=sum(v['on'] for v in items), ever_on=sum(v['ever_on'] for v in items),
                button_and_on=sum(v['button_and_on'] for v in items), drawer_open=sum(v['drawer_open'] for v in items),
                **{k:numbers([v[k] for v in items]) for k in
                   ('last_drawer_relative','last_drawer_after','first_stove','first_button','first_on')})


def direct_gate(outcomes, plan):
    by = {}
    for family in ('public','layout'):
        names = [n for n,e in plan.items() if e['stage']=='direct' and e['condition'].startswith(family)]
        by[family] = {str(h):summarize([outcomes[n][str(h)] for n in names]) for h in (D['primary_budget'],D['full_budget'])}
    return dict(passed=all(s[str(D['full_budget'])]['button_and_on'] > 0 for s in by.values()),by_family=by)


def paired(outcomes, tick, horizon):
    seeds = D['primary_seeds'] if tick == D['primary_switch'] else D['timing_seeds']
    counts = Counter()
    delta = {k:[] for k in ('first_stove','first_button','first_on','last_drawer_relative')}
    for b in range(1,D['blocks']+1):
        for k in seeds:
            a,v = [outcomes[f'continuation-{b}-{arm}-{tick}-k{k}'][str(horizon)] for arm in 'AB']
            status = {(True,True):'both_on',(True,False):'A_only',(False,True):'B_only',(False,False):'both_off'}
            counts[status[(a['on'],v['on'])]] += 1
            for measure,values in delta.items():
                if a[measure] is not None and v[measure] is not None:
                    values.append(v[measure]-a[measure])
    return dict(pairs=len(seeds)*D['blocks'],outcomes={n:counts[n] for n in ('both_on','A_only','B_only','both_off')},
                B_minus_A={k:dict(numbers(v),earlier=sum(x<0 for x in v),same=v.count(0),later=sum(x>0 for x in v))
                           for k,v in delta.items()})


def score(out, only_direct=False):
    q,schedule = qualification(out)
    plan = planned()
    seen = set()
    outcomes = {n:check_path(out,e,q,schedule,seen) for n,e in plan.items() if e['stage']=='direct'}
    g = direct_gate(outcomes,plan)
    if only_direct:
        return g
    assert g == read(out/'gate.json')
    if g['passed']:
        outcomes.update({n:check_path(out,e,q,schedule,seen) for n,e in plan.items() if e['stage']=='continuation'})
    assert set(outcomes) == {p.stem for p in (out/'paths').glob('*.json')} == {p.stem for p in (out/'receipts').glob('*.jsonl')}
    hs = [D['primary_budget'],D['full_budget']]
    summary = {c:{str(h):summarize([v[str(h)] for n,v in outcomes.items() if plan[n]['condition']==c]) for h in hs}
               for c in sorted({plan[n]['condition'] for n in outcomes})}
    comparisons = ({str(t):{str(h):paired(outcomes,t,h) for h in hs} for t in [D['primary_switch'],*D['timing_controls']]}
                   if g['passed'] else {})
    fixed = check_crosses(out,q,outcomes) if g['passed'] else None
    return dict(paths=len(outcomes),post_switch_controls=len(outcomes)*D['full_budget'],gate=g,by_condition=summary,
                paired=comparisons,fixed_commands=fixed,first_frame_hashes=len(seen),outcomes_by_path=outcomes)


def replay(out):
    def one(path):
        cmd = [sys.executable,str(PACKET/'stove_sim.py'),str(out),'replay',path.stem]
        run = subprocess.run(cmd,capture_output=True,text=True)
        if run.returncode:
            raise RuntimeError(path.stem+' '+run.stderr[-1800:])
        return json.loads(run.stdout.splitlines()[-1])
    with ThreadPoolExecutor(max_workers=4) as pool:
        paths = sorted([*(out/'paths').glob('*.json'),*(out/'crossed').glob('*.json')])
        results = list(pool.map(one,paths))
    return dict(paths=len(results),closed_loop=sum(p.parent.name=='paths' for p in paths),
                fixed_command_crosses=sum(p.parent.name=='crossed' for p in paths),post_switch_controls=sum(x['controls'] for x in results),
                replayed_prefix_controls=sum(x['prefix_controls'] for x in results),runs=results)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('folder',type=Path)
    ap.add_argument('stage',nargs='?',choices=['gate','score','verify','replay'],default='verify')
    args = ap.parse_args()
    with unpack(args.folder) as root:
        if args.stage == 'replay':
            print(json.dumps(replay(root)))
        elif args.stage == 'verify':
            report = score(root)
            for n,v in read(root/'runtime.json')['sources'].items():
                assert any(p.is_file() and sha(p)==v for p in (root/'sources'/n,PACKET/n)), n
            assert report == read(args.folder/'verification.json')
            print('Verified stove paths',report['paths'],'controls',report['post_switch_controls'])
        else:
            result = score(root,only_direct=args.stage=='gate')
            write_json(root/('gate.json' if args.stage=='gate' else 'verification.json'),result)
            print(args.stage,'complete',flush=True)
