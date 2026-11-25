"""Check physical endpoints, policy dispatch, drawer contact and native upper-drawer placements."""
import argparse
from collections import Counter
import json
from pathlib import Path

import numpy as np

from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_stove import numbers, sha
from verify_stove_fingers import DESIGN as FINGERS, prep_signature
from verify_stove_layouts import DESIGN as BASE, check_freeze, check_replayed_paths, digest, replay
from verify_stove_pose import PLAN, check_receipts, preparation_metrics

DESIGN_FILE = 'drawer/upper_bowl.json'
DESIGN = read(PACKET/DESIGN_FILE)
NEUTRAL = 'neutral'


def preparation_cells():
    return [(NEUTRAL,'immediate',0)] + [(a,m,0 if m=='immediate' else BASE['lead'])
                                        for a in FINGERS['arms'] for m in DESIGN['modes']]


def planned():
    entries = {}
    def entry(arm, mode, block, key):
        direct = arm == NEUTRAL
        name = f'{arm}-{mode}-b{block}-s{key}'
        lead = 0 if mode=='immediate' else BASE['lead']
        horizon = DESIGN['extension']
        return dict(session=name, arm=arm, mode=mode, block=block, key=key, source=DESIGN['prompt'], lead=lead,
                    stage='standalone' if direct else 'continuation', prefix_controls=0 if direct else BASE['drawer_horizon'],
                    key_offset=0 if direct else BASE['key_offset'], queries=(horizon-lead)//BASE['period'],
                    horizon=horizon, receipts='receipts/'+name+'.jsonl')
    for block in FINGERS['blocks']:
        group = [entry(NEUTRAL,'immediate',block,k) for k in BASE['stove_seeds']]
        for i,arm in enumerate(FINGERS['arms']):
            modes = DESIGN['modes']
            for key in BASE['stove_seeds']:
                shift = (key+i)%len(modes)
                group.extend(entry(arm,m,block,key) for m in modes[shift:]+modes[:shift])
        for e in group if block==1 else reversed(group):
            entries[e['session']] = e
    return entries


def check_rows(rows, geometry):
    top, bowl, fingers = (set(geometry[k]) for k in ('top','bowl','fingers'))
    assert top and bowl and fingers and top.isdisjoint(bowl|fingers|set(geometry['middle']))
    xyz = np.asarray([r['bowl_xyz'] for r in rows])
    target = np.asarray([r['target_xyz'] for r in rows])
    extent = np.asarray(geometry['site_extent_world'])
    lower = target - extent
    lower[:,2] -= geometry['lower_z_allowance_m']
    assert np.isfinite(xyz).all() and np.isfinite(target).all() and np.all(extent>0)
    inside = np.all((xyz>lower) & (xyz<target+extent),axis=1)
    assert np.array_equal(inside,[r['bowl_in'] for r in rows])
    for r in rows:
        joints = r['joints']
        assert len(joints)==3 and (joints[0]<geometry['open_below_m'])==r['top_open']
        assert (joints[1]<geometry['open_below_m'])==r['middle_open']
        pairs = r['gripper_pairs']
        assert all(a in fingers and b not in fingers for a,b in pairs)
        assert any(b in top for _,b in pairs)==r['top_contact']
        assert any(b in bowl for _,b in pairs)==r['bowl_contact']
        assert all(a in bowl and b in top for a,b in r['bowl_top_pairs'])


def validate_preparations(out,geometry):
    preps,summary = {},{}
    donors = read(PACKET/FINGERS['donors'])
    assert digest(donors)==FINGERS['donors_sha256']
    for arm,mode,lead in preparation_cells():
        tape = read(out/'preparation'/f'{arm}-{mode}-{lead}.json')
        assert (tape['arm'],tape['mode'],tape['length'])==(arm,mode,lead)
        expected = donors[FINGERS['arms'][0]]['initial'] if arm==NEUTRAL else donors[arm]['final']
        assert tape['donor_physics']==expected and len(tape['rows'])==len(tape['actions'])==lead
        scenes = [tape['start'],*tape['rows'],tape['handoff']]
        rows = [s['upper'] for s in scenes]
        check_rows(rows,geometry)
        assert all(not r['bowl_in'] and not r['top_open'] for r in rows)
        assert all(r['middle_open']==(arm!=NEUTRAL) for r in rows)
        assert tape['first']['state'][:3] == tape['handoff']['tool']['xyz']
        if not lead:
            assert tape['first']['physics']==expected
        if arm != NEUTRAL:
            # Compare the full legacy recorder view with its archived physical fingerprint.
            def legacy(scene):
                return {k:v for k,v in scene.items() if k!='upper'}
            prior = dict(tape,start=legacy(tape['start']),rows=[legacy(v) for v in tape['rows']],handoff=legacy(tape['handoff']))
            assert prep_signature(prior)==DESIGN['preparation_signatures'][arm][mode]
            assert tape['start']['stove']['drawer_contact']
        metrics = preparation_metrics(tape) if lead else {}
        if lead:
            assert metrics['passed'] and metrics['open_drawer_stove_untouched']
        if mode=='finger_hold':
            start = np.asarray(tape['start']['tool']['fingers'])
            peak = 1000*np.max(np.abs(np.asarray([s['tool']['fingers'] for s in scenes])-start))
            assert peak<=PLAN['limits']['finger_mm']
            metrics['peak_finger_error_mm']=float(peak)
        summary[f'{arm}/{mode}'] = dict(donor=expected,handoff=tape['first']['physics'],metrics=metrics,
                                         top_contact_at_handoff=rows[-1]['top_contact'],
                                         middle_contact_at_handoff=tape['handoff']['stove']['drawer_contact'])
        preps[arm,mode] = tape
    return preps,summary


def outcome(rows,tick):
    section = rows[:tick+1]
    end = section[-1]
    first = {name:next((i for i,r in enumerate(section) if r[name]),None)
             for name in ('top_contact','top_open','bowl_contact','bowl_in')}
    tail = section[-DESIGN['release_window']:]
    return dict(first=first, bowl_in=end['bowl_in'], top_open=end['top_open'], middle_open=end['middle_open'],
                released_in=all(r['bowl_in'] and not r['bowl_contact'] for r in tail),
                bowl_touching_top=bool(end['bowl_top_pairs']))


def path_score(out,e,prep,geometry,keys,frames):
    tape=read(out/'paths'/(e['session']+'.json'))
    assert all(tape[k]==e[k] for k in ('session','arm','mode','lead','block')) and tape['seed']==e['key']
    check_receipts(out,e,tape,keys,frames,prep['first'])
    rows=[prep['start']['upper'],*[r['upper'] for r in prep['rows']],*tape['rows']]
    assert len(rows)==e['horizon']+1
    check_rows(rows,geometry)
    scores = {str(t):outcome(rows,t) for t in DESIGN['deadlines']}
    for horizon in (DESIGN['primary'],DESIGN['extension']):
        exposure=horizon-BASE['lead']
        scores['policy_'+str(exposure)]=outcome(rows,e['lead']+exposure)
    return scores


def summarize(values):
    return dict(paths=len(values),**{k:sum(v[k] for v in values) for k in
                ('bowl_in','released_in','middle_open','top_open','bowl_touching_top')},
                first={k:numbers([v['first'][k] for v in values]) for k in
                       ('top_contact','top_open','bowl_contact','bowl_in')})


def compare(scores,entries,when):
    rows={(e['arm'],e['block'],e['key'],e['mode']):scores[e['session']][when] for e in entries}
    by_mode={m:summarize([v for k,v in rows.items() if k[-1]==m]) for m in DESIGN['modes']}
    pairs={}
    for left,right in [('finger_hold','pose'),('immediate','pose'),('finger_hold','immediate')]:
        counts=Counter((v['bowl_in'],rows[(*key[:-1],right)]['bowl_in']) for key,v in rows.items() if key[-1]==left)
        pairs[f'{left}_vs_{right}']=dict(left_only=counts[True,False],right_only=counts[False,True],
                                        both_in=counts[True,True],neither=counts[False,False])
    return dict(by_mode=by_mode,paired=pairs)


def score(out, standalone_only=False):
    sources=out/'sources'
    check_freeze(sources)
    qual=read(out/'qualification.json')
    runtime=read(out/'runtime.json')
    assert 'NVIDIA' in qual['renderer'] and read(out/'design.json')==DESIGN
    assert read(sources/DESIGN_FILE)==DESIGN and sha(sources/DESIGN['bddl'])==DESIGN['bddl_sha256']
    assert all(sha(sources/n)==v for n,v in runtime['sources'].items())
    assert digest(runtime['checkpoint'])==BASE['checkpoint_manifest_sha256']
    keys=read(out/'rng.json')
    assert digest(keys)==DESIGN['rng_sha256']
    assert digest({seed:seq[:BASE['key_offset']+BASE['budgets'][-1]//BASE['period']+1] for seed,seq in keys.items()})==BASE['rng_schedule_sha256']
    preps,summary=validate_preparations(out,qual['geometry'])
    assert summary==qual['preparations'] and planned()==read(out/'sessions.json')
    entries=list(planned().values())
    if standalone_only:
        entries=[e for e in entries if e['stage']=='standalone']
    names={e['session'] for e in entries}
    assert names=={p.stem for p in (out/'paths').glob('*.json')}=={p.stem for p in (out/'receipts').glob('*.jsonl')}
    frames=set()
    scores={e['session']:path_score(out,e,preps[e['arm'],e['mode']],qual['geometry'],keys,frames) for e in entries}
    times=list(next(iter(scores.values())))
    direct=[e for e in entries if e['stage']=='standalone']
    def direct_counts(group):
        return {t:summarize([scores[e['session']][t] for e in group]) for t in times}
    gate=dict(all=direct_counts(direct), by_block={str(b):direct_counts([e for e in direct if e['block']==b]) for b in FINGERS['blocks']})
    if standalone_only:
        return gate
    assert gate==read(out/'standalone.json')
    follow=[e for e in entries if e['stage']=='continuation']
    groups={'all':follow}
    cells=[]
    for arm in FINGERS['arms']:
        groups[arm]=[e for e in follow if e['arm']==arm]
        for block in FINGERS['blocks']:
            k=f'{arm}/b{block}'
            cells.append(k)
            groups[k]=[e for e in groups[arm] if e['block']==block]
    comparisons={k:{t:compare(scores,group,t) for t in times} for k,group in groups.items()}
    direction={}
    for tick in DESIGN['deadlines']:
        t=str(tick)
        pairs=[comparisons[k][t]['paired']['finger_hold_vs_pose'] for k in cells]
        direction[t]=dict(standalone_succeeded=gate['all'][t]['first']['bowl_in']['n']>0,
                          hold_ahead_every_cell=all(p['left_only']>p['right_only'] for p in pairs),
                          return_ahead_every_cell=all(p['right_only']>p['left_only'] for p in pairs))
    return dict(standalone=gate, comparisons=comparisons, direction=direction, paths=len(entries), standalone_paths=len(direct),
                continuation_paths=len(follow), controls=sum(e['horizon'] for e in entries),
                prefix_controls=sum(e['prefix_controls'] for e in entries), policy_queries=sum(e['queries'] for e in entries),
                outcomes=scores)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('stage',choices=['gate','score','verify','replay'],nargs='?',default='verify')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with unpack(args.folder) as out:
        if args.stage=='replay':
            proof=replay(out,script='upper_bowl_sim.py',entries=read(out/'sessions.json'))
            if args.output:
                write_json(args.output,proof)
                print('Physically replayed',proof['paths'],'paths')
            else:
                print(json.dumps(proof))
        elif args.stage=='gate':
            gate=score(out,standalone_only=True)
            write_json(out/'standalone.json',gate)
            print('Standalone placements at 15 and 30 s:',[gate['all'][str(t)]['bowl_in'] for t in (300,600)])
        else:
            result=score(out)
            if args.stage=='score':
                write_json(out/'verification.json',result)
            else:
                assert result==read(args.folder/'verification.json')
                proof=args.folder/'physical_replay.json'
                if proof.is_file():
                    check_replayed_paths(out,read(proof),planned(),{})
            print('Verified',result['standalone_paths'],'standalone and',result['continuation_paths'],'continuation paths')
