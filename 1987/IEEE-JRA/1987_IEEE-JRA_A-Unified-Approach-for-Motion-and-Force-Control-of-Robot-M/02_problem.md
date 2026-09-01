# Problem - A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://cs.stanford.edu/group/manips/publications.html; PDF retrieval source: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 3 (I. Inrropucrion)): The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 1 / Abstract - extractive body cue:** Fist, issues related to the description of end-effector tasks that involve constrained motion and active force contro are discussed. ‘The fundamentals of the operational space ...
- **p. 1 / Abstract - extractive body cue:** The extension of this formulation to redundant manipulator systems is also presented, constructing the end-effector equations of ‘motion and describing their behavior with respect to ...
- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** configuration, the manipulator is treated as ame ‘redundant with respect tothe motion ofthe end-effector in the subspace ‘of operational space orthogonal to the singular direction.
- **p. 1 / I. Inrropucrion - extractive body cue:** The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.
- **p. 1 / I. Inrropucrion - extractive body cue:** Obviously, these characteristics cannot be found in the manipulator joint space dynamic model, which only provides a description of the interaction between joint motions.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered. | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector. | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF |
| State / latent | However, task, specification, motion, contact, forces, dynamics, force, sensing, feedback | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | vectors, total, force, moment, applied, maintain, imposed, constraints | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: However, task, specification, motion, contact, forces, dynamics, force, sensing, feedback | p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: development, dealing, problems, arising, kinematic, framework, analysis, control | p. 1 (Abstract), p. 1 (Abstract), p. 3 (I. Inrropucrion) |
| Objective / loss / cost | tracking or interaction error; cue terms: number, degrees, freedom, constrained, end-effector, given, difference, between | p. 2 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 1 (Abstract), p. 2 (I. Inrropucrion), p. 3 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (I. Inrropucrion), p. 3 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 5 (IV. Exp-Errecror Morton Controt), p. 7 (V. Constnainep Motion Operarions), p. 6 (V. Constnainep Motion Operarions) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. Inrropucrion - extractive body cue:** Obviously, these characteristics cannot be found in the manipulator joint space dynamic model, which only provides a description of the interaction between joint motions.
- **p. 2 / I. Inrropucrion - extractive body cue:** Tl, GeneRALizeD Task SpEciricaTion MarRices
- **p. 2 / I. Inrropucrion - extractive body cue:** In this paper, a new approach for dealing with the problem of kinematic singularities within the operational space framework is presented.
- **p. 3 / I. Inrropucrion - extractive body cue:** First, let us consider the case of nonredundant manipulators, where a set of operational coordinates can be selected asa system of generalized coordinates for the ...

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (Abstract), p. 3 (I. Inrropucrion)): These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn

- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 3 / I. Inrropucrion - extractive body cue:** This allows a more efficient implementation of the control system for real-time operations.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | ‘The configuration of a redundant manipulator cannot be specified by a set of parameters that only describes the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | ‘manipulator, and the dynamic behavior of the entire redundant system cannot be represented by a dynamic model in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Within this framework of control and at the level ‘f the uncoupled system linear, nonlinear, robust [32], and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 5 (IV. Exp-Errecror Morton Controt). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 3 (I. Inrropucrion), interface p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 5 (IV. Exp-Errecror Morton Controt), objective p. 2 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 1 (Abstract), p. 2 (I. Inrropucrion), p. 3 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
