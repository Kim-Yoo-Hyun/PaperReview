#!/usr/bin/env python3
"""Docker-only, bounded ALLOC P0. No optimizer, training loop or P1/P2 entry point."""
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

ROOT = Path('/opt/allocation')
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
    key = f'allocation-n2|{stage}|{master_seed}|{task}|{init_index}|{query}|{purpose}'
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
    require(file_hash(CACHE / 'model/dataset_statistics.json') == plan['checkpoint']['normalizer_sha256'], 'Normalizer changed')
    states = []
    for f in plan['init_files']:
        path = ROOT / 'libero' / f['path']
        verify_file(path, f['size'], f['sha'], 'sha1', git_blob=True)
        rows = torch.load(path, map_location='cpu', weights_only=False)
        require(len(rows) == 50, 'Expected 50 state rows; revise split before any outcomes')
        hashes = []
        for row in rows:
            a = np.asarray(row)
            require(a.ndim == 1 and a.dtype.kind == 'f' and bool(np.isfinite(a).all()), 'Malformed state')
            a = np.ascontiguousarray(a.astype(a.dtype.newbyteorder('<'), copy=False))
            header = json.dumps({'dtype': a.dtype.str, 'shape': list(a.shape)}, sort_keys=True).encode()
            hashes.append(hashlib.sha256(header + b'\0' + a.tobytes()).hexdigest())
        splits = [set(hashes[:30]), set(hashes[30:40]), set(hashes[40:])]
        require(not any(splits[i] & splits[j] for i in range(3) for j in range(i+1, 3)), 'Cross-split duplicate state; no automatic repair')
        states.append({'path': f['path'], 'sha256': file_hash(path), 'row_sha256': hashes,
                       'split': {'train': list(range(30)), 'dev': list(range(30,40)), 'eval': list(range(40,50))}})
    for case in plan['cases']:
        require(file_hash(ROOT / 'libero' / case['bddl_path']) == case['bddl_sha256'], 'BDDL changed')
    assets = ROOT / 'libero/libero/libero/assets'
    asset_hashes = {}
    for path in sorted(assets.rglob('*')):
        if path.is_file():
            with path.open('rb') as f:
                require(not f.read(100).startswith(b'version https://git-lfs.github.com/spec'), 'Unresolved LFS asset')
            asset_hashes[str(path.relative_to(assets))] = file_hash(path)
    require(asset_hashes, 'LIBERO assets absent')
    return {'checkpoint_files': files, 'states': states, 'assets': asset_hashes,
            'pretraining_or_sft_holdout_verified': False, 'near_duplicate_physical_state_review': 'not performed'}


def module_paths():
    import prismatic
    import transformers
    import rlinf
    from libero.libero import envs
    paths = {}
    for name, module in {'oft': prismatic, 'transformers': transformers, 'rlinf': rlinf, 'libero': envs}.items():
        path = Path(module.__file__).resolve()
        require(path.is_relative_to(ROOT / name), 'Import shadowing: ' + str(path))
        paths[name] = str(path)
    return paths


def gpu_info():
    import torch
    require(torch.cuda.is_available() and torch.cuda.device_count() == 1, 'One CUDA GPU required')
    require(torch.cuda.is_bf16_supported(), 'BF16 unavailable; no dtype fallback')
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
    record = {'packet_sha': os.environ['ALLOC_PACKET_SHA'], 'sources': identity,
              'runtime': runtime, 'payload': payload, 'native_p0_passed': False}
    write_json(CACHE / 'prepared.json', record)
    write_json(RESULTS / 'prepared.json', record)


def p0(plan, report):
    import numpy as np
    import torch
    from omegaconf import OmegaConf
    from allocation import Allocation, attach_steps, tensor_check, weighted_loss
    from rlinf.data.schema.embodied_types import Trajectory, TrajectoryStep
    from rlinf.utils.nested_dict_process import process_nested_dict_for_adv, process_nested_dict_for_train
    require(os.environ.get('HF_HUB_OFFLINE') == '1', 'P0 must be offline')
    sources(plan)
    configure_libero()
    report['gpu'] = gpu_info()
    report['module_paths'] = module_paths()
    ready = json.loads((CACHE / 'prepared.json').read_text())
    require(ready['packet_sha'] == os.environ['ALLOC_PACKET_SHA'], 'Stale payload manifest')
    require(payload_manifest(plan) == ready['payload'], 'Prepared payload changed')
    c = plan['contract']
    budget = Budget(c['limits'], c['p0_timeout_seconds'])
    report['counts'] = budget.counts
    report['tensor_fixture'] = tensor_check(budget)
    report['native_scope'] = 'Two tasks,8 sampled one-chunk fragments per task; synthetic return gradient on replicate0 only. Full worker channels/training/allocator effect untested.'
    random.seed(c['seed']); np.random.seed(c['seed']); torch.manual_seed(c['seed']); torch.cuda.manual_seed_all(c['seed'])
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    from rlinf.models.embodiment.openvla_oft.rlinf import get_model
    model = get_model(OmegaConf.create(c['model_config']), torch_dtype=torch.bfloat16).cuda().eval()
    require(model.unnorm_key == c['model_config']['unnorm_key'], 'Actual normalizer key mismatch')
    stats = json.loads((CACHE / 'model/dataset_statistics.json').read_text())[model.unnorm_key]
    require(model.norm_stats[model.unnorm_key] == stats, 'Loaded normalizer differs')
    require(model.language_model.config._attn_implementation == 'sdpa', 'Bidirectional SDPA required')
    require(all(type(x.self_attn).__name__ == 'LlamaSdpaAttention' for x in model.language_model.model.layers), 'Wrong attention implementation')
    def check_logits(module, args, output):
        require(output.logits.dtype == torch.float32, 'Logits not FP32; no silent sampler change')
    model.language_model.register_forward_hook(check_logits)
    params = [(name, p) for name, p in model.named_parameters() if p.requires_grad]
    require(params, 'No trainable parameters')
    report['trainable_elements'] = sum(p.numel() for _, p in params)
    versions = {name: p._version for name, p in model.named_parameters()}
    import mujoco
    from robosuite.environments.base import MujocoEnv
    reset_orig, control_orig, physics_orig = MujocoEnv._reset_internal, MujocoEnv.step, mujoco.mj_step
    def reset_guard(self, *a, **kw):
        budget.take('reset'); return reset_orig(self, *a, **kw)
    def control_guard(self, *a, **kw):
        budget.take('control'); return control_orig(self, *a, **kw)
    def physics_guard(*a, **kw):
        budget.take('physics', int(kw.get('nstep', a[2] if len(a) > 2 else 1)))
        return physics_orig(*a, **kw)
    MujocoEnv._reset_internal, MujocoEnv.step, mujoco.mj_step = reset_guard, control_guard, physics_guard
    env = None
    records, saved, allocations, lens = [], [], [], []
    report['io'] = records
    try:
        from libero.libero import benchmark
        from libero.libero.envs import OffScreenRenderEnv
        suite = benchmark.get_benchmark_dict()['libero_goal'](task_order_index=0)
        for group_id, case in enumerate(plan['cases']):
            task = suite.get_task(case['task_id'])
            require(Path(task.bddl_file).stem == case['stem'], 'Task order mismatch')
            init_meta = next(f for f in plan['init_files'] if Path(f['path']).stem == case['stem'])
            rows = torch.load(ROOT / 'libero' / init_meta['path'], map_location='cpu', weights_only=False)
            env = OffScreenRenderEnv(bddl_file_name=str(ROOT / 'libero' / case['bddl_path']), camera_heights=256, camera_widths=256, control_freq=c['control_hz'])
            def reset_observation():
                env.seed(seed_key('P0', c['seed'], case['task_id'], case['init_row'], 0, 'reset'))
                env.env.reset()  # Bypass unbounded wrapper retry; failure stops probe.
                obs = env.set_init_state(rows[case['init_row']])
                for _ in range(c['settling_steps']):
                    obs, reward, done, info = env.step([0.,0.,0.,0.,0.,0.,-1.])
                    require(not done, 'Task ended in settling')
                require(not env.check_success(), 'Initially successful state')
                image = np.ascontiguousarray(obs['agentview_image'][::-1, ::-1])
                require(image.shape == (256,256,3) and image.dtype == np.uint8, 'Unexpected RGB')
                return image
            frame = reset_observation()
            require(float(env.env.control_freq) == c['control_hz'], 'Control rate mismatch')
            frame_hash = hashlib.sha256(frame.tobytes()).hexdigest()
            qseed = seed_key('P0', c['seed'], case['task_id'], case['init_row'], 0, 'query')
            torch.manual_seed(qseed); torch.cuda.manual_seed_all(qseed)
            budget.take('query'); budget.take('query_slots', 8)
            with torch.no_grad():
                acts, result = model.predict_action_batch(env_obs={'main_images':torch.from_numpy(frame.copy()).unsqueeze(0).repeat(8,1,1,1),
                    'states':torch.zeros(8,8),'task_descriptions':[task.language]*8}, do_sample=True,
                    temperature=c['temperature'],top_k=c['top_k'],calculate_logprobs=True,calculate_values=False)
            require(tuple(acts.shape)==(8,8,7) and bool(torch.isfinite(acts).all()), 'Invalid action batch')
            action_array = acts.cpu().numpy()
            saved.append({k:v.detach().cpu().clone() for k,v in result['forward_inputs'].items()})
            old = result['prev_logprobs'].detach().cpu().reshape(8,8,7)
            require(old.dtype == torch.float32 and bool(torch.isfinite(old).all()), 'Invalid stored logprobs')
            group_lengths, group_actions = [], []
            for rep in range(8):
                if rep:
                    repeat = reset_observation()
                    require(hashlib.sha256(repeat.tobytes()).hexdigest()==frame_hash, 'Reset observation differs; group not matched')
                executed = []
                for action in action_array[rep]:
                    converted=action.copy();converted[-1]=-np.sign(2.*converted[-1]-1.)
                    budget.take('executed_actions')
                    obs,reward,done,info=env.step(converted.tolist())
                    executed.append(converted.tolist())
                    if done:break
                group_lengths.append(len(executed));group_actions.append(executed)
                allocations.append(Allocation(0,group_id,case['task_id'],case['init_row'],rep,0,0,
                                  c['fixture_q'][case['task_id']],.1))
            records.append({'task_id':case['task_id'],'row':case['init_row'],'goal':task.language,'frame_sha256':frame_hash,
                            'fragment_lengths':group_lengths,'actions_model':action_array.tolist(),'actions_environment':group_actions,
                            'tokens':saved[-1]['action_tokens'].tolist(),'old_logprobs':old.tolist(),'synthetic_q':c['fixture_q'][case['task_id']]})
            lens.extend(group_lengths)
            records[-1]['old_tensor_index']=group_id
            # Save tensor only within this process; JSON above is sufficient provenance.
            saved[-1]['_old']=old
            del result, acts
            env.close();env=None
        # Exercise actual Trajectory batching/reshape with the collected fragments.
        inputs={key:torch.cat([d[key] for d in saved],dim=0) for key in saved[0] if key!='_old'}
        old_all=torch.cat([d['_old'] for d in saved],dim=0)
        synthetic_returns=torch.tensor([5.,0.,0.,0.,0.,0.,0.,0.]*2)
        from rlinf.algorithms.advantages import compute_grpo_advantages
        advantage,_=compute_grpo_advantages(synthetic_returns.reshape(2,8),torch.ones(1,16),8)
        step=TrajectoryStep(prev_logprobs=old_all,forward_inputs=inputs,rewards=torch.zeros(16,8),
                            dones=torch.zeros(16,8,dtype=torch.bool),initial_dones=torch.zeros(16,8,dtype=torch.bool))
        trajectory=attach_steps([step],[allocations],max_episode_length=8)
        batch=process_nested_dict_for_adv(Trajectory.to_batch([trajectory]),1)
        batch=process_nested_dict_for_train(batch,torch.arange(16))
        require(batch['allocation_ids'].tolist()==[r.ids() for r in allocations], 'Native metadata alignment failed')
        report['gradient_fixture']=[]
        for index in [0,8]:
            inp={key:value[index:index+1].cuda().clone() for key,value in batch['forward_inputs'].items()}
            prior=batch['prev_logprobs'][index:index+1].cuda()
            def score():
                budget.take('rescore')
                out=model.default_forward(forward_inputs={k:v.clone() for k,v in inp.items()},compute_logprobs=True,
                    compute_entropy=False,compute_values=False,use_cache=False,temperature=c['temperature'],top_k=c['top_k'])
                lp=out['logprobs'].reshape(1,8,7)
                require(lp.dtype==torch.float32 and bool(torch.isfinite(lp).all()),'Invalid rescored likelihood')
                return lp
            with torch.no_grad(): same=score()
            error=float((same-prior).abs().max())
            require(error<=c['same_goal_logprob_atol'],'Saved/rescored likelihood mismatch; no tolerance retuning')
            model.zero_grad(set_to_none=True)
            lp=score();length=lens[index]
            mask=(torch.arange(8,device='cuda')<length).reshape(1,8,1)
            valid_length=torch.full((1,8,1),float(length),device='cuda')
            adv=advantage[0,index].expand(1,8,1).cuda().float()
            q,p=batch['allocation_probs'][index].tolist()
            weight=torch.tensor([p/q],device='cuda').reshape(1,1,1)
            loss=weighted_loss(lp,prior,adv,mask,valid_length,8,weight)
            budget.take('backward');loss.backward()
            norm2,nonzero=0.,0
            for _,parameter in params:
                if parameter.grad is not None:
                    require(bool(torch.isfinite(parameter.grad).all()),'Nonfinite gradient')
                    norm=float(torch.linalg.vector_norm(parameter.grad.detach().float()).item());norm2+=norm*norm;nonzero+=int(norm>0)
            require(nonzero>0,'Zero gradient fixture')
            report['gradient_fixture'].append({'task':allocations[index].task,'replicate':0,'synthetic_advantage':float(adv[0,0,0]),
                'p_over_q':p/q,'loss':float(loss.detach()),'gradient_l2':norm2**.5,'rescore_max_abs_error':error})
            del loss,lp,same,inp
        require(budget.counts['physics']>0 and budget.counts['control']>=budget.counts['executed_actions'],'Cost hooks missed native steps')
        require(versions=={name:p._version for name,p in model.named_parameters()},'Policy parameters changed')
        report['status']='P0_PARTIAL_PATH_WIRING_PASS_ONLY'
        report['peak_cuda_allocated_bytes']=torch.cuda.max_memory_allocated()
        report['full_envworker_collector_integration']=False
    finally:
        MujocoEnv._reset_internal,MujocoEnv.step,mujoco.mj_step=reset_orig,control_orig,physics_orig
        if env is not None:env.close()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase',choices=['source-build','prepare','p0'])
    args=parser.parse_args();container_only()
    plan=json.loads((PACKET/'plan.json').read_text())
    if args.phase=='source-build':
        write_json(PACKET/'build_sources.json',{'sources':sources(plan,fetch=True),'packages':package_versions()});return
    require(os.environ.get('ALLOC_PACKET_SHA')==os.environ.get('ALLOC_IMAGE_SHA') and os.environ.get('ALLOC_PACKET_SHA'),'Stale image/packet')
    report={'phase':args.phase,'started_utc':datetime.now(timezone.utc).isoformat(),'status':'INCOMPLETE','research_effect_measured':False,'optimizer_steps':0}
    start=time.monotonic()
    try:
        if args.phase=='prepare':
            prepare(plan);report['status']='PAYLOAD_VERIFIED_NATIVE_P0_PENDING'
        else:p0(plan,report)
    except BaseException as exc:
        report.update(error=str(exc),traceback=traceback.format_exc(),status='FAILED_NO_RESEARCH_CONCLUSION');raise
    finally:
        report['elapsed_seconds']=time.monotonic()-start;write_json(RESULTS/'result.json',report)


if __name__=='__main__':main()
