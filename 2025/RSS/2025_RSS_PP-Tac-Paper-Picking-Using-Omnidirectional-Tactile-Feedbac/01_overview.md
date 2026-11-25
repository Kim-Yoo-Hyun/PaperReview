# PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p056.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p056.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Pei Lin, Yuzhe Huang, Wanlin Li, Jianpeng Ma, Chenxi Xiao, Ziyuan Jiao
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, dexterous manipulation, deformable objects, force control, slip detection
- Official paper: https://www.roboticsproceedings.org/rss21/p056.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p056.pdf
- Code/Project: https://peilin-666.github.io/projects/PP-Tac/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

PP-Tac은 종이처럼 얇고 휘는 물체를 다지 손으로 집을 때 손끝의 전방향 촉각으로 미끄러짐을 감지하고 힘을 조절한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p056.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robots are inereasingly envisioned as human com- 1.
- **p. 1 / Abstract - extractive body cue:** Ivrropucrion anions, assisting with everyday tasks that offen involve manip
- **p. 1 / Abstract - extractive body cue:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly ...
- **p. 1 / Abstract - extractive body cue:** and fabric. ‘These' limitations stem from the lack of robust perception techniques for reliable state estimation under diverse often involving the grasp of thin, deformable ...
- **p. 1 / Abstract - extractive body cue:** fal conditions and the absence of planning methods capa- paper and fabric [51].
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Although creases or irregularities in the ‘material can sometimes provide grasping points, a particularly challenging scenario arises when the object is extremely flat and lacks ...

## Core Idea

- **p. 5 / V. POLICY LEARNING FOR PAPER-PICKING - extractive body cue:** To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating ...
- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** These evaluations showcase the robustness and adaptability of our approach,
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** This research introduces a novel approach to tackle the paper picking problem that was previously unexplored.
- **p. 6 / A. Implementation Details - extractive body cue:** Our diffusion policy is implemented as a fourlayer Transformer encoder with a latent dimension of 512 and four attention heads.
- **p. 6 / B. PP-Tac Policy - extractive body cue:** Such an overparameterized input allows the network to extract more robust and expressive latent features for the diffusion policy.
- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** trajectory with compliant finger control via tactile feedback; (3) Model based force tracking": combines the PP-Tac-lerived hand trajectory with compliant finger control via tactile feedback; ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2) Diffusion Policy Training: Train a policy fon this dataset t0 infer motions from tactile feedback and proprioceptive states, ensuring generalization to real-world robotic systems, | tactile image/force, vision과 proprioceptive history | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS) |
| State/latent | Diffusion, Policy, Training, Train, dataset, infer, motions, tactile, feedback, proprioceptive, states, ensuring | contact geometry, force state 또는 latent dynamics | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details) |
| Output/action | trajectory with compliant finger control via tactile feedback; (3) Model based force tracking": combines the PP-Tac-lerived hand trajectory with compliant finger control via tactile feedback; (4) Non-disturbance: grasp using our dextero ... | grasp/contact action, force command 또는 object motion | p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details), p. 6 (B. PP-Tac Policy) |
| Objective/outcome | reconstruction loss of 0.35 mm, and a median loss of 0.28 mm, with 60% of reconstruction losses below 0.3 mm. | slip/contact success, force/pose error와 robustness | p. 7 (B. Depth Reconstruction of VBTS), p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 8 (B. Depth Reconstruction of VBTS) |

## Main Claims and Actual Contribution

- 반구형 R-Tac 센서와 미끄럼 피드백을 사용하고, 합성 핀치 궤적으로 손과 손가락을 함께 제어하는 확산 정책을 학습했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p056.pdf#page=1) · [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p056.pdf#page=5)
- 재료·두께·강성이 서로 다른 얇은 물체를 실제 손으로 집는 성공률을 측정했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p056.pdf#page=1) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p056.pdf#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS) |
| Embodiment/environment | of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support further research and. community development, | hardware/simulator version and reset protocol | p. 2 (4) We provide a full implementation and systematic evaluation), p. 6 (A. Grasp Motion Dataset Synthesis) |
| Dataset/benchmark | We synthesize grasping motions via trajectory optimization in simulation, eliminating the need for complex teleoperation interfaces. | role, split, size and leakage | p. 2 (4) We provide a full implementation and systematic evaluation), p. 6 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis) |
| Metric | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 5 (A. Grasp Motion Dataset Synthesis), p. 7 (Figure/Table caption) |
| Baseline/ablation | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We also compare our system with various manipulators to highlight its advantages and limitations (Section VI-D).
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Inference pipeline of the proposed PP-Tae policy. Conditioned on robot proprioception and the target force that needs to be exerted, PP-Tac can infer ...
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** Slip) and the final success rate (Suce.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** The average number of slip events detected (No.
- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** Additionally, the increase in material stiffness also led to a higher number of detected slips.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT), p. 6 (A. Implementation Details), p. 6 (B. PP-Tac Policy)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces. (p. 4, IV. PROBLEM STATEMENT).
- **Actual contribution:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly within household environments (3) with ... (p. 1, Abstract).
- **Evaluation boundary:** Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** However, vision-based methods often struggle in real-world DOM tasks due to variability in object appearance, unknown physical properties, visual occlusions [25, 6], and inconsistent lighting conditions [48, 22) ‘These limitations ... (p. 2, A. Deformable Object Manipulation).

## 원문과 공개 자료

- RSS 표제면에서 Wanlin Li, Jianpeng Ma, Chenxi Xiao의 순서를 확인했다. [표제면](https://www.roboticsproceedings.org/rss21/p056.pdf#page=1)
- 가중치 · R-Tac 센서 보정 훈련의 모델 파일 · Calibration/training/checkpoint/20241031/ckpt/model_18 [배포 파일](https://raw.githubusercontent.com/bigai-ai/PP-Tac/e4dc92daaf1cb31098316b7253821bcbbf77d095/Calibration/training/checkpoint/20241031/ckpt/model_18)
- 코드 · R-Tac 센서 보정 코드. 전체 집기 정책과 범위를 구별 · Calibration/3SensorCalibration.py [배포 파일](https://raw.githubusercontent.com/bigai-ai/PP-Tac/e4dc92daaf1cb31098316b7253821bcbbf77d095/Calibration/3SensorCalibration.py)
- 데이터 · R-Tac 센서 외부 보정의 촬영 표본 · Calibration/sensor1/calib_extrinsic/01_02_06_14_22.png [배포 파일](https://raw.githubusercontent.com/bigai-ai/PP-Tac/e4dc92daaf1cb31098316b7253821bcbbf77d095/Calibration/sensor1/calib_extrinsic/01_02_06_14_22.png)
