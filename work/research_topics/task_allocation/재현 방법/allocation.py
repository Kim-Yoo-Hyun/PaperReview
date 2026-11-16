"""Allocation metadata and actor-only loss adapter. Torch imports are Docker-only."""
from dataclasses import dataclass
import math
import random


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def probabilities(successes, trials):
    require(len(successes) == len(trials) == 10, 'Exactly ten tasks required')
    require(all(isinstance(n, int) and isinstance(k, int) and 0 <= k <= n for k, n in zip(successes, trials)), 'Invalid counts')
    scores = [(1 + k) / (2 + n) for k, n in zip(successes, trials)]
    a = [s * (1 - s) for s in scores]
    return [.02 + .8 * v / sum(a) for v in a]


@dataclass(frozen=True)
class Allocation:
    epoch: int
    group: int
    task: int
    row: int
    replicate: int
    policy: int
    q_version: int
    q: float
    p: float

    def __post_init__(self):
        require(all(isinstance(v, int) and v >= 0 for v in self.ids()), 'Invalid integer identity')
        require(self.task < 10 and self.replicate < 8 and self.row < 50, 'Identity out of range')
        require(math.isfinite(self.q) and math.isfinite(self.p) and .02 - 1e-12 <= self.q <= 1 and self.p == .1, 'Invalid probability')

    def ids(self):
        return [self.epoch, self.group, self.task, self.row, self.replicate, self.policy, self.q_version]

    def weight(self):
        return self.p / self.q


def sample_groups(q, groups, seed, epoch=0, policy=0, q_version=0):
    require(len(q) == 10 and all(math.isfinite(v) and v >= .02 - 1e-12 for v in q) and abs(sum(q) - 1) < 1e-10, 'Invalid q vector')
    require(isinstance(groups, int) and groups > 0, 'Invalid group count')
    rng = random.Random(seed)
    result = []
    for g in range(groups):
        task = rng.choices(range(10), weights=q)[0]
        row = rng.randrange(30)
        result += [Allocation(epoch, g, task, row, k, policy, q_version, q[task], .1) for k in range(8)]
    return result


def validate_groups(rows):
    require(rows and len(rows) % 8 == 0, 'Complete groups of eight required')
    for start in range(0, len(rows), 8):
        group = rows[start:start + 8]
        a = group[0]
        key = lambda x: (x.epoch, x.group, x.task, x.row, x.policy, x.q_version, x.q, x.p)
        require(all(key(x) == key(a) for x in group), 'Group identity/probability mixed')
        require([x.replicate for x in group] == list(range(8)), 'Replicates reordered or missing')
    keys = [(rows[i].epoch, rows[i].group) for i in range(0, len(rows), 8)]
    require(len(set(keys)) == len(keys), 'Duplicate group identity')


def attach_steps(steps, rows_by_step, max_episode_length):
    """Extend actor-facing Trajectory, not an installed EnvWorker/collector patch."""
    import torch
    from dataclasses import dataclass
    from rlinf.data.schema.embodied_types import Trajectory
    require(len(steps) == len(rows_by_step) > 0, 'Step/metadata count mismatch')
    for rows in rows_by_step:
        validate_groups(rows)
    require(len({len(r) for r in rows_by_step}) == 1, 'Changing batch size')
    base = Trajectory.from_steps(steps, max_episode_length=max_episode_length)
    require(base.prev_logprobs is not None and base.prev_logprobs.shape[:2] == (len(steps), len(rows_by_step[0])), 'Actor/metadata shape mismatch')

    @dataclass
    class AllocationTrajectory(Trajectory):
        allocation_ids: object = None
        allocation_probs: object = None

    return AllocationTrajectory(**vars(base),
        allocation_ids=torch.tensor([[r.ids() for r in rows] for rows in rows_by_step], dtype=torch.int64),
        allocation_probs=torch.tensor([[[r.q, r.p] for r in rows] for rows in rows_by_step], dtype=torch.float64))


def weighted_loss(logprobs, old, advantages, mask, length, horizon, weight):
    import torch
    from rlinf.utils.utils import masked_mean_ratio
    require(logprobs.dtype == old.dtype == advantages.dtype == torch.float32, 'FP32 logprob/advantage required')
    require(logprobs.ndim == 3 and logprobs.shape == old.shape, 'Expected [B,C,d] logprobs')
    require(mask.dtype == torch.bool and mask.shape == length.shape == advantages.shape == logprobs.shape[:2] + (1,), 'Invalid actor mask/advantage/length shapes')
    require(weight.shape == (logprobs.shape[0], 1, 1) and not weight.requires_grad, 'Detached task weight required')
    require(bool(torch.isfinite(logprobs).all() and torch.isfinite(old).all() and torch.isfinite(advantages).all()), 'Nonfinite policy values')
    require(horizon > 0 and bool((length > 0).all() and (length <= horizon).all()), 'Invalid pre-filter length')
    require(bool(torch.isfinite(weight).all() and (weight > 0).all() and (weight <= 5.000001).all()), 'Invalid task weight')
    ratio = torch.where(mask, (torch.where(mask, logprobs - old, 0.)).exp(), 0.)
    element = torch.maximum(-advantages * ratio, -advantages * ratio.clamp(.8, 1.28))
    return masked_mean_ratio(element * weight, mask, length.float() / horizon)


def tensor_check(budget):
    """Native CPU tensors inside the pinned Docker image; one backward reservation."""
    import torch
    from rlinf.algorithms.losses import compute_ppo_actor_loss
    from rlinf.data.schema.embodied_types import Trajectory, TrajectoryStep
    from rlinf.utils.nested_dict_process import process_nested_dict_for_adv, process_nested_dict_for_train
    from rlinf.utils.utils import masked_mean_ratio
    values = torch.tensor([[[1.], [3.], [0.], [0.]], [[4.], [4.], [4.], [4.]]])
    mask = torch.tensor([[[1], [1], [0], [0]], [[1], [1], [1], [1]]], dtype=torch.bool)
    length = torch.tensor([2., 4.])[:, None, None].expand(2, 4, 1)
    require(masked_mean_ratio(values, mask, length / 4).item() == 3., 'Native length reduction differs')
    masked = mask.clone(); masked[0] = False
    require(masked_mean_ratio(values, masked, length / 4).item() == 2., 'Native filter denominator differs')
    lp = torch.zeros(2, 4, 1, dtype=torch.float32, requires_grad=True)
    adv = torch.ones_like(lp)
    native, _ = compute_ppo_actor_loss(lp, lp.detach(), .2, .28, adv, loss_mask=mask, loss_mask_sum=length, max_episode_steps=4)
    loss = weighted_loss(lp, lp.detach(), adv, mask, length, 4, torch.ones(2, 1, 1))
    require(torch.allclose(loss, native), 'Adapter w=1 differs from pinned native loss')
    weighted = weighted_loss(lp, lp.detach(), adv, mask, length, 4, torch.tensor([2/3, 2.])[:, None, None])
    budget.take('backward')
    gradient, = torch.autograd.grad(weighted, lp)
    expected = -mask.float() / length / 2 * torch.tensor([2/3, 2.])[:, None, None]
    require(torch.allclose(gradient, expected, atol=1e-7), 'Weight/length gradient differs')
    rows, steps = [], []
    for epoch in range(2):
        group = sample_groups([.1] * 10, 2, seed=epoch, epoch=epoch)
        for chunk in range(2):
            rows.append(group)
            steps.append(TrajectoryStep(prev_logprobs=torch.zeros(16, 8, 7), rewards=torch.zeros(16, 8),
                         dones=torch.zeros(16, 8, dtype=torch.bool),
                         initial_dones=torch.zeros(16, 8, dtype=torch.bool) if chunk == 0 else None))
    traj = attach_steps(steps, rows, max_episode_length=16)
    batch = Trajectory.to_batch([traj])
    batch = process_nested_dict_for_adv(batch, 2)
    require(batch['allocation_ids'].shape == (2, 32, 7), 'Epoch reshape lost metadata')
    expected_ids = traj.allocation_ids.reshape(2, 2, 16, 7).transpose(0, 1).reshape(2, 32, 7)
    require(torch.equal(batch['allocation_ids'], expected_ids), 'Epoch metadata mismatch')
    order = torch.arange(63, -1, -1)
    batch = process_nested_dict_for_train(batch, order)
    require(torch.equal(batch['allocation_ids'], expected_ids.reshape(64, 7)[order]), 'Shuffle metadata mismatch')
    require(torch.allclose(batch['allocation_probs'], torch.full((64, 2), .1, dtype=torch.float64)), 'Probabilities changed')
    return {'status': 'TENSOR_FIXTURE_PASS', 'checks': ['length_mean', 'filter_denominator', 'native_unit_weight', 'weighted_gradient', 'trajectory_epoch_shuffle'],
            'worker_channel_or_multirank_validated': False, 'research_effect_measured': False}
