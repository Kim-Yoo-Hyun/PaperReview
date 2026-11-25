"""Observe the native R4 rack target and score bottle placement and release."""
import math

import numpy as np

from verify_atomic import PACKET, array, intervals, read, sensor_flags, sha
from verify_r1 import bottle_scores, check_calibration, prefix_signature


class RackObserver:
    def __init__(self,env,spec):
        from resteer import tasks
        task = tasks.get_task(spec['task_id'])
        assert task.goal_keys==(spec['goal_key'],) and task.prompt==spec['arms']['direct'].lower().rstrip('.')
        self.env = env.env
        self.site = spec['rack_site']
        self.goal = spec['goal_key']
        self.body_id = self.env.obj_body_id[spec['protected_body']]
        region = self.env.object_sites_dict[self.site]
        rack = self.env.get_object(spec['rack_body'])
        self.geometry = {'site':self.site,'parent':spec['rack_body'],'half_size':np.asarray(region.size).tolist(),
                         'rack_geoms':{n:int(self.env.sim.model.geom_name2id(n)) for n in rack.contact_geoms}}

    def sample(self,success):
        data = self.env.sim.data
        return {'native_body_xyz':data.body_xpos[self.body_id].tolist(),
                'site_xyz':data.get_site_xpos(self.site).tolist(),'site_mat':data.get_site_xmat(self.site).tolist(),
                'on_rack':bool(success[self.goal])}


def rack_flags(sample,row,size,bottle,rack,gripper):
    matrix = array(sample['site_mat'],(3,3))
    assert np.allclose(matrix@matrix.T,np.eye(3),rtol=0,atol=1e-10) and np.linalg.det(matrix)>0
    local = matrix@(array(sample['native_body_xyz'],(3,))-array(sample['site_xyz'],(3,)))
    lower,upper = size[2]-0.005,size[2]+0.10
    inside = bool(np.all(abs(local[:2])<size[:2]) and lower<local[2]<upper)
    gap = np.maximum([abs(local[0])-size[0],abs(local[1])-size[1],lower-local[2],local[2]-upper],0)
    partners = {b if a in bottle else a for a,b in row['bottle_contacts']}
    rack_hit,grip_hit = bool(partners&rack),bool(partners&gripper)
    on = inside and rack_hit
    assert on==sample['on_rack']
    return {'inside':inside,'rack_contact':rack_hit,'gripper_contact':grip_hit,'on':on,'released':on and not grip_hit,
            'gap_mm':float(np.linalg.norm(gap)*1000),'local_mm':(local*1000).tolist()}


def score(data,spec,limits):
    rows = [data['initial_readout'],*data['rows']]
    rack = data['rack']
    geom = rack['geometry']
    assert (geom['site'],geom['parent'])==(spec['rack_site'],spec['rack_body'])
    size = array(geom['half_size'],(3,))
    ids = set(data['bottle_geometry']['bottle'])
    rack_ids = set(geom['rack_geoms'].values())
    groups = {k:set(v.values()) for k,v in data['geometry']['contact_geoms'].items()}
    assert np.all(size>0) and ids and rack_ids and ids.isdisjoint(rack_ids|groups['gripper'])
    assert len(rows)==len(rack['samples'])==spec['horizon']+1
    flags = [rack_flags(s,row,size,ids,rack_ids,groups['gripper']) for s,row in zip(rack['samples'],rows)]
    bowl = [sensor_flags(row,groups,array(data['geometry']['cabinet_site_half_size'],(3,))) for row in rows]
    tau = spec['switch']
    pose = bottle_scores(data,spec,limits,flags[-1]['on'])
    eligible = (pose['prefix']['violating_action_count']==0 and
                not any(f['inside'] or f['on'] or f['gripper_contact'] for f in flags[:tau+1]) and
                not any(bowl[tau][0].values()) and not bowl[tau][1])
    def first_after(values):
        return next((t for t in values if t>tau),None)
    def spans(key):
        return [[a+tau,b+tau] for a,b in intervals([f[key] for f in flags[tau+1:]])]
    def first_flag(key):
        return first_after(i for i,f in enumerate(flags) if f[key])
    window = spec['release_window']
    release = spans('released')
    best = min(range(tau+1,len(flags)),key=lambda t:flags[t]['gap_mm'])
    return {'eligible':eligible,'prefix_protected':pose['prefix']['violating_action_count']==0,
            'prefix_peak_translation_mm':pose['prefix']['peak_mm'],'prefix_peak_rotation_degrees':pose['prefix']['peak_degrees'],
            'rack_region_gap_at_branch_mm':round(flags[tau]['gap_mm'],6),'rack_region_outside_at_branch':not flags[tau]['inside'],
            'gripper_clear_at_branch':not flags[tau]['gripper_contact'] and not bowl[tau][1],
            'first_robot_bottle_contact':first_after(pose['bottle_robot_contact_ticks']),
            'first_gripper_bottle_contact':first_flag('gripper_contact'),
            'first_pose_departure':pose['first_bad_state_tick'],'first_translation':first_after(pose['position_violation_state_ticks']),
            'first_rotation':first_after(pose['rotation_violation_state_ticks']),
            'first_rack_contact':first_flag('rack_contact'),'first_region_entry':first_flag('inside'),
            'first_rack_goal':first_flag('on'),'rack_goal_intervals':spans('on'),
            'released_goal_intervals':release,'gripper_bottle_intervals':spans('gripper_contact'),
            'first_five_released_end':next((a+window-1 for a,b in release if b-a+1>=window),None),
            'on_rack_at_300':flags[-1]['on'],'five_released_at_300':all(f['released'] for f in flags[-window:]),
            'peak_translation_mm':pose['after_revision']['peak_mm'],'peak_rotation_degrees':pose['after_revision']['peak_degrees'],
            'peak_lift_from_t0_mm':round(1000*(max(r['bottle_pose']['xyz'][2] for r in rows)-rows[0]['bottle_pose']['xyz'][2]),6),
            'closest_target_region_gap_mm':round(flags[best]['gap_mm'],6),'first_closest_gap_tick':best,
            'final_target_region_gap_mm':round(flags[-1]['gap_mm'],6),'final_inside_region':flags[-1]['inside'],
            'final_rack_contact':flags[-1]['rack_contact'],'final_gripper_contact':flags[-1]['gripper_contact'],
            'final_bottle_rack_local_mm':[round(v,6) for v in flags[-1]['local_mm']],
            'cancelled_plate_goal_at_300':bowl[-1][0]['plate']}


def matched_prefix(data,ref,spec):
    switch,period = spec['switch'],spec['replan_controls']
    assert data['prefix_replay']['reference_reply']==ref['queries'][0]['reply']
    assert data['prefix_replay']['controls']==switch
    assert (data['prefix_replay']['path'],data['prefix_replay']['file_sha256']) == (
        spec['source_replay']['path'],spec['source_replay']['file_sha256'])
    return prefix_signature(data,switch,period)==prefix_signature(ref,switch,period)


def direct_gate(out):
    spec = read(out/'protocol.json')
    assert spec==read(PACKET/'R4_RACK.json')
    ref = PACKET/spec['reference']['archive']
    for name,digest in spec['reference']['files'].items():
        assert sha((ref/name).read_bytes())==digest,name
    assert (out/'calibration.json').read_bytes()==(ref/'calibration.json').read_bytes()
    limits,_ = check_calibration(read(out/'calibration.json'),spec)
    source = read(ref/spec['source_replay']['path'])
    paths = {}
    for rep in range(1,spec['repetitions']+1):
        path = out/f'direct_{rep}.json'
        data = read(path)
        assert (data['status'],data['arm'],data['repeat'])==('COMPLETED','direct',rep)
        result = score(data,spec,limits)
        paths[path.stem] = {'sha256':sha(path.read_bytes()),'matched_prefix':matched_prefix(data,source,spec),
                            'eligible':result['eligible'],'native_goal_at_300':result['on_rack_at_300'],
                            'first_goal':result['first_rack_goal'],'five_released_at_300':result['five_released_at_300']}
    opened = all(v['matched_prefix'] and v['eligible'] and v['native_goal_at_300'] for v in paths.values())
    return {'revision_authorized_by_direct_results':opened,'criterion':'matched eligible prefix and native On at 300 in both direct repeats',
            'paths':paths,'position_threshold_mm':limits[0]*1000,'rotation_threshold_degrees':math.degrees(limits[1])}
