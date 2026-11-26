# Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/LRA.2023.3270034.
> PDF retrieval source: https://doi.org/10.1109/LRA.2023.3270034. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / IEEE Robotics and Automation Letters
- Authors: Mayank Mittal, Calvin Yu, Qinxi Yu, Jingzhou Liu, Nikita Rudin, David Hoeller, Jia Lin Yuan, Ritvik Singh, Yunrong Guo, Hammad Mazhar, Ajay Mandlekar, Buck Babich, Gavriel State, Marco Hutter, Animesh Garg
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, simulation, Robot Learning, Benchmark, sim-to-real
- Official paper: https://api.crossref.org/works/10.1109/LRA.2023.3270034
- Full-text retrieval: https://arxiv.org/pdf/2301.04195v2
- Code/Project: https://isaac-orbit.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2301.04195v2) 기준이다.

## Why This Paper Is Here

ORBIT는 Isaac Sim에서 센서·로봇·제어기를 조합해 강화학습, 시연 수집과 정책 평가 환경을 만들 수 있는 프레임워크다. [PDF 1쪽](https://arxiv.org/pdf/2301.04195v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present ORBIT, a unified and modular framework for robot learning powered by NVIDIA Isaac Sim.
- **p. 1 / Abstract - extractive body cue:** It offers a modular design to easily and efficiently create robotic environments with photo-realistic scenes and high-fidelity rigid and deformable body simulation.
- **p. 1 / Abstract - extractive body cue:** With ORBIT, we provide a suite of benchmark tasks of varying difficulty- from singlestage cabinet opening and cloth folding to multi-stage tasks such as room ...
- **p. 1 / Abstract - extractive body cue:** To support working with diverse observations and action spaces, we include fixed-arm and mobile manipulators with different physically-based sensors and motion generators.
- **p. 1 / Abstract - extractive body cue:** ORBIT allows training reinforcement learning policies and collecting large demonstration datasets from hand-crafted or expert solutions in a matter of minutes by leveraging GPU-based parallelization.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, existing platforms often need to make a trade-off between these aspects.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Currently, this feature is under development for ORBIT.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our main contributions are as follows:
- **p. 1 / Abstract - extractive body cue:** We present ORBIT, a unified and modular framework for robot learning powered by NVIDIA Isaac Sim.
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** ORBIT is a unified simulation infrastructure that provides both pre-built environments and easy-to-use interfaces that enables extendability and customization.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To prevent a scattering of efforts for building the necessary tooling to use the simulator for robot learning, we design a unified and modular framework ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Currently, this feature is under development for ORBIT.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We design the system bottom-up - from incorporating user-defined models for the actuator dynamics to modularizing task specifications for learning with different levels of observations ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** On the other hand, physics simulators for robotics, such as Isaac Gym [13] or SAPIEN [11], provide fast and reasonably accurate rigid-body contact dynamics but ...
- **p. 5 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** 7, we show the training of Franka-Reach and Franka-Cabinet-Opening with PPO [37] using different RL frameworks and action spaces.

## Observation, State, and Output Interface

Isaac Sim 기반 플랫폼은 RGB·깊이·관절 상태 등 선택형 센서와 제어·시연 수집을 제공한다. Franka 조작의 PPO 및 시연 모방학습을 평가하고, 시뮬레이션에서 학습한 보행 정책은 실물 ANYmal-D로 전이했다. [PDF 6쪽](https://arxiv.org/pdf/2301.04195v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2301.04195v2#page=7)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To support working with diverse observations and action spaces, we include fixed-arm and mobile manipulators with different physically-based sensors and motion generators. | 과제별 상태·센서 관측 및 보행 명령 | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| State/latent | support, working, diverse, observations, action, spaces, include, fixed-arm, mobile, manipulators, different, physically-based | Isaac Sim의 로봇·물체·센서·제어 모듈 | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (2) It provides a batteries-included experience for roboti) |
| Output/action | We design the system bottom-up - from incorporating user-defined models for the actuator dynamics to modularizing task specifications for learning with different levels of observations and action spaces. | 조작 행동과 보행 정책 명령 | p. 1 (I. INTRODUCTION), p. 2 (2) It provides a batteries-included experience for roboti), p. 2 (2) It provides a batteries-included experience for roboti) |
| Objective/outcome | Since RSL-rl and rl-games are optimized for GPU, we observe a training speed of 50,00075,000 frames per second (FPS) with 2048 environments, while with stable-baselines3, we receive 6,000-18,000 FPS. | 조작 학습 성과와 실물 보행 실행 | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

## Main Claims and Actual Contribution

- 로봇·물체·센서와 운동 생성기를 모듈로 구성해 팔 조작, 이동 조작 및 변형체 과제에 재사용하게 했다. [PDF 3쪽](https://arxiv.org/pdf/2301.04195v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2301.04195v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2301.04195v2#page=5)
- 병렬 강화학습과 시연 수집 절차를 예시하고 학습한 이동 정책을 실물 ANYmal-D에서 실행하는 과정을 제시했다. [PDF 6쪽](https://arxiv.org/pdf/2301.04195v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2301.04195v2#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Embodiment/environment | It readily comes with different robotic platforms, sensors, CPU and GPU-based motion generators, and benchmark tasks that aim to provide a batteries-included experience for roboticists. | hardware/simulator version and reset protocol | p. 7 (VI. DISCUSSION), p. 7 (VI. DISCUSSION) |
| Dataset/benchmark | Owing to highquality physics, sensor simulation, and rendering, ORBIT is useful for multiple robotics challenges in both perception and decision-making. | role, split, size and leakage | p. 7 (VI. DISCUSSION), p. 7 (VI. DISCUSSION), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Metric | The success rate and trajectory lengths are reported over 100 trials. | definition, denominator, direction and uncertainty | p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 3 (Figure/Table caption), p. 7 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |
| Baseline/ablation | We provide wrappers to rlgames [35], RSL-rl [34], and stable-baselines-3 [36]. | fair input/data/compute/action matching | p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT), p. 6 (V. EXEMPLAR WORKFLOWS WITH ORBIT) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. DISCUSSION - extractive body cue:** ORBIT exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the simulation, ...
- **p. 6 / V. EXEMPLAR WORKFLOWS WITH ORBIT - extractive body cue:** To make the policy robust, we randomize the base mass (22 ± 5 kg) and add simulated random pushes.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (V. EXEMPLAR WORKFLOWS WITH ORBIT)이다.
