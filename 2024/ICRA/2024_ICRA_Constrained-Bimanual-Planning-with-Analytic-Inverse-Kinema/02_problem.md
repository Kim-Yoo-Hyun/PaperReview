# Problem - Constrained Bimanual Planning with Analytic Inverse Kinematics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.08770; PDF retrieval source: https://arxiv.org/pdf/2309.08770. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In order for a bimanual robot to manipulate an object that is held by both hands, it must construct motion plans such that the transformation ...
- **p. 1 / Abstract - extractive body cue:** This amounts to complicated nonlinear equality constraints in the configuration space, which are difficult for trajectory optimizers.
- **p. 1 / Abstract - extractive body cue:** In addition, the set of feasible configurations becomes a measure zero set, which presents a challenge to sampling-based motion planners.
- **p. 1 / Abstract - extractive body cue:** We leverage an analytic solution to the inverse kinematics problem to parametrize the configuration space, resulting in a lower-dimensional representation where the set of valid ...
- **p. 1 / Abstract - extractive body cue:** We describe how to use this parametrization with existing motion planning algorithms, including sampling-based approaches, trajectory optimizers, and techniques that plan through convex inner-approximations of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Configurations where the subordinate arm cannot reach the end-effector of the primary arm, or where doing so would require violating joint limits, are treated as ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box, Hyperellipsoid, Constraint | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | connected, components, preimages, W-sheets, called, Cbundles, composed, regular | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box, Hyperellipsoid, Constraint | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: Then, present, parametrization, constraint, manifold, bimanual, planning, discuss | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box | p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 6 (IV. RESULTS), p. 1 (Figure/Table caption), p. 5 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Configurations where the subordinate arm cannot reach the end-effector of the primary arm, or where doing so would require violating joint limits, are treated as ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.

- **p. 1 / I. INTRODUCTION - extractive body cue:** If a robot must move an object that it is holding with both hands, we propose constructing a plan for one "controllable" arm, and then ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, we present various experiments demonstrating the efficacy of these new techniques.
- **p. 2 / III. METHODOLOGY - extractive body cue:** We introduce a bijective mapping between joint angles and end-effector pose for a single arm with analytic IK.
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Section IV, we demonstrate that this theoretical limitation is not a major roadblock to our framework's efficacy.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Paths marked with an asterisk were not collision-free. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Plans from the trajectory optimization baseline also had slight collisions with obstacles. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown). | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), objective p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
