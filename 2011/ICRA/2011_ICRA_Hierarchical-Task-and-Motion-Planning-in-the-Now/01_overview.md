# Hierarchical Task and Motion Planning in the Now

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980391.
> PDF retrieval source: https://doi.org/10.1109/ICRA.2011.5980391. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://doi.org/10.1109/ICRA.2011.5980391
- Full-text retrieval: https://doi.org/10.1109/ICRA.2011.5980391
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 planning 문제를 이해하기 위해 읽는다. 본문은 We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization of the first plan step, there exist ...를 문제로 두고, The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper we outline an approach to the integration of task planning and motion planning that has the following key properties: It is aggressively ...
- **p. 1 / Abstract - extractive body cue:** It operates on detailed, continuous geometric representations and does not require a-priori discretization of the state or action spaces.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As robots become more physically robust and capable of sophisticated sensing, navigation, and manipulation, we want them to carry out increasingly complex tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** A robot that helps in a household must plan over the scale of hours or days, considering abstract features such as the desires of the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of such tasks derives from very long time horizons and large numbers of objects to be considered and manipulated.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** If, for some reason, serializability fails, then we formulate an interleaved plan for achieving the effects of both steps; as long as actions in the ...

## Core Idea

- **p. 7 / V. ALGORITHMS - extractive body cue:** The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.
- **p. 7 / V. ALGORITHMS - extractive body cue:** The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | HPN(currentState, goal, operators, absLevel, world): if holds(goal, currentState): return TRUE else p = PLAN(currentState, goal, operators, absLevel) for (oi, gi) in p if prim(oi): currentState = world.execute(oi) else HPN(currentState, ... | start/goal, map, dynamics와 successor/operator description | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |
| State/latent | HPN, currentState, goal, operators, absLevel, world, holds, return, TRUE, else, PLAN, prim | path, trajectory, symbolic state 또는 task-motion decision | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION) |
| Output/action | The planning and execution system is invoked by calling HPN(currentState, goal, operators, absLevel, world), where currentState is a description of the current state of world; goal is a conjunction of fluents describing ... | feasible action sequence 또는 minimum-cost plan | p. 7 (V. ALGORITHMS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | A motion planner lazily builds a 4-dof visibility-graph; x, y translation constraints are represented as C-space polygons for discrete ranges of z and θ. | path cost, goal reachability, feasibility와 computation | p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS) |

## Main Claims and Actual Contribution

- **p. 3 / B C - extractive body cue:** Note that executing the operator for removing c from the swept volume of a requires no further planning or execution, as the condition it was ...
- **p. 6 / C C - extractive body cue:** In this case, the planner will achieve p1, ...., pn in whatever way it can, and then execute o and r will be achieved; the ...
- **p. 6 / C C - extractive body cue:** For example, if it is important that the object not be regrasped as part of the Place operation, it is possible to 'expose' the choice ...
- **p. 7 / VI. CORRECTNESS - extractive body cue:** So, we need to examine the effects of hierarchy and of operating in infinite domains on the ability of HPN to achieve feasible goals.
- **p. 2 / III. EXAMPLE - extractive body cue:** The primitive operation is executed in the world, which results in the robot grasping c.
- **p. 5 / C C - extractive body cue:** The pick operation results in the robot holding object O: Holding() = O: define: Ts = {T : ClearX (T, X) ∈goal ∧O̸ ∈X} exists: ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 3 (B C), p. 6 (C C) |
| Embodiment/environment | The first requires that a swept volume of the robot moving to object a and picking it up be free. | hardware/simulator version and reset protocol | p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE) |
| Dataset/benchmark | Washing domain, in which the robot must move object A to the washing area, wash it, and put it in the storage area. tree we have constructed. | role, split, size and leakage | p. 2 (III. EXAMPLE), p. 2 (III. EXAMPLE), p. 3 (B C), p. 3 (IV. REPRESENTATION) |
| Metric | To operate in infinite domains, we augment the standard operator descriptions with the following features: Suggesters, which are procedures that map current start and goal states, and bindings of other variables, to ... | definition, denominator, direction and uncertainty | p. 5 (C C), p. 2 (III. EXAMPLE), p. 5 (C C) |
| Baseline/ablation | First, it may not be possible to make pn true without undoing p1, . . . , pn-1. | fair input/data/compute/action matching | p. 6 (C C), p. 5 (C C), p. 2 (III. EXAMPLE) |

## Explicit Limitations and Failure Boundary

- **p. 6 / C C - extractive body cue:** Because these variables both have infinite domains in our setting, we cannot enumerate them.
- **p. 6 / C C - extractive body cue:** If at attempt at serializing operations at an abstract level fails, then the planning problem is
- **p. 7 / V. ALGORITHMS - extractive body cue:** SuggestPoses(O, R, Taboos): finds a set of poses for O where it is completely inside region R, there is no collision with taboo regions, and ...
- **p. 7 / V. ALGORITHMS - extractive body cue:** SuggestParking(O, Taboos, start): find an "out of the way" location for O that does not overlap any of the regions in Taboos.

## Why Read It

Manipulation, contact, tactile, and dexterity의 planning 문제를 이해하기 위해 읽는다. 본문은 We attempt to avoid such failures by constraining the abstract plan steps so that they are serializable [1]; that is, so that for any realization of the first plan step, there exist ...를 문제로 두고, The architecture can be thought of as doing a depth-first traversal of a planning tree, and is implemented as a recursive algorithm, as shown below.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 7 (V. ALGORITHMS), p. 7 (V. ALGORITHMS), p. 3 (B C), p. 6 (C C) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
