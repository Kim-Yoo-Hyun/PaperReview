"""Executable contract checks and exactly three bounded smoke scenes. Docker only."""
import argparse
import copy
from dataclasses import asdict, is_dataclass, replace
import datetime
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import traceback

if not Path('/.dockerenv').exists():
    raise SystemExit('Use bash run.sh check; host execution is forbidden.')

from adapter import (World, Forecasts, Controller, Observation, Track, distance,
                     swept_clearance, stream)

CFG = json.loads(Path('scenes.json').read_text())


def encode(obj):
    return asdict(obj) if is_dataclass(obj) else str(obj)


def serial(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), default=encode, allow_nan=False)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def obs(tick, x=0., episode='fixture', generation=0, missing=False):
    tracks = () if missing else (Track('h0', generation, (x, 0.), tick),)
    return Observation(episode, tick, (-10., 0.), (0., 0.), (10., 0.), 'hold', tracks)


def raises(fn, exception=ValueError):
    try:
        fn()
    except exception:
        return
    raise AssertionError(f'Expected {exception.__name__}')


def timestamp_maturity():
    f = Forecasts(CFG, 'fixture', 1)
    f.observe(obs(0)); initial, _ = f.issue(obs(0))
    assert not any(r['prediction_valid'] for r in initial)
    assert not f.pending
    assert not f.observe(obs(1, .25))
    rows, _ = f.issue(obs(1, .25))
    assert [r['target_time_s'] for r in rows] == [.5, .75, 1., 1.25, 1.5]
    assert [r['predicted_position_xy_m'][0] for r in rows] == [.5, .75, 1., 1.25, 1.5]
    raises(lambda: f.issue(obs(1, .25)))
    matured = f.observe(obs(2, .5))
    assert len(matured) == 1 and matured[0]['horizon_index'] == 1
    assert matured[0]['nonconformity_score_m'] == 0
    assert len(f.pending) == 4
    raises(lambda: f.observe(obs(2, .5)))
    return {'first_valid_issue_s': .25, 'first_matured_target_s': .5, 'future_scores_still_pending': 4}


def track_permutation():
    a, b = Forecasts(CFG, 'perm', 4), Forecasts(CFG, 'perm', 4)
    last = []
    for tick in (0, 1):
        tracks = (Track('near', 0, (1.+tick*.25, 0.), tick), Track('far', 0, (3.-tick*.25, 0.), tick))
        o = Observation('perm', tick, (0., 0.), (0., 0.), (9., 0.), 'hold', tracks)
        rev = Observation(**{**o.__dict__, 'tracks': tuple(reversed(tracks))})
        a.observe(o); b.observe(rev)
        ra, pa = a.issue(o); rb, pb = b.issue(rev)
        assert serial(ra) == serial(rb) and pa == pb
        last = ra
    by = {r['track_id']: r for r in last if r['horizon_index'] == 1}
    assert by['near']['predicted_position_xy_m'][0] == 1.5
    assert by['far']['predicted_position_xy_m'][0] == 2.5
    return {'reversed_input_same_id_forecasts': True, 'opposite_track_velocities_preserved': True}


def missing_and_reappearance():
    f = Forecasts(CFG, 'fixture', 5)
    for tick in (0, 1):
        o = obs(tick, tick*.25); f.observe(o); f.issue(o)
    absent = f.observe(obs(2, missing=True))
    assert len(absent) == 1 and absent[0]['score_used'] is False
    assert absent[0]['nonconformity_score_m'] is None
    f.issue(obs(2, missing=True))
    back = f.observe(obs(3, .75))
    assert len(back) == 1 and back[0]['horizon_index'] == 2
    assert back[0]['nonconformity_score_m'] == 0
    issued, _ = f.issue(obs(3, .75))
    assert issued[0]['predicted_position_xy_m'] == (1., 0.)
    # Skipped clock ticks must not be retroactively assigned a later observation.
    skipped = f.observe(obs(5, 1.25))
    assert any(r['target_tick'] == 4 and not r['score_used'] for r in skipped)
    return {'missing_score_is_null': True, 'gap_velocity_uses_elapsed_0_5s': True, 'skipped_target_not_relabelled': True}


def generation_replacement():
    f = Forecasts(CFG, 'fixture', 7)
    for tick in (0, 1):
        o = obs(tick, tick*.25); f.observe(o); f.issue(o)
    replaced = obs(2, 100., generation=1)
    rows = f.observe(replaced)
    assert rows and not any(r['score_used'] for r in rows)
    issued, _ = f.issue(replaced)
    assert not any(r['prediction_valid'] for r in issued)
    assert all(not c.scores for key, c in f.calibrators.items() if key[1] == 1)
    return {'same_slot_new_generation_no_old_history': True}


def episode_reset():
    f = Forecasts(CFG, 'fixture', 8)
    f.observe(obs(0)); f.issue(obs(0))
    raises(lambda: f.observe(obs(1, episode='other')))
    fresh = Forecasts(CFG, 'other', 8)
    o = obs(0, episode='other'); fresh.observe(o); rows, _ = fresh.issue(o)
    assert not fresh.pending and not any(r['prediction_valid'] for r in rows)
    return {'cross_episode_rejected': True, 'fresh_episode_no_pending_scores': True}


def issued_clipped_radius():
    cfg = copy.deepcopy(CFG)
    cfg['controller']['fixed_fixture_radius_m'] = [2.] * 5
    f = Forecasts(cfg, 'fixture', 11)
    for tick in (0, 1):
        o = obs(tick); f.observe(o); rows, _ = f.issue(o)
    assert rows[0]['radius_raw_m'] == 2. and rows[0]['radius_used_m'] == 1.
    f.calibrator(('h0', 0), 1).experts = [99.] * 3
    matured = f.observe(obs(2, 1.5))[0]
    assert matured['nonconformity_score_m'] == 1.5
    assert matured['covered'] is False
    assert matured['nonconformity_score_m'] <= matured['radius_raw_m']
    return {'score_m': 1.5, 'issued_raw_m': 2., 'issued_used_m': 1., 'actual_coverage': False,
            'negative_control_raw_radius_would_falsely_cover': True}


def terminal_and_swept_collision():
    # Both endpoint clearances are positive, yet the discs cross midway.
    clearance = swept_clearance((-1., 0.), (1., 0.), (0., -1.), (0., 1.), .6)
    assert math.isclose(clearance, -.6)
    assert distance((-1., 0.), (0., -1.)) > .6
    cfg = copy.deepcopy(CFG); cfg['episode_limit_ticks'] = 1
    w = World(cfg, cfg['scenes'][0], delay_ticks=0)
    step = w.step((.5, 0.))
    assert step['terminal_reason'] == 'timeout'
    assert step['terminal_observation']['ego'] == w.ego
    assert math.isclose(step['path_length_m'], .125)
    raises(lambda: w.step((.5, 0.)))
    new = World(cfg, cfg['scenes'][0], episode_id='new')
    assert new.path_length == 0 and new.tick == 0
    assert w.tick == 1 and w.ego != new.ego
    return {'swept_collision_clearance_m': clearance, 'terminal_path_m': .125, 'no_reset_jump': True}


def warm_world(method='M1'):
    w = World(CFG, CFG['scenes'][0], delay_ticks=0)
    f = Forecasts(CFG, w.episode_id, w.seed, method)
    o = w.observe(); f.observe(o); f.issue(o); w.step((.5, 0.))
    o = w.observe(); f.observe(o); rows, _ = f.issue(o)
    return w, f, o, rows


def oracle_input_invariance():
    w, f, o, rows = warm_world()
    changed = w.clone()
    for h in changed.humans:
        h['goal'] = (999., -999.)
    changed.hidden_future_truth = {'collision': True, 'preferred_mode': 'oracle'}
    changed.reactive = not changed.reactive
    o2 = changed.observe()
    assert o == o2
    c = Controller(CFG)
    c2 = copy.deepcopy(c)
    assert c.choose(o, rows, w.queue, 0) == c2.choose(o2, rows, changed.queue, 0)
    forbidden = {'goal', 'human_goal', 'future', 'reaction', 'outcome'}
    assert not (forbidden & set(o.__dict__))
    bad_rows = copy.deepcopy(rows); bad_rows[0]['issue_tick'] += 1
    raises(lambda: c.choose(o, bad_rows, w.queue, 0))
    return {'hidden_goal_future_reaction_changed_same_command': True, 'wrong_issue_tick_rejected': True}


def rng_isolation_and_clone():
    w, f, o, rows = warm_world()
    clone, ff = w.clone(), copy.deepcopy(f)
    before = {k: v.getstate() for k, v in w.rng.items()}
    for _ in range(100):
        f.calibrator(('h0', 0), 1).rng.random()
    assert before == {k: v.getstate() for k, v in w.rng.items()}
    assert serial(w.step((.5, 0.))) == serial(clone.step((.5, 0.)))
    assert ff.calibrator(('h0', 0), 1).rng.getstate() != f.calibrator(('h0', 0), 1).rng.getstate()
    assert stream(1, 'scene').getstate() != stream(1, 'calibrator').getstate()
    return {'calibrator_rng_cannot_advance_world_rng': True, 'cloned_physics_identical': True}


def reactive_human_input():
    w = World(CFG, CFG['scenes'][0], delay_ticks=0)
    w.ego, w.velocity = (1., 0.), (-1., 0.)
    w.humans[0].update(position=(-1., 0.), velocity=(1., 0.), goal=(5., 0.))
    for i, h in enumerate(w.humans[1:]):
        h.update(position=(30.+i*3, 30.), velocity=(0., 0.), goal=(40.+i*3, 30.))
    unreactive = w.clone(); unreactive.reactive = False
    a, witness = w.human_actions(); b, _ = unreactive.human_actions()
    delta = distance(a[0], b[0])
    assert delta > 1e-6
    assert 'ego' in witness[0]['observed_agent_ids']
    step = w.step((0., 1.))
    assert step['human_input'][0]['ego_velocity_seen'] == (-1., 0.)
    assert step['applied_action'] == (0., 1.)
    return {'reactivity_velocity_difference_mps': delta, 'old_ego_velocity_seen_before_new_action_integration': True}


def actuation_delay_and_clock():
    w = World(CFG, CFG['scenes'][0], reactive=False, delay_ticks=2)
    start, human = w.ego, w.humans[0]['position']
    steps = [w.step((1., 0.)) for _ in range(3)]
    assert steps[0]['ego_after'] == start and steps[1]['ego_after'] == start
    assert math.isclose(distance(steps[2]['ego_after'], start), .25)
    assert [s['physical_time_s'] for s in steps] == [.25, .5, .75]
    assert steps[2]['applied_command_tick'] == 0
    assert distance(w.humans[0]['position'], human) > 0
    direct = World(CFG, CFG['scenes'][0], reactive=False, delay_ticks=0)
    assert math.isclose(distance(direct.step((1., 0.))['ego_after'], start), .25)
    return {'queued_command_delay_s': .5, 'world_advances_while_ego_waits': True, 'wall_clock_not_used': True}


def method_interface_and_hysteresis():
    count = []
    for method in ('M0', 'M1', 'M2', 'M3'):
        w, f, o, rows = warm_world(method)
        c = Controller(CFG, method)
        action, reason = c.choose(o, rows, w.queue, 0)
        assert len(c.candidates) == 33 and math.hypot(*action) <= 1.00000001
        count.append(len(c.candidates))
    w, f, o, rows = warm_world('M3')
    c = Controller(CFG, 'M3')
    close = copy.deepcopy(o.__dict__)
    close['tracks'] = (Track('h0', 0, (o.ego[0]+.8, o.ego[1]), o.tick),) + o.tracks[1:]
    assert c.choose(Observation(**close), rows, [], 0)[1] == 'hysteresis_wait'
    def retime(tick):
        timed = replace(o, tick=tick, tracks=tuple(replace(t, observed_tick=tick) for t in o.tracks))
        issued = copy.deepcopy(rows)
        for r in issued:
            r.update(issue_tick=tick, issue_time_s=tick*CFG['dt_s'],
                     target_tick=tick+r['horizon_index'], target_time_s=(tick+r['horizon_index'])*CFG['dt_s'])
        return timed, issued
    o2, rows2 = retime(2)
    assert c.choose(o2, rows2, [], 0)[1] == 'hysteresis_wait'
    raises(lambda: c.choose(o2, rows2, [], 0))
    o3, rows3 = retime(3)
    assert c.choose(o3, rows3, [], 0)[1] != 'hysteresis_wait'
    wrong = copy.deepcopy(rows3); wrong[0]['track_generation'] += 1
    raises(lambda: Controller(CFG, 'M3').choose(o3, wrong, [], 0))
    return {'same_action_counts': count, 'two_clear_ticks_required_to_resume': True,
            'baseline_calibration_is_fixture_only': True}


def run_smoke(trace):
    summaries = []
    for scene in CFG['scenes']:
        w = World(CFG, scene)
        f, controller = Forecasts(CFG, w.episode_id, w.seed), Controller(CFG)
        matured_count, issued_count, fork_checked, event_seen = 0, 0, False, False
        for _ in range(CFG['smoke_limit_ticks']):
            o = w.observe(reverse=w.tick % 2 == 1)
            matured = f.observe(o)
            rows, permutation = f.issue(o)
            action, reason = controller.choose(o, rows, w.queue, w.delay_ticks)
            if w.tick == CFG['event_tick']:
                event_seen = o.route_id == 'switch'
                twin = w.clone(); twin.switch = False
                assert twin.ego == w.ego and twin.humans == w.humans and twin.queue == w.queue
                assert twin.observe().route_id == 'hold'
                assert twin.observe().route_target != o.route_target
                assert {k:r.getstate() for k,r in twin.rng.items()} == {k:r.getstate() for k,r in w.rng.items()}
                fork_f = copy.deepcopy(f)
                assert fork_f.history == f.history and fork_f.pending == f.pending
                assert {k:c.rng.getstate() for k,c in fork_f.calibrators.items()} == {k:c.rng.getstate() for k,c in f.calibrators.items()}
                fork_checked = True
            step = w.step(action)
            row = dict(episode_id=w.episode_id, pair_id=f"{w.episode_id}:event40", split='smoke_only',
                       scene_hash=sha('scenes.json'), source_revision=sha('adapter.py'),
                       route_id=o.route_id, event_time_s=CFG['event_tick']*CFG['dt_s'],
                       observation=o, forecast=rows, matured=matured, sort_permutation=permutation,
                       fallback_reason=reason, rng_stream_id=f'{scene["seed"]}:separate_named_streams', **step)
            line = serial(row)
            trace.write((line+'\n').encode())
            assert step['physical_tick'] == o.tick + 1
            assert all(r['target_time_s'] > r['issue_time_s'] for r in rows)
            assert all(r['score_available_time_s'] >= r['target_time_s'] for r in matured)
            assert all(r['track_id'] in {t.track_id for t in o.tracks} for r in rows)
            issued_count += len(rows); matured_count += len(matured)
            if w.terminal:
                break
        # A premature termination is a qualification failure, never silently replaced.
        assert event_seen and fork_checked, f'{scene["id"]}: pre-event termination {w.terminal}'
        summaries.append(dict(scene=scene['id'], seed=scene['seed'], physical_ticks=w.tick,
                              physical_time_s=w.tick*CFG['dt_s'], terminal_reason=w.terminal,
                              stop_reason=w.terminal or 'probe_limit', forecast_records=issued_count,
                              matured_records=matured_count, route_event_and_fork_verified=True))
    assert len(summaries) == 3
    return summaries


def audit_persisted_trace(path):
    """Rejoin saved predictions to observations independently of Forecasts internals."""
    issued, last_times, commands = {}, {}, {}
    joined, step_count = 0, 0
    with gzip.open(path, 'rt') as source:
        for line in source:
            row = json.loads(line)
            o, ep = row['observation'], row['episode_id']
            assert ep == o['episode_id']
            assert row['physical_tick'] == o['tick']+1
            assert o['tick'] == last_times.get(ep, -1)+1
            last_times[ep] = o['tick']
            tracks = {(t['track_id'], t['generation']):t for t in o['tracks']}
            for m in row['matured']:
                original = issued[m['prediction_id']]
                assert all(m[k] == original[k] for k in ('episode_id', 'track_id', 'track_generation',
                           'target_tick', 'radius_used_m', 'radius_raw_m', 'predicted_position_xy_m'))
                if m['score_used']:
                    assert m['target_tick'] == o['tick']
                    actual = tracks[(m['track_id'], m['track_generation'])]['position']
                    assert m['observed_target_position_xy_m'] == actual
                    error = math.hypot(*(a-b for a,b in zip(actual, original['predicted_position_xy_m'])))
                    assert math.isclose(error, m['nonconformity_score_m'], abs_tol=1e-12)
                    assert m['covered'] == (error <= original['radius_used_m'])
                joined += 1
            for prediction in row['forecast']:
                assert prediction['prediction_id'] not in issued
                issued[prediction['prediction_id']] = prediction
            commands[(ep, o['tick'])] = row['command']
            expected = [0., 0.] if o['tick'] < 2 else commands[(ep, o['tick']-2)]
            assert row['applied_action'] == expected
            assert row['scheduled_execution_time_s'] == (o['tick']+2)*CFG['dt_s']
            assert row['execution_time_s'] == (o['tick']*CFG['dt_s'] if o['tick'] >= 2 else None)
            assert row['applied_command_time_s'] == ((o['tick']-2)*CFG['dt_s'] if o['tick'] >= 2 else None)
            expected_position = [p+v*CFG['dt_s'] for p,v in zip(row['ego_before'], expected)]
            assert row['ego_after'] == expected_position
            step_count += 1
    assert step_count == 150 and joined == 2760 and len(issued) == 3000
    return {'independently_rejoined_matured_records': joined, 'unique_prediction_ids': len(issued),
            'fifo_and_physical_step_rows': step_count, 'episode_count': len(last_times)}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', required=True); args = ap.parse_args()
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(Path('RUN_MANIFEST.json').read_text())
    for name, expected in manifest['artifact_hashes'].items():
        if sha(name) != expected:
            raise RuntimeError(f'Frozen artifact changed: {name}; refreeze before execution')
    checks = []
    functions = [timestamp_maturity, track_permutation, missing_and_reappearance, generation_replacement,
                 episode_reset, issued_clipped_radius, terminal_and_swept_collision, oracle_input_invariance,
                 rng_isolation_and_clone, reactive_human_input, actuation_delay_and_clock,
                 method_interface_and_hysteresis]
    for fn in functions:
        try:
            witness = fn(); checks.append(dict(id=fn.__name__, status='PASS', witness=witness))
        except Exception:
            checks.append(dict(id=fn.__name__, status='FAIL', error=traceback.format_exc()))
    if all(c['status'] == 'PASS' for c in checks):
        try:
            with (out/'smoke_trace.jsonl.gz').open('wb') as raw:
                with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as trace:
                    scenes = run_smoke(trace)
            audit = audit_persisted_trace(out/'smoke_trace.jsonl.gz')
            checks.append(dict(id='smoke_trace_schema_and_bounds', status='PASS', scenes=scenes, persisted_trace_audit=audit))
        except Exception:
            checks.append(dict(id='smoke_trace_schema_and_bounds', status='FAIL', error=traceback.format_exc()))
    else:
        checks.append(dict(id='smoke_trace_schema_and_bounds', status='NOT_RUN', reason='unit contract failed'))
    report = dict(task='GAP-P3', scope='contract qualification only',
                  status='PASS' if all(c['status']=='PASS' for c in checks) else 'FAIL', checks=checks,
                  research_effect_tested=False, native_vla_tested=False, training=False,
                  artifacts={name:sha(name) for name in manifest['artifact_hashes']},
                  manifest_sha256=sha('RUN_MANIFEST.json'))
    if (out/'smoke_trace.jsonl.gz').exists():
        report['trace_sha256'] = sha(out/'smoke_trace.jsonl.gz')
    (out/'contract_report.json').write_text(json.dumps(report, indent=2)+'\n')
    provenance = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      python=sys.version, platform=platform.platform(), machine=platform.machine(),
                      container_marker=Path('/.dockerenv').exists(), omp_threads=os.environ.get('OMP_NUM_THREADS'),
                      rvo_binary_sha256=sha(sys.modules['rvo2'].__file__),
                      build_records={p.name:p.read_text() for p in Path('/opt/provenance').iterdir()})
    (out/'runtime_provenance.json').write_text(json.dumps(provenance, indent=2)+'\n')
    print(json.dumps({'status':report['status'], 'checks':{c['id']:c['status'] for c in checks}}, indent=2))
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
