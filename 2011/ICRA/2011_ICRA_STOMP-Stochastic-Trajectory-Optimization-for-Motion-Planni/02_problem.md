# Problem - STOMP: Stochastic Trajectory Optimization for Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980280; PDF retrieval source: https://whiteoak.umd.edu/roswiki/attachments/Papers%282f%29ICRA2011_Kalakrishnan/kalakrishnan_icra2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): We present a new approach to motion planning using a stochastic trajectory optimization framework.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a new approach to motion planning using a stochastic trajectory optimization framework.
- **p. 1 / Abstract - extractive body cue:** The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated ...
- **p. 1 / Abstract - extractive body cue:** A cost function based on a combination of obstacle and smoothness cost is optimized in each iteration.
- **p. 1 / Abstract - extractive body cue:** No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the approach both in simulation and on a mobile manipulation system for unconstrained and constrained tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a new approach to motion planning that can deal with general constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We present a new approach to motion planning using a stochastic trajectory optimization framework. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | Inspired, previous, probability, matching, literature, well, recent, areas, path, integral | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | start, following, optimization, problem, where, noisy, parameter, vector | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: Inspired, previous, probability, matching, literature, well, recent, areas, path, integral | p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: present, motion, planning, deal, general, constraints, Inspired, previous | p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: treat, motion, planning, optimization, problem, search, smooth, trajectory | p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 3 (IV. MOTION PLANNING FOR A ROBOT ARM) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 4 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM)): In this paper, we present a new approach to motion planning that can deal with general constraints.

- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach involves stochastic trajectory optimization using a series of noisy trajectories.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** This allows us to optimize arbitrary costs q(˜θ) for which derivatives are not available, or are non-differentiable or non-smooth.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We address the design of a cost function that allows planning for obstacle avoidance, optimization of task constraints, and minimization of joint torques.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | (c) Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | STOMP produced a collision-free trajectory in all (a) (b) (c) Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Success in this scenario implies the generation of a collision-free trajectory. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), objective p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
