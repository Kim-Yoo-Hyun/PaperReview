# Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p036.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p036.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, deformable objects, dynamics, RGB-D, model-based planning
- Official paper: https://www.roboticsproceedings.org/rss21/p036.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p036.pdf
- Code/Project: https://kywind.github.io/pgnd
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, video-based predictive ...를 문제로 두고, The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing objects with 3D Gaussian Splatting and int ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By combining object particles with spatial grids, our framework parameterizes dynamics in both Lagrangian and Eulerian coordinates, drawing an analogy to physics-based deformable object simulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In deformable object manipulation, an accurate predictive object dynamics model enables model-based planning, policy evaluation, and real-to-sim asset generation.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The application of this model within a Model Predictive Control (MPC) framework is covered in Section IILE, An overview of our method is also provided ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve and ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ Can the model improve the performance of 3D actionconditioned video prediction and model-based planning?

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, video-based predictive ...를 문제로 두고, The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing objects with 3D Gaussian Splatting and int ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 5 (B. Model Components) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
