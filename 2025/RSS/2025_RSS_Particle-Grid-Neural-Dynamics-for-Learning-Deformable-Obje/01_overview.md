# Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p036.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p036.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, deformable objects, dynamics, RGB-D, model-based planning
- Official paper: https://www.roboticsproceedings.org/rss21/p036.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p036.pdf
- Code/Project: https://kywind.github.io/pgnd
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

입자와 공간 격자를 결합한 신경 동역학 모델은 소수 시점 RGB-D 영상에서 변형 물체가 로봇 동작에 어떻게 반응하는지 학습한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p036.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Modeling the dynamics of deformable objects is ‘challenging due to their diverse physical properties and the
- **p. 1 / Abstract - extractive body cue:** ulty of estimating states from limited yisual information.
- **p. 1 / Abstract - extractive body cue:** We address these challenges with a neural dynamics framework that combines object particles and spatial grids in a hybrid representation.
- **p. 1 / Abstract - extractive body cue:** Our particle-grid model captures global shape and motion information while predicting dense particle movements,
- **p. 1 / Abstract - extractive body cue:** the 3D space to ensure spatial continuity and enhance learning ‘efficiency.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, developing dynamics models for deformable objects that are both accurate and generalizable remains a significant challenge.

## Core Idea

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By combining object particles with spatial grids, our framework parameterizes dynamics in both Lagrangian and Eulerian coordinates, drawing an analogy to physics-based deformable object simulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In deformable object manipulation, an accurate predictive object dynamics model enables model-based planning, policy evaluation, and real-to-sim asset generation.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The application of this model within a Model Predictive Control (MPC) framework is covered in Section IILE, An overview of our method is also provided ...
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ...
- **p. 5 / B. Model Components - extractive body cue:** We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** A detailed description of the model is provided in Section IIL-A and III-B, We introduce the data collection pipeline and the models training method in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes the kinematic states Of the particles as input and predicts a spatial velocity field at fixed grid points. | observation, uncertainty/risk estimate와 task command | p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling) |
| State/latent | takes, kinematic, states, particles, input, predicts, spatial, velocity, field, fixed, grid, points | safe set, recovery state 또는 constraint margin | p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 2 (A. Physics-Based Deformable Modeling) |
| Output/action | Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ‘encoder to extract particle features and predict ... | shielded, recovery 또는 safe action | p. 3 (B. Learning-Based Deformable Modeling), p. 2 (A. Physics-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling) |
| Objective/outcome | We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions. | task return과 violation/failure probability | p. 5 (B. Model Components), p. 5 (B. Model Components), p. 4 (B. Model Components) |

## Main Claims and Actual Contribution

- 입자로 물체 형상을 표현하고 격자에서 운동을 전달하며 Gaussian Splatting으로 행동에 따른 관측 영상을 렌더링한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p036.pdf#page=1) · [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p036.pdf#page=5)
- 로프·천 등에서 미관측 물체로의 동역학 일반화를 평가하고 학습한 모델로 목표 형상에 맞는 조작 행동을 계획했다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p036.pdf#page=1) · [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p036.pdf#page=5)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 9 (Figure/Table caption) |
| Embodiment/environment | ‘€) Box: Two robot arms are used to open and close shipping boxes. | hardware/simulator version and reset protocol | p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup) |
| Dataset/benchmark | With the robot end-effectors, and employs a Graph Neural Network (GNN) to predict particle motions. | role, split, size and leakage | p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup), p. 7 (A. Experiment Setup), p. 5 (IV. EXPERIMENTS) |
| Metric | Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve and the final success rate curve with respect ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (A. Experiment Setup), p. 7 (A. Experiment Setup) |
| Baseline/ablation | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 5 (B. Model Components)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, developing dynamics models for deformable objects that are both accurate and generalizable remains a significant challenge. (p. 1, I. INTRODUCTION).
- **Actual contribution:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 13: Additional Qualitative Comparisons on Dynamics Prediction. Given the initial states and actions (leftmost column), we present the prediction results of the MPM with parameter identification baseline, the GBND ... (p. 19, Figure/Table caption).
- **Explicit failure boundary:** For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, ... (p. 1, I. INTRODUCTION).

## 원문과 공개 자료

- 가중치 · PGND 로프 실험의 저장 모델 · experiments/log/rope/train/ckpt/100000.pt [배포 파일](https://huggingface.co/kaifz/pgnd-checkpoints/blob/893e8b9b2f443f8c98066f7eadca0dbf7d92851d/experiments/log/rope/train/ckpt/100000.pt)
- 코드 · 입자·격자 신경 동역학 모델 구현 · pgnd/sim/model.py [배포 파일](https://raw.githubusercontent.com/kywind/pgnd/06ef5dbbe9612b56aaee317c938dcf953074c05f/pgnd/sim/model.py)
- 데이터 · PGND 변형체 실험의 로프 자료 · data/rope/rope.tar [배포 파일](https://huggingface.co/datasets/kaifz/pgnd-dataset/blob/58932f8ac660a2cba3d880675181369a4dc66cbc/data/rope/rope.tar)
