"""Run one native R8 development trajectory, preserving the two-command common prefix."""
import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import random

import mujoco
import numpy as np
from PIL import Image
from resteer import tasks
from resteer.client import PolicyClient
from resteer.sim import libero as sim


HERE = Path(__file__).resolve().parent
SPEC = json.loads((HERE/'ATOMIC_CONTROL.json').read_bytes())
SITE = 'wooden_cabinet_1_top_side'
BODIES = {'bowl': 'akita_black_bowl_1', 'plate': 'plate_1', 'cabinet': 'wooden_cabinet_1'}


def digest(array):
    return hashlib.sha256(np.ascontiguousarray(array).tobytes()).hexdigest()


def capture_state(env):
    e = env.env
    model, data = e.sim.model._model, e.sim.data._data
    kind = mujoco.mjtState.mjSTATE_INTEGRATION
    values = np.empty(mujoco.mj_stateSize(model, kind), dtype=np.float64)
    mujoco.mj_getState(model, data, values, kind)
    controller = e.robots[0].controller
    assert controller.interpolator_pos is None and controller.interpolator_ori is None
    fields = ('goal_pos', 'goal_ori', 'relative_ori', 'ori_ref', 'initial_joint', 'initial_ee_pos',
              'initial_ee_ori_mat', 'ee_pos', 'ee_ori_mat', 'ee_pos_vel', 'ee_ori_vel', 'joint_pos',
              'joint_vel', 'J_pos', 'J_ori', 'mass_matrix', 'torques', 'new_update')
    dyn = {k: np.asarray(getattr(controller,k)).tolist() for k in fields}
    n = np.random.get_state()
    rng = [n[0], n[1].tolist(), *n[2:], random.getstate()]
    return {'integration_state': values.tolist(), 'controller': dyn, 'control_tick': int(e.timestep),
            'gripper_command_state': e.robots[0].gripper.current_action.tolist(),
            'rng_sha256': hashlib.sha256(json.dumps(rng).encode()).hexdigest()}


def geom_info(env):
    e = env.env
    names = {k: list(e.get_object(v).contact_geoms) for k,v in BODIES.items()}
    names['gripper'] = list(e.robots[0].gripper.contact_geoms)
    return {'contact_geoms': {k: {name:int(e.sim.model.geom_name2id(name)) for name in v} for k,v in names.items()},
            'cabinet_site_half_size': np.asarray(e.object_sites_dict[SITE].size).tolist()}


def measurements(env, groups, success):
    e = env.env
    d = e.sim.data
    contacts = d._data.contact
    # Keep the unordered unique MuJoCo geom pairs involving the bowl.
    pairs = {tuple(sorted((int(a),int(b)))) for a,b in zip(contacts.geom1,contacts.geom2)
             if a in groups['bowl'] or b in groups['bowl']}
    return {'bowl_contacts': sorted(pairs),
            'bowl_xyz': d.body_xpos[e.obj_body_id[BODIES['bowl']]].tolist(),
            'plate_xyz': d.body_xpos[e.obj_body_id[BODIES['plate']]].tolist(),
            'cabinet_site_xyz': d.get_site_xpos(SITE).tolist(), 'cabinet_site_mat': d.get_site_xmat(SITE).tolist(),
            'goals': {arm['arm']: bool(success[arm['goal_key']]) for arm in SPEC['arms']}}


def policy_observation(out, env, prompt, save_frames=True):
    sim.set_camera_rendering(env, True)
    obs = sim.get_observation(env)
    sim.set_camera_rendering(env, False)
    query = sim.policy_input(obs, prompt)
    state = query['observation/state']
    assert state.shape == (8,) and np.isfinite(state).all()
    images = {}
    for key in ('observation/image','observation/wrist_image'):
        img = query[key]
        assert img.shape == (224,224,3) and img.dtype == np.uint8 and np.ptp(img) > 0
        sha = digest(img)
        path = out/'frames'/(sha+'.png')
        if save_frames and not path.exists():
            Image.fromarray(img).save(path)
        images[key] = sha
    return query, {'rgb_sha256': images, 'proprioception': state.tolist()}


def rollout(out, arm, rep):
    from OpenGL import GL

    seed, switch = SPEC['environment_seed'], SPEC['shared_source_controls']
    source, target = tasks.get_task(SPEC['source_task_id']), tasks.get_task(arm['task_id'])
    assert source.prompt == SPEC['source_prompt'] and target.prompt == arm['prompt'] and target.goal_keys == (arm['goal_key'],)
    random.seed(seed)
    np.random.seed(seed)
    client = PolicyClient('127.0.0.1',8000)
    env = sim.make_env(seed=seed)
    rec = {'arm': arm['arm'], 'repeat': rep, 'status': 'STARTED', 'queries': [], 'rows': [], 'snapshots': {}}
    try:
        sim.reset(env, num_warmup_steps=SPEC['warmup_controls'])
        e = env.env
        rec['geometry'] = geom_info(env)
        rec['control_hz'] = e.control_freq
        rec['renderer'] = GL.glGetString(GL.GL_RENDERER).decode()
        assert 'NVIDIA' in rec['renderer']
        groups = {k:set(g.values()) for k,g in rec['geometry']['contact_geoms'].items()}
        rec['initial_readout'] = measurements(env, groups, e._check_success(return_success_dict=True))
        sim.set_camera_rendering(env, False)
        queue = collections.deque()
        for t in range(SPEC['policy_controls_per_path']):
            if t == switch:
                rec['discarded_at_switch'] = len(queue)
                queue.clear()
            if not queue:
                prompt = source.prompt if t < switch else target.prompt
                query, info = policy_observation(out, env, prompt)
                if t in (0,switch):
                    rec['snapshots'][str(t)] = capture_state(env)
                reply = np.asarray(client.infer(query)['actions'])
                assert reply.shape == (SPEC['action_horizon'],SPEC['action_dim']) and np.isfinite(reply).all()
                rec['queries'].append(dict(info, completed_controls=t, prompt=prompt, reply=reply.tolist()))
                queue.extend(enumerate(reply[:SPEC['replan_controls']]))
            index, action = queue.popleft()
            _, success = sim.step(env, action)
            rec['rows'].append({'tick':t+1,'query':len(rec['queries'])-1,'index':index,
                                'dispatched':action.tolist(), **measurements(env, groups, success)})
        rec['final_state'] = capture_state(env)
        _, rec['final_observation'] = policy_observation(out, env, target.prompt)
        assert len(rec['queries']) == SPEC['queries_per_path']
        rec['status'] = 'COMPLETED'
    finally:
        (out/f'{arm["arm"]}_{rep}.json').write_text(json.dumps(rec,allow_nan=False,separators=(',',':'))+'\n')
        env.close()
        client.close()


if __name__ == '__main__':
    assert Path('/.dockerenv').is_file() and os.environ['PYTHONHASHSEED'] == str(SPEC['python_hash_seed'])
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('arm', choices=[a['arm'] for a in SPEC['arms']])
    parser.add_argument('repeat', type=int, choices=range(1,SPEC['repetitions']+1))
    args = parser.parse_args()
    assert not (args.output/f'{args.arm}_{args.repeat}.json').exists()
    rollout(args.output,next(a for a in SPEC['arms'] if a['arm']==args.arm),args.repeat)
