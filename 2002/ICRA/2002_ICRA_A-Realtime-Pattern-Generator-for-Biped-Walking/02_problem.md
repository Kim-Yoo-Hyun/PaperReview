# Problem - A Realtime Pattern Generator for Biped Walking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2002.1013335; PDF retrieval source: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 4 (1 Introduction)): Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing projects.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** For realtime walking control of a biped robot, we analyze the dynamics of a three-dimensional inverted pendulum whose motions are constrained onto an arbitrarily defined ...
- **p. 1 / Abstract - extractive body cue:** This analysis leads us a simple linear dynamics, the Three-Dimensional Linear Inverted Pendulum Mode (3D-LIPM).
- **p. 1 / Abstract - extractive body cue:** Geometric nature of trajectories under the 3D-LIPM is discussed, and an algorithm for walking pattern generation is presented.
- **p. 1 / Abstract - extractive body cue:** Experimental results of realtime walking control of a 12 d.o.f. biped robot HRP-2L using an input device such as a game pad are also shown.
- **p. 1 / 1 Introduction - extractive body cue:** Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing ...
- **p. 4 / 1 Introduction - extractive body cue:** 3.2 Pattern generation along a local axis Now the problem becomes a control of the motion along X or Y -axis for each step.
- **p. 1 / 1 Introduction - extractive body cue:** It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r). | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Tani, introduced, two-dimensional, version, dynamics, mode, Hara, Yokokawa | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Decision / output variable | joint/whole-body action; body terms: allows, separate, controller, design, sagittal, lateral, motions, simplifies | p. 1 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Derivation, Linear, Inverted, Pendulum, Mode, Motion, equation, When | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Success / guarantee | motion/task success and recovery | p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 4 / 1 Introduction - extractive body cue:** 3.2 Pattern generation along a local axis Now the problem becomes a control of the motion along X or Y -axis for each step.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction)): It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Although we assume an ideal robot, which can step towards any direction at all time, in the former ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 4 (1 Introduction), interface p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), objective p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
