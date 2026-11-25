# Maximum a Posteriori Policy Optimisation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1806.06920.
> PDF retrieval source: https://openreview.net/forum?id=S1ANxQW0b. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / ICLR
- Authors: Abbas Abdolmaleki, Jost Tobias Springenberg, Yuval Tassa, Remi Munos, Nicolas Heess, Martin Riedmiller
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning
- Official paper: https://arxiv.org/abs/1806.06920
- Full-text retrieval: https://openreview.net/forum?id=S1ANxQW0b
- Code/Project: https://github.com/google-deepmind/acme
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

MPO는 연속 제어에서 오프폴리시 경험으로 정책을 개선하는 문제를 최대 사후확률 최적화로 다룬다.

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

- 정책 개선과 파라미터 갱신을 교대로 수행한다.
- 확률적 최적화 절차를 연속 제어 과제에서 평가한다.

[저자 원문](https://arxiv.org/abs/1806.06920)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Embodiment/environment | For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Dataset/benchmark | The single learner vanilla DDPG implementation learns the lower dimensional environments quickly but suffers in terms of learning speed in environments with sparse rewards (finger, acrobot) and higher dimensional action spaces. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Metric | The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. | definition, denominator, direction and uncertainty | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We plot the median performance over 10 experiments ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 training_steps 1e7 0 200 400 600 800 1000 mean_return task_name=run, domain_name=humanoid agent=DDPG agent=EPG + retrace + entropy ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks. (p. 1, 1 INTRODUCTION).
- **Actual contribution:** In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. (p. 1, 1 INTRODUCTION).
- **Evaluation boundary:** Figure 2: Ablation study of the MPO algorithm and comparison to common baselines from the liter- ature on three domains from the control suite. We plot the median performance over ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: where standard PPO requires approximately 1M trajectories to find a good policy ... (p. 9, 5 EXPERIMENTS).

## 원문과 공개 자료

- 코드 · DeepMind Acme가 제공하는 MPO 학습기. 2018년 실험 실행본과의 동일성은 미확인 · acme/agents/tf/mpo/learning.py [배포 파일](https://raw.githubusercontent.com/google-deepmind/acme/1bc05bea97b94a2da7e5315b315118bdaa98f1f3/acme/agents/tf/mpo/learning.py)
- 데이터 · 원문은 DeepMind Control Suite 실험에 사용한 자료를 보고한다. 이 연구의 해당 자료 배포 파일은 미확인이다. [검토 근거](https://arxiv.org/pdf/1806.06920)
