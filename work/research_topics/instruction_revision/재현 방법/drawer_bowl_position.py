"""Compare first contact under reciprocal bowl-position interventions in LIBERO."""
import argparse
from collections import Counter
from functools import partial
import json
import os
from pathlib import Path
import subprocess
from zipfile import ZipFile

from drawer_bowl_position_starts import (DESIGN, DESIGN_FILE, HOSTS, INDICES, LAYOUT, MODES, POSITIONS, SCRIPT, STUDIES,
    alternate, archive_for, check_first, checked_inputs, live_study, prepare, prepare_start)
from drawer_view_duration import LIMIT, PERIOD, behavior_record, numbers, rendered_inputs
from drawer_width import tape_for
from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import (BASE, TASK, check_archive_repeat, check_donors, check_sessions,
                                    contact_geometry, path_outcomes, planned)
from verify_stove import sha
from verify_stove_layouts import check_freeze, check_replayed_paths, digest, replay


def sessions():
    studies = {**STUDIES[2], 'arms': list(LAYOUT)}
    entries = planned(studies, modes=[m + '.' + v for v in INDICES for m in HOSTS])
    for e in entries.values():
        e['mode'], e['view'] = e['mode'].split('.')
        e['layout'] = LAYOUT[e['arm']]
    return entries


def run_path(out, entry, replaying):
    from drawer_location_sim import run
    from drawer_view_render import ViewSchedule

    arm, mode = entry['arm'], entry['mode']
    bank = read(out/'camera_inputs.json')['images'][arm]
    factory = partial(ViewSchedule, drawer='bottom', width=DESIGN['camera_width_m'], indices=INDICES[entry['view']],
                      limit=LIMIT, bank=bank[mode], opposite_bank=bank[alternate(mode)], initial_attempts=8)
    return run(out, entry, replay=replaying, view_factory=factory, cohort=live_study(out, LAYOUT[arm]),
               arrangements=read(out/'clearance.json')['arrangements'][arm])


def collect(out):
    from run_atomic import SIM_PYTHON
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block

    with ZipFile(archive_for(3)) as z:
        sources = list(json.loads(z.read('runtime.json'))['sources'])
    os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
    initialize_study(out, DESIGN, [*sources, DESIGN_FILE, SCRIPT, 'drawer_bowl_position_starts.py', 'plot_drawer_bowl_position.py'],
                     key_count=BASE['key_offset'] + TASK['extension']//PERIOD)
    sim = [SIM_PYTHON, str(PACKET/SCRIPT), str(out)]
    subprocess.run([*sim, 'prepare'], check=True)
    entries = sessions()
    write_json(out/'sessions.json', entries)
    for block in STUDIES[2]['blocks']:
        subset = [e for e in entries.values() if e['block'] == block]
        policy_block(out, sim, subset, f'block-{block}', f'policy-{block}.log', workers=5)
        print(f'Completed model load {block} with {len(subset)} paths', flush=True)
    write_json(out/'verification.json', score(out))


def direction(cells, view):
    changes = Counter()
    for positions in cells:
        flags = tuple(positions[pos]['self']['contact'] != positions[pos][view]['contact'] for pos in POSITIONS)
        changes[flags] += 1
    both = changes[True,True]
    native, crossed = changes[True,False], changes[False,True]
    return dict(pairs=len(cells), native_changed=both+native, crossed_changed=both+crossed,
                native_only=native, crossed_only=crossed, both=both, neither=changes[False,False],
                crossed_minus_native=crossed-native)


def position_outcomes(rows):
    result, transitions = {}, {}
    for view in INDICES:
        samples = [r[view] for r in rows]
        times = [s['place_tick']/20 for s in samples if s['place_tick'] is not None]
        result[view] = dict(first_placement_s=numbers(times), never_placed=len(samples)-len(times),
                            **{k: dict(Counter(s[k] for s in samples)) for k in ('contact','first_destination','at15','at30')})
        if view != 'self':
            transitions[view] = {k: dict(Counter(r['self'][k]+'->'+r[view][k] for r in rows)) for k in ('contact','at15','at30')}
    eligible = [r for r in rows if r['self']['contact'] != r['four']['contact']]
    matches = Counter()
    for r in eligible:
        target = r['late']['contact']
        matches['self' if target == r['self']['contact'] else 'four' if target == r['four']['contact'] else 'neither'] += 1
    return dict(schedules=result, transitions_from_self=transitions, eligible=len(eligible),
                late_when_controls_differ={k: matches[k] for k in ('self','four','neither')},
                late_matches_four_all=sum(r['late']['contact'] == r['four']['contact'] for r in rows))


def agreement(pairs):
    fields = ('first_20_sha256','contact','contact_tick','first_destination','place_tick','at15','at30')
    return dict(pairs=len(pairs), **{k: sum(a[k] == b[k] for a,b in pairs) for k in fields})


def layout_summary(layout, entries, paths):
    study = STUDIES[layout]
    rows = {}
    matched_parent = {v: [] for v in INDICES}
    prior = archive_for(layout).with_name('verification.json')
    assert sha(prior) == DESIGN[('layout2_parent' if layout == 2 else 'parent') + '_verification_sha256']
    reference = read(prior)['paths_by_session']
    for n,e in entries.items():
        if e['layout'] != layout:
            continue
        k = e['arm'], e['block'], e['key']
        pos,view = e['mode'].split('-')[0],e['view']
        rows.setdefault(k, {}).setdefault(pos, {})[view] = paths[n]
        if pos == 'native':
            parent_name = f"{e['arm']}-full-bottom.{view}-b{e['block']}-s{e['key']}"
            matched_parent[view].append((paths[n], reference[parent_name]))
    assert len(rows) == len(study['arms'])*len(study['blocks'])*len(BASE['stove_seeds'])
    assert all(set(r) == set(POSITIONS) and all(set(r[p]) == set(INDICES) for p in POSITIONS) for r in rows.values())
    cells = list(rows.values())
    by_start = {f'{a}/b{b}': direction([r for (arm,block,k),r in rows.items() if (arm,block)==(a,b)],'late')
                for a in study['arms'] for b in study['blocks']}
    crossings = {v: {f: dict(Counter(r['native'][v][f]+'->'+r['crossed'][v][f] for r in cells))
                      for f in ('contact','at15','at30')} for v in INDICES}
    repeats = [(r[p][v],rows[a,2,k][p][v]) for (a,b,k),r in rows.items() if b == 1 for p in POSITIONS for v in INDICES]
    return dict(late=direction(cells,'late'), four=direction(cells,'four'), by_posture_load=by_start,
                positions={p: position_outcomes([r[p] for r in cells]) for p in POSITIONS},
                native_to_crossed=crossings, parent_agreement={v: agreement(pairs) for v,pairs in matched_parent.items()},
                reload_agreement={**agreement(repeats),'final_physics':sum(a['final_physics']==b['final_physics'] for a,b in repeats)})


def score(out):
    src, runtime = out/'sources', read(out/'runtime.json')
    assert read(src/DESIGN_FILE) == DESIGN == read(out/'design.json')
    assert all(sha(src/n) == h for n,h in runtime['sources'].items())
    assert digest(runtime['checkpoint']) == BASE['checkpoint_manifest_sha256']
    check_freeze(src)
    for study in STUDIES.values():
        assert read(src/study['task_design']) == TASK and sha(src/TASK['bddl']) == TASK['bddl_sha256']
        check_donors(src, study)
    entries = sessions()
    check_sessions(out, entries, STUDIES[2]['blocks'])
    a,b = (read(out/f'block-{i}.json') for i in (1,2))
    order = lambda e: (e['layout'],e['arm'],e['mode'],e['view'],e['key'])
    assert [order(e) for e in a] == [order(e) for e in reversed(b)]
    keys = read(out/'rng.json')
    assert digest(keys) == DESIGN['rng_sha256']
    qual, bank = checked_inputs(out)
    geometry = {i: contact_geometry(qual['geometry'][str(i)]) for i in STUDIES}
    preps = {(arm,m): tape_for(out,arm,m) for arm in LAYOUT for m in MODES}
    paths, seen, raster = {}, set(), Counter()
    for n,e in entries.items():
        arm, mode = e['arm'], e['mode']
        host, other = preps[arm,mode], preps[arm,alternate(mode)]
        geo = geometry[e['layout']]
        tape = read(out/'paths'/(n+'.json'))
        sent, exchanged = rendered_inputs(tape,e,host,other,geo,INDICES)
        values,_ = path_outcomes(out,e,host,geo,keys,seen,sent_by_tick=sent,tape=tape)
        info = behavior_record(values,tape,exchanged)
        info['first_20_sha256'] = digest(info.pop('controls'))
        paths[n] = {**info,'final_physics':tape['final_physics'],'assigned':INDICES[e['view']]}
        for q in tape['queries'][:LIMIT]:
            render = q['render']
            rejected = render.get('reference_retries',[])
            raster['initial_reference_retries'] += len(rejected)
            for record in [*rejected, render]:
                failures = record.get('mismatches',[])
                raster['unmatched_renders'] += len(failures)
                raster['native_reacquisitions'] += record.get('native_reacquisitions',0)
                for f in failures:
                    raster['max_pixels_one_camera'] = max(raster['max_pixels_one_camera'], *f['pixels'].values())
    summaries = {str(i): layout_summary(i,entries,paths) for i in STUDIES}
    expected = {'2':-1,'3':1}
    overall = all(summaries[i]['late']['crossed_minus_native']*sign > 0 for i,sign in expected.items())
    every = all(row['crossed_minus_native']*expected[i] > 0 for i,s in summaries.items() for row in s['by_posture_load'].values())
    return dict(figure_name=DESIGN['figure'], paths=len(paths), policy_queries=sum(e['queries'] for e in entries.values()),
                changed_camera_pixels=bank['changed_pixels'], physical_starts=qual['starts'], render_checks=LIMIT*len(paths),
                raster_retries=dict(raster), exchanged_queries=sum(len(r['exchanged']) for r in paths.values()),
                early_cutoffs=sum(r['exchanged'] != r['assigned'] for r in paths.values()),
                transfer_in_predicted_directions=overall, transfer_in_every_posture_load=every, layouts=summaries, paths_by_session=paths)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=('collect','prepare','prepare-start','check-first','verify','run','replay'),
                        nargs='?', default='verify')
    parser.add_argument('arguments', nargs='*')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    out = args.folder
    if args.stage in ('prepare-start', 'check-first'):
        arm, mode = args.arguments
        fn = prepare_start if args.stage == 'prepare-start' else check_first
        print(json.dumps(fn(out, arm, mode)))
    elif args.stage == 'prepare':
        prepare(out)
    elif args.stage == 'collect':
        collect(out)
    elif args.arguments:
        name, = args.arguments
        assert args.stage in ('run','replay')
        report = run_path(out, read(out/'sessions.json')[name], args.stage == 'replay')
        if report is not None:
            print(json.dumps(report))
    else:
        assert args.stage in ('verify','replay')
        with unpack(args.folder) as raw:
            result = score(raw)
            assert result == read(out/'verification.json')
            entries = sessions()
            if args.stage == 'replay':
                report = replay(raw, script=SCRIPT, entries=entries, workers=6)
                check_replayed_paths(raw, report, entries, {})
                if args.output:
                    if args.output.exists():
                        raise FileExistsError(args.output)
                    write_json(args.output, report)
                else:
                    print(json.dumps(report))
            elif (out/'physical_replay.json').is_file():
                report = read(out/'physical_replay.json')
                check_replayed_paths(raw, report, entries, {})
                if 'archive_repeat' in report:
                    check_archive_repeat(out, raw, report, entries)
            print(f"Verified {result['paths']} bowl-position paths and {result['policy_queries']} receipts", flush=True)


if __name__ == '__main__':
    main()
