"""Check the physical handoff, match every policy receipt and score equal total budgets."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import statistics
import zipfile

import numpy as np

from inside import write_json
from verify_atomic import PACKET, read
from verify_drawer import command_sha, pixels
from verify_layouts import unpack
from verify_stove import D as STOVE, numbers, outcome, physical_readouts, sha


PLAN_FILE = 'drawer/stove_pose.json'
PLAN = read(PACKET/PLAN_FILE)
BASE = PACKET/PLAN['baseline']


def angle(a,b):
    cosine = abs(float(np.dot(a,b))) / (np.linalg.norm(a)*np.linalg.norm(b))
    return math.degrees(2*math.acos(np.clip(cosine,0,1)))


def max_difference(a,b):
    return max(abs(x-y) for x,y in zip(a,b,strict=True))


def pose_error(a,b):
    return dict(tool_mm=1000*math.dist(a['xyz'],b['xyz']),tool_deg=angle(a['quat'],b['quat']),
                joint_rad=max_difference(a['joints'],b['joints']),
                finger_mm=1000*max_difference(a['fingers'],b['fingers']))


def scene_error(a,b):
    assert set(a['objects']) == set(b['objects']) == set(PLAN['scene_objects'])
    before,after = a['stove'],b['stove']
    return dict(object_mm=max(1000*math.dist(v[:3],b['objects'][n][:3]) for n,v in a['objects'].items()),
                object_deg=max(angle(v[3:],b['objects'][n][3:]) for n,v in a['objects'].items()),
                drawer_mm=1000*max_difference(before['drawer_joints'],after['drawer_joints']),
                stove_rad=abs(before['angle']-after['angle']))


def within(values):
    return all(x<=PLAN['limits'][k] for k,x in values.items())


def preparation_metrics(t):
    rows = t['rows']
    assert len(rows)==len(t['actions'])==t['length'] and t['handoff']['stove']==rows[-1]['stove']
    tail = rows[-PLAN['limits']['clear_tail']:] + [t['handoff']]
    target = t['common'] if t['mode']=='pose' else t['start']['tool']
    scene = [scene_error(t['start'],r) for r in [*rows,t['handoff']]]
    err = [pose_error(r['tool'],target) for r in tail]
    limits = {k:max(e[k] for e in err) for k in err[0]}
    limits.update({k:max(d[k] for d in scene) for k in scene[0]})
    limits['final_velocity_rad_s'] = max(abs(v) for v in t['handoff']['tool']['velocity'])
    clear = all(not x['robot_contacts'] for x in tail)
    stable = all(x['stove']['drawer_open'] and not x['stove']['on'] and not x['stove']['stove_contact']
                 for x in [t['start'],*rows,t['handoff']])
    return dict(maximum=limits,clear_tail=clear,open_drawer_stove_untouched=stable,
                        passed=within(limits) and stable and (clear or t['mode'] in ('wait','finger_hold')))


def geometry(tapes):
    report = {name:preparation_metrics(t) for name,t in tapes.items()}
    a,b = (tapes[arm+'-pose']['handoff'] for arm in PLAN['arms'])
    common = pose_error(a['tool'],b['tool'])
    scene_pair = {m:scene_error(tapes['A-'+m]['handoff'],tapes['B-'+m]['handoff']) for m in ('pose','wait')}
    return dict(passed=all(x['passed'] for x in report.values()) and within(common) and all(within(v) for v in scene_pair.values()),
                by_condition=report,pair_posture=common,pair_scene=scene_pair)

def planned(lead):
    entries = []
    period = PLAN['replan_every']
    for block in range(1,PLAN['blocks']+1):
        group = []
        for seed in PLAN['seeds']:
            arms = PLAN['arms'] if seed%2 == 0 else list(reversed(PLAN['arms']))
            for i,arm in enumerate(arms):
                modes = PLAN['conditions']
                split = (seed+i)%len(modes)
                for mode in modes[split:]+modes[:split]:
                    pre = 0 if mode=='immediate' else lead
                    name = f'pose-{block}-{arm}-{mode}-k{seed}'
                    group.append(dict(session=name,block=block,arm=arm,mode=mode,lead=pre,key=seed,
                                      key_offset=PLAN['key_offset'],source=STOVE['prompt'],
                                      queries=(PLAN['budgets'][-1]-pre)//period,receipts=f'receipts/{name}.jsonl'))
        entries.extend(group if block%2 else reversed(group))
    return {e['session']:e for e in entries}

def qualified(out):
    from verify_stove import DONORS
    assert sha(BASE)==PLAN['baseline_sha256'] and sha(DONORS)==STOVE['donor_sha256']
    assert read(out/'design.json')==PLAN
    with zipfile.ZipFile(BASE) as z:
        base = json.loads(z.read('qualification.json'))
        keys = json.loads(z.read('rng.json'))
        previous = json.loads(z.read('runtime.json'))
    runtime = read(out/'runtime.json')
    assert runtime['baseline_sha256']==sha(BASE) and runtime['checkpoint']==previous['checkpoint']
    for name,h in runtime['sources'].items():
        assert sha(out/'sources'/name)==h
    qual = read(out/'qualification.json')
    attempts,selected = qual['attempts'],qual['lead']
    assert [a['length'] for a in attempts]==PLAN['lead_options'][:len(attempts)] and attempts
    used = {}
    for attempt in attempts:
        n = attempt['length']
        cells = {a+'-'+m:read(out/'preparation'/f'{a}-{m}-{n}.json')
                 for a in PLAN['arms'] for m in ('wait','pose')}
        assert attempt==dict(length=n,**geometry(cells))
        if n==selected:
            used.update(cells)
    assert all(not a['passed'] for a in attempts[:-1])
    assert attempts[-1]['passed'] and selected==attempts[-1]['length']
    for arm in PLAN['arms']:
        used[arm+'-immediate'] = read(out/'preparation'/f'{arm}-immediate-0.json')
    for t in used.values():
        old = base['states'][t['arm']+'-160']
        assert t['geometry']==base['geometry'] and t['donor_physics']==old['physics']
        assert t['start']['stove']==old['initial'] and t['start']['tool']['xyz']==old['state'][:3]
        assert t['common']==used['A-immediate']['common']
        assert t['first']['state'][:3]==t['handoff']['tool']['xyz']
        if t['mode']=='immediate':
            assert t['first']['physics']==old['physics'] and t['rows']==t['actions']==[]
        for i,cmd in enumerate(t['actions']):
            assert len(cmd)==(7 if i<PLAN['clear_controls'] else 8) and cmd[-1]==PLAN['open_gripper']
            assert np.isfinite(cmd).all() and max(map(abs,cmd))<=1
    return selected,used,base,keys


def check_receipts(out,e,tape,keys,seen,first):
    wire = [json.loads(line) for line in (out/e['receipts']).read_bytes().splitlines()]
    period = PLAN['replan_every']
    assert len(wire)==len(tape['queries'])==e['queries'] and len(tape['rows'])==len(wire)*period
    assert len(tape['final_physics'])==64
    for i,(sample,rec) in enumerate(zip(tape['queries'],wire,strict=True)):
        assert sample['tick']==e['lead']+i*period and rec['prompt']==e['source']
        assert (sample['live'],sample['state'])==(rec['rgb_sha256'],rec['proprioception'])
        sequence = keys[str(e['key'])]
        k = e['key_offset']+i
        assert [rec['rng_before'],rec['rng_after']]==sequence[k:k+2]
        assert np.asarray(sample['reply']).shape==(10,7) and command_sha(sample['reply'])==rec['actions_sha256']
        assert sample['reply'][:period]==[r['action'] for r in tape['rows'][i*period:(i+1)*period]]
        if i==0:
            assert (sample['physics'],sample['state'])==(first['physics'],first['state'])
            for h in sample['live'].values():
                if h not in seen:
                    pixels(out,h)
                    seen.add(h)


def one_path(out,e,prep,base,keys,seen,lead):
    name = e['session']
    tape = read(out/'paths'/(name+'.json'))
    assert (tape['session'],tape['arm'],tape['mode'],tape['lead'],tape['seed'],tape['block'])==(
        name,e['arm'],e['mode'],e['lead'],e['key'],e['block'])
    check_receipts(out,e,tape,keys,seen,prep['first'])
    condition = e['arm']+'-160'
    st = base['states'][condition]
    combined = [r['stove'] for r in prep['rows']] + tape['rows']
    native = dict(session=name,condition=condition,block=e['block'],seed=e['key'],initial=st['initial'],
                  initial_physics=st['physics'],rows=combined)
    vals = physical_readouts(native,dict(e,condition=condition),base)
    for deadline in PLAN['budgets']:
        exposure = deadline-lead
        vals['policy_'+str(exposure)] = outcome([st['initial'],*combined],exposure+e['lead'],
                                                st['last_prior_drawer'],PLAN['donor_tick'])
    return vals


def summarize(values):
    return dict(paths=len(values),on=sum(v['on'] for v in values),ever_on=sum(v['ever_on'] for v in values),
                drawer_open=sum(v['drawer_open'] for v in values),
                first_button=numbers([v['first_button'] for v in values]),
                first_stove=numbers([v['first_stove'] for v in values]),first_on=numbers([v['first_on'] for v in values]))


def contrasts(outcomes,arm,measure,blocks):
    result = {}
    for mode in ('immediate','wait'):
        pairs = [(outcomes[f'pose-{b}-{arm}-pose-k{k}'][measure]['on'],
                  outcomes[f'pose-{b}-{arm}-{mode}-k{k}'][measure]['on']) for b in blocks for k in PLAN['seeds']]
        counts = Counter(pairs)
        result[mode] = dict(pairs=len(pairs),both_on=counts[True,True],pose_only=counts[True,False],
                            control_only=counts[False,True],both_off=counts[False,False])
    return result


def score(out):
    lead,preps,base,keys = qualified(out)
    plan = planned(lead)
    assert read(out/'sessions.json')==plan
    assert set(plan)=={p.stem for p in (out/'paths').glob('*.json')}=={p.stem for p in (out/'receipts').glob('*.jsonl')}
    seen = set()
    outcomes = {n:one_path(out,e,preps[e['arm']+'-'+e['mode']],base,keys,seen,lead) for n,e in plan.items()}
    measures = list(next(iter(outcomes.values())))
    summary = {}
    for arm in PLAN['arms']:
        for mode in PLAN['conditions']:
            rows = [outcomes[n] for n,e in plan.items() if e['arm']==arm and e['mode']==mode]
            summary[arm+'-'+mode] = {m:summarize([v[m] for v in rows]) for m in measures}
    blocks = list(range(1,PLAN['blocks']+1))
    by = {m:{arm:{label:contrasts(outcomes,arm,m,bs) for label,bs in
                       [('all',blocks),*[(str(b),[b]) for b in blocks]]} for arm in PLAN['arms']} for m in measures}
    passed = {m:all(pair['pose_only']>pair['control_only'] for variants in by[m].values()
                     for controls in variants.values() for pair in controls.values()) for m in measures}
    return dict(paths=len(plan),lead=lead,total_controls=len(plan)*PLAN['budgets'][-1],
                policy_queries=sum(e['queries'] for e in plan.values()),first_frame_hashes=len(seen),
                criteria_by_deadline=passed,by_condition=summary,paired=by,outcomes_by_path=outcomes)


def replay(out):
    from concurrent.futures import ThreadPoolExecutor
    import subprocess
    import sys
    def run(name):
        cmd=[sys.executable,str(PACKET/'stove_pose_sim.py'),str(out),'replay',name]
        proc=subprocess.run(cmd,capture_output=True,text=True,timeout=300)
        if proc.returncode:
            raise RuntimeError(name+' '+proc.stderr[-1600:])
        return json.loads(proc.stdout.strip().splitlines()[-1])
    names=sorted(read(out/'sessions.json'))
    with ThreadPoolExecutor(max_workers=4) as pool:
        runs=list(pool.map(run,names))
    assert [r['session'] for r in runs]==names
    return dict(paths=len(runs),total_controls=sum(r['lead']+r['policy_controls'] for r in runs),
                prefix_controls=sum(r['prefix_controls'] for r in runs),runs=runs)


def check_replay(out,report,result):
    plan = read(out/'sessions.json')
    runs = report['runs']
    assert report['paths']==len(runs)==result['paths'] and {r['session'] for r in runs}==set(plan)
    assert report['total_controls']==result['total_controls']
    assert report['prefix_controls']==len(runs)*PLAN['donor_tick']
    for r in runs:
        e = plan[r['session']]
        assert r['lead']==e['lead'] and r['prefix_controls']==PLAN['donor_tick']
        assert r['observations']==e['queries'] and r['policy_controls']==e['queries']*PLAN['replan_every']
        assert r['final_physics']==read(out/'paths'/(r['session']+'.json'))['final_physics']
        assert all(t in range(r['lead'],PLAN['budgets'][-1],PLAN['replan_every']) for t in r['changed_rgb_ticks'])


if __name__ == '__main__':
    cli = argparse.ArgumentParser()
    cli.add_argument('folder',type=Path)
    cli.add_argument('stage',nargs='?',choices=['score','verify','replay'],default='verify')
    cli.add_argument('--output',type=Path)
    args = cli.parse_args()
    with unpack(args.folder) as raw:
        if args.stage=='replay':
            evidence = replay(raw)
            if args.output:
                write_json(args.output,evidence)
                print('Replayed paths',evidence['paths'],'controls',evidence['total_controls'])
            else:
                print(json.dumps(evidence))
        else:
            result = score(raw)
            if args.stage=='score':
                write_json(raw/'verification.json',result)
            else:
                assert result==read(args.folder/'verification.json')
                proof = args.folder/'physical_replay.json'
                if proof.is_file():
                    check_replay(raw,read(proof),result)
            print('Verified pose paths',result['paths'],'total controls',result['total_controls'],flush=True)


