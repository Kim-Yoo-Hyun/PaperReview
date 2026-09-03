# Learning Robust Rewards with Adversarial Inverse Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1710.11248.
> PDF retrieval source: https://arxiv.org/pdf/1710.11248. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, inverse reinforcement learning, adversarial learning, reward learning
- Official paper: https://arxiv.org/abs/1710.11248
- Full-text retrieval: https://arxiv.org/pdf/1710.11248
- Code/Project: https://github.com/justinjfu/inverse_rl
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation and recover a generalizable and portable reward ...를 문제로 두고, In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Reinforcement learning provides a powerful and general framework for decision making and control, but its application in practice is often hindered by the need for ...
- **p. 1 / ABSTRACT - extractive body cue:** Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features, but still require a manually specified reward function.
- **p. 1 / ABSTRACT - extractive body cue:** Inverse reinforcement learning holds the promise of automatic reward acquisition, but has proven exceptionally difficult to apply to large, high-dimensional problems with unknown dynamics.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose AIRL, a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation.
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate that AIRL is able to recover reward functions that are robust to changes in dynamics, enabling us to learn policies even under significant ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, adversarial IRL methods (Finn et al., 2016b;a) hold promise for tackling difficult tasks due to the ability to adapt training samples to improve learning ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** When compared to GAIL (Ho & Ermon, 2016), which does not attempt to directly recover rewards, our method achieves comparable results on tasks that do ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** In order to decouple the reward function from the advantage, we propose to modify the discriminator of Sec.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** There are many scenarios where IRL may be preferred over direct imitation learning, such as re-optimizing a reward in novel environments (Finn et al., 2017) ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** If the ground truth reward is also only a function of state, this allows us to recover the true reward up to a constant.
- **p. 3 / 3 BACKGROUND - extractive body cue:** The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** Suppose IRL recovers a state-only reward r′(s) such that it produces an optimal policy in T: Q∗ r′,T (s, a) = Q∗ r,T (s, a) ...
- **p. 3 / 3 BACKGROUND - extractive body cue:** The dynamics or transition distribution T (s′/a, s), the initial state distribution ρ0(s), and the reward function r(s, a) are unknown in the standard reinforcement ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: π∗= arg maxπ Eτ∼π " T X ... | observation history와 expert trajectory/action | p. 3 (3 BACKGROUND), p. 3 (3 BACKGROUND) |
| State/latent | goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized, discounted, reward | behavior policy와 temporal action context | p. 3 (3 BACKGROUND), p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND) |
| Output/action | 4 ADVERSARIAL INVERSE REINFORCEMENT LEARNING (AIRL) In practice, using full trajectories as proposed by GAN-GCL can result in high variance estimates as compared to using single state, action pairs, and our experimental ... | predicted action 또는 action chunk | p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND) |
| Objective/outcome | The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: π∗= arg maxπ Eτ∼π " T X ... | imitation error, task success, robustness와 compounding error | p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** When compared to GAIL (Ho & Ermon, 2016), which does not attempt to directly recover rewards, our method achieves comparable results on tasks that do ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** In order to decouple the reward function from the advantage, we propose to modify the discriminator of Sec.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** There are many scenarios where IRL may be preferred over direct imitation learning, such as re-optimizing a reward in novel environments (Finn et al., 2017) ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** If the ground truth reward is also only a function of state, this allows us to recover the true reward up to a constant.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only reward achieves optimal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. In our second task, we modify the agent itself. We train a quadrupedal "ant" agent to run forwards, and at test time we ...
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning setups, and outperforms ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption) |
| Embodiment/environment | (2016a), which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer. | hardware/simulator version and reset protocol | p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS) |
| Dataset/benchmark | In this way, we simulate a scenario where we wish to use RL to solve a task but wish to refrain from manual reward engineering and instead seek to learn a reward ... | role, split, size and leakage | p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS), p. 6 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS) |
| Metric | Table 1: Results on transfer learning tasks. Mean scores (higher is better) are reported over 5 runs. We also include results for TRPO optimizing the ground truth reward, and the performance of ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (7 EXPERIMENTS), p. 6 (7 EXPERIMENTS) |
| Baseline/ablation | We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning setups, and outperforms GAN-GCL in both settings. | fair input/data/compute/action matching | p. 6 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3 BACKGROUND - extractive body cue:** 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer that the goal in the maze is ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** However, we leave this direction to future work.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** (2016a) does not implement or evaluate GAN-GCL and, to our knowledge, we present the first empirical evaluation of this algorithm.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** We subtract a constant offset from all reward functions so that they share the same mean for visualization - this does not influence the optimal ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** GAIL learns successfully in the training domain, but does not acquire a representation that is suitable for transfer to test domains.

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation and recover a generalizable and portable reward ...를 문제로 두고, In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 BACKGROUND) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
