"""Docker-only analysis of the first-pass evidence; no policy performance claims."""
import collections
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path('/tmp/c2')
OUT = ROOT / 'out'


def read(name):
    return json.loads((OUT / name).read_bytes())


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def main():
    manifest = read('episode_manifest.json')
    rows = manifest['episodes']
    payloads = read('payload_audit.json')['episodes']
    metadata = read('task_metadata.json')
    instructions = read('instruction_audit.json')['entries']
    # This small source file was manually inspected: imports numpy and defines
    # check_training_route. It does not import the simulator or deserialize data.
    route_path = ROOT / 'sources/routes.py'
    spec = importlib.util.spec_from_file_location('audited_routes', route_path)
    route_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(route_module)
    report = {'kind': 'data/predicate feasibility audit, not policy evaluation',
              'task_count': len(metadata), 'inventory_episode_count': len(rows),
              'payload_episode_count': len(payloads), 'payload_errors': [],
              'metadata_by_task': {}, 'training_route_rechecks': [],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'route_function_source_sha256': hashlib.sha256(route_path.read_bytes()).hexdigest()}
    for item in metadata:
        task = item['task_id']
        erows = [e for e in rows if e['task_id'] == task]
        infos = [(e.get('scene_info') or {}).get('info', {}) for e in erows]
        report['metadata_by_task'][task] = {
            'task_partition': item['partition'], 'episodes': len(erows),
            'route_trace_count': sum(bool(i.get('route_samples')) for i in infos),
            'route_check_count': sum('route_check' in i for i in infos),
            'collection_manifest_present': 'collection.json' in item['metadata'],
            'declared_upstream_commit': item['metadata'].get('collection.json', {}).get('upstream_commit'),
            'declared_code_hash': item['metadata'].get('collection.json', {}).get('code_sha256'),
            'ordered_seeds_equal_json': item['seed_ids'] == item['metadata'].get('seeds.json') if 'seeds.json' in item['metadata'] else None,
        }
    # Use training traces only. Never label or score heldout trajectories.
    for e in rows:
        info = (e.get('scene_info') or {}).get('info', {})
        samples = info.get('route_samples')
        if e['task_partition'] == 'train' and samples:
            initial_z = samples[0]['source'][2]
            factual = route_module.check_training_route(samples, initial_z, 'via')
            swapped = [{'source': s['source'], 'correct': s['wrong'], 'wrong': s['correct']} for s in samples]
            counterfactual = route_module.check_training_route(swapped, initial_z, 'via')
            report['training_route_rechecks'].append({
                'task_id': e['task_id'], 'episode_id': e['episode_id'],
                'initial_z_basis': 'first recorded route sample; native _route_initial_z is not separately saved',
                'source_report': info.get('route_check'), 'factual_recomputed': factual,
                'source_report_equal_recomputed': factual == info.get('route_check'),
                'alternate_training_task': 'r_pick3_via5_to6_short_front',
                'alternate_waypoint_recomputed': counterfactual,
                'full_joint_reward_verified': False,
                'scope': 'Waypoint-only recheck; goal and object final orientation not independently available',
            })
    checks = report['training_route_rechecks']
    report['route_recheck_summary'] = {
        'training_traces': len(checks),
        'reported_recomputed_agreement': sum(x['source_report_equal_recomputed'] for x in checks),
        'factual_route_pass': sum(x['factual_recomputed']['passed'] for x in checks),
        'alternate_route_fail': sum(not x['alternate_waypoint_recomputed']['passed'] for x in checks),
        'independent_complete_reward_labels': 0,
    }
    train_seeds = set().union(*(set(x['seed_ids']) for x in metadata if x['partition'] == 'train'))
    test_seeds = set().union(*(set(x['seed_ids']) for x in metadata if x['partition'] == 'holdout'))
    report['seed_overlap'] = {'train_unique': len(train_seeds), 'holdout_unique': len(test_seeds),
        'shared_seed_ids': sorted(train_seeds & test_seeds),
        'holdout_episodes_with_seed_seen_in_train': sum(e['task_partition'] == 'holdout' and e['seed_from_ordered_seed_txt'] in train_seeds for e in rows),
        'interpretation': 'Declared seed reuse warns against naive task-only split; equality of complete physical states is not proved.'}
    verified_identity = 0
    image_checks = []
    first_frame_groups = collections.defaultdict(list)
    for p in payloads:
        for key in p:
            if key.endswith('_error'):
                report['payload_errors'].append({'task': p['task_id'], 'episode': p['episode_id'], 'error': p[key]})
        h = p.get('hdf5', {})
        matching = next(e for e in rows if e['task_id'] == p['task_id'] and e['episode_id'] == p['episode_id'])
        attrs = h.get('attributes', {})
        valid = (attrs.get('robofollow_seed') == str(matching['seed_from_ordered_seed_txt'])
                 and attrs.get('robofollow_episode') == str(p['episode_id'])
                 and attrs.get('robofollow_task') == p['task_id'] and attrs.get('robofollow_scene') == 'scene3')
        matching['seed_mapping_verified_against_payload'] = valid
        verified_identity += valid
        image_checks.extend(c for cs in h.get('image_decode_checks', {}).values() for c in cs)
        for name, cs in h.get('image_decode_checks', {}).items():
            for c in cs:
                if c['frame'] == 0 and 'decoded_sha256' in c:
                    first_frame_groups[(name, c['decoded_sha256'])].append([p['task_id'], p['episode_id']])
    report['payload_summary'] = {
        'total_frames': sum(p['hdf5']['time_lengths'][0] for p in payloads),
        'frame_range': [min(p['hdf5']['time_lengths'][0] for p in payloads), max(p['hdf5']['time_lengths'][0] for p in payloads)],
        'aligned_sequence_lengths': sum(len(p['hdf5']['time_lengths']) == 1 for p in payloads),
        'finite_joint_vectors': sum(p['hdf5']['datasets']['joint_action/vector']['finite'] for p in payloads),
        'identity_attributes_verified': verified_identity,
        'image_samples_decoded': sum('error' not in x for x in image_checks),
        'image_decode_errors': [x for x in image_checks if 'error' in x],
        'image_dimensions': sorted({tuple(x['size']) for x in image_checks if 'size' in x}),
        'dataset_key_signatures': [list(s) for s in sorted({tuple(sorted(p['hdf5']['datasets'])) for p in payloads})],
        'object_pose_dataset_keys': sorted({k for p in payloads for k in p['hdf5']['datasets'] if any(x in k.lower() for x in ['obj_pos', 'obj_quat', 'object_pose'])}),
        'pointcloud_shapes': [p['hdf5']['datasets'].get('pointcloud', {}).get('shape') for p in payloads],
        'duplicate_initial_image_groups': [{'camera': key[0], 'sha256': key[1], 'episodes': es}
            for key, es in first_frame_groups.items() if len(es) > 1],
    }
    report['instruction_summary'] = {
        'files_read': len(instructions),
        'unique_seen_texts': len({s for x in instructions for s in x['value'].get('seen', [])}),
        'unseen_text_entries': sum(len(x['value'].get('unseen', [])) for x in instructions),
        'variants_per_file': sorted({len(x['value'].get('seen', [])) for x in instructions}),
    }
    # Retain episode provenance and trace hash, not external trajectory payloads.
    for e in rows:
        scene_info = e.pop('scene_info', None)
        info = (scene_info or {}).get('info', {})
        samples = info.get('route_samples')
        e['scene_info_summary'] = {
            'sha256_canonical_json': sha(scene_info), 'declared_task_fields': {k: v for k, v in info.items() if k.startswith('{')},
            'route_trace_present': bool(samples), 'route_trace_samples': len(samples) if samples else 0,
            'route_trace_sha256_canonical_json': sha(samples) if samples else None,
            'upstream_route_check': info.get('route_check') if e['task_partition'] == 'train' else 'heldout outcome not analyzed',
        }
    (OUT / 'episode_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (OUT / 'first_pass_analysis.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['task_count', 'inventory_episode_count', 'payload_episode_count', 'payload_errors', 'route_recheck_summary', 'seed_overlap', 'instruction_summary']}, indent=2))
    print('Payload summary', json.dumps({k:v for k,v in report['payload_summary'].items() if k not in ['dataset_key_signatures','duplicate_initial_image_groups']}, indent=2))


if __name__ == '__main__':
    if not Path('/.dockerenv').exists():
        raise SystemExit('Run this analysis in Docker')
    main()
