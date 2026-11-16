"""Frozen, scene-paired P4 analysis and persisted-trace checks; Docker only."""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import random
import statistics

if not Path('/.dockerenv').exists():
    raise SystemExit('Use local Docker via run.sh.')


def write(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def mean(xs):
    xs = [x for x in xs if x is not None]
    return statistics.fmean(xs) if xs else None


def interval(xs):
    if not xs:
        return dict(n=0, mean=None, ci95=None)
    rng = random.Random(95001)
    estimates = sorted(mean(rng.choices(xs, k=len(xs))) for _ in range(1000))
    return dict(n=len(xs), mean=mean(xs), ci95=[estimates[24], estimates[974]])


def metric(row, name):
    if name.startswith('miscoverage_change_h'):
        h = name.rsplit('h', 1)[1]
        pre, post = row['pre_coverage'][h]['miscoverage'], row['post_coverage'][h]['miscoverage']
        return None if pre is None or post is None else post-pre
    return row[name]


def difference(cells, name):
    vals = {k:metric(v, name) for k,v in cells.items()}
    if len(vals)!=4 or any(v is None for v in vals.values()):
        return None
    return (vals[(True,True)]-vals[(True,False)])-(vals[(False,True)]-vals[(False,False)])


def trace_audit(out, rows):
    """Recompute risk/progress/coverage denominators from stored tick records."""
    by_id = {r['branch_id']:r for r in rows}
    seen, pairs = set(), {}
    with gzip.open(out/'compact_traces.jsonl.gz', 'rt') as f:
        for line in f:
            trace = json.loads(line); key=trace['branch_id']; r=by_id[key]
            assert key not in seen; seen.add(key)
            logs=trace['steps']; steps=[s for s in logs if 'clearance_m' in s]
            assert [s['tick'] for s in logs]==list(range(r['terminal_tick']+1))
            assert logs[-1]['terminal_observation'] and len(steps)==r['terminal_tick']
            collision=next((s['tick'] for s in steps if s['terminal']=='collision'), None)
            observed={s['tick']:s for s in steps}
            risks=[int(observed[t]['clearance_m']<=.25) if t in observed
                   else int(collision is not None and collision<t) for t in range(40,60)]
            assert abs(sum(risks)/20-r['post_risk'])<1e-12
            start=logs[min(40,r['terminal_tick'])]['ego']; end=logs[min(60,r['terminal_tick'])]['ego']
            progress=math.dist(start,[12,0])-math.dist(end,[12,0])
            assert abs(progress-r['post_progress_m'])<1e-10
            for window,start_t,end_t in [('pre',5,10),('post',10,15)]:
                for h in map(str,range(1,6)):
                    s=[x['coverage'][h] for x in logs if start_t<=x['time_s']<end_t]
                    n=sum(x['n'] for x in s); uncovered=sum(x['uncovered'] for x in s)
                    saved=r[window+'_coverage'][h]
                    assert n==saved['n'] and uncovered==saved['uncovered']
                    assert n<=80 and (saved['miscoverage'] is None if not n
                                     else abs(saved['miscoverage']-uncovered/n)<1e-12)
            prefix_key=(r['scene_id'],r['method'],r['reaction'],r['delay'])
            prefix=json.dumps(logs[:40],sort_keys=True)
            prefix_digest=hashlib.sha256(prefix.encode()).hexdigest()
            if prefix_key in pairs:
                assert pairs[prefix_key]==(prefix_digest,r['fork_hash'])
            else:pairs[prefix_key]=(prefix_digest,r['fork_hash'])
            if r['method']=='M0':
                assert r['shadow']['M0']==r['shadow']['M3']
    assert seen==set(by_id)
    return dict(status='PASS',trace_branches=len(seen),matched_prefix_pairs=len(pairs),
                checks=['physical tick continuity/terminal observation','absorbing post risk',
                        'terminal-held progress','coverage counts and missing denominators',
                        'identical persisted prefix and state hash within event pair','M0/M3 shadow equality'])


def run(out):
    # Hand-computable estimator example, independent of simulator outcomes.
    fake={(False,False):{'post_risk':1},(False,True):{'post_risk':3},
          (True,False):{'post_risk':4},(True,True):{'post_risk':9}}
    assert difference(fake,'post_risk')==3 and interval([2,2])['ci95']==[2,2]
    if (out/'STOP.json').exists():
        write(out/'analysis.json',dict(decision='HOLD_PRECONDITION_FAILED',gate=json.loads((out/'STOP.json').read_text())))
        return
    rows=json.loads((out/'episodes.json').read_text())
    failures=json.loads((out/'prefix_failures.json').read_text())
    audit=trace_audit(out,rows)
    fields=['post_risk','post_progress_m','collision','post_collision','success','no_progress',
            'final_distance_m','restricted_finish_time_s','path_length_m','remaining_nominal_route_m',
            'fallback_ticks','wait_ticks']
    names=fields+['miscoverage_change_h'+str(h) for h in range(1,6)]
    cells=[];interactions=[];shadow=[]
    for method in ('M0','M1','M2','M3'):
        for delay in (0,2):
            selected=[r for r in rows if r['method']==method and r['delay']==delay]
            for reaction in (False,True):
                for event in (False,True):
                    group=[r for r in selected if r['reaction']==reaction and r['event']==event]
                    summary={k:mean([metric(r,k) for r in group]) for k in names}
                    cells.append(dict(method=method,delay=delay,reaction=reaction,event=event,n=len(group),
                                      means=summary,collisions=sum(r['collision'] for r in group),
                                      post_risk_nonzero=sum(r['post_risk']>0 for r in group),
                                      coverage_denominators={h:dict(pre=sum(r['pre_coverage'][h]['n'] for r in group),
                                                                  post=sum(r['post_coverage'][h]['n'] for r in group))
                                                             for h in map(str,range(1,6))}))
            scenes={sid:{(r['reaction'],r['event']):r for r in selected if r['scene_id']==sid}
                    for sid in sorted({r['scene_id'] for r in selected})}
            values={k:{sid:difference(g,k) for sid,g in scenes.items() if len(g)==4} for k in names}
            summary={k:interval([v for v in vmap.values() if v is not None]) for k,vmap in values.items()}
            interactions.append(dict(method=method,delay=delay,estimates=summary,scene_values=values))
    for method in ('M0','M1','M2','M3'):
        for delay in (0,2):
            selected=[r for r in rows if r['method']=='M0' and r['delay']==delay]
            for reaction in (False,True):
                for event in (False,True):
                    group=[r for r in selected if r['reaction']==reaction and r['event']==event]
                    shadow.append(dict(calibrator=method,executed_policy='M0',delay=delay,reaction=reaction,event=event,
                                       n=len(group),h5_post_miscoverage=mean([r['shadow'][method]['post']['5']['miscoverage'] for r in group]),
                                       h5_post_radius_m=mean([r['shadow'][method]['post']['5']['radius_mean'] for r in group]),
                                       h5_change=mean([r['shadow'][method]['post']['5']['miscoverage']-r['shadow'][method]['pre']['5']['miscoverage']
                                                       for r in group if r['shadow'][method]['post']['5']['n'] and r['shadow'][method]['pre']['5']['n']])))
    def estimate(m,d,k):
        return next(x for x in interactions if x['method']==m and x['delay']==d)['estimates'][k]
    def pattern(m,d):
        risk,cov=estimate(m,d,'post_risk'),estimate(m,d,'miscoverage_change_h5')
        return (min(risk['n'],cov['n'])>=9 and risk['mean']>=.05 and cov['mean']>=.05)
    def simple_comparison(m,d):
        a={(r['scene_id'],r['reaction'],r['event']):r for r in rows if r['method']=='M1' and r['delay']==d}
        b={(r['scene_id'],r['reaction'],r['event']):r for r in rows if r['method']==m and r['delay']==d}
        ids=[k for k in a.keys()&b.keys() if k[1:] == (True,True)]
        risk=mean([b[k]['post_risk']-a[k]['post_risk'] for k in ids])
        progress=mean([b[k]['post_progress_m']-a[k]['post_progress_m'] for k in ids])
        matched=len(ids)>=9 and progress is not None and abs(progress)<=.5
        return dict(baseline=m,delay=d,n=len(ids),risk_difference_vs_M1=risk,progress_difference_vs_M1_m=progress,
                    matched_progress=matched,eliminates_joint_pattern=matched and risk<=.02 and not pattern(m,d))
    comparisons=[simple_comparison(m,d) for m in ('M0','M2','M3') for d in (0,2)]
    primary,delayed=pattern('M1',0),pattern('M1',2)
    enough=all(estimate('M1',d,k)['n']>=9 for d in (0,2) for k in ('post_risk','miscoverage_change_h5'))
    floor=not any(r['post_risk']>0 for r in rows)
    explained=any(x['delay']==0 and x['eliminates_joint_pattern'] for x in comparisons)
    if not enough or floor:decision='INCONCLUSIVE_HOLD'
    elif primary and not explained:decision='DIAGNOSTIC_REVISE_NO_METHOD_GO'
    elif primary and explained:decision='REJECT_NEW_METHOD_JUSTIFICATION_SIMPLE_BASELINE'
    elif delayed:decision='DELAY_SPECIFIC_REVISE_NO_METHOD_GO'
    else:decision='PRIMARY_PATTERN_NOT_SUPPORTED_HOLD'
    write(out/'analysis.json',dict(decision=decision,gate=dict(no_delay_joint_pattern=primary,delayed_joint_pattern=delayed,
          simple_explanation_at_matched_progress=explained,enough_paired_scenes=enough,all_zero_post_risk=floor),
          denominators=dict(branches=len(rows),pre_event_failed_prefixes=len(failures),
                            counterfactual_branches_not_started=2*len(failures),scene_instances=12,
                            post_risk_nonzero=sum(r['post_risk']>0 for r in rows),collisions=sum(r['collision'] for r in rows),
                            post_collisions=sum(r['post_collision'] for r in rows),successes=sum(r['success'] for r in rows)),
          trace_audit=audit,cells=cells,interactions=interactions,paired_simple_alternatives=comparisons,
          shadow_on_M0_observations=shadow,uncertainty='1000 paired scene bootstrap; descriptive small-n interval, not confirmatory',
          scope='One synthetic topology, ORCA response, 12 held-out parameter-band scenes; no native VLA or general safety claim'))
    print('analysis',decision,'branches',len(rows),'collisions',sum(r['collision'] for r in rows),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    run(Path(parser.parse_args().output))
