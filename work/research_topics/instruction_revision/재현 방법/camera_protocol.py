"""Frozen contexts, placements and first-query input contracts for the R1 camera comparison."""
from pathlib import Path

import numpy as np

from verify_atomic import CAMERAS, PACKET, read


DESIGN = 'R1_CAMERA_FACTORIAL.json'


def contexts(d):
    primary = tuple(d['primary'])
    rows = [primary]
    for scene in d['historical_scenes']:
        for host,donor in [('s','o'),('o','s')]:
            for wording in d['historical_prompts']:
                item = (scene,host,donor,wording,0)
                if item != primary:
                    rows.append(item)
    rows.extend((*primary[:4],key) for key in d['additional_policy_seeds_on_primary'])
    rows.extend((11,'s',donor,'B',0) for donor in d['additional_donors_about_s'])
    for scene in d['new_scene_seeds']:
        rows.extend([(scene,'n','d','B',0),(scene,'d','n','B',0),(scene,'d','n','T',0)])
    assert len(rows) == len(set(rows)) == 31
    return rows


def key(context):
    scene,host,donor,wording,seed = context
    return f'{scene}-{host}-{donor}-{wording}-k{seed}'


def placements(d, scene, native=None):
    o,s = (np.array(d['positions'][k]) for k in ('o','s'))
    if scene in d['new_scene_seeds']:
        n = np.array(native)
        return {'n':n.tolist(), 'd':(n+(s-o)).tolist()}
    positions = dict(d['positions'])
    if scene == 11:
        length = np.linalg.norm(o-s)
        axes = {'positive_x':[length,0],'negative_x':[-length,0],
                'positive_y':[0,length],'negative_y':[0,-length],
                'half_toward_o':0.5*(o-s),'double_toward_o':2*(o-s)}
        positions.update({label:(s+axes[direction]).tolist() for label,direction in d['additional_donors_about_s'].items()})
    return positions


def geometry(out,scene,position):
    return out/'geometry'/f'{scene}-{position}'


def eligibility(out, context, gates):
    scene,host,donor,_,_ = context
    if not all(gates[f'{scene}-{p}']['eligible'] for p in (host,donor)):
        return False
    a,b = [read(geometry(out,scene,p)/'prefix.json') for p in (host,donor)]
    qa,qb = a['queries'][1],b['queries'][1]
    return (qa['proprioception'] == qb['proprioception'] and
            all(qa['rgb_sha256'][c] != qb['rgb_sha256'][c] for c in CAMERAS) and
            [r['dispatched'] for r in a['rows']] == [r['dispatched'] for r in b['rows']])


def protocol(out, d, context, condition):
    scene,host,donor,wording,seed = context
    physical = geometry(out,scene,host)
    spec = read(physical/'protocol.json')
    pair = [read(geometry(out,scene,pos)/'prefix.json')['queries'][1]['rgb_sha256'] for pos in (host,donor)]
    assigned = {camera:pair[index][camera] for camera,index in zip(CAMERAS,d['camera_sources'][condition])}
    words = {**read(PACKET/'R1_CONTROL.json')['arms'],**read(PACKET/'R1_MENTION_MATCHED.json')['arms']}
    spec.pop('words',None)
    spec.update(arms={wording:words[wording]}, run_order=[[wording],[wording]], policy_rng_seed=seed,
                camera_factorial={'context':list(context),'condition':condition},
                first_view={'study':DESIGN,'rgb_sha256':assigned})
    return spec


def cell_folder(out, context, condition):
    return out/'cells'/(key(context)+'-'+condition)
