"""Replay every native path and cross each complete command sequence onto the other slide position."""
import argparse
from collections import Counter
from itertools import groupby
import json
from pathlib import Path

from inside import write_json
from verify_atomic import PACKET, read
from verify_layouts import unpack
from verify_middle_aperture import (BASE, DESIGN, LEVELS, TASK, check_destinations, contact_geometry, direct_plan,
                                    outcome, planned, recorded_study, summary, targets)
from verify_stove import sha
from verify_stove_layouts import check_replayed_paths, digest, replay


# Every path contributes both geometries. Sampling and endpoints are fixed before
# opening the policy outcomes; success in the alternate world needs no live replan.
FLAGS = ('top_contact','top_open','middle_open','bowl_contact','bowl_in','middle_in','bottom_in',
         'bowl_top_pairs','middle_pairs','bottom_pairs')
CONTACTS = (*LEVELS,'bowl','other')


def event_trace(rows, geometry, flags=FLAGS):
    masks = []
    for row in rows:
        touched = targets(row,geometry)
        bits = [bool(row[k]) for k in flags] + [k in touched for k in CONTACTS]
        masks.append(sum(1 << i for i,flag in enumerate(bits) if flag))
    return [[m,sum(1 for _ in same)] for m,same in groupby(masks)]


def read_trace(trace, flags=FLAGS):
    rows, contacts = [], []
    for mask, length in trace:
        assert 0 <= mask < 1 << (len(flags)+len(CONTACTS)) and length > 0
        bits = [bool(mask & (1 << i)) for i in range(len(flags)+len(CONTACTS))]
        rows.extend([dict(zip(flags,bits[:len(flags)]))]*length)
        contacts.extend([sorted(k for k,flag in zip(CONTACTS,bits[len(flags):]) if flag)]*length)
    assert len(rows)==TASK['extension']-BASE['lead']+1
    return rows,contacts


def replay_one(out,e):
    from middle_aperture_sim import Cabinet,branch,run_path
    study = recorded_study(out)
    native = run_path(out,e,replay=True)
    alternate = next(m for m in DESIGN['modes'] if m != e['mode'])
    src = read(out/'paths'/(e['session']+'.json'))
    commands = [r['action'] for r in src['rows']]
    native['alternate'] = play_commands(out,e,commands,alternate,study,Cabinet,branch)
    return native


def play_commands(out, e, commands, alternate, study, scene_type, prepare_fn, flags=FLAGS):
    from atomic_control import capture_state
    from drawer_sim import observe,state_hash
    from middle_aperture_sim import environment,restore
    arm = e['arm']
    expected = read(out/'preparation'/f"{arm}-{alternate}-{e['lead']}.json")
    env = environment(arm,layout=study['layout'])
    try:
        scene = scene_type(env)
        common = restore(env,scene,arm,out,donors_file=study['donors'])
        assert state_hash(capture_state(env))==expected['donor_physics']
        prep = prepare_fn(env,scene,common,alternate,e['lead'])
        assert all(v==expected[k] for k,v in prep.items())
        handoff = scene.read()
        assert handoff==expected['handoff']
        rows = [handoff['upper']]
        for i,cmd in enumerate(commands):
            if i % BASE['period']==0:
                _, sample = observe(env,out,False,TASK['prompt'])
                if i==0:
                    assert (sample['physics'],sample['state'])==(expected['first']['physics'],expected['first']['state'])
            env.step(cmd)
            rows.append(scene.policy_row())
        geometry = contact_geometry(scene.geometry)
        check_destinations(rows,geometry)
        return dict(mode=alternate, controls=len(commands), commands_sha256=digest(commands),
                    handoff=expected['first']['physics'], final_physics=state_hash(capture_state(env)),
                    measurements_sha256=digest(rows), trace=event_trace(rows,geometry,flags))
    finally:
        env.close()


def crossover(out, report, native_result):
    study = recorded_study(out)
    entries = planned(study)
    check_replayed_paths(out,report,entries,{})
    assert report['schema']==dict(flags=list(FLAGS),contacts=list(CONTACTS))
    assert len(report['runs'])==native_result['paths']
    geometry = contact_geometry(read(out/'qualification.json')['geometry'])
    preps = {(arm,m):read(out/'preparation'/f"{arm}-{m}-{BASE['lead']}.json") for arm in study['arms'] for m in DESIGN['modes']}
    outcomes = {}
    for r in report['runs']:
        name = r['session']
        e, cross = entries[name],r['alternate']
        src = read(out/'paths'/(name+'.json'))
        prep = preps[e['arm'],e['mode']]
        opposite = cross['mode']
        assert opposite in DESIGN['modes'] and opposite != e['mode']
        assert cross['handoff']==preps[e['arm'],opposite]['first']['physics']
        assert cross['controls']==r['policy_controls'] and cross['commands_sha256']==digest([v['action'] for v in src['rows']])
        assert len(cross['final_physics'])==len(cross['measurements_sha256'])==64
        own = event_trace([prep['handoff']['upper'],*src['rows']],geometry)
        for mode,trace in [(e['mode'],own),(opposite,cross['trace'])]:
            rows,grip = read_trace(trace)
            scores = {str(t):outcome(rows,grip,t-e['lead']) for t in TASK['deadlines']}
            if mode == e['mode']:
                assert scores==native_result['outcomes'][name]
            outcomes[name,mode] = scores
    groups = {'all':list(entries.values())}
    for arm in study['arms']:
        for b in study['blocks']:
            groups[f'{arm}/b{b}'] = [e for e in entries.values() if e['arm']==arm and e['block']==b]
    matrix = {}
    for group, subset in groups.items():
        matrix[group] = {}
        for t in map(str,TASK['deadlines']):
            cells = {}
            for source in DESIGN['modes']:
                names = [e['session'] for e in subset if e['mode']==source]
                values = {scene:[outcomes[n,scene][t] for n in names] for scene in DESIGN['modes']}
                paired = {}
                for key in ('top_open','top_in','middle_in'):
                    counts = Counter((a[key],b[key]) for a,b in zip(values['open'],values['closed'],strict=True))
                    paired[key] = dict(open_only=counts[True,False],closed_only=counts[False,True],
                                       both=counts[True,True],neither=counts[False,False])
                cells[source] = dict(open=summary(values['open']),closed=summary(values['closed']),paired=paired)
            if 'standalone' in study:
                # Both command sources face the very same open physical scene.
                key_to_scores = {(e['arm'],e['block'],e['key'],e['mode']):outcomes[e['session'],'open'][t] for e in subset}
                pairs = [(a,key_to_scores[(*k[:-1],'closed')]) for k,a in key_to_scores.items() if k[-1]=='open']
                cells['command_pairs_in_open_scene'] = {}
                for key in ('top_in','middle_in'):
                    counts = Counter((a[key],b[key]) for a,b in pairs)
                    cells['command_pairs_in_open_scene'][key] = dict(open_only=counts[True,False],closed_only=counts[False,True],
                                                                    both=counts[True,True],neither=counts[False,False])
            matrix[group][t] = cells
    return matrix


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folder',type=Path)
    parser.add_argument('stage',choices=['replay','one','verify'],nargs='?',default='verify')
    parser.add_argument('session',nargs='?')
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    if args.stage=='one' or (args.stage=='replay' and args.session):
        print(json.dumps(replay_one(args.folder,planned(recorded_study(args.folder))[args.session])))
    else:
        with unpack(args.folder) as out:
            reference = read(args.folder/'verification.json')
            if args.stage=='verify':
                proof = read(args.folder/'physical_replay.json')
                assert proof['crossover']==crossover(out,proof,reference)
            else:
                study = recorded_study(out)
                proof = replay(out,script=Path(__file__).name,entries=planned(study))
                if 'standalone' in study:
                    proof['standalone'] = replay(out/'standalone',script='middle_aperture_sim.py',entries=direct_plan())
                proof['schema'] = dict(flags=list(FLAGS),contacts=list(CONTACTS))
                proof['crossover'] = crossover(out,proof,reference)
                proof['alternate_controls'] = sum(r['alternate']['controls'] for r in proof['runs'])
                proof['replay_source_sha256'] = sha(PACKET/Path(__file__).name)
                if args.output:
                    if args.output.exists():
                        raise FileExistsError(args.output)
                    write_json(args.output,proof)
                else:
                    print(json.dumps(proof))
            assert proof['alternate_controls']==sum(r['policy_controls'] for r in proof['runs'])
            if 'standalone' in reference:
                check_replayed_paths(out/'standalone',proof['standalone'],direct_plan(),{})
                print(f"Verified {proof['standalone']['paths']} standalone paths")
            print(f"Verified {proof['paths']} native and {proof['paths']} crossed command sequences")
