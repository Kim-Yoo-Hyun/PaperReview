# Maximum a Posteriori Policy Optimisation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=S1ANxQW0b.
> PDF retrieval source: https://openreview.net/forum?id=S1ANxQW0b. Reading tracker status/evidence was not changed.

- Year/Venue: 2018 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning
- Official paper: https://openreview.net/forum?id=S1ANxQW0b
- Full-text retrieval: https://openreview.net/forum?id=S1ANxQW0b
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.를 문제로 두고, In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 1 / ABSTRACT - extractive body cue:** We show that several existing methods can directly be related to our derivation.
- **p. 1 / ABSTRACT - extractive body cue:** We develop two off-policy algorithms and demonstrate that they are competitive with the state-of-the-art in deep reinforcement learning.
- **p. 1 / ABSTRACT - extractive body cue:** In particular, for continuous control, our method outperforms existing methods with respect to sample efficiency, premature convergence and robustness to hyperparameter settings.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Model free reinforcement learning algorithms can acquire sophisticated behaviours by interacting with the environment while receiving simple rewards.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two types of algorithms currently dominate scalable learning for continuous control problems: First, Trust-Region Policy Optimisation (TRPO; Schulman et al.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show below that several algorithms, including TRPO, can be directly related to this perspective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We leverage the fast convergence properties of EM-style coordinate ascent by alternating a nonparametric data-based E-step which re-weights state-action samples, with a supervised, parametric M-step ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen. | state 또는 observation, action, reward와 transition history | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| State/latent | subsequently, updates, policy, better, actions, state, will, have, probabilities, chosen, develop, off-policy | policy/value state와 action-selection variable | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Output/action | We develop two off-policy algorithms and demonstrate that they are competitive with the state-of-the-art in deep reinforcement learning. | action policy와 induced trajectory | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Objective/outcome | In contrast to typical off-policy value-gradient algorithms, the new algorithm does not require gradient of the Q-function to update the policy. | expected return, task success, stability와 sample efficiency | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relativeentropy objective.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show below that several algorithms, including TRPO, can be directly related to this perspective.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we thus ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** For the Humanoid running domain we can observe a similar trend to the experiments from the previous section: MPO quickly finds a stable running policy, ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Furthermore, we can observe that changing from the non-parametric variational distribution to a parametric distribution3 (which, as described above, can be related to PPO) results ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** While we include plots depicting the performance of our algorithm on all tasks below; comparing it against the state-of-the-art algorithms in terms of data-efficiency.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We plot the median performance over 10 experiments with different random seeds.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Embodiment/environment | For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Dataset/benchmark | Published as a conference paper at ICLR 2018 5.1.1 DETAILED ANALYSIS ON WALKER-2D, ACROBOT, HOPPER We start by looking at the results for the classical Acrobot task (two degrees of freedom, one ... | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Metric | The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. | definition, denominator, direction and uncertainty | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We plot the median performance over 10 experiments ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.를 문제로 두고, In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
