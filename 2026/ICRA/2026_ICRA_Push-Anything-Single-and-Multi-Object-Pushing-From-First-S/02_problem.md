# Problem - Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2510.19974; PDF retrieval source: https://arxiv.org/pdf/2510.19974. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number of contacts.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Non-prehensile manipulation of diverse objects remains a core challenge in robotics, driven by unknown physical properties and the complexity of contact-rich interactions.
- **p. 1 / Abstract - extractive PDF cue:** Recent advances in contact-implicit model predictive control (CI-MPC), with contact reasoning embedded directly in the trajectory optimization, have shown promise in tackling the task efficiently ...
- **p. 1 / Abstract - extractive PDF cue:** However, demonstrations have been limited to narrowly curated examples.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we showcase the broader capabilities of CI-MPC through precise planar pushing tasks over a wide range of object geometries, including multi-object domains.
- **p. 1 / Abstract - extractive PDF cue:** These scenarios demand reasoning over numerous inter-object and object-environment contacts to strategically manipulate and de-clutter the environment, which was intractable for prior CI-MPC methods.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address this limitation, Venkatesh, Bianchini et al.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially ... | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and ... | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF |
| State / latent | comprises, feasible, satisfying, coupled, constraints, across, time, linear, dynamics, slack-variable | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | increases, number, variables, constraints, often, leads, better-conditioned, problems | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: comprises, feasible, satisfying, coupled, constraints, across, time, linear, dynamics, slack-variable | p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: introduce, Push, Anything, manipulation, pipeline, real-time, planar, pushing | p. 1 (I. INTRODUCTION), p. 3 (IV. METHODS), p. 3 (IV. METHODS) |
| Objective / loss / cost | tracking or interaction error; cue terms: Combining, LCS, model, standard, quadratic, cost, function, yields | p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 5 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 5 (IV. METHODS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (IV. METHODS), p. 5 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 2 (Figure/Table caption), p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address this limitation, Venkatesh, Bianchini et al.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 4 (IV. METHODS)): We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.

- **p. 3 / IV. METHODS - extractive PDF cue:** Our framework operates in two phases.
- **p. 3 / IV. METHODS - extractive PDF cue:** We present the Push Anything framework (Fig.
- **p. 4 / IV. METHODS - extractive PDF cue:** (4d) Our method, C3+, seeks a more efficient solution than solving with an MIQP.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Another limitation is we model all objects with identical mass and inertia. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | All failures occurred when an object moved beyond the robot's reach. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We predefine contact geometries, but contact point pairs and their corresponding normals are determined dynamically via collision detection ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), objective p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 5 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 5 (IV. METHODS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
