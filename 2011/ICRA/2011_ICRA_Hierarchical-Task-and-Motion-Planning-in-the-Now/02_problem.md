# Problem - Hierarchical Task and Motion Planning in the Now

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980391; PDF retrieval source: https://doi.org/10.1109/ICRA.2011.5980391. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization of the first plan step, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper we outline an approach to the integration of task planning and motion planning that has the following key properties: It is aggressively ...
- **p. 1 / Abstract - extractive body cue:** It operates on detailed, continuous geometric representations and does not require a-priori discretization of the state or action spaces.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As robots become more physically robust and capable of sophisticated sensing, navigation, and manipulation, we want them to carry out increasingly complex tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** A robot that helps in a household must plan over the scale of hours or days, considering abstract features such as the desires of the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of such tasks derives from very long time horizons and large numbers of objects to be considered and manipulated.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that ... | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | HPN(currentState, goal, operators, absLevel, world): if holds(goal, currentState): return TRUE else p = PLAN(currentState, goal, operators, absLevel) for (oi, gi) in p ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | makes, choices, commits, them, limiting, length, plans, exponentially | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: architecture, thought, doing, depth-first, traversal, planning, tree, implemented | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: motion, planner, lazily, builds, visibility-graph, translation, constraints, represented | p. 7 (V. ALGORITHMS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 5 (C C), p. 2 (III. EXAMPLE), p. 5 (C C) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...

## What the Paper Changes

PDF body contribution framing (p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS)): The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.

- **p. 7 / V. ALGORITHMS - extractive body cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Because these variables both have infinite domains in our setting, we cannot enumerate them. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | If at attempt at serializing operations at an abstract level fails, then the planning problem is | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | SuggestPoses(O, R, Taboos): finds a set of poses for O where it is completely inside region R, there ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | SuggestParking(O, Taboos, start): find an "out of the way" location for O that does not overlap any of ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective p. 7 (V. ALGORITHMS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
