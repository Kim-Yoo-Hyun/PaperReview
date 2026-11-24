# GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.03984.
> PDF retrieval source: https://arxiv.org/pdf/2503.03984. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Navigation, Gaussian Splatting
- Official paper: https://arxiv.org/abs/2503.03984
- Full-text retrieval: https://arxiv.org/pdf/2503.03984
- Code/Project: https://qianzhong-chen.github.io/gradnav.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

GRaD-Nav는 Gaussian Splatting으로 만든 시각 환경과 미분 가능한 비행 동역학을 결합해 드론 이동 정책을 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2503.03984v3#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Autonomous visual navigation is an essential element in robot autonomy.
- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) offers a promising policy training paradigm.
- **p. 1 / Abstract - extractive body cue:** However, existing RL methods suffer from high sample complexity, poor sim-to-real transfer, and limited runtime adaptability.
- **p. 1 / Abstract - extractive body cue:** These problems are particularly challenging for drones, with complex nonlinear and unstable dynamics, and strong dynamic coupling between control and perception.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To tackle the challenge, one of the most important bottlenecks lies on the difficulty in getting high-quality perception data when training the policy in conventional ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the integration of these different modules has many issues, including high system complexity and computational overhead, communication latency between modules, multiple points of failure, ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our main contributions are: • We introduce a simulator for training robot vision-based control policies by integrating 3DGS for high-fidelity visuals with a differentiable dynamics ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To achieve the goal of visual-motor navigation, we propose a novel approach that leverages 3DGS in conjunction with DDRL, using SHAC-like training algorithm and a ...
- **p. 3 / III. METHOD - extractive body cue:** (10) The state st = [pt, vt, qt, ωt] consists of position, velocity, orientation (quaternion), and angular velocity.
- **p. 3 / III. METHOD - extractive body cue:** At its core, we introduce GRaD-Nav, a DDRL algorithm tailored for end-to-end visual navigation, improving sample efficiency over prior methods.
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive body cue:** icy: Beyond training a single policy for a long horizon trajectory, our method can also train generalizable policies that can adapt to different surrounding environments ...
- **p. 3 / III. METHOD - extractive body cue:** The differentiable drone dynamics model is also implemented with PyTorch, which enables efficient Jacobian computation through autograd for training the policy using our GRaD-Nav algorithm.
- **p. 3 / III. METHOD - extractive body cue:** 2) Hybrid simulation with 3DGS: We used a pre-trained 3DGS model to deliver the drone's first person perspective visual information and to imitate the drone's ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive body cue:** By rolling training across these different environments, we finally trained a policy that can adapt to different gate positions and achieve generalizable navigation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy transfers zero-shot to drone hardware and adapts to new navigation task instances at runtime. directly map sensor inputs to control outputs, bypassing the need for explicit modular separation [9]. | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| State/latent | policy, transfers, zero-shot, drone, hardware, adapts, navigation, task, instances, runtime, directly, sensor | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (II. BACKGROUND) |
| Output/action | Our system takes body rates ωd t ∈ R3 and normalized thrust ct ∈[0, 1] as control inputs, and outputs the next state st+1 = (p, q, v, ω, a) ∈R16 containing ... | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND) |
| Objective/outcome | Simulator Setting 1) Differentiable Quadrotor Dynamics Simulation: We implemented a parallelized, differentiable quadrotor dynamics simulator in PyTorch that computes gradients through full state transitions. | goal reach, safety, localization error와 replanning latency | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol) |

## Main Claims and Actual Contribution

- 시각 관측과 동역학을 이용한 정책 학습에 환경 변화를 추정하는 네트워크와 여러 장면의 교과학습을 결합한다. [PDF 2쪽](https://arxiv.org/pdf/2503.03984v3#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2503.03984v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2503.03984v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2503.03984v3#page=5)
- 실물 드론에서 추가 미세조정 없이 비행을 시험하고 게이트의 위치나 주변 배치가 달라졌을 때의 전이를 측정했다. [PDF 6쪽](https://arxiv.org/pdf/2503.03984v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2503.03984v3#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |
| Embodiment/environment | 7: Robot hardware experiments of drone flying through middle gate. | hardware/simulator version and reset protocol | p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | It is to be noted that BPTT samples the whole trajectory for policy updating, meaning the horizon length equals the episode length, which can take up a lot of memory for each ... | role, split, size and leakage | p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Metric | Our ablation test metrics include: (i) training reward, (ii) test reward, and (iii) test success rate. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |
| Baseline/ablation | Without CENet, our method can still train a policy network that achieves high rewards compared to other ablation cases. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. CONCLUSIONS - extractive body cue:** Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate traversal.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** All of the failure cases without CENet on two trajectories "crash" due to unsuccessful obstacle avoidance.
- **p. 7 / V. CONCLUSIONS - extractive body cue:** Future work includes (i) multi-task training with language input, (ii) improving generalization via stronger backbones and diverse environments, and (iii) extending to contact-rich tasks such ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** As visual perception is our navigation policy's major sensor input, it is not surprising that the policy without visual observation cannot conduct successful navigation.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. BACKGROUND), p. 3 (III. METHOD)이다.
