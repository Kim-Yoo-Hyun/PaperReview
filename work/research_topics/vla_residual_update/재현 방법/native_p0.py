#!/usr/bin/env python3
"""Candidate native IO probe. Docker only; no training/full-task rollout or automatic retry."""
import argparse
import ast
import gc
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

SRC = Path('/opt/vrl/SimpleVLA-RL')
LIBERO = Path('/opt/vrl/LIBERO/libero/libero')
CACHE = Path('/cache')
NORMALIZER = 'libero_10_no_noops'
ZERO_ATOL = 1e-7  # NumPy float64 action conversion; NOT a BF16 forward-equivalence test.


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def tree_hashes(root):
    return {str(p.relative_to(root)): sha(p) for p in sorted(root.rglob('*')) if p.is_file() and p.suffix != '.pyc'}


class Budget:
    CAPS = {'resets': 2, 'queries': 2, 'warmup_steps': 20, 'policy_steps': 16, 'encoder_calls': 4}

    def __init__(self):
        self.used = dict.fromkeys(self.CAPS, 0)

    def charge(self, key):
        require(key in self.CAPS, 'Unknown budget counter')
        require(self.used[key] < self.CAPS[key], f'P0 {key} cap reached; no retry')
        self.used[key] += 1  # Count attempted calls, including calls which fail.


def validate_contract(ledger):
    contract = ledger['r2_review']['comparison_contract']
    b = contract['budget']['P0']
    require(b == {'scope': 'IO only; not full rollout or residual learning', 'dev_init_id': 0,
                  'resets': 2, 'policy_steps': 16, 'warmup_steps': 20, 'env_steps': 36,
                  'vla_queries': 2, 'encoder_calls_max': 4}, 'P0 contract changed; review adapter before execution')
    require(contract['action']['base_shape'] == [8, 7] and contract['action']['residual_shape'] == [8, 6], 'Action contract drift')
    require(contract['task']['warmup_control_steps_per_reset'] == 10, 'Warmup contract drift')
    require(contract['task']['control_frequency_hz'] == 20, 'Control rate drift')
    require(contract['observation']['history_chunk_boundaries'] == 2, 'History contract drift')
    return contract


def setup_runtime():
    require(Path('/.dockerenv').exists(), 'Native dependencies/payload work is allowed only inside Docker')
    for k, v in {'ROBOT_PLATFORM': 'LIBERO', 'MUJOCO_GL': 'egl', 'PYOPENGL_PLATFORM': 'egl'}.items():
        require(os.environ.get(k) == v, f'{k} must equal {v}')
    import torch
    require(torch.cuda.is_available(), 'CUDA unavailable')
    require(torch.cuda.is_bf16_supported(), 'Native BF16 capability required; no CPU/FP32 substitution')
    require(torch.version.cuda == '12.4', 'Torch CUDA version changed')
    import tensorflow as tf
    tf.config.set_visible_devices([], 'GPU')  # TF implements exact image preprocessing on container CPU.
    import yaml
    cfg = Path(os.environ['LIBERO_CONFIG_PATH'])
    cfg.mkdir(parents=True, exist_ok=True)
    paths = {'benchmark_root': str(LIBERO), 'bddl_files': str(LIBERO / 'bddl_files'),
             'init_states': str(LIBERO / 'init_files'), 'assets': str(LIBERO / 'assets'),
             'datasets': '/cache/unused-datasets'}
    Path(paths['datasets']).mkdir(exist_ok=True)
    (cfg / 'config.yaml').write_text(yaml.safe_dump(paths))
    return {'torch': torch.__version__, 'cuda': torch.version.cuda, 'gpu': torch.cuda.get_device_name(0),
            'gpu_memory_bytes': torch.cuda.get_device_properties(0).total_memory,
            'bf16': True, 'tf_gpu_disabled': True}


def helpers():
    """Load only audited standalone definitions, without importing Ray/veRL's rollout module."""
    import math
    import numpy as np
    import tensorflow as tf
    from PIL import Image
    ns = {'np': np, 'tf': tf, 'Image': Image, 'math': math, 'ACTION_PROPRIO_NORMALIZATION_TYPE': 'bounds_q99'}
    selection = {
        'verl/utils/libero_utils.py': ['resize_image', 'get_libero_image', 'quat2axisangle',
                                      'normalize_gripper_action', 'invert_gripper_action'],
        'verl/workers/rollout/rob_rollout.py': ['crop_and_resize', 'center_crop_image', 'normalize_proprio'],
    }
    for relative, names in selection.items():
        path = SRC / relative
        parsed = ast.parse(path.read_text())
        functions = [n for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name in names]
        require({n.name for n in functions} == set(names), f'Helper source API changed: {relative}')
        exec(compile(ast.Module(body=functions, type_ignores=[]), str(path), 'exec'), ns)
    return ns


def task_and_states(contract):
    import numpy as np
    import torch
    from libero.libero import benchmark
    suite = benchmark.get_benchmark_dict()[contract['task']['suite']]()
    matches = [suite.get_task(i) for i in range(suite.n_tasks) if suite.get_task(i).name == contract['task']['name']]
    require(len(matches) == 1, 'Expected exactly one contracted task')
    task = matches[0]
    init = LIBERO / 'init_files' / task.problem_folder / task.init_states_file
    bddl = LIBERO / 'bddl_files' / task.problem_folder / task.bddl_file
    require(not init.read_bytes()[:100].startswith(b'version https://git-lfs'), 'Unresolved Git LFS init-state pointer')
    states = torch.load(init, map_location='cpu', weights_only=False)  # Pinned official payload; inside Docker only.
    require(len(states) > 0, 'No dev init state')
    hashes = [hashlib.sha256(np.asarray(s).tobytes()).hexdigest() for s in states]
    return task, states, {'init_file': str(init), 'init_sha256': sha(init), 'bddl_file': str(bddl),
                          'bddl_sha256': sha(bddl), 'init_count': len(states), 'state_hashes': hashes,
                          'distinct_state_count': len(set(hashes)),
                          'later_50_state_split_qualified': len(states) >= 50 and len(set(hashes[:50])) == 50}


def verify_sources(ledger, contract):
    # Source revision is also checked during image build; do not infer from a mutable branch.
    for folder, revision in [(SRC, '7c51662df27b586f9e8a1ab35fcf849f2b8852f9'),
                             (LIBERO.parents[1], contract['task']['libero_commit'])]:
        actual = subprocess.check_output(['git', '-C', str(folder), 'rev-parse', 'HEAD'], text=True).strip()
        require(actual == revision, f'Source revision mismatch: {folder}')
    original = SRC / 'verl/utils/vla_utils/openvla_oft'
    require(tree_hashes(original) == tree_hashes(Path('/opt/vrl/packages/openvla_oft')), 'Standalone model copy differs from pinned source')
    return {str(p.relative_to(SRC)): sha(p) for p in [
        original / 'modeling_prismatic.py', original / 'configuration_prismatic.py',
        original / 'processing_prismatic.py', original / 'constants.py', original / 'train_utils.py',
        SRC / 'verl/utils/libero_utils.py', SRC / 'verl/workers/rollout/rob_rollout.py']}


def prepare(ledger, contract, report):
    from huggingface_hub import snapshot_download
    # Resolve simulator prerequisites before fetching ~42 GiB of weight tensors.
    _, _, report['task'] = task_and_states(contract)
    report['assets_sha256'] = tree_hashes(LIBERO / 'assets')
    require(bool(report['assets_sha256']), 'No simulator assets')
    for name in report['assets_sha256']:
        with (LIBERO / 'assets' / name).open('rb') as f:
            require(not f.read(100).startswith(b'version https://git-lfs'), 'Unresolved simulator asset LFS pointer')
    pair = ledger['r1_review']['checkpoint_candidate']
    report['models'] = {}
    for label in ('A', 'B'):
        spec = pair[label]
        path = Path(snapshot_download(spec['repo'], revision=spec['revision'],
                    allow_patterns=['*.json', '*.safetensors', 'tokenizer.model']))
        require(sha(path / 'model.safetensors.index.json') == spec['index_sha256'], 'Weight index hash mismatch')
        require(sha(path / 'dataset_statistics.json') == pair['normalizer']['sha256'], 'Normalizer hash mismatch')
        files = tree_hashes(path)
        index = json.loads((path / 'model.safetensors.index.json').read_text())
        require(all(n in files for n in set(index['weight_map'].values())), 'Missing weight shard')
        report['models'][label] = {'path': str(path), 'repo': spec['repo'], 'revision': spec['revision'], 'sha256': files}
    report['status'] = 'PAYLOAD_PREPARED_NATIVE_IO_UNVERIFIED'
    (CACHE / 'vrl-p0-assets.json').write_text(json.dumps(report, indent=2) + '\n')


def load_prepared(report):
    p = CACHE / 'vrl-p0-assets.json'
    require(p.exists(), 'Run prepare in Docker before p0')
    data = json.loads(p.read_text())
    for key in ('ledger_sha256', 'packet_sha256', 'image_id', 'source_sha256'):
        require(data[key] == report[key], f'Stale prepared payload: {key}')
    for model in data['models'].values():
        root = Path(model['path'])
        require(all(sha(root / name) == h for name, h in model['sha256'].items()), 'Payload hash mismatch')
    require(data['assets_sha256'] == tree_hashes(LIBERO / 'assets'), 'Simulator asset hash mismatch')
    report['prepared_manifest_sha256'] = sha(p)
    return data


def run_p0(ledger, contract, report, budget):
    import numpy as np
    import torch
    from PIL import Image
    from transformers import AutoTokenizer
    from openvla_oft.configuration_prismatic import OpenVLAConfig
    from openvla_oft.modeling_prismatic import OpenVLAForActionPrediction
    from openvla_oft.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
    from openvla_oft.constants import ACTION_DIM, NUM_ACTIONS_CHUNK, PROPRIO_DIM
    from libero.libero.envs import OffScreenRenderEnv
    require((ACTION_DIM, NUM_ACTIONS_CHUNK, PROPRIO_DIM) == (7, 8, 8), 'Wrong robot constants')
    prepared = load_prepared(report)
    task, states, task_info = task_and_states(contract)
    require(task_info == prepared['task'], 'Init/task payload changed')
    report['task'] = task_info
    fn = helpers()

    class CapturingVLA(OpenVLAForActionPrediction):
        def _unnormalize_actions(self, normalized_actions, unnorm_key=None):
            self.p0_normalized = np.asarray(normalized_actions).copy()
            return super()._unnormalize_actions(normalized_actions, unnorm_key)

    env = None
    report['arms'] = []
    frozen_encoder = None
    first_reset = None
    stats_a = None
    try:
        env = OffScreenRenderEnv(bddl_file_name=task_info['bddl_file'], robots=['Panda'],
                                 controller='OSC_POSE', control_freq=20, camera_heights=256, camera_widths=256)
        low, high = env.env.action_spec
        require(np.shape(low) == (7,) and np.shape(high) == (7,), 'Controller action bounds mismatch')
        report['controller'] = {'control_freq': env.env.control_freq, 'low': low.tolist(), 'high': high.tolist(),
                                'config': env.env.robots[0].controller_config}
        report['controller_sha256'] = hashlib.sha256(json.dumps(report['controller'], sort_keys=True, default=str).encode()).hexdigest()
        require(env.env.control_freq == 20, 'Native control rate mismatch')
        for label in ('A', 'B'):
            arm = {'label': label, 'steps': 0, 'query_attempts': 0}
            report['arms'].append(arm)
            budget.charge('resets')
            env.seed(0)
            env.env.reset()  # Bypass wrapper's unbounded RandomizationError retry loop.
            obs = env.set_init_state(states[0])
            warmup = contract['task']['warmup_environment_action']
            for _ in range(10):
                budget.charge('warmup_steps')
                obs, _, done, _ = env.step(warmup)
                require(not done and not env.check_success(), 'Terminal during warmup; pair not IO-qualified')
            state_bytes = env.env.sim.get_state().flatten().tobytes()
            reset = {'state_sha256': hashlib.sha256(state_bytes).hexdigest(),
                     'rgb_sha256': hashlib.sha256(obs['agentview_image'].tobytes()).hexdigest()}
            arm['reset'] = reset
            if first_reset is None:
                first_reset = reset
            require(reset == first_reset, 'A/B reset state or RGB differs; stop before second query')
            from OpenGL.GL import glGetString, GL_RENDERER, GL_VENDOR
            renderer, vendor = glGetString(GL_RENDERER), glGetString(GL_VENDOR)
            arm['graphics'] = {'renderer': str(renderer), 'vendor': str(vendor)}
            require(vendor is not None and b'NVIDIA' in vendor.upper(), 'NVIDIA EGL renderer not established')
            path = Path(prepared['models'][label]['path'])
            stats = json.loads((path / 'dataset_statistics.json').read_text())
            if stats_a is None:
                stats_a = stats[NORMALIZER]
            require(stats[NORMALIZER] == stats_a, 'A/B normalizer mismatch')
            config = OpenVLAConfig.from_pretrained(path, local_files_only=True)
            require(not config.use_proprio, 'Checkpoint unexpectedly uses VLA proprio')
            config.norm_stats = stats
            torch.manual_seed(0)
            torch.cuda.reset_peak_memory_stats()
            model, loading = CapturingVLA.from_pretrained(path, config=config, torch_dtype=torch.bfloat16,
                                attn_implementation='eager', low_cpu_mem_usage=True, local_files_only=True,
                                output_loading_info=True)
            require(not any(loading.get(k) for k in ('missing_keys', 'unexpected_keys', 'mismatched_keys', 'error_msgs')),
                    f'Checkpoint loading mismatch: {loading}')
            model.eval().requires_grad_(False).cuda()
            model.vision_backbone.set_num_images_in_input(1)
            # Count both explicit residual-encoder calls and each base query's vision forward.
            model.vision_backbone.register_forward_pre_hook(lambda _module, _inputs: budget.charge('encoder_calls'))
            if label == 'A':
                frozen_encoder = (model.vision_backbone, model.projector)
            processor = PrismaticProcessor(PrismaticImageProcessor.from_pretrained(path, local_files_only=True),
                            AutoTokenizer.from_pretrained(path, local_files_only=True, trust_remote_code=False))
            image = fn['center_crop_image'](Image.fromarray(fn['get_libero_image'](obs, 224)).convert('RGB'))
            prompt = f'In: What action should the robot take to {task.language.lower()}?\nOut:'
            inputs = processor(prompt, image).to('cuda')
            if not torch.all(inputs['input_ids'][:, -1] == 29871):
                inputs['input_ids'] = torch.cat([inputs['input_ids'], torch.tensor([[29871]], device='cuda')], dim=1)
                inputs['attention_mask'] = torch.cat([inputs['attention_mask'], torch.ones((1, 1), device='cuda', dtype=inputs['attention_mask'].dtype)], dim=1)
            require(processor.tokenizer.pad_token_id is not None, 'Missing padding token')
            with torch.inference_mode(), torch.autocast('cuda', dtype=torch.bfloat16):
                patches = frozen_encoder[1](frozen_encoder[0](inputs['pixel_values']))
                require(patches.ndim == 3 and patches.shape[-1] == model.config.text_config.hidden_size,
                        'Projected feature shape mismatch')
                require(torch.isfinite(patches).all().item(), 'Nonfinite frozen A features')
                feat = patches.mean(dim=1).float().cpu().numpy()[0]
                arm['encoder'] = {'source': 'A', 'shape': list(patches.shape), 'dtype': str(patches.dtype),
                                  'patch_mean_sha256': hashlib.sha256(feat.tobytes()).hexdigest()}
                del patches
                budget.charge('queries')
                arm['query_attempts'] += 1
                actions, ids = model.generate_action_verl(**inputs, proprio=None, use_film=False,
                    padding_idx=processor.tokenizer.pad_token_id, do_sample=False, temperature=1.0, unnorm_key=NORMALIZER)
            require(np.shape(actions) == (1, 8, 7), 'Expected one 8x7 chunk')
            normalized = model.p0_normalized.reshape(8, 7)
            from_ids = model.bin_centers[np.clip(model.vocab_size - ids.cpu().numpy() - 1, 0, len(model.bin_centers) - 1)].reshape(8, 7)
            require(np.array_equal(normalized, from_ids), 'Token decode mismatch')
            require(np.isfinite(actions).all() and np.isfinite(normalized).all(), 'Nonfinite action')
            composed_norm = normalized.copy()
            composed_norm[:, :6] = np.clip(composed_norm[:, :6] + contract['action']['residual_scale'] * np.zeros((8, 6)), -1, 1)
            # Invoke the pinned original unnormalizer without another model query.
            composed = OpenVLAForActionPrediction._unnormalize_actions(model, composed_norm, NORMALIZER)

            def command(a):
                return np.clip(fn['invert_gripper_action'](fn['normalize_gripper_action'](a, binarize=True)), low, high)

            native, zero = command(actions[0]), command(composed)
            error = float(np.max(np.abs(native - zero)))
            require(np.allclose(native, zero, atol=ZERO_ATOL, rtol=0), 'Zero-residual action mismatch')
            proprio = np.concatenate([obs['robot0_eef_pos'], fn['quat2axisangle'](obs['robot0_eef_quat'].copy()), obs['robot0_gripper_qpos']])
            require(proprio.shape == (8,), 'Proprio order/width mismatch')
            pn = fn['normalize_proprio'](proprio, stats_a['proprio'])
            x = np.concatenate([feat, feat, pn, pn, np.asarray(warmup), [1.0]])
            require(x.shape == (2 * len(feat) + 24,) and np.isfinite(x).all(), 'Residual state mismatch')
            arm.update(normalized_chunk=normalized.tolist(), native_commands=native.tolist(), zero_commands=zero.tolist(),
                       zero_max_error=error, zero_atol=ZERO_ATOL, zero_rtol=0, proprio_order='eef_pos3, axis_angle3, gripper_qpos2',
                       proprio=proprio.tolist(), residual_state_dimension=len(x), action_dtype=str(actions.dtype),
                       first_history='duplicate current; last command=warmup; remaining policy fraction=1')
            for action in zero:
                budget.charge('policy_steps')
                obs, reward, done, _ = env.step(action.tolist())
                arm['steps'] += 1
                if done or env.check_success():
                    arm['early_terminal'] = True
                    break
            arm['cuda_peak_allocated_bytes'] = torch.cuda.max_memory_allocated()
            arm['cuda_peak_reserved_bytes'] = torch.cuda.max_memory_reserved()
            del model, inputs, processor
            gc.collect()
            torch.cuda.empty_cache()
        require(budget.used['queries'] == 2 and budget.used['resets'] == 2 and budget.used['encoder_calls'] == 4,
                'Incomplete IO packet; not a P0 pass')
        report['status'] = 'P0_IO_PASSED_NOT_POLICY_EVIDENCE'
    finally:
        if env is not None:
            env.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('phase', choices=['prepare', 'p0'])
    ap.add_argument('--ledger', type=Path, required=True)
    args = ap.parse_args()
    require(Path('/.dockerenv').exists(), 'Run through resume.py on local Docker')
    target = Path('/results') / (args.phase + '.json')
    require(not target.exists(), 'Do not overwrite previous phase evidence')
    ledger = json.loads(args.ledger.read_text())
    budget = Budget()
    report = {'status': 'STARTED', 'phase': args.phase, 'ledger_sha256': sha(args.ledger),
              'packet_sha256': os.environ['VRL_PACKET_SHA'], 'image_id': os.environ['VRL_IMAGE_ID'],
              'policy_effect_measured': False, 'training_updates': 0, 'model_attention': 'eager',
              'model_precision': 'BF16 (B stored FP32 cast on load)', 'automatic_retry': False,
              'package_freeze': Path('/opt/vrl/resolved-packages.txt').read_text(),
              'system_package_freeze': Path('/opt/vrl/resolved-system-packages.txt').read_text()}
    start = time.monotonic()
    try:
        contract = validate_contract(ledger)
        report['runtime'] = setup_runtime()
        report['source_sha256'] = verify_sources(ledger, contract)
        if args.phase == 'prepare':
            prepare(ledger, contract, report)
        else:
            run_p0(ledger, contract, report, budget)
    except Exception as exc:
        report.update(status='STOPPED_NO_RETRY', error_type=type(exc).__name__, error=str(exc))
        raise
    finally:
        report.update(attempted_calls=budget.used, env_step_attempts=budget.used['warmup_steps'] + budget.used['policy_steps'],
                      wall_seconds=time.monotonic() - start)
        target.write_text(json.dumps(report, indent=2, default=str) + '\n')


if __name__ == '__main__':
    main()
