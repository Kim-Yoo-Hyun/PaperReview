# Problem - Differentiable Robust Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p003.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p003.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND)): However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur due to environmental factors, model uncertainty, etc.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Deterministic model predictive control (MPC), while powerful, is often insufficient for effectively controlling autonomous systems in the real-world.
- **p. 1 / Abstract - extractive body cue:** Factors such as environmental noise and model error can cause deviations from the expected nominal performance.
- **p. 1 / Abstract - extractive body cue:** Robust MPC algorithms aim to bridge this gap between deterministic and uncertain control.
- **p. 1 / Abstract - extractive body cue:** However, these methods are often excessively difficult to tune for robustness due to the nonlinear and non-intuitive effects that controller parameters have on performance.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we first present a unifying perspective on differentiable optimization for control using the implicit function theorem (IFT), from which existing state-of-the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur due to environmental ...
- **p. 2 / II. MATHEMATICAL BACKGROUND - extractive body cue:** However, in practice, the system under study is subject to large dynamical uncertainty through effects such as unmodeled physics, random noise, etc., that results in ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur ... | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | Safety is enforced through the use of discrete barrier states [3], which enables scalable constraint satisfaction such that safe planning and control ... | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF body |
| State / latent | Safety, enforced, through, discrete, barrier, states, enables, scalable, constraint, satisfaction | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | address, shortcoming, tube-based, MPC, augments, nominal, controller, feedback | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: Safety, enforced, through, discrete, barrier, states, enables, scalable, constraint, satisfaction | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: main, contribution, development, novel, differentiable, tube-based, MPC, DT-MPC | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | tracking or interaction error; cue terms: Algorithm, Differentiable, Optimal, Control, DOC, Input, Derivatives, equivalently | p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 1 (I. INTRODUCTION) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / II. MATHEMATICAL BACKGROUND - extractive body cue:** However, in practice, the system under study is subject to large dynamical uncertainty through effects such as unmodeled physics, random noise, etc., that results in ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** A potential failure mode of nominal MPC when applied for the control of the true system is safety violations caused by this large predictive error ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** This approach is inherently robust to small uncertainty providing one explanation for the success of nominal MPC in practice, even when Problem 1 is not ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 4 (II. MATHEMATICAL BACKGROUND)): The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of ...
- **p. 1 / Abstract - extractive body cue:** Drawing parallels with differential dynamic programming, the IFT enables the derivation of an efficient differentiable optimal control framework.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of control algorithms that explicitly account for unknown disturbances in the dynamics and guarantee robustness.
- **p. 4 / II. MATHEMATICAL BACKGROUND - extractive body cue:** From the safe MPC via barrier methods perspective, the proposed work provides a novel expansion of the works [3], [14] and [19] to a tube-based ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | The results in Table I show that, while NT-MPC fails to reach the target in the majority of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | While the deterministic nominal trajectory reaches the target state during every trial, the ancillary controller cannot keep up ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Fig. 4: Controlled Dubins vehicle trajectories subject to large noise. NT-MPC trajectories diverge from the nominal trajec- tory ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND), interface p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND), objective p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of the problem [43]. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of the implicit function theorem, 2) ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number of failures even when controlled ... (p. 10, V. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
