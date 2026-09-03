# Problem - HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/lpr/publication/he2025hover/; PDF retrieval source: https://research.nvidia.com/labs/lpr/publication/he2025hover/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): This is a non-trivial challenge, as each mode operates within a distinct command space, making direct integration impractical.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humanoid whole-body control requires adapting to diverse tasks such as navigation, loco-manipulation, and tabletop manipulation, each demanding a different mode of control.
- **p. 1 / Abstract - extractive body cue:** For example, navigation relies on root velocity or position tracking, while tabletop manipulation prioritizes upperbody joint angle tracking.
- **p. 1 / Abstract - extractive body cue:** Existing approaches typically train individual policies tailored to a specific command space, limiting their transferability across modes.
- **p. 1 / Abstract - extractive body cue:** We present the key insight that full-body kinematic motion imitation can serve as a common abstraction for all these tasks and provide generalpurpose motor skills ...
- **p. 1 / Abstract - extractive body cue:** Building on this, we propose HOVER (Humanoid Versatile Controller), a multi-mode policy distillation framework that consolidates diverse control modes into a unified policy.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This is a non-trivial challenge, as each mode operates within a distinct command space, making direct integration impractical.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This versatile command space covers most modes used in prior works [9, 10, 12, 13].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This is a non-trivial challenge, as each mode operates within a distinct command space, making direct integration impractical. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Using these oracle states, we query the oracle teacher policy πoracle(ˆat/sp-oracle t , sg-oracle t ) to obtain the reference action ˆat. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | oracle, states, query, teacher, policy, at/sp-oracle, sg-oracle, obtain, reference, action | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | student, policy, sp-student, sg-student, distilled, oracle, teacher, proprioception | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: oracle, states, query, teacher, policy, at/sp-oracle, sg-oracle, obtain, reference, action | p. 4 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD) |
| Decision / output variable | joint/whole-body action; body terms: summarize, contributions, threefold, present, HOVER, unified, neural, controller | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. METHOD) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: employ, proximal, policy, optimization, PPO, algorithm, maximize, cumulative | p. 4 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD) |
| Success / guarantee | motion/task success and recovery | p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENT), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** This versatile command space covers most modes used in prior works [9, 10, 12, 13].
- **p. 2 / I. INTRODUCTION - extractive body cue:** These shared skills enhance generalization, leading to better performance across all modes.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This design choice leverages the inherent adaptability and natural efficiency of human movements, providing the policy with rich motor priors that can be reused across ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (II. METHOD), p. 3 (II. METHOD), p. 1 (I. INTRODUCTION)): To summarize, our contributions are threefold: 1) we present HOVER, a unified neural controller for humanoid whole-body control supporting multiple control modes; 2) we show that, through policy distillation, HOVER ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we present HOVER, a unified neural controller for humanoid whole-body control that supports diverse control modes as shown in Figure 1, including ...
- **p. 3 / II. METHOD - extractive body cue:** In our framework, as shown in Figure 1, a one-hot masking vector is introduced to specify which components of the command space are activated for ...
- **p. 3 / II. METHOD - extractive body cue:** This space consists of two primary control regions-upper-body and lower-body control-and incorporates three distinct control modes: • Kinematic Position Tracking: target 3D positions of key ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: HOVER enables versatile humanoid control with a unified multi-mode command space.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Future work will explore further developing an automated mode-switching module for real-world applications. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 4 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD), objective p. 4 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** This is a non-trivial challenge, as each mode operates within a distinct command space, making direct integration impractical. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** To summarize, our contributions are threefold: 1) we present HOVER, a unified neural controller for humanoid whole-body control supporting multiple control modes; 2) we show that, through policy distillation, HOVER ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the reference motions). (p. 6, III. EXPERIMENT).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
