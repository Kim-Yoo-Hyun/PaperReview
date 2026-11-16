"""Frozen GAP-P4 diagnostic. All execution (including analysis) is Docker-only."""
import argparse
import copy
from dataclasses import replace
import datetime
import gzip
import hashlib
import json
import math
from pathlib import Path
import platform
import random
import sys

if not Path('/.dockerenv').exists():
    raise SystemExit('Execute with bash run.sh inside local Docker only.')
sys.path.insert(0, '/contract')
from adapter import World, Forecasts, Controller, distance, add, scale

SPEC = json.loads(Path('PROTOCOL.json').read_text())
BASE = json.loads(Path('/contract/scenes.json').read_text())


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def filehash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, allow_nan=False)+'\n')


class PilotWorld(World):
    """Hold means the same active waypoint; only switch changes it at tick40."""
    def observe(self, missing=(), reverse=False):
        o = super().observe(missing=missing, reverse=reverse)
        if self.tick < self.config['event_tick']:
            return replace(o, route_id='hold', route_target=tuple(self.config['routes']['hold']))
        return o


class PilotForecasts(Forecasts):
    def __init__(self, config, episode_id, seed, method, warm=None):
        super().__init__(config, episode_id, seed, method)
        self.warm = warm or {}

    def calibrator(self, key, h):
        new = (*key, h) not in self.calibrators
        c = super().calibrator(key, h)
        if new and self.method == 'M2':
            c.scores = list(self.warm.get(str(h), []))
        return c


def make_splits():
    result = {}
    for name in ('development', 'calibration', 'test'):
        spec = SPEC['splits'][name]
        scenes = []
        for idx in range(spec['count']):
            seed = spec['seed_start']+idx
            rng = random.Random(seed)
            band = idx // spec['instances_per_band']
            center = spec['angle_centers_deg'][band]
            angle = center+rng.uniform(-SPEC['splits']['angle_jitter_deg'], SPEC['splits']['angle_jitter_deg'])
            humans = []
            for k, offset_angle in enumerate(SPEC['splits']['angle_offsets_deg']):
                theta = math.radians(angle+offset_angle)
                velocity = (math.cos(theta), math.sin(theta))
                perpendicular = (-velocity[1], velocity[0])
                offset = SPEC['splits']['line_offsets_m'][k]+rng.uniform(-.15, .15)
                focus = add(tuple(SPEC['splits']['focus_xy']), scale(perpendicular, offset))
                arrival = SPEC['splits']['arrival_times_s'][k]+rng.uniform(-.4, .4)
                humans.append(dict(id=f'h{k}', start=add(focus, scale(velocity, -arrival)),
                                   goal=add(focus, scale(velocity, 10.))))
            scene = dict(id=f'{name}-{seed}', seed=seed, parameter_band=f'{name}:{center}',
                         angle_deg=angle, ego=SPEC['splits']['ego_xy'], humans=humans)
            scene['instance_hash'] = digest(scene)
            scenes.append(scene)
        result[name] = scenes
    assert len({s['seed'] for rows in result.values() for s in rows}) == 48
    assert len({s['instance_hash'] for rows in result.values() for s in rows}) == 48
    return result


def weighted_quantile(episodes, q=.9):
    """Each episode contributes total weight one, irrespective of its length."""
    rows = sorted((x, 1/len(xs)) for xs in episodes if xs for x in xs)
    target = q*sum(w for _, w in rows)
    cumulative = 0.
    for value, weight in rows:
        cumulative += weight
        if cumulative >= target-1e-12:
            return value
    raise ValueError('No calibration residuals')


def collect_scores(matured):
    return {str(h): [r['nonconformity_score_m'] for r in matured
                    if r['score_used'] and r['horizon_index']==h] for h in range(1, 6)}


def mature_summary(rows):
    summary = {}
    for h in range(1, 6):
        selected = [r for r in rows if r['horizon_index']==h]
        valid = [r for r in selected if r['score_used']]
        assert all(r['target_time_s'] <= r['score_available_time_s'] for r in selected)
        summary[str(h)] = dict(n=len(valid), uncovered=sum(not r['covered'] for r in valid),
                               invalid=len(selected)-len(valid), error_sum=sum(r['nonconformity_score_m'] for r in valid),
                               radius_sum=sum(r['radius_used_m'] for r in valid),
                               saturation=sum(r['radius_raw_m']>1 for r in valid),
                               straddling=sum(r['issue_time_s']<10<=r['target_time_s'] for r in valid))
    return summary


class Episode:
    def __init__(self, cfg, scene, method, reaction, delay, warm=None):
        ep = f'{scene["id"]}:{method}:r{int(reaction)}:d{delay}'
        self.world = PilotWorld(cfg, scene, ep, reaction, delay, False)
        self.forecasts = PilotForecasts(cfg, ep, scene['seed'], method, warm)
        self.controller = Controller(cfg, method)
        self.shadows = {m:PilotForecasts(cfg, ep, scene['seed'], m, warm)
                        for m in SPEC['execution']['main_methods'] if m != method} if method=='M0' else {}
        self.logs, self.scores = [], {str(h):[] for h in range(1, 6)}
        self.method, self.reaction, self.delay = method, reaction, delay

    def sample(self, terminal=False):
        w = self.world
        o = w.observe()
        matured = self.forecasts.observe(o)
        scores = collect_scores(matured)
        for h in self.scores:
            self.scores[h].extend(scores[h])
        shadow = {}
        for m, f in self.shadows.items():
            shadow[m] = mature_summary(f.observe(o))
        summary = mature_summary(matured)
        row = dict(tick=o.tick, time_s=o.tick*.25, ego=o.ego, velocity=o.velocity,
                   route=o.route_id, coverage=summary, shadow=shadow, terminal_observation=terminal)
        if terminal:
            self.logs.append(row)
            return
        predictions, _ = self.forecasts.issue(o)
        for f in self.shadows.values():
            f.issue(o)
        command, fallback = self.controller.choose(o, predictions, w.queue, w.delay_ticks)
        step = w.step(command)
        assert step['physical_tick']==o.tick+1
        row.update(command=command, applied=step['applied_action'], fallback=fallback,
                   clearance_m=step['actual_clearance_m'], end_ego=step['ego_after'],
                   terminal=step['terminal_reason'], path_length_m=step['path_length_m'])
        self.logs.append(row)

    def advance(self, limit):
        while self.world.tick < limit and not self.world.terminal:
            self.sample()

    def finish(self):
        self.advance(self.world.config['episode_limit_ticks'])
        self.sample(terminal=True)


def snapshot(ep):
    f, w = ep.forecasts, ep.world
    def forecast_state(f):
        return dict(history={str(k):v for k,v in f.history.items()}, pending=f.pending,
                    last_tick=f.last_tick, last_issue_tick=f.last_issue_tick,
                    calibrators={str(k):dict(experts=c.experts, scores=c.scores, weights=c.weights,
                                             chosen=c.chosen, rng=c.rng.getstate()) for k,c in f.calibrators.items()})
    return dict(ego=w.ego, velocity=w.velocity, humans=w.humans, queue=w.queue, tick=w.tick, route_reached=w.route_reached,
                world_rng={k:r.getstate() for k,r in w.rng.items()},
                forecast=forecast_state(f), shadows={m:forecast_state(s) for m,s in ep.shadows.items()},
                controller=ep.controller.__dict__)


def window_coverage(logs, start, end, shadow=None):
    result = {}
    for h in map(str, range(1,6)):
        stats = [r['shadow'][shadow][h] if shadow else r['coverage'][h]
                 for r in logs if start <= r['time_s'] < end and (not shadow or shadow in r['shadow'])]
        n = sum(s['n'] for s in stats)
        result[h] = dict(n=n, invalid=sum(s['invalid'] for s in stats),
                         uncovered=sum(s['uncovered'] for s in stats),
                         miscoverage=sum(s['uncovered'] for s in stats)/n if n else None,
                         error_mean=sum(s['error_sum'] for s in stats)/n if n else None,
                         radius_mean=sum(s['radius_sum'] for s in stats)/n if n else None,
                         saturation=sum(s['saturation'] for s in stats),
                         straddling=sum(s['straddling'] for s in stats))
    return result


def post_risk(logs):
    by_tick={r['tick']:r for r in logs if 'clearance_m' in r}
    collision_ticks=[t for t,r in by_tick.items() if r['terminal']=='collision']
    collision_tick=min(collision_ticks) if collision_ticks else None
    at_risk=0
    for tick in range(40,60):
        if tick in by_tick:
            at_risk += by_tick[tick]['clearance_m']<=.25
        elif collision_tick is not None and tick>collision_tick:
            at_risk += 1
    return at_risk/20


def metrics(ep, scene, event, fork_hash, fork_pos):
    w, rows = ep.world, ep.logs
    steps = [r for r in rows if 'clearance_m' in r]
    def position_at(tick):
        before = [r for r in rows if r['tick']<=tick]
        return before[-1]['ego']
    start, end = position_at(40), position_at(60)
    pre, post = window_coverage(rows,5,10), window_coverage(rows,10,15)
    no_progress=False
    positions={r['tick']:r['ego'] for r in rows}
    for t in positions:
        if t+20 in positions and distance(positions[t], positions[t+20])<.1 and distance(positions[t], BASE['routes']['final'])>.5:
            no_progress=True
    target=BASE['routes']['switch' if event else 'hold']
    route_length=distance(fork_pos,target)+distance(target,BASE['routes']['final'])
    out=dict(branch_id=f'{w.episode_id}:e{int(event)}',scene_id=scene['id'],scene_hash=scene['instance_hash'],
             method=ep.method,reaction=ep.reaction,delay=ep.delay,event=event,fork_hash=fork_hash,
             fork_position=fork_pos,remaining_nominal_route_m=route_length,
             prefix_eligible=True,terminal=w.terminal,terminal_tick=w.tick,path_length_m=w.path_length,
             collision=w.terminal=='collision',post_collision=any(r['terminal']=='collision' and 40<=r['tick']<60 for r in steps),
             post_risk=post_risk(rows),post_exposed_ticks=sum(40<=r['tick']<60 for r in steps),
             post_progress_m=distance(start,BASE['routes']['final'])-distance(end,BASE['routes']['final']),
             final_distance_m=distance(w.ego,BASE['routes']['final']),success=w.terminal=='goal',
             restricted_finish_time_s=w.tick*.25 if w.terminal=='goal' else 30.,
             no_progress=no_progress,fallback_ticks=sum(r['fallback'] is not None for r in steps),
             wait_ticks=sum(r['fallback']=='hysteresis_wait' for r in steps),pre_coverage=pre,post_coverage=post,
             right_censored_predictions=len(ep.forecasts.pending),shadow={})
    if ep.method=='M0':
        out['shadow']['M0']={'pre':pre,'post':post}
        for method in ep.shadows:
            out['shadow'][method]={'pre':window_coverage(rows,5,10,method),'post':window_coverage(rows,10,15,method)}
    return out


def checks():
    # Long episode should not outweigh short episode solely due to frame count.
    assert weighted_quantile([[0.]*100,[10.]])==10.
    assert weighted_quantile([[0.,1.,2.,3.,4.,5.,6.,7.,8.,9.]])==8.
    assert post_risk([dict(tick=40,clearance_m=-.1,terminal='collision')])==1.
    assert post_risk([dict(tick=40,clearance_m=1.,terminal='goal')])==0.
    w=PilotWorld(BASE,BASE['scenes'][0],switch=False)
    assert w.observe().route_target==(2.,2.)
    w.tick=40
    assert w.observe().route_target==(2.,2.)
    w.switch=True
    assert w.observe().route_target==(2.,-2.)
    assert digest({'x':[1,2]})==digest({'x':[1,2]})
    return {'weighted_episode_calibration':'PASS','collision_absorbing_window':'PASS',
            'hold_vs_switch_semantics':'PASS','stable_serialization':'PASS'}


def run(out):
    split=make_splits()
    write(out/'split.json',split)
    frozen=dict(protocol_sha256=filehash('PROTOCOL.json'),pilot_sha256=filehash('pilot.py'),
                analysis_sha256=filehash('analyse.py'),parent_adapter_sha256=filehash('/contract/adapter.py'),
                split_sha256=filehash(out/'split.json'),frozen_before_outcomes=True,
                utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),image_id=SPEC['image_id'])
    write(out/'FROZEN_RUN.json',frozen)
    write(out/'checks.json',checks())
    dev=[]
    for scene in split['development']:
        ep=Episode(BASE,scene,'M0',True,2)
        ep.advance(40)
        alive=ep.world.terminal is None
        fork_possible=alive and not ep.world.route_reached
        ep.finish()
        dev.append(dict(scene=scene['id'],alive_at_event=alive,fork_possible=fork_possible,terminal=ep.world.terminal))
    write(out/'development.json',dev)
    print('development',sum(r['alive_at_event'] for r in dev),'of',len(dev),flush=True)
    if sum(r['alive_at_event'] for r in dev)<9 or sum(r['fork_possible'] for r in dev)<9:
        write(out/'STOP.json',{'gate':'development','status':'NOT_MET'});return
    cal_scores={str(h):[] for h in range(1,6)}; cal_rows=[]
    for i,scene in enumerate(split['calibration']):
        ep=Episode(BASE,scene,'M0',bool(i%2),2*((i//2)%2));ep.world.switch=bool((i//4)%2)
        ep.finish()
        cal_rows.append(dict(scene=scene['id'],reaction=ep.reaction,delay=ep.delay,event=ep.world.switch,
                             terminal=ep.world.terminal,residuals_by_horizon=ep.scores))
        for h,xs in ep.scores.items():
            if xs:cal_scores[h].append(xs)
    if min(len(xs) for xs in cal_scores.values())<20:
        write(out/'STOP.json',{'gate':'calibration','status':'NOT_MET'});return
    radii=[weighted_quantile(cal_scores[str(h)]) for h in range(1,6)]
    warm={h:[weighted_quantile([xs]) for xs in episodes] for h,episodes in cal_scores.items()}
    calibration=dict(radii_raw_m=radii,radii_applied_m=[min(1.,max(0.,v)) for v in radii],warm_episode_quantiles=warm,
                     episodes_per_horizon={h:len(xs) for h,xs in cal_scores.items()},episodes=cal_rows,
                     estimator=SPEC['calibration']['radius_estimator'],guarantee='NONE')
    write(out/'calibration.json',calibration)
    write(out/'TEST_FREEZE.json',dict(**frozen,calibration_sha256=filehash(out/'calibration.json'),
                                     development_sha256=filehash(out/'development.json'),test_tuning=False,
                                     before_first_test_rollout=True))
    print('calibration radii',radii,flush=True)
    cfg=copy.deepcopy(BASE);cfg['controller']['fixed_fixture_radius_m']=radii
    cfg['controller']['fixed_radius_provenance']='P4 episode-balanced empirical calibration; no guarantee'
    results=[];prefix_failures=[];prefixes=0
    with (out/'compact_traces.jsonl.gz').open('wb') as raw:
        with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as trace:
            for scene in split['test']:
                for method in SPEC['execution']['main_methods']:
                    for reaction in (False,True):
                        for delay in (0,2):
                            prefix=Episode(cfg,scene,method,reaction,delay,warm)
                            prefix.advance(40);prefixes+=1
                            if prefix.world.terminal:
                                prefix_failures.append(dict(scene_id=scene['id'],method=method,reaction=reaction,
                                                            delay=delay,terminal=prefix.world.terminal,tick=prefix.world.tick))
                                continue
                            frozen_state=snapshot(prefix);fork_hash=digest(frozen_state)
                            for event in (False,True):
                                ep=copy.deepcopy(prefix)
                                assert digest(snapshot(ep))==fork_hash
                                ep.world.switch=event
                                ep.finish()
                                record=metrics(ep,scene,event,fork_hash,prefix.world.ego)
                                results.append(record)
                                trace.write((canonical(dict(branch_id=record['branch_id'],scene_id=scene['id'],
                                                             method=method,reaction=reaction,delay=delay,event=event,
                                                             steps=ep.logs))+'\n').encode())
                print('test',scene['id'],'branches',len(results),'prefix_failures',len(prefix_failures),flush=True)
    assert len(results)<=384 and prefixes==192
    write(out/'episodes.json',results)
    write(out/'prefix_failures.json',prefix_failures)
    write(out/'execution.json',dict(status='COMPLETED',prefixes=prefixes,branch_episodes=len(results),
                                   pre_event_failures=len(prefix_failures),calibration_episodes=24,development_episodes=12,
                                   test_scene_instances=12,total_branch_ticks=sum(r['terminal_tick'] for r in results),
                                   actual_unique_test_ticks=40*(prefixes-len(prefix_failures))+sum(r['tick'] for r in prefix_failures)
                                   +sum(r['terminal_tick']-40 for r in results),
                                   platform=platform.platform(),python=sys.version,
                                   adapter_unchanged=filehash('/contract/adapter.py')==frozen['parent_adapter_sha256']))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    destination=Path(args.output);destination.mkdir(parents=True,exist_ok=True)
    if (destination/'FROZEN_RUN.json').exists():
        raise SystemExit('Use fresh output directory; do not overwrite frozen evidence.')
    for name,expected in SPEC['frozen_artifacts'].items():
        if filehash(name)!=expected:raise SystemExit(f'Frozen artifact changed: {name}')
    run(destination)
