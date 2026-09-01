# Problem - Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1177/0278364914521306; PDF retrieval source: https://gepettoweb.laas.fr/uploads/Publications/2014_escande_ijrr.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction)): An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Hierarchical least-square optimization is often used in robotics to inverse a direct function when multiple incompatible objectives are involved.
- **p. 1 / Abstract - extractive body cue:** Typical examples are inverse kinematics or dynamics.
- **p. 1 / Abstract - extractive body cue:** The objectives can be given as equalities to be satisfied (e.g. point-to-point task) or as areas of satisfaction (e.g. the joint range).
- **p. 1 / Abstract - extractive body cue:** This paper proposes a complete solution to solve multiple least-square quadratic problems of both equality and inequality constraints ordered into a strict hierarchy.
- **p. 1 / Abstract - extractive body cue:** Our method is able to solve a hierarchy of only equalities ten times faster than the iterativeprojection hierarchical solvers and can consider inequalities at any ...
- **p. 2 / 1 Introduction - extractive body cue:** An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main problem.
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, it is difficult to relax a DOF that was clamped.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | An improvement is done by temporarily relaxing the most distant DOF in [Mansard and Chaumette, 2009], but that cannot solve the main ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | Consider, robot, defined, configuration, vector, whose, control, input, joint, velocity | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | observation, exploited, Escande, constitute, preliminary, version, fasten, computation | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Consider, robot, defined, configuration, vector, whose, control, input, joint, velocity | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Decision / output variable | joint/whole-body action; body terms: original, decomposition, encompasses, hierarchy, among, constraints, Equality, hierarchical | p. 6 (1 Introduction), p. 6 (1 Introduction), p. 5 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: note, total, number, constraints, first, outer, iteration, begins | p. 28 (B.2 Algorithm 3 termination), p. 28 (B.2 Algorithm 3 termination) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 28 (B.2 Algorithm 3 termination), p. 28 (B.2 Algorithm 3 termination) |
| Success / guarantee | motion/task success and recovery | p. 27 (6.2.2 Results), p. 26 (6.2.2 Results), p. 26 (6.2.2 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Moreover, it is difficult to relax a DOF that was clamped.
- **p. 4 / 1 Introduction - extractive body cue:** The form (2) can be extended to inequalities by introducing an additional variable w, named the slack variable, in the parameter vector: min x,w ∥w ...
- **p. 5 / 1 Introduction - extractive body cue:** However, both methods [Kanoun et al., 2011] and [De Lasa et al., 2010] have the same intrinsic problem due to the nature of the underlying ...
- **p. 3 / 1 Introduction - extractive body cue:** A simplified version was proposed in [De Lasa et al., 2010], that improves the computation cost but prevents the inclusion of inequality except at the ...

## What the Paper Changes

PDF contribution framing (p. 6 (1 Introduction), p. 6 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction)): We propose an original decomposition that encompasses the hierarchy among the constraints.

- **p. 6 / 1 Introduction - extractive body cue:** 2 Equality hierarchical quadratic program We propose in this section a method to solve a hierarchy of linear equality in the least-square sense.
- **p. 5 / 1 Introduction - extractive body cue:** However, this expressivity reduction enables to obtain very impressive result for walking, jumping or, as shown in [Mordatch et al., 2012], for planning contacts and ...
- **p. 3 / 1 Introduction - extractive body cue:** Before defining the objectives and specificities of our approach, we rewrite briefly the main resolution schemes for hierarchy of quadratic problems (with and without inequalities) ...
- **p. 2 / 1 Introduction - extractive body cue:** A dedicated simplex solver was designed in [Isermann, 1982] for linear problem only.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 19 | The ball is then placed back in front of the robot: the COM comes back to the 2We ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Adaptating the method for iHQP is done through the following changes: • using our eHQP solver instead of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | As observed in [Kanoun et al., 2011], strongly active constraints cannot be deactivated at a next level. | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | However, one cannot guarantee the number of necessary iterations to reach the optimum. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), interface p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction), objective p. 28 (B.2 Algorithm 3 termination), p. 28 (B.2 Algorithm 3 termination).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
