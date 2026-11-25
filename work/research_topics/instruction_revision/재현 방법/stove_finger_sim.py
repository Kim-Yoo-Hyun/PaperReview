"""Hold each measured finger position with the native servos during the original arm wait."""
import argparse
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np

from atomic_control import capture_state
from drawer_sim import DESIGN as DRAWER, observe, save, state_hash
from stove_layouts_sim import layout_env
from stove_pose_sim import posture, prepare, record_prep, trajectory
from verify_atomic import PACKET, read
from verify_stove_fingers import BASE, DESIGN, digest, physical_metrics


def environment(arm):
    assert arm in DESIGN['arms']
    return layout_env(DESIGN['layout'],'stove')


def restore(env, scene, arm, out, *, donors_file=None):
    source = read(PACKET/(donors_file or DESIGN['donors']))[arm]
    common = posture(env)
    assert state_hash(capture_state(env)) == source['initial']
    assert digest([common,scene.stove.geometry,scene.stove.sample()]) == source['start']
    measurements, observations = [], []
    assert len(source['actions']) == BASE['drawer_horizon']
    for tick,action in enumerate(source['actions']):
        if tick % BASE['period'] == 0:
            _,sample = observe(env,out,False,DRAWER['prompt'])
            observations.append([tick,sample['physics'],sample['state']])
        env.step(action)
        measurements.append(scene.stove.sample())
    assert digest(measurements) == source['measurements'] and digest(observations) == source['observations']
    assert state_hash(capture_state(env)) == source['final']
    return common


def prepare_with_fingers(env, scene, common, mode, length):
    if mode != 'finger_hold':
        return prepare(env,scene,common,mode,length)
    robot = env.robots[0]
    model = env.sim.model
    gripper = robot.gripper
    ids = [model.actuator_name2id(a) for a in gripper.actuators]
    joints = model.actuator_trnid[ids,0]
    assert len(ids) == 2 and np.array_equal(model.jnt_qposadr[joints], robot._ref_gripper_joint_pos_indexes)
    assert np.all(model.actuator_trntype[ids] == 0) and np.all(model.actuator_gear[ids,0] == 1)
    bounds = model.actuator_ctrlrange[ids]
    target = env.sim.data.qpos[robot._ref_gripper_joint_pos_indexes].copy()
    normalized = (target - bounds.mean(axis=1)) / (np.diff(bounds).ravel()/2)
    assert np.all(np.abs(normalized) <= 1)
    # Robosuite integrates the sign of the gripper channel. Zero holds these
    # actuator targets through every physics substep and into the native handoff.
    gripper.current_action = normalized.copy()
    actions, applied = [], []

    def step(action):
        command = [*action[:-1], 0.0]
        env.step(command)
        actions.append(command)
        applied.append(env.sim.data.ctrl[ids].tolist())

    # Route only the gripper channel of the frozen arm preparation through step().
    wait_env = SimpleNamespace(sim=env.sim, robots=env.robots, env=env.env, step=step)
    tape = prepare(wait_env,scene,common,'wait',length)
    assert [a[:-1] for a in actions] == [a[:-1] for a in tape['actions']]
    assert np.array_equal(gripper.current_action,normalized)
    tape['actions'] = actions
    tape['finger_actuators'] = dict(names=list(gripper.actuators), ranges=bounds.tolist(),
                                    normalized_targets=normalized.tolist(), applied_targets=applied)
    return tape


def qualify(out):
    import mujoco
    from OpenGL import GL
    for arm in DESIGN['arms']:
        for mode in DESIGN['modes']:
            lead = 0 if mode == 'immediate' else BASE['lead']
            tape = record_prep(out,arm,mode,lead,open_env=environment,restore_prefix=restore,
                               prepare_fn=prepare_with_fingers)
            save(out/'preparation'/f'{arm}-{mode}-{lead}.json',tape)
    endpoints = physical_metrics(out,read(PACKET/DESIGN['donors']))
    env = environment(DESIGN['arms'][0])
    try:
        renderer = GL.glGetString(GL.GL_RENDERER).decode()
        assert 'NVIDIA' in renderer
    finally:
        env.close()
    save(out/'qualification.json',dict(endpoints=endpoints,renderer=renderer,mujoco=mujoco.__version__))
    for arm,m in endpoints.items():
        print(arm,'finger peak (mm)',m['finger_hold']['peak_finger_from_donor_mm'],
              'qualified',m['finger_hold']['passed_all_steps'],flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('out',type=Path)
    parser.add_argument('stage',choices=['prepare','run','replay'])
    parser.add_argument('session',nargs='?')
    args = parser.parse_args()
    if args.stage == 'prepare':
        qualify(args.out)
    else:
        entry = read(args.out/'sessions.json')[args.session]
        report = trajectory(args.out,entry,replay=args.stage=='replay',open_env=environment,
                            restore_prefix=restore,prepare_fn=prepare_with_fingers)
        if report:
            print(json.dumps(report))
