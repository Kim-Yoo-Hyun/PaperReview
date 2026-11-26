"""Physically prepare a common Panda posture or hold the drawer endpoint in LIBERO."""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.spatial.transform import Rotation
from robosuite.controllers import load_controller_config

from atomic_control import capture_state
from drawer_sim import client_for, frame, observe, save, state_hash
from stove_sim import Stove, environment, prefix
from verify_atomic import PACKET, read
from verify_stove import D as STOVE


PLAN = read(PACKET/'drawer/stove_pose.json')


def posture(env):
    data, robot = env.sim.data, env.robots[0]
    site = robot.eef_site_id
    return dict(xyz=data.site_xpos[site].tolist(),
                quat=Rotation.from_matrix(data.site_xmat[site].reshape(3,3)).as_quat().tolist(),
                joints=data.qpos[robot._ref_joint_pos_indexes].tolist(),
                fingers=data.qpos[robot._ref_gripper_joint_pos_indexes].tolist(),
                velocity=data.qvel[robot._ref_joint_vel_indexes].tolist())


class Scene:
    def __init__(self, env, *, stove_goal=None):
        self.env = env
        model = env.sim.model
        self.bodies = {name:model.body_name2id(name) for name in PLAN['scene_objects']}
        self.robot_geoms = {i for i in range(model.ngeom)
                            if str(model.body_id2name(model.geom_bodyid[i])).startswith(('robot0_','gripper0_'))}
        self.stove = Stove(env,goal=stove_goal)

    def policy_row(self):
        return self.stove.sample()

    def read(self):
        data = self.env.sim.data
        pairs = set()
        for a,b in zip(data._data.contact.geom1,data._data.contact.geom2):
            if (a in self.robot_geoms) != (b in self.robot_geoms):
                pairs.add((int(a),int(b)) if a in self.robot_geoms else (int(b),int(a)))
        return dict(tool=posture(self.env),
                    objects={n:[*data.body_xpos[i].tolist(),*data.body_xquat[i].tolist()] for n,i in self.bodies.items()},
                    robot_contacts=[list(p) for p in sorted(pairs)], stove=self.stove.sample())


def prepare(env, scene, common, mode, length):
    start = scene.read()
    rows, actions = [], []
    if mode == 'immediate':
        return dict(start=start,rows=rows,actions=actions)
    robot = env.robots[0]
    native, config = robot.controller, robot.controller_config
    dest = common if mode == 'pose' else start['tool']
    offset = np.asarray(PLAN['clear_translation_world_m']) if mode == 'pose' else np.zeros(3)
    xyz = np.asarray(start['tool']['xyz']) + offset
    orientation = Rotation.from_quat(start['tool']['quat'])

    def advance(cmd):
        action = [*cmd.tolist(), PLAN['open_gripper']]
        env.step(action)
        actions.append(action)
        rows.append(scene.read())

    for _ in range(PLAN['clear_controls']):
        current = posture(env)
        angle = (orientation * Rotation.from_quat(current['quat']).inv()).as_rotvec()
        delta = np.r_[xyz - current['xyz'],angle]
        advance(np.clip(delta/native.output_max,-1,1))

    original_dim = env.env.action_dim
    try:
        limit = PLAN['joint_delta_limit_rad']
        robot.controller_config = dict(load_controller_config(default_controller='JOINT_POSITION'),
                                       kp=PLAN['joint_kp'],output_min=-limit,output_max=limit)
        robot._load_controller()
        env.env._action_dim = robot.action_dim
        source = np.array(rows[-1]['tool']['joints'])
        target = np.array(dest['joints'])
        remaining = length - len(rows)
        ramp = max(1,round(remaining*PLAN['ramp_fraction']))
        for i in range(1,remaining+1):
            weight = (1 - np.cos(np.pi*min(i/ramp,1)))/2
            ref = source + weight*(target-source)
            measured = env.sim.data.qpos[robot._ref_joint_pos_indexes]
            advance(np.clip((ref-measured)/limit,-1,1))
    finally:
        robot.controller_config, robot.controller = config, native
        env.env._action_dim = original_dim
        native.update(force=True)
        native.reset_goal()
    return dict(start=start,rows=rows,actions=actions)


def restore(env, scene, arm, out):
    common = posture(env)
    prefix(env,scene.stove,arm,PLAN['donor_tick'],out)
    return common


def drawer_environment(arm):
    return environment(arm+'-160')


def record_prep(out, arm, mode, length, *, open_env=drawer_environment, restore_prefix=restore, prepare_fn=prepare,
                scene_type=Scene, prompt=STOVE['prompt']):
    env = open_env(arm)
    try:
        scene = scene_type(env)
        common = restore_prefix(env,scene,arm,out)
        initial = state_hash(capture_state(env))
        tape = prepare_fn(env,scene,common,mode,length)
        _, start = observe(env,out,False,prompt)
        return dict(arm=arm,mode=mode,length=length,common=common,donor_physics=initial,
                    handoff=scene.read(),first=start,geometry=scene.stove.geometry,**tape)
    finally:
        env.close()

def qualify(out):
    from OpenGL import GL
    import mujoco
    from verify_stove_pose import geometry
    folder = out/'preparation'
    folder.mkdir(exist_ok=True)
    trials = []
    for length in PLAN['lead_options']:
        tapes = {}
        for arm in PLAN['arms']:
            for mode in ('wait','pose'):
                name = arm+'-'+mode
                tape = record_prep(out,arm,mode,length)
                save(folder/f'{name}-{length}.json',tape)
                tapes[name] = tape
        assessment = geometry(tapes)
        trials.append(dict(length=length,**assessment))
        print('lead',length,'passed',assessment['passed'],flush=True)
        if assessment['passed']:
            break
    for arm in PLAN['arms']:
        save(folder/f'{arm}-immediate-0.json',record_prep(out,arm,'immediate',0))
    write = dict(attempts=trials,lead=length if trials[-1]['passed'] else None,mujoco=mujoco.__version__)
    save(out/'qualification.json',write)
    return write

def trajectory(out, entry, replay=False, *, open_env=drawer_environment, restore_prefix=restore, prepare_fn=prepare,
               scene_type=Scene, first_images=None, view_factory=None):
    arm, mode, name = entry['arm'],entry['mode'],entry['session']
    length = entry['lead']
    reference = read(out/'preparation'/f'{arm}-{mode}-{length}.json')
    env = open_env(arm)
    client = None
    try:
        scene = scene_type(env)
        common = restore_prefix(env,scene,arm,out)
        assert common == reference['common'] and state_hash(capture_state(env)) == reference['donor_physics']
        prep = prepare_fn(env,scene,common,mode,length)
        assert all(value == reference[key] for key,value in prep.items())
        views = view_factory(env, scene) if view_factory is not None else None
        path = out/'paths'/(name+'.json')
        saved = read(path) if replay else None
        if not replay:
            client = client_for(name)
        data = dict(session=name,arm=arm,mode=mode,lead=length,seed=entry['key'],block=entry['block'],
                    queries=[],rows=[])
        changed = []
        period = PLAN['replan_every']
        for tick in range(length, entry.get('horizon',PLAN['budgets'][-1]), period):
            query, sample = observe(env,out,tick==length and not replay,entry.get('source',STOVE['prompt']))
            if tick == length:
                assert (sample['physics'],sample['state']) == (reference['first']['physics'],reference['first']['state'])
                assert scene.read() == reference['handoff']
                if first_images is not None and not replay:
                    assert sample['live'] == reference['first']['live']
                    sample['sent'] = first_images
                    for camera, signature in first_images.items():
                        query[camera] = frame(out, signature)
            if views is not None:
                views.apply((tick-length)//period, query, sample, data['rows'])
            if replay:
                old = saved['queries'][(tick-length)//period]
                assert (tick,sample['physics'],sample['state']) == (old['tick'],old['physics'],old['state'])
                # Count this query once if either native or delivered pixels changed.
                rendered_difference = views is not None and views.compare_replay(sample, old)
                if sample['live'] != old['live'] or rendered_difference:
                    changed.append(tick)
                commands = [r['action'] for r in saved['rows'][tick-length:tick-length+period]]
            else:
                reply = np.asarray(client.infer(query)['actions'],dtype='<f8')
                assert reply.shape == (10,7) and np.isfinite(reply).all()
                data['queries'].append(dict(tick=tick,reply=reply.tolist(),**sample))
                commands = reply[:period].tolist()
            for action in commands:
                env.step(action)
                row = dict(action=action,**scene.policy_row())
                if replay:
                    assert row == saved['rows'][len(data['rows'])], (name,tick)
                data['rows'].append(row)
        final = state_hash(capture_state(env))
        if replay:
            assert final == saved['final_physics']
            return dict(session=name,prefix_controls=entry.get('prefix_controls',PLAN['donor_tick']),lead=length,policy_controls=len(data['rows']),
                        observations=len(saved['queries']),changed_rgb_ticks=changed,final_physics=final)
        save(path,dict(data,final_physics=final))
    finally:
        if client is not None:
            client.close()
        env.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('out',type=Path)
    parser.add_argument('stage',choices=['qualify','run','replay'])
    parser.add_argument('session',nargs='?')
    args = parser.parse_args()
    if args.stage == 'qualify':
        qualify(args.out)
    else:
        session = read(args.out/'sessions.json')[args.session]
        report = trajectory(args.out,session,replay=args.stage=='replay')
        if report:
            print(json.dumps(report),flush=True)


