# Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2310.03581.
> PDF retrieval source: https://arxiv.org/pdf/2310.03581. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: Chong Zhang, Jin Jin, Jonas Frey, Nikita Rudin, Matías Mattamala, Cesar Cadena, Marco Hutter
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, legged locomotion, Navigation, robust perception, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2310.03581
- Full-text retrieval: https://arxiv.org/pdf/2310.03581
- Code/Project: https://bit.ly/45NBTuh
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이 연구는 장애물이나 구덩이가 외부 센서에서 사라지는 상황에서도 사족 로봇을 안내하는 국소 탐색 정책을 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2310.03581v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Autonomous robots must navigate reliably in unknown environments even under compromised exteroceptive perception, or perception failures.
- **p. 1 / Abstract - extractive body cue:** Such failures often occur when harsh environments lead to degraded sensing, or when the perception algorithm misinterprets the scene due to limited generalization.
- **p. 1 / Abstract - extractive body cue:** In this paper, we model perception failures as invisible obstacles and pits, and train a reinforcement learning (RL) based local navigation policy to guide our ...
- **p. 1 / Abstract - extractive body cue:** Unlike previous works relying on heuristics and anomaly detection to update navigational information, we train our navigation policy to reconstruct the environment information in the ...
- **p. 1 / Abstract - extractive body cue:** To this end, we incorporate both proprioception and exteroception into our policy inputs, thereby enabling the policy to sense collisions on different body parts and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, such manually-designed rules cannot scale well to diverse situations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Generally, given an accurate map, it is not difficult for existing navigation planners to guide the robot towards the local goal safely.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion.
- **p. 2 / III. METHOD - extractive body cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, such manually-designed rules cannot scale well to diverse situations.
- **p. 3 / III. METHOD - extractive body cue:** Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged ...
- **p. 2 / III. METHOD - extractive body cue:** Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical RL structure.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged Information Observations ... | proprioception, terrain/perception observation과 velocity command | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| State/latent | Actor, Critic, Low-Level, Exteroception, Proprioception, Previous, Action, Position, Command, Heading, Corrupted, Map | body/contact state, foothold 또는 behavior mode | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (III. METHOD) |
| Output/action | The learned navigation policy generates velocity commands to a pre-existing low-level locomotion policy, and takes low-level observations as part of its inputs. | joint target, torque, footstep 또는 locomotion action | p. 2 (I. INTRODUCTION), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Overview The objective of our method is to guide the robot to a local target within the given time. | velocity/progress, stability, energy와 terrain generalization | p. 2 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- 손상된 지형 관측과 자기수용감각을 결합해 지형 정보를 잠재 공간에서 복원하도록 정책을 훈련한다. [PDF 3쪽](https://arxiv.org/pdf/2310.03581v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2310.03581v1#page=4)
- 시뮬레이션의 반응형 계획기 비교와 실제 ANYmal의 접촉·낙차 대응 실험으로 인지 실패 시 행동을 평가한다. [PDF 4쪽](https://arxiv.org/pdf/2310.03581v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2310.03581v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2310.03581v1#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES) |
| Embodiment/environment | Environments We verify our methodology on the quadruped ANYmal robot both in simulation and in the real world. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP) |
| Dataset/benchmark | Ours outperforms others in the metrics. commands directing away from the pit until the robot regains stability. | role, split, size and leakage | p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES) |
| Metric | According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect 100 % success rate. | definition, denominator, direction and uncertainty | p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES), p. 4 (Figure/Table caption) |
| Baseline/ablation | Comparison Results We compare the proposed Ours with the baselines Oracle and Planner in simulation. | fair input/data/compute/action matching | p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive body cue:** Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.
- **p. 5 / V. RESULTS AND ANALYSES - extractive body cue:** These results indicate that the navigation policy cannot learn to react to perception failures without being exposed to them, and the locomotion policy cannot overcome ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is in ...
- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive body cue:** Hence, it is of great interest if we can train a policy to actively explore these areas and explicitly revise the map allowing it to ...
- **p. 5 / V. RESULTS AND ANALYSES - extractive body cue:** We draw the following conclusions based on the ablation results: 1) The proprioception as part of the observations is generally beneficial to the robustness against ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3. An overview of our learning system. Left The actor-critic design of the navigation policy. Right: Our high-level navigation policy generates velocity commands tracked ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (III. METHOD)이다.
