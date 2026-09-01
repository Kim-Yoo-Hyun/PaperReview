# Problem - TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1310.7730; PDF retrieval source: https://arxiv.org/pdf/1310.7730. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional motion planning problems.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a new optimization-based approach for robotic motion planning among obstacles.
- **p. 1 / Abstract - extractive body cue:** Like CHOMP, our algorithm can be used to find collision-free trajectories from na¨ıve, straight-line initializations that might be in collision.
- **p. 1 / Abstract - extractive body cue:** At the core of our approach are (i) A sequential convex optimization procedure, which penalizes collisions with a hinge loss and increases the penalty coefficients ...
- **p. 1 / Abstract - extractive body cue:** (ii) An efficient formulation of the no-collisions constraint that directly considers continuous-time safety Our algorithm is implemented in a software package called TrajOpt.
- **p. 1 / Abstract - extractive body cue:** We report results from a series of experiments comparing TrajOpt with CHOMP and randomized planners from OMPL, with regard to planning time and path quality.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional motion planning problems.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, in addition to providing a revised and extended version of our work [43], (i) we describe an extension to the algorithm described ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | Let S and G denote the start and goal states for a planning problem. | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF |
| State / latent | Let, denote, start, goal, states, planning, problem, Trajectory, optimization, fundamental | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | TrajOpt, applied, several, motion, planning, scenarios, trajectory, PR2 | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: Let, denote, start, goal, states, planning, problem, Trajectory, optimization, fundamental | p. 8 (V. MOTION PLANNING BENCHMARK), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: handling, collisions, yields, polyhedral, approximation, free, part, configuration | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (A. Sequential Convex Optimization over SE(3)) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: Note, even, though, initialize, tucked, arms, optimization, typically | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 11 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, in addition to providing a revised and extended version of our work [43], (i) we describe an extension to the algorithm described ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** requires solving a non-convex, constrained optimization problem.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3))): Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem that is solved at each ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This parametrization is provided by the Lie algebra se(3), which is defined as the tangent vector space at the identity of SE(3), and, informally, consists ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | At the core of our approach is the use of sequential convex optimization with ℓ1 penalty terms for ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 8 (V. MOTION PLANNING BENCHMARK), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 8 (V. MOTION PLANNING BENCHMARK), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
