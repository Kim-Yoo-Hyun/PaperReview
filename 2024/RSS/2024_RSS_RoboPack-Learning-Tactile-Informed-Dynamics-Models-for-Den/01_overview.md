# RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p130.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p130.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Bo Ai, Stephen Tian, Haochen Shi, Yixuan Wang, Cheston Tan, Yunzhu Li, Jiajun Wu
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, tactile sensing, dynamics model
- Official paper: https://www.roboticsproceedings.org/rss20/p130.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p130.pdf
- Code/Project: https://robo-pack.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RoboPack은 시각·촉각 이력으로 물체의 운동과 물성을 추정해 좁은 공간에 물체를 밀어 넣을 행동을 계획한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p130.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tactile feedback is critical for understanding the dynamics of both rigid and deformable objects in many manipulation tasks, such as non-prehensile manipulation and dense packing.
- **p. 1 / Abstract - extractive body cue:** We introduce an approach that combines visual and tactile sensing for robotic manipulation by learning a neural, tactile-informed dynamics model.
- **p. 1 / Abstract - extractive body cue:** Our proposed framework, RoboPack, employs a recurrent graph neural network to estimate object states, including particles and object-level latent physics information, from historical visuo-tactile observations ...
- **p. 1 / Abstract - extractive body cue:** Our tactile-informed dynamics model, learned from real-world data, can solve downstream robotics tasks with model-predictive control.
- **p. 1 / Abstract - extractive body cue:** We demonstrate our approach on a real robot equipped with a compliant SoftBubble tactile sensor on non-prehensile manipulation and dense packing tasks, where the robot ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These tasks involve multi-object interactions with complex dynamics that cannot be determined from vision alone.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction ...
- **p. 4 / III. METHOD - extractive body cue:** For multi-object packing settings with significant occlusion, we introduce an objective that constrains tracked points to be near the corresponding object masks, providing more consistent ...
- **p. 5 / III. METHOD - extractive body cue:** In the following paragraphs, we describe how our method performs state estimation using history information and future prediction.
- **p. 5 / III. METHOD - extractive body cue:** For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 4 / III. METHOD - extractive body cue:** F x, F y are the mean of local force vectors across spatial dimensions, and /Q/ is defined as /Q/ = r max i,j /qx ...
- **p. 5 / III. METHOD - extractive body cue:** Concretely, we use Model Predictive Path Integral (MPPI) to perform this optimization [58].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To formulate this problem, we define the observation space as O, the state space as S, and the action space as A. | tactile image/force, vision과 proprioceptive history | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | formulate, problem, define, observation, space, state, action, Secondly, estimator, infers, object, states | contact geometry, force state 또는 latent dynamics | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | Secondly, the state estimator g infers object states s from any prior interactions, which includes a single visual frame ovis 0 , the subsequent tactile observations otact 0:t , and the corresponding ... | grasp/contact action, force command 또는 object motion | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Objective/outcome | The objective is to find a sequence of actions a0, ..., aH-1 to minimize a cost function J between the final states and a given target state sg: (a0, ..., aH-1) = ... | slip/contact success, force/pose error와 robustness | p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD) |

## Main Claims and Actual Contribution

- 순환 그래프 신경망이 입자 상태와 물체별 잠재 물성을 추정하고 후보 행동이 만들 미래 상태를 예측한다. [PDF 4쪽](https://www.roboticsproceedings.org/rss20/p130.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss20/p130.pdf#page=5)
- 실물 상호작용 자료로 동역학을 학습해 Soft-Bubble 촉각 센서를 장착한 로봇의 비파지 밀기와 밀집 포장을 모델 예측 제어로 수행했다. [PDF 7쪽](https://www.roboticsproceedings.org/rss20/p130.pdf#page=7) · [PDF 10쪽](https://www.roboticsproceedings.org/rss20/p130.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |
| Embodiment/environment | Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks. | hardware/simulator version and reset protocol | p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP) |
| Dataset/benchmark | The robot has access to tactile feedback at all steps but only visual observations in between pushes, which corresponds to the real-world feedback loop frequency. | role, split, size and leakage | p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. EXPERIMENTS) |
| Metric | We report the minimum error to goal across 10 plan executions per trial, trial success rates, and number of execution steps to solve the task. | definition, denominator, direction and uncertainty | p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline methods in the Non-prehensile Box Pushing task. Red dots indicate the rod and blue dots represent ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of the ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Metrics such as EMD and CD that emphasize global shape and distribution but are insensitive to subtle positional changes cannot differentiate the two methods in ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Mathematically, the loss function is J (ˆot, og, at) = X x∈ˆot min y∈og //x -y//2 - X y∈og min x∈ˆot //x -y//2 + r ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Tactile sensing for dense packing. Tactile feedback is critical in tasks with heavy occlusion and rich contact, such as dense packing. (a) Humans ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (III. METHOD), p. 4 (III. METHOD)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone is insufficient to determine the ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction data per task on average. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ± 0.006 1.18 ± 0.043 ... (p. 8, V. EXPERIMENTS).
- **Explicit failure boundary:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, but again tactile signals are ... (p. 6, IV. EXPERIMENTAL SETUP).

## 배포 범위 대조

- 코드 — 저자 구현 파일 · demo_packing.py [배포 파일](https://raw.githubusercontent.com/BoAi01/robopack/ac02a01006b50dbb7379b676ec5a622921875c5b/demo_packing.py)
- 가중치 — RoboPack의 촉각을 포함한 동역학 모델 체크포인트다. [배포 파일](https://raw.githubusercontent.com/BoAi01/robopack/ac02a01006b50dbb7379b676ec5a622921875c5b/trained_models/dec7_version32/epoch%3D97-step%3D25774-val_loss%3D0.00207-val_tac_loss%3D0.00330.ckpt)
- 데이터 — 저자 README의 표본 데이터 Drive 파일이 재검사에서 HTTP 404를 반환했다. 현재 받을 수 있는 대체 파일은 미확인이다. [저자 배포 안내](https://github.com/BoAi01/robopack/blob/ac02a01006b50dbb7379b676ec5a622921875c5b/README.md)
