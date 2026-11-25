"""Verify the two matched native prompts against each other and the archived R1 continuations."""
import argparse
from contextlib import nullcontext
import json
from pathlib import Path
import zipfile

import numpy as np

from verify_atomic import read, sensor_flags, sha
from verify_r1 import PACKET, prefix_signature, verify


def check_run(path, protocol):
    frames = path/'frames.zip'
    with (zipfile.ZipFile(frames) if frames.exists() else nullcontext()) as archive:
        return verify(path,archive,protocol)


def token_comparison(out, reference, spec):
    current = read(out/'tokens_before.json')
    old = read(reference/'tokens_before.json')
    assert current['model'] == old['model'] == spec['policy']
    assert not current['discrete_state_input'] and not old['discrete_state_input']
    records = {k:v[0] for k,v in current['records'].items()}
    ids = {}
    for k,v in records.items():
        ids[k] = v['ids']
        assert v['tokens'] == len(ids[k]) and sha(np.asarray(ids[k],dtype='<i4').tobytes()) == v['ids_sha256']
    assert records['source']['ids_sha256'] == old['records']['source'][0]['ids_sha256']
    counts = {k:v[0]['tokens'] for k,v in old['records'].items() if k!='source'}
    counts.update({k:records[k]['tokens'] for k in spec['arms']})
    assert counts['B'] == counts['T'] == counts['O'] == spec['words']['expected_tokens']
    for arm in ('A','O'):
        if arm in records:
            assert records[arm]['ids_sha256'] == old['records'][arm][0]['ids_sha256']
    unequal = [i for i,(b,t) in enumerate(zip(ids['B'],ids['T'])) if b!=t]
    assert unequal == spec['words']['differing_token_indices_zero_based']
    return {'effective_tokens':counts,'source_tokens':len(ids['source']),
            'changed_positions_zero_based':unequal,'matched_referent_tokens':{
                arm:[ids[arm][i] for i in unequal] for arm in ('B','T')}}


def trajectory(data, score):
    bottle,bowl = score['bottle'],score['bowl']
    release = score['at_first_five_released_posthoc']['tick']
    breach = bottle['first_bad_state_tick']
    when = 'no_violation'
    if breach is not None:
        if release is None:
            when = 'no_five_tick_released_placement'
        elif breach <= release:
            when = 'by_first_five_tick_released_placement'
        else:
            when = 'after_first_five_tick_released_placement'
    contacts = bottle['bottle_robot_contact_ticks']
    rows = [data['initial_readout'],*data['rows']]
    # Query state begins with the native end effector world position. Distance is to the
    # bottle body origin, not to its surface. Include the separately captured terminal view.
    samples = []
    if release is not None:
        queries = [(q['completed_controls'],q) for q in data['queries']]
        queries.append((len(data['rows']),data['final_observation']))
        for tick,q in queries:
            if tick >= release:
                delta = np.asarray(q['proprioception'][:3])-rows[tick]['bottle_pose']['xyz']
                samples.append((float(np.linalg.norm(delta))*1000,tick))
    closest = min(samples) if samples else (None,None)
    peak = bottle['after_revision']
    return {'goal_at_300':bowl['requested_at_deadline'],'bottle_compliant_all':bottle['compliant_all'],
            'joint_at_300':bottle['goal_and_compliance'],'first_native_goal':bowl['first_native_tick'],
            'first_five_released_end':release,'goal_and_compliance_at_first_five_released':
                score['at_first_five_released_posthoc']['compliant_through_tick'],
            'first_violation_tick':breach,'violation_relative_to_release':when,
            'steps_release_to_first_violation':None if breach is None or release is None else breach-release,
            'first_robot_contact':contacts[0] if contacts else None,
            'first_bowl_contact':next(iter(bottle['bottle_bowl_contact_ticks']),None),
            'first_rotation_violation':next(iter(bottle['rotation_violation_state_ticks']),None),
            'first_position_violation':next(iter(bottle['position_violation_state_ticks']),None),
            'peak_translation_mm':peak['peak_mm'],'peak_rotation_degrees':peak['peak_degrees'],
            'min_sampled_eef_to_bottle_origin_mm_after_release':None if closest[0] is None else round(closest[0],6),
            'min_distance_tick':closest[1],'num_distance_samples_after_release':len(samples),
            'bowl_released_last_five':bowl['released_last_five']}


def verdict(paths, paired):
    if not paired:
        return 'UNMATCHED_OR_INELIGIBLE_PREFIX'
    phases = {}
    for arm in ('B','T'):
        trials = [row for name,row in paths.items() if name.startswith(arm+'_')]
        if not all(p['goal_at_300'] and p['first_five_released_end'] is not None for p in trials):
            return 'INCOMPLETE_PLACEMENT_CONTROL'
        outcomes = {p['violation_relative_to_release'] for p in trials}
        if len(outcomes) != 1:
            return 'DISCORDANT_RESTART_OUTCOMES'
        phases[arm], = outcomes
    if any(v not in ('no_violation','after_first_five_tick_released_placement') for v in phases.values()):
        return 'VIOLATION_BEFORE_OR_AT_RELEASE'
    post = tuple(arm for arm,phase in phases.items() if phase != 'no_violation')
    return {():'NEITHER_NEUTRAL_CLAUSE_REPRODUCES_POST_RELEASE_VIOLATION',
            ('B',):'POST_RELEASE_VIOLATION_ONLY_WITH_NEUTRAL_BOTTLE_MENTION',
            ('T',):'POST_RELEASE_VIOLATION_ONLY_WITH_NEUTRAL_TABLE_MENTION',
            ('B','T'):'BOTH_NEUTRAL_CLAUSES_SHOW_POST_RELEASE_VIOLATION'}[post]


def same_prompt_restarts(out,reference,spec,arms):
    results = {}
    for arm in arms:
        if arm not in spec['arms']:
            continue
        for repeat in range(1,spec['repetitions']+1):
            name = f'{arm}_{repeat}'
            old,new = (read(path/f'{name}.json') for path in (reference,out))
            a,b = old['queries'][1],new['queries'][1]
            assert a['prompt'] == b['prompt'] and a['completed_controls'] == b['completed_controls'] == spec['switch']
            delta = abs(np.asarray(a['reply'])-b['reply'])
            different = next((x['tick'] for x,y in zip(old['rows'],new['rows']) if x['dispatched']!=y['dispatched']),None)
            results[name] = {'branch_both_images_and_proprio_exact':a['rgb_sha256']==b['rgb_sha256'] and a['proprioception']==b['proprioception'],
                             'max_delta_first_post_branch_command':round(float(delta[0].max()),12),
                             'max_delta_first_five_post_branch_commands':round(float(delta[:spec['replan_controls']].max()),12),
                             'first_different_dispatched_tick':different}
    return results


def compare(out):
    key = read(out/'protocol.json')['id']
    protocol = {'REVISION-R1-MENTION':'R1_MENTION.json',
                'REVISION-R1-MENTION-MATCHED':'R1_MENTION_MATCHED.json'}[key]
    spec = read(PACKET/protocol)
    reference = PACKET/spec['reference']['archive']
    for name,digest in spec['reference']['files'].items():
        assert sha((reference/name).read_bytes()) == digest
    prior = check_run(reference,'R1_CONTROL.json')
    assert prior == read(reference/'verification.json')
    new = check_run(out,protocol)
    assert (out/'calibration.json').read_bytes() == (reference/'calibration.json').read_bytes()
    meta,old_meta = (read(path/'runtime_manifest.json') for path in (out,reference))
    fixed = ('resteer_revision','openpi_revision','jax_devices')
    assert all(meta[k] == old_meta[k] for k in fixed)
    assert meta['artifacts']['files'] == old_meta['artifacts']['files']
    tokens = token_comparison(out,reference,spec)
    anchor = prefix_signature(read(reference/'O_1.json'),spec['switch'],spec['replan_controls'])
    matched = dict.fromkeys(anchor,True)
    reference_paths,new_paths = {},{}
    live_prefix = {}
    for path,report in ((reference,prior),(out,new)):
        for name,score in report['per_path'].items():
            data = read(path/f'{name}.json')
            for k,v in prefix_signature(data,spec['switch'],spec['replan_controls']).items():
                matched[k] &= anchor[k] == v
            (new_paths if path==out else reference_paths)[name] = trajectory(data,score)
            if path==out:
                raw = np.asarray(data['queries'][0]['reply'])
                origin = np.asarray(anchor['source_reply_and_obs']['reply'])
                d = abs(raw-origin)
                live_prefix[name] = {'initial_images_exact':data['queries'][0]['rgb_sha256']==anchor['source_reply_and_obs']['rgb_sha256'],
                                     'initial_proprio_exact':data['queries'][0]['proprioception']==anchor['source_reply_and_obs']['proprioception'],
                                     'max_live_first_two_action_difference':round(float(d[:spec['switch']].max()),12),
                                     'max_live_full_reply_difference':round(float(d.max()),12)}
    eligible = all(prior['pre_eligible']+new['pre_eligible'])
    locally_paired = all(new['exact_prefix_across_all'].values()) and all(new['pre_eligible'])
    return {'decision':verdict(new_paths,eligible and all(matched.values())),
            'within_batch_decision':verdict(new_paths,locally_paired),'independent_layouts':1,'scene_seed':spec['scene_seed'],
            'new_paths':len(new_paths),'reference_paths':len(reference_paths),'matched_executed_prefix_with_historical_paths':matched,
            'new_prefix_exact_within_batch':new['exact_prefix_across_all'],'all_prefixes_eligible':eligible,
            'source_actions_from_archive':('source_replay' in spec),'live_source_inference_against_archive':live_prefix,
            'same_prompt_at_matched_branch_vs_historical':same_prompt_restarts(out,reference,spec,spec['reference']['conditions']),
            'same_checkpoint_bytes':True,'same_image_id_as_reference':meta['image_id']==old_meta['image_id'],
            'tokens':tokens,'untruncated_new_queries':new['verified_untruncated_actual_queries'],
            'new_policy_controls':new['policy_controls'],'new_unique_rgb':new['unique_rgb'],
            'new_bottle_pose_samples':new['checked_pose_samples'],'new_goal_flags_recomputed':new['checked_native_goal_flags'],
            'stored_reference_controls':prior['policy_controls'],'stored_reference_queries':prior['model_queries'],
            'thresholds':{'mm':new['translation_tolerance_mm'],'degrees':new['rotation_tolerance_degrees']},
            'whole_trajectory_exact_restarts':new['exact_restarts'],
            'repeat_endpoint_and_key_event_ticks':new['same_endpoints_first_goal_first_violation_and_first_released_window'],
            'conditions':new['conditions'],'paths':new_paths,
            'historical_conditions':prior['conditions'],'historical_paths':reference_paths}


def compare_batches(first,second):
    spec = read(PACKET/'R1_MENTION_MATCHED.json')
    reports = [compare(path) for path in (first,second)]
    runs = [read(path/'run.json') for path in (first,second)]
    assert runs[0]['started_at'] < runs[0]['finished_at'] < runs[1]['started_at'] < runs[1]['finished_at']
    assert runs[0]['input_sha256'] == runs[1]['input_sha256']
    for name in ('protocol.json','runtime_manifest.json','tokens_before.json','calibration.json'):
        assert (first/name).read_bytes() == (second/name).read_bytes(), name
    assert all(rep['all_prefixes_eligible'] and rep['source_actions_from_archive']
               and all(rep['matched_executed_prefix_with_historical_paths'].values()) for rep in reports)
    assert all(rep['same_image_id_as_reference'] and rep['same_checkpoint_bytes'] for rep in reports)
    restarts = same_prompt_restarts(second,first,spec,spec['arms'])
    assert all(r['branch_both_images_and_proprio_exact'] for r in restarts.values())
    summaries = []
    for report in reports:
        summary = {}
        for arm in spec['arms']:
            trials = [report['paths'][f'{arm}_{i}'] for i in range(1,spec['repetitions']+1)]
            summary[arm] = {
                'placements_at_300':sum(t['goal_at_300'] for t in trials),
                'joint_successes_at_300':sum(t['joint_at_300'] for t in trials),
                'first_five_released_end':[t['first_five_released_end'] for t in trials],
                'first_bottle_violation':[t['first_violation_tick'] for t in trials]}
        summaries.append(summary)
    donors = ('B_1','T_1')
    first_release = max(reports[0]['paths'][name]['first_five_released_end'] for name in donors)
    tick = next(i for i in range(spec['switch'],spec['horizon'],spec['replan_controls']) if i >= first_release)
    eligible_donors = {}
    for name in donors:
        data = read(first/f'{name}.json')
        query, = (q for q in data['queries'] if q['completed_controls']==tick)
        geom = data['geometry']
        groups = {k:set(v.values()) for k,v in geom['contact_geoms'].items()}
        recent = [sensor_flags(r,groups,np.asarray(geom['cabinet_site_half_size'])) for r in data['rows'][tick-5:tick]]
        first_breach = reports[0]['paths'][name]['first_violation_tick']
        eligible_donors[name] = {'five_released_goal_steps':all(g['cabinet'] and not c for g,c in recent),
                                 'bottle_in_tolerance_through_tick':first_breach is None or first_breach>tick,
                                 'query_image_hashes':query['rgb_sha256']}
    return {
        'matched_batches':2,'independent_layouts':1,'scene_seed':spec['scene_seed'],
        'matched_controls':sum(report['new_policy_controls'] for report in reports),
        'matched_queries':sum(report['untruncated_new_queries'] for report in reports),
        'batch_start_utc':[run['started_at'] for run in runs],
        'identical_executed_prefix_at_revision':True,'identical_recorded_runtime_and_protocol':True,
        'same_checkpoint_files':17,'tokens':reports[0]['tokens'],
        'neutral_clause_decision_by_batch':[r['decision'] for r in reports],
        'neutral_clause_outcome_repeats_between_containers':reports[0]['decision']==reports[1]['decision'],
        'first_matched_batch':summaries[0],'independent_matched_repeat':summaries[1],
        'same_prompt_first_response_at_matched_branch_between_containers':restarts,
        'development_donors_for_next_test':{'earliest_common_post_release_query_tick':tick,'donors':eligible_donors}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    parser.add_argument('--repeat',type=Path,help='Compare two independently started, matched 4-arm batches.')
    args = parser.parse_args()
    result = compare_batches(args.run,args.repeat) if args.repeat else compare(args.run)
    print(json.dumps(result,indent=2,allow_nan=False))
