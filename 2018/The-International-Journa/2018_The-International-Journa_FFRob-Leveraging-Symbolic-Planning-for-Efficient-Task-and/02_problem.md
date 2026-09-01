# Problem - FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://journals.sagepub.com/doi/10.1177/0278364917739114; PDF retrieval source: https://journals.sagepub.com/doi/10.1177/0278364917739114. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1.1 Approach)): Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Mobile manipulation problems involving many objects are challenging to solve due to the high dimensionality and multi-modality of their hybrid configuration spaces.
- **p. 1 / Abstract - extractive body cue:** Planners that perform a purely geometric search are prohibitively slow for solving these problems because they are unable to factor the configuration space.
- **p. 1 / Abstract - extractive body cue:** Symbolic task planners can efficiently construct plans involving many variables but cannot represent the geometric and kinematic constraints required in manipulation.
- **p. 1 / Abstract - extractive body cue:** We present the FFROB algorithm for solving task and motion planning problems.
- **p. 1 / Abstract - extractive body cue:** First, we introduce Extended Action Specification (EAS) as a general purpose planning representation that supports arbitrary predicates as conditions.
- **p. 1 / 1 Introduction - extractive body cue:** Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges.
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation planning remains challenging because it is notoriously difficult to work in a high-dimensional space and make a long sequence of intertwined decisions.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Planning for mobile manipulation problems involving cluttered environments and multiple manipulation primitives still presents substantial challenges. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces. | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | have, been, tackling, problems, require, long, sequences, actions, large, discrete | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | introduce, Extended, Action, Specification, EAS, symbolic, planing, representation | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: have, been, tackling, problems, require, long, sequences, actions, large, discrete | p. 1 (1 Introduction), p. 2 (1.1 Approach), p. 2 (1.1 Approach) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: introduce, Extended, Action, Specification, EAS, symbolic, planing, representation | p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 1 (1 Introduction) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: model, task, motion, planning, symbolic, where, conditions, actions | p. 2 (1.1 Approach), p. 2 (1.1 Approach) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1.1 Approach), p. 2 (1.1 Approach) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 30 (11.4 Results), p. 30 (11 Experiments), p. 31 (11.4 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Manipulation planning remains challenging because it is notoriously difficult to work in a high-dimensional space and make a long sequence of intertwined decisions.
- **p. 2 / 1 Introduction - extractive body cue:** We cannot efficiently maintain a representation of this connectivity with a set of static assertions updated by symbolic actions; determining how the connectivity of the ...
- **p. 1 / 1 Introduction - extractive body cue:** 2004) have been tackling problems that require long sequences of actions and large discrete state-spaces.
- **p. 3 / 1.1 Approach - extractive body cue:** Finally, we perform experiments on challenging manipulation problems and explore the effect of various planner configurations on their performance.

## What the Paper Changes

PDF contribution framing (p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 1 (1 Introduction)): We introduce Extended Action Specification (EAS), a new symbolic planing representation that supports complex conditions.

- **p. 2 / 1.1 Approach - extractive body cue:** The primary contribution of this paper is FFROB, an efficient and probabilistically complete algorithm for fully integrated task and motion planning.
- **p. 1 / 1 Introduction - extractive body cue:** A long-standing goal in robotics is to develop robots that can operate autonomously in unstructured human environments.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 30 | In practice, we do not increase the sampling parameter sizes upon a sampling failure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 30 | We enforce timeouts of 30 iterations for S-PICK-PLACE due to inverse reachability, inverse kinematics, or motion planning failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 33 | Finally, each segment from q0 to q0 ∈B0 or from q∗to qk ∈Bk is collision-free by the problem ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 33 | For any robustly feasible motion planning problem, there exists a sequence of k + 1, where k = ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 Introduction), p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1.1 Approach), interface p. 1 (1 Introduction), p. 2 (1.1 Approach), p. 2 (1.1 Approach), p. 1 (1 Introduction), objective p. 2 (1.1 Approach), p. 2 (1.1 Approach).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
