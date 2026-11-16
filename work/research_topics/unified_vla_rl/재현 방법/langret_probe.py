#!/usr/bin/env python3
"""Bounded LANGRET P0. Import is stdlib-only; native entry points require Docker."""
import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import random
import shutil
import signal
import subprocess
import time
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
BASE = Path('/opt/langret')
RESULTS = Path('/results')
P0_CAPS = dict(resets=2, policy_queries=2, actor_rescores=2, backwards=1, control_steps=36, physics_steps=10000)


def require_container():
    if not Path('/.dockerenv').exists():
        raise RuntimeError('Native/payload operations are Docker-only')


def digest_file(path, algorithm='sha256', git_blob=False):
    h = hashlib.new(algorithm)
    if git_blob:
        h.update(('blob ' + str(path.stat().st_size) + '\0').encode())
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_file(path, record):
    if not path.is_file() or path.stat().st_size != record['size']:
        raise RuntimeError('Missing/wrong size: ' + str(path))
    value = digest_file(path, record['algorithm'], record.get('git_blob', False))
    if value != record['hash']:
        raise RuntimeError('Hash mismatch: ' + str(path))


class Budget:
    def __init__(self, limits):
        self.limits = dict(limits)
        self.counts = dict.fromkeys(limits, 0)

    def take(self, key, amount=1):
        if key not in self.limits or type(amount) is not int or amount < 0:
            raise RuntimeError('Unknown counter or invalid increment')
        if self.counts[key] + amount > self.limits[key]:
            raise RuntimeError('Budget exhausted BEFORE operation: ' + key)
        self.counts[key] += amount


def safe_path(root, relative):
    p = (root / relative).resolve()
    if p == root.resolve() or root.resolve() not in p.parents:
        raise RuntimeError('Path escapes owned directory')
    return p


def validate_plan(plan):
    if set(plan['limits']) != set(P0_CAPS):
        raise RuntimeError('Incomplete P0 budget')
    for key, cap in P0_CAPS.items():
        value = plan['limits'][key]
        if type(value) is not int or not 0 <= value <= cap:
            raise RuntimeError('P0 cap exceeded: ' + key)
    if len(plan['pair']['prompts']) != 2 or len(set(plan['pair']['targets'])) != 2:
        raise RuntimeError('P0 requires exactly two paired prompts and distinct targets')
    if len(plan['pair']['targets']) != 2 or plan['init_row'] != 0:
        raise RuntimeError('P0 is restricted to the selected dev row and two targets')


def bounded_call(budget, key, operation):
    def call(*args, **kwargs):
        budget.take(key)
        return operation(*args, **kwargs)
    return call


def physics_call(budget, name, operation):
    def call(*args, **kwargs):
        # Half-step primitives count conservatively; multi-step calls consume their whole budget first.
        count = kwargs.get('nstep', args[2] if name == 'mj_step' and len(args) > 2 else 1)
        budget.take('physics_steps', count)
        return operation(*args, **kwargs)
    return call


def read_plan():
    return json.loads((HERE / 'plan.json').read_text())


def install_sources(plan):
    require_container()
    for src in plan['sources']:
        dst = BASE / src['directory']
        subprocess.run(['git', 'init', str(dst)], check=True)
        subprocess.run(['git', '-C', str(dst), 'remote', 'add', 'origin', src['url']], check=True)
        env = dict(os.environ, GIT_LFS_SKIP_SMUDGE='1')
        subprocess.run(['git', '-C', str(dst), 'fetch', '--depth=1', 'origin', src['revision']], env=env, check=True)
        subprocess.run(['git', '-C', str(dst), 'checkout', '--detach', 'FETCH_HEAD'], env=env, check=True)
        got = subprocess.check_output(['git', '-C', str(dst), 'rev-parse', 'HEAD'], text=True).strip()
        if got != src['revision']:
            raise RuntimeError('Source revision mismatch')
    verify_sources(plan)
    package = BASE / 'packages/langret_hf'
    package.mkdir(parents=True)
    (package / '__init__.py').write_text('')
    for name in ('modeling_prismatic.py', 'configuration_prismatic.py', 'processing_prismatic.py', 'constants.py', 'train_utils.py'):
        shutil.copyfile(BASE / 'SimpleVLA-RL/verl/utils/vla_utils/openvla_oft' / name, package / name)


def verify_sources(plan):
    for r in plan['source_files']:
        p = safe_path(BASE / r['directory'], r['path'])
        if digest_file(p) != r['sha256']:
            raise RuntimeError('Reviewed source changed: ' + str(p))


def configure():
    require_container()
    import yaml
    root = BASE / 'VLA-CF/libero/libero'
    conf = dict(benchmark_root=str(root), bddl_files=str(root / 'bddl_files'),
                init_states=str(root / 'init_files'), assets=str(root / 'assets'),
                conditions=str(root / 'conditions'), datasets='/cache/datasets')
    dest = BASE / 'libero-config'
    dest.mkdir(exist_ok=True)
    (dest / 'config.yaml').write_text(yaml.safe_dump(conf))


def checkpoint_records(plan):
    return plan['checkpoint']['files']


def verify_checkpoint(plan, cp):
    for r in checkpoint_records(plan):
        verify_file(safe_path(cp, r['path']), r)


def prepare(plan):
    require_container()
    verify_sources(plan)
    import torch
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError('CUDA/BF16 unavailable; no checkpoint download')
    for name in ('resolved-packages.txt', 'resolved-system-packages.txt'):
        shutil.copyfile(BASE / name, RESULTS / name)
    cp = Path('/cache/checkpoint')
    cp.mkdir(parents=True, exist_ok=True)
    Path('/cache/datasets').mkdir(exist_ok=True)
    if shutil.disk_usage('/cache').free < 50 * 1024**3:
        raise RuntimeError('Selected free cache-space floor 50 GiB not met')
    for r in checkpoint_records(plan):
        dest = safe_path(cp, r['path'])
        if dest.exists():
            verify_file(dest, r)
            continue
        url = 'https://huggingface.co/' + plan['checkpoint']['repo'] + '/resolve/' + plan['checkpoint']['revision'] + '/' + r['path']
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_name(dest.name + '.part')
        with urlopen(Request(url, headers={'User-Agent': 'PaperRegistry-LANGRET-P0'}), timeout=60) as response, tmp.open('wb') as f:
            shutil.copyfileobj(response, f, length=1024 * 1024)
        verify_file(tmp, r)
        tmp.replace(dest)
    verify_checkpoint(plan, cp)
    asset_root = BASE / 'VLA-CF/libero/libero/assets'
    assets = {}
    for p in sorted(asset_root.rglob('*')):
        if p.is_file():
            with p.open('rb') as f:
                if f.read(80).startswith(b'version https://git-lfs.github.com/spec/v1'):
                    raise RuntimeError('Unmaterialized Git LFS asset: ' + str(p))
            assets[str(p.relative_to(asset_root))] = digest_file(p)
    if not assets:
        raise RuntimeError('No simulator assets found')
    init = BASE / 'VLA-CF' / plan['pair']['init']['path']
    verify_file(init, plan['pair']['init'])
    record = dict(packet_sha256=plan['packet_sha256'], checkpoint_files=checkpoint_records(plan),
                  init_sha256=digest_file(init), assets_sha256=assets, native_model_or_simulation_run=False)
    (Path('/cache') / 'prepared.json').write_text(json.dumps(record, indent=2))
    (RESULTS / 'prepared.json').write_text(json.dumps(record, indent=2))


def extract_functions(path, names, namespace):
    """Execute only the frozen upstream preprocessing functions, without importing the RL worker."""
    tree = ast.parse(path.read_text())
    selected = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    if {n.name for n in selected} != set(names):
        raise RuntimeError('Required upstream preprocessing function missing')
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), 'exec'), namespace)
    return namespace


def goal_consistency(target, observed, reward, done):
    expected = bool(observed[target])
    if bool(done) != expected or not math.isclose(float(reward), float(expected), abs_tol=1e-8):
        raise RuntimeError('Target predicate/reward/termination disagree')


def require_prepared(plan, prepared):
    if prepared['packet_sha256'] != plan['packet_sha256']:
        raise RuntimeError('Prepared cache belongs to a different packet')


def native(plan, report, budget):
    require_container()
    verify_sources(plan)
    cp = Path('/cache/checkpoint')
    verify_checkpoint(plan, cp)
    prepared = json.loads(Path('/cache/prepared.json').read_text())
    require_prepared(plan, prepared)
    for rel, sha in prepared['assets_sha256'].items():
        if digest_file(safe_path(BASE / 'VLA-CF/libero/libero/assets', rel)) != sha:
            raise RuntimeError('Simulator asset changed: ' + rel)
    import numpy as np
    import torch
    import tensorflow as tf
    from PIL import Image
    from peft import LoraConfig, get_peft_model
    from transformers import AutoTokenizer
    from langret_hf.configuration_prismatic import OpenVLAConfig
    from langret_hf.modeling_prismatic import OpenVLAForActionPrediction
    from langret_hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
    from langret_hf.constants import ACTION_DIM, NUM_ACTIONS_CHUNK, ACTION_PROPRIO_NORMALIZATION_TYPE
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError('CUDA/BF16 unavailable')
    if ACTION_DIM != 7 or NUM_ACTIONS_CHUNK != 8 or ACTION_PROPRIO_NORMALIZATION_TYPE.value != 'bounds_q99':
        raise RuntimeError('Wrong LIBERO constants')
    report['device'] = dict(name=torch.cuda.get_device_name(0), cuda=torch.version.cuda,
                            capability=torch.cuda.get_device_capability(0))
    tf.config.set_visible_devices([], 'GPU')
    namespace = dict(np=np, tf=tf, Image=Image)
    extract_functions(BASE / 'SimpleVLA-RL/verl/workers/rollout/rob_rollout.py', ['crop_and_resize', 'center_crop_image'], namespace)
    extract_functions(BASE / 'SimpleVLA-RL/verl/utils/libero_utils.py', ['normalize_gripper_action', 'invert_gripper_action', 'get_libero_dummy_action'], namespace)
    config = OpenVLAConfig.from_pretrained(cp)
    config.text_config._attn_implementation = 'sdpa'
    config.text_config.use_cache = False
    base = OpenVLAForActionPrediction.from_pretrained(cp, config=config, torch_dtype=torch.bfloat16,
                                                    attn_implementation='sdpa', low_cpu_mem_usage=True).to('cuda')
    base.vision_backbone.set_num_images_in_input(1)
    base.norm_stats = json.loads((cp / 'dataset_statistics.json').read_text())
    key = plan['normalizer_key']
    if key not in base.norm_stats or base.vocab_size != 32000:
        raise RuntimeError('Wrong normalizer/vocabulary')
    processor = PrismaticProcessor(PrismaticImageProcessor.from_pretrained(cp),
                                    AutoTokenizer.from_pretrained(cp, trust_remote_code=False))
    if processor.tokenizer.pad_token_id is None:
        raise RuntimeError('Tokenizer has no pad ID')
    torch.manual_seed(plan['seed'])
    model = get_peft_model(base, LoraConfig(r=32, lora_alpha=32, lora_dropout=0,
                                           target_modules='all-linear', init_lora_weights='gaussian'))
    model.eval()
    trainable = [(name, p) for name, p in model.named_parameters() if p.requires_grad]
    if not trainable or any('lora_' not in name for name, _ in trainable):
        raise RuntimeError('Unexpected trainable parameter set')
    report['trainable'] = dict(names=[n for n, _ in trainable], parameters=sum(p.numel() for _, p in trainable))
    import mujoco
    from robosuite.environments.base import MujocoEnv
    from libero.libero.envs import OffScreenRenderEnv
    init_file = BASE / 'VLA-CF' / plan['pair']['init']['path']
    verify_file(init_file, plan['pair']['init'])
    # Trusted, hash-pinned project init data is deserialized only in the isolated offline container.
    rows = torch.load(init_file, map_location='cpu', weights_only=False)
    if len(rows) <= plan['init_row']:
        raise RuntimeError('Requested dev init row missing')
    initial = np.asarray(rows[plan['init_row']], dtype=np.float64)
    if initial.ndim != 1 or not np.isfinite(initial).all():
        raise RuntimeError('Invalid init row')
    report['init'] = dict(row=plan['init_row'], row_count=len(rows), shape=list(initial.shape),
                          sha256=hashlib.sha256(initial.tobytes()).hexdigest(), selection='IO dev only; no train/test split assigned')
    original_reset = MujocoEnv._reset_internal
    original_steps = {name: getattr(mujoco, name) for name in ('mj_step', 'mj_step1', 'mj_step2')}
    MujocoEnv._reset_internal = bounded_call(budget, 'resets', original_reset)
    for name, fn in original_steps.items():
        setattr(mujoco, name, physics_call(budget, name, fn))
    first_state = first_rgb = first_ctrl = None
    report['branches'] = []
    try:
        for branch, (prompt, target) in enumerate(zip(plan['pair']['prompts'], plan['pair']['targets'])):
            random.seed(plan['seed']); np.random.seed(plan['seed']); torch.manual_seed(plan['seed'])
            env = None
            try:
                # Constructor already initializes the episode; no unbounded ControlEnv.reset retry loop.
                env = OffScreenRenderEnv(bddl_file_name=str(BASE / 'VLA-CF' / plan['pair']['bddl']),
                                         camera_heights=256, camera_widths=256, control_freq=20,
                                         render_gpu_device_id=0, horizon=1000)
                env.seed(plan['seed'])
                env.set_success_any_conditions([target])
                if env.env._custom_success_any != [target.split()]:
                    raise RuntimeError('Singleton goal binding failed')
                obs = env.set_init_state(initial.copy())
                observed = env.evaluate_conditions(plan['pair']['targets'])
                if any(observed.values()):
                    raise RuntimeError('A/B goal already true before action')
                for _ in range(10):
                    budget.take('control_steps')
                    obs, reward, done, _ = env.step(namespace['get_libero_dummy_action']('openvla'))
                    observed = env.evaluate_conditions(plan['pair']['targets'])
                    goal_consistency(target, observed, reward, done)
                    if any(observed.values()):
                        raise RuntimeError('Goal became true during settle')
                state = env.get_sim_state().copy()
                rgb = obs['agentview_image'][::-1, ::-1].copy()
                controller = env.robots[0].controller
                ctrl = {k: v.tolist() if isinstance(v, np.ndarray) else v for k, v in vars(controller).items()
                        if isinstance(v, (np.ndarray, float, int, bool, str))}
                ctrl_sha = hashlib.sha256(json.dumps(ctrl, sort_keys=True, allow_nan=False).encode()).hexdigest()
                if first_state is None:
                    first_state, first_rgb, first_ctrl = state, rgb, ctrl_sha
                elif not np.array_equal(first_state, state) or not np.array_equal(first_rgb, rgb) or first_ctrl != ctrl_sha:
                    raise RuntimeError('Paired reset state/RGB/controller fields differ')
                Image.fromarray(rgb).save(RESULTS / ('initial_' + str(branch) + '.png'))
                image = namespace['center_crop_image'](Image.fromarray(rgb).convert('RGB'))
                batch = processor('In: What action should the robot take to ' + prompt.lower() + '?\nOut:', image)
                if batch['input_ids'][0, -1].item() != 29871:
                    batch['input_ids'] = torch.cat([batch['input_ids'], torch.tensor([[29871]])], dim=1)
                    batch['attention_mask'] = torch.cat([batch['attention_mask'], torch.ones((1, 1), dtype=batch['attention_mask'].dtype)], dim=1)
                batch = {k: v.to('cuda', dtype=torch.bfloat16) if k == 'pixel_values' else v.to('cuda') for k, v in batch.items()}
                sampled_logits = []
                patch_count = base.vision_backbone.get_num_patches()
                start = batch['input_ids'].shape[1] - 1 + patch_count
                def capture_logits(module, args, output):
                    # The pinned Llama head emits FP32 even for BF16 weights. Refuse silent casting.
                    if output.logits.dtype != torch.float32:
                        raise RuntimeError('Sampler logit dtype differs from reviewed FP32 source')
                    sampled_logits.append(output.logits[:, start:start + 56, -320:-64].detach())
                hook = base.language_model.register_forward_hook(capture_logits)
                try:
                    budget.take('policy_queries')
                    with torch.no_grad():
                        actions, ids = base.generate_action_verl(**batch, proprio=None, padding_idx=processor.tokenizer.pad_token_id,
                                                               do_sample=True, temperature=1.6, unnorm_key=key)
                finally:
                    hook.remove()
                if len(sampled_logits) != 1 or tuple(sampled_logits[0].shape) != (1, 56, 256):
                    raise RuntimeError('Unexpected query output/forward count')
                if tuple(ids.shape) != (1, 56) or tuple(actions.shape) != (1, 8, 7):
                    raise RuntimeError('Unexpected token/action shape')
                index = ids.long() - 31744
                if index.min() < 0 or index.max() > 255:
                    raise RuntimeError('Out-of-support action token')
                sampled_logp = torch.log_softmax(sampled_logits[0] / 1.6, -1).gather(-1, index.unsqueeze(-1)).squeeze(-1)
                # Actual multinomial uses softmax weights; log_softmax is a numerical approximation to them.
                sampling_weights = torch.softmax(sampled_logits[0] / 1.6, -1)
                sampling_weights = sampling_weights / sampling_weights.sum(-1, keepdim=True)
                actual_logp = sampling_weights.gather(-1, index.unsqueeze(-1)).squeeze(-1).log()
                rounding_error = (sampled_logp - actual_logp).abs().max().item()
                if not torch.isfinite(actual_logp).all() or rounding_error > 1e-5:
                    raise RuntimeError('Softmax/log_softmax sampling discrepancy')
                budget.take('actor_rescores')
                with torch.set_grad_enabled(branch == 0):
                    logits = model(**batch, proprio=None)
                    logits = logits[..., -320:-64].float()
                    if tuple(logits.shape) != (1, 56, 256):
                        raise RuntimeError('Actor output shape mismatch')
                    logp = torch.log_softmax(logits / 1.6, -1).gather(-1, index.unsqueeze(-1)).squeeze(-1)
                    error = (logp.detach() - sampled_logp).abs().max().item()
                    if not torch.isfinite(logp).all() or error > 0.02:
                        raise RuntimeError('Sample/re-score mismatch, max absolute log-prob error=' + str(error))
                    if branch == 0:
                        budget.take('backwards')
                        (-logp.mean()).backward()
                        grads = [p.grad for _, p in trainable if p.grad is not None]
                        if not grads or not all(torch.isfinite(g).all() for g in grads) or not any(g.abs().max() > 0 for g in grads):
                            raise RuntimeError('LoRA gradient fixture failed')
                        model.zero_grad(set_to_none=True)
                original_actions = np.asarray(actions[0])
                if not np.isfinite(original_actions).all():
                    raise RuntimeError('Nonfinite decoded action')
                events = []
                for a in original_actions:
                    command = namespace['invert_gripper_action'](namespace['normalize_gripper_action'](a.copy(), binarize=True))
                    budget.take('control_steps')
                    obs, reward, done, _ = env.step(command.tolist())
                    observed = env.evaluate_conditions(plan['pair']['targets'])
                    goal_consistency(target, observed, reward, done)
                    events.append(dict(predicates=observed, reward=float(reward), done=bool(done), command=command.tolist()))
                    if done:
                        break
                np.savez_compressed(RESULTS / ('query_' + str(branch) + '.npz'), token_ids=ids.cpu().numpy(),
                                    token_logits=sampled_logits[0].cpu().numpy(), sampled_logp=sampled_logp.cpu().numpy(),
                                    rescored_logp=logp.detach().cpu().numpy(), actions=original_actions)
                report['branches'].append(dict(prompt=prompt, target=target, state_sha256=hashlib.sha256(state.tobytes()).hexdigest(),
                    rgb_sha256=hashlib.sha256(rgb.tobytes()).hexdigest(), controller_fields_sha256=ctrl_sha,
                    logprob_max_abs_error=error, sampler_rounding_error=rounding_error,
                    executed_actions=len(events), events=events))
            finally:
                if env is not None:
                    env.close()
    finally:
        MujocoEnv._reset_internal = original_reset
        for name, fn in original_steps.items():
            setattr(mujoco, name, fn)
    report['peak_cuda_bytes'] = torch.cuda.max_memory_allocated()
    report['status'] = 'P0_IO_VERIFIED'
    report['boundary'] = 'No optimizer update, task competence, retention effect or complete controller-state restoration claim. True-target events may remain unobserved; inspect branch events.'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=['install-sources', 'configure', 'prepare', 'p0'])
    args = p.parse_args()
    require_container()
    plan = read_plan()
    validate_plan(plan)
    if args.phase == 'install-sources':
        install_sources(plan)
        return 0
    if args.phase == 'configure':
        configure()
        return 0
    if args.phase == 'prepare':
        prepare(plan)
        return 0
    budget = Budget(plan['limits'])
    report = dict(status='RUNNING', started_utc=datetime.now(timezone.utc).isoformat(),
                  packet_sha256=plan['packet_sha256'], optimizer_updates=0)
    started = time.monotonic()
    def timeout_handler(*_):
        raise RuntimeError('P0 wall-time limit reached')
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(7100)
    try:
        native(plan, report, budget)
        return 0
    except Exception as exc:
        report['status'] = 'P0_FAILED'
        report['error'] = repr(exc)
        raise
    finally:
        signal.alarm(0)
        report['counts'] = budget.counts
        report['elapsed_seconds'] = time.monotonic() - started
        (RESULTS / 'p0_result.json').write_text(json.dumps(report, indent=2))


if __name__ == '__main__':
    raise SystemExit(main())
