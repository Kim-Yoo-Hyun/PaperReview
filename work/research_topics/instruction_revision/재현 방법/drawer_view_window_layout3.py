"""Rebuild, qualify and evaluate the same camera windows on the second layout."""
from collections import Counter
from functools import partial
import json
from zipfile import ZipFile

import numpy as np

from drawer_width import CLOSED, tape_for
from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_drawer import pixels
from verify_middle_aperture import BASE, LEVELS, ORIGINAL, check_donors, stationary
from verify_stove import sha
from verify_stove_fingers import DESIGN as FINGERS, source_donors
from verify_stove_layouts import digest


DESIGN_FILE = 'drawer/drawer_view_window_layout3.json'
DESIGN = read(PACKET / DESIGN_FILE)
MODES = DESIGN['physical_modes']
OBJECTS = ('akita_black_bowl_1_main', 'plate_1_main')


def local_cohort(out):
    return {**ORIGINAL, 'donors': (out / 'sources' / ORIGINAL['donors']).resolve()}


def candidates():
    archive = PACKET / DESIGN['parent']
    assert sha(archive) == DESIGN['parent_sha256']
    with ZipFile(archive) as z:
        prior = json.loads(z.read('clearance.json'))['arrangements']
    assert prior['full']['width_m'] is None and prior['narrow']['width_m'] == .076
    shift = prior['full']['shift_xy_m']
    assert shift == prior['narrow']['shift_xy_m'] and set(shift) == set(OBJECTS)
    return {'native': {n: [0., 0.] for n in OBJECTS}, 'layout2': shift}


def reference_observation(env, out, keep, prompt):
    from drawer_sim import observe
    frames = [observe(env, out, True, prompt)[1] for _ in range(9)]
    assert all((f['state'], f['physics']) == (frames[0]['state'], frames[0]['physics']) for f in frames)
    samples = [tuple(f['live'][c] for c in CAMERAS) for f in frames]
    pair, count = Counter(samples).most_common(1)[0]
    assert count > len(samples) // 2
    first = dict(frames[samples.index(pair)], reference_samples=samples)
    return None, first


def prepare(out):
    import mujoco
    from drawer_location_clearance import Probe
    from drawer_location_sim import LocationCabinet, branch
    from middle_aperture_sim import environment, record_branches

    study = local_cohort(out)
    write_json(study['donors'], source_donors(PACKET / FINGERS['parent']))
    check_donors(out / 'sources', ORIGINAL)
    shifts = candidates()
    tested, widths = {label: {} for label in shifts}, {}
    for arm in study['arms']:
        env = environment(arm, layout=study['layout'])
        try:
            probe = Probe(env, arm, out, cohort=study)
            widths[arm] = probe.width
            for label, shift in shifts.items():
                tested[label][arm] = {}
                for mode in [CLOSED, *MODES]:
                    width, level = mode.split('-')
                    travel = probe.width if width == 'full' else .076
                    tested[label][arm][mode] = probe.sample(level, travel, shift)
        finally:
            env.close()
    chosen = next(label for label in shifts if all(row['clear'] for modes in tested[label].values() for row in modes.values()))
    arrangements = {w: dict(width_m=width, shift_xy_m=shifts[chosen]) for w, width in [('full', None), ('narrow', .076)]}
    write_json(out / 'clearance.json', dict(arrangements=arrangements, candidates=tested, selected=chosen, widths=widths))
    geometry, renderer = record_branches(out, study, [CLOSED, *MODES], scene_type=LocationCabinet,
                                         prepare_fn=partial(branch, corrections=arrangements), first_observe=reference_observation)
    qual = dict(geometry=geometry, renderer=renderer, mujoco=mujoco.__version__)
    write_json(out / 'qualification.json', dict(qual, starts=validate_starts(out, qual)))
    bank, changes = camera_bank(out)
    write_json(out / 'camera_inputs.json', dict(images=bank, changed_pixels=changes))
    print(f'Qualified both layout-3 returns with {chosen} tabletop, widths {widths}', flush=True)


def validate_starts(out, qual):
    clearance = read(out / 'clearance.json')
    shifts, tested = candidates(), clearance['candidates']
    chosen = next(label for label in shifts if all(row['clear'] for cases in tested[label].values() for row in cases.values()))
    assert chosen == clearance['selected'] and 'NVIDIA' in qual['renderer']
    shift = shifts[chosen]
    assert clearance['arrangements'] == {k: dict(width_m=w, shift_xy_m=shift) for k, w in [('full', None), ('narrow', .076)]}
    geometry, starts = qual['geometry'], {}
    for arm, donor in zip(ORIGINAL['arms'], ORIGINAL['donor_physics'], strict=True):
        ref = tape_for(out, arm, CLOSED)
        before, closed = (ref['branch'][k] for k in ('before', 'after'))
        assert ref['donor_physics'] == donor and digest(before) == ORIGINAL['returned_physics'][arm]
        slides = geometry['slides']
        width = slides['middle']['closed'] - before['integration_state'][1 + slides['middle']['qpos']]
        assert width == clearance['widths'][arm] and .159 <= width <= .160
        expected = before['integration_state'].copy()
        for slide in slides.values():
            expected[1 + slide['qpos']] = slide['closed']
            expected[1 + geometry['nq'] + slide['qvel']] = 0.
        for obj, pos in geometry['object_free_qpos'].items():
            for axis, delta in enumerate(shift[obj]):
                expected[1 + pos + axis] += delta
        assert closed == dict(before, integration_state=expected)
        starts[arm] = {}
        for mode in [CLOSED, *MODES]:
            tape = tape_for(out, arm, mode)
            assert (tape['arm'], tape['mode'], tape['length']) == (arm, mode, BASE['lead'])
            assert all(tape[k] == ref[k] for k in ('common', 'start', 'actions', 'rows', 'donor_physics'))
            assert len(tape['actions']) == len(tape['rows']) == BASE['lead']
            branch, hand = tape['branch'], tape['handoff']
            assert branch['before'] == before and branch['shift_xy_m'] == shift
            assert not hand['robot_contacts'] and not branch['slide_contacts']
            assert all(hand[k] == ref['handoff'][k] for k in ('tool', 'objects'))
            assert tape['first']['state'] == ref['first']['state']
            reference = tape['first']
            pairs = [tuple(pair) for pair in reference['reference_samples']]
            modal = tuple(reference['live'][cam] for cam in CAMERAS)
            assert len(pairs) == 9 and pairs.count(modal) > len(pairs)//2
            for pair in set(pairs):
                for h in pair:
                    pixels(out, h)
            aperture, level = mode.split('-')
            travel = width if aperture == 'full' else .076
            assert branch['displacement_m'] == -travel
            state = closed['integration_state'].copy()
            if level != 'closed':
                state[1 + slides[level]['qpos']] -= travel
            assert branch['after'] == dict(closed, integration_state=state)
            assert tape['first']['physics'] == digest(branch['after'])
            for i, drawer in enumerate(LEVELS):
                q = ref['handoff']['upper']['joints'][i] - (travel if drawer == level else 0.)
                assert hand['upper']['joints'][i] == q and hand['upper'][drawer + '_open'] == (q < geometry['open_below_m'])
            assert not any(hand['upper'][k] for k in ('bowl_in', 'middle_in', 'bottom_in'))
            contact = tested[chosen][arm][mode]
            assert contact['clear'] and not contact['contacts'] and set(contact['supported']) == set(OBJECTS)
            hold = stationary(tape)['maximum']
            assert hold['drawer_mm'] <= 1.
            starts[arm][mode] = dict(physics=tape['first']['physics'], opening_m=0. if level == 'closed' else travel,
                                     max_stationary_drawer_mm=hold['drawer_mm'], max_stationary_object_mm=hold['object_mm'])
    return starts


def camera_bank(out):
    bank, changes = {}, {}
    for arm in ORIGINAL['arms']:
        bank[arm] = {m: tape_for(out, arm, m)['first']['live'] for m in MODES}
        changes[arm] = {}
        for level in ('middle', 'bottom'):
            changes[arm][level] = {}
            for cam in CAMERAS:
                a, b = (pixels(out, bank[arm][w + '-' + level][cam]) for w in ('narrow', 'full'))
                count = int(np.any(a != b, axis=2).sum())
                assert count > 0
                changes[arm][level][cam] = count
    return bank, changes


def inputs(out):
    qual = read(out / 'qualification.json')
    assert qual['starts'] == validate_starts(out, qual)
    bank, changes = camera_bank(out)
    assert read(out / 'camera_inputs.json') == dict(images=bank, changed_pixels=changes)
    return bank, changes


def layout_outcomes(paths, entries):
    groups = {}
    for view in DESIGN['exchange_indices']:
        rows = [paths[n] for n, e in entries.items() if e['view'] == view]
        times = [r['place_tick'] for r in rows if r['place_tick'] is not None]
        groups[view] = {k: dict(Counter(r[k] for r in rows)) for k in ('contact', 'first_destination', 'at15', 'at30')}
        groups[view]['first_placement'] = dict(observed=len(times), missing=len(rows)-len(times),
            median_s=float(np.median(times))/20 if times else None, range_s=[min(times)/20, max(times)/20] if times else [])
    return groups


def compare_layouts(records, tables, entries):
    from drawer_view_duration import sessions
    archive = PACKET / DESIGN['parent']
    reference = archive.with_name('verification.json')
    assert sha(reference) == DESIGN['parent_verification_sha256']
    ref = read(reference)
    with ZipFile(archive) as z:
        plan = json.loads(z.read('sessions.json'))
    assert plan == sessions(DESIGN['exchange_indices'])
    result = {}
    for layout, paths, comparisons, plan in ((2, ref['paths_by_session'], ref['comparisons'], plan),
                                              (3, records, tables, entries)):
        rows = {}
        for mode in MODES:
            row = comparisons['all'][mode]
            cells = [t[mode] for name, t in comparisons.items() if name != 'all']
            rows[mode] = dict(pairs=row['self_to_early']['pairs'], alignment=row['alignment'],
                contact_changes={k: row[k]['contact']['changed'] for k in ('self_to_early', 'self_to_late', 'early_to_late')},
                late_exceeds_early_in_every_cell=all(c['self_to_late']['contact']['changed'] > c['self_to_early']['contact']['changed'] for c in cells))
        result[str(layout)] = dict(by_mode=rows, by_schedule=layout_outcomes(paths, plan))
    return result


if __name__ == '__main__':
    from drawer_view_duration import main
    main(DESIGN_FILE, 'drawer_view_window_layout3.py')
