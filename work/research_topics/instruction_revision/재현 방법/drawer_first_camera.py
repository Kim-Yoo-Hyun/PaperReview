"""Swap the initial external and wrist images across drawer widths at fixed physics."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
from zipfile import ZipFile

import numpy as np

from drawer_location import COHORT, destination
from drawer_width import alternate_modes, tape_for, validate_starts
from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_drawer import pixels
from verify_layouts import unpack
from verify_middle_aperture import (BASE, TASK, check_donors, check_sessions, contact_geometry,
                                    path_outcomes, planned)
from verify_stove import sha
from verify_stove_layouts import check_freeze, check_replayed_paths, digest, replay


DESIGN_FILE = 'drawer/drawer_first_camera.json'
DESIGN = read(PACKET / DESIGN_FILE)
MODES = DESIGN['physical_modes']
VIEWS = DESIGN['swapped_cameras']
SCRIPT = 'drawer_first_camera.py'


def sessions():
    conditions = [mode + '.' + view for view in VIEWS for mode in MODES]
    plan = planned(COHORT, modes=conditions)
    for entry in plan.values():
        entry['mode'], entry['view'] = entry['mode'].split('.')
    return plan


def assignments(bank, arm, mode, view):
    host = bank[arm][mode]
    donor = bank[arm][alternate_modes(mode)[0]]
    return {cam: (donor if cam in VIEWS[view] else host)[cam] for cam in CAMERAS}


def parent_inputs(out, *, install=False):
    archive = PACKET / DESIGN['parent']
    assert sha(archive) == DESIGN['parent_sha256']
    with ZipFile(archive) as z:
        def match(name):
            target = out / name
            data = z.read(name)
            if install:
                target.write_bytes(data)
            assert target.read_bytes() == data, name

        for name in ('clearance.json', 'qualification.json'):
            match(name)
        for name in z.namelist():
            if name.startswith('preparation/') and name.endswith('.json'):
                match(name)
        qual = read(out / 'qualification.json')
        assert qual['starts'] == validate_starts(out, qual)
        bank, changes = {}, {}
        for arm in COHORT['arms']:
            tapes = {m: tape_for(out, arm, m)['first'] for m in MODES}
            bank[arm] = {m: t['live'] for m, t in tapes.items()}
            changes[arm] = {}
            for m, t in tapes.items():
                assert t['physics'] == qual['starts'][arm][m]['physics']
                for h in t['live'].values():
                    match('frames/' + h + '.png')
            for drawer in ('middle', 'bottom'):
                a, b = (tapes[w + '-' + drawer] for w in ('narrow', 'full'))
                assert a['physics'] != b['physics'] and a['state'] == b['state']
                changes[arm][drawer] = {}
                for cam in CAMERAS:
                    left, right = (pixels(out, t['live'][cam]) for t in (a, b))
                    count = int(np.any(left != right, axis=2).sum())
                    assert count > 0
                    changes[arm][drawer][cam] = count
        return bank, changes


def collect(out):
    from run_atomic import SIM_PYTHON
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block

    archive = PACKET / DESIGN['parent']
    assert sha(archive) == DESIGN['parent_sha256']
    with ZipFile(archive) as z:
        sources = list(json.loads(z.read('runtime.json'))['sources'])
    os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
    initialize_study(out, DESIGN, [*sources, DESIGN_FILE, SCRIPT, 'run_atomic.py', 'verify_drawer.py'],
                     key_count=BASE['key_offset'] + TASK['extension'] // BASE['period'])
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.50'
    check_donors(out / 'sources', COHORT)
    bank, changes = parent_inputs(out, install=True)
    write_json(out / 'camera_inputs.json', dict(images=bank, changed_pixels=changes))
    entries = sessions()
    write_json(out / 'sessions.json', entries)
    print('Checked eight physical starts and sixteen initial camera images against the width study', flush=True)
    sim = [SIM_PYTHON, str(PACKET / SCRIPT), str(out)]
    for block in COHORT['blocks']:
        subset = [e for e in entries.values() if e['block'] == block]
        policy_block(out, sim, subset, f'block-{block}', f'policy-{block}.log', workers=5)
        print(f'Completed model load {block} with {len(subset)} paths', flush=True)
    write_json(out / 'verification.json', score(out))


def cell(records, keys, mode, view):
    other = alternate_modes(mode)[0]
    contact, destinations = Counter(), {tick: Counter() for tick in ('300', '600')}
    paired = {metric: Counter() for metric in ('first_contact', '300', '600')}
    delta_self, delta_donor = [], []
    reversals = opportunities = 0
    for key in keys:
        own, donor, test = (records[(*key, m, v)] for m, v in ((mode, 'self'), (other, 'self'), (mode, view)))
        contact[test['first_contact']] += 1
        for tick in destinations:
            destinations[tick][test[tick]] += 1
        for metric in paired:
            paired[metric][own[metric] + '->' + test[metric]] += 1
        differs = own['first_contact'] != donor['first_contact']
        opportunities += differs
        reversals += differs and test['first_contact'] == donor['first_contact']
        for values, control in ((delta_self, own), (delta_donor, donor)):
            values.append(max(abs(x - y) for x, y in zip(test['action'], control['action'], strict=True)))
    def distances(deltas):
        return dict(changed=sum(v > 0 for v in deltas), minimum=min(deltas), median=float(np.median(deltas)),
                    maximum=max(deltas))
    return dict(paths=len(keys), first_contact=dict(contact), destinations={k: dict(v) for k, v in destinations.items()},
                self_to_treatment={k: dict(v) for k, v in paired.items()}, different_self_contacts=opportunities,
                to_opposite_self_contact=reversals, first_action_delta_self=distances(delta_self),
                first_action_delta_opposite_self=distances(delta_donor))


def score(out):
    runtime = read(out / 'runtime.json')
    src = out / 'sources'
    assert read(src / DESIGN_FILE) == DESIGN == read(out / 'design.json')
    assert all(sha(src / n) == h for n, h in runtime['sources'].items())
    assert digest(runtime['checkpoint']) == BASE['checkpoint_manifest_sha256']
    assert read(src / COHORT['task_design']) == TASK and sha(src / TASK['bddl']) == TASK['bddl_sha256']
    check_freeze(src)
    check_donors(src, COHORT)
    entries = sessions()
    check_sessions(out, entries, COHORT['blocks'])
    keys = read(out / 'rng.json')
    assert digest(keys) == DESIGN['rng_sha256']
    bank, changes = parent_inputs(out)
    assert read(out / 'camera_inputs.json') == dict(images=bank, changed_pixels=changes)
    geometry = contact_geometry(read(out / 'qualification.json')['geometry'])
    preps = {(a, m): tape_for(out, a, m) for a in COHORT['arms'] for m in MODES}
    seen, records = set(), {}
    for name, e in entries.items():
        arm, mode, view = e['arm'], e['mode'], e['view']
        assigned = assignments(bank, arm, mode, view)
        outcomes, first = path_outcomes(out, e, preps[arm, mode], geometry, keys, seen, first_images=assigned)
        last = outcomes['600']
        records[arm, e['block'], e['key'], mode, view] = dict(
            first_contact=last['first_task_contact']['target'], contact_tick=last['first_task_contact']['tick'],
            action=first['reply'][0], chunk=digest(first['reply'][:BASE['period']]),
            **{t: destination(outcomes[t]) for t in ('300', '600')})
    cohort = [(a, b, k) for a in COHORT['arms'] for b in COHORT['blocks'] for k in BASE['stove_seeds']]
    assert len(records) == len(entries) == len(cohort) * len(MODES) * len(VIEWS)
    groups = {'all': cohort}
    for arm in COHORT['arms']:
        for block in COHORT['blocks']:
            groups[f'{arm}/b{block}'] = [k for k in cohort if k[:2] == (arm, block)]
    comparisons = {g: {m: {v: cell(records, group, m, v) for v in VIEWS} for m in MODES}
                   for g, group in groups.items()}
    repeats = [(r, records[a, 2, k, m, v]) for (a, b, k, m, v), r in records.items() if b == 1]
    agreement = {key: sum(a[key] == b[key] for a, b in repeats) for key in ('action', 'chunk', 'first_contact', '300', '600')}
    complementary = {'self': 'both', 'both': 'self', 'external': 'wrist', 'wrist': 'external'}
    same_input = {}
    for drawer in ('middle', 'bottom'):
        equal = Counter()
        for a, b, k in cohort:
            for v, inverse in complementary.items():
                m, other = 'narrow-' + drawer, 'full-' + drawer
                assert assignments(bank, a, m, v) == assignments(bank, a, other, inverse)
                one, two = records[a, b, k, m, v], records[a, b, k, other, inverse]
                equal['pairs'] += 1
                for metric in ('action', 'chunk', 'first_contact', '300', '600'):
                    equal[metric] += one[metric] == two[metric]
        same_input[drawer] = dict(equal)
    return dict(paths=len(entries), unique_posture_seed_pairs=len(cohort) // len(COHORT['blocks']),
                policy_queries=sum(e['queries'] for e in entries.values()), changed_camera_pixels=changes,
                comparisons=comparisons, complementary_inputs=same_input, reload_pairs=len(repeats),
                reload_agreement=agreement,
                paths_by_session={e['session']: records[e['arm'], e['block'], e['key'], e['mode'], e['view']]
                                  for e in entries.values()})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', nargs='?', default='verify', choices=('collect', 'verify', 'run', 'replay'))
    parser.add_argument('session', nargs='?')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.stage == 'collect':
        collect(args.folder)
    elif args.session:
        from drawer_location_sim import run
        assert args.stage in ('run', 'replay')
        entry = read(args.folder / 'sessions.json')[args.session]
        bank = read(args.folder / 'camera_inputs.json')['images']
        images = assignments(bank, entry['arm'], entry['mode'], entry['view'])
        result = run(args.folder, entry, replay=args.stage == 'replay', first_images=images)
        if result is not None:
            print(json.dumps(result))
    else:
        assert args.stage in ('verify', 'replay')
        with unpack(args.folder) as out:
            result = score(out)
            assert result == read(args.folder / 'verification.json')
            entries = sessions()
            if args.stage == 'replay':
                proof = replay(out, script=SCRIPT, entries=entries, workers=6)
                check_replayed_paths(out, proof, entries, {})
                if args.output:
                    if args.output.exists():
                        raise FileExistsError(args.output)
                    write_json(args.output, proof)
                else:
                    print(json.dumps(proof))
            elif (args.folder / 'physical_replay.json').is_file():
                proof = read(args.folder / 'physical_replay.json')
                check_replayed_paths(out, proof, entries, {})
                if 'archive_repeat' in proof:
                    from verify_middle_aperture import check_archive_repeat
                    check_archive_repeat(args.folder, out, proof, entries)
            print(f"Verified {result['paths']} first-camera paths and {result['policy_queries']} policy receipts", flush=True)


if __name__ == '__main__':
    main()
