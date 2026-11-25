"""Prepare and physically replay drawer widths with a common tabletop in LIBERO."""
import argparse
from functools import partial
import json
from pathlib import Path

import mujoco

from drawer_location import BASE, COHORT, FLAGS
from drawer_location_clearance import Probe
from drawer_location_sim import LocationCabinet, branch, run
from drawer_width import CONDITIONS, alternate_modes, fixed_arrangements, validate_starts
from inside import write_json
from middle_aperture_sim import environment, record_branches
from replay_middle_aperture import play_commands
from verify_atomic import read


def prepare(out):
    arrangements = fixed_arrangements()
    write_json(out / 'clearance.json', {'arrangements': arrangements})
    prepare_scene = partial(branch, corrections=arrangements)
    geometry, renderer = record_branches(out, COHORT, CONDITIONS, scene_type=LocationCabinet, prepare_fn=prepare_scene)
    clearance = {}
    for arm in COHORT['arms']:
        env = environment(arm, layout=COHORT['layout'])
        try:
            probe = Probe(env, arm, out)
            clearance[arm] = {}
            for condition in CONDITIONS:
                width, level = condition.split('-')
                settings = arrangements[width]
                travel = probe.width if width == 'full' else settings['width_m']
                clearance[arm][condition] = probe.sample(level, travel, settings['shift_xy_m'])
        finally:
            env.close()
    qual = dict(geometry=geometry, renderer=renderer, mujoco=mujoco.__version__, clearance=clearance)
    starts = validate_starts(out, qual)
    write_json(out / 'qualification.json', {**qual, 'starts': starts})
    print('Qualified ten starts against the archived tabletop and returned postures', flush=True)


def replay_path(out, entry):
    result = run(out, entry, replay=True)
    rows = read(out / 'paths' / (entry['session'] + '.json'))['rows']
    commands = [row['action'] for row in rows]
    prepare_scene = partial(branch, corrections=read(out / 'clearance.json')['arrangements'])
    result['alternates'] = {
        mode: play_commands(out, entry, commands, mode, COHORT, LocationCabinet, prepare_scene, FLAGS)
        for mode in alternate_modes(entry['mode'])
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=('prepare', 'run', 'replay'))
    parser.add_argument('session', nargs='?')
    args = parser.parse_args()
    if args.stage == 'prepare':
        prepare(args.folder)
    else:
        entry = read(args.folder / 'sessions.json')[args.session]
        if args.stage == 'run':
            run(args.folder, entry)
        else:
            print(json.dumps(replay_path(args.folder, entry)))
