# DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2301.10602.
> PDF retrieval source: https://arxiv.org/pdf/2301.10602. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: I Made Aswin Nahrendra, Byeongho Yu, Hyun Myung
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, terrain estimation
- Official paper: https://arxiv.org/abs/2301.10602
- Full-text retrieval: https://arxiv.org/pdf/2301.10602
- Code/Project: not identified
- Code availability: 기존 링크는 RMA·Cross-Modal Supervision 구현이다. 원 DreamWaQ의 저자 구현은 미확인. [근거](https://github.com/antonilo/rl_locomotion)
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

DreamWaQ는 사족 로봇의 자기수용감각 이력에서 몸체 속도와 지형 문맥을 함께 추정해 외부 지형 센서 없이 걷도록 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2301.10602v2#page=1) · [PDF 2쪽](https://arxiv.org/pdf/2301.10602v2#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Quadrupedal robots resemble the physical ability of legged animals to walk through unstructured terrains.
- **p. 1 / Abstract - extractive body cue:** However, designing a controller for quadrupedal robots poses a significant challenge due to their functional complexity and requires adaptation to various terrains.
- **p. 1 / Abstract - extractive body cue:** Recently, deep reinforcement learning, inspired by how legged animals learn to walk from their experiences, has been utilized to synthesize natural quadrupedal locomotion.
- **p. 1 / Abstract - extractive body cue:** However, state-of-the-art methods strongly depend on a complex and reliable sensing framework.
- **p. 1 / Abstract - extractive body cue:** Furthermore, prior works that rely only on proprioception have shown a limited demonstration for overcoming challenging terrains, especially for a long distance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This dilemma is often called the representation learning bottleneck [25], which can hinder optimal policy learning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Unlike wheeled mobile robots, quadrupedal robots can traverse unstructured terrains but are relatively difficult to control.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are threefold:
- **p. 2 / II. DREAMWAQ - extractive body cue:** The reward function consists of task rewards for tracking the
- **p. 3 / II. DREAMWAQ - extractive body cue:** Therefore, we introduced a power distribution reward to reduce motor overheating in the real world by penalizing motors' power with high variance over all motors ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 20018216, "Development of Mobile Intelligence SW for Autonomous Navigation of Legged Robots in Dynamic and Atypical Environments for Real Application").
- **p. 3 / II. DREAMWAQ - extractive body cue:** The shared encoder is trained to provide a robust body state and context estimation jointly. of only explicitly estimating the robot's state, we propose a ...
- **p. 2 / II. DREAMWAQ - extractive body cue:** 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a proprioceptive observation ot, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Conventional model-based controllers often require a complex pipeline consisting of state estimation, trajectory optimization, gait optimization, and actuator control [1]-[3], [7]-[11].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a proprioceptive observation ot, body velocity vt, and latent state zt. ... | proprioception, terrain/perception observation과 velocity command | p. 2 (II. DREAMWAQ), p. 2 (II. DREAMWAQ) |
| State/latent | Policy, Network, at/ot, neural, parameterized, infers, action, given, proprioceptive, observation, body, velocity | body/contact state, foothold 또는 behavior mode | p. 2 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 3 (II. DREAMWAQ) |
| Output/action | In DreamWaQ, the policy (actor) receives temporal partial observations, oH t , as the input, while the value network (critic) receives the full state, st, as shown in Fig. | joint target, torque, footstep 또는 locomotion action | p. 2 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ) |
| Objective/outcome | However, this reward minimizes the overall power without considering each motor's power usage balance. | velocity/progress, stability, energy와 terrain generalization | p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ) |

## Main Claims and Actual Contribution

- 몸체 상태와 잠재 환경 표현을 예측하는 추정기를 보행 정책과 함께 학습한다. [PDF 2쪽](https://arxiv.org/pdf/2301.10602v2#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2301.10602v2#page=3)
- 상태 추정 오차를 비교하고 여러 바닥·계단을 포함한 실제 야외 장거리 이동에서 정책을 시험한다. [PDF 5쪽](https://arxiv.org/pdf/2301.10602v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2301.10602v2#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENTS) |
| Embodiment/environment | Real-World Experimental Setup Real-world experiments were conducted using a Unitree A1 [26] robot. | hardware/simulator version and reset protocol | p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Dataset/benchmark | Explicit Estimation Comparison We simulated the robot walking in a stairs environment to compare the CENet with EstimatorNet in terms of their squared estimation error, as shown in Fig. | role, split, size and leakage | p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 2 (3) A robustness and durability evaluation of the learned) |
| Metric | Fig. 3: Learning curves of different algorithms. The results shown are obtained from ten different random seeds. The curves and shaded regions indicate the mean and standard deviation of the reward over ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Baseline/ablation | Compared Methods For a comparative evaluation, we compared the following algorithms with access to proprioceptions only: 1) Baseline [12]: The policy was trained without any adaptation mechanism. | fair input/data/compute/action matching | p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. CONCLUSION - extractive body cue:** DreamWaQ's limitation lies in its adaptation mechanism, where it must first hit the obstacles with its legs.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** In severe cases, inaccurate estimation can lead to catastrophic failure.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** (a) Foot stumble Foot slip Normal walk Normal walk Normal walk Climb upstairs Go downstairs Irregular foothold Adaptation Recovery (a) (b) Normal walk Fig.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** 6 shows the robot's foot reflex when faced with foot stumbling and slipping.
- **p. 2 / 3) A robustness and durability evaluation of the learned - extractive body cue:** Finally, Section IV concludes this work and briefly discusses directions for future work.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The architecture of CENet consists of a body velocity estimation model and an auto-encoder model that shares a unified encoder. The shared encoder ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ)이다.
