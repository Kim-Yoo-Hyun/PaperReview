# Rapid Locomotion via Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss18/p022.html.
> PDF retrieval source: https://arxiv.org/pdf/2205.02824. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RSS
- Authors: Gabriel B. Margolis, Ge Yang, Kartik Paigwar, Tao Chen, Pulkit Agrawal
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, high-speed locomotion
- Official paper: https://www.roboticsproceedings.org/rss18/p022.html
- Full-text retrieval: https://arxiv.org/pdf/2205.02824
- Code/Project: https://agility.csail.mit.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

이 연구는 시뮬레이션 강화학습 정책을 MIT Mini Cheetah에 옮겨 자연 노면에서 빠른 달리기와 방향 전환을 제어한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss18/p022.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Agile maneuvers such as sprinting and high-speed turning in the wild are challenging for legged robots.
- **p. 1 / Abstract - extractive body cue:** We present an end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
- **p. 1 / Abstract - extractive body cue:** This system runs and turns fast on natural terrains like grass, ice, and gravel and responds robustly to disturbances.
- **p. 1 / Abstract - extractive body cue:** Our controller is a neural network trained in simulation via reinforcement learning and transferred to the real world.
- **p. 1 / Abstract - extractive body cue:** The two key components are (i) an adaptive curriculum on velocity commands and (ii) an online system identification strategy for sim-to-real transfer leveraged from prior ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Task difficulty is a function of both the system dynamics and the optimization algorithm, making manual curriculum design tedious and problem-dependent.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, increasing the range of commanded velocities to include high speeds results in training failure.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter sprint ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The same policy can spin the robot at 5.7 rad/s on flat ground and also enables the robot to spin on the more challenging icy ...
- **p. 3 / III. METHOD - extractive body cue:** Teacher-student training enables the agent to specialize its behavior to the current dynamics dt, instead of learning a single behavior that works across different dt.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that reinforcement learning can be used to learn locomotion controllers that simultaneously achieve linear and angular high-speed behaviors and operate on diverse natural ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One possibility is to resolve these issues by making targeted improvements to the hand-designed models used in modelbased control.
- **p. 2 / III. METHOD - extractive body cue:** As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ...
- **p. 3 / III. METHOD - extractive body cue:** (hθa) x[t-h:t-1] (42 × 15) [256, 32] zt (8) Body (πθb) xt (42), zt (8) [512, 256, 128] at (12) TABLE II: Network architecture for ...
- **p. 2 / III. METHOD - extractive body cue:** Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives as output joint ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives as output joint position commands (see Figure 2), which are ... | proprioception, terrain/perception observation과 velocity command | p. 2 (III. METHOD), p. 2 (III. METHOD) |
| State/latent | goal, learn, policy, parameters, takes, input, sensory, data, velocity, commands, gives, output | body/contact state, foothold 또는 behavior mode | p. 2 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Output/action | As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ˙qt, gori t , at-1]. | joint target, torque, footstep 또는 locomotion action | p. 2 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | The policy πT (xt, dt), commonly referred to as a teacher policy, is trained using an RL algorithm to maximize the expected sum of rewards. | velocity/progress, stability, energy와 terrain generalization | p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- 이미 추종할 수 있는 속도에서 이웃 명령으로 학습 범위를 넓혀 고속 영역까지 탐색하게 한다. [PDF 2쪽](https://www.roboticsproceedings.org/rss18/p022.pdf#page=2) · [PDF 3쪽](https://www.roboticsproceedings.org/rss18/p022.pdf#page=3)
- 최근 관측 이력에서 동역학 정보를 추정하도록 하고 지면과 명령이 바뀔 때 실물 속도 추종을 평가한다. [PDF 6쪽](https://www.roboticsproceedings.org/rss18/p022.pdf#page=6) · [PDF 7쪽](https://www.roboticsproceedings.org/rss18/p022.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Embodiment/environment | The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length. | hardware/simulator version and reset protocol | p. 6 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Dataset/benchmark | The robot stands 30 cm tall and weighs 9 kg. | role, split, size and leakage | p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), p. 2 (II. EXPERIMENTAL SETUP), p. 2 (II. EXPERIMENTAL SETUP) |
| Metric | Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum for all error thresholds. (b) Velocity tracking error ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Baseline/ablation | Unlike our learned controller, the baseline did not recover from (1) slipping down the gravelly incline and (4) tripping over the barrier. | fair input/data/compute/action matching | p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. DISCUSSION - extractive body cue:** Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or ...
- **p. 8 / VI. DISCUSSION - extractive body cue:** We cannot use motion capture to record the robot's state outdoors as we do in the lab.
- **p. 7 / IV. RESULTS - extractive body cue:** Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline made ...
- **p. 7 / IV. RESULTS - extractive body cue:** While these results highlight the robustness of policies, we want to emphasize that we are not claiming that such (or even more) robustness cannot be ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum for ...
- **p. 6 / IV. RESULTS - extractive body cue:** We observe that the policy trained without any curriculum fails to learn.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 3 (III. METHOD)이다.
