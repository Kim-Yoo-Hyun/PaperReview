"""Measure physical upper-drawer contact, articulation and the official bowl-in-region goal."""
import argparse
import json
from pathlib import Path

import numpy as np

from drawer_sim import reset, save
from stove_finger_sim import prepare_with_fingers, restore as restore_contact
from stove_pose_sim import Scene, posture, record_prep, trajectory
from verify_atomic import PACKET, read
from verify_stove import D as STOVE
from verify_upper_bowl import BASE, DESIGN, NEUTRAL, preparation_cells, validate_preparations


class UpperDrawer(Scene):
    def __init__(self, env):
        super().__init__(env, stove_goal=STOVE['goal'])
        model, native = env.sim.model, env.env
        _, bowl, site = DESIGN['goal']
        self.site = model.site_name2id(site)
        self.bowl_body = native.obj_body_id[bowl]
        top_body = model.body_name2id('wooden_cabinet_1_cabinet_top')
        top_joint = model.joint_name2id('wooden_cabinet_1_top_level')
        assert model.jnt_bodyid[top_joint] == top_body
        self.top = set(np.flatnonzero(model.geom_bodyid == top_body).tolist())
        self.bowl = {int(model.geom_name2id(g)) for g in native.get_object(bowl).contact_geoms}
        drawer = self.stove.drawer
        assert self.top and self.bowl and self.top.isdisjoint(drawer.drawer | self.bowl | drawer.gripper)
        self.half_size = np.asarray(native.object_sites_dict[site].size)
        self.extent = self.site_extent()
        ranges = native.get_object('wooden_cabinet_1').object_properties['articulation']['default_open_ranges']
        self.target_geometry = dict(top=sorted(self.top), bowl=sorted(self.bowl),
                                    fingers=sorted(drawer.gripper), middle=sorted(drawer.drawer),
                                    top_geom_names=[model.geom_id2name(i) for i in sorted(self.top)],
                                    open_below_m=max(ranges), site_half_size=self.half_size.tolist(),
                                    site_extent_world=self.extent.tolist(), lower_z_allowance_m=0.01)

    def site_extent(self):
        return np.abs(self.env.sim.data.site_xmat[self.site].reshape(3,3) @ self.half_size)

    def policy_row(self):
        data = self.env.sim.data
        drawer = self.stove.drawer.sample()
        pairs = [list(pair) for pair in drawer['gripper_pairs']]
        support = set()
        for a, b in zip(data._data.contact.geom1, data._data.contact.geom2):
            if a in self.bowl and b in self.top:
                support.add((int(a),int(b)))
            elif b in self.bowl and a in self.top:
                support.add((int(b),int(a)))
        # This cabinet is fixed to the table and its drawers translate without rotating.
        assert np.allclose(self.site_extent(),self.extent,rtol=0,atol=1e-12)
        return dict(joints=drawer['joints'], gripper_pairs=pairs, top_contact=any(b in self.top for _,b in pairs),
                    bowl_contact=any(b in self.bowl for _,b in pairs), bowl_top_pairs=sorted(map(list,support)),
                    top_open=bool(self.env.env._eval_predicate(DESIGN['open_goal'])),
                    middle_open=bool(self.env.env._eval_predicate(['open','wooden_cabinet_1_middle_region'])),
                    bowl_in=drawer['goal'], bowl_xyz=data.body_xpos[self.bowl_body].tolist(),
                    target_xyz=data.site_xpos[self.site].tolist())

    def read(self):
        return dict(super().read(), upper=self.policy_row())


def environment(arm, *, layout=None):
    from verify_stove_fingers import DESIGN as FINGERS
    return reset(FINGERS['layout'] if layout is None else layout, task_file=PACKET/DESIGN['bddl'], starts_file=PACKET/BASE['starts_file'],
                 goal=DESIGN['goal'])


def restore(env, scene, arm, out):
    if arm == NEUTRAL:
        return posture(env)
    return restore_contact(env,scene,arm,out)


def qualify(out):
    import mujoco
    from OpenGL import GL
    env = environment(NEUTRAL)
    try:
        geometry = UpperDrawer(env).target_geometry
        renderer = GL.glGetString(GL.GL_RENDERER).decode()
        assert 'NVIDIA' in renderer
    finally:
        env.close()
    for arm,mode,lead in preparation_cells():
        tape = record_prep(out,arm,mode,lead,open_env=environment,restore_prefix=restore,prepare_fn=prepare_with_fingers,
                           scene_type=UpperDrawer,prompt=DESIGN['prompt'])
        save(out/'preparation'/f'{arm}-{mode}-{lead}.json',tape)
    _,summary = validate_preparations(out,geometry)
    save(out/'qualification.json',dict(geometry=geometry, preparations=summary, renderer=renderer, mujoco=mujoco.__version__))
    print('Verified neutral start and the six preparations from the two archived contact states',flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('out',type=Path)
    parser.add_argument('stage',choices=['prepare','run','replay'])
    parser.add_argument('session',nargs='?')
    args = parser.parse_args()
    if args.stage == 'prepare':
        qualify(args.out)
    else:
        e = read(args.out/'sessions.json')[args.session]
        result = trajectory(args.out,e,replay=args.stage=='replay',open_env=environment,restore_prefix=restore,
                            prepare_fn=prepare_with_fingers,scene_type=UpperDrawer)
        if result:
            print(json.dumps(result))
