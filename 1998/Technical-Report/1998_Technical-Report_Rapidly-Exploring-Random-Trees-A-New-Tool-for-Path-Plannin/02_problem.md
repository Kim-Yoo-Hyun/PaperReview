# Problem - Rapidly-Exploring Random Trees: A New Tool for Path Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (4 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://lavalle.pl/rrtpubs.html; PDF retrieval source: https://lavalle.pl/papers/Lav98c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce the concept of a Rapidly-exploring Random Tree (RRT) as a randomized data structure that is designed for a broad class of path planning ...
- **p. 1 / Abstract - extractive body cue:** An RRT is iteratively expanded by applying control inputs that drive the system slightly toward randomly-selected points, 18 opposed to requiring point-to-point convergence, as in ...
- **p. 1 / Abstract - extractive body cue:** Several desir- ‘able properties and a basic implementation of RRTs are discussed.
- **p. 1 / Abstract - extractive body cue:** To date, we have successfully applied RRTs to holonomic, nonholonomic, and kinodynamic planning problems of up to twelve degrees of freedom.
- **p. 1 / 1 Introduction - extractive body cue:** ‘Over the past decade, several randomized approaches have been proposed and successfully applied to the general problem of path planning in a high-dimensional configuration space, ...
- **p. 1 / 1 Introduction - extractive body cue:** The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic planning problems.
- **p. 1 / 1 Introduction - extractive body cue:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The primary difficulty with existing techniques is that, although powerful for standard path planning, they do not naturally extend to general nonholonomic ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | Step 5 selects an input, w, that m rizes the distance from year tO rand» and ensures that the state remains in ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | Step, selects, input, rizes, distance, year, rand, ensures, state, remains | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | RRT, iteratively, expanded, applying, control, inputs, drive, system | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: Step, selects, input, rizes, distance, year, rand, ensures, state, remains | p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: introduce, randomized, data, structure, path, planning, designed, problems | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: state, transition, equation, form, defined, express, nonholonomic, constraints | p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Nice Properties of RRTs), p. 2 (2. Rapidly-Exploring Random Trees), p. 3 (3. Nice Properties of RRTs) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 2 (3. Nice Properties of RRTs), p. 3 (3. Nice Properties of RRTs), p. 1 (Abstract) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** For planning of holonomic systems or steerable nonholonomic systems (see [6] and references therein), the local planning step might be efficient; however, in general, the ...

## What the Paper Changes

PDF contribution framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Tn this paper, we introduce a randomized data structure for path planning that is designed for problems that, have nonholonomic constraints.

- **p. 1 / 1 Introduction - extractive body cue:** Both are designed with as few heutisties and arbitrary

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Collision detection can be performed by an incremental method such as Mirtich's V-Clip. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | States in Xj» could correspond to ver locity bounds, configurations at which a robot is in collision with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | In a related paper [7], we presented an RRT-based, planner that computes collision-free kinodynamic trajec~ tories that fire ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Collision detection is a key bottleneck in path planning, and an RRT is completely suited for incremental collision ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (9 Return T), p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (Abstract), p. 1 (1 Introduction), objective p. 2 (2. Rapidly-Exploring Random Trees), p. 1 (1 Introduction), p. 1 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
