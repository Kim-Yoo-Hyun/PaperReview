# Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2510.19974.
> PDF retrieval source: https://arxiv.org/pdf/2510.19974. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, contact-rich manipulation, model predictive control, non-prehensile manipulation
- Official paper: https://arxiv.org/abs/2510.19974
- Full-text retrieval: https://arxiv.org/pdf/2510.19974
- Code/Project: https://dairlab.github.io/push-anything
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 control 문제를 이해하기 위해 읽는다. 본문은 Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number of contacts.를 문제로 두고, We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Non-prehensile manipulation of diverse objects remains a core challenge in robotics, driven by unknown physical properties and the complexity of contact-rich interactions.
- **p. 1 / Abstract - extractive body cue:** Recent advances in contact-implicit model predictive control (CI-MPC), with contact reasoning embedded directly in the trajectory optimization, have shown promise in tackling the task efficiently ...
- **p. 1 / Abstract - extractive body cue:** However, demonstrations have been limited to narrowly curated examples.
- **p. 1 / Abstract - extractive body cue:** In this work, we showcase the broader capabilities of CI-MPC through precise planar pushing tasks over a wide range of object geometries, including multi-object domains.
- **p. 1 / Abstract - extractive body cue:** These scenarios demand reasoning over numerous inter-object and object-environment contacts to strategically manipulate and de-clutter the environment, which was intractable for prior CI-MPC methods.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this limitation, Venkatesh, Bianchini et al.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.
- **p. 3 / IV. METHODS - extractive body cue:** Our framework operates in two phases.
- **p. 3 / IV. METHODS - extractive body cue:** We present the Push Anything framework (Fig.
- **p. 4 / IV. METHODS - extractive body cue:** (4d) Our method, C3+, seeks a more efficient solution than solving with an MIQP.
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** Hybrid models capture these behaviors by switching dynamics depending on the active contact mode.
- **p. 4 / IV. METHODS - extractive body cue:** While using linearized terms, this model preserves the multi-modal nature of contact dynamics through the complementarity constraint (3b).
- **p. 4 / IV. METHODS - extractive body cue:** The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input bounds (5e). | joint/task state, reference와 sensor feedback | p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics) |
| State/latent | comprises, feasible, satisfying, coupled, constraints, across, time, linear, dynamics, slack-variable, equality, initial | state estimate, task-space error와 control decision | p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics) |
| Output/action | A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx is the state, uk ∈Rnu the control ... | torque, force, velocity 또는 position command | p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS) |
| Objective/outcome | Combining this LCS model with a standard quadratic cost function yields a Quadratic Program with Complementarity Constraints (QPCC), a well-known class of non-convex optimization problems that can be reformulated into a MixedInteger ... | tracking, stability, constraint satisfaction과 contact behavior | p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.
- **p. 3 / IV. METHODS - extractive body cue:** Our framework operates in two phases.
- **p. 3 / IV. METHODS - extractive body cue:** We present the Push Anything framework (Fig.
- **p. 4 / IV. METHODS - extractive body cue:** (4d) Our method, C3+, seeks a more efficient solution than solving with an MIQP.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive body cue:** Under the tight tolerance, our method achieved a 92.5% success rate (210/227), with time-to-goal statistics for both tight and loose tolerances reported in Table II.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive body cue:** Each experiment was run until 10 successful trials were achieved.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** 7, this results in 16 contact pairs, yielding λ ∈R64.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Embodiment/environment | 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained. | hardware/simulator version and reset protocol | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Dataset/benchmark | The few outliers for the chicken broth and milk bottle occurred when the robot took longer to bring the objects back into reach, while the clamp's numerous outliers are better explained by ... | role, split, size and leakage | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 6 (V. HARDWARE EXPERIMENTS) |
| Metric | Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon to enable precise multi-object manipulation. • Hardware validation: ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Baseline/ablation | For the Push T task, our framework achieves a mean time-to-goal of 26.9 s, improving upon prior work [4] at 30.5 s by 3.5 s (about 11.5%) while being more broadly applicable. | fair input/data/compute/action matching | p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. LIMITATIONS AND FUTURE WORK - extractive body cue:** Another limitation is we model all objects with identical mass and inertia.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive body cue:** All failures occurred when an object moved beyond the robot's reach.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** We predefine contact geometries, but contact point pairs and their corresponding normals are determined dynamically via collision detection at each control loop.

## Why Read It

Manipulation, contact, tactile, and dexterity의 control 문제를 이해하기 위해 읽는다. 본문은 Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number of contacts.를 문제로 두고, We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), p. 4 (IV. METHODS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
