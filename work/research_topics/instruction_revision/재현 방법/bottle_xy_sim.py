"""Prepare one bottle placement with the original scene's two archived commands in MuJoCo."""
import argparse
from pathlib import Path

import numpy as np

from atomic_control import capture_state, geom_info, measurements, policy_observation
from r1_motion import BottleObserver, calibration_trial, reset, sim, write
from verify_atomic import read, sha


def support_sample(env, observer, bowl):
    contact = observer.live.contact
    pairs = zip(contact.geom1, contact.geom2)
    bowl_partners = {int(b if a in bowl else a) for a,b in pairs if a in bowl or b in bowl}
    bottle_partners = {b if a in observer.bottle else a for a,b in observer.contacts()}
    model = env.env
    return {'bowl_xyz':model.sim.data.body_xpos[model.obj_body_id['akita_black_bowl_1']].tolist(),
            'bowl_partners':sorted(bowl_partners), 'bottle_partners':sorted(bottle_partners)}


def prepare(folder):
    spec = read(folder/'protocol.json')
    seed = spec['scene_seed']
    cal = read(folder/'calibration.json')
    cal['check'] = calibration_trial(seed, include_layout=True, bottle_xy=spec['bottle_xy'])
    write(folder/'calibration.json', cal)
    source_path = folder/'base_prefix.json'
    assert sha(source_path.read_bytes()) == spec['archived_command_source']
    donor = read(source_path)
    assert donor['status'] == 'PREFIX_ONLY' and donor['queries'][0]['prompt'] == spec['source_prompt']
    commands = donor['queries'][0]['reply']
    assert [r['dispatched'] for r in donor['rows']] == commands[:spec['switch']]
    edit = {}
    env = reset(seed, spec['bottle_xy'], edit)
    try:
        observer = BottleObserver(env)
        geometry = geom_info(env)
        groups = {k:set(v.values()) for k,v in geometry['contact_geoms'].items()}
        def readout(success):
            return dict(measurements(env, groups, success),
                        bottle_pose=observer.pose(), bottle_contacts=observer.contacts())
        tape = {'status':'PREFIX_ONLY','geometry':geometry,'bottle_geometry':observer.geometry,
                'command_origin':spec['archived_command_source'],'policy_queries_for_prefix':0,
                'initial_readout':readout(env.env._check_success(return_success_dict=True)),
                'queries':[],'rows':[],'snapshots':{}}
        for tick in (0, spec['switch']):
            _, observation = policy_observation(folder, env, spec['source_prompt'])
            tape['snapshots'][str(tick)] = capture_state(env)
            query = dict(observation, completed_controls=tick)
            tape['queries'].append(query)
            if tick == 0:
                query.update(prompt=spec['source_prompt'], reply=commands)
                for index, command in enumerate(commands[:spec['switch']]):
                    _, success = sim.step(env, np.asarray(command))
                    tape['rows'].append(dict(readout(success),tick=index+1,query=0,index=index,dispatched=command))
        write(folder/'prefix.json', tape)
        write(folder/'reset_edit.json', edit)
    finally:
        env.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    prepare(parser.parse_args().folder)
