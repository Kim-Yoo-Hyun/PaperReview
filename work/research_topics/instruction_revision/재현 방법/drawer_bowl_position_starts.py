"""Restore, cross and audit the two archived world-frame bowl positions."""
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache, partial
import json
import math
import subprocess
import sys
from zipfile import ZipFile

import numpy as np

from drawer_location import COHORT
from drawer_view_window_layout3 import OBJECTS, local_cohort, reference_observation
from drawer_width import tape_for
from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_drawer import pixels
from verify_middle_aperture import BASE, ORIGINAL, TASK, stationary
from verify_stove import sha
from verify_stove_fingers import DESIGN as FINGERS, source_donors
from verify_stove_layouts import digest


DESIGN_FILE = 'drawer/drawer_bowl_position.json'
DESIGN = read(PACKET / DESIGN_FILE)
SCRIPT = 'drawer_bowl_position.py'
STUDIES = {2: COHORT, 3: ORIGINAL}
LAYOUT = {arm: layout for layout, study in STUDIES.items() for arm in study['arms']}
BOWL = OBJECTS[0]
POSITIONS = DESIGN['positions']
INDICES = DESIGN['exchange_indices']
HOSTS = [position + '-bottom' for position in POSITIONS]


def alternate(mode):
    return mode.split('-')[0] + '76-bottom'


MODES = [*HOSTS, *(alternate(m) for m in HOSTS)]


def live_study(out, layout):
    return COHORT if layout == 2 else local_cohort(out)


def archive_for(layout):
    key = 'layout2_parent' if layout == 2 else 'parent'
    path = PACKET / DESIGN[key]
    assert sha(path) == DESIGN[key + '_sha256']
    return path


@lru_cache(maxsize=2)
def parent_starts(layout):
    with ZipFile(archive_for(layout)) as z:
        settings = json.loads(z.read('clearance.json'))['arrangements']
        assert settings['full']['shift_xy_m'] == settings['narrow']['shift_xy_m']
        starts = {arm: {w: json.loads(z.read(f"preparation/{arm}-{w}-bottom-{BASE['lead']}.json"))
                        for w in ('full', 'narrow')} for arm in STUDIES[layout]['arms']}
        geometry = json.loads(z.read('qualification.json'))['geometry']
    centers = {tuple(t['handoff']['upper']['bowl_xyz'][:2]) for widths in starts.values() for t in widths.values()}
    assert len(centers) == 1
    return starts, centers.pop(), settings, geometry


def arrangements(arm):
    layout = LAYOUT[arm]
    starts, native_xy, native, geometry = parent_starts(layout)
    other_xy = parent_starts(5 - layout)[1]
    addr = 1 + geometry['object_free_qpos'][BOWL]
    before = starts[arm]['full']['branch']['before']['integration_state'][addr:addr+2]
    assert .009 < math.dist(native_xy, other_xy) < .010
    base = native['full']['shift_xy_m']
    cross = {**base, BOWL: [v - initial for v, initial in zip(other_xy, before, strict=True)]}
    return {pos + width: dict(width_m=travel, shift_xy_m=shift)
            for pos, shift in [('native', base), ('crossed', cross)]
            for width, travel in [('', None), ('76', DESIGN['camera_width_m'])]}


def prepare_start(out, arm, mode):
    from drawer_location_sim import LocationCabinet, branch
    from middle_aperture_sim import record_branches

    study = {**live_study(out, LAYOUT[arm]), 'arms': [arm]}
    physical = read(out / 'clearance.json')['arrangements'][arm]
    geometry, renderer = record_branches(out, study, [mode], scene_type=LocationCabinet,
        prepare_fn=partial(branch, corrections=physical), first_observe=reference_observation)
    return dict(geometry=geometry, renderer=renderer)


def check_first(out, arm, mode, *, prepare_fn=None):
    from drawer_location_sim import LocationCabinet, branch
    if prepare_fn is None:
        prepare_fn = branch
    from drawer_sim import observe
    from drawer_view_render import ViewSchedule
    from middle_aperture_sim import environment, restore

    study = live_study(out, LAYOUT[arm])
    env = environment(arm, layout=study['layout'])
    try:
        scene = LocationCabinet(env)
        common = restore(env, scene, arm, out, donors_file=study['donors'])
        prepare_fn(env, scene, common, mode, BASE['lead'], corrections=read(out/'clearance.json')['arrangements'][arm])
        bank = read(out/'camera_inputs.json')['images'][arm]
        result = {}
        for name, indices in [('self', []), ('opposite', [0])]:
            view = ViewSchedule(env, scene, drawer='bottom', width=DESIGN['camera_width_m'],
                                limit=4, bank=bank[mode], opposite_bank=bank[alternate(mode)], indices=indices, initial_attempts=8)
            query, sample = observe(env, out, False, TASK['prompt'])
            view.apply(0, query, sample, [])
            result[name] = sample['render']
        return result
    finally:
        env.close()


def subprocess_starts(out, stage, modes, *, script=SCRIPT):
    cells = [(a, m) for a in LAYOUT for m in modes]
    def one(cell):
        output = subprocess.check_output([sys.executable, str(PACKET/script), str(out), stage, *cell], text=True)
        return json.loads(output.strip().splitlines()[-1])
    with ThreadPoolExecutor(max_workers=2) as pool:
        return dict(zip(cells, pool.map(one, cells), strict=True))


def prepare(out):
    import mujoco
    from drawer_location_clearance import Probe, environment

    write_json(local_cohort(out)['donors'], source_donors(PACKET/FINGERS['parent']))
    settings = {arm: arrangements(arm) for arm in LAYOUT}
    contact = {}
    for arm, layout in LAYOUT.items():
        env = environment(arm, layout=layout)
        try:
            p = Probe(env, arm, out, cohort=live_study(out, layout))
            contact[arm] = {}
            for m in MODES:
                s = settings[arm][m.split('-')[0]]
                row = p.sample('bottom', s['width_m'] or p.width, s['shift_xy_m'])
                assert row['clear'], (arm, m, row)
                contact[arm][m] = row
        finally:
            env.close()
    write_json(out/'clearance.json', dict(arrangements=settings, contacts=contact))
    captures = subprocess_starts(out, 'prepare-start', MODES)
    geometry = {str(i): captures[s['arms'][0], HOSTS[0]]['geometry'] for i,s in STUDIES.items()}
    renderer = next(iter(captures.values()))['renderer']
    assert 'NVIDIA' in renderer and all(v == dict(geometry=geometry[str(LAYOUT[a])], renderer=renderer)
                                        for (a,m),v in captures.items())
    qual = dict(geometry=geometry, renderer=renderer, mujoco=mujoco.__version__)
    qual['starts'], bank = validate(out, qual)
    write_json(out/'camera_inputs.json', bank)
    checks = subprocess_starts(out, 'check-first', HOSTS)
    qual['first_inputs'] = {a: {m: checks[a,m] for m in HOSTS} for a in LAYOUT}
    write_json(out/'qualification.json', qual)
    checked_inputs(out)
    print('Qualified 8 full-width hosts and 8 native 76 mm camera references before inference', flush=True)


def validate(out, qual):
    c = read(out/'clearance.json')
    starts, images, changes = {}, {}, {}
    assert 'NVIDIA' in qual['renderer']
    for arm, layout in LAYOUT.items():
        study = STUDIES[layout]
        old, xy, _, geometry = parent_starts(layout)
        other = parent_starts(5-layout)[1]
        assert qual['geometry'][str(layout)] == geometry and c['arrangements'][arm] == arrangements(arm)
        tapes = {m: tape_for(out, arm, m) for m in MODES}
        addr = 1 + geometry['object_free_qpos'][BOWL]
        starts[arm], images[arm], changes[arm] = {}, {}, {}
        for mode, tape in tapes.items():
            wide = mode in HOSTS
            archived = old[arm]['full' if wide else 'narrow']
            crossed = mode.startswith('crossed')
            target = other if crossed else xy
            b, h, first = tape['branch'], tape['handoff'], tape['first']
            assert (tape['arm'],tape['mode'],tape['length']) == (arm,mode,BASE['lead'])
            assert all(tape[k] == archived[k] for k in ('donor_physics','common','start','actions','rows'))
            assert b['before'] == archived['branch']['before'] and digest(b['before']) == study['returned_physics'][arm]
            assert b['shift_xy_m'] == c['arrangements'][arm][mode.split('-')[0]]['shift_xy_m']
            assert b['displacement_m'] == archived['branch']['displacement_m']
            assert h['upper']['joints'] == archived['handoff']['upper']['joints']
            assert h['tool'] == archived['handoff']['tool'] and first['state'] == archived['first']['state']
            assert not b['slide_contacts'] and not h['robot_contacts']
            assert not any(h['upper'][k] for k in ('bowl_in','middle_in','bottom_in'))
            for name, pos in h['objects'].items():
                prior = archived['handoff']['objects'][name]
                assert pos[2:] == prior[2:] and (pos == prior if name != BOWL else math.dist(pos[:2],target) < 1e-12)
            assert tuple(h['upper']['bowl_xyz']) == tuple(h['objects'][BOWL][:3])
            ref = archived['branch']['after']
            expected = ref['integration_state'].copy()
            if crossed:
                assert math.dist(b['after']['integration_state'][addr:addr+2], target) < 1e-12
                expected[addr:addr+2] = b['after']['integration_state'][addr:addr+2]
            assert b['after'] == dict(ref, integration_state=expected)
            assert first['physics'] == digest(b['after'])
            if not crossed:
                assert first['physics'] == archived['first']['physics']
            row = c['contacts'][arm][mode]
            assert row['clear'] and not row['contacts'] and set(row['supported']) == set(OBJECTS)
            hold = stationary(tape)['maximum']
            assert hold['drawer_mm'] <= 1.
            pair = tuple(first['live'][cam] for cam in CAMERAS)
            samples = [tuple(s) for s in first['reference_samples']]
            assert len(samples) == 9 and samples.count(pair) > len(samples)//2
            for hashes in set(samples):
                for hsh in hashes:
                    pixels(out,hsh)
            images[arm][mode] = first['live']
            starts[arm][mode] = dict(physics=first['physics'], opening_m=-b['displacement_m'], bowl_xyz=h['upper']['bowl_xyz'],
                max_stationary_object_mm=hold['object_mm'], max_stationary_drawer_mm=hold['drawer_mm'])
        comparisons = [(m,alternate(m)) for m in HOSTS] + [(HOSTS[0],HOSTS[1]),(alternate(HOSTS[0]),alternate(HOSTS[1]))]
        for a,b in comparisons:
            diffs = {cam: int(np.any(pixels(out,images[arm][a][cam]) != pixels(out,images[arm][b][cam]),axis=2).sum()) for cam in CAMERAS}
            assert all(diffs.values()), (arm,a,b,diffs)
            changes[arm][a + '_to_' + b] = diffs
    return starts, dict(images=images, changed_pixels=changes)


def checked_inputs(out, *, validate_fn=validate):
    qual = read(out/'qualification.json')
    starts, bank = validate_fn(out, qual)
    assert qual['starts'] == starts and read(out/'camera_inputs.json') == bank
    for arm in LAYOUT:
        for mode in HOSTS:
            for name, donor in [('self',mode),('opposite',alternate(mode))]:
                rec = qual['first_inputs'][arm][mode][name]
                assert rec['host_after'] == starts[arm][mode]['physics'] and rec['self_rgb'] == bank['images'][arm][mode]
                assert rec['sent'] == bank['images'][arm][donor] and rec['exchange'] == (name == 'opposite')
    return qual, bank
