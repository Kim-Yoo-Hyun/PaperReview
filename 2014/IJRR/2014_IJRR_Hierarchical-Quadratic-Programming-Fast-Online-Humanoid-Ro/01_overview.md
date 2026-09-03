# Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1177/0278364914521306.
> PDF retrieval source: https://gepettoweb.laas.fr/uploads/Publications/2014_escande_ijrr.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2014 / IJRR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, whole-body control, hierarchical QP, task hierarchy
- Official paper: https://doi.org/10.1177/0278364914521306
- Full-text retrieval: https://gepettoweb.laas.fr/uploads/Publications/2014_escande_ijrr.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem.를 문제로 두고, We propose an original decomposition that encompasses the hierarchy among the constraints.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Hierarchical least-square optimization is often used in robotics to inverse a direct function when multiple incompatible objectives are involved.
- **p. 1 / Abstract - extractive body cue:** Typical examples are inverse kinematics or dynamics.
- **p. 1 / Abstract - extractive body cue:** The objectives can be given as equalities to be satisfied (e.g. point-to-point task) or as areas of satisfaction (e.g. the joint range).
- **p. 1 / Abstract - extractive body cue:** This paper proposes a complete solution to solve multiple least-square quadratic problems of both equality and inequality constraints ordered into a strict hierarchy.
- **p. 1 / Abstract - extractive body cue:** Our method is able to solve a hierarchy of only equalities ten times faster than the iterativeprojection hierarchical solvers and can consider inequalities at any ...
- **p. 2 / 1 Introduction - extractive body cue:** An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem.
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, it is difficult to relax a DOF that was clamped.

## Core Idea

- **p. 6 / 1 Introduction - extractive body cue:** We propose an original decomposition that encompasses the hierarchy among the constraints.
- **p. 6 / 1 Introduction - extractive body cue:** 2 Equality hierarchical quadratic program We propose in this section a method to solve a hierarchy of linear equality in the least-square sense.
- **p. 5 / 1 Introduction - extractive body cue:** However, this expressivity reduction enables to obtain very impressive result for walking, jumping or, as shown in [Mordatch et al., 2012], for planning contacts and ...
- **p. 3 / 1 Introduction - extractive body cue:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) ...
- **p. 2 / 1 Introduction - extractive body cue:** A dedicated simplex solver was designed in [Isermann, 1982] for linear problem only.
- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** We prove here that each outer loop of Algorithm 3 terminates.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q. | proprioception, reference pose/motion, visual or language command | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | Consider, robot, defined, configuration, vector, whose, control, input, joint, velocity, evolution, image | whole-body pose, balance/contact state와 skill/mode | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Output/action | The evolution in the image space (or task space) with respect to the robot input is given by ˙e = J ˙q, with J = ∂e ∂q the task Jacobian. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | We note m the total number of constraints, and w = (∥w1∥, · · · , ∥wp∥). | tracking, balance, skill/task success와 recovery | p. 28 (B.2 Algorithm 3 termination), p. 28 (B.2 Algorithm 3 termination) |

## Main Claims and Actual Contribution

- **p. 6 / 1 Introduction - extractive body cue:** We propose an original decomposition that encompasses the hierarchy among the constraints.
- **p. 6 / 1 Introduction - extractive body cue:** 2 Equality hierarchical quadratic program We propose in this section a method to solve a hierarchy of linear equality in the least-square sense.
- **p. 5 / 1 Introduction - extractive body cue:** However, this expressivity reduction enables to obtain very impressive result for walking, jumping or, as shown in [Mordatch et al., 2012], for planning contacts and ...
- **p. 3 / 1 Introduction - extractive body cue:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) ...
- **p. 2 / 1 Introduction - extractive body cue:** A dedicated simplex solver was designed in [Isermann, 1982] for linear problem only.
- **p. 22 / 6.2.2 Results - extractive body cue:** Moreover, the numerical behavior is improved by limiting the number of iteration in the search loop.
- **p. 22 / 6.2.2 Results - extractive body cue:** The motion is composed of two parts: the robot first manipulates the wheel using one hand, then rotates the wheel using both hands with successive ...
- **p. 27 / 6.2.2 Results - extractive body cue:** The timing scores are summarized on Table 1.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 22 (6.2.2 Results), p. 22 (6.2.2 Results) |
| Embodiment/environment | The robot has to grasp a point object while looking at it and avoiding its joint limits and the collisions with the environment. | hardware/simulator version and reset protocol | p. 25 (6.2.2 Results), p. 22 (6.2.2 Results) |
| Dataset/benchmark | Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of the wheel. | role, split, size and leakage | p. 25 (6.2.2 Results), p. 22 (6.2.2 Results), p. 23 (6.2.2 Results), p. 24 (6.2.2 Results) |
| Metric | 24 and illustrate very well the hierarchical order: the task erh has priority over the three other ones, and is always accomplished: the error exponentially converges as imposed. | definition, denominator, direction and uncertainty | p. 27 (6.2.2 Results), p. 26 (6.2.2 Results), p. 26 (6.2.2 Results) |
| Baseline/ablation | 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without and with warm start. | fair input/data/compute/action matching | p. 21 (6.2.2 Results), p. 21 (6.2.2 Results), p. 22 (6.2.2 Results) |

## Explicit Limitations and Failure Boundary

- **p. 19 / 3.6 Conclusion - extractive body cue:** The ball is then placed back in front of the robot: the COM comes back to the 2We cannot compare the HQP with [De Lasa ...
- **p. 12 / 2.6 Conclusion - extractive body cue:** Adaptating the method for iHQP is done through the following changes: • using our eHQP solver instead of the eQP, obviously, to find the hierarchical ...
- **p. 13 / 2.6 Conclusion - extractive body cue:** As observed in [Kanoun et al., 2011], strongly active constraints cannot be deactivated at a next level.
- **p. 16 / 3.6 Conclusion - extractive body cue:** However, one cannot guarantee the number of necessary iterations to reach the optimum.
- **p. 16 / 3.6 Conclusion - extractive body cue:** However, we cannot yet guarantee that the solver answers in a bounded number of iterations.
- **p. 17 / 3.6 Conclusion - extractive body cue:** The collision avoidance is enforced by the task ecoll by imposing the distance between a body of the robot and an object to be positive.
- **p. 17 / 3.6 Conclusion - extractive body cue:** In that case, the pair of bodies and object to check has to be specified (no systematic collision checking was performed here, it should be ...

## Why Read It

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem.를 문제로 두고, We propose an original decomposition that encompasses the hierarchy among the constraints.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 28 (B.2 Algorithm 3 termination) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (32 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem. (p. 2, 1 Introduction).
- **Actual contribution:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) in the next sections. (p. 3, 1 Introduction).
- **Evaluation boundary:** For this last experiment, only the real-time version of the HQP was run by the physical robot, the other scores being obtained offline on a similar computer. (p. 27, 6.2.2 Results).
- **Explicit failure boundary:** Contrary to the previous simulation, the joints do not systematically remain on the exact limits since the robot is moving to follow the rotation of the wheel. (p. 23, 6.2.2 Results).
