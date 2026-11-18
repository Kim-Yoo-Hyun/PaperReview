"""Container-only OpenPI endpoint actor and bounded JSON-lines worker.

The mean uses the complete Euler chain, not a last-step surrogate. The worker
never receives object/contact labels. No optimizer or rollout trainer exists here.
"""
import json
import os
from pathlib import Path
import sys
import time

import numpy as np
import torch

ARM = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
FLIP = np.array([1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1])


def covariance(jacobian, coupling, cfg):
    j = jacobian.float()
    eye = torch.eye(12, device=j.device)
    inverse = torch.linalg.solve(eye + coupling * (j.T @ j), eye)
    c = (1 - cfg['eta']) * 12 * inverse / torch.trace(inverse) + cfg['eta'] * eye
    sigma = torch.eye(14, device=j.device) * cfg['sigma_gripper']**2
    ix = torch.tensor(ARM, device=j.device)
    sigma[ix[:, None], ix[None, :]] = cfg['sigma_arm']**2 * c
    return (sigma + sigma.T) / 2


class EndpointActor:
    def __init__(self, plan):
        from openpi.models.pi0_config import Pi0Config
        from openpi.models_pytorch.pi0_pytorch import PI0Pytorch
        from openpi.models.tokenizer import PaligemmaTokenizer
        from openpi.shared import normalize
        from safetensors.torch import load_model

        self.plan = plan
        torch.manual_seed(0)
        self.model = PI0Pytorch(Pi0Config(pi05=True, action_horizon=32, pytorch_compile_mode=None))
        # Do not ignore checkpoint keys, replace tensors, or relax strictness.
        missing, unexpected = load_model(self.model, '/cache/model/model.safetensors', strict=True)
        if missing or unexpected:
            raise ValueError({'missing': list(missing), 'unexpected': list(unexpected)})
        self.model.paligemma_with_expert.to_bfloat16_for_selected_params('bfloat16')
        self.model.to('cuda').eval()
        allowed = ('paligemma_with_expert.gemma_expert.', 'action_in_proj.', 'action_out_proj.', 'time_mlp_in.', 'time_mlp_out.')
        for name, p in self.model.named_parameters():
            p.requires_grad_(name.startswith(allowed))
        width = self.model.action_out_proj.in_features
        self.head = torch.nn.Linear(width + 12, 1).cuda().float()
        self.stats = normalize.load(Path('/cache/model') / Path(plan['model']['normalizer_path']).parent)
        for key in ('state', 'actions'):
            for attr in ('q01', 'q99'):
                x = np.asarray(getattr(self.stats[key], attr))
                if x.shape != (14,) or not np.isfinite(x).all():
                    raise ValueError('Normalizer shape or finite check failed')
            if np.any(self.stats[key].q99 < self.stats[key].q01):
                raise ValueError('Invalid quantile range')
        self.tokenizer = PaligemmaTokenizer(200)
        self.last = None
        self.queries = self.forwards = self.backwards = 0

    def inputs(self, packet):
        from openpi import transforms as tr
        from openpi.policies.aloha_policy import AlohaInputs
        from openpi.models.model import Observation

        images = {k: packet[k].transpose(2, 0, 1) for k in ('cam_high', 'cam_left_wrist', 'cam_right_wrist')}
        if any(x.dtype != np.uint8 or x.ndim != 3 or x.shape[0] != 3 for x in images.values()):
            raise ValueError('Three uint8 RGB cameras required')
        if packet['state'].shape != (14,) or packet['q'].shape != (12,):
            raise ValueError('State14/actual-arm12 contract violated')
        prompt = str(packet['prompt'].item())
        if not prompt.strip():
            raise ValueError('Empty prompt')
        d = AlohaInputs(adapt_to_pi=True)({'images': images, 'state': packet['state'].copy(), 'prompt': prompt})
        d = tr.Normalize(self.stats, use_quantiles=True)(d)
        restored_state_input = d['state'].copy()
        d = tr.ResizeImages(224, 224)(d)
        # Record truncation explicitly, using the pinned tokenizer's exact formatting.
        bins = np.digitize(d['state'], bins=np.linspace(-1, 1, 257)[:-1]) - 1
        clean = prompt.strip().replace('_', ' ').replace('\n', ' ')
        text = f"Task: {clean}, State: {' '.join(map(str, bins))};\nAction: "
        token_count = len(self.tokenizer._tokenizer.encode(text, add_bos=True))
        if token_count > 200:
            raise ValueError(f'Prompt truncated: {token_count}>200')
        d = tr.TokenizePrompt(self.tokenizer, discrete_state_input=True)(d)
        d = tr.PadStatesAndActions(32)(d)
        def tensor(x):
            if isinstance(x, dict):
                return {k: tensor(v) for k, v in x.items()}
            return torch.from_numpy(np.array(x)).to('cuda')[None]
        obs = Observation.from_dict(tensor(d))
        return obs, d['state'].copy(), token_count, restored_state_input

    def ode(self, observation, noise):
        from openpi.models_pytorch.pi0_pytorch import make_att_2d_masks
        self.forwards += 1
        if self.forwards > 7:
            raise RuntimeError('ODE forward budget exceeded')
        m = self.model
        images, masks, tokens, token_masks, state = m._preprocess_observation(observation, train=False)
        # Prefix backbone is frozen; expert gradients through every Euler step remain live.
        with torch.no_grad():
            prefix, pads, att = m.embed_prefix(images, masks, tokens, token_masks)
            pos = torch.cumsum(pads, dim=1) - 1
            attention = m._prepare_attention_masks_4d(make_att_2d_masks(pads, att))
            m.paligemma_with_expert.paligemma.language_model.config._attn_implementation = 'eager'
            _, cache = m.paligemma_with_expert.forward(attention_mask=attention, position_ids=pos,
                past_key_values=None, inputs_embeds=[prefix, None], use_cache=True)
        captured = []
        def feature_hook(module, inputs):
            captured[:] = [inputs[0][:, 0, :]]
        hook = m.action_out_proj.register_forward_pre_hook(feature_hook)
        try:
            x = noise
            dt = torch.tensor(-0.1, dtype=torch.float32, device='cuda')
            t = torch.tensor(1.0, dtype=torch.float32, device='cuda')
            for _ in range(10):
                x = x + dt * m.denoise_step(state, pads, cache, x, t.expand(x.shape[0]))
                t = t + dt
            if x.shape != (1, 32, 32) or len(captured) != 1:
                raise ValueError('ODE/action feature contract violated')
            return x[0, 0, :14].float(), captured[0].float()
        finally:
            hook.remove()

    def distribution(self, obs, noise, q, j):
        mu, feature = self.ode(obs, noise)
        lam = self.plan['actor']['lambda_max'] * torch.sigmoid(self.head(torch.cat((feature, q[None]), dim=-1))).squeeze()
        sigma = covariance(j, lam, self.plan['actor'])
        chol = torch.linalg.cholesky(sigma)
        if not torch.isfinite(mu).all() or not torch.isfinite(chol).all():
            raise ValueError('Nonfinite policy distribution')
        return torch.distributions.MultivariateNormal(mu, scale_tril=chol), lam, sigma

    def query(self, directory):
        from openpi import transforms as tr
        from openpi.policies.aloha_policy import AlohaOutputs
        self.queries += 1
        if self.queries > 3:
            raise RuntimeError('Query budget exceeded')
        with np.load(directory / 'observation.npz', allow_pickle=False) as z:
            packet = {k: z[k] for k in z.files}
        obs, state, ntok, state14 = self.inputs(packet)
        q = torch.tensor(packet['q'], device='cuda', dtype=torch.float32)
        d = FLIP[ARM] * (self.stats['actions'].q99[ARM] - self.stats['actions'].q01[ARM] + 1e-6) / 2
        j = torch.tensor(np.diag([10]*3+[1]*3) @ packet['jacobian'] @ np.diag(d), device='cuda', dtype=torch.float32)
        xi = torch.randn(1, 32, 32, device='cuda').detach()
        started = time.monotonic()
        with torch.no_grad():
            dist, lam, sigma = self.distribution(obs, xi, q, j)
            raw = dist.sample().detach()
            old = dist.log_prob(raw)
            replay, _, _ = self.distribution(obs, xi, q, j)
            score = replay.log_prob(raw)
        error = abs(float(score - old))
        if not np.isfinite(error) or error > self.plan['budget']['same_weights_density_abs_tolerance']:
            raise ValueError(f'Same-weights raw logp replay mismatch: {error}')
        # Exact pinned transform order; never evaluate density at this transformed command.
        data = tr.Unnormalize(self.stats, use_quantiles=True)({'state': state, 'actions': raw.cpu().numpy()[None]})
        data = tr.AbsoluteActions(tr.make_bool_mask(6, -1, 6, -1))(data)
        command = AlohaOutputs(adapt_to_pi=True)(data)['actions'][0]
        self.last = (obs, xi, raw, q, j)
        np.savez_compressed(directory / 'actor.npz', xi=xi.cpu().numpy(), raw_u=raw.cpu().numpy(),
            mu=dist.mean.cpu().numpy(), sigma=sigma.cpu().numpy(), coupling=lam.cpu().numpy(),
            logp_old=old.cpu().numpy(), logp_replay=score.cpu().numpy(), command=command,
            normalized_state14=state14, token_ids=obs.tokenized_prompt.cpu().numpy())
        return {'status': 'IO_RESCORE_PASS', 'command': command.tolist(), 'coupling': float(lam),
                'logp_error': error, 'tokens': ntok, 'forward_count': self.forwards,
                'seconds': time.monotonic()-started, 'peak_vram_bytes': torch.cuda.max_memory_allocated()}

    def backward(self):
        if self.last is None or self.backwards:
            raise RuntimeError('Backward requires accepted IO and may run once')
        self.backwards += 1
        obs, xi, raw, q, j = self.last
        frozen = [(n, p, p._version) for n, p in self.model.named_parameters() if not p.requires_grad]
        self.model.zero_grad(set_to_none=True)
        self.head.zero_grad(set_to_none=True)
        dist, _, _ = self.distribution(obs, xi.detach(), q, j)
        (-dist.log_prob(raw.detach())).backward()
        grads = {}
        for name, p in list(self.model.named_parameters()) + [('relation_head.'+n, v) for n, v in self.head.named_parameters()]:
            if p.requires_grad:
                if p.grad is not None and not torch.isfinite(p.grad).all():
                    raise ValueError('Nonfinite gradient: ' + name)
                grads[name] = None if p.grad is None else float(p.grad.norm())
        if not any(v and v > 0 for k, v in grads.items() if 'gemma_expert.' in k):
            raise ValueError('No expert gradient')
        if not any(v and v > 0 for k, v in grads.items() if k.startswith('relation_head.')):
            raise ValueError('No relation-head gradient')
        if any(p.grad is not None or p._version != version for _, p, version in frozen):
            raise ValueError('Frozen backbone changed/received gradients')
        return {'status': 'GRADIENT_PASS', 'optimizer_steps': 0, 'grad_norms': grads,
                'frozen_parameter_versions_unchanged': True, 'forward_count': self.forwards,
                'peak_vram_bytes': torch.cuda.max_memory_allocated()}


def main():
    if os.environ.get('RELATION_IN_DOCKER') != '1' or not Path('/.dockerenv').exists():
        raise SystemExit('Docker-only worker')
    protocol = sys.stdout
    sys.stdout = sys.stderr
    def send(obj):
        protocol.write(json.dumps(obj, allow_nan=False) + '\n')
        protocol.flush()
    try:
        plan = json.loads(Path('/opt/relation/PLAN.json').read_text())
        actor = EndpointActor(plan)
        send({'status': 'LOADED', 'trainable': {n: list(p.shape) for n, p in actor.model.named_parameters() if p.requires_grad}})
        for line in sys.stdin:
            req = json.loads(line)
            if req['op'] == 'close':
                break
            if req['op'] == 'query':
                directory = Path(req['directory']).resolve()
                if not directory.is_relative_to('/results'):
                    raise ValueError('IPC files must stay in this run directory')
                send(actor.query(directory))
            elif req['op'] == 'backward':
                send(actor.backward())
            else:
                raise ValueError('Unknown operation')
    except Exception as e:
        import traceback
        traceback.print_exc()
        send({'status': 'FAILED', 'type': type(e).__name__, 'error': str(e)})
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
