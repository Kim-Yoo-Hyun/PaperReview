# Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v164/rudin22a.html.
> PDF retrieval source: https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / CoRL
- Authors: Nikita Rudin, David Hoeller, Philipp Reist, Marco Hutter
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, locomotion, Reinforcement Learning, massively parallel simulation
- Official paper: https://proceedings.mlr.press/v164/rudin22a.html
- Full-text retrieval: https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf
- Code/Project: https://leggedrobotics.github.io/legged_gym/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Rudin 등은 한 GPU에서 많은 로봇을 병렬 시뮬레이션해 ANYmal 보행 정책을 짧은 벽시계 시간에 학습한다. [PDF 1쪽](https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this work, we present and study a training set-up that achieves fast policy generation for real-world robotic tasks by using massive parallelism on a ...
- **p. 1 / Abstract - extractive body cue:** We analyze and discuss the impact of different training algorithm components in the massively parallel regime on the final policy performance and training times.
- **p. 1 / Abstract - extractive body cue:** In addition, we present a novel game-inspired curriculum that is well suited for training with thousands of simulated robots in parallel.
- **p. 1 / Abstract - extractive body cue:** We evaluate the approach by training the quadrupedal robot ANYmal to walk on challenging terrain.
- **p. 1 / Abstract - extractive body cue:** The parallel approach allows training policies for flat terrain in under four minutes, and in twenty minutes for uneven terrain.
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- **p. 3 / 1 Introduction - extractive body cue:** Resets based on failure or reaching a goal are not a problem because the critic can predict them.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 1 / Abstract - extractive body cue:** In addition, we present a novel game-inspired curriculum that is well suited for training with thousands of simulated robots in parallel.
- **p. 5 / 1 Introduction - extractive body cue:** Furthermore, our method doesn't require tuning and is straightforward to implement in a parallel manner with nearzero processing cost.
- **p. 1 / Abstract - extractive body cue:** In this work, we present and study a training set-up that achieves fast policy generation for real-world robotic tasks by using massive parallelism on a ...
- **p. 3 / 1 Introduction - extractive body cue:** Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence optimize training times, ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we use NVIDIA's Isaac Gym simulation environment [8], which runs both the simulation and training on the GPU and is capable of ...
- **p. 1 / Abstract - extractive body cue:** We analyze and discuss the impact of different training algorithm components in the massively parallel regime on the final policy performance and training times.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The observations are composed of: base linear and angular velocities, measurement of the gravity vector, joint positions and velocities, the previous actions selected by the policy, and finally, 108 measurements of the ... | proprioception, terrain/perception observation과 velocity command | p. 5 (1 Introduction), p. 5 (1 Introduction) |
| State/latent | observations, composed, base, linear, angular, velocities, measurement, gravity, vector, joint, positions, previous | body/contact state, foothold 또는 behavior mode | p. 5 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | 3.2 Observations, Actions, and Rewards The policy receives proprioceptive measurements of the robot as well as terrain information around the robot's base. | joint target, torque, footstep 또는 locomotion action | p. 5 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | In supplementary material, we show the effect of this solution on the total reward as well as the critic loss. | velocity/progress, stability, energy와 terrain generalization | p. 4 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 로봇이 이동한 거리에 따라 각 환경의 지형 난도를 바꿔 서로 다른 난이도를 동시에 학습하게 한다. [PDF 4쪽](https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf#page=4) · [PDF 5쪽](https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf#page=5)
- 시뮬레이션에서 학습한 험지 정책을 실제 ANYmal로 옮겨 장애물이 있는 지형에서 보행을 확인한다. [PDF 7쪽](https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf#page=7) · [PDF 8쪽](https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Results), p. 7 (4 Results) |
| Embodiment/environment | As such, we simplify the task by reducing the maximum step size of stairs and obstacles and directly train robots on the full range of difficulties. | hardware/simulator version and reset protocol | p. 6 (4 Results), p. 6 (4 Results) |
| Dataset/benchmark | In terms of training time, we see a nearly linear scaling up to 4000 robots, after which simulation throughput gains slow down. | role, split, size and leakage | p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results) |
| Metric | (b) Success rate for climbing and descending sloped terrains. | definition, denominator, direction and uncertainty | p. 7 (4 Results), p. 7 (4 Results), p. 6 (4 Results) |
| Baseline/ablation | We begin by setting a baseline with nrobots = 20000 and nsteps = 50, resulting in a batch size of 1M samples. | fair input/data/compute/action matching | p. 6 (4 Results), p. 6 (4 Results), p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 Results - extractive body cue:** As such, we can conclude that increasing the number of robots is beneficial for both final performance and training time, but there is an upper ...
- **p. 8 / 5 Conclusion - extractive body cue:** The purpose of this work is not to obtain the absolute best-performing policy with the highest robustness.
- **p. 8 / 4 Results - extractive body cue:** As part of future work, we plan to merge the two approaches.
- **p. 7 / 4 Results - extractive body cue:** To that end, we perform robustness and traversability tests.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)이다.
