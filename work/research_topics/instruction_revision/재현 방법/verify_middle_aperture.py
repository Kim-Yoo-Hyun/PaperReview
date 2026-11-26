"""Run, score and independently replay paired middle-slide interventions in Docker."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import subprocess
from zipfile import ZipFile

import numpy as np

from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_stove import numbers, sha
from verify_stove_fingers import DESIGN as FINGERS, donor_trace
from verify_stove_layouts import DESIGN as BASE, check_freeze, check_replayed_paths, digest, replay
from verify_stove_pose import PLAN, angle, check_receipts, pose_error
from verify_upper_bowl import DESIGN as TASK, NEUTRAL, check_rows, planned as upper_plan


DESIGN_FILE = 'drawer/middle_aperture.json'
LAYOUT2_FILE = 'drawer/middle_aperture_layout2.json'
DESIGN = read(PACKET/DESIGN_FILE)
ORIGINAL = {**FINGERS, **DESIGN, 'design_file':DESIGN_FILE, 'prefix_contact':True}
LEVELS = ('top', 'middle', 'bottom')


def study_for(raw):
    if raw == DESIGN:
        return ORIGINAL
    assert raw == read(PACKET/LAYOUT2_FILE) and sha(PACKET/DESIGN_FILE)==raw['template_sha256']
    return {**ORIGINAL, **raw, 'design_file':LAYOUT2_FILE}


def recorded_study(out):
    return study_for(read(out/'design.json'))


def direct_plan():
    return {n:e for n,e in upper_plan().items() if e['arm']==NEUTRAL}


def check_donors(sources, study):
    donors = read(sources/study['donors'])
    assert digest(donors)==study['donors_sha256']
    assert [donors[n]['final'] for n in study['arms']]==study['donor_physics']
    if 'donor_archive' not in study:
        return
    assert set(donors)==set(study['arms'])
    assert all(donors[n]['returned']==study['returned_physics'][n] and
               donors[n]['end_contact']==study['prefix_contact'] for n in donors)
    parent = PACKET/study['donor_archive']
    if parent.is_file():
        assert sha(parent)==study['donor_archive_sha256']
        with ZipFile(parent) as z:
            gate = json.loads(z.read('gate.json'))[str(study['layout'])]
            assert gate['competent'] and gate['unique_donor_states']==len(donors)
            seen = {}
            for name in sorted(gate['donors']):
                src = json.loads(z.read(f'gates/{name}.json'))
                prep = json.loads(z.read(f"preparation/{name}-pose-{BASE['lead']}.json"))
                assert src['layout']==study['layout'] and src['task']=='drawer' and src['rows'][-1]['drawer_open']
                arm = seen.setdefault(src['final_physics'],name)
                assert donors[arm]==dict(donor_trace(src), returned=prep['first']['physics'],
                                         end_contact=src['rows'][-1]['drawer_contact'])
            assert set(seen.values())==set(donors)


def planned(study=ORIGINAL, *, modes=None):
    entries = {}
    for block in study['blocks']:
        group = []
        for i, arm in enumerate(study['arms']):
            for key in BASE['stove_seeds']:
                if modes is None:
                    order = DESIGN['modes'] if (i + key) % 2 == 0 else reversed(DESIGN['modes'])
                else:
                    offset = (i + key) % len(modes)
                    order = modes[offset:] + modes[:offset]
                for mode in order:
                    name = f'{arm}-{mode}-b{block}-s{key}'
                    group.append(dict(session=name, arm=arm, mode=mode, block=block, key=key,
                                      lead=BASE['lead'], horizon=TASK['extension'], source=TASK['prompt'],
                                      prefix_controls=BASE['drawer_horizon'], key_offset=BASE['key_offset'],
                                      queries=(TASK['extension']-BASE['lead'])//BASE['period'],
                                      receipts=f'receipts/{name}.jsonl'))
        for entry in group if block == 1 else reversed(group):
            entries[entry['session']] = entry
    return entries


def stationary(tape):
    start, samples = tape['handoff'], tape['stationary']
    assert len(samples) == DESIGN['hold_controls'] and all(not s['robot_contacts'] and not s['slide_contacts'] for s in samples)
    poses = [pose_error(s['tool'], start['tool']) for s in samples]
    maxima = {k:max(p[k] for p in poses) for k in poses[0]}
    maxima['object_mm'] = 1000 * max(math.dist(v[:3], s['objects'][n][:3])
                                     for s in samples for n,v in start['objects'].items())
    maxima['object_deg'] = max(angle(v[3:], s['objects'][n][3:]) for s in samples for n,v in start['objects'].items())
    maxima['drawer_mm'] = 1000 * max(abs(a-b) for s in samples for a,b in zip(s['joints'], start['upper']['joints']))
    assert all(v <= PLAN['limits'][k] for k,v in maxima.items()), maxima
    middle_drift = max(abs(s['joints'][1]-start['upper']['joints'][1]) for s in samples)
    assert middle_drift <= DESIGN['max_middle_drift_m']
    return dict(maximum=maxima, middle_drift_m=middle_drift)


def qualify_pairs(out, geometry, study=ORIGINAL):
    tapes, summaries = {}, {}
    pos = 1 + geometry['slide_qpos']  # mjSTATE_INTEGRATION starts with time then qpos.
    vel = 1 + geometry['nq'] + geometry['slide_qvel']
    for arm, expected in zip(study['arms'], study['donor_physics'], strict=True):
        holds, branches = {}, {}
        for mode in DESIGN['modes']:
            tape = read(out/'preparation'/f"{arm}-{mode}-{BASE['lead']}.json")
            assert (tape['arm'],tape['mode'],tape['length'],tape['donor_physics']) == (arm,mode,BASE['lead'],expected)
            before, after = (tape['branch'][k] for k in ('before','after'))
            assert len(tape['actions']) == len(tape['rows']) == BASE['lead']
            assert digest(before) == study['returned_physics'][arm] and digest(after) == tape['first']['physics']
            assert {k:v for k,v in before.items() if k != 'integration_state'} == {k:v for k,v in after.items() if k != 'integration_state'}
            values = list(before['integration_state'])
            assert values[pos] == tape['rows'][-1]['upper']['joints'][1] and abs(values[vel]) < 1e-8
            if mode == 'closed':
                values[pos] = tape['branch']['closed_reference']
            values[vel] = 0.
            assert values == after['integration_state']
            row = tape['handoff']['upper']
            assert values[pos] == row['joints'][1]
            assert row['middle_open'] == (mode=='open') and not row['top_open']
            assert not any(row[k] for k in ('bowl_in','middle_in','bottom_in','bowl_contact'))
            assert row['joints'][1] < geometry['open_below_m'] if mode == 'open' else row['joints'][1] == 0.
            assert not tape['handoff']['robot_contacts'] and not tape['branch']['slide_contacts']
            assert not tape['rows'][-1]['robot_contacts']
            assert tape['start']['stove']['drawer_open'] and tape['start']['stove']['drawer_contact']==study['prefix_contact']
            assert tape['first']['state'][:3] == tape['handoff']['tool']['xyz']
            handoff_speed = max(map(abs, tape['handoff']['tool']['velocity']))
            assert handoff_speed <= PLAN['limits']['final_velocity_rad_s']
            holds[mode] = stationary(tape)
            tapes[arm,mode] = branches[mode] = tape
        a, b = branches['open'], branches['closed']
        assert all(a[k] == b[k] for k in ('common','start','rows','actions','donor_physics'))
        assert a['branch']['before'] == b['branch']['before']
        assert a['first']['state'] == b['first']['state']
        ah, bh = a['handoff'], b['handoff']
        assert ah['tool'] == bh['tool'] and ah['objects'] == bh['objects']
        assert all(ah['upper'][k] == bh['upper'][k] for k in ('target_xyz','bowl_xyz','bottom_xyz'))
        av, bv = (t['branch']['after']['integration_state'] for t in (a,b))
        assert [i for i,(x,y) in enumerate(zip(av,bv,strict=True)) if x!=y] == [pos]
        summaries[arm] = dict(returned=study['returned_physics'][arm], open_m=av[pos], closed_m=bv[pos],
                              only_changed_integration_index=pos, integration_length=len(av), slide_velocity_m_s=av[vel],
                              peak_arm_velocity_rad_s=max(map(abs,ah['tool']['velocity'])), stationary=holds)
    return tapes,summaries


def contact_geometry(raw):
    geometry = dict(raw)
    for key in (*LEVELS,'bowl','fingers','robot_geoms'):
        geometry[key] = set(geometry[key])
    geometry['targets'] = set.union(*(geometry[k] for k in (*LEVELS,'bowl')))
    return geometry


def targets(row, geometry):
    other = {g for _,g in row['gripper_pairs']} - geometry['robot_geoms']
    labels = {k for k in (*LEVELS,'bowl') if other & geometry[k]}
    if other - geometry['targets']:
        labels.add('other')
    return sorted(labels)


def check_destinations(rows, geometry):
    check_rows(rows, geometry)
    if 'bottom_open' in rows[0]:
        assert all(r['bottom_open'] == (r['joints'][2] < geometry['open_below_m']) for r in rows)
    xyz = np.asarray([r['bowl_xyz'] for r in rows])
    for level in ('middle','bottom'):
        center = np.asarray([r[level+'_xyz'] for r in rows])
        extent = np.asarray(geometry[level+'_extent'])
        lower = center - extent
        lower[:,2] -= geometry['lower_z_allowance_m']
        inside = ((xyz > lower) & (xyz < center + extent)).all(axis=1)
        assert np.array_equal(inside, [r[level+'_in'] for r in rows])
        assert all(a in geometry['bowl'] and b in geometry[level] for r in rows for a,b in r[level+'_pairs'])


def outcome(rows, contacts, tick):
    section = rows[:tick+1]
    end = section[-1]
    first = {k:next((i for i,r in enumerate(section) if r[k]),None) for k in
             ('top_contact','top_open','bowl_contact','bowl_in','middle_in','bottom_in')}
    def first_target(include_other):
        for i,labels in enumerate(contacts[:tick+1]):
            selected = labels if include_other else [v for v in labels if v!='other']
            if selected:
                return dict(tick=i, target='+'.join(selected))
        return dict(tick=None, target='none')
    result = dict(first=first, first_external=first_target(True), first_task_contact=first_target(False),
                  top_open=end['top_open'], middle_open=end['middle_open'])
    if 'bottom_open' in end:
        result['bottom_open'] = end['bottom_open']
    for level, key, pairs in [('top','bowl_in','bowl_top_pairs'),('middle','middle_in','middle_pairs'),
                              ('bottom','bottom_in','bottom_pairs')]:
        result[level+'_in'] = end[key]
        result[level+'_supported'] = end[key] and bool(end[pairs])
        result[level+'_released'] = all(r[key] and not r['bowl_contact'] for r in section[-TASK['release_window']:])
    return result


def summary(values):
    return dict(paths=len(values), counts={k:sum(v[k] for v in values) for k in values[0] if isinstance(values[0][k],bool)},
                first={k:numbers([v['first'][k] for v in values]) for k in values[0]['first']},
                first_external=dict(Counter(v['first_external']['target'] for v in values)),
                first_task_contact=dict(Counter(v['first_task_contact']['target'] for v in values)))


def comparison(entries, outcomes, tick):
    by_mode, pairs = {}, {}
    for mode in DESIGN['modes']:
        values = [outcomes[e['session']][str(tick)] for e in entries if e['mode']==mode]
        by_mode[mode] = summary(values)
    indexed = {(e['arm'],e['block'],e['key'],e['mode']):outcomes[e['session']][str(tick)] for e in entries}
    for endpoint in ('top_in','middle_in','top_open','top_released','middle_released'):
        counts = Counter((o[endpoint],indexed[(*k[:-1],'closed')][endpoint]) for k,o in indexed.items() if k[-1]=='open')
        pairs[endpoint] = dict(open_only=counts[True,False],closed_only=counts[False,True],
                               both=counts[True,True],neither=counts[False,False])
    return dict(by_mode=by_mode, paired=pairs)


def path_outcomes(out, entry, prep, geometry, keys, frames, *, first_images=None,sent_by_tick=None,tape=None):
    if tape is None:
        tape = read(out/'paths'/(entry['session']+'.json'))
    assert all(tape[k]==entry[k] for k in ('session','arm','mode','block','lead')) and tape['seed']==entry['key']
    check_receipts(out,entry,tape,keys,frames,prep['first'],first_images=first_images,sent_by_tick=sent_by_tick)
    rows = [prep['handoff']['upper'],*tape['rows']]
    assert len(rows)==entry['horizon']-entry['lead']+1
    check_destinations(rows,geometry)
    contacts = [targets(r,geometry) for r in rows]
    return {str(t):outcome(rows,contacts,t-entry['lead']) for t in TASK['deadlines']},tape['queries'][0]


def check_sessions(out, entries, blocks):
    assert entries==read(out/'sessions.json')
    for b in blocks:
        assert read(out/f'block-{b}.json') == [e for e in entries.values() if e['block']==b]
    assert set(entries)=={p.stem for p in (out/'paths').glob('*.json')}=={p.stem for p in (out/'receipts').glob('*.jsonl')}


def score_standalone(root, study):
    out = root/'standalone'
    entries = direct_plan()
    check_sessions(out,entries,study['blocks'])
    keys = read(root/'rng.json')
    assert digest(keys)==study['rng_sha256']
    qual = read(out/'qualification.json')
    assert 'NVIDIA' in qual['renderer']
    geometry = contact_geometry(qual['geometry'])
    prep = read(out/'preparation'/f'{NEUTRAL}-immediate-0.json')
    donors = read(root/'sources'/study['donors'])
    assert all(d['initial']==prep['donor_physics']==prep['first']['physics'] for d in donors.values())
    assert prep['mode']=='immediate' and prep['arm']==NEUTRAL and prep['length']==0 and prep['rows']==prep['actions']==[]
    assert prep['start']==prep['handoff']
    initial = prep['handoff']['upper']
    assert not any(initial[k] for k in ('top_open','middle_open','bowl_in','middle_in','bottom_in'))
    frames = set()
    outcomes = {n:path_outcomes(out,e,prep,geometry,keys,frames)[0] for n,e in entries.items()}
    groups = {'all':list(entries)}
    groups.update({f'b{b}':[n for n,e in entries.items() if e['block']==b] for b in study['blocks']})
    scores = {g:{str(t):summary([outcomes[n][str(t)] for n in names]) for t in TASK['deadlines']} for g,names in groups.items()}
    competence = {g:sum(outcomes[n][str(TASK['primary'])]['top_in'] and
                        outcomes[n][str(TASK['primary'])]['first']['top_open'] is not None for n in names)
                  for g,names in groups.items() if g!='all'}
    return dict(paths=len(entries),controls=sum(e['horizon'] for e in entries.values()),
                policy_queries=sum(e['queries'] for e in entries.values()), initial=prep['first']['physics'],
                primary_success_by_block=competence, primary_pass=all(v>0 for v in competence.values()),
                groups=scores,outcomes=outcomes)


def score(out):
    sources = out/'sources'
    check_freeze(sources)
    runtime, qual = read(out/'runtime.json'), read(out/'qualification.json')
    study = recorded_study(out)
    assert read(out/'design.json') == read(sources/study['design_file'])
    assert all(sha(sources/n)==v for n,v in runtime['sources'].items())
    assert read(sources/study['task_design'])==TASK and sha(sources/TASK['bddl'])==TASK['bddl_sha256']
    assert read(sources/study['donor_design'])==FINGERS
    check_donors(sources,study)
    assert digest(runtime['checkpoint'])==BASE['checkpoint_manifest_sha256'] and 'NVIDIA' in qual['renderer']
    keys = read(out/'rng.json')
    assert digest(keys)==DESIGN['rng_sha256']==TASK['rng_sha256']
    entries = planned(study)
    check_sessions(out,entries,study['blocks'])
    preps, checks = qualify_pairs(out, qual['geometry'],study)
    assert checks == qual['pairs']
    geometry = contact_geometry(qual['geometry'])
    frames, outcomes, signatures = set(), {}, {}
    for name,e in entries.items():
        prep = preps[e['arm'],e['mode']]
        outcomes[name], signatures[e['arm'],e['block'],e['key'],e['mode']] = path_outcomes(out,e,prep,geometry,keys,frames)
    matches = Counter()
    for k,a in signatures.items():
        if k[-1] != 'open':
            continue
        b = signatures[(*k[:-1],'closed')]
        assert a['state']==b['state'] and a['live'].keys()==b['live'].keys()
        for camera in a['live']:
            matches[camera] += a['live'][camera]!=b['live'][camera]
        matches['first_command'] += a['reply'][0]!=b['reply'][0]
    groups = {'all':list(entries.values())}
    for arm in study['arms']:
        for block in study['blocks']:
            groups[f'{arm}/b{block}'] = [e for e in entries.values() if e['arm']==arm and e['block']==block]
    comparisons = {n:{str(t):comparison(subset,outcomes,t) for t in TASK['deadlines']} for n,subset in groups.items()}
    direction = {}
    for t in TASK['deadlines']:
        cells = [ss[str(t)]['paired']['top_in'] for g,ss in comparisons.items() if g!='all']
        direction[str(t)] = dict(closed_ahead_in_all_cells=all(c['closed_only']>c['open_only'] for c in cells),
                                 open_ahead_in_all_cells=all(c['open_only']>c['closed_only'] for c in cells))
    result = dict(paths=len(entries), unique_donor_seed_pairs=len(study['arms'])*len(BASE['stove_seeds']),
                prefix_controls=sum(e['prefix_controls'] for e in entries.values()),
                evaluated_controls=sum(e['horizon'] for e in entries.values()),
                policy_queries=sum(e['queries'] for e in entries.values()), first_input_or_action_differences=dict(matches),
                physical_pairs=checks, comparisons=comparisons, direction=direction, outcomes=outcomes)
    if 'standalone' in study:
        assert qual['geometry']==read(out/'standalone/qualification.json')['geometry']
        result['standalone'] = score_standalone(out,study)
        assert result['standalone']==read(out/'standalone_gate.json')
        result['primary_closure_replicated'] = (result['standalone']['primary_pass'] and
                                                direction[str(TASK['primary'])]['closed_ahead_in_all_cells'])
    return result


def collect(out, design_file=DESIGN_FILE):
    from run_atomic import SIM_PYTHON
    from run_stove_layouts import initialize_study
    from run_stove_pose import policy_block
    raw = read(PACKET/design_file)
    study = study_for(raw)
    extra = [DESIGN_FILE,study['task_design'],TASK['bddl'],study['donor_design'],study['donors'],
             'verify_stove_fingers.py','stove_finger_sim.py','upper_bowl_sim.py','verify_upper_bowl.py',
             'middle_aperture_sim.py','verify_middle_aperture.py','verify_atomic.py','verify_layouts.py',
             'replay_middle_aperture.py','plot_middle_aperture.py']
    if design_file!=DESIGN_FILE:
        extra.append(design_file)
    initialize_study(out,raw,extra,key_count=BASE['key_offset']+TASK['extension']//BASE['period'])
    check_donors(out/'sources',study)
    def run_blocks(folder, entries):
        sim = [SIM_PYTHON,str(PACKET/'middle_aperture_sim.py'),str(folder)]
        for b in study['blocks']:
            subset = [e for e in entries.values() if e['block']==b]
            policy_block(folder,sim,subset,f'block-{b}',f'policy-{b}.log')
            print(f'Finished {folder.name} model load {b}, {len(subset)} paths',flush=True)
    sim = [SIM_PYTHON,str(PACKET/'middle_aperture_sim.py'),str(out)]
    if 'standalone' in study:
        direct = out/'standalone'
        for d in ('preparation','paths','frames','receipts','logs'):
            (direct/d).mkdir(parents=True)
        gates = direct_plan()
        write_json(direct/'sessions.json',gates)
        subprocess.run([*sim,'prepare-standalone'],check=True)
        run_blocks(direct,gates)
        gate = score_standalone(out,study)
        write_json(out/'standalone_gate.json',gate)
        print('Standalone primary successes by model load',gate['primary_success_by_block'],flush=True)
    entries = planned(study)
    write_json(out/'sessions.json',entries)
    subprocess.run([*sim,'prepare'],check=True)
    run_blocks(out,entries)
    write_json(out/'verification.json',score(out))


def check_archive_repeat(folder, out, proof, entries=None):
    # The second report is identical except for explicitly recorded rerender differences.
    repeat = dict(proof)
    metadata = repeat.pop('archive_repeat')
    overrides = metadata['rerender_overrides']
    assert set(overrides) <= {r['session'] for r in proof['runs']}
    repeat['runs'] = [dict(r, changed_rgb_ticks=overrides.get(r['session'],r['changed_rgb_ticks'])) for r in proof['runs']]
    if 'standalone' in proof:
        runs = proof['standalone']['runs']
        changed = metadata['standalone_rerender_overrides']
        assert set(changed) <= {r['session'] for r in runs}
        repeat['standalone'] = dict(proof['standalone'],runs=[dict(r,changed_rgb_ticks=changed.get(r['session'],r['changed_rgb_ticks'])) for r in runs])
        check_replayed_paths(out/'standalone',repeat['standalone'],direct_plan(),{})
    assert digest(repeat) == metadata['repeat_report_digest']
    assert sha(folder/'study.zip') == metadata['source_zip_sha256']
    check_replayed_paths(out, repeat, planned(recorded_study(out)) if entries is None else entries, {})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('stage',choices=['collect','replay','verify'],default='verify',nargs='?')
    parser.add_argument('--output',type=Path)
    parser.add_argument('--layout',type=int,choices=[2,3],default=3,help='Layout for a new collection')
    args = parser.parse_args()
    if args.stage=='collect':
        collect(args.folder,LAYOUT2_FILE if args.layout==2 else DESIGN_FILE)
    else:
        with unpack(args.folder) as out:
            if args.stage=='replay':
                entries = planned(recorded_study(out))
                report = replay(out,script='middle_aperture_sim.py',entries=entries)
                check_replayed_paths(out,report,entries,{})
                if args.output:
                    write_json(args.output,report)
                else:
                    print(json.dumps(report))
                print(f"Physically replayed {report['paths']} paths")
            else:
                result = score(out)
                assert result==read(args.folder/'verification.json')
                if (args.folder/'physical_replay.json').is_file():
                    proof = read(args.folder/'physical_replay.json')
                    check_replayed_paths(out,proof,planned(recorded_study(out)),{})
                    if 'standalone' in result:
                        check_replayed_paths(out/'standalone',proof['standalone'],direct_plan(),{})
                    if 'crossover' in proof:
                        from replay_middle_aperture import crossover
                        assert proof['crossover'] == crossover(out,proof,result)
                        assert proof['alternate_controls'] == sum(r['policy_controls'] for r in proof['runs'])
                        archived = out/'sources/replay_middle_aperture.py'
                        if archived.is_file():
                            assert proof['replay_source_sha256'] == sha(archived)
                    if 'archive_repeat' in proof:
                        check_archive_repeat(args.folder,out,proof)
                print(f"Verified {result['paths']} matched open and closed paths")
                if 'standalone' in result:
                    print(f"Verified {result['standalone']['paths']} standalone paths")
