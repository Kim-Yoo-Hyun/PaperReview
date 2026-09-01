# Problem - Expressive Whole-Body Control for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p107.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p107.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION)): The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on both of these two form factors tend to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Can we enable humanoid robots to generate rich, diverse, and expressive motions in the real world?
- **p. 1 / Abstract - extractive PDF cue:** We propose to learn a whole-body control policy on a human-sized robot to mimic human motions as realistic as possible.
- **p. 1 / Abstract - extractive PDF cue:** To train such a policy, we leverage the large-scale human motion capture data from the graphics community in a Reinforcement Learning framework.
- **p. 1 / Abstract - extractive PDF cue:** However, directly performing imitation learning with the motion capture dataset would not work on the real humanoid robot, given the large gap in degrees of ...
- **p. 1 / Abstract - extractive PDF cue:** Our method Expressive Whole-Body Control (ExBody) tackles this problem by encouraging the upper humanoid body to imitate a reference motion, while relaxing the imitation constraint ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on both of these ...
- **p. 3 / II. PROBLEM FORMULATION - extractive PDF cue:** However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | consider, humanoid, motion, control, learning, goalconditioned, motor, policy, where, goal | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | train, novel, controller, takes, reference, motion, root, movement | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: consider, humanoid, motion, control, learning, goalconditioned, motor, policy, where, goal | p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | joint/whole-body action; body terms: compare, applying, more, imitation, constraints, legged, motion, simulation | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: assume, rest, without, loss, generality, observation, action, space | p. 3 (II. PROBLEM FORMULATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (II. PROBLEM FORMULATION) |
| Success / guarantee | motion/task success and recovery | p. 7 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / II. PROBLEM FORMULATION - extractive PDF cue:** However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** While our current results focus on expressive humanoid control, we hope our approach can also shed some light on studying generalizable humanoid whole-body manipulation
- **p. 3 / II. PROBLEM FORMULATION - extractive PDF cue:** Specifically, in this work, we work with a relaxed problem where we exclude the joints and key points from the lower half of the body ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that relaxes the constraints indeed leads ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Auto recovery and initialization could be explored to reduce the cost of doing experiments. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | We introduce a method designed to enable a humanoid robot to track expressive upper body motions while ensuring ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Note that although Random Sample looks better than Motion Sample, the heatmap does not consider the sample density. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Why does not ExBody do full DoF tracking? | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION), interface p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 3 (II. PROBLEM FORMULATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
