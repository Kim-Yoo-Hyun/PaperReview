# Learning Vision-Based Bipedal Locomotion for Challenging Terrain

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2309.14594.
> PDF retrieval source: https://arxiv.org/pdf/2309.14594. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: Helei Duan, Bikram Pandit, Mohitvishnu S. Gadde, Bart Van Marum, Jeremy Dao, Chanho Kim, Alan Fern
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, bipedal locomotion, sim-to-real, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2309.14594
- Full-text retrieval: https://arxiv.org/pdf/2309.14594
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이족 보행 정책은 깊이 영상 이력으로 로봇 기준의 높이 지도를 추정해 목표 속도와 방향을 유지하면서 지형에 대응한다. [PDF 1쪽](https://arxiv.org/pdf/2309.14594v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) for bipedal locomotion has recently demonstrated robust gaits over moderate terrains using only proprioceptive sensing.
- **p. 1 / Abstract - extractive body cue:** However, such blind controllers will fail in environments where robots must anticipate and adapt to local terrain, which requires visual perception.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a fully-learned system that allows bipedal robots to react to local terrain while maintaining commanded travel speed and direction.
- **p. 1 / Abstract - extractive body cue:** Our approach first trains a controller in simulation using a heightmap expressed in the robot's local frame.
- **p. 1 / Abstract - extractive body cue:** Next, data is collected in simulation to train a heightmap predictor, whose input is the history of depth images and robot states.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Robustly achieving such an integration of vision and locomotion remains an open problem for bipedal robots.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For this purpose, bipedal robots have the potential to match human locomotion capabilities, but currently are far inferior.

## Core Idea

- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using global ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The key contribution of our work is the sim-to-real pipeline and the system integration for these components, which allows the overall locomotion controller to transfer ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The proposed approach enables bipedal robot Cassie traversing over challenging terrains, including random high blocks, stairs, 0.5m step up (∼60% leg length), with speed up ...
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** 3: Policy consists of a blind policy and a vision-based modulator. cos (2π(ϕt + γi t)).
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** This allows the policy to gain some experience on easier terrains, which is useful early in learning, but focuses most of the learning effort on ...
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** We use a neural network to represent the policy for mapping observation sequences to actions.
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Below, we describe the observation space, action space, architecture of the policy, and training methods.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The RL policy operates at 50Hz and outputs PD setpoints for all motors, which are provided to a PD controller operating at 2kHz.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to the vision-based modulator includes all of the available observations, including the heightmap, in addition to the action produced by the blind policy. | proprioception, terrain/perception observation과 velocity command | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION) |
| State/latent | input, vision-based, modulator, includes, available, observations, including, heightmap, addition, action, produced, blind | body/contact state, foothold 또는 behavior mode | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 1 (I. INTRODUCTION), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Output/action | In particular, our architecture is composed of two primary learned components: 1) a control policy whose input is proprioceptive information and a heightmap of a local region in front of the robot ... | joint target, torque, footstep 또는 locomotion action | p. 1 (I. INTRODUCTION), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Objective/outcome | However, due to the nature of RL, this term only acts as a soft constraint that the robot may violate in favor of not falling down, in order to collect more reward ... | velocity/progress, stability, energy와 terrain generalization | p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |

## Main Claims and Actual Contribution

- 시뮬레이터의 높이 지도를 쓰는 제어기를 학습한 뒤 깊이 영상과 로봇 상태로 같은 지도를 예측하도록 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2309.14594v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2309.14594v2#page=4)
- 지형·센서 변이를 넣어 학습한 정책을 실물 이족 로봇에 옮겨 시각 정보의 유무에 따른 장애물 대응을 비교한다. [PDF 5쪽](https://arxiv.org/pdf/2309.14594v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2309.14594v2#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS) |
| Embodiment/environment | Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision events are unfavorable towards hardware deployment. | hardware/simulator version and reset protocol | p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS) |
| Dataset/benchmark | Model Architecture Reconstruction Loss (MAE) [cm] LSTM 2.806 Transformer 4.221 MLP 4.932 LSTM (w/o robot states) 4.448 loop performance in simulation shown in Figure 7-B. | role, split, size and leakage | p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS) |
| Metric | Although foot collisions lead to frequent failures, policy w/o Foot Collision Reward has a similar success rate as Ours. | definition, denominator, direction and uncertainty | p. 5 (VI. SIMULATION RESULTS), p. 6 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS) |
| Baseline/ablation | Episodes with foot collision shows that, compared to Ours, other policies have significantly more foot collisions events. | fair input/data/compute/action matching | p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data ...
- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** These random foot collisions with the terrain could lead to failures.
- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** Indeed, Terminations due to foot collision indicates that collisions account for most failure cases overall.
- **p. 6 / VI. SIMULATION RESULTS - extractive body cue:** In Termination due to foot collision, compared to LSTM, other models fails with higher chances from unfavorable foot collisions.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are weighted ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY)이다.
