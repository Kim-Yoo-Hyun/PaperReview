# Problem - Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf; PDF retrieval source: https://www.ijcai.org/Proceedings/15/Papers/274.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We consider problems of sequential robot manipulation (aka. combined task and motion planning) where the objective is primarily given in terms of a cost function ...
- **p. 1 / Abstract - extractive body cue:** In this case we should leverage optimization methods to inform search over potential action sequences.
- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...
- **p. 1 / Abstract - extractive body cue:** We tackle the challenge of solving such programs by proposing three levels of approximation: The coarsest level introduces the concept of the effective end state ...
- **p. 1 / Abstract - extractive body cue:** Optimization on this level is fast and can inform symbolic search.
- **p. 1 / 1 Introduction - extractive body cue:** Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description.
- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Most existing TAMP approaches, however, require a well-defined task planning problem including a symbolic goal description. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | formulate, problem, holistically, storder, logic, extension, mathematical, program, non-linear, constrained | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | implies, challenge, motion, optimization, across, kinematic, switches, world | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: formulate, problem, holistically, storder, logic, extension, mathematical, program, non-linear, constrained | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: Besides, novel, formulation, manipulation, planning, LGP, think, concept | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: consider, problems, sequential, robot, manipulation, combined, task, motion | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 5 (5 Experiments), p. 5 (5 Experiments), p. 6 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** All three levels raise novel interesting challenges for motion (or configuration) optimizers.
- **p. 2 / 1 Introduction - extractive body cue:** This implies the challenge of motion optimization across kinematic switches of the world configuration (across action boundaries) to allow for the optimization over the full ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)): Besides the novel formulation of manipulation planning as an LGP, we think of the concept of the effective end space and its optimization as a search heuristic as the core ...

- **p. 1 / 1 Introduction - extractive body cue:** The specific methods we propose in this paper are (yet!) in many respects less efficient than existing TAMP approaches; in particular we cannot scale to ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper we propose three levels on which geometric reasoning (that is, optimization over geometric configurations and paths) may inform symbolic search towards a ...
- **p. 1 / Abstract - extractive body cue:** We propose to formulate the problem holistically as a 1storder logic extension of a mathematical program: a non-linear constrained program over the full world trajectory ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Further constraints concern standard motion optimization aspects such as collision avoidance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The geometric and differential constraints hpath, gpath implement zero velocity of the object-hand pose while inhand, zero velocities ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The resulting trajectories are smooth and collision free (if keyframe optimization indicated feasibility) and generate the optimized end ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (1 Introduction), p. 1 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
