# HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10011640.
> PDF retrieval source: https://arxiv.org/pdf/2503.00923. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Sixu Lin, Guanren Qiao, Yunxin Tai, Ang Li, Kui Jia, Guiliang Liu
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, robust locomotion, safety recovery
- Official paper: https://iclr.cc/virtual/2026/poster/10011640
- Full-text retrieval: https://arxiv.org/pdf/2503.00923
- Code/Project: https://simonlinsx.github.io/HWC_Loco/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

HWC-Loco는 휴머노이드 보행에서 목표 추종을 계속할지 안전한 상태로 회복할지 조절하는 계층 정책을 학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c854e7870dc67e0b410a266cd45e0ad-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence.
- **p. 1 / Abstract - extractive body cue:** However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies ...
- **p. 1 / Abstract - extractive body cue:** In this study, we propose HWCLoco, a robust whole-body control algorithm tailored for humanoid locomotion tasks.
- **p. 1 / Abstract - extractive body cue:** By reformulating policy learning as a robust optimization problem, HWCLoco explicitly learns to recover from safety-critical scenarios.
- **p. 1 / Abstract - extractive body cue:** While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks.
- **p. 2 / 1 Introduction - extractive body cue:** However, excessive regularization can greatly affect the efficiency of control policy, and unstructured randomization often fails to capture safety-critical patterns in real-world applications.
- **p. 1 / 1 Introduction - extractive body cue:** These limitations significantly influence the scalability of these approaches.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To develop a reliable locomotion policy capable of generalizing from the training to the deployment environment, we propose formulating policy optimization as a robust optimization ...
- **p. 2 / 1 Introduction - extractive body cue:** To address this limitation, we propose a high-level planning policy that dynamically selects which policy to activate based on the scenario.
- **p. 15 / A.2 Implementation Details - extractive body cue:** To address this, we introduce a terrain curriculum method [63].
- **p. 15 / A.2 Implementation Details - extractive body cue:** The training terrain consists of various types, including flat planes, rough surfaces, steps, and slopes.
- **p. 17 / A.2 Implementation Details - extractive body cue:** To further promote stable posture restoration and enable smooth transitions back to the goal-tracking policy, we introduce an additional stand reward, defined as: rstand = ...
- **p. 15 / A.2 Implementation Details - extractive body cue:** Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques.
- **p. 16 / A.2 Implementation Details - extractive body cue:** During training, two trained low-level policies are loaded and rolled out to generate training data for optimizing the high-level policy.
- **p. 16 / A.2 Implementation Details - extractive body cue:** For the High-level policy, the input is the same set of observations as used by the low-level policies, with the output being a two-dimensional Q-value.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For the High-level policy, the input is the same set of observations as used by the low-level policies, with the output being a two-dimensional Q-value. | proprioception, reference pose/motion, visual or language command | p. 16 (A.2 Implementation Details), p. 15 (A.2 Implementation Details) |
| State/latent | High-level, policy, input, same, observations, low-level, policies, output, being, two-dimensional, Q-value, Action | whole-body pose, balance/contact state와 skill/mode | p. 16 (A.2 Implementation Details), p. 15 (A.2 Implementation Details), p. 15 (A.2 Implementation Details) |
| Output/action | Action Space: The policy outputs continuous actions at ∈Rn, which are utilized as target positions for a PD controller to compute joint torques. | joint/whole-body action, motion target 또는 task trajectory | p. 15 (A.2 Implementation Details), p. 15 (A.2 Implementation Details), p. 2 (1 Introduction) |
| Objective/outcome | As a result, this reward term serves as a back-tracking reward for the safety recovery mechanism, encouraging it to return to a stable goal-tracking state. | tracking, balance, skill/task success와 recovery | p. 17 (A.2 Implementation Details), p. 16 (A.2 Implementation Details), p. 16 (A.2 Implementation Details) |

## Main Claims and Actual Contribution

- 위험 상태에서 복귀하는 제어와 목표 추종을 구분하고 상위 정책이 두 행동의 사용을 조절한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c854e7870dc67e0b410a266cd45e0ad-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c854e7870dc67e0b410a266cd45e0ad-Paper-Conference.pdf#page=5)
- 지형·로봇 구조·외란을 바꾼 보행 조건에서 과제 달성과 강건성을 기존 제어기와 비교한다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c854e7870dc67e0b410a266cd45e0ad-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/8c854e7870dc67e0b410a266cd45e0ad-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 20 (Figure/Table caption), p. 8 (5 Experiment) |
| Embodiment/environment | Second, the humanoid robot used in real-world deployment has only 19 degrees of freedom, which limits whole-body coordination and constrains the expression of complex recovery behaviors. | hardware/simulator version and reset protocol | p. 9 (5 Experiment), p. 7 (5 Experiment) |
| Dataset/benchmark | 2) Robustness: How well can HWC-Loco stabilize the humanoid robot under varying levels of disturbance? | role, split, size and leakage | p. 9 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment) |
| Metric | Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on HWC-Loco's performance. Setting H = 10 achieves the ... | definition, denominator, direction and uncertainty | p. 20 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment) |
| Baseline/ablation | HWC-Loco reaches a success rate of 81.27%, outperforming all baselines by a significant margin. | fair input/data/compute/action matching | p. 8 (5 Experiment), p. 9 (5 Experiment), p. 9 (5 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 Experiment - extractive body cue:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 10: Climb Stairs Test. The blue segments indicate the activation of the goal-tracking policy, while the orange segments correspond to the safety recovery policy. ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 13: Robustness in Outdoor Settings: The robot responds to external disturbances in an outdoor environment by waving its arms and adjusting its gaits to ...
- **p. 9 / 5 Experiment - extractive body cue:** 6 Limitation Our approach has three main limitations.
- **p. 9 / 5 Experiment - extractive body cue:** Importantly, the controller does not rely solely on recovery mode but dynamically switches between goal-tracking and recovery policies, thereby adapting the action distribution to environmental ...
- **p. 7 / 5 Experiment - extractive body cue:** 2) Robustness: How well can HWC-Loco stabilize the humanoid robot under varying levels of disturbance?
- **p. 8 / 5 Experiment - extractive body cue:** This highlights the robustness of HWC-Loco to unseen disturbances.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 15 (A.2 Implementation Details), p. 17 (A.2 Implementation Details)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, excessive regularization can greatly affect the efficiency of control policy, and unstructured randomization often fails to capture safety-critical patterns in real-world applications. (p. 2, 1 Introduction).
- **Actual contribution:** To address this limitation, we propose a high-level planning policy that dynamically selects which policy to activate based on the scenario. (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 9: Extreme State: Policy's state distribution in the extreme cases A.8 History Length Experiments We investigate the impact of observation history length on HWC-Loco's performance. Setting H = 10 ... (p. 20, Figure/Table caption).
- **Explicit failure boundary:** To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to a lower value, thereby reducing ... (p. 7, 5 Experiment).
