"""Independently score the registered held-out layouts or physically replay their commands."""
import argparse
from contextlib import contextmanager
import json
import math
from pathlib import Path
import tempfile
import zipfile

from run_layouts import STUDY, base_inputs, layout_gate, layout_spec, positions, prefix_gate
from verify_atomic import read, sha
from verify_mention import trajectory
from verify_r1 import PACKET, prefix_signature, verify
from verify_raw_update import classify, event_timing


@contextmanager
def unpack(folder):
    bundle = folder/'study.zip'
    if not bundle.exists():
        yield folder
        return
    sums = folder/'SHA256SUMS'
    if sums.is_file():
        listed = [line.split('  ',1) for line in sums.read_text().splitlines()]
        assert sorted(name for _,name in listed)==sorted(p.name for p in folder.iterdir() if p!=sums)
        assert all(sha((folder/name).read_bytes())==digest for digest,name in listed)
    with tempfile.TemporaryDirectory() as scratch, zipfile.ZipFile(bundle) as z:
        names = z.namelist()
        assert len(set(names))==len(names)
        for name in names:
            assert name and not Path(name).is_absolute() and '..' not in Path(name).parts
        z.extractall(scratch)
        yield Path(scratch)


def object_motion(tape):
    rows = [tape['initial_readout'], *tape['rows']]
    first, last = rows[0], rows[-1]
    bottle = set(tape['bottle_geometry']['bottle'])
    cabinet = set(tape['geometry']['contact_geoms']['cabinet'].values())
    assert bottle.isdisjoint(cabinet)
    contact = [i for i,row in enumerate(rows) if any(
        (a in bottle and b in cabinet) or (b in bottle and a in cabinet) for a,b in row['bottle_contacts'])]
    return {'bowl_peak_displacement_mm':round(1000*max(math.dist(first['bowl_xyz'], r['bowl_xyz']) for r in rows),6),
            'bowl_net_displacement_mm':round(1000*math.dist(first['bowl_xyz'],last['bowl_xyz']),6),
            'bottle_net_displacement_mm':round(1000*math.dist(first['bottle_pose']['xyz'],last['bottle_pose']['xyz']),6),
            'first_bottle_cabinet_contact':next(iter(contact),None), 'bottle_cabinet_contact_at_deadline':len(rows)-1 in contact}


def assessment(out):
    design, base, ref = base_inputs()
    assert read(out/'study.json')==design
    recorded = read(out/'gates.json')
    run = read(out/'run.json')
    assert run['status']=='COMPLETED' and recorded['started_at']<recorded['frozen_at']<run['finished_at']
    for name, digest in run['input_sha256'].items():
        assert any(p.is_file() and sha(p.read_bytes())==digest for p in (out/'executed_sources'/name,PACKET/name)),name
    old = read(ref/'O_1.json')['initial_readout']
    previous = {str(design['reference_seed']):positions(old['bowl_xyz'],old['bottle_pose']['xyz'])}
    frozen = read(ref/'calibration.json')
    results = {}
    for seed in design['seeds']:
        key = str(seed)
        folder = out/f'seed-{seed}'
        cal = read(folder/'calibration.json')
        assert {k:v for k,v in cal.items() if k!='check'}=={k:v for k,v in frozen.items() if k!='check'}
        spec = layout_spec(base,seed)
        layout = layout_gate(cal,spec,previous)
        saved_layout = recorded['layouts'][key]
        assert math.isclose(layout['peak_zero_rotation_deg'],saved_layout['peak_zero_rotation_deg'],rel_tol=0,abs_tol=1e-12)
        assert dict(layout,peak_zero_rotation_deg=saved_layout['peak_zero_rotation_deg'])==saved_layout
        result = results[key] = {'layout':saved_layout}
        if not layout['layout_eligible']:
            assert key not in recorded['prefixes'] and not (folder/'prefix.json').exists()
            continue
        previous[key] = layout['xyz_m']
        branch = prefix_gate(folder,spec,cal)
        assert branch==recorded['prefixes'][key]
        result['branch'] = branch
        if not branch['eligible']:
            assert not (folder/'run.json').exists()
            continue
        spec = layout_spec(base,seed,branch['prefix_sha256'])
        assert (folder/'runtime_manifest.json').read_bytes()==(out/'runtime_manifest.json').read_bytes()
        assert read(folder/'run.json')['frozen_at']==recorded['frozen_at']
        check = verify(folder,None,expected_spec=spec)
        prefix = prefix_signature(read(folder/'prefix.json'),spec['switch'],spec['replan_controls'])
        assert all(check['pre_eligible']) and all(check['exact_prefix_across_all'].values())
        scores = {}
        for name,s in check['per_path'].items():
            tape = read(folder/f'{name}.json')
            assert prefix_signature(tape,spec['switch'],spec['replan_controls'])==prefix
            row = trajectory(tape,s)
            rel = row['first_five_released_end']
            bottle = s['bottle']
            row['robot_contact_timing'] = event_timing(bottle['bottle_robot_contact_ticks'],rel)
            row['violation_timing'] = event_timing(bottle['rotation_violation_state_ticks']+bottle['position_violation_state_ticks'],rel)
            row['posthoc_object_motion'] = object_motion(tape)
            scores[name]=row
        verdict,delta = classify(scores,True)
        result.update(decision=verdict,paired_joint_difference_O_minus=delta,paths=scores)
        for k in ('conditions','exact_restarts','same_endpoints_first_goal_first_violation_and_first_released_window',
                  'translation_tolerance_mm','rotation_tolerance_degrees','model_queries','policy_controls','checked_pose_samples',
                  'checked_native_goal_flags','unique_rgb','verified_untruncated_actual_queries','control_hz'):
            result[k]=check[k]
    eligible = [key for key,r in results.items() if 'conditions' in r]
    complete = len(eligible)==len(design['seeds'])
    winners = all(results[k]['decision']=='ALL_THREE_JOINTLY_SUCCEED_NO_MEASURED_GAIN' for k in eligible)
    decision = ('CLOSE_CURRENT_R1_METHOD_SEARCH' if complete and winners else
                'REPORT_LAYOUT_SPECIFIC_OUTCOMES' if complete else 'INCOMPLETE_LAYOUT_COVERAGE')
    return {'decision':decision,'registered_seeds':design['seeds'],'eligible_layouts':eligible,
            'reference_xyz_m':previous[str(design['reference_seed'])], 'layouts':results,
            'rollout_controls':sum(results[k]['policy_controls'] for k in eligible),
            'rollout_queries':sum(results[k]['model_queries'] for k in eligible),
            'additional_source_only_queries':len(recorded['prefixes']),
            'calibration_zero_controls':sum(r['layout']['zero_command_states']-1 for r in results.values())}


def physical(out):
    from replay_r1 import main as replay
    gate = read(out/'gates.json')
    reports = {seed:replay(out/f'seed-{seed}',None) for seed,branch in gate['prefixes'].items() if branch['eligible']}
    return {'replayed_controls':sum(r['replayed_controls'] for r in reports.values()),'policy_queries':0,'seeds':reports}


def check_saved_replays(folder, score):
    path = folder/'physical_replay.json'
    if not path.is_file():
        return
    replays = read(path)
    assert set(replays)=={'first','second'}
    for report in replays.values():
        assert report['replayed_controls']==score['rollout_controls'] and report['policy_queries']==0
        assert set(report['seeds'])==set(score['eligible_layouts'])
        for key,trial in report['seeds'].items():
            layout = score['layouts'][key]
            assert trial['replayed_controls']==layout['policy_controls'] and trial['policy_queries']==0
            assert set(trial['paths'])==set(layout['paths'])
            assert trial['original_native_restart_comparison']==replays['first']['seeds'][key]['original_native_restart_comparison']
            for record in trial['paths'].values():
                assert record['actions']==300 and record['native_rows_and_bottle_poses_exact']
                assert set(record['snapshots'])=={'0','2','terminal'} and all(all(v.values()) for v in record['snapshots'].values())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    parser.add_argument('--replay',action='store_true')
    args = parser.parse_args()
    with unpack(args.run) as out:
        if args.replay:
            result = physical(out)
        else:
            result = assessment(out)
            check_saved_replays(args.run,result)
        print(json.dumps(result,indent=2,allow_nan=False))
