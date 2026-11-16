#!/usr/bin/env python3
"""Docker-only, bounded HINDSIGHT P0. No optimizer, training loop or P1/P2 entry point."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import random
import subprocess
import time
import traceback

ROOT = Path('/opt/hindsight')
PACKET = ROOT / 'packet'
CACHE = Path('/cache')
RESULTS = Path('/results')


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def require(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def container_only():
    require(Path('/.dockerenv').exists(), 'This probe must run inside local Docker')


def file_hash(path, algorithm='sha256', git_blob=False):
    h = hashlib.new(algorithm)
    if git_blob:
        h.update(b'blob ' + str(path.stat().st_size).encode() + b'\0')
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def verify_file(path, size, digest, algorithm='sha256', git_blob=False):
    require(path.is_file() and path.stat().st_size == size, 'File missing/size mismatch: ' + str(path))
    require(file_hash(path, algorithm, git_blob) == digest, 'File digest mismatch: ' + str(path))


def seed_key(stage, master_seed, task, init_index, query, purpose):
    key = f'hindsight-n2|{stage}|{master_seed}|{task}|{init_index}|{query}|{purpose}'
    return int.from_bytes(hashlib.sha256(key.encode()).digest()[:4], 'big')


class Budget:
    def __init__(self, limits, seconds, clock=time.monotonic):
        self.limits, self.clock, self.seconds = limits, clock, seconds
        self.start = clock()
        self.counts = {key: 0 for key in limits}

    def take(self, key, n=1):
        require(key in self.counts and isinstance(n, int) and n > 0, 'Invalid budget event')
        require(self.clock() - self.start < self.seconds, 'P0 time limit reached')
        require(self.counts[key] + n <= self.limits[key], 'P0 limit reached: ' + key)
        self.counts[key] += n  # Reserve BEFORE work, including failed attempts.


def sources(plan, fetch=False):
    result = {}
    for repo in plan['repos']:
        root = ROOT / repo['name']
        if fetch:
            root.mkdir(parents=True, exist_ok=False)
            for command in (['git', 'init', str(root)],
                            ['git', '-C', str(root), 'fetch', '--depth', '1', repo['url'], repo['revision']],
                            ['git', '-C', str(root), 'checkout', '--detach', 'FETCH_HEAD']):
                subprocess.run(command, check=True, timeout=1800)
        rev = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
        require(rev == repo['revision'], 'Source revision mismatch: ' + repo['name'])
        for item in repo['files']:
            require(file_hash(root / item['path']) == item['sha256'], 'Source file mismatch: ' + item['path'])
        result[repo['name']] = rev
    return result


def package_versions():
    return {d.metadata['Name']: d.version for d in importlib.metadata.distributions() if d.metadata['Name']}


def configure_libero():
    base = ROOT / 'libero/libero/libero'
    cfg = Path(os.environ['LIBERO_CONFIG_PATH'])
    cfg.mkdir(parents=True, exist_ok=True)
    # JSON is valid YAML; prevents LIBERO's interactive first-import prompt.
    write_json(cfg / 'config.yaml', {'benchmark_root': str(base), 'bddl_files': str(base / 'bddl_files'),
        'init_states': str(base / 'init_files'), 'assets': str(base / 'assets'), 'datasets': '/cache/datasets'})


def payload_manifest(plan):
    import numpy as np
    import torch
    files = []
    for f in plan['checkpoint']['files']:
        path = CACHE / 'model' / f['rfilename']
        lfs = f.get('lfs')
        verify_file(path, f['size'], lfs['sha256'] if lfs else f['blobId'],
                    'sha256' if lfs else 'sha1', git_blob=not bool(lfs))
        files.append({'path': f['rfilename'], 'sha256': file_hash(path), 'size': f['size']})
    require(file_hash(CACHE / 'model/dataset_statistics.json') == plan['checkpoint']['normalizer_sha256'],
            'Normalizer hash mismatch')
    stats = json.loads((CACHE / 'model/dataset_statistics.json').read_text())
    require(plan['contract']['model_config']['unnorm_key'] in stats, 'Normalizer key absent')
    cases = []
    for case in plan['cases']:
        root = ROOT / 'libero'
        require(file_hash(root / case['bddl_path']) == case['bddl_sha256'], 'BDDL hash mismatch')
        f = case['init_file']
        path = root / f['path']
        verify_file(path, f['size_bytes'], f['git_blob_sha1'], 'sha1', git_blob=True)
        # Deserialize only after matching the pinned public Git blob, and only in Docker.
        rows = torch.load(path, map_location='cpu', weights_only=False)
        hashes = []
        for row in rows:
            a = np.asarray(row, dtype='<f8')
            require(a.ndim == 1 and bool(np.isfinite(a).all()), 'Malformed init state')
            hashes.append(hashlib.sha256(a.tobytes()).hexdigest())
        require(hashes, 'No state rows')
        cases.append({'label': case['label'], 'payload_sha256': file_hash(path),
                      'rows': len(hashes), 'row_sha256': hashes})
    # All duplicate identities, with roles left visible; no automatic split repair.
    identities = {}
    for case in cases:
        for i, digest in enumerate(case['row_sha256']):
            identities.setdefault(digest, []).append([case['label'], i])
    duplicates = [rows for rows in identities.values() if len(rows) > 1]
    assets = ROOT / 'libero/libero/libero/assets'
    asset_hashes = {}
    for p in sorted(assets.rglob('*')):
        if p.is_file():
            with p.open('rb') as f:
                require(not f.read(100).startswith(b'version https://git-lfs.github.com/spec'), 'Unresolved LFS asset')
            asset_hashes[str(p.relative_to(assets))] = file_hash(p)
    require(asset_hashes, 'LIBERO assets absent; do not silently use another asset revision')
    return {'checkpoint_files': files, 'init_cases': cases, 'duplicate_rows': duplicates,
            'at_least_30_rows_each': all(c['rows'] >= 30 for c in cases),
            'split_approved_for_p2': False, 'near_state_review': 'pending; exact hashes do not prove independence',
            'assets': asset_hashes}


def module_paths():
    import prismatic
    import transformers
    import rlinf
    from libero.libero import envs
    modules = {'oft': prismatic, 'transformers': transformers, 'rlinf': rlinf, 'libero': envs}
    paths = {}
    for name, module in modules.items():
        path = Path(module.__file__).resolve()
        require(path.is_relative_to(ROOT / name), 'Import shadowing: ' + str(path))
        paths[name] = str(path)
    return paths


def gpu_info():
    import torch
    require(torch.cuda.is_available() and torch.cuda.device_count() == 1, 'Exactly one CUDA device required')
    require(torch.cuda.is_bf16_supported(), 'BF16 unsupported; no dtype fallback')
    p = torch.cuda.get_device_properties(0)
    return {'name': p.name, 'total_memory': p.total_memory, 'torch': torch.__version__,
            'cuda': torch.version.cuda, 'capability': list(torch.cuda.get_device_capability(0))}


def prepare(plan):
    identity = sources(plan)
    configure_libero()
    runtime = {'gpu': gpu_info(), 'module_paths': module_paths(), 'packages': package_versions()}
    from huggingface_hub import snapshot_download
    cp = plan['checkpoint']
    snapshot_download(repo_id=cp['repo'], revision=cp['revision'], local_dir=str(CACHE / 'model'),
                      allow_patterns=[f['rfilename'] for f in cp['files']])
    payload = payload_manifest(plan)
    record = {'packet_sha': os.environ['HINDSIGHT_PACKET_SHA'], 'sources': identity,
              'runtime': runtime, 'payload': payload, 'native_p0_passed': False}
    write_json(CACHE / 'prepared.json', record)
    write_json(RESULTS / 'prepared.json', record)


def p0(plan, report):
    import numpy as np
    import torch
    from omegaconf import OmegaConf
    from PIL import Image
    require(os.environ.get('HF_HUB_OFFLINE') == '1', 'P0 must be offline')
    sources(plan)
    configure_libero()
    report['gpu'] = gpu_info()
    report['module_paths'] = module_paths()
    ready = json.loads((CACHE / 'prepared.json').read_text())
    require(ready['packet_sha'] == os.environ['HINDSIGHT_PACKET_SHA'], 'Stale payload manifest')
    require(payload_manifest(plan) == ready['payload'], 'Prepared payload changed')
    contract = plan['contract']
    budget = Budget(contract['limits'], contract['p0_timeout_seconds'])
    report['counts'] = budget.counts
    report['resolved_config'] = contract
    case = plan['cases'][0]
    s = seed_key('P0', 11, case['stem'], 0, 0, 'collection')
    random.seed(s)
    np.random.seed(s)
    torch.manual_seed(s)
    torch.cuda.manual_seed_all(s)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    report['rng_seed'] = s
    from rlinf.models.embodiment.openvla_oft.rlinf import get_model
    model = get_model(OmegaConf.create(contract['model_config']), torch_dtype=torch.bfloat16).cuda().eval()
    require(model.unnorm_key == contract['model_config']['unnorm_key'], 'Actual normalizer key mismatch')
    saved_stats = json.loads((CACHE / 'model/dataset_statistics.json').read_text())[model.unnorm_key]
    require(model.norm_stats[model.unnorm_key] == saved_stats, 'Loaded normalizer differs')
    require(model.language_model.config._attn_implementation == 'sdpa', 'Bidirectional SDPA path required')
    require(all(type(layer.self_attn).__name__ == 'LlamaSdpaAttention'
                for layer in model.language_model.model.layers), 'Wrong attention class')
    # Check actual pre-softmax precision, not just returned logprob dtype.
    def check_logits(module, args, output):
        require(output.logits.dtype == torch.float32, 'Logits are not FP32; no silent sampler change')
    model.language_model.register_forward_hook(check_logits)
    params = [(n, p) for n, p in model.named_parameters() if p.requires_grad]
    require(params, 'No trainable parameters')
    manifest = [{'name': n, 'shape': list(p.shape), 'dtype': str(p.dtype), 'elements': p.numel()} for n, p in params]
    report['trainable_elements'] = sum(p.numel() for _, p in params)
    report['parameter_manifest_sha256'] = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
    write_json(RESULTS / 'parameters.json', manifest)
    versions = {n: p._version for n, p in model.named_parameters()}
    import mujoco
    from robosuite.environments.base import MujocoEnv
    native_reset, native_step = MujocoEnv._reset_internal, mujoco.mj_step
    def guarded_reset(self, *args, **kwargs):
        budget.take('reset')
        return native_reset(self, *args, **kwargs)
    def guarded_step(*args, **kwargs):
        nstep = int(kwargs.get('nstep', args[2] if len(args) > 2 else 1))
        budget.take('physics', nstep)
        return native_step(*args, **kwargs)
    MujocoEnv._reset_internal, mujoco.mj_step = guarded_reset, guarded_step
    env = None
    trace, frames = [], []
    try:
        from libero.libero import benchmark
        from libero.libero.envs import OffScreenRenderEnv
        suite = benchmark.get_benchmark_dict()['libero_10'](task_order_index=0)
        task = suite.get_task(0)
        require(Path(task.bddl_file).stem == case['stem'], 'Task order/identity mismatch')
        env = OffScreenRenderEnv(bddl_file_name=str(ROOT / 'libero' / case['bddl_path']),
                                camera_heights=256, camera_widths=256, control_freq=20)
        # Avoid ControlEnv.reset's unbounded RandomizationError retry loop.
        env.env.reset()
        rows = torch.load(ROOT / 'libero' / case['init_file']['path'], map_location='cpu', weights_only=False)
        obs = env.set_init_state(rows[0])
        report['physics_timestep'] = float(env.sim.model.opt.timestep)
        report['control_hz'] = float(env.env.control_freq)
        require(report['control_hz'] == contract['control_hz'], 'Control rate mismatch')
        objects = ['alphabet_soup_1', 'tomato_sauce_1', 'cream_cheese_1', 'ketchup_1',
                   'orange_juice_1', 'milk_1', 'butter_1']
        def observe(observation, label):
            atomic = {o: bool(env.env._eval_predicate(['In', o, 'basket_1_contain_region'])) for o in objects}
            success = bool(env.check_success())
            require(success == (atomic[objects[0]] and atomic[objects[1]]), 'Goal conjunction mismatch')
            frame = np.ascontiguousarray(observation['agentview_image'][::-1, ::-1])
            require(frame.shape == (256, 256, 3) and frame.dtype == np.uint8, 'Unexpected RGB')
            frames.append(frame)
            trace.append({'event': label, 'control_count': budget.counts['control'],
                          'atomic': atomic, 'original': success, 'frame_index': len(frames) - 1,
                          'frame_sha256': hashlib.sha256(frame.tobytes()).hexdigest()})
            return frame
        observe(obs, 'init')
        for _ in range(contract['settling_steps']):
            budget.take('control')
            obs, reward, done, info = env.step([0., 0., 0., 0., 0., 0., -1.])
            observe(obs, 'settling')
            require(not done, 'Task ended during settling')
        require(budget.counts['physics'] > 0, 'Physics accounting hook did not observe steps')
        initial = frames[-1]
        def query(frame, index):
            qseed = seed_key('P0', 11, case['stem'], 0, index, 'collection')
            torch.manual_seed(qseed)
            torch.cuda.manual_seed_all(qseed)
            budget.take('query')
            actions, result = model.predict_action_batch(env_obs={
                'main_images': torch.from_numpy(frame.copy()).unsqueeze(0),
                'states': torch.zeros(1, 8), 'task_descriptions': [task.language]},
                do_sample=True, temperature=1.6, top_k=-1, calculate_logprobs=True, calculate_values=False)
            require(tuple(actions.shape) == (1, 8, 7), 'Unexpected action shape')
            require(bool(torch.isfinite(actions).all()), 'Nonfinite action')
            return actions.detach().cpu().numpy()[0], result
        actions, original = query(initial, 0)
        g_inputs = {k: v.detach().clone() for k, v in original['forward_inputs'].items()}
        old = original['prev_logprobs'].detach().reshape(1, 56)
        require(bool(torch.isfinite(old).all()), 'Nonfinite saved likelihood')
        executed, environment_actions = 0, []
        for action in actions:
            converted = action.copy()
            converted[-1] = -np.sign(2. * converted[-1] - 1.)
            budget.take('control')
            obs, reward, done, info = env.step(converted.tolist())
            executed += 1
            environment_actions.append(converted.tolist())
            observe(obs, 'policy')
            if done:
                break
        if not done:
            second_actions, second = query(frames[-1], 1)
            write_json(RESULTS / 'second_query.json', {'executed': False, 'actions': second_actions.tolist(),
                'tokens': second['forward_inputs']['action_tokens'].cpu().tolist(),
                'logprobs': second['prev_logprobs'].float().cpu().tolist()})
            del second, second_actions
        mask = torch.zeros_like(old, dtype=torch.bool)
        mask[:, :executed * 7] = True
        require(bool(mask.any()), 'No executed policy tokens')
        h = contract['auxiliary_goal_fixture']
        proc = model.input_processor(text=[f'In: What action should the robot take to {h.lower()}?\nOut: '],
            images={'images': torch.from_numpy(initial.copy()).permute(2, 0, 1)[None, None]},
            proprio_states=torch.zeros(1, 8), padding='max_length', max_length=128)
        pv = proc['pixel_values'].to(device='cuda', dtype=torch.bfloat16)
        pv = pv.reshape(1, -1, *pv.shape[-2:])
        require(tuple(pv.shape[-2:]) == (224, 224), 'Processor size mismatch')
        require(torch.equal(pv, g_inputs['pixel_values']), 'Goal change altered image input')
        h_inputs = dict(g_inputs, input_ids=proc['input_ids'].cuda().long(),
                        attention_mask=proc['attention_mask'].cuda().bool())
        require(h_inputs['input_ids'].shape == g_inputs['input_ids'].shape == (1, 128), 'Prompt length mismatch')
        require(not torch.equal(h_inputs['input_ids'], g_inputs['input_ids']), 'Goal fixture did not change tokens')
        def score(inputs):
            budget.take('rescore')
            lp = model.default_forward(forward_inputs={k: v.clone() for k, v in inputs.items()},
                    compute_logprobs=True, compute_entropy=False, compute_values=False,
                    use_cache=False, temperature=1.6, top_k=-1)['logprobs'].reshape(1, 56)
            require(lp.dtype == torch.float32 and bool(torch.isfinite(lp).all()), 'Invalid rescore')
            return lp
        with torch.no_grad():
            same, changed = score(g_inputs), score(h_inputs)
        error = (same - old).abs().max().item()
        report['same_goal_max_abs_error'] = error
        require(error <= contract['same_goal_logprob_atol'], 'Same-goal rescore differs; no tolerance retuning')
        report['gradient_fixture'] = []
        for name, inputs, advantage in [('zero_g', g_inputs, 0.), ('negative_h', h_inputs, -1.)]:
            model.zero_grad(set_to_none=True)
            lp = score(inputs)
            ratio = (lp - old).float().exp()
            require(bool(torch.isfinite(ratio).all()), 'Nonfinite ratio')
            loss = -torch.minimum(ratio * advantage, ratio.clamp(.8, 1.2) * advantage)[mask].mean()
            budget.take('backward')
            loss.backward()
            grad_sq, nonzero = 0., 0
            for _, param in params:
                if param.grad is not None:
                    require(bool(torch.isfinite(param.grad).all()), 'Nonfinite gradient')
                    norm = float(torch.linalg.vector_norm(param.grad.detach().float()).item())
                    grad_sq += norm * norm
                    nonzero += int(norm > 0.)
            report['gradient_fixture'].append({'name': name, 'synthetic_advantage': advantage,
                'loss': loss.item(), 'gradient_l2': grad_sq ** .5, 'nonzero_tensors': nonzero})
            require(nonzero == 0 if advantage == 0 else nonzero > 0, 'Gradient fixture inconclusive/failed')
            del loss, ratio, lp
        require(versions == {n: p._version for n, p in model.named_parameters()}, 'Parameters mutated during P0')
        normalized = model.bin_centers[np.clip(model.vocab_size - g_inputs['action_tokens'].cpu().numpy() - 1,
                                               0, len(model.bin_centers) - 1)]
        write_json(RESULTS / 'io.json', {'goal': task.language, 'hindsight_goal_is_synthetic_fixture': h,
            'actions_model': actions.tolist(), 'actions_normalized': normalized.tolist(),
            'actions_environment': environment_actions, 'tokens': g_inputs['action_tokens'].cpu().tolist(),
            'executed_token_mask': mask.cpu().tolist(), 'old_logprob': old.cpu().tolist(),
            'same_goal_logprob': same.cpu().tolist(), 'changed_goal_logprob': changed.cpu().tolist(),
            'g_input_ids': g_inputs['input_ids'].cpu().tolist(), 'h_input_ids': h_inputs['input_ids'].cpu().tolist(),
            'g_attention_mask': g_inputs['attention_mask'].cpu().tolist(),
            'h_attention_mask': h_inputs['attention_mask'].cpu().tolist()})
        np.savez_compressed(RESULTS / 'processed_image.npz', pixels=g_inputs['pixel_values'].float().cpu().numpy())
        report['status'] = 'P0_WIRING_PASS_ONLY'
        report['peak_cuda_allocated_bytes'] = torch.cuda.max_memory_allocated()
    finally:
        report['predicate_trace'] = trace
        MujocoEnv._reset_internal, mujoco.mj_step = native_reset, native_step
        for i, frame in enumerate(frames):
            Image.fromarray(frame).save(RESULTS / f'frame_{i:02d}.png')
        if env is not None:
            env.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['source-build', 'prepare', 'p0'])
    args = parser.parse_args()
    container_only()
    plan = json.loads((PACKET / 'plan.json').read_text())
    if args.phase == 'source-build':
        write_json(PACKET / 'build_sources.json', {'sources': sources(plan, fetch=True), 'packages': package_versions()})
        return
    require(os.environ.get('HINDSIGHT_PACKET_SHA') == os.environ.get('HINDSIGHT_IMAGE_SHA')
            and os.environ.get('HINDSIGHT_PACKET_SHA'), 'Stale image/packet identity')
    report = {'phase': args.phase, 'started_utc': datetime.now(timezone.utc).isoformat(),
              'status': 'INCOMPLETE', 'research_effect_measured': False, 'optimizer_steps': 0}
    start = time.monotonic()
    try:
        if args.phase == 'prepare':
            prepare(plan)
            report['status'] = 'PAYLOAD_VERIFIED_NATIVE_P0_PENDING'
        else:
            p0(plan, report)
    except BaseException as exc:
        report.update(error=str(exc), traceback=traceback.format_exc(), status='FAILED_NO_RESEARCH_CONCLUSION')
        raise
    finally:
        report['elapsed_seconds'] = time.monotonic() - start
        write_json(RESULTS / 'result.json', report)


if __name__ == '__main__':
    main()
