"""Run and replay the official singleton tasks and their natural drawer-to-stove handoffs."""
import argparse
import json
from pathlib import Path

import numpy as np

from atomic_control import capture_state
from drawer_sim import ASSETS, DESIGN as DRAWER, client_for, observe, reset, save, state_hash
from stove_pose_sim import Scene, posture, record_prep, trajectory
from verify_atomic import PACKET, read
from verify_stove import D as STOVE
from verify_stove_layouts import DESIGN


def layout_env(layout, task):
    return reset(layout, starts_file=PACKET/DESIGN['starts_file'],
                 task_file=ASSETS/('task.bddl' if task=='drawer' else 'stove.bddl'),
                 goal=(DRAWER if task=='drawer' else STOVE)['goal'])


def measurement(env, scene, native_task):
    row = scene.stove.sample()
    on = bool(env.env._eval_predicate(STOVE['goal']))
    assert row['on']==(row['drawer_open'] if native_task=='drawer' else on)
    row['on'] = on
    return row


def direct(out, e, replay=False):
    name,task=e['session'],e['task']
    env=layout_env(e['layout'],task)
    client=None
    try:
        scene=Scene(env)
        path=out/'gates'/(name+'.json')
        old=read(path) if replay else None
        data=dict(session=name,task=task,layout=e['layout'],key=e['key'],block=e['block'],
                  geometry=scene.stove.geometry,common=posture(env),initial=measurement(env,scene,task),
                  initial_physics=state_hash(capture_state(env)),queries=[],rows=[])
        if replay:
            assert all(data[k]==old[k] for k in ('session','geometry','common','initial','initial_physics'))
        else:
            client=client_for(name)
        changed=[]
        period=DESIGN['period']
        for i in range(e['queries']):
            tick=i*period
            query,sample=observe(env,out,i==0 and not replay,e['source'])
            if replay:
                previous=old['queries'][i]
                assert (sample['state'],sample['physics'],tick)==(previous['state'],previous['physics'],previous['tick'])
                if sample['live']!=previous['live']:
                    changed.append(tick)
                actions=[r['action'] for r in old['rows'][tick:tick+period]]
            else:
                reply=np.asarray(client.infer(query)['actions'],dtype='<f8')
                assert reply.shape==(10,7) and np.isfinite(reply).all()
                data['queries'].append(dict(tick=tick,reply=reply.tolist(),**sample))
                actions=reply[:period].tolist()
            for action in actions:
                env.step(action)
                row=dict(action=action,**measurement(env,scene,task))
                if replay:
                    assert row==old['rows'][len(data['rows'])]
                data['rows'].append(row)
        final=state_hash(capture_state(env))
        if replay:
            assert final==old['final_physics']
            return dict(session=name,prefix_controls=0,lead=0,policy_controls=len(data['rows']),
                        observations=e['queries'],changed_rgb_ticks=changed,final_physics=final)
        save(path,dict(data,final_physics=final))
    finally:
        if client is not None:
            client.close()
        env.close()


def restore_natural(env,scene,arm,out):
    tape=read(out/'gates'/(arm+'.json'))
    common=posture(env)
    assert tape['task']=='drawer' and common==tape['common'] and scene.stove.geometry==tape['geometry']
    assert state_hash(capture_state(env))==tape['initial_physics']
    assert scene.stove.sample()==tape['initial']
    period=DESIGN['period']
    for i,row in enumerate(tape['rows']):
        if i%period==0:
            _,sample=observe(env,out,False,DRAWER['prompt'])
            previous=tape['queries'][i//period]
            assert (sample['physics'],sample['state'])==(previous['physics'],previous['state']), (arm,i)
        env.step(row['action'])
        assert dict(action=row['action'],**scene.stove.sample())==row,(arm,i+1)
    assert len(tape['rows'])==DESIGN['drawer_horizon'] and state_hash(capture_state(env))==tape['final_physics']
    return common


def preparation(out):
    from OpenGL import GL
    import mujoco
    from verify_stove_pose import preparation_metrics
    gate=read(out/'gate.json')
    checked={}
    for layout in DESIGN['layouts']:
        for donor in gate[str(layout)]['donors']:
            bundle={}
            for mode in DESIGN['modes']:
                n=0 if mode=='immediate' else DESIGN['lead']
                frame=record_prep(out,donor,mode,n,open_env=lambda _:layout_env(layout,'stove'),restore_prefix=restore_natural)
                save(out/'preparation'/f'{donor}-{mode}-{n}.json',frame)
                if n:
                    bundle[mode]=preparation_metrics(frame)
            checked[donor]=bundle
    env=layout_env(DESIGN['layouts'][0],'stove')
    try:
        renderer=GL.glGetString(GL.GL_RENDERER).decode()
        assert 'NVIDIA' in renderer
    finally:
        env.close()
    save(out/'qualification.json',dict(lead=DESIGN['lead'],donors=checked,renderer=renderer,mujoco=mujoco.__version__))


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('out',type=Path)
    ap.add_argument('stage',choices=['run','replay','prepare'])
    ap.add_argument('session',nargs='?')
    a=ap.parse_args()
    if a.stage=='prepare':
        preparation(a.out)
    else:
        gate_sessions=read(a.out/'gate_sessions.json')
        if a.session in gate_sessions:
            result=direct(a.out,gate_sessions[a.session],replay=a.stage=='replay')
        else:
            entry=read(a.out/'sessions.json')[a.session]
            result=trajectory(a.out,entry,replay=a.stage=='replay',open_env=lambda _:layout_env(entry['layout'],'stove'),
                              restore_prefix=restore_natural)
        if result:
            print(json.dumps(result),flush=True)
