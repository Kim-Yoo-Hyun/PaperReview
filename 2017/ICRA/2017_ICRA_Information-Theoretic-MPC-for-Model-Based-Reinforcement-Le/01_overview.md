# Information Theoretic MPC for Model-Based Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ieeexplore.ieee.org/document/7989202/.
> PDF retrieval source: https://ieeexplore.ieee.org/document/7989202/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / ICRA
- Authors: Grady Williams, Nolan Wagener, Brian Goldfain, Paul Drews, James M. Rehg, Byron Boots, Evangelos A. Theodorou
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, model predictive control, model-based RL, Planning
- Official paper: https://ieeexplore.ieee.org/document/7989202/
- Full-text retrieval: https://ieeexplore.ieee.org/document/7989202/
- Code/Project: https://github.com/AutoRally/autorally
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

정보이론적 MPC는 비선형 동역학 모델에서 표본 궤적의 비용으로 제어 입력을 갱신하며 학습한 신경망 동역학도 사용할 수 있다. [PDF 1쪽](https://homes.cs.washington.edu/~bboots/files/InformationTheoreticMPC.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce an information theoretic model predictive control (MPC) algorithm capable of handling complex cost criteria and general nonlinear dynamics.
- **p. 1 / Abstract - extractive body cue:** The generality of the approach makes it possible to use multi-layer neural networks as dynamics models, which we incorporate into our MPC algorithm in order ...
- **p. 1 / Abstract - extractive body cue:** We test the algorithm in simulation on a cartpole swing up and quadrotor navigation task, as well as on actual hardware in an aggressive driving ...
- **p. 1 / Abstract - extractive body cue:** Empirical results demonstrate that the algorithm is capable of achieving a high level of performance and does so only utilizing data collected from the system.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many robotic tasks can be framed as reinforcement learning (RL) problems, where a robot seeks to optimize a cost function encoding a task by utilizing ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite all of the progress on both model-based and model-free RL methods, generalization remains a primary challenge.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, in prior work, MPPI could only be applied to systems with control affine dynamics.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** This is a significant step forward because it enables a purely data-driven approach to model learning within the MPPI framework.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This limits the method's ability to discover novel optimal control behaviors.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The information theoretic MPC algorithm that we develop is originally based on path integral control theory.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The complexity of the objectives in RL tasks increases the computational cost of the optimization, a major problem since optimization must occur in real time.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The types of reinforcement learning problems encountered in robotic tasks are frequently in the continuous state-action space and high dimensional [1]. | joint/task state, reference와 sensor feedback | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| State/latent | types, reinforcement, learning, problems, encountered, robotic, tasks, frequently, continuous, state-action, space, high | state estimate, task-space error와 control decision | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Output/action | In the second paradigm, model-based RL approaches first learn a model of the system and then train a feedback control policy using the learned model [6]-[8]. | torque, force, velocity 또는 position command | p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Objective/outcome | The complexity of the objectives in RL tasks increases the computational cost of the optimization, a major problem since optimization must occur in real time. | tracking, stability, constraint satisfaction과 contact behavior | p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL) |

## Main Claims and Actual Contribution

- 정보이론적 목적에서 표본 기반 제어 갱신을 도출하고 실제 시스템 자료로 학습한 동역학을 예측에 결합했다. [PDF 2쪽](https://homes.cs.washington.edu/~bboots/files/InformationTheoreticMPC.pdf#page=2) · [PDF 4쪽](https://homes.cs.washington.edu/~bboots/files/InformationTheoreticMPC.pdf#page=4)
- 카트폴·쿼드로터는 시뮬레이션에서, 고속 주행은 실제 차량에서 평가해 학습한 모델을 쓰는 제어기의 동작을 확인했다. [PDF 5쪽](https://homes.cs.washington.edu/~bboots/files/InformationTheoreticMPC.pdf#page=5) · [PDF 6쪽](https://homes.cs.washington.edu/~bboots/files/InformationTheoreticMPC.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 5 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS) |
| Embodiment/environment | The bootstrapping dataset for the cart-pole comes from 5 minutes of multiple MPPI demonstrations using known dynamics but a different cost function for the swing-up task. | hardware/simulator version and reset protocol | p. 5 (V. SIMULATED RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | One explanation for this is that the initial dataset was deliberately collected for system identification, and it consists of a variety of maneuvers meant to excite various modes of the dynamics. | role, split, size and leakage | p. 5 (V. SIMULATED RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 5 (V. SIMULATED RESULTS) |
| Metric | Multi-Step Error We train the neural network dynamics on one-step prediction error, which does not necessarily result in accurate multistep prediction. | definition, denominator, direction and uncertainty | p. 6 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Baseline/ablation | In our prior work, MPPI was successfully applied to this task using a physics-inspired model. | fair input/data/compute/action matching | p. 6 (VI. EXPERIMENTAL RESULTS), p. 5 (V. SIMULATED RESULTS), p. 5 (V. SIMULATED RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** Running the algorithm without a bootstrapped neural network results in repeated failures.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** The slip angle is defined as -arctan( vy /vx/), where vx and vy are the longitudinal and lateral velocities, respectively.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** M(x, y) is the cost-map value at the position (x, y), and Sc is an indicator variable which activates if the magnitude of the slip ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** During training, we set the slip angle threshold to 15.76 degrees (0.275 radians), and for the final testing runs we raised it to 21.5 degrees ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Slip 10 m/s 10.34 9.93 8.05 38.68 11 m/s 9.97 9.43 8.71 34.65 12 m/s 9.88 9.47 8.63 43.72 13 m/s 9.74 9.36 8.44 48.70 ...
- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** The temperature was set as λ = 1 and the system noise to (2.5, .25, .25, .25), where the 2.5 value corresponds to the thrust ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL), p. 5 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, in prior work, MPPI could only be applied to systems with control affine dynamics. (p. 1, I. INTRODUCTION).
- **Actual contribution:** This limits the method's ability to discover novel optimal control behaviors. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** The final performance margins for both the cart-pole and quadrotor are within 10% of what can be achieved with perfect model knowledge, which indicates that, in this case, our MPC ... (p. 6, V. SIMULATED RESULTS).
- **Explicit failure boundary:** Running the algorithm without a bootstrapped neural network results in repeated failures. (p. 5, V. SIMULATED RESULTS).

## 원문과 공개 자료

- 코드 · AutoRally 차량의 MPPI 제어기 구현 · autorally_control/include/autorally_control/path_integral/mppi_controller.cu [배포 파일](https://raw.githubusercontent.com/AutoRally/autorally/48bae14fe4b2d56e5ca11fd2fec3d7dfac7a0e75/autorally_control/include/autorally_control/path_integral/mppi_controller.cu)
- 데이터 · 원문은 cart-pole swing-up 실험에 사용한 자료를 보고한다. 이 연구의 해당 자료 배포 파일은 미확인이다. [검토 근거](https://homes.cs.washington.edu/~bboots/files/InformationTheoreticMPC.pdf)
