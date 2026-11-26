# Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p130.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p130.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Guanqi He, Xiaofeng Guo, Luyi Tang, Yuanhang Zhang, Mohammadreza Mousaei, Jiahe Xu, Junyi Geng, Sebastian Scherer, Guanya Shi
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, aerial manipulation, whole-body control, teleoperation, Imitation Learning, assembly
- Official paper: https://www.roboticsproceedings.org/rss21/p130.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p130.pdf
- Code/Project: https://lecar-lab.github.io/flying_hand/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://www.roboticsproceedings.org/rss21/p130.pdf) 기준이다.

## Why This Paper Is Here

Flying Hand는 비행체와 로봇팔의 결합 동역학을 하위 제어기가 처리해 상위 정책과 조작자가 말단의 움직임으로 공중 조작을 지시하게 한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Aerial manipulation has recently attracted inereasing interest from both industry and academia.
- **p. 1 / Abstract - extractive body cue:** Previous approaches have demonstrated success in various specific tasks.
- **p. 1 / Abstract - extractive body cue:** However, their hardware design and control frameworks are often tightly coupled with task specifications, limiting the detelopment of cros-las and crompatform algorithms, Ingpred by the ...
- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 1 / Abstract - extractive body cue:** Real-world experiments show that the proposed framework significantly improves end-effector tracking accuracy and can handle multiple aerial teleoperation and tion learning tasks, including writing, peg-inchanging ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** However, there is no precedent to incorporate such IL-based policy into aerial manipulation fields due to the lack of a mature demonstration collection system, such ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** [As we mentioned, our framework enables the decoupling between the high-level policy and low-level controller, with the ee-centric interface serving asthe sole connection between them.
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [25] proposed a framework that consists of a robust humanoid whole-body controller with a high-level policy, either an autonomous agent like GPT-40 or an imitation ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** In this section, we introduce two aerial manipulation systems we ‘developed based on this framework: the ee-centrc aerial tele- ‘operation system and the imitaton-Iearning-based autonomous ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By effectively decoupling high-level policies from low-level control, it enables the development ‘of embodiment-agnostic policies 47}, {10}.
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** The transformerbased decoder generates action sequences from the latent variable (only during training and set to be the mean of the prior during testing), current ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **p. 7 / B. EE-Centrie Policy Learning - extractive body cue:** ACT utilizes a Conditional Variational Autoencoder (CVAE) where the encoder compresses action sequences and Joint observations into a latent style variable.

## Observation, State, and Output Interface

그림 2에서 ACT는 말단 상태와 두 RGB 관측으로 목표 말단 자세를 예측한다. 전신 MPC가 비행체·팔 명령을 계산한다. 물체 집기와 연속 과제는 시뮬레이션에서, 자율 핀 삽입은 실제 비행체에서도 평가했다. [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=3) · [PDF 12쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=12)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose in the observation and action space is replaced ... | 말단 상태와 기체·말단의 RGB 영상 | p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning) |
| State/latent | After, train, joint, space, ACT, policy, same, training, setting, ee-centric, except, end-effector | 말단 목표 자세와 결합 기체·팔 동역학 | p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface) |
| Output/action | At the most highlevel, the ee-centric policy module gets current observations and generates the target end-effector states online without the need to consider the specific platform jointly. | ACT의 목표 말단 자세와 MPC의 기체·팔 명령 | p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (B. EE-Centrie Policy Learning) |
| Objective/outcome | ‘The MPC formulation minimizes a cost function over a finite time horizon H while subject to system dynamics and constraints: | 비행 추종 오차와 조작 과제 성공 | p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 8 (B. Implementation Details) |

## Main Claims and Actual Contribution

- 완전 구동 육회전익에 4자유도 팔을 장착하고 말단 기준 전신 예측 제어기를 구성했다. [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=4) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=6)
- 비행 중 말단 추종과 원격조작을 시험하고 시연으로 학습한 정책의 공중 핀 삽입을 평가했다. [PDF 9쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=9) · [PDF 11쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=11) · [PDF 12쪽](https://www.roboticsproceedings.org/rss21/p130.pdf#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Embodiment/environment | Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware designs. | hardware/simulator version and reset protocol | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| Dataset/benchmark | 2) Real-world Experiments: We adopt the aerial peg-inhole task to demonstrate our capability to derive an autonomous policy from human demonstrations for aerial manipulation in the real world. ‘The task configurations are ... | role, split, size and leakage | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Metric | + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole task, directly benefiting from task-space supervision that eliminates the accumulated end-effector error fro ... | definition, denominator, direction and uncertainty | p. 10 (B. Implementation Details), p. 11 (B. Implementation Details), p. 10 (B. Implementation Details) |
| Baseline/ablation | 4, compared with our method (blue), the baseline wo. | fair input/data/compute/action matching | p. 8 (B. Implementation Details), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 11 / IX. LIMITATIONS - extractive body cue:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.
- **p. 11 / IX. LIMITATIONS - extractive body cue:** Incorporating onboard perception to detect obstacles and generate safety constraints in real-time will be our next step, as various studies have demonstrated the feasibility of ...
- **p. 8 / B. Implementation Details - extractive body cue:** MPC (orange) suffers from significant motion lag, as DFFC fails to account for trajectory feedforward.
- **p. 7 / A. Experimental Setup - extractive body cue:** LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution.
- **p. 8 / B. Implementation Details - extractive body cue:** 8 shows disturbances along the base x (red), = (blue) and Open (green), respectively. ‘The disturbances and model uncertainties primarily arise from arm motions, inaccurate ...
- **p. 9 / B. Implementation Details - extractive body cue:** 7 reveals that tracking error increases at lower altitudes (around Im), likely due to unmodeled ground and wall effect disturbances.
- **p. 10 / B. Implementation Details - extractive body cue:** Disturbance zeae and LI disturbance

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction), p. 7 (B. EE-Centrie Policy Learning)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, In real-world scenarios, manipulation tasks ... (p. 1, 1. Iyrropuction).
- **Actual contribution:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for ... (p. 1, Abstract).
- **Evaluation boundary:** Root Mean Square Error (RMSE) is used as the tracking performance evaluation criterion. (p. 8, A. Experimental Setup).
- **Explicit failure boundary:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. (p. 11, IX. LIMITATIONS).
