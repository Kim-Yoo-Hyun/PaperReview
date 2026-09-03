# Problem - Control-Limited Differential Dynamic Programming

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2014.6907001; PDF retrieval source: https://roboti.us/lab/papers/TassaICRA14.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define complex task trajectories, but this is difficult to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Trajectory optimizers are a powerful class of methods for generating goal-directed robot motion.
- **p. 1 / Abstract - extractive body cue:** Differential Dynamic Programming (DDP) is an indirect method which optimizes only over the unconstrained control-space and is therefore fast enough to allow real-time control of ...
- **p. 1 / Abstract - extractive body cue:** Although indirect methods automatically take into account state constraints, control limits pose a difficulty.
- **p. 1 / Abstract - extractive body cue:** This is particularly problematic when an expensive robot is strong enough to break itself.
- **p. 1 / Abstract - extractive body cue:** In this paper, we demonstrate that simple heuristics used to enforce limits (clamping and penalizing) are not efficient in general.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define complex task trajectories, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In that context the problem is transcribed into a generic sequential quadratic programming (SQP) which easily admits both equality and inequality constraints.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define ... | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | (5a) This is a locally-linear feedback policy with k ≜-Q-1 uuQu and K ≜-Q-1 uuQux (5b) the feed-forward modification and feedback gain ... | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF body |
| State / latent | locally-linear, feedback, policy, Q-1, uuQu, uuQux, feed-forward, modification, gain, matrix | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | idea, behind, task-function, operational-space, approaches, instead, working, configuration | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: locally-linear, feedback, policy, Q-1, uuQu, uuQux, feed-forward, modification, gain, matrix | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: Finally, Section, describes, illustrating, usefulness, experimentally, simulation, simplistic | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | tracking or interaction error; cue terms: Trajectory, optimization, process, finding, statecontrol, sequence, locally, minimizes | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 3 (III. CONTROL LIMITS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 4 (III. CONTROL LIMITS) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 4 (IV. RESULTS), p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** In that context the problem is transcribed into a generic sequential quadratic programming (SQP) which easily admits both equality and inequality constraints.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we consider the solution of controlconstrained problems using indirect methods.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We characterize the boxconstrained control problem in Section III, along with the proposed original solution.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Finally, Section IV describes the results, illustrating the usefulness of our approach.

- **p. 2 / I. INTRODUCTION - extractive body cue:** We show experimentally in simulation that simplistic ways of handling them are inefficient and detrimental to convergence.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (C. Line Search). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (C. Line Search), objective p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 3 (III. CONTROL LIMITS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In that context the problem is transcribed into a generic sequential quadratic programming (SQP) which easily admits both equality and inequality constraints. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Finally, Section IV describes the results, illustrating the usefulness of our approach. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** A running cost is added to penalize cartesian distance from the origin ℓ(x) = 0.01(z(x,px) + z(y,py)) This term encourages parking maneuvers which do not take the car far from ... (p. 5, IV. RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
