"""Synthetic/adversarial contract tests, with isolated upstream AST call sites.

No RoboMME, Torch, rendering, checkpoint, or native policy is imported.
"""
import ast
import copy
import itertools
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace as NS
import unittest

import fixture_api as api
import source_repair as repair

SOURCE_ROOT = None


def fixture(perm=None, target='red'):
    return {'schema_version': 1, 'group_id': 'n3-dev-scene-21000-v1', 'split': 'qualification_dev',
            'scene_seed': 21000, 'target_color': target, 'color_permutation': list(perm or [0, 1, 2])}


def execute_nodes(nodes, namespace):
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    module = ast.fix_missing_locations(ast.Module(body=[future] + copy.deepcopy(nodes), type_ignores=[]))
    exec(compile(module, '<isolated-upstream-AST>', 'exec'), namespace)


def binding(source, config):
    env_class = next(n for n in ast.parse(source).body if isinstance(n, ast.ClassDef) and n.name == 'VideoUnmask')
    load_scene = next(n for n in env_class.body if isinstance(n, ast.FunctionDef) and n.name == '_load_scene')
    bins = [NS(name='bin_' + str(i)) for i in range(3)]
    resolved = api.resolve_fixture(config, 21000, 'easy')
    obj = NS(proxy_fixture=resolved, spawned_bins=bins, bin_0=bins[0], bin_1=bins[1])
    ns = {'self': obj, 'color_names': [['red', 'green', 'blue'][i] for i in config['color_permutation']],
          'static_check': lambda *a, **k: True, 'solve_hold_obj': lambda *a, **k: None,
          'is_bin_pickup': lambda self, obj: obj,
          'is_any_bin_pickup': lambda self, objects: objects,
          'solve_pickup_bin': lambda env, planner, obj: obj}
    for node in load_scene.body:
        if not isinstance(node, ast.Assign):
            continue
        target = node.targets[0]
        if isinstance(target, ast.Attribute) and target.attr in {'color_names', 'proxy_target_index', 'proxy_target_bin', 'proxy_target_color'}:
            execute_nodes([node], ns)
        if isinstance(target, ast.Name) and target.id == 'tasks':
            execute_nodes([node], ns)
            break
    return obj, ns['tasks'][1], bins[resolved['target_bin_index']]


def goal_text(source, obj):
    branch = next(n for n in ast.walk(ast.parse(source)) if isinstance(n, ast.If)
                  and ast.unparse(n.test) == "env == 'VideoUnmask'")
    obj.configs = {'easy': {'pick': 1}}
    ns = {'self': NS(env=NS(unwrapped=obj), difficulty='easy'), 'language_goals': []}
    execute_nodes(branch.body, ns)
    return ns['language_goals'][0]


class SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original, cls.modified = repair.repair(SOURCE_ROOT)

    def test_three_colors_six_permutations_bind_same_target(self):
        for color, perm in itertools.product(['red', 'green', 'blue'], itertools.permutations(range(3))):
            with self.subTest(color=color, permutation=perm):
                obj, task, target = binding(self.modified[repair.ENV], fixture(perm, color))
                self.assertIs(task['func'](), target)
                self.assertIs(task['solve'](None, None), target)
                self.assertIs(task['segment'], target)
                self.assertNotIn(target, task['failure_func']())
                self.assertEqual(len(task['failure_func']()), 2)
                self.assertIn(color, task['name'])
                self.assertIn(color, task['subgoal_segment'])
                self.assertEqual(goal_text(self.modified[repair.GOAL], obj),
                                 f'watch the video carefully, then pick up the container hiding the {color} cube')

    def test_original_binding_is_not_counterfactual_fixture(self):
        obj, task, intended = binding(self.original[repair.ENV], fixture([1, 2, 0]))
        self.assertIsNot(task['func'](), intended)
        self.assertNotIn('red', goal_text(self.original[repair.GOAL], obj))

    def test_patch_nonfixture_keeps_first_bin(self):
        source = self.modified[repair.ENV]
        node = next(n for n in ast.walk(ast.parse(source)) if isinstance(n, ast.Assign)
                    and isinstance(n.targets[0], ast.Attribute) and n.targets[0].attr == 'proxy_target_index')
        obj = NS(proxy_fixture=None)
        execute_nodes([node], {'self': obj})
        self.assertEqual(obj.proxy_target_index, 0)

    def test_metadata_roundtrip_and_builder_forwarding(self):
        tree = ast.parse(self.modified[repair.BUILDER])
        funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in {'load_episode_metadata', 'get_episode_metadata'}]
        ns = {'json': json, 'Path': Path, 'logger': NS(debug=lambda *a: None)}
        execute_nodes(funcs, ns)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'metadata.json'
            path.write_text(json.dumps({'env_id': 'VideoUnmask', 'records': [
                {'episode': 0, 'seed': 21000, 'difficulty': 'easy', 'proxy_fixture': fixture([1, 2, 0])}]}))
            metadata = ns['load_episode_metadata'](path)
        self.assertEqual(metadata[('VideoUnmask', 0)]['proxy_fixture'], fixture([1, 2, 0]))
        method = copy.deepcopy(next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == 'make_env_for_episode'))
        body = []
        for node in method.body:
            if isinstance(node, ast.ImportFrom):
                continue
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'env':
                break
            body.append(node)
        method.body = body + [ast.Return(value=ast.Name(id='env_kwargs', ctx=ast.Load()))]
        execute_nodes([method], ns)
        builder = NS(env_id='VideoUnmask', action_space='joint_angle', render_mode='rgb_array',
                     max_steps_without_demonstration=100, metadata_index=metadata,
                     resolve_episode=lambda idx: (21000, 'easy'))
        kwargs = ns['make_env_for_episode'](builder, 0)
        self.assertEqual(kwargs['proxy_fixture'], fixture([1, 2, 0]))
        self.assertEqual(kwargs['seed'], kwargs['proxy_fixture']['scene_seed'])
        builder.action_space = 'multi_choice'
        with self.assertRaises(ValueError):
            ns['make_env_for_episode'](builder, 0)

    def test_wrong_source_revision_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path, text in self.original.items():
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text + '\n')
            with self.assertRaises(ValueError):
                repair.repair(root)


class ContractTests(unittest.TestCase):
    def test_fixture_rejects_malformed_or_out_of_scope(self):
        for changes in [{'color_permutation': [0, 0, 2]}, {'color_permutation': [False, 1, 2]},
                        {'scene_seed': 1}, {'target_color': 'purple'}, {'extra': 'answer'}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                api.resolve_fixture({**fixture(), **changes}, 21000, 'easy')
        with self.assertRaises(ValueError):
            api.resolve_fixture(fixture(), 21000, 'hard')

    def test_identity_stable_after_file_reordering(self):
        rows = [{'raw_file_sha256': str(i) * 64, 'raw_episode_key': 'episode_0',
                 'group_id': 'g', 'split': 'train', 'variant_id': i} for i in [1, 2, 3]]
        self.assertEqual(api.build_identity_index(rows), api.build_identity_index(list(reversed(rows))))

    def test_identity_rejects_cross_split_group_and_duplicates(self):
        row = {'raw_file_sha256': '1' * 64, 'raw_episode_key': 'episode_0', 'group_id': 'g', 'split': 'train'}
        with self.assertRaises(ValueError):
            api.build_identity_index([row, row])
        with self.assertRaises(ValueError):
            api.build_identity_index([row, {**row, 'raw_episode_key': 'episode_1', 'split': 'test'}])

    def rows(self):
        return [{'episode_id': 'e', 'physics_step': i, 'observation_phase': 'post_action',
                 'post_observation': 'after_' + str(i), 'executed_action': 'action_' + str(i)} for i in range(4)]

    def test_time_alignment_uses_next_action_and_drops_final(self):
        aligned = api.align_post_step_rows(self.rows())
        self.assertEqual(len(aligned), 3)
        self.assertEqual([(r['observation'], r['target_action']) for r in aligned],
                         [('after_0', 'action_1'), ('after_1', 'action_2'), ('after_2', 'action_3')])

    def test_time_alignment_rejects_gap_cross_episode_and_unknown_phase(self):
        for key, value in [('physics_step', 9), ('episode_id', 'other'), ('observation_phase', 'unknown')]:
            rows = self.rows()
            rows[1][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                api.align_post_step_rows(rows)

    def test_history_keeps_slots_and_matches_mask_counts(self):
        views = api.make_history_views([0, 10, 20, 30], 30, [0], [10])
        self.assertEqual(views['raw_time_slots'], [0, 10, 20, 30] + [None] * 28)
        self.assertEqual({k: sum(v) for k, v in views['masks'].items()},
                         {'cue_access': 64, 'cue_withheld': 48, 'irrelevant_removed': 48})
        self.assertTrue(all(len(v) == 512 for v in views['masks'].values()))

    def test_history_rejects_future_absent_cue_and_changed_current(self):
        for indices, cutoff, cue, ctrl in [([0, 10, 31], 30, [0], [10]),
                                          ([0, 10, 30], 30, [5], [10]),
                                          ([0, 10, 30], 30, [0], [30]),
                                          ([0, 10], 30, [0, 10], [0, 10])]:
            with self.subTest(indices=indices, cue=cue, ctrl=ctrl), self.assertRaises(ValueError):
                api.make_history_views(indices, cutoff, cue, ctrl)

    def input(self):
        keys = {'front_rgb', 'wrist_rgb', 'proprioception', 'goal_prompt', 'history_rgb_features', 'history_position', 'history_valid_mask'}
        resolved = {key: 'a' * 64 for key in ['checkpoint_sha256', 'normalizer_sha256', 'offline_encoder_sha256', 'online_encoder_sha256']}
        return keys, {**resolved, 'variant': 'perceptual-framesamp-modul', 'predictor': 'none', 'valid_history_tokens': 16}

    def test_input_description_accepts_only_frozen_contract(self):
        self.assertTrue(api.check_policy_input(*self.input()))

    def test_input_rejects_labels_overrides_allmask_and_encoder_mismatch(self):
        keys, resolved = self.input()
        for extra in ['target_bin_index', 'grounded_subgoal', 'success']:
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                api.check_policy_input(keys | {extra}, resolved)
        for changes in [{'variant': 'symbolic'}, {'predictor': 'oracle'}, {'valid_history_tokens': 0},
                        {'online_encoder_sha256': 'b' * 64}, {'checkpoint_sha256': None}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                api.check_policy_input(keys, {**resolved, **changes})

    def test_approach_requires_two_distinct_ticks_and_latches(self):
        observer = api.ApproachObserver()
        centers = [[0, 0, 0], [0.2, 0, 0], [0.4, 0, 0]]
        self.assertIsNone(observer.observe(0, [0.2, 0, 0.1], centers))
        with self.assertRaises(ValueError):
            observer.observe(0, [0.2, 0, 0.1], centers)
        event = observer.observe(1, [0.2, 0, 0.1], centers)
        self.assertEqual(event, {'status': 'committed_region', 'tick': 1, 'bin_index': 1})
        self.assertEqual(observer.observe(2, [0.4, 0, 0.1], centers, True), event)

    def test_approach_preserves_ambiguous_lift_and_no_commitment_outcomes(self):
        centers = [[0, 0, 0], [0.02, 0, 0], [0.4, 0, 0]]
        observer = api.ApproachObserver()
        self.assertEqual(observer.observe(0, [0.01, 0, 0.1], centers)['status'], 'ambiguous')
        observer = api.ApproachObserver()
        self.assertEqual(observer.observe(0, [0.4, 0, 0.1], centers, True)['status'], 'unobserved_before_lift')
        observer = api.ApproachObserver()
        observer.observe(0, [1, 1, 1], centers)
        self.assertEqual(observer.finish()['status'], 'no_commitment')

    def test_approach_streak_resets_on_region_exit(self):
        observer = api.ApproachObserver()
        centers = [[0, 0, 0], [0.2, 0, 0], [0.4, 0, 0]]
        for tick, tcp in enumerate([[0, 0, 0.1], [1, 1, 1], [0, 0, 0.1]]):
            self.assertIsNone(observer.observe(tick, tcp, centers))
        self.assertEqual(observer.finish()['status'], 'no_commitment')
