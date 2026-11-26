"""Target opposite-layout tool coordinates through a fixed 60-control return."""
from collections import Counter
from copy import copy
from functools import lru_cache, partial
import json
import math
from zipfile import ZipFile

import numpy as np

from drawer_bowl_position_starts import (HOSTS, INDICES, LAYOUT, MODES, POSITIONS, STUDIES,
    alternate, check_first, checked_inputs, live_study, subprocess_starts)
from drawer_view_window_layout3 import OBJECTS, local_cohort, reference_observation
from drawer_width import tape_for
from inside import write_json
from verify_atomic import CAMERAS, PACKET, read
from verify_drawer import pixels
from verify_middle_aperture import BASE, TASK, stationary
from verify_stove import sha
from verify_stove_fingers import DESIGN as FINGERS, source_donors
from verify_stove_layouts import digest
from verify_stove_pose import angle

SCRIPT = 'drawer_gripper_position.py'
DESIGN_FILE = 'drawer/drawer_gripper_position.json'
DESIGN = read(PACKET / DESIGN_FILE)
PAIRS = {a: b for x,y in DESIGN['paired_arms'] for a,b in ((x,y),(y,x))}
assert set(PAIRS) == set(LAYOUT) and all(LAYOUT[a] != LAYOUT[b] for a,b in PAIRS.items())
assert DESIGN['positions'] == POSITIONS and DESIGN['exchange_indices'] == INDICES


@lru_cache(maxsize=1)
def parent():
    path = PACKET / DESIGN['parent']
    assert sha(path) == DESIGN['parent_sha256']
    with ZipFile(path) as z:
        starts = {a: {m: json.loads(z.read(f"preparation/{a}-{m}-{BASE['lead']}.json"))
                      for m in (HOSTS[0], alternate(HOSTS[0]))} for a in LAYOUT}
        return starts, json.loads(z.read('qualification.json'))['geometry']


def joint_target(env, native, delta):
    import mujoco
    from scipy.spatial.transform import Rotation

    model, live = env.sim.model._model, env.sim.data._data
    scratch = copy(live)
    assert not np.shares_memory(scratch.qpos, live.qpos)
    robot = env.robots[0]
    pos, vel, site = robot._ref_joint_pos_indexes, robot._ref_joint_vel_indexes, robot.eef_site_id
    scratch.qpos[pos] = native
    mujoco.mj_forward(model, scratch)
    goal = scratch.site_xpos[site] + delta
    def orientation():
        return Rotation.from_matrix(scratch.site_xmat[site].reshape(3,3))
    target_rot = orientation()
    lower, upper = model.jnt_range[model.dof_jntid[vel]].T
    linear, angular = (np.zeros((3,model.nv)) for _ in range(2))
    for _ in range(20):
        error = np.r_[goal - scratch.site_xpos[site], (target_rot * orientation().inv()).as_rotvec()]
        if np.linalg.norm(error) < 1e-11:
            return scratch.qpos[pos].tolist()
        mujoco.mj_jacSite(model, scratch, linear, angular, site)
        jac = np.vstack((linear[:,vel],angular[:,vel]))
        update = np.linalg.lstsq(jac,error,rcond=1e-8)[0]
        scratch.qpos[pos] += update
        assert np.all((lower < scratch.qpos[pos]) & (scratch.qpos[pos] < upper))
        mujoco.mj_forward(model, scratch)
    raise ValueError('No converged six-axis gripper target')


def settings(env, arm):
    starts, _ = parent()
    native = starts[arm][HOSTS[0]]
    own = native['handoff']['tool']
    other = starts[PAIRS[arm]][HOSTS[0]]['handoff']['tool']
    delta = np.subtract(other['xyz'], own['xyz'])
    assert .029 < np.linalg.norm(delta) < .031
    joints = native['common']['joints']
    cross = joint_target(env, joints, delta)
    return {pos + suffix: dict(width_m=width, shift_xy_m=native['branch']['shift_xy_m'],
                               joint_target=q, target_xyz=xyz)
            for pos,q,xyz in [('native',joints,own['xyz']),('crossed',cross,other['xyz'])]
            for suffix,width in [('',-native['branch']['displacement_m']),('76',DESIGN['camera_width_m'])]}


def contact_snapshot(env, scene):
    model, data = env.sim.model, env.sim.data._data
    table = model.geom_name2id('table_collision')
    obj = {int(i):name for name in OBJECTS for i in np.flatnonzero(model.geom_bodyid == model.body_name2id(name))}
    pairs = sorted({tuple(sorted((int(a),int(b)))) for a,b in zip(data.contact.geom1, data.contact.geom2)})
    supported = {obj[a] for pair in pairs for a,b in (pair,pair[::-1]) if a in obj and b == table}
    obstructions = [pair for pair in pairs if ((pair[0] in scene.robot_geoms) != (pair[1] in scene.robot_geoms)
                    or scene.contact_slides.intersection(pair) or (set(obj).intersection(pair) and table not in pair))]
    return dict(pairs=[list(p) for p in pairs], table_geom=table, object_geoms={n:sorted(i for i in obj if obj[i]==n) for n in OBJECTS},
                supported=sorted(supported), obstructions=[list(p) for p in obstructions])


def branch(env, scene, common, mode, length, *, corrections):
    from drawer_location_sim import branch as open_drawer
    target = corrections[mode.split('-')[0]]['joint_target']
    tape = open_drawer(env, scene, {**common, 'joints':target}, mode, length, corrections=corrections)
    return dict(tape, contacts_at_start=contact_snapshot(env,scene))


def prepare_start(out, arm, mode):
    from drawer_location_sim import LocationCabinet
    from middle_aperture_sim import record_branches

    study = {**live_study(out,LAYOUT[arm]), 'arms':[arm]}
    geometry, renderer = record_branches(out, study, [mode], scene_type=LocationCabinet,
        prepare_fn=partial(branch,corrections=read(out/'clearance.json')['arrangements'][arm]), first_observe=reference_observation)
    return dict(geometry=geometry,renderer=renderer)


def prepare(out):
    import mujoco
    from middle_aperture_sim import environment

    write_json(local_cohort(out)['donors'],source_donors(PACKET/FINGERS['parent']))
    arrangements = {}
    for arm, layout in LAYOUT.items():
        env = environment(arm,layout=layout)
        try:
            arrangements[arm] = settings(env,arm)
        finally:
            env.close()
    write_json(out/'clearance.json',dict(arrangements=arrangements))
    captures = subprocess_starts(out,'prepare-start',MODES,script=SCRIPT)
    geometry = parent()[1]
    renderer = next(iter(captures.values()))['renderer']
    assert 'NVIDIA' in renderer and all(v == dict(geometry=geometry[str(LAYOUT[a])],renderer=renderer) for (a,m),v in captures.items())
    qual = dict(geometry=geometry,renderer=renderer,mujoco=mujoco.__version__)
    qual['starts'], bank = validate(out,qual)
    write_json(out/'camera_inputs.json',bank)
    checks = subprocess_starts(out,'check-first',HOSTS,script=SCRIPT)
    qual['first_inputs'] = {a:{m:checks[a,m] for m in HOSTS} for a in LAYOUT}
    write_json(out/'qualification.json',qual)
    checked_inputs(out,validate_fn=validate)
    print('Qualified eight gripper starts and eight matched narrow references',flush=True)


def finger_gap(tool):
    left,right = tool['fingers']
    return left - right


def validate(out, qual):
    archives, geometry = parent()
    assert qual['geometry'] == geometry and 'NVIDIA' in qual['renderer']
    arrangements = read(out/'clearance.json')['arrangements']
    limits = DESIGN['limits']
    starts, images, changes = {}, {}, {}
    for arm, layout in LAYOUT.items():
        starts[arm], images[arm], changes[arm] = {}, {}, {}
        tapes = {m:tape_for(out,arm,m) for m in MODES}
        for mode, t in tapes.items():
            native = mode.startswith('native')
            width_mode = HOSTS[0] if mode in HOSTS else alternate(HOSTS[0])
            ref = archives[arm][width_mode]
            dest = archives[arm if native else PAIRS[arm]][width_mode]['handoff']['tool']['xyz']
            setting = arrangements[arm][mode.split('-')[0]]
            h, fis, b = t['handoff'],t['first'],t['branch']
            tool, own = h['tool'],ref['handoff']['tool']
            assert (t['arm'],t['mode'],t['length']) == (arm,mode,BASE['lead'])
            assert all(t[k] == ref[k] for k in ('start','donor_physics','common'))
            assert len(t['actions']) == len(t['rows']) == BASE['lead']
            assert t['actions'][:8] == ref['actions'][:8] and all(a[-1] == -1. for a in t['actions'])
            assert setting['target_xyz'] == dest and setting['shift_xy_m'] == b['shift_xy_m'] == ref['branch']['shift_xy_m']
            assert setting['width_m'] == -b['displacement_m'] == -ref['branch']['displacement_m']
            assert not b['slide_contacts'] and not h['robot_contacts'] and digest(b['after']) == fis['physics']
            assert not any(r['robot_contacts'] for r in t['rows'][-5:])
            assert not any(h['upper'][k] for k in ('bowl_in','middle_in','bottom_in'))
            assert fis['state'][:3] == tool['xyz'] and fis['state'][-2:] == tool['fingers']
            contact = t['contacts_at_start']
            assert not contact['obstructions'] and set(contact['supported']) == set(OBJECTS)
            assert all(any(sorted([contact['table_geom'],i]) in contact['pairs'] for i in indices) for indices in contact['object_geoms'].values())
            if native:
                assert setting['joint_target'] == ref['common']['joints']
                assert all(t[k] == ref[k] for k in ('actions','rows','branch','handoff','stationary'))
                assert (fis['physics'],fis['state']) == (ref['first']['physics'],ref['first']['state'])
            else:
                assert t['actions'][8:] != ref['actions'][8:]
            other_width = tapes[mode.split('76-')[0]+'-bottom'] if '76-' in mode else tapes[alternate(mode)]
            assert all(t[k] == other_width[k] for k in ('actions','rows')) and tool == other_width['handoff']['tool']
            assert h['objects'] == other_width['handoff']['objects'] and fis['state'] == other_width['first']['state']
            hold = stationary(t)['maximum']
            scene_mm = max(1000*math.dist(v[:3],ref['handoff']['objects'][n][:3]) for n,v in h['objects'].items())
            scene_deg = max(angle(v[3:],ref['handoff']['objects'][n][3:]) for n,v in h['objects'].items())
            drawer_mm = 1000*max(abs(v-w) for v,w in zip(h['upper']['joints'],ref['handoff']['upper']['joints'],strict=True))
            errors = dict(target_mm=1000*math.dist(tool['xyz'],dest), orientation_deg=angle(tool['quat'],own['quat']),
                finger_gap_mm=1000*abs(finger_gap(tool)-finger_gap(own)),joint_speed_rad_s=max(map(abs,tool['velocity'])),
                object_mm=scene_mm,drawer_mm=drawer_mm)
            assert all(v <= limits[k] for k,v in errors.items()), (arm,mode,errors)
            assert scene_deg < 1e-4 and hold['drawer_mm'] < .01 and hold['object_mm'] < .01
            pair = tuple(fis['live'][cam] for cam in CAMERAS)
            samples = Counter(tuple(s) for s in fis['reference_samples'])
            assert sum(samples.values()) == 9 and samples[pair] > 4
            for hashes in samples:
                for hsh in hashes:
                    pixels(out,hsh)
            images[arm][mode] = fis['live']
            starts[arm][mode] = dict(physics=fis['physics'], opening_m=-b['displacement_m'], target_xyz=dest, tool=tool,
                proprio=fis['state'], achieved_shift_mm=(1000*np.subtract(tool['xyz'],own['xyz'])).tolist(),
                joint_target=setting['joint_target'], joint_change_rad=np.subtract(tool['joints'],own['joints']).tolist(),
                finger_gap_mm=1000*finger_gap(tool), errors=errors, objects_angle_deg=scene_deg,
                stationary_max=hold, contacts=contact, native_pixels_match_parent=(fis['live']==ref['first']['live']))
        comparisons = [(m,alternate(m)) for m in HOSTS] + [(HOSTS[0],HOSTS[1]),(alternate(HOSTS[0]),alternate(HOSTS[1]))]
        for a,b in comparisons:
            diffs = {cam:int(np.any(pixels(out,images[arm][a][cam]) != pixels(out,images[arm][b][cam]),axis=2).sum()) for cam in CAMERAS}
            assert all(diffs.values()), (arm,a,b,diffs)
            changes[arm][a+'_to_'+b] = diffs
    return starts, dict(images=images,changed_pixels=changes)
