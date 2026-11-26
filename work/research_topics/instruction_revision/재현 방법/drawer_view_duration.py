"""Vary how long both policy cameras show a different physical drawer opening."""
import argparse
from collections import Counter
from functools import partial
from itertools import combinations
import json
import os
from pathlib import Path
from zipfile import ZipFile

import numpy as np

from drawer_first_camera import parent_inputs
from drawer_location import COHORT, destination
from drawer_width import alternate_modes, tape_for
from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import (BASE, TASK, LEVELS, check_archive_repeat, check_donors, check_sessions,
                                    contact_geometry, path_outcomes, planned, targets)
from verify_stove import sha
from verify_stove_layouts import check_freeze, check_replayed_paths, digest, replay


DESIGN_FILE = 'drawer/drawer_view_duration.json'
DESIGN = read(PACKET / DESIGN_FILE)
MODES, VIEWS = DESIGN['physical_modes'], DESIGN['opposite_queries']
LIMIT, PERIOD = DESIGN['render_queries'], BASE['period']
SCRIPT = 'drawer_view_duration.py'
DEFAULT_INDICES = {view: list(range(count)) for view, count in VIEWS.items()}


def sessions(indices=DEFAULT_INDICES):
    entries = planned(COHORT, modes=[m + '.' + v for v in indices for m in MODES])
    for e in entries.values():
        e['mode'], e['view'] = e['mode'].split('.')
    return entries


def inputs(out, design=DESIGN, *, install=False):
    archive = PACKET / design['parent']
    assert sha(archive) == design['parent_sha256']
    bank, changes = parent_inputs(out, install=install)
    with ZipFile(archive) as z:
        data = z.read('camera_inputs.json')
        assert json.loads(data) == dict(images=bank, changed_pixels=changes)
        if 'exchange_indices' in design:
            for name in ('clearance.json', 'qualification.json', *[n for n in z.namelist() if n.startswith('preparation/')]):
                assert z.read(name) == (out / name).read_bytes()
        if install:
            (out / 'camera_inputs.json').write_bytes(data)
        assert (out / 'camera_inputs.json').read_bytes() == data
        return bank, changes


def collect(out, design_file=DESIGN_FILE, script=SCRIPT):
    from run_atomic import SIM_PYTHON
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block

    design = read(PACKET / design_file)
    assert design['physical_modes'] == MODES and design['render_queries'] == LIMIT
    with ZipFile(PACKET / design['parent']) as z:
        sources = list(json.loads(z.read('runtime.json'))['sources'])
    os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
    figure_script = 'plot_' + design.get('figure', 'drawer_view_duration.png').replace('.png', '.py')
    initialize_study(out, design, [*sources, design_file, script, SCRIPT, 'drawer_view_render.py',
                                   figure_script, 'plot_drawer_location.py'],
                     key_count=BASE['key_offset'] + TASK['extension'] // PERIOD)
    check_donors(out / 'sources', COHORT)
    inputs(out, design, install=True)
    entries = sessions(design.get('exchange_indices', DEFAULT_INDICES))
    write_json(out / 'sessions.json', entries)
    sim = [SIM_PYTHON, str(PACKET / script), str(out)]
    for block in COHORT['blocks']:
        subset = [e for e in entries.values() if e['block'] == block]
        policy_block(out, sim, subset, f'block-{block}', f'policy-{block}.log', workers=5)
        print(f'Completed model load {block} with {len(subset)} paths', flush=True)
    write_json(out / 'verification.json', score(out, design_file))


def run_path(out, e, replaying, indices=DEFAULT_INDICES):
    from drawer_location_sim import run
    from drawer_view_render import ViewSchedule

    arm, mode = e['arm'], e['mode']
    drawer = mode.split('-')[1]
    other = alternate_modes(mode)[0]
    qual = read(out / 'qualification.json')['starts'][arm]
    bank = read(out / 'camera_inputs.json')['images'][arm]
    configure = partial(ViewSchedule, drawer=drawer, width=qual[other]['opening_m'], indices=indices[e['view']],
                        limit=LIMIT, bank=bank[mode], opposite_bank=bank[other])
    return run(out, e, replay=replaying, view_factory=configure)


def rendered_inputs(tape, e, prep, other, geometry, indices=DEFAULT_INDICES):
    drawer = e['mode'].split('-')[1]
    pos = LEVELS.index(drawer)
    handoff = prep['handoff']['upper']
    assert not (set(targets(handoff, geometry)) - {'other'})
    rows = [handoff, *tape['rows']]
    sent, exchanged = {}, []
    for i, q in enumerate(tape['queries']):
        if i >= LIMIT:
            assert 'render' not in q and 'sent' not in q
            continue
        r = q['render']
        attempts = r.get('mismatches', [])
        reacquired = r.get('native_reacquisitions', 0)
        assert 0 <= reacquired <= 2 and 4*reacquired <= len(attempts) < 4*(reacquired+1)
        for j, attempt in enumerate(attempts):
            assert attempt['observation'] == j//4 and any(attempt['pixels'].values())
            assert all((attempt['pixels'][c] > 0) == (attempt['native'][c] != attempt['detached'][c]) for c in CAMERAS)
            if attempt['observation'] == reacquired:
                assert attempt['native'] == q['live']
        stopped = any(set(targets(row, geometry)) - {'other'} for row in rows[:i * PERIOD + 1])
        active = i in indices[e['view']] and not stopped
        assert r['exchange'] == active
        assert r['host_after'] == q['physics'] and r['self_rgb'] == q['live']
        assert r['host_qpos'] == rows[i * PERIOD]['joints'][pos]
        assert r['render_qpos'] == (other['handoff']['upper']['joints'][pos] if active else r['host_qpos'])
        assert set(r['sent']) == set(r['changed_pixels']) == set(CAMERAS)
        for c in CAMERAS:
            assert 0 <= r['changed_pixels'][c] <= 224**2
            assert (r['changed_pixels'][c] > 0) == (r['sent'][c] != q['live'][c])
        if active:
            exchanged.append(i)
        else:
            assert r['sent'] == q['live']
        if i == 0:
            assert q['live'] == prep['first']['live'] and r['sent'] == (other if active else prep)['first']['live']
        sent[q['tick']] = r['sent']
    return sent, exchanged


def numbers(values):
    if not values:
        return dict(n=0)
    return dict(n=len(values), min=min(values), median=float(np.median(values)), max=max(values))


def summarize(pairs):
    info = {}
    for field in ('contact', 'first_destination', 'at15', 'at30'):
        trans = Counter((a[field], b[field]) for a, b in pairs)
        info[field] = dict(changed=sum(n for (x, y), n in trans.items() if x != y),
                           transitions={x + '->' + y: n for (x, y), n in trans.items()})
    for field in ('contact_tick', 'place_tick'):
        both = [(a[field], b[field]) for a, b in pairs if a[field] is not None and b[field] is not None]
        delta = [y - x for x, y in both]
        info[field] = dict(delta=numbers(delta), earlier=sum(d < 0 for d in delta), later=sum(d > 0 for d in delta),
                           only_reference=sum(a[field] is not None and b[field] is None for a, b in pairs),
                           only_test=sum(a[field] is None and b[field] is not None for a, b in pairs))
    diffs = np.abs(np.asarray([b['controls'] for _, b in pairs]) - np.asarray([a['controls'] for a, _ in pairs]))
    chunks = diffs.reshape(len(pairs), LIMIT, PERIOD, 7).max(axis=(2, 3))
    info['controls'] = dict(per_control_changed=(diffs.max(axis=2) > 0).sum(axis=0).tolist(),
                            chunks=[dict(changed=int(np.sum(v > 0)), max_abs_delta=numbers(v.tolist())) for v in chunks.T])
    return dict(pairs=len(pairs), **info)


def alignment(records, cohort, mode):
    classifications = {'early': Counter(), 'late': Counter()}
    joint = Counter()
    for k in cohort:
        own, four = (records[(*k, mode, v)]['contact'] for v in ('self', 'four'))
        if own == four:
            continue
        labels = []
        for v in classifications:
            observed = records[(*k, mode, v)]['contact']
            label = 'self' if observed == own else 'four' if observed == four else 'neither'
            classifications[v][label] += 1
            labels.append(label)
        joint['->'.join(labels)] += 1
    return dict(eligible=sum(joint.values()), joint=dict(joint),
                **{v: {k: cnt[k] for k in ('self', 'four', 'neither')} for v, cnt in classifications.items()})


def comparisons(records, cohort, indices=DEFAULT_INDICES):
    results = {}
    for mode in MODES:
        other = alternate_modes(mode)[0]
        result = {}
        for a, b in combinations(indices, 2):
            pairs = [(records[(*k, mode, a)], records[(*k, mode, b)]) for k in cohort]
            result[a + '_to_' + b] = summarize(pairs)
        if 'early' in indices:
            results[mode] = dict(result, alignment=alignment(records, cohort, mode))
            continue
        opportunities = reversals = 0
        for k in cohort:
            own, one, four, donor = (records[(*k, m, v)]['contact'] for m, v in
                                     ((mode, 'self'), (mode, 'one'), (mode, 'four'), (other, 'self')))
            eligible = own != donor and own == one
            opportunities += eligible
            reversals += eligible and four == donor
        results[mode] = dict(result, eligible=opportunities, reversals=reversals)
    return results


def score(out, design_file=DESIGN_FILE):
    src, runtime = out / 'sources', read(out / 'runtime.json')
    design = read(PACKET / design_file)
    assert read(src / design_file) == design == read(out / 'design.json')
    assert design['physical_modes'] == MODES and design['render_queries'] == LIMIT
    indices = design.get('exchange_indices', DEFAULT_INDICES)
    assert all(sorted(set(window)) == window and all(i in range(LIMIT) for i in window) for window in indices.values())
    assert all(sha(src / n) == h for n, h in runtime['sources'].items())
    assert digest(runtime['checkpoint']) == BASE['checkpoint_manifest_sha256']
    assert read(src / COHORT['task_design']) == TASK and sha(src / TASK['bddl']) == TASK['bddl_sha256']
    check_freeze(src)
    check_donors(src, COHORT)
    entries = sessions(indices)
    check_sessions(out, entries, COHORT['blocks'])
    keys = read(out / 'rng.json')
    assert digest(keys) == design['rng_sha256']
    _, changes = inputs(out, design)
    geometry = contact_geometry(read(out / 'qualification.json')['geometry'])
    preps = {(a, m): tape_for(out, a, m) for a in COHORT['arms'] for m in MODES}
    records, seen = {}, set()
    raster = Counter()
    for name, e in entries.items():
        arm, mode, view = e['arm'], e['mode'], e['view']
        prep, other = (preps[arm, m] for m in (mode, alternate_modes(mode)[0]))
        tape = read(out / 'paths' / (name + '.json'))
        sent, exchanged = rendered_inputs(tape, e, prep, other, geometry, indices)
        for q in tape['queries'][:LIMIT]:
            r = q['render']
            attempts = r.get('mismatches', [])
            raster['queries_with_retries'] += bool(attempts)
            raster['nonmatching_renders'] += len(attempts)
            raster['native_reacquisitions'] += r.get('native_reacquisitions', 0)
            for a in attempts:
                raster['max_pixels_one_camera'] = max(raster['max_pixels_one_camera'], *a['pixels'].values())
        vals, _ = path_outcomes(out, e, prep, geometry, keys, seen, sent_by_tick=sent, tape=tape)
        last = vals['600']
        firsts = {l: last['first'][f] for l, f in zip(LEVELS, ('bowl_in', 'middle_in', 'bottom_in'), strict=True)}
        tick = min((t for t in firsts.values() if t is not None), default=None)
        first = '+'.join(l for l, t in firsts.items() if tick is not None and t == tick) or 'none'
        records[arm, e['block'], e['key'], mode, view] = dict(
            contact=last['first_task_contact']['target'], contact_tick=last['first_task_contact']['tick'],
            per_drawer_first_tick=firsts, place_tick=tick, first_destination=first, exchanged=exchanged,
            at15=destination(vals['300']), at30=destination(last),
            controls=[r['action'] for r in tape['rows'][:LIMIT * PERIOD]])
    cohort = [(a, b, k) for a in COHORT['arms'] for b in COHORT['blocks'] for k in BASE['stove_seeds']]
    groups = {'all': cohort}
    for a in COHORT['arms']:
        for b in COHORT['blocks']:
            groups[f'{a}/b{b}'] = [k for k in cohort if k[:2] == (a, b)]
    tables = {g: comparisons(records, group, indices) for g, group in groups.items()}
    repeats = [(r, records[a, 2, k, m, v]) for (a, b, k, m, v), r in records.items() if b == 1]
    agreement = {field: sum(a[field] == b[field] for a, b in repeats)
                 for field in ('controls', 'contact', 'contact_tick', 'first_destination', 'place_tick', 'at15', 'at30')}
    by_session = {}
    for name, e in entries.items():
        r = records[e['arm'], e['block'], e['key'], e['mode'], e['view']].copy()
        r['first_20_sha256'] = digest(r.pop('controls'))
        if 'early' in indices:
            r['assigned'] = indices[e['view']]
        by_session[name] = r
    extra = {}
    if 'early' in indices:
        for m in MODES:
            cells = [t[m]['alignment'] for g, t in tables.items() if g != 'all']
            winners = [v for v, other in (('early', 'late'), ('late', 'early'))
                       if all(c['eligible'] and c[v]['four'] > c[other]['four'] for c in cells)]
            extra.setdefault('more_full_matches_in_every_cell', {})[m] = next(iter(winners), None)
        ref_file = (PACKET / design['parent']).with_name('verification.json')
        assert sha(ref_file) == design['parent_verification_sha256']
        reference = read(ref_file)['paths_by_session']
        extra['prior_reference_agreement'] = {}
        for v in ('self', 'four'):
            pairs = [(r, reference[n]) for n, r in by_session.items() if entries[n]['view'] == v]
            extra['prior_reference_agreement'][v] = dict(pairs=len(pairs), **{
                f: sum(x[f] == y[f] for x, y in pairs) for f in ('contact', 'contact_tick', 'first_destination',
                                                                 'place_tick', 'at15', 'at30', 'first_20_sha256')})
    else:
        extra['consistent_contact_reversal'] = {m: all(2*t[m]['reversals'] > len(groups[g])
            for g, t in tables.items() if g != 'all') for m in MODES}
    return dict(figure_name=design.get('figure', 'drawer_view_duration.png'), paths=len(entries),
                policy_queries=sum(e['queries'] for e in entries.values()),
                changed_camera_pixels=changes, render_checks=len(entries)*LIMIT, raster_retries=dict(raster),
                exchanged_queries=sum(len(r['exchanged']) for r in by_session.values()),
                early_cutoffs=sum(len(r['exchanged']) < len(indices[entries[n]['view']]) for n, r in by_session.items()),
                comparisons=tables, **extra,
                reload_pairs=len(repeats), reload_agreement=agreement, paths_by_session=by_session)


def main(design_file=DESIGN_FILE, script=SCRIPT):
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=('collect', 'verify', 'run', 'replay'), nargs='?', default='verify')
    parser.add_argument('session', nargs='?')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    design = read(PACKET / design_file)
    indices = design.get('exchange_indices', DEFAULT_INDICES)
    if args.session:
        assert args.stage in ('run', 'replay')
        report = run_path(args.folder, read(args.folder / 'sessions.json')[args.session], args.stage == 'replay', indices)
        if report is not None:
            print(json.dumps(report))
    elif args.stage == 'collect':
        collect(args.folder, design_file, script)
    else:
        assert args.stage in ('verify', 'replay')
        with unpack(args.folder) as out:
            result = score(out, design_file)
            assert result == read(args.folder / 'verification.json')
            entries = sessions(indices)
            if args.stage == 'replay':
                report = replay(out, script=script, entries=entries, workers=6)
                check_replayed_paths(out, report, entries, {})
                if args.output:
                    if args.output.exists():
                        raise FileExistsError(args.output)
                    write_json(args.output, report)
                else:
                    print(json.dumps(report))
            elif (args.folder / 'physical_replay.json').is_file():
                report = read(args.folder / 'physical_replay.json')
                check_replayed_paths(out, report, entries, {})
                if 'archive_repeat' in report:
                    check_archive_repeat(args.folder, out, report, entries)
            print(f"Verified {result['paths']} {Path(script).stem} paths and {result['policy_queries']} policy receipts", flush=True)


if __name__ == '__main__':
    main()
