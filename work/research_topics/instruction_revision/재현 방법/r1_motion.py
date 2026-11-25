"""Measure the R1 bottle in a read-only kinematics copy and run the two native continuations."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import random

import mujoco
import numpy as np
from OpenGL import GL
from PIL import Image
from resteer.client import PolicyClient
from resteer.sim import libero as sim

from atomic_control import capture_state, geom_info, measurements, policy_observation


PACKET = Path(__file__).resolve().parent
SPEC = json.loads((PACKET/'R1_CONTROL.json').read_text())


def write(path, obj):
    path.write_text(json.dumps(obj, allow_nan=False, separators=(',', ':')) + '\n')


class BottleObserver:
    def __init__(self, env):
        e = env.env
        self.model, self.live = e.sim.model._model, e.sim.data._data
        self.scratch = mujoco.MjData(self.model)
        obj = e.get_object(SPEC['protected_body'])
        self.body = int(e.obj_body_id[SPEC['protected_body']])
        joint = e.sim.model.joint_name2id(obj.joints[0])
        self.start = int(self.model.jnt_qposadr[joint])
        assert self.model.jnt_type[joint] == mujoco.mjtJoint.mjJNT_FREE
        assert self.model.jnt_bodyid[joint] == self.body and self.model.body_parentid[self.body] == 0
        self.bottle = {e.sim.model.geom_name2id(n) for n in obj.contact_geoms}
        robot = e.robots[0].robot_model
        robot_root = e.sim.model.body_name2id(robot.root_body)
        def on_robot(body):
            while body and body != robot_root:
                body = self.model.body_parentid[body]
            return body == robot_root
        self.robot = {i for i,b in enumerate(self.model.geom_bodyid) if on_robot(b)}
        self.geometry = {'bottle':sorted(self.bottle), 'robot':sorted(self.robot),
                         'body_name':e.sim.model.body_id2name(self.body), 'body_id':self.body,
                         'world_parent':0, 'joint_name':obj.joints[0], 'qpos_address':self.start,
                         'robot_root':robot.root_body}
        assert self.bottle and self.robot and not self.bottle.intersection(self.robot)

    def pose(self):
        self.scratch.qpos[:] = self.live.qpos
        mujoco.mj_kinematics(self.model, self.scratch)
        return {'xyz':self.scratch.xpos[self.body].tolist(), 'wxyz':self.scratch.xquat[self.body].tolist(),
                'rotation':self.scratch.xmat[self.body].reshape(3,3).tolist(),
                'free_joint':self.scratch.qpos[self.start:self.start+7].tolist()}

    def contacts(self):
        pairs = zip(self.live.contact.geom1,self.live.contact.geom2)
        return sorted({tuple(sorted((int(a),int(b)))) for a,b in pairs if a in self.bottle or b in self.bottle})


def pose_error(ref, pose):
    position = np.linalg.norm(np.asarray(pose['xyz'])-ref['xyz'])
    q, r = np.asarray(pose['wxyz']), np.asarray(ref['wxyz'])
    cosine = np.dot(q/np.linalg.norm(q),r/np.linalg.norm(r))
    return np.array([position, 2*math.acos(np.clip(abs(cosine),0,1))])


def reset(seed, bottle_xy=None, edit_record=None):
    random.seed(seed)
    np.random.seed(seed)
    env = sim.make_env(seed=seed)
    if bottle_xy is None:
        sim.reset(env,num_warmup_steps=SPEC['warmup_controls'])
    else:
        sim.reset(env,num_warmup_steps=0)
        observer = BottleObserver(env)
        xy = observer.live.qpos[observer.start:observer.start+2]
        assert np.array_equal(xy, bottle_xy['native'])
        if edit_record is not None:
            edit_record['before'] = capture_state(env)
            edit_record['qpos_address'] = observer.start
            edit_record['nq'] = observer.model.nq
            edit_record['nv'] = observer.model.nv
            assert np.array_equal(edit_record['before']['integration_state'][1:1+observer.model.nq], observer.live.qpos)
        xy[:] = bottle_xy['target']
        if edit_record is not None:
            edit_record['after'] = capture_state(env)
        mujoco.mj_forward(observer.model,observer.live)
        for _ in range(SPEC['warmup_controls']):
            env.step(np.zeros(7))
    assert env.env.control_freq == 20 and b'NVIDIA' in GL.glGetString(GL.GL_RENDERER)
    sim.set_camera_rendering(env,False)
    return env


def calibration_trial(seed, include_layout=False, bottle_xy=None):
    env = reset(seed, bottle_xy)
    try:
        obs = BottleObserver(env)
        reference = obs.pose()
        layout = {}
        if include_layout:
            e = env.env
            layout['bowl_xyz'] = e.sim.data.body_xpos[e.obj_body_id['akita_black_bowl_1']].tolist()
        if bottle_xy is not None:
            from bottle_xy_sim import support_sample
            bowl = set(geom_info(env)['contact_geoms']['bowl'].values())
            layout['table_geom'] = int(env.env.sim.model.geom_name2id('table_collision'))
            layout['passive_support'] = [support_sample(env, obs, bowl)]
        poses = [reference]
        for _ in range(SPEC['horizon']):
            sim.step(env,np.zeros(7))
            poses.append(obs.pose())
            if bottle_xy is not None:
                layout['passive_support'].append(support_sample(env, obs, bowl))
        # Apply each calibration displacement to the original free joint after the drift run has ended.
        settings = SPEC['calibration']
        axis = np.asarray(settings['world_rotation_axis'],dtype=float)
        axis /= np.linalg.norm(axis)
        delta = np.empty(4)
        mujoco.mju_axisAngle2Quat(delta,axis,math.radians(settings['rotation_degrees']))
        rotated = np.empty(4)
        mujoco.mju_mulQuat(rotated,delta,np.asarray(reference['wxyz']))
        probes = {}
        for name in ('translation','rotation','sign_flip'):
            free = np.array(reference['free_joint'])
            if name == 'translation':
                free[:3] += settings['translation_m']
            elif name == 'rotation':
                free[3:] = rotated
            else:
                free[3:] *= -1
            obs.live.qpos[obs.start:obs.start+7] = free
            mujoco.mj_forward(obs.model,obs.live)
            probes[name] = obs.pose()
        return {'seed':seed,'geometry':obs.geometry,'drift':poses,'probes':probes,**layout,
                'control_hz':env.env.control_freq,'renderer':GL.glGetString(GL.GL_RENDERER).decode()}
    finally:
        env.close()


def calibrate(out):
    fit = calibration_trial(SPEC['calibration_seed'])
    def errors(trial):
        ref = trial['drift'][0]
        drift = np.max([pose_error(ref,s) for s in trial['drift']],axis=0)
        probes = {k:pose_error(ref,v) for k,v in trial['probes'].items()}
        return drift,probes
    drift, positives = errors(fit)
    known = np.array([positives['translation'][0],positives['rotation'][1]])
    thresholds = (drift+known)/2
    check = calibration_trial(SPEC['scene_seed'])
    for trial in (fit,check):
        maximum, probes = errors(trial)
        assert (maximum < thresholds).all()
        assert np.allclose(probes['translation'],[np.linalg.norm(SPEC['calibration']['translation_m']),0],atol=1e-7,rtol=0)
        assert np.allclose(probes['rotation'],[0,math.radians(SPEC['calibration']['rotation_degrees'])],atol=1e-7,rtol=0)
        assert (probes['translation'] > thresholds).tolist() == [True,False]
        assert (probes['rotation'] > thresholds).tolist() == [False,True]
        assert np.max(probes['sign_flip']) < 1e-7
    write(out,{'status':'FROZEN','fit':fit,'check':check,'translation_m':thresholds[0],'rotation_rad':thresholds[1]})
    print('Frozen tolerance (m, rad)',thresholds.tolist(),flush=True)


def rollout(out, arm, repeat, prefix_only=False):
    protocol_file = out/'protocol.json'
    spec = json.loads(protocol_file.read_bytes()) if protocol_file.exists() else SPEC
    if arm not in spec['arms']:
        raise ValueError(f'Unknown arm {arm} in this protocol')
    reference = None
    if 'source_replay' in spec:
        replay = spec['source_replay']
        source = (out if 'layout_study' in spec else PACKET/spec['reference']['archive'])/replay['path']
        payload = source.read_bytes()
        assert hashlib.sha256(payload).hexdigest() == replay['file_sha256']
        reference = json.loads(payload)
        assert replay['controls'] == spec['switch'] and reference['queries'][0]['prompt'] == spec['source_prompt']
    donor = None
    if 'branch_donors' in spec:
        donor_name = spec['branch_donors'][arm]
        payload = (PACKET/spec['reference']['archive']/donor_name).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == spec['reference']['files'][donor_name]
        donor = json.loads(payload)
        boundary = spec['intervention_tick']
        anchor = json.loads((out/'donor_states.json').read_bytes())[donor_name]
        assert anchor['controls'] == boundary
    env = reset(spec['scene_seed'], spec.get('bottle_xy'))
    session = os.environ.get('CAMERA_STUDY_SESSION') if 'camera_factorial' in spec else None
    client = PolicyClient(f'ws://127.0.0.1:8000/{session}', None) if session else PolicyClient('127.0.0.1',8000)
    try:
        observer = BottleObserver(env)
        geometry = geom_info(env)
        groups = {k:set(v.values()) for k,v in geometry['contact_geoms'].items()}
        assert groups['gripper'] <= observer.robot
        def sample(success):
            return dict(measurements(env,groups,success), bottle_pose=observer.pose(), bottle_contacts=observer.contacts())
        data = {'arm':arm,'repeat':repeat,'status':'STARTED','geometry':geometry,'bottle_geometry':observer.geometry,
                'renderer':GL.glGetString(GL.GL_RENDERER).decode(),'control_hz':env.env.control_freq,
                'initial_readout':sample(env.env._check_success(return_success_dict=True)),
                'queries':[],'rows':[],'snapshots':{}}
        rack = None
        if spec['case']=='R4':
            from r4_rack import RackObserver
            rack = RackObserver(env,spec)
            data['rack'] = {'geometry':rack.geometry,'samples':[rack.sample(env.env._check_success(return_success_dict=True))]}
        switch, period, horizon = spec['switch'],spec['replan_controls'],spec['horizon']
        if donor is not None:
            data['donor_prefix'] = {'file':donor_name,'sha256':spec['reference']['files'][donor_name],'controls':boundary}
            assert data['geometry'] == donor['geometry'] and data['bottle_geometry'] == donor['bottle_geometry']
            assert json.loads(json.dumps(data['initial_readout'])) == donor['initial_readout']
        for query_index,start in enumerate([0,*range(switch,horizon,period)]):
            prompt = spec['source_prompt'] if start == 0 or prefix_only else spec['arms'][arm]
            if donor is not None and start < boundary:
                prompt = donor['queries'][query_index]['prompt']
            query, input_info = policy_observation(out,env,prompt,save_frames='camera_factorial' not in spec or start <= switch)
            assert set(query) == {'observation/image','observation/wrist_image','observation/state','prompt'}
            if start in (0,switch) or (donor is not None and start == boundary):
                data['snapshots'][str(start)] = capture_state(env)
                if reference is not None:
                    saved = reference['queries'][query_index]
                    assert data['snapshots'][str(start)] == reference['snapshots'][str(start)]
                    assert all(value == saved[k] for k,value in input_info.items())
                    assert json.loads(json.dumps(data['rows'])) == reference['rows'][:start]
            if donor is not None and start <= boundary:
                saved = donor['queries'][query_index]
                assert saved['completed_controls'] == start and all(v == saved[k] for k,v in input_info.items())
                if start in (0,switch):
                    assert data['snapshots'][str(start)] == donor['snapshots'][str(start)]
                if start == boundary:
                    assert data['snapshots'][str(start)] == anchor['state']
                    assert json.loads(json.dumps(data['rows'])) == donor['rows'][:boundary]
            if prefix_only and start == switch:
                data['queries'].append(dict(input_info, completed_controls=start))
                data['status'] = 'PREFIX_ONLY'
                write(out/'prefix.json',data)
                return
            if 'first_view' in spec:
                live = input_info['rgb_sha256']
                data.setdefault('live_camera_sha256', []).append(live)
                assigned = spec['first_view']['rgb_sha256'] if start == switch else live
                if start == switch:
                    for camera, digest in assigned.items():
                        with Image.open(out/'frames'/f'{digest}.png') as img:
                            query[camera] = np.array(img)
                        assert query[camera].dtype == np.uint8 and query[camera].shape == (224,224,3)
                sent = {camera:hashlib.sha256(query[camera].tobytes()).hexdigest() for camera in live}
                assert sent == assigned and query['prompt'] == prompt
                assert query['observation/state'].tolist() == input_info['proprioception']
                input_info = dict(input_info, rgb_sha256=sent)
            actions = np.asarray(client.infer(query)['actions'])
            assert actions.shape == (10,7) and np.isfinite(actions).all()
            data['queries'].append(dict(input_info,completed_controls=start,prompt=prompt,reply=actions.tolist()))
            count = switch if start == 0 else min(period,horizon-start)
            if start == 0:
                data['discarded_at_switch'] = period-count
                if reference is not None:
                    # Keep the live reply above. Only the archived queue owns the two common controls.
                    saved = reference['queries'][0]['reply']
                    data['prefix_replay'] = {'path':replay['path'],'file_sha256':replay['file_sha256'],
                                             'controls':count,'reference_reply':saved}
                    actions = np.asarray(saved)
            if donor is not None and start < boundary:
                assert start+count <= boundary
                actions = np.asarray([row['dispatched'] for row in donor['rows'][start:start+count]])
            for index,action in enumerate(actions[:count]):
                _,success = sim.step(env,action)
                data['rows'].append(dict(sample(success),tick=start+index+1,query=query_index,
                                         index=index,dispatched=action.tolist()))
                if rack is not None:
                    data['rack']['samples'].append(rack.sample(success))
        data['final_state'] = capture_state(env)
        _,data['final_observation'] = policy_observation(out,env,spec['arms'][arm],save_frames='camera_factorial' not in spec)
        data['status'] = 'COMPLETED'
        write(out/f'{arm}_{repeat}.json',data)
    finally:
        env.close()
        client.close()


if __name__ == '__main__':
    assert Path('/.dockerenv').exists() and os.environ['PYTHONHASHSEED'] == str(SPEC['python_hash_seed'])
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['calibrate','rollout','prefix'])
    parser.add_argument('out',type=Path)
    parser.add_argument('arm',nargs='?')
    parser.add_argument('repeat',nargs='?',type=int,choices=(1,2))
    args = parser.parse_args()
    if args.mode == 'calibrate':
        assert not args.out.exists()
        calibrate(args.out)
    else:
        assert args.arm and args.repeat and not (args.out/f'{args.arm}_{args.repeat}.json').exists()
        if args.mode == 'prefix':
            assert not (args.out/'prefix.json').exists()
        rollout(args.out,args.arm,args.repeat,prefix_only=args.mode=='prefix')
