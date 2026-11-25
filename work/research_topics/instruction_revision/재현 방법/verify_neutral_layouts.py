"""Score neutral mentions against the sealed two-layout branches and the earlier three arms."""
import argparse
import json
import math
from pathlib import Path
import zipfile

from run_neutral_layouts import inputs, protocol
from verify_atomic import PACKET, read, sha
from verify_layouts import check_saved_replays, object_motion, unpack
from verify_mention import token_comparison, trajectory
from verify_r1 import prefix_signature, verify


def transport_motion(tape, limit_mm, robot_contact, first_bowl_goal):
    motion = object_motion(tape)
    first = tape['initial_readout']
    rows = [first, *tape['rows']]
    bowl_peak = max(math.dist(first['bowl_xyz'], r['bowl_xyz']) for r in rows)*1000
    bottle_net = math.dist(first['bottle_pose']['xyz'], rows[-1]['bottle_pose']['xyz'])*1000
    # Use the full-precision distances for the registered transport signature.
    transport = bool(robot_contact is not None and bottle_net > limit_mm
        and motion['bottle_cabinet_contact_at_deadline'] and bowl_peak <= limit_mm and first_bowl_goal is None)
    motion = dict(motion, bottle_peak_displacement_mm=round(1000*max(
        math.dist(first['bottle_pose']['xyz'], r['bottle_pose']['xyz']) for r in rows), 6))
    return motion, transport


def measured_path(tape, score, limit_mm):
    row = trajectory(tape, score)
    motion, transported = transport_motion(
        tape, limit_mm, row['first_robot_contact'], row['first_native_goal'])
    row['bottle_transport_signature'] = transported
    row['motion'] = motion
    return row


def assessment(out):
    design, reference, mention, base, _ = inputs()
    assert read(out/'study.json') == design
    history = read(reference/'verification.json')
    run = read(out/'run.json')
    assert run['status'] == 'COMPLETED' and run['jax_memory_fraction'] == '0.50'
    sources = out/'executed_sources'
    assert set(run['input_sha256']) == {f.name for f in sources.iterdir() if f.is_file()}
    assert all(sha((sources/name).read_bytes()) == value for name, value in run['input_sha256'].items())
    layouts = {}
    with zipfile.ZipFile(reference/'study.zip') as prior:
        assert (out/'gates.json').read_bytes() == prior.read('gates.json')
        gate = read(out/'gates.json')
        assert gate['frozen_at'] < run['frozen_at'] < run['finished_at']
        old_runtime = json.loads(prior.read('runtime_manifest.json'))
        runtime = read(out/'runtime_manifest.json')
        assert runtime['image_id'] == old_runtime['image_id'] and runtime['artifacts']['files'] == old_runtime['artifacts']['files']
        for seed in design['seeds']:
            key = str(seed)
            folder = out/f'seed-{seed}'
            spec = protocol(design, mention, base, seed)
            assert gate['layouts'][key]['layout_eligible'] and gate['prefixes'][key]['eligible']
            assert gate['prefixes'][key]['prefix_sha256'] == design['reference']['prefix_sha256'][key]
            for name in ('calibration.json', 'prefix.json'):
                assert (folder/name).read_bytes() == prior.read(f'seed-{seed}/{name}')
            trial = read(folder/'run.json')
            assert trial['frozen_at'] == run['frozen_at'] and trial['input_sha256'] == run['input_sha256']
            assert trial['finished_at'] <= run['finished_at'] and (folder/'runtime_manifest.json').read_bytes() == (out/'runtime_manifest.json').read_bytes()
            check = verify(folder, None, expected_spec=spec)
            assert all(check['pre_eligible']) and all(check['exact_prefix_across_all'].values())
            tokens = token_comparison(folder, PACKET/mention['reference']['archive'], spec)
            prefix = prefix_signature(read(folder/'prefix.json'), spec['switch'], spec['replan_controls'])
            paths = {}
            for name, score in check['per_path'].items():
                tape = read(folder/f'{name}.json')
                assert prefix_signature(tape, spec['switch'], spec['replan_controls']) == prefix
                paths[name] = measured_path(tape, score, check['translation_tolerance_mm'])
            counts = {arm:sum(paths[f'{arm}_{rep}']['bottle_transport_signature']
                              for rep in range(1, spec['repetitions']+1)) for arm in spec['arms']}
            layout = {k:check[k] for k in ('conditions', 'exact_restarts', 'translation_tolerance_mm',
                      'rotation_tolerance_degrees', 'policy_controls', 'model_queries', 'unique_rgb',
                      'checked_pose_samples', 'checked_native_goal_flags', 'verified_untruncated_actual_queries',
                      'same_endpoints_first_goal_first_violation_and_first_released_window')}
            old = history['layouts'][key]
            assert set(old['conditions']) == {'raw', 'O', 'A'} and old['branch'] == gate['prefixes'][key]
            layout.update(paths=paths, tokens=tokens, prefix_sha256=gate['prefixes'][key]['prefix_sha256'],
                          run_order=spec['run_order'], historical_conditions=old['conditions'], transport_count=counts)
            layouts[key] = layout
    repeated = all(r['transport_count']['B'] == 2 and r['conditions']['T']['joint'] == 2 for r in layouts.values())
    return {'decision':('B_TRANSPORT_AND_T_JOINT_REPEATED_ON_BOTH' if repeated else 'REPORT_EACH_LAYOUT_AND_PATH'),
            'eligible_layouts':list(layouts), 'historical_reference':design['reference'], 'layouts':layouts,
            'control_hz':20, 'rollout_controls':sum(r['policy_controls'] for r in layouts.values()),
            'rollout_queries':sum(r['model_queries'] for r in layouts.values())}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    folder = parser.parse_args().run
    with unpack(folder) as out:
        result = assessment(out)
        check_saved_replays(folder, result)
    print(json.dumps(result, indent=2, allow_nan=False))
