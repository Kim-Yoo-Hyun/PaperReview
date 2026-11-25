"""Find a matched, collision-free starting scene using only native simulator geometry."""
from collections import Counter
from contextlib import ExitStack
from itertools import product
import math

import numpy as np

from atomic_control import capture_state
from drawer_location import COHORT, DESIGN, MODES
from drawer_location_sim import LocationCabinet, set_opening
from middle_aperture_sim import environment, restore
from stove_pose_sim import prepare
from verify_atomic import read
from verify_middle_aperture import BASE
from verify_stove_layouts import digest


class Probe:
    def __init__(self, env, arm, out):
        self.env = env
        self.scene = LocationCabinet(env)
        common = restore(env,self.scene,arm,out,donors_file=COHORT['donors'])
        prepare(env,self.scene,common,'pose',BASE['lead'])
        assert digest(capture_state(env)) == COHORT['returned_physics'][arm]
        data, model = env.sim.data, env.sim.model
        self.qpos,self.qvel,self.warm = data.qpos.copy(),data.qvel.copy(),data.qacc_warmstart.copy()
        slide = self.scene.slides['middle']
        self.width = slide['closed']-self.qpos[slide['qpos']]
        self.table = model.geom_name2id('table_collision')
        self.objects = {int(i):name for name in self.scene.moved_objects
                        for i in np.flatnonzero(model.geom_bodyid==model.body_name2id(name))}

    def sample(self, mode, width, shift):
        env, scene = self.env, self.scene
        data, model = env.sim.data, env.sim.model
        data.qpos[:],data.qvel[:],data.qacc_warmstart[:] = self.qpos,self.qvel,self.warm
        set_opening(env,scene,mode,-width,shift)
        supported, obstacles, min_dist = set(), Counter(), 0.
        contacts = data._data.contact
        for a,b,d in zip(contacts.geom1,contacts.geom2,contacts.dist):
            a,b = int(a),int(b)
            for obj,other in ((a,b),(b,a)):
                if obj in self.objects and other==self.table:
                    supported.add(self.objects[obj])
            object_obstacle = (a in self.objects or b in self.objects) and self.table not in (a,b)
            robot_obstacle = (a in scene.robot_geoms)!=(b in scene.robot_geoms)
            if object_obstacle or robot_obstacle or a in scene.contact_slides or b in scene.contact_slides:
                bodies = sorted(model.body_id2name(model.geom_bodyid[i]) for i in (a,b))
                obstacles[' / '.join(bodies)] += 1
                min_dist = min(min_dist,float(d))
        return dict(clear=not obstacles and supported==set(scene.moved_objects), supported=sorted(supported),
                    contacts=dict(obstacles), max_penetration_mm=-1000*min_dist)


def separate_shifts(probes, directions):
    names = list(next(iter(probes.values())).scene.moved_objects)
    candidates = {n:[] for n in names}
    for name in names:
        for mm in range(0,151,5):
            for index,vec in enumerate(directions if mm else directions[:1]):
                unit = vec/np.linalg.norm(vec)
                xy, back = ((unit*d/1000).tolist() for d in (mm,max(0,mm-2)))
                valid = True
                for p in probes.values():
                    for pos in (xy,back):
                        shift = {n:(pos if n==name else [0.,0.]) for n in names}
                        for mode in MODES:
                            result = p.sample(mode,p.width,shift)
                            collisions = [pair.split(' / ') for pair in result['contacts']]
                            if name not in result['supported'] or any(name in pair and set(pair)!=set(names) for pair in collisions):
                                valid = False
                                break
                        if not valid:
                            break
                    if not valid:
                        break
                if valid:
                    candidates[name].append((mm,index,xy,back))
    def rank(pair):
        a,b = pair
        return max(a[0],b[0]),a[0]**2+b[0]**2,a[:2],b[:2]
    attempts = 0
    for pair in sorted(product(*(candidates[n] for n in names)),key=rank):
        attempts += 1
        accepted = all(p.sample(mode,p.width,dict(zip(names,positions)))['clear']
                       for p in probes.values() for mode in MODES for positions in product(*(v[2:] for v in pair)))
        if accepted:
            return ({n:v[2] for n,v in zip(names,pair)},dict(eligible_candidates={n:len(v) for n,v in candidates.items()},
                    joint_pairs_tested=attempts, grid_choice={n:v[:2] for n,v in zip(names,pair)}))
    raise ValueError('The fixed independent tabletop position grid has no contact-free supported pair')


def select_clearance(original):
    with ExitStack() as stack:
        probes = {}
        initial = {}
        for arm in COHORT['arms']:
            env = environment(arm,layout=COHORT['layout'])
            stack.callback(env.close)
            probe = probes[arm] = Probe(env,arm,original)
            initial[arm] = {}
            for mode in MODES:
                tape = read(original/'preparation'/f"{arm}-{mode}-{BASE['lead']}.json")
                metrics = probe.sample(mode,probe.width,[0.,0.])
                assert digest(capture_state(env))==tape['first']['physics']
                if mode in DESIGN['previous_handoffs'][arm]:
                    assert tape['first']['physics']==DESIGN['previous_handoffs'][arm][mode]
                hand = tape['handoff']
                metrics['object_drift_mm'] = {n:1000*max(math.dist(pos[:3],s['objects'][n][:3]) for s in tape['stationary'])
                                              for n,pos in hand['objects'].items()}
                metrics['drawer_drift_mm'] = [1000*max(abs(s['joints'][i]-x) for s in tape['stationary'])
                                              for i,x in enumerate(hand['upper']['joints'])]
                initial[arm][mode] = metrics
        floor_mm = math.floor(1000*min(p.width for p in probes.values()))
        sweep = {}
        for arm,p in probes.items():
            sweep[arm] = [p.sample('bottom',mm/1000,[0.,0.]) for mm in range(floor_mm+1)]
        threshold = -probe.scene.geometry['open_below_m']
        widths = [mm for mm in range(floor_mm,0,-1) if mm/1000>threshold]
        first_collision = next(mm for mm in range(floor_mm+1) if any(not v[mm]['clear'] for v in sweep.values()))
        partial_mm = first_collision-3
        assert partial_mm>0 and all(p.sample('middle',partial_mm/1000,[0.,0.])['clear'] for p in probes.values())
        full = all(s['clear'] for modes in initial.values() for s in modes.values())
        width, shift = None, [0.,0.]
        tested, separate = [], None
        if not full:
            for mm in widths:
                if all(sweep[a][mm]['clear'] and p.sample('middle',mm/1000,shift)['clear'] for a,p in probes.items()):
                    width = mm/1000
                    break
            else:
                t = read(original/'preparation'/f"{arm}-middle-{BASE['lead']}.json")
                c = read(original/'preparation'/f"{arm}-closed-{BASE['lead']}.json")
                outward = np.subtract(t['handoff']['upper']['middle_xyz'][:2],c['handoff']['upper']['middle_xyz'][:2])
                outward /= np.linalg.norm(outward)
                right = np.array([outward[1],-outward[0]])
                directions = (outward,right,-right,outward+right,outward-right,-outward,-outward+right,-outward-right)
                found = False
                for mm in range(5,151,5):
                    for index,vec in enumerate(directions):
                        unit = vec/np.linalg.norm(vec)
                        xy = (unit*mm/1000).tolist()
                        passed = all(p.sample(m,p.width,(unit*d/1000).tolist())['clear']
                                     for p in probes.values() for m in MODES for d in (mm,mm-2))
                        tested.append(dict(mm=mm,direction=index,clear=passed))
                        if passed:
                            shift,found = xy,True
                            break
                    if found:
                        break
                if not found:
                    shift,separate = separate_shifts(probes,directions)
        return dict(original=initial, measured_openings_m={a:p.width for a,p in probes.items()},
                    width_sweep_mm=sweep, official_open_widths_mm=widths, translations=tested, independent_translations=separate,
                    arrangements=dict(full=dict(width_m=width,shift_xy_m=shift),partial=dict(width_m=partial_mm/1000,shift_xy_m=[0.,0.])))
