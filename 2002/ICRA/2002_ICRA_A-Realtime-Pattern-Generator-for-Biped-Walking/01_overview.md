# A Realtime Pattern Generator for Biped Walking

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/ROBOT.2002.1013335.
> PDF retrieval source: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2002 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, bipedal locomotion, 3D linear inverted pendulum, real-time control
- Official paper: https://doi.org/10.1109/ROBOT.2002.1013335
- Full-text retrieval: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing projects.를 문제로 두고, It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** For realtime walking control of a biped robot, we analyze the dynamics of a three-dimensional inverted pendulum whose motions are constrained onto an arbitrarily defined ...
- **p. 1 / Abstract - extractive body cue:** This analysis leads us a simple linear dynamics, the Three-Dimensional Linear Inverted Pendulum Mode (3D-LIPM).
- **p. 1 / Abstract - extractive body cue:** Geometric nature of trajectories under the 3D-LIPM is discussed, and an algorithm for walking pattern generation is presented.
- **p. 1 / Abstract - extractive body cue:** Experimental results of realtime walking control of a 12 d.o.f. biped robot HRP-2L using an input device such as a game pad are also shown.
- **p. 1 / 1 Introduction - extractive body cue:** Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing ...
- **p. 4 / 1 Introduction - extractive body cue:** 3.2 Pattern generation along a local axis Now the problem becomes a control of the motion along X or Y -axis for each step.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a robot with limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.
- **p. 3 / 1 Introduction - extractive body cue:** Since the 3DLIPM is a dynamics under the central force field, the motion along Y ′ and X′ is also governed by the identical equations ...
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, it mainly relies on the accuracy of the model data [3, 5, 10, 14].
- **p. 2 / 1 Introduction - extractive body cue:** (11) Therefore, we have the same dynamics of Eq.
- **p. 4 / 1 Introduction - extractive body cue:** The initial body state (x(n) i , v(n) i ) and the final body state (x(n) f , v(n) f ) have the relationship given ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r). | proprioception, reference pose/motion, visual or language command | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero, input, considered | whole-body pose, balance/contact state와 skill/mode | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | 2 Derivation of 3D Linear Inverted Pendulum Mode 2.1 Motion equation of a 3D inverted pendulum When a biped robot is supporting its body on one leg, its dominant dynamics can be ... | tracking, balance, skill/task success와 recovery | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.
- **p. 6 / 4 Experiments - extractive body cue:** From the experimental results, the effectiveness of the proposed realtime walk generation method was confirmed.
- **p. 6 / 4 Experiments - extractive body cue:** The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was successfully ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 6: Two successive steps in the sagittal plane are illustrated. The body travels from B to D in the single-leg support phase, then moves ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Embodiment/environment | of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for the experiments. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Dataset/benchmark | The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was successfully performed. | role, split, size and leakage | p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Metric | In order to reduce the error between the desired ZMP trajectory and the actual ZMP, the horizontal position of the torso is adjusted. | definition, denominator, direction and uncertainty | p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Baseline/ablation | not recovered | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing projects.를 문제로 두고, It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
