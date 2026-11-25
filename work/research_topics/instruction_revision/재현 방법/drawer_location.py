"""Score matched drawer-location interventions and full command crossovers in Docker."""
import argparse
from collections import Counter
from itertools import combinations
import json
import math
from pathlib import Path
import subprocess

import numpy as np

from inside import write_json
from replay_middle_aperture import CONTACTS, FLAGS as APERTURE_FLAGS, event_trace, read_trace
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import (BASE, LAYOUT2_FILE, LEVELS, PLAN, TASK, check_archive_repeat,
                                    check_donors, check_sessions, contact_geometry, outcome, path_outcomes,
                                    planned, stationary, study_for, summary)
from verify_stove import sha
from verify_stove_layouts import check_freeze, check_replayed_paths, digest, replay


DESIGN_FILE = 'drawer/drawer_location.json'
DESIGN = read(PACKET/DESIGN_FILE)
COHORT = study_for(read(PACKET/LAYOUT2_FILE))
MODES = DESIGN['modes']
ARRANGEMENTS = ('partial','full')
CONDITIONS = [f'{arrangement}-{mode}' for mode in MODES for arrangement in ARRANGEMENTS]
FLAGS = (*APERTURE_FLAGS, 'bottom_open')
TIMES = tuple(map(str, TASK['deadlines']))
SIM = 'drawer_location_sim.py'


def qualify_starts(out, geometry):
    preps, checks = {}, {}
    for arrangement in ARRANGEMENTS:
        cells,checks[arrangement] = qualify_arrangement(out,geometry,arrangement)
        preps.update(cells)
    return preps,checks


def qualify_arrangement(out, geometry, arrangement):
    slides = geometry['slides']
    assert slides['middle']['axis'] == slides['bottom']['axis'] and slides['middle']['limits'] == slides['bottom']['limits']
    clearance = read(out/'clearance.json')
    selected = clearance['arrangements'][arrangement]
    shift = selected['shift_xy_m']
    preps, checks = {}, {}
    for arm in COHORT['arms']:
        cells = {mode:read(out/'preparation'/f"{arm}-{arrangement}-{mode}-{BASE['lead']}.json") for mode in MODES}
        ref = cells['closed']
        handoff = ref['handoff']
        prior = ref['branch']['before']
        assert digest(prior) == COHORT['returned_physics'][arm]
        assert ref['donor_physics'] == COHORT['donor_physics'][COHORT['arms'].index(arm)]
        assert not ref['start']['stove']['drawer_contact'] and ref['start']['stove']['drawer_open']
        assert len(ref['rows']) == len(ref['actions']) == BASE['lead']
        displacement = ref['branch']['displacement_m']
        natural = ref['rows'][-1]['upper']['joints'][1] - slides['middle']['closed']
        assert natural == -clearance['measured_openings_m'][arm]
        assert displacement == (natural if selected['width_m'] is None else -selected['width_m'])
        assert displacement < 0 and (displacement < geometry['open_below_m']) == (arrangement=='full')
        assert max(map(abs,handoff['tool']['velocity'])) <= PLAN['limits']['final_velocity_rad_s']
        holds, moved, coordinates = {}, {}, {}
        for mode, tape in cells.items():
            condition = f'{arrangement}-{mode}'
            assert (tape['arm'],tape['mode'],tape['length']) == (arm,condition,BASE['lead'])
            assert all(tape[k] == ref[k] for k in ('common','start','rows','actions','donor_physics'))
            change, end = tape['branch'], tape['handoff']
            assert change['before'] == prior and change['displacement_m'] == displacement and change['shift_xy_m']==shift
            after = change['after']
            assert digest(after) == tape['first']['physics']
            original = read(out/'original/preparation'/f"{arm}-{mode}-{BASE['lead']}.json")
            assert original['branch']['before']==prior
            if mode in DESIGN['previous_handoffs'][arm]:
                assert original['first']['physics']==DESIGN['previous_handoffs'][arm][mode]
            if not any(shift) and selected['width_m'] is None:
                assert tape['first']['physics']==original['first']['physics']
            expected = list(prior['integration_state'])
            for name,pos in geometry['object_free_qpos'].items():
                for i,delta in enumerate(shift[name] if isinstance(shift,dict) else shift):
                    expected[1+pos+i] += delta
            for level, slide in slides.items():
                pos, vel = 1 + slide['qpos'], 1 + geometry['nq'] + slide['qvel']
                assert abs(expected[vel]) < 1e-8 and slide['closed'] == 0.
                expected[pos] = slide['closed'] + (displacement if mode == level else 0.)
                expected[vel] = 0.
                assert end['upper']['joints'][LEVELS.index(level)] == expected[pos]
                assert end['upper'][level+'_open'] == (mode==level and arrangement=='full')
            assert dict(prior, integration_state=expected) == after
            assert tape['first']['state'] == ref['first']['state'] and tape['first']['state'][:3] == end['tool']['xyz']
            assert all(end[k] == handoff[k] for k in ('tool','objects'))
            for name, pose in end['objects'].items():
                offset = (shift[name] if isinstance(shift,dict) else shift) if name in geometry['object_free_qpos'] else [0.,0.]
                start = original['handoff']['objects'][name]
                assert np.allclose(np.subtract(pose[:2],start[:2]),offset,atol=1e-12,rtol=0) and pose[2:]==start[2:]
            row = end['upper']
            assert all(row[k] == handoff['upper'][k] for k in ('target_xyz','bowl_xyz'))
            assert not any(row[k] for k in ('top_open','bowl_in','middle_in','bottom_in','bowl_contact'))
            assert not end['robot_contacts'] and not change['slide_contacts']
            holds[mode] = stationary(tape)
            assert holds[mode]['maximum']['drawer_mm'] <= 1.
            coordinates[mode] = [i for i,(a,b) in enumerate(zip(ref['branch']['after']['integration_state'],expected,strict=True)) if a!=b]
            assert coordinates[mode] == ([] if mode=='closed' else [1+slides[mode]['qpos']])
            for level in slides:
                delta = np.subtract(row[level+'_xyz'],handoff['upper'][level+'_xyz'])
                if mode == level:
                    moved[level] = delta.tolist()
                    assert math.isclose(np.linalg.norm(delta),abs(displacement),abs_tol=1e-12) and abs(delta[2])<1e-12
                else:
                    assert not delta.any()
            preps[arm,condition] = tape
        assert np.allclose(moved['middle'],moved['bottom'],atol=1e-12,rtol=0)
        checks[arm] = dict(opening_m=abs(displacement), world_displacement_m=moved, changed_indices_from_closed=coordinates,
                           integration_length=len(prior['integration_state']), stationary=holds,
                           handoffs={mode:t['first']['physics'] for mode,t in cells.items()})
    return preps, checks


def cohorts(entries):
    groups = {'all':list(entries)}
    for arm in COHORT['arms']:
        for block in COHORT['blocks']:
            groups[f'{arm}/b{block}'] = [e for e in entries if e['arm']==arm and e['block']==block]
    return groups


def arrangement_entries(entries, arrangement):
    return [dict(e,mode=e['mode'].split('-')[1]) for e in entries if e['mode'].startswith(arrangement+'-')]


def destination(value):
    return '+'.join(l for l in LEVELS if value[l+'_in']) or 'none'


def matched(entries):
    triplets = {}
    for e in entries:
        triplets.setdefault((e['arm'],e['block'],e['key']),{})[e['mode']] = e['session']
    assert all(set(row)==set(MODES) for row in triplets.values())
    return list(triplets.values())


def compare_native(entries, outcomes, tick):
    cells = {m:summary([outcomes[e['session']][tick] for e in entries if e['mode']==m]) for m in MODES}
    trips = [{m:outcomes[n][tick] for m,n in names.items()} for names in matched(entries)]
    transitions = {}
    for a,b in combinations(MODES,2):
        transitions[a+'_to_'+b] = dict(Counter(destination(row[a])+'->'+destination(row[b]) for row in trips))
    switched = sum(row['middle']['middle_in'] and row['bottom']['bottom_in'] for row in trips)
    return dict(by_mode=cells, destination_transitions=transitions, opened_drawer_switches=switched, pairs=len(trips))


def score(out):
    src = out/'sources'
    runtime = read(out/'runtime.json')
    assert DESIGN == read(out/'design.json') == read(src/DESIGN_FILE)
    assert DESIGN['cohort'] == LAYOUT2_FILE and sha(src/LAYOUT2_FILE) == DESIGN['cohort_sha256']
    assert all(sha(src/n)==h for n,h in runtime['sources'].items())
    assert digest(runtime['checkpoint']) == BASE['checkpoint_manifest_sha256']
    assert read(src/COHORT['task_design'])==TASK and sha(src/TASK['bddl'])==TASK['bddl_sha256']
    check_freeze(src)
    check_donors(src,COHORT)
    entries = planned(COHORT,modes=CONDITIONS)
    check_sessions(out,entries,COHORT['blocks'])
    keys, qual = read(out/'rng.json'),read(out/'qualification.json')
    assert digest(keys) == DESIGN['rng_sha256'] and 'NVIDIA' in qual['renderer']
    preps, checks = qualify_starts(out,qual['geometry'])
    assert checks == qual['starts']
    geometry = contact_geometry(qual['geometry'])
    frames, outcomes, firsts = set(), {}, {}
    for name,e in entries.items():
        outcomes[name],firsts[name] = path_outcomes(out,e,preps[e['arm'],e['mode']],geometry,keys,frames)
    differences,comparisons,follows = {},{},{}
    for arr in ARRANGEMENTS:
        subset = arrangement_entries(entries.values(),arr)
        differences[arr] = {}
        for a,b in combinations(MODES,2):
            counts = Counter()
            for trip in matched(subset):
                x,y = firsts[trip[a]],firsts[trip[b]]
                assert x['state']==y['state']
                for camera in x['live']:
                    counts[camera] += x['live'][camera]!=y['live'][camera]
                counts['first_command'] += x['reply'][0]!=y['reply'][0]
            differences[arr][a+'_to_'+b] = dict(counts)
        comparisons[arr] = {g:{t:compare_native(values,outcomes,t) for t in TIMES} for g,values in cohorts(subset).items()}
        follows[arr] = all(2*cell[TIMES[-1]]['opened_drawer_switches']>cell[TIMES[-1]]['pairs']
                           for g,cell in comparisons[arr].items() if g!='all')
    clearance = read(out/'clearance.json')
    return dict(figure_name='drawer_location.png', paths=len(entries), unique_donor_seed_pairs=len(COHORT['arms'])*len(BASE['stove_seeds']),
                clearance=clearance['arrangements'], original_clear={a:{m:v['clear'] for m,v in cells.items()} for a,cells in clearance['original'].items()},
                prefix_controls=sum(e['prefix_controls'] for e in entries.values()), evaluated_controls=sum(e['horizon'] for e in entries.values()),
                policy_queries=sum(e['queries'] for e in entries.values()), physical_starts=checks, first_differences=differences,
                comparisons=comparisons, usual_destination_follows_open_drawer=follows, outcomes=outcomes)


def cross_scores(out, proof, reference):
    entries = planned(COHORT,modes=CONDITIONS)
    check_replayed_paths(out,proof,entries,{})
    assert proof['schema'] == dict(flags=list(FLAGS),contacts=list(CONTACTS))
    assert proof['alternatives_per_path']==len(MODES)-1
    starts = reference['physical_starts']
    geometry = contact_geometry(read(out/'qualification.json')['geometry'])
    preps = {(a,m):read(out/'preparation'/f"{a}-{m}-{BASE['lead']}.json") for a in COHORT['arms'] for m in CONDITIONS}
    outcomes = {}
    for r in proof['runs']:
        name = r['session']
        e = entries[name]
        arm = e['arm']
        arr,source = e['mode'].split('-')
        path = read(out/'paths'/(name+'.json'))
        control_hash = digest([row['action'] for row in path['rows']])
        own = event_trace([preps[arm,e['mode']]['handoff']['upper'],*path['rows']],geometry,FLAGS)
        assert set(r['alternates']) == set(MODES)-{source}
        traces = {source:own}
        for mode,v in r['alternates'].items():
            assert v['mode']==f'{arr}-{mode}' and v['controls']==r['policy_controls'] and v['commands_sha256']==control_hash
            assert v['handoff']==starts[arr][arm]['handoffs'][mode] and len(v['final_physics'])==len(v['measurements_sha256'])==64
            traces[mode] = v['trace']
        for mode,trace in traces.items():
            rows, contacts = read_trace(trace,FLAGS)
            vals = {t:outcome(rows,contacts,int(t)-e['lead']) for t in TIMES}
            if mode==source:
                assert vals==reference['outcomes'][name]
            outcomes[name,mode] = vals
    assert proof['alternate_controls']==sum(v['controls'] for r in proof['runs'] for v in r['alternates'].values())
    return {arr:cross_matrix(arrangement_entries(entries.values(),arr),outcomes) for arr in ARRANGEMENTS}


def cross_matrix(entries,outcomes):
    matrix = {}
    for group, subset in cohorts(entries).items():
        matrix[group] = {}
        trips = matched(subset)
        for t in TIMES:
            cells = {source:{mode:summary([outcomes[trip[source],mode][t] for trip in trips]) for mode in MODES} for source in MODES}
            success = [trip for trip in trips if outcomes[trip['closed'],'closed'][t]['top_in']]
            cells['closed_success_on_bottom'] = dict(eligible=len(success), retained=sum(outcomes[trip['closed'],'bottom'][t]['top_in'] for trip in success))
            matrix[group][t] = cells
    return matrix


def collect(out):
    from run_atomic import SIM_PYTHON
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block
    sources = [DESIGN_FILE,LAYOUT2_FILE,'drawer/middle_aperture.json',COHORT['task_design'],TASK['bddl'],
               COHORT['donor_design'],COHORT['donors'],SIM,'drawer_location.py','middle_aperture_sim.py','verify_middle_aperture.py',
               'replay_middle_aperture.py','stove_finger_sim.py','verify_stove_fingers.py','upper_bowl_sim.py','verify_upper_bowl.py',
               'verify_atomic.py','verify_layouts.py','plot_drawer_location.py','drawer_location_clearance.py']
    initialize_study(out,DESIGN,sources,key_count=BASE['key_offset']+TASK['extension']//BASE['period'])
    check_donors(out/'sources',COHORT)
    entries = planned(COHORT,modes=CONDITIONS)
    write_json(out/'sessions.json',entries)
    sim = [SIM_PYTHON,str(PACKET/SIM),str(out)]
    subprocess.run([*sim,'prepare'],check=True)
    for b in COHORT['blocks']:
        subset = [e for e in entries.values() if e['block']==b]
        policy_block(out,sim,subset,f'block-{b}',f'policy-{b}.log',workers=4)
        print('Completed model load',b,'paths',len(subset),flush=True)
    write_json(out/'verification.json',score(out))


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('stage',choices=('collect','verify','replay'),default='verify',nargs='?')
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    if args.stage=='collect':
        collect(args.folder)
    else:
        with unpack(args.folder) as out:
            result = read(args.folder/'verification.json')
            entries = planned(COHORT,modes=CONDITIONS)
            if args.stage=='replay':
                proof = replay(out,script=SIM,entries=entries,workers=8)
                proof.update(schema=dict(flags=list(FLAGS),contacts=list(CONTACTS)),alternatives_per_path=len(MODES)-1,
                             alternate_controls=sum(v['controls'] for r in proof['runs'] for v in r['alternates'].values()),
                             replay_source_sha256=sha(PACKET/SIM))
                proof['crossover'] = cross_scores(out,proof,result)
                if args.output:
                    if args.output.exists():
                        raise FileExistsError(args.output)
                    write_json(args.output,proof)
                else:
                    print(json.dumps(proof))
                print('Physically replayed',len(entries),'native and',len(entries)*(len(MODES)-1),'crossed paths')
            else:
                assert score(out)==result
                proof_file = args.folder/'physical_replay.json'
                if proof_file.is_file():
                    proof = read(proof_file)
                    assert sha(out/'sources'/SIM)==proof['replay_source_sha256']
                    assert cross_scores(out,proof,result)==proof['crossover']
                    if 'archive_repeat' in proof:
                        check_archive_repeat(args.folder,out,proof,entries)
                print('Verified',len(entries),'paths, three drawer positions, two arrangements, two model loads')
