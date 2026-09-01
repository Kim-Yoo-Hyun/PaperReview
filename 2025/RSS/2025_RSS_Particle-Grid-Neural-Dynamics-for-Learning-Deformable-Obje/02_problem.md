# Problem - Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p036.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p036.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Modeling the dynamics of deformable objects is ‘challenging due to their diverse physical properties and the
- **p. 1 / Abstract - extractive body cue:** ulty of estimating states from limited yisual information.
- **p. 1 / Abstract - extractive body cue:** We address these challenges with a neural dynamics framework that combines object particles and spatial grids in a hybrid representation.
- **p. 1 / Abstract - extractive body cue:** Our particle-grid model captures global shape and motion information while predicting dense particle movements,
- **p. 1 / Abstract - extractive body cue:** the 3D space to ensure spatial continuity and enhance learning ‘efficiency.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, developing dynamics models for deformable objects that are both accurate and generalizable remains a significant challenge.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | It takes the kinematic states Of the particles as input and predicts a spatial velocity field at fixed grid points. | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | takes, kinematic, states, particles, input, predicts, spatial, velocity, field, fixed | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | While, uses, hybrid, particle-grid, representation, similar, MPM, leverage | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: takes, kinematic, states, particles, input, predicts, spatial, velocity, field, fixed | p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 2 (A. Physics-Based Deformable Modeling) |
| Decision / output variable | filtered/recovery action u_safe; body terms: model, updates, particle, positions, predicted, velocities, perform, iterative | p. 3 (B. Learning-Based Deformable Modeling), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: apply, Model-Predictive, Path, Integral, MPPD, trajectory, optimization, algorithm | p. 4 (B. Model Components), p. 5 (B. Model Components), p. 5 (B. Model Components), p. 3 (B. Learning-Based Deformable Modeling) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (B. Model Components), p. 4 (B. Learning-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 9 (Figure/Table caption), p. 7 (A. Experiment Setup), p. 7 (A. Experiment Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, developing dynamics models for deformable objects that are both accurate and generalizable remains a significant challenge.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these methods face significant challenges: the effectiveness of message passing is highly sensitive to the spatial distribution and connectivity of the graph nodes, making ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.

## What the Paper Changes

PDF contribution framing (p. 3 (B. Learning-Based Deformable Modeling), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling)): The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing objects with 3D Gaussian Splatting ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By combining object particles with spatial grids, our framework parameterizes dynamics in both Lagrangian and Eulerian coordinates, drawing an analogy to physics-based deformable object simulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In deformable object manipulation, an accurate predictive object dynamics model enables model-based planning, policy evaluation, and real-to-sim asset generation.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The application of this model within a Model Predictive Control (MPC) framework is covered in Section IILE, An overview of our method is also provided ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 2 (A. Physics-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 2 (A. Physics-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling), objective p. 4 (B. Model Components), p. 5 (B. Model Components), p. 5 (B. Model Components), p. 3 (B. Learning-Based Deformable Modeling).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
