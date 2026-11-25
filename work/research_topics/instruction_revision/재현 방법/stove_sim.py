"""Qualify the two archived drawer branches and execute the native stove continuation."""
import argparse
import json
from pathlib import Path

import numpy as np

from atomic_control import capture_state
from drawer_sim import ASSETS, DESIGN as DRAWER, Drawer, client_for, observe, reset, save, state_hash
from verify_atomic import read
from verify_stove import D, command_sha, crossed, donor, scenario


class Stove:
    def __init__(self, env, *, goal=None):
        self.env = env
        self.goal = goal
        self.drawer = Drawer(env)
        model = env.sim.model
        joint = model.joint_name2id(D['button_joint'])
        self.address = int(model.jnt_qposadr[joint])
        button_body = int(model.jnt_bodyid[joint])
        self.button = set(np.flatnonzero(model.geom_bodyid == button_body).tolist())
        self.stove = {i for i in range(model.ngeom)
                      if str(model.body_id2name(model.geom_bodyid[i])).startswith('flat_stove_1_')}
        assert self.button and self.button < self.stove and self.stove.isdisjoint(self.drawer.drawer)
        ranges = env.env.get_object('flat_stove_1').object_properties['articulation']['default_turnon_ranges']
        assert min(ranges) == D['on_angle_rad']
        self.geometry = json.loads(json.dumps(dict(self.drawer.geometry, button_qpos=self.address,
            stove={i:model.geom_id2name(i) for i in sorted(self.stove)},
            button={i:model.geom_id2name(i) for i in sorted(self.button)})))

    def sample(self):
        row = self.drawer.sample()
        pairs = [list(p) for p in row['gripper_pairs']]
        return dict(drawer_joints=row['joints'], drawer_contact=row['target_contact'],
                    drawer_open=bool(self.env.env._eval_predicate(DRAWER['goal'])), gripper_pairs=pairs,
                    stove_contact=any(b in self.stove for _,b in pairs),
                    button_contact=any(b in self.button for _,b in pairs),
                    angle=float(self.env.sim.data.qpos[self.address]),
                    on=row['goal'] if self.goal is None else bool(self.env.env._eval_predicate(self.goal)))


def environment(condition):
    public, start, _, _ = scenario(condition)
    return reset(start, task_file=ASSETS/'stove.bddl', goal=D['goal'],
                 starts_file=ASSETS/('stove_starts.json' if public else 'starts.json'))


def snapshot(env, obs, out, last_touch):
    _, q = observe(env, out, False, D['prompt'])
    return dict(physics=q['physics'], state=q['state'], initial=obs.sample(), last_prior_drawer=last_touch)


def prefix(env, obs, arm, until, out, checkpoints=()):
    tape = donor(arm)
    assert state_hash(capture_state(env)) == tape['initial_physics']
    assert obs.geometry['drawer'] == tape['geometry']['drawer'] and obs.geometry['gripper'] == tape['geometry']['gripper']
    saved, last = {}, None
    for i, old in enumerate(tape['rows'][:until]):
        if i % D['replan_every'] == 0:
            _, view = observe(env, out, False)
            archived = tape['queries'][i//D['replan_every']]
            assert (view['physics'], view['state']) == (archived['physics'], archived['state']), (arm, i)
        env.step(old['action'])
        row = obs.sample()
        assert (row['drawer_joints'],row['drawer_open'],row['drawer_contact'],row['gripper_pairs']) == (
            old['joints'],old['goal'],old['target_contact'],old['gripper_pairs']), (arm,i+1)
        assert not row['on']
        if row['drawer_contact']:
            last = i+1
        if i+1 in checkpoints:
            saved[f'{arm}-{i+1}'] = snapshot(env,obs,out,last)
    if until == D['primary_switch']:
        assert state_hash(capture_state(env)) == tape['final_physics']
    return saved, last


def qualify(out):
    from OpenGL import GL
    import mujoco
    conditions = [*(f'public-{s}' for s in D['public_starts']), 'layout', 'A-160', 'B-160']
    states, geometry = {}, None
    for condition in conditions:
        env = environment(condition)
        try:
            obs = Stove(env)
            if geometry is None:
                geometry = obs.geometry
            assert geometry == obs.geometry
            _, _, arm, tick = scenario(condition)
            if arm:
                samples, _ = prefix(env,obs,arm,tick,out,[*D['timing_controls'],tick])
                states.update(samples)
            else:
                states[condition] = snapshot(env,obs,out,None)
            renderer = GL.glGetString(GL.GL_RENDERER).decode()
            assert 'NVIDIA' in renderer
        finally:
            env.close()
    save(out/'qualification.json',dict(states=states,geometry=geometry,renderer=renderer,mujoco=mujoco.__version__))


def trajectory(out, entry, replay=False):
    name, cond = entry['session'], entry['condition']
    env = environment(cond)
    client = None
    try:
        obs = Stove(env)
        qualification = read(out/'qualification.json')
        registered = qualification['states'][cond]
        assert obs.geometry == qualification['geometry']
        _, _, arm, switch = scenario(cond)
        last = prefix(env,obs,arm,switch,out)[1] if arm else None
        assert state_hash(capture_state(env)) == registered['physics']
        assert obs.sample() == registered['initial'] and last == registered['last_prior_drawer']
        motor = entry.get('motor_source')
        path = out/('crossed' if motor else 'paths')/(name+'.json')
        fixed = read(out/'paths'/(motor+'.json')) if motor else None
        old = read(path) if replay else None
        if not replay and not motor:
            client = client_for(name)
        data = dict(session=name,condition=cond,seed=entry['key'],block=entry['block'],
                    initial_physics=registered['physics'],initial=obs.sample(),queries=[],rows=[])
        if motor:
            data.update(motor_source=motor,commands_sha256=command_sha([r['action'] for r in fixed['rows']]))
        changed = []
        period = D['replan_every']
        for tick in range(0,D['full_budget'],period):
            query, rec = observe(env,out,tick == 0 and not replay,D['prompt'])
            if tick == 0:
                assert rec['state'] == registered['state'] and rec['physics'] == registered['physics']
            if replay:
                src = old['queries'][tick//period]
                assert (rec['physics'],rec['state']) == (src['physics'],src['state']), (name,tick)
                if rec['live'] != src['live']:
                    changed.append(tick)
            if motor:
                actions = [r['action'] for r in fixed['rows'][tick:tick+period]]
                if not replay:
                    data['queries'].append(dict(tick=tick,**rec))
            elif replay:
                actions = [r['action'] for r in old['rows'][tick:tick+period]]
            else:
                reply = np.asarray(client.infer(query)['actions'],dtype='<f8')
                assert reply.shape == (10,7) and np.isfinite(reply).all()
                data['queries'].append(dict(tick=tick,reply=reply.tolist(),**rec))
                actions = reply[:period].tolist()
            for action in actions:
                env.step(action)
                row = obs.sample()
                if not motor:
                    row['action'] = action
                if replay:
                    assert row == old['rows'][len(data['rows'])], (name,len(data['rows'])+1)
                data['rows'].append(row)
        final = state_hash(capture_state(env))
        if replay:
            assert final == old['final_physics']
            return dict(session=name,controls=len(data['rows']),queries=D['full_budget']//period,
                        prefix_controls=switch,changed_rgb_ticks=changed)
        save(path,dict(data,final_physics=final))
    finally:
        if client is not None:
            client.close()
        env.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('out',type=Path)
    ap.add_argument('mode',choices=['qualify','run','cross','replay'])
    ap.add_argument('session',nargs='?')
    a = ap.parse_args()
    if a.mode == 'qualify':
        qualify(a.out)
    else:
        entry = crossed()[a.session] if a.session.startswith('cross-') else read(a.out/'sessions.json')[a.session]
        result = trajectory(a.out,entry,replay=a.mode=='replay')
        if result:
            print(json.dumps(result),flush=True)
