# Planning Optimal Grasps

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/ROBOT.1992.219918.
> PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. Reading tracker status/evidence was not changed.

- Year/Venue: 1992 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, Grasp Planning, manipulation, contact
- Official paper: https://doi.org/10.1109/ROBOT.1992.219918
- Full-text retrieval: https://doi.org/10.1109/ROBOT.1992.219918
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research.를 문제로 두고, In section four, we introduce and discuss the quality criteria we are proposing.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper we will address the problem of planning optimal grasps.
- **p. 1 / Abstract - extractive body cue:** Two general optimality criteria, that consider the total finger force and the maximum finger force will be introduced and discussed.
- **p. 1 / Abstract - extractive body cue:** Moreover their formalization, using various metrics on a space of generalized forces, will be detailed.
- **p. 1 / Abstract - extractive body cue:** The geometric interpretation of the two criteria will lead to an efficient planning algorithm.
- **p. 1 / Abstract - extractive body cue:** An example of its use in a robotic environment equipped with two-jaw and three-jaw grippers will also be shown.
- **p. 1 / 1 Introduction - extractive body cue:** Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research.
- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** In section four, we introduce and discuss the quality criteria we are proposing.
- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at ...
- **p. 1 / 2 Working hypotheses - extractive body cue:** In this model, fingers can exert any force pointing into the friction cone at the point of contact.
- **p. 2 / 2 Working hypotheses - extractive body cue:** Hence we have an immediate representation of each point contact force exerted by the fingers.
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** 4.4 In this case we state the hypothesis that the sum of the magnitude of the forces at the contact points is upper-bounded, and we ...
- **p. 4 / 4.3 Minimizing the maximum Anger force - extractive body cue:** The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object ...
- **p. 2 / 4 The Quality of Grasp - extractive body cue:** Then a precise definition for magnitude of the applied forces will be given in the next.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass of the object to the point contact where the force ... | RGB-D/point cloud, object state와 contact/task observation | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces) |
| State/latent | reaction, torque, given, where, vector, pointing, center, mass, object, point, contact, force | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Output/action | Of course, there can still be some directions where the reaction wrench can be greater, but we want to be assured we get a lower bound over all directions. | grasp, pose, force 또는 end-effector trajectory | p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (2 Working hypotheses) |
| Objective/outcome | The first is concerned with finding the grasp configurations that maximize the wrench, given independent force limits, i.e. that minimize the worst-case force applied at any point contact. | task completion, contact success, pose/force error와 generalization | p. 3 (4.1 Representing Anger forces), p. 2 (4 The Quality of Grasp), p. 2 (4 The Quality of Grasp) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** In section four, we introduce and discuss the quality criteria we are proposing.
- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** We therefore want to guarantee a level of performance as judged by the local quality measure over all possible wrenches, and this is the measure ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 3 (4.1 Representing Anger forces) |
| Embodiment/environment | Avoiding large forces minimizes the deformation of both the object and the jaws. | hardware/simulator version and reset protocol | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses) |
| Dataset/benchmark | Given a grasp configuration (i.e. a set of point contacts on the object), Q is defined as follows: Q = minLQw W We take the minimum because we usually have no control ... | role, split, size and leakage | p. 2 (4 The Quality of Grasp), p. 2 (2 Working hypotheses), p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces) |
| Metric | Without loss of generality, we choose llwll so that 11g11 = 1. | definition, denominator, direction and uncertainty | p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Baseline/ablation | Some grasp configurations can be better than others in the sense that they can balance every external force, without applying too large finger forces. | fair input/data/compute/action matching | p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), p. 2 (4 The Quality of Grasp) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there is an additional test in order to ...
- **p. 3 / 4.1 Representing Anger forces - extractive body cue:** Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine the actual wrench acting on the object ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research.를 문제로 두고, In section four, we introduce and discuss the quality criteria we are proposing.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (4.1 Representing Anger forces), p. 1 (2 Working hypotheses), p. 2 (2 Working hypotheses), p. 4 (4.3 Minimizing the maximum Anger force) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
