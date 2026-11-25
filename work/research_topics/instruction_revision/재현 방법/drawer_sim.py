"""Execute or physically replay a fixed-horizon LIBERO-Goal drawer trajectory."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import random

import numpy as np
from PIL import Image
from resteer.client import PolicyClient
from resteer.sim import libero as sim

from atomic_control import capture_state, digest
from verify_atomic import CAMERAS, PACKET, read


ASSETS = PACKET / 'drawer'
DESIGN = read(ASSETS / 'protocol.json')


def state_hash(value):
    raw = json.dumps(value, separators=(',', ':'), sort_keys=True, allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, separators=(',', ':'), allow_nan=False) + '\n')
    tmp.replace(path)


def frame(out, signature):
    with Image.open(out / 'frames' / (signature + '.png')) as source:
        pixels = np.array(source)
    assert pixels.dtype == np.uint8 and pixels.shape == (224, 224, 3) and digest(pixels) == signature
    return pixels


def observe(env, out, keep, prompt=DESIGN['prompt']):
    sim.set_camera_rendering(env, True)
    obs = sim.get_observation(env)
    sim.set_camera_rendering(env, False)
    query = sim.policy_input(obs, prompt)
    images = {cam: digest(query[cam]) for cam in CAMERAS}
    if keep:
        for cam, signature in images.items():
            path = out / 'frames' / (signature + '.png')
            if not path.is_file():
                tmp = path.with_suffix(f'.{os.getpid()}.png')
                Image.fromarray(query[cam]).save(tmp)
                tmp.replace(path)
    return query, dict(live=images, state=query['observation/state'].tolist(), physics=state_hash(capture_state(env)))


class Drawer:
    def __init__(self, env):
        self.env = env
        m = env.sim.model
        names = ('top', 'middle', 'bottom')
        self.addresses = [int(m.jnt_qposadr[m.joint_name2id(f'wooden_cabinet_1_{n}_level')]) for n in names]
        target = m.body_name2id('wooden_cabinet_1_cabinet_middle')
        self.drawer = set(np.flatnonzero(m.geom_bodyid == target).tolist())
        self.gripper = {int(m.geom_name2id(v)) for v in env.robots[0].gripper.contact_geoms}
        self.geometry = dict(joints=list(names), qpos_indices=self.addresses,
                             drawer={i: m.geom_id2name(i) for i in sorted(self.drawer)},
                             gripper={i: m.geom_id2name(i) for i in sorted(self.gripper)})
        assert self.drawer and self.gripper and self.drawer.isdisjoint(self.gripper)

    def sample(self):
        data = self.env.sim.data
        pairs = set()
        for a, b in zip(data._data.contact.geom1, data._data.contact.geom2):
            if a in self.gripper and b not in self.gripper:
                pairs.add((int(a), int(b)))
            if b in self.gripper and a not in self.gripper:
                pairs.add((int(b), int(a)))
        return dict(joints=data.qpos[self.addresses].tolist(), gripper_pairs=sorted(pairs),
                    target_contact=any(b in self.drawer for _, b in pairs), goal=bool(self.env.check_success()))


def reset(start, *, task_file=ASSETS/'task.bddl', starts_file=ASSETS/'starts.json', goal=DESIGN['goal']):
    seed = DESIGN['environment_seed']
    random.seed(seed)
    np.random.seed(seed)
    env = sim.OffScreenRenderEnv(bddl_file_name=str(task_file), camera_heights=512, camera_widths=512)
    env.seed(seed)
    env.reset()
    state = np.array(read(starts_file)[str(start)], dtype=np.float64)
    assert state.shape == env.get_sim_state().shape and env.env.parsed_problem['goal_state'] == [goal]
    env.set_init_state(state)
    sim.set_camera_rendering(env, False)
    for _ in range(DESIGN['warmup_controls']):
        env.step(DESIGN['warmup_action'])
    return env


def tape(out, name):
    return read(out / 'paths' / (name + '.json'))


def anchor_name(start):
    return f'direct-1-{start}'


def client_for(name):
    return PolicyClient(f'ws://127.0.0.1:8000/{name}', None)


def probe(out, name, start):
    # Replay the archived observations, with the native key stream starting from zero.
    source = tape(out, anchor_name(start))
    client = client_for(name)
    try:
        for row in source['queries']:
            obs = {cam: frame(out, row['live'][cam]) for cam in CAMERAS}
            obs.update({'observation/state': np.array(row['state']), 'prompt': DESIGN['prompt']})
            client.infer(obs)
    finally:
        client.close()


def rollout(out, mode, name, start, pair=None, arm=None, reference=None, source_root=None):
    period, horizon = DESIGN['replan_every'], DESIGN['horizon']
    source = tape(source_root or out, reference or anchor_name(start)) if mode != 'direct' else None
    online = mode in ('direct', 'branch')
    boundary = pair['tick'] if pair else horizon
    env = reset(start)
    client = client_for(name) if online else None
    try:
        physical = Drawer(env)
        initial = physical.sample()
        assert not initial['goal'] and not initial['target_contact']
        data = dict(name=name, start=start, mode=mode, initial=initial, geometry=physical.geometry,
                    initial_physics=state_hash(capture_state(env)), queries=[], rows=[])
        if pair:
            data.update(pair=pair['id'], arm=arm, tick=boundary)
        for tick in range(0, horizon, period):
            query, record = observe(env, out, mode in ('survey', 'direct'))
            qi = tick // period
            record['tick'] = tick
            if source is not None and (tick <= boundary or mode == 'replay'):
                saved = source['queries'][qi]
                assert (record['physics'], record['state']) == (saved['physics'], saved['state']), (name, tick)
            if online:
                sent = record['live']
                if pair and tick == boundary:
                    sent = pair[arm]
                    for cam in CAMERAS:
                        query[cam] = frame(out, sent[cam])
                actions = np.asarray(client.infer(query)['actions'], dtype='<f8')
                assert actions.shape == (10, 7) and np.isfinite(actions).all()
                record.update(sent=sent, reply=actions.tolist())
            if source is not None and (tick < boundary or not online):
                actions = np.array([r['action'] for r in source['rows'][tick:tick + period]])
            data['queries'].append(record)
            for action in actions[:period]:
                env.step(action.tolist())
                data['rows'].append(dict(action=action.tolist(), **physical.sample()))
        data['final_physics'] = state_hash(capture_state(env))
        if mode in ('survey', 'replay'):
            assert json.loads(json.dumps(data['rows'])) == source['rows'] and data['final_physics'] == source['final_physics']
            # Identical saved-command physics and contacts were checked at every control.
            report = dict(name=name, reference=source['name'], start=start, controls=len(data['rows']),
                          queries=data['queries'], final_physics=data['final_physics'])
            if mode == 'survey':
                save(out / 'survey' / (name + '.json'), report)
            else:
                return dict(name=reference, controls=len(data['rows']), queries=len(data['queries']),
                            changed_live_query_ticks=[r['tick'] for r,s in zip(data['queries'],source['queries']) if r['live'] != s['live']])
        else:
            save(out / 'paths' / (name + '.json'), data)
    finally:
        env.close()
        if client is not None:
            client.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('out', type=Path)
    ap.add_argument('mode', choices=['probe', 'direct', 'survey', 'branch'])
    ap.add_argument('name')
    ap.add_argument('start', type=int)
    ap.add_argument('--pair')
    ap.add_argument('--arm', choices=['A', 'B'])
    args = ap.parse_args()
    if args.mode == 'probe':
        probe(args.out, args.name, args.start)
    else:
        match = next((p for p in read(args.out / 'selection.json')['pairs'] if p['id'] == args.pair), None) if args.pair else None
        assert (args.mode == 'branch') == bool(match and args.arm)
        rollout(args.out, args.mode, args.name, args.start, match, args.arm)
