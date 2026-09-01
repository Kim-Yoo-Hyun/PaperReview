# Problem - Planning Optimal Grasps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.1992.219918; PDF retrieval source: https://doi.org/10.1109/ROBOT.1992.219918. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper we will address the problem of planning optimal grasps.
- **p. 1 / Abstract - extractive body cue:** Two general optimality criteria, that consider the total finger force and the maximum finger force will be introduced and discussed.
- **p. 1 / Abstract - extractive body cue:** Moreover their formalization, using various metrics on a space of generalized forces, will be detailed.
- **p. 1 / Abstract - extractive body cue:** The geometric interpretation of the two criteria will lead to an efficient planning algorithm.
- **p. 1 / Abstract - extractive body cue:** An example of its use in a robotic environment equipped with two-jaw and three-jaw grippers will also be shown.
- **p. 1 / 1 Introduction - extractive body cue:** Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research.
- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Because of their intricate design, they are difficult to control and plan *Supported by the Italian Ministry for University and Scientific Research. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | The reaction torque rj is given by ~j x f , where Tj is the vector pointing from the center of mass ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | reaction, torque, given, where, vector, pointing, center, mass, object, point | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | case, state, hypothesis, magnitude, forces, contact, points, upper-bounded | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: reaction, torque, given, where, vector, pointing, center, mass, object, point | p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: section, four, introduce, discuss, quality, criteria, proposing, give | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | task/contact/pose objective; cue terms: first, concerned, finding, grasp, configurations, maximize, wrench, given | p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.1 Representing Anger forces) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (4 The Quality of Grasp), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |
| Success / guarantee | completion, contact success and robustness | p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** The geometrical aspects of grasping will be emphasized while the problem of controlling compliance between the object and the jaws is not considered.

## What the Paper Changes

PDF contribution framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): In section four, we introduce and discuss the quality criteria we are proposing.

- **p. 1 / 1 Introduction - extractive body cue:** We give a geometric interpretation of the criteria which unifies them, and allows simple algorithms for optimal grasp planning according to either criterion.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Figure 2: Three-jaw Gripper grasping a Polygonal Ob- ject In the case of a three fingered gripper there ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Given n contacts, we have the following definition: As we pointed out earlier, specifying g does not determine ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (2 Working hypotheses). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 4 (4.3 Minimizing the maximum Anger force), p. 3 (4.1 Representing Anger forces), p. 4 (4.3 Minimizing the maximum Anger force), p. 2 (2 Working hypotheses), objective p. 3 (4.1 Representing Anger forces), p. 3 (4.1 Representing Anger forces), p. 4 (4.1 Representing Anger forces).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
