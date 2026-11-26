"""Branch the actual returned Panda state on the middle slide of the cabinet."""
import argparse
from functools import partial
import json
from pathlib import Path

import mujoco
import numpy as np

from atomic_control import capture_state
from drawer_sim import observe, save, state_hash
from stove_finger_sim import restore
from stove_pose_sim import prepare, record_prep, trajectory
from upper_bowl_sim import UpperDrawer, environment, restore as restore_upper
from verify_atomic import read
from verify_middle_aperture import BASE, DESIGN, NEUTRAL, TASK, qualify_pairs, recorded_study


class Cabinet(UpperDrawer):
    def __init__(self, env):
        super().__init__(env)
        model, data = env.sim.model, env.sim.data
        joint = model.joint_name2id('wooden_cabinet_1_middle_level')
        assert model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_SLIDE
        self.slide = int(model.jnt_qposadr[joint])
        self.speed = int(model.jnt_dofadr[joint])
        self.closed = float(data.qpos[self.slide])
        self.regions = {}
        self.geometry = dict(self.target_geometry, robot_geoms=sorted(self.robot_geoms),
                             slide_qpos=self.slide, slide_qvel=self.speed, nq=model.nq,
                             slide_range=model.jnt_range[joint].tolist())
        for level in ('middle', 'bottom'):
            name = f'wooden_cabinet_1_{level}_region'
            site = model.site_name2id(name)
            half_size = np.asarray(env.env.object_sites_dict[name].size)
            extent = np.abs(data.site_xmat[site].reshape(3, 3) @ half_size)
            body = model.body_name2id(f'wooden_cabinet_1_cabinet_{level}')
            geoms = set(np.flatnonzero(model.geom_bodyid == body).tolist())
            self.regions[level] = (site, geoms, ['in', TASK['goal'][1], name])
            self.geometry[level] = sorted(geoms)
            self.geometry[level + '_extent'] = extent.tolist()
        assert set(self.geometry['middle']) == self.stove.drawer.drawer
        self.contact_slides = self.stove.drawer.drawer

    def policy_row(self):
        row = super().policy_row()
        data = self.env.sim.data
        contacts = data._data.contact
        bowl_pairs = [(int(a), int(b)) if a in self.bowl else (int(b), int(a))
                      for a, b in zip(contacts.geom1, contacts.geom2) if a in self.bowl or b in self.bowl]
        for level, (site, geoms, goal) in self.regions.items():
            row[level + '_xyz'] = data.site_xpos[site].tolist()
            row[level + '_in'] = bool(self.env.env._eval_predicate(goal))
            row[level + '_pairs'] = [list(p) for p in sorted({p for p in bowl_pairs if p[1] in geoms})]
        return row

    def slide_contacts(self):
        contact = self.env.sim.data._data.contact
        geoms = self.contact_slides
        return sorted({tuple(sorted((int(a), int(b)))) for a, b in zip(contact.geom1, contact.geom2)
                       if a in geoms or b in geoms})


def branch(env, scene, common, mode, length):
    assert mode in DESIGN['modes'] and length == BASE['lead']
    tape = prepare(env, scene, common, 'pose', length)
    before = capture_state(env)
    data = env.sim.data
    warmstart = data.qacc_warmstart.copy()
    if mode == 'closed':
        data.qpos[scene.slide] = scene.closed
    data.qvel[scene.speed] = 0.0
    env.sim.forward()
    # Forward dynamics also writes the solver warm start. Both branches retain
    # the warm start from the exact recorded return, including its unmodified arm.
    data.qacc_warmstart[:] = warmstart
    tape['branch'] = dict(before=before, after=capture_state(env), closed_reference=scene.closed,
                          slide_contacts=[list(p) for p in scene.slide_contacts()])
    return tape


def stationary_probe(env, scene):
    rows = []
    for _ in range(DESIGN['hold_controls']):
        env.step([0., 0., 0., 0., 0., 0., -1.])
        sample = scene.read()
        rows.append(dict(tool=sample['tool'], objects=sample['objects'], joints=sample['upper']['joints'],
                         robot_contacts=sample['robot_contacts'], slide_contacts=[list(p) for p in scene.slide_contacts()]))
    return rows


def run_path(out, entry, replay=False):
    direct = entry['arm']==NEUTRAL
    study = recorded_study(out.parent if direct else out)
    return trajectory(out,entry,replay=replay,open_env=partial(environment,layout=study['layout']),
                      restore_prefix=restore_upper if direct else partial(restore,donors_file=study['donors']),
                      prepare_fn=prepare if direct else branch,scene_type=Cabinet)


def qualify_standalone(out):
    from OpenGL import GL
    study = recorded_study(out)
    folder = out/'standalone'
    open_env = partial(environment,layout=study['layout'])
    tape = record_prep(folder,NEUTRAL,'immediate',0,open_env=open_env,restore_prefix=restore_upper,
                       scene_type=Cabinet,prompt=TASK['prompt'])
    save(folder/'preparation'/f'{NEUTRAL}-immediate-0.json',tape)
    env = open_env(NEUTRAL)
    try:
        geometry = Cabinet(env).geometry
        renderer = GL.glGetString(GL.GL_RENDERER).decode()
        assert 'NVIDIA' in renderer
        save(folder/'qualification.json',dict(geometry=geometry,renderer=renderer,mujoco=mujoco.__version__))
    finally:
        env.close()


def record_branches(out, study, modes, *, scene_type=Cabinet, prepare_fn=branch, first_observe=observe):
    from OpenGL import GL
    geometry = None
    for arm in study['arms']:
        for mode in modes:
            env = environment(arm,layout=study['layout'])
            try:
                scene = scene_type(env)
                if geometry is None:
                    geometry = scene.geometry
                assert geometry == scene.geometry
                common = restore(env, scene, arm, out, donors_file=study['donors'])
                donor = state_hash(capture_state(env))
                tape = prepare_fn(env, scene, common, mode, BASE['lead'])
                _, first = first_observe(env, out, False, TASK['prompt'])
                tape.update(arm=arm, mode=mode, length=BASE['lead'], common=common, donor_physics=donor,
                            first=first, handoff=scene.read(), stationary=stationary_probe(env, scene))
                save(out/'preparation'/f"{arm}-{mode}-{BASE['lead']}.json", tape)
                renderer = GL.glGetString(GL.GL_RENDERER).decode()
                assert 'NVIDIA' in renderer
            finally:
                env.close()
    return geometry, renderer


def qualify(out):
    study = recorded_study(out)
    geometry, renderer = record_branches(out, study, DESIGN['modes'])
    _, pairs = qualify_pairs(out, geometry, study)
    save(out/'qualification.json', dict(geometry=geometry, pairs=pairs, renderer=renderer, mujoco=mujoco.__version__))
    print('Verified both physical branches and stationary probes at both returned arm states', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=Path)
    parser.add_argument('stage', choices=['prepare','prepare-standalone','run','replay'])
    parser.add_argument('session', nargs='?')
    args = parser.parse_args()
    if args.stage == 'prepare-standalone':
        qualify_standalone(args.folder)
    elif args.stage == 'prepare':
        qualify(args.folder)
    else:
        entry = read(args.folder/'sessions.json')[args.session]
        result = run_path(args.folder,entry,replay=args.stage=='replay')
        if result:
            print(json.dumps(result))
