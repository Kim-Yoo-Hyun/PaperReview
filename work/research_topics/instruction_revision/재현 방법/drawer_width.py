"""Collect and verify paired drawer-width interventions on one fixed tabletop."""
import argparse
from collections import Counter
from functools import lru_cache
import json
import os
from pathlib import Path
import subprocess
from zipfile import ZipFile

from drawer_location import COHORT, FLAGS, TIMES, cohorts, destination
from inside import write_json
from replay_middle_aperture import CONTACTS, read_trace
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import (BASE, LAYOUT2_FILE, LEVELS, TASK, check_archive_repeat, check_donors, check_sessions,
                                    contact_geometry, outcome, path_outcomes, planned, stationary, summary)
from verify_stove import sha
from verify_stove_layouts import check_freeze, check_replayed_paths, digest, replay


DESIGN_FILE = 'drawer/drawer_width.json'
DESIGN = read(PACKET / DESIGN_FILE)
CONDITIONS = DESIGN['conditions']
CLOSED = 'full-closed'
SIM = 'drawer_width_sim.py'


@lru_cache(maxsize=1)
def parent():
    archive = PACKET / DESIGN['parent']
    assert sha(archive) == DESIGN['parent_sha256']
    with ZipFile(archive) as z:
        full = json.loads(z.read('clearance.json'))['arrangements']['full']
        starts = json.loads(z.read('qualification.json'))['starts']['full']
    assert full['width_m'] is None and set(full['shift_xy_m']) == {'akita_black_bowl_1_main', 'plate_1_main'}
    return full, starts


def fixed_arrangements():
    full, _ = parent()
    return {'full': full, 'narrow': {**full, 'width_m': DESIGN['short_width_m']}}


def alternate_modes(source):
    if source == CLOSED:
        return [mode for mode in CONDITIONS if mode != CLOSED]
    width, drawer = source.split('-')
    return [('full' if width == 'narrow' else 'narrow') + '-' + drawer]


def tape_for(out, arm, mode):
    return read(out / 'preparation' / f"{arm}-{mode}-{BASE['lead']}.json")


def validate_starts(out, qual):
    geometry = qual['geometry']
    full, old = parent()
    assert DESIGN['layout'] == COHORT['layout'] and 'NVIDIA' in qual['renderer']
    assert read(out / 'clearance.json')['arrangements'] == fixed_arrangements()
    starts = {}
    for arm in COHORT['arms']:
        ref = tape_for(out, arm, CLOSED)
        after = ref['branch']['after']
        assert ref['first']['physics'] == digest(after) == old[arm]['handoffs']['closed']
        assert digest(ref['branch']['before']) == COHORT['returned_physics'][arm]
        starts[arm] = {}
        for mode in CONDITIONS:
            width, drawer = mode.split('-')
            tape = tape_for(out, arm, mode)
            change, end = tape['branch'], tape['handoff']
            assert (tape['arm'], tape['mode'], tape['length']) == (arm, mode, BASE['lead'])
            assert all(tape[k] == ref[k] for k in ('common', 'start', 'rows', 'actions', 'donor_physics'))
            assert change['before'] == ref['branch']['before'] and change['shift_xy_m'] == full['shift_xy_m']
            assert end['tool'] == ref['handoff']['tool'] and end['objects'] == ref['handoff']['objects']
            assert not end['robot_contacts'] and not change['slide_contacts']
            assert tape['first']['state'] == ref['first']['state']
            expected = list(after['integration_state'])
            travel = old[arm]['opening_m'] if width == 'full' else DESIGN['short_width_m']
            assert change['displacement_m'] == -travel
            if drawer != 'closed':
                expected[1 + geometry['slides'][drawer]['qpos']] -= travel
            assert change['after'] == dict(after, integration_state=expected)
            state_hash = digest(change['after'])
            assert tape['first']['physics'] == state_hash
            if width == 'full':
                assert state_hash == old[arm]['handoffs'][drawer]
            for i, level in enumerate(LEVELS):
                aperture = -travel if level == drawer else 0.
                assert end['upper']['joints'][i] == ref['handoff']['upper']['joints'][i] + aperture
                assert end['upper'][level + '_open'] == (aperture < geometry['open_below_m'])
            clearance = qual['clearance'][arm][mode]
            assert clearance['clear'] and not clearance['contacts']
            assert set(clearance['supported']) == set(full['shift_xy_m'])
            hold = stationary(tape)['maximum']
            assert hold['drawer_mm'] <= 1.
            starts[arm][mode] = dict(physics=state_hash, opening_m=0. if drawer == 'closed' else travel,
                                      max_stationary_drawer_mm=hold['drawer_mm'], max_stationary_object_mm=hold['object_mm'])
    return starts


def collect(out):
    from run_atomic import SIM_PYTHON
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block

    sources = [DESIGN_FILE, 'drawer_width.py', SIM, 'drawer_location.py', 'drawer_location_sim.py',
               'drawer_location_clearance.py', 'drawer/drawer_location.json', LAYOUT2_FILE, 'drawer/middle_aperture.json',
               COHORT['task_design'], TASK['bddl'], COHORT['donor_design'], COHORT['donors'], 'verify_middle_aperture.py',
               'middle_aperture_sim.py', 'replay_middle_aperture.py', 'stove_finger_sim.py', 'verify_stove_fingers.py',
               'upper_bowl_sim.py', 'verify_upper_bowl.py', 'verify_atomic.py', 'verify_layouts.py']
    # Grow the GPU allocation on demand on shared local devices, including during RNG setup.
    os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
    initialize_study(out, DESIGN, sources, key_count=BASE['key_offset'] + TASK['extension'] // BASE['period'])
    os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = os.environ.get('DRAWER_XLA_FRACTION', '0.40')
    check_donors(out / 'sources', COHORT)
    entries = planned(COHORT, modes=CONDITIONS)
    write_json(out / 'sessions.json', entries)
    sim = [SIM_PYTHON, str(PACKET / SIM), str(out)]
    subprocess.run([*sim, 'prepare'], check=True)
    for block in COHORT['blocks']:
        subset = [e for e in entries.values() if e['block'] == block]
        policy_block(out, sim, subset, f'block-{block}', f'policy-{block}.log', workers=3)
        print(f'Completed model load {block}, {len(subset)} native paths', flush=True)
    write_json(out / 'verification.json', score(out))


def native_summary(entries, outcomes, tick):
    by_mode = {mode: summary([outcomes[e['session']][tick] for e in entries if e['mode'] == mode])
               for mode in CONDITIONS}
    pairs = {}
    for e in entries:
        pairs.setdefault((e['arm'], e['block'], e['key']), {})[e['mode']] = outcomes[e['session']][tick]
    transitions = {level: Counter() for level in ('middle', 'bottom')}
    switches = Counter()
    for cases in pairs.values():
        assert set(cases) == set(CONDITIONS)
        follows = {w: cases[w+'-middle']['middle_in'] and cases[w+'-bottom']['bottom_in'] for w in ('narrow', 'full')}
        switches['both' if all(follows.values()) else 'narrow_only' if follows['narrow'] else
                 'full_only' if follows['full'] else 'neither'] += 1
        for level, counts in transitions.items():
            counts[destination(cases['narrow-'+level]) + '->' + destination(cases['full-'+level])] += 1
    return dict(by_mode=by_mode, paired_switches=dict(switches), pairs=len(pairs),
                narrow_to_full_destinations={level: dict(values) for level, values in transitions.items()})


def score(out):
    src = out / 'sources'
    runtime = read(out / 'runtime.json')
    assert read(src / DESIGN_FILE) == DESIGN == read(out / 'design.json')
    assert all(sha(src / name) == h for name, h in runtime['sources'].items())
    assert digest(runtime['checkpoint']) == BASE['checkpoint_manifest_sha256']
    assert read(src / COHORT['task_design']) == TASK and sha(src / TASK['bddl']) == TASK['bddl_sha256']
    check_freeze(src)
    check_donors(src, COHORT)
    entries = planned(COHORT, modes=CONDITIONS)
    check_sessions(out, entries, COHORT['blocks'])
    assert set(entries) == {p.stem for p in (out / 'paths').glob('*.json')}
    keys = read(out / 'rng.json')
    assert digest(keys) == DESIGN['rng_sha256']
    qual = read(out / 'qualification.json')
    starts = validate_starts(out, qual)
    assert starts == qual['starts']
    geometry = contact_geometry(qual['geometry'])
    preps = {(arm, mode): tape_for(out, arm, mode) for arm in COHORT['arms'] for mode in CONDITIONS}
    outcomes, firsts, trajectories = {}, {}, {}
    frames = set()
    for name, e in entries.items():
        outcomes[name], firsts[name] = path_outcomes(out, e, preps[e['arm'], e['mode']], geometry, keys, frames)
        path = read(out / 'paths' / (name + '.json'))
        trajectories[name] = (digest([r['action'] for r in path['rows']]), path['final_physics'])
    comparisons = {group: {t: native_summary(subset, outcomes, t) for t in TIMES}
                   for group, subset in cohorts(entries.values()).items()}
    observations = {}
    for level in ('middle', 'bottom'):
        counts = Counter()
        for name, e in entries.items():
            if e['mode'] != 'narrow-' + level:
                continue
            first, other = firsts[name], firsts[name.replace('-narrow-', '-full-')]
            assert first['state'] == other['state']
            counts['pairs'] += 1
            for camera in first['live']:
                counts[camera] += first['live'][camera] != other['live'][camera]
            counts['first_command'] += first['reply'][0] != other['reply'][0]
        observations[level] = dict(counts)
    repeats = [(v, trajectories[n.replace('-b1-', '-b2-')]) for n, v in trajectories.items() if '-b1-' in n]
    return dict(paths=len(entries), unique_posture_seed_pairs=len(COHORT['arms']) * len(BASE['stove_seeds']),
                policy_queries=sum(e['queries'] for e in entries.values()), starts=starts, width_comparisons=comparisons,
                first_input_and_action_differences=observations, reload_pairs=len(repeats),
                identical_action_and_final_state_pairs=sum(a == b for a, b in repeats), outcomes=outcomes)


def score_crossovers(out, proof, reference):
    entries = planned(COHORT, modes=CONDITIONS)
    check_replayed_paths(out, proof, entries, {})
    assert proof['schema'] == {'flags': list(FLAGS), 'contacts': list(CONTACTS)}
    cells, retained = {}, {}
    controls = 0
    for run in proof['runs']:
        name = run['session']
        entry = entries[name]
        source = entry['mode']
        assert set(run['alternates']) == set(alternate_modes(source))
        path = read(out / 'paths' / (name + '.json'))
        commands = digest([r['action'] for r in path['rows']])
        for mode, result in run['alternates'].items():
            assert result['commands_sha256'] == commands and result['mode'] == mode
            assert result['controls'] == run['policy_controls'] and len(result['measurements_sha256']) == len(result['final_physics']) == 64
            assert result['handoff'] == reference['starts'][entry['arm']][mode]['physics']
            controls += result['controls']
            rows, contacts = read_trace(result['trace'], FLAGS)
            cell = source + '_on_' + mode
            for t in TIMES:
                native = reference['outcomes'][name][t]
                crossed = outcome(rows, contacts, int(t) - entry['lead'])
                cells.setdefault(cell, {}).setdefault(t, []).append(crossed)
                counts = retained.setdefault(cell, {}).setdefault(t, {})
                for level in LEVELS:
                    group = counts.setdefault(level, {'eligible': 0, 'retained': 0})
                    success = native[level + '_in']
                    group['eligible'] += success
                    group['retained'] += success and crossed[level + '_in']
    assert controls == proof['alternate_controls']
    return dict(by_source_and_state={cell: {t: summary(values) for t, values in times.items()} for cell, times in cells.items()},
                retained_source_successes=retained)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=('collect', 'verify', 'replay'), default='verify', nargs='?')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.stage == 'collect':
        collect(args.folder)
    else:
        with unpack(args.folder) as out:
            result = read(args.folder / 'verification.json')
            assert score(out) == result
            if args.stage == 'replay':
                proof = replay(out, script=SIM, entries=planned(COHORT, modes=CONDITIONS), workers=6)
                proof.update(schema={'flags': list(FLAGS), 'contacts': list(CONTACTS)},
                             replay_source_sha256=sha(PACKET / SIM),
                             alternate_controls=sum(v['controls'] for r in proof['runs'] for v in r['alternates'].values()))
                proof['crossover'] = score_crossovers(out, proof, result)
                if args.output:
                    if args.output.exists():
                        raise FileExistsError(args.output)
                    write_json(args.output, proof)
                else:
                    print(json.dumps(proof))
            elif (args.folder / 'physical_replay.json').is_file():
                proof = read(args.folder / 'physical_replay.json')
                assert sha(out / 'sources' / SIM) == proof['replay_source_sha256']
                assert score_crossovers(out, proof, result) == proof['crossover']
                if 'archive_repeat' in proof:
                    check_archive_repeat(args.folder, out, proof, planned(COHORT, modes=CONDITIONS))
            print(f"Verified {result['paths']} native paths on one fixed tabletop", flush=True)
