"""Validate two held-out drawer layouts, standalone gates, and paired stove continuations."""
import argparse
import ast
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_stove import D as STOVE, check_contact_rows, first, outcome, sha
from verify_stove_pose import PLAN as POSE, check_receipts, preparation_metrics, summarize

DESIGN_FILE='drawer/stove_layouts.json'
DESIGN=read(PACKET/DESIGN_FILE)
DRAWER=read(PACKET/'drawer/protocol.json')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def check_freeze(root):
    assert sha(root/DESIGN['starts_file'])==DESIGN['starts_sha256']
    assert sha(root/DESIGN['preparation'])==DESIGN['preparation_sha256']
    assert sha(root/'drawer/task.bddl')==DRAWER['bddl_sha256'] and sha(root/'drawer/stove.bddl')==STOVE['bddl_sha256']
    src=(root/'stove_pose_sim.py').read_text()
    fn=next(n for n in ast.parse(src).body if isinstance(n,ast.FunctionDef) and n.name=='prepare')
    assert hashlib.sha256(ast.get_source_segment(src,fn).encode()).hexdigest()==DESIGN['prepare_function_sha256']
    assert DESIGN['lead']==60 and DESIGN['stove_seeds']==POSE['seeds'] and DESIGN['budgets']==POSE['budgets']


def gate_plan():
    entries=[]
    for block in DESIGN['blocks']:
        group=[]
        for layout in DESIGN['layouts']:
            for key in DESIGN['gate_seeds']:
                for task in ('drawer','stove'):
                    name=f'{task}-{block}-{layout}-k{key}'
                    horizon=DESIGN['drawer_horizon'] if task=='drawer' else DESIGN['budgets'][-1]
                    group.append(dict(session=name,block=block,layout=layout,task=task,key=key,key_offset=0,lead=0,
                                      source=(DRAWER if task=='drawer' else STOVE)['prompt'],
                                      queries=horizon//DESIGN['period'],receipts='receipts/'+name+'.jsonl'))
        entries.extend(group if block==1 else reversed(group))
    return {e['session']:e for e in entries}


def follow_plan(gate):
    entries=[]
    for block in DESIGN['blocks']:
        group=[]
        for layout in DESIGN['layouts']:
            donors=gate[str(layout)]['donors']
            for arm in donors:
                src=gate[str(layout)]['trials'][arm]
                if src['block']!=block:
                    continue
                for key in DESIGN['stove_seeds']:
                    modes=DESIGN['modes']
                    split=(key+src['key'])%len(modes)
                    for mode in modes[split:]+modes[:split]:
                        n=0 if mode=='immediate' else DESIGN['lead']
                        name=f'{arm}-{mode}-s{key}'
                        group.append(dict(session=name,arm=arm,block=block,layout=layout,mode=mode,lead=n,key=key,
                                          key_offset=DESIGN['key_offset'],source=STOVE['prompt'],
                                          queries=(DESIGN['budgets'][-1]-n)//DESIGN['period'],receipts='receipts/'+name+'.jsonl'))
        entries.extend(group if block==1 else reversed(group))
    return {e['session']:e for e in entries}


def gate_score(out, keys, seen):
    plan=gate_plan()
    assert read(out/'gate_sessions.json')==plan
    assert {p.stem for p in (out/'gates').glob('*.json')}==set(plan)
    result={}
    for layout in DESIGN['layouts']:
        trials={}
        initials=set()
        for name,e in plan.items():
            if e['layout']!=layout:
                continue
            t=read(out/'gates'/(name+'.json'))
            assert all(t[k]==e[k] for k in ('session','block','layout','key','task'))
            assert not t['initial']['on'] and not t['initial']['drawer_open'] and not t['initial']['button_contact']
            initials.add(t['initial_physics'])
            sample=t['queries'][0]
            assert sample['state'][:3]==t['common']['xyz']
            check_receipts(out,e,t,keys,seen,dict(physics=t['initial_physics'],state=sample['state']))
            rows=[t['initial'],*t['rows']]
            check_contact_rows(rows,t['geometry'])
            horizons=[v for v in DESIGN['budgets'] if v<len(rows)]
            values={str(h):outcome(rows,h,None,0) for h in horizons}
            touched=first(rows,'drawer_contact')
            success=(touched is not None and rows[-1]['drawer_open'] if e['task']=='drawer'
                     else values[str(horizons[-1])]['button_and_on'])
            trials[name]=dict(task=e['task'],block=e['block'],key=e['key'],success=success,first_drawer_contact=touched,
                              first_drawer_open=first(rows,'drawer_open'),last_drawer_contact=max(
                                  (i for i,r in enumerate(rows) if r['drawer_contact']),default=None),
                              end_drawer_contact=rows[-1]['drawer_contact'],ever_stove_on=first(rows,'on') is not None,
                              final_physics=t['final_physics'],deadlines=values)
        assert len(initials)==1
        counts={task:sum(x['success'] for x in trials.values() if x['task']==task) for task in ('drawer','stove')}
        eligible=all(counts.values())
        donors=[n for n,x in trials.items() if eligible and x['task']=='drawer' and x['success'] and not x['ever_stove_on']]
        result[str(layout)]=dict(initial_physics=next(iter(initials)),successes=counts,competent=eligible,donors=donors,
                                 unique_donor_states=len({trials[n]['final_physics'] for n in donors}),trials=trials)
    assert len({x['initial_physics'] for x in result.values()})==len(DESIGN['layouts'])
    return result


def qualifications(out,gate):
    report=read(out/'qualification.json')
    assert report['lead']==DESIGN['lead'] and 'NVIDIA' in report['renderer']
    preps,metrics={},{}
    for layout,group in gate.items():
        for arm in group['donors']:
            source=read(out/'gates'/(arm+'.json'))
            metrics[arm]={}
            for mode in DESIGN['modes']:
                n=0 if mode=='immediate' else DESIGN['lead']
                pre=read(out/'preparation'/f'{arm}-{mode}-{n}.json')
                assert (pre['arm'],pre['mode'],pre['length'])==(arm,mode,n)
                assert pre['common']==source['common'] and pre['geometry']==source['geometry']
                assert pre['donor_physics']==source['final_physics']
                assert pre['start']['stove']=={k:v for k,v in source['rows'][-1].items() if k!='action'}
                assert len(pre['rows'])==len(pre['actions'])==n
                if n:
                    metrics[arm][mode]=preparation_metrics(pre)
                    for i,cmd in enumerate(pre['actions']):
                        assert len(cmd)==(7 if i<POSE['clear_controls'] else 8)
                        assert cmd[-1]==POSE['open_gripper'] and max(map(abs,cmd))<=1
                else:
                    assert pre['first']['physics']==pre['donor_physics']
                assert pre['first']['state'][:3]==pre['handoff']['tool']['xyz']
                preps[arm,mode]=pre
    assert report['donors']==metrics
    return preps,metrics


def score_continuation(out,e,pre,trial,keys,seen):
    t=read(out/'paths'/(e['session']+'.json'))
    assert all(t[k]==e[k] for k in ('session','arm','mode','block','lead')) and t['seed']==e['key']
    check_receipts(out,e,t,keys,seen,pre['first'])
    rows=[pre['start']['stove'],*[x['stove'] for x in pre['rows']],*t['rows']]
    assert len(rows)==1+DESIGN['budgets'][-1]
    check_contact_rows(rows,pre['geometry'])
    def at(h):
        return outcome(rows,h,trial['last_drawer_contact'],DESIGN['drawer_horizon'])
    values={str(h):at(h) for h in DESIGN['budgets']}
    for h in DESIGN['budgets']:
        exposure=h-DESIGN['lead']
        values['policy_'+str(exposure)]=at(e['lead']+exposure)
    return values


def comparison(rows,donors,measure):
    by_mode={}
    pairs={}
    for mode in DESIGN['modes']:
        group=[rows[f'{d}-{mode}-s{k}'][measure] for d in donors for k in DESIGN['stove_seeds']]
        by_mode[mode]=summarize(group)
        if mode=='pose':
            continue
        count=Counter((rows[f'{d}-pose-s{k}'][measure]['on'],rows[f'{d}-{mode}-s{k}'][measure]['on'])
                      for d in donors for k in DESIGN['stove_seeds'])
        pairs[mode]=dict(both_on=count[True,True],pose_only=count[True,False],control_only=count[False,True],
                         both_off=count[False,False])
    return dict(by_mode=by_mode,paired=pairs,
                pose_beats_both=bool(donors) and all(v['pose_only']>v['control_only'] for v in pairs.values()))


def score(out):
    assert read(out/'design.json')==DESIGN
    check_freeze(out/'sources')
    runtime=read(out/'runtime.json')
    assert digest(runtime['checkpoint'])==DESIGN['checkpoint_manifest_sha256']
    assert all(sha(out/'sources'/n)==v for n,v in runtime['sources'].items())
    keys=read(out/'rng.json')
    assert digest(keys)==DESIGN['rng_schedule_sha256']
    seen=set()
    gate=gate_score(out,keys,seen)
    assert gate==read(out/'gate.json')
    preps,metrics=qualifications(out,gate)
    plan=follow_plan(gate)
    assert plan==read(out/'sessions.json')
    assert set(plan)=={p.stem for p in (out/'paths').glob('*.json')}
    assert set(gate_plan())|set(plan)=={p.stem for p in (out/'receipts').glob('*.jsonl')}
    outcomes={}
    for n,e in plan.items():
        trial=gate[str(e['layout'])]['trials'][e['arm']]
        outcomes[n]=score_continuation(out,e,preps[e['arm'],e['mode']],trial,keys,seen)
    by_layout={}
    for l,group in gate.items():
        donors=group['donors']
        valid=[n for n in donors if all(v['passed'] for v in metrics[n].values())]
        groups={'all':donors,'qualified_only':valid,
                **{f'block_{b}':[n for n in donors if group['trials'][n]['block']==b] for b in DESIGN['blocks']}}
        measures=[str(h) for h in DESIGN['budgets']]+['policy_'+str(h-DESIGN['lead']) for h in DESIGN['budgets']]
        stats={stage:{h:comparison(outcomes,ds,h) for h in measures} for stage,ds in groups.items()}
        passed={h:all(stats[f'block_{b}'][h]['pose_beats_both'] for b in DESIGN['blocks']) for h in measures}
        endpoint={n:{h:comparison(outcomes,[n],h) for h in map(str,DESIGN['budgets'])} for n in donors}
        by_layout[l]=dict(donors=len(donors),qualified=valid,preparation={n:metrics[n] for n in donors},comparisons=stats,
                          by_endpoint=endpoint,advantage_each_block=passed,qualified_transfer_15s=bool(
                              group['competent'] and len(valid)==len(donors) and passed['300']))
    g=gate_plan()
    return dict(gate=gate,layout_results=by_layout,two_layout_transfer=all(v['qualified_transfer_15s'] for v in by_layout.values()),
                gate_paths=len(g),gate_controls=sum(e['queries']*DESIGN['period'] for e in g.values()),
                continuations=len(plan),continuation_controls=len(plan)*DESIGN['budgets'][-1],
                total_policy_queries=sum(e['queries'] for e in [*g.values(),*plan.values()]),
                first_frame_hashes=len(seen),outcomes_by_path=outcomes)


def replay(out, *, script='stove_layouts_sim.py', entries=None, workers=4):
    if entries is None:
        entries={**read(out/'gate_sessions.json'),**read(out/'sessions.json')}
    def run(name):
        cmd=[sys.executable,str(PACKET/script),str(out),'replay',name]
        proc=subprocess.run(cmd,capture_output=True,text=True,timeout=360)
        if proc.returncode:
            raise RuntimeError(name+' '+proc.stderr[-1400:])
        return json.loads(proc.stdout.strip().splitlines()[-1])
    with ThreadPoolExecutor(max_workers=workers) as pool:
        runs=list(pool.map(run,sorted(entries)))
    return dict(paths=len(runs),total_controls=sum(v['lead']+v['policy_controls'] for v in runs),
                prefix_controls=sum(v['prefix_controls'] for v in runs),runs=runs)


def check_replay(out,report,result):
    gates=gate_plan()
    entries={**gates,**read(out/'sessions.json')}
    assert report['total_controls']==result['gate_controls']+result['continuation_controls']
    assert report['prefix_controls']==DESIGN['drawer_horizon']*result['continuations']
    check_replayed_paths(out,report,entries,gates)


def check_replayed_paths(out,report,entries,gates):
    runs=report['runs']
    assert report['paths']==len(runs)==len(entries) and {r['session'] for r in runs}==set(entries)
    assert report['total_controls']==sum(r['lead']+r['policy_controls'] for r in runs)
    assert report['prefix_controls']==sum(r['prefix_controls'] for r in runs)
    for r in runs:
        n=r['session']
        e=entries[n]
        section='gates' if n in gates else 'paths'
        assert r['final_physics']==read(out/section/(n+'.json'))['final_physics']
        assert r['prefix_controls']==e.get('prefix_controls',0 if n in gates else DESIGN['drawer_horizon'])
        assert r['lead']==e['lead'] and r['observations']==e['queries'] and r['policy_controls']==e['queries']*DESIGN['period']
        assert all(t in range(e['lead'],e['lead']+r['policy_controls'],DESIGN['period']) for t in r['changed_rgb_ticks'])


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('folder',type=Path)
    ap.add_argument('stage',choices=['verify','score','gate','replay'],nargs='?',default='verify')
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    with unpack(a.folder) as out:
        if a.stage=='gate':
            write_json(out/'gate.json',gate_score(out,read(out/'rng.json'),set()))
        elif a.stage=='replay':
            proof=replay(out)
            if a.output:
                write_json(a.output,proof)
                print('Physical replay completed for',proof['paths'],'paths')
            else:
                print(json.dumps(proof))
        else:
            result=score(out)
            if a.stage=='score':
                write_json(out/'verification.json',result)
            else:
                assert result==read(a.folder/'verification.json')
                report=a.folder/'physical_replay.json'
                if report.is_file():
                    check_replay(out,read(report),result)
            print('Verified',result['gate_paths'],'standalone and',result['continuations'],'continuation paths')
