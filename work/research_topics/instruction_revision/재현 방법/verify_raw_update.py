"""Score the actual R1 update and its two contemporary controls against the frozen branch."""
import argparse
import json
from pathlib import Path

import numpy as np

from verify_atomic import PACKET, read, sha
from verify_mention import check_run, trajectory
from verify_r1 import prefix_signature


def event_timing(ticks, release):
    ticks = sorted(set(ticks))
    first = next(iter(ticks), None)
    if release is None:
        return {'first': first, 'release_confirmed': False, 'by_release': None,
                'active_at_release': None, 'first_strictly_after': None, 'new_onset_after': None}
    active = set(ticks)
    return {'first': first, 'release_confirmed': True,
            'by_release': any(t <= release for t in ticks), 'active_at_release': release in active,
            'first_strictly_after': next((t for t in ticks if t > release), None),
            'new_onset_after': next((t for t in ticks if t > release and t-1 not in active), None)}


def classify(scores, eligible):
    delta = {arm: [int(scores[f'O_{i}']['joint_at_300']) - int(scores[f'{arm}_{i}']['joint_at_300'])
                   for i in (1, 2)] for arm in ('raw', 'A')}
    if not eligible:
        decision = 'INELIGIBLE_BRANCH'
    elif all(s['joint_at_300'] for s in scores.values()):
        decision = 'ALL_THREE_JOINTLY_SUCCEED_NO_MEASURED_GAIN'
    elif delta['raw'] == delta['A'] == [1, 1]:
        decision = 'COMPLETE_INSTRUCTION_BEATS_BOTH_ON_THIS_LAYOUT'
    elif delta['raw'] == [1, 1] and delta['A'] == [0, 0]:
        decision = 'GOAL_ONLY_REWRITE_ALSO_RECOVERS_BOTH_RAW_FAILURES'
    elif delta['raw'] == delta['A'] == [-1, -1]:
        decision = 'COMPLETE_INSTRUCTION_WORSE_THAN_BOTH_ON_THIS_LAYOUT'
    else:
        decision = 'REPORT_EACH_PAIRED_DIFFERENCE'
    return decision, delta


def verify_update(out):
    spec = read(out/'protocol.json')
    checked = check_run(out, 'R1_RAW_UPDATE.json')
    repeat_file = out/'fixed_action_replay_repeat.json'
    if repeat_file.is_file():
        primary, repeat = read(out/'fixed_action_replay.json'), read(repeat_file)
        assert primary['paths'].keys() == repeat['paths'].keys()
        for key in ('replayed_controls', 'policy_queries', 'original_native_restart_comparison'):
            assert primary[key] == repeat[key]
        for name, path in primary['paths'].items():
            for key in ('actions', 'snapshots', 'native_rows_and_bottle_poses_exact'):
                assert path[key] == repeat['paths'][name][key], (name, key)
    cases = read(PACKET/'SEMANTIC_CASES.json')['cases']
    case, = [c for c in cases if c['case_id'] == 'R1']
    assert spec['source_prompt'] == case['initial_utterance']
    assert spec['arms'] == {'raw': case['revision_utterance'], 'O': case['oracle_policy_prompt'],
                           'A': read(PACKET/'R1_CONTROL.json')['arms']['A']}
    assert spec['run_order'] == [['raw', 'O', 'A'], ['A', 'O', 'raw']]
    paths = {}
    reference = PACKET/spec['reference']['archive']
    for name, digest in spec['reference']['files'].items():
        assert sha((reference/name).read_bytes()) == digest, name
    assert (out/'calibration.json').read_bytes() == (reference/'calibration.json').read_bytes()
    assert (out/'runtime_manifest.json').read_bytes() == (reference/'runtime_manifest.json').read_bytes()
    old = read(reference/spec['source_replay']['path'])
    branch = prefix_signature(old, spec['switch'], spec['replan_controls'])
    match = {}
    for name, score in checked['per_path'].items():
        data = read(out/f'{name}.json')
        match[name] = prefix_signature(data, spec['switch'], spec['replan_controls']) == branch
        summary = trajectory(data, score)
        bottle = score['bottle']
        exceedances = bottle['position_violation_state_ticks'] + bottle['rotation_violation_state_ticks']
        release = summary['first_five_released_end']
        summary['robot_bottle_contact'] = event_timing(bottle['bottle_robot_contact_ticks'], release)
        summary['bowl_bottle_contact'] = event_timing(bottle['bottle_bowl_contact_ticks'], release)
        summary['bottle_pose_exceedance'] = event_timing(exceedances, release)
        assert summary['bottle_pose_exceedance']['first'] == summary['first_violation_tick']
        assert summary['joint_at_300'] == (summary['goal_at_300'] and not exceedances)
        summary['native_bowl_on_intervals'] = score['bowl']['native_intervals']
        summary['released_bowl_on_intervals'] = score['bowl']['released_intervals']
        paths[name] = summary

    records = read(out/'tokens_before.json')['records']
    old_tokens = read(reference/'tokens_before.json')['records']
    tokens = {}
    for name, (record,) in records.items():
        assert record['tokens'] == len(record['ids'])
        assert sha(np.asarray(record['ids'], dtype='<i4').tobytes()) == record['ids_sha256']
        if name in old_tokens:
            assert record['ids_sha256'] == old_tokens[name][0]['ids_sha256']
        tokens[name] = record['tokens']
    eligible = all(match.values()) and all(checked['pre_eligible']) and all(checked['exact_prefix_across_all'].values())
    decision, delta = classify(paths, eligible)
    keys = ('conditions', 'calibration', 'translation_tolerance_mm', 'rotation_tolerance_degrees',
            'exact_prefix_across_all', 'exact_restarts', 'same_endpoints_first_goal_first_violation_and_first_released_window',
            'model_queries', 'policy_controls', 'checked_pose_samples', 'checked_native_goal_flags', 'unique_rgb',
            'token_limit', 'verified_untruncated_actual_queries', 'control_hz')
    return {'decision': decision, 'scene_seed': spec['scene_seed'], 'independent_layouts': 1,
            'observed_order': [row['arm'] for row in read(out/'run.json')['paths']],
            'eligible_common_protected_branch': eligible, 'archived_branch_match_by_path': match,
            'paired_joint_difference_O_minus_comparator': delta, 'effective_token_counts': tokens,
            'fixed_prefix_controls': len(paths)*spec['switch'],
            'new_post_revision_controls': len(paths)*(spec['horizon']-spec['switch']),
            **{k: checked[k] for k in keys}, 'paths': paths}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    print(json.dumps(verify_update(parser.parse_args().run), indent=2, allow_nan=False))
