"""Place a matched opening on one of two cabinet slides in LIBERO."""
import argparse
from functools import partial
import json
from pathlib import Path

import mujoco

from atomic_control import capture_state
from drawer_location import COHORT, FLAGS, MODES, CONDITIONS, qualify_starts
from drawer_sim import save
from middle_aperture_sim import Cabinet, environment, record_branches, restore
from replay_middle_aperture import play_commands
from stove_pose_sim import prepare, trajectory
from verify_atomic import read
from verify_middle_aperture import BASE


class LocationCabinet(Cabinet):
    def __init__(self, env):
        super().__init__(env)
        model, data = env.sim.model, env.sim.data
        self.slides = {}
        for level in ('middle', 'bottom'):
            joint = model.joint_name2id(f'wooden_cabinet_1_{level}_level')
            body = model.body_name2id(f'wooden_cabinet_1_cabinet_{level}')
            assert model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_SLIDE and model.jnt_bodyid[joint] == body
            qpos, qvel = int(model.jnt_qposadr[joint]), int(model.jnt_dofadr[joint])
            self.slides[level] = dict(qpos=qpos, qvel=qvel, closed=float(data.qpos[qpos]),
                                      axis=model.jnt_axis[joint].tolist(), limits=model.jnt_range[joint].tolist())
        self.geometry['slides'] = self.slides
        self.contact_slides = set(self.geometry['middle']) | set(self.geometry['bottom'])
        self.moved_objects = {}
        for name in ('akita_black_bowl_1_main', 'plate_1_main'):
            body = model.body_name2id(name)
            joint = int(model.body_jntadr[body])
            assert model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_FREE
            self.moved_objects[name] = int(model.jnt_qposadr[joint])
        self.geometry['object_free_qpos'] = self.moved_objects

    def policy_row(self):
        row = super().policy_row()
        row['bottom_open'] = bool(self.env.env._eval_predicate(['open', 'wooden_cabinet_1_bottom_region']))
        return row


def set_opening(env, scene, mode, displacement, shift_xy):
    data = env.sim.data
    warmstart = data.qacc_warmstart.copy()
    for level, slide in scene.slides.items():
        target = slide['closed'] + (displacement if mode == level else 0.)
        assert slide['limits'][0] <= target <= slide['limits'][1]
        data.qpos[slide['qpos']] = target
        data.qvel[slide['qvel']] = 0.
    for name,pos in scene.moved_objects.items():
        shift = shift_xy[name] if isinstance(shift_xy,dict) else shift_xy
        if any(shift):
            data.qpos[pos:pos+2] += shift
    env.sim.forward()
    data.qacc_warmstart[:] = warmstart


def branch(env, scene, common, mode, length, *, corrections=None):
    correction = None
    if corrections is not None:
        arrangement,mode = mode.split('-')
        correction = corrections[arrangement]
    assert mode in MODES and length == BASE['lead']
    tape = prepare(env, scene, common, 'pose', length)
    before = capture_state(env)
    middle = scene.slides['middle']
    measured = float(env.sim.data.qpos[middle['qpos']]) - middle['closed']
    width = correction['width_m'] if correction else None
    shift = correction['shift_xy_m'] if correction else [0.,0.]
    displacement = measured if width is None else -width
    set_opening(env,scene,mode,displacement,shift)
    tape['branch'] = dict(before=before, after=capture_state(env), displacement_m=displacement, shift_xy_m=shift,
                          slide_contacts=[list(pair) for pair in scene.slide_contacts()])
    return tape


def run(out, entry, replay=False, *, first_images=None, view_factory=None, cohort=COHORT):
    return trajectory(out, entry, replay=replay, open_env=partial(environment, layout=cohort['layout']),
                      restore_prefix=partial(restore, donors_file=cohort['donors']),
                      prepare_fn=partial(branch,corrections=read(out/'clearance.json')['arrangements']), scene_type=LocationCabinet,
                      first_images=first_images, view_factory=view_factory)


def replay_all_scenes(out, entry):
    result = run(out, entry, replay=True)
    path = read(out/'paths'/(entry['session']+'.json'))
    commands = [row['action'] for row in path['rows']]
    prepare_fn = partial(branch,corrections=read(out/'clearance.json')['arrangements'])
    arrangement,source = entry['mode'].split('-')
    result['alternates'] = {mode:play_commands(out, entry, commands, f'{arrangement}-{mode}', COHORT, LocationCabinet, prepare_fn, FLAGS)
                            for mode in MODES if mode != source}
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=('prepare', 'run', 'replay'))
    parser.add_argument('session', nargs='?')
    args = parser.parse_args()
    if args.stage == 'prepare':
        from drawer_location_clearance import select_clearance
        original = args.folder/'original'
        (original/'preparation').mkdir(parents=True)
        record_branches(original,COHORT,MODES,scene_type=LocationCabinet,prepare_fn=branch)
        clearance = select_clearance(original)
        save(args.folder/'clearance.json',clearance)
        print('Clearance from physics only',clearance['arrangements'],flush=True)
        prepare_fn = partial(branch,corrections=clearance['arrangements'])
        geometry, renderer = record_branches(args.folder, COHORT, CONDITIONS, scene_type=LocationCabinet, prepare_fn=prepare_fn)
        _, checks = qualify_starts(args.folder, geometry)
        save(args.folder/'qualification.json', dict(geometry=geometry, renderer=renderer, mujoco=mujoco.__version__, starts=checks))
        print('Qualified all twelve starts and matched physical drawer displacements', flush=True)
    else:
        entry = read(args.folder/'sessions.json')[args.session]
        if args.stage == 'run':
            run(args.folder, entry)
        else:
            print(json.dumps(replay_all_scenes(args.folder, entry)))
