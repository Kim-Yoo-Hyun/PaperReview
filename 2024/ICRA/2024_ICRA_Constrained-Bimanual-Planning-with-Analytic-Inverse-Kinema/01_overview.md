# Constrained Bimanual Planning with Analytic Inverse Kinematics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2309.08770.
> PDF retrieval source: https://arxiv.org/pdf/2309.08770. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, bimanual manipulation, motion planning, inverse kinematics
- Official paper: https://arxiv.org/abs/2309.08770
- Full-text retrieval: https://arxiv.org/pdf/2309.08770
- Code/Project: https://tommycohn.com/Bimanual-Web/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 planning 문제를 이해하기 위해 읽는다. 본문은 Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms.를 문제로 두고, Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In order for a bimanual robot to manipulate an object that is held by both hands, it must construct motion plans such that the transformation ...
- **p. 1 / Abstract - extractive body cue:** This amounts to complicated nonlinear equality constraints in the configuration space, which are difficult for trajectory optimizers.
- **p. 1 / Abstract - extractive body cue:** In addition, the set of feasible configurations becomes a measure zero set, which presents a challenge to sampling-based motion planners.
- **p. 1 / Abstract - extractive body cue:** We leverage an analytic solution to the inverse kinematics problem to parametrize the configuration space, resulting in a lower-dimensional representation where the set of valid ...
- **p. 1 / Abstract - extractive body cue:** We describe how to use this parametrization with existing motion planning algorithms, including sampling-based approaches, trajectory optimizers, and techniques that plan through convex inner-approximations of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Configurations where the subordinate arm cannot reach the end-effector of the primary arm, or where doing so would require violating joint limits, are treated as ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If a robot must move an object that it is holding with both hands, we propose constructing a plan for one "controllable" arm, and then ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, we present various experiments demonstrating the efficacy of these new techniques.
- **p. 2 / III. METHODOLOGY - extractive body cue:** We introduce a bijective mapping between joint angles and end-effector pose for a single arm with analytic IK.
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Section IV, we demonstrate that this theoretical limitation is not a major roadblock to our framework's efficacy.
- **p. 4 / III. METHODOLOGY - extractive body cue:** 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Although this constraint would be enforced by the later constraints, specifically handling this case first greatly improves the performance of the later counterexample searches.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , CSk Output: Halfspace Intersection H(A, b) 1 ... | start/goal, map, dynamics와 successor/operator description | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| State/latent | Algorithm, Constrained, IRIS, Single, Iteration, Input, Bounding, Box, Hyperellipsoid, Constraint, Sets, CS1 | path, trajectory, symbolic state 또는 task-motion decision | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Output/action | When a rigid object is held with both end effectors, a rigid transformation T ∈SE(3) between them becomes fixed; we let ϕT : XL →SE(3) take in an end-effector pose for the ... | feasible action sequence 또는 minimum-cost plan | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , CSk Output: Halfspace Intersection H(A, b) 1 ... | path cost, goal reachability, feasibility와 computation | p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If a robot must move an object that it is holding with both hands, we propose constructing a plan for one "controllable" arm, and then ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, we present various experiments demonstrating the efficacy of these new techniques.
- **p. 2 / III. METHODOLOGY - extractive body cue:** We introduce a bijective mapping between joint angles and end-effector pose for a single arm with analytic IK.
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Section IV, we demonstrate that this theoretical limitation is not a major roadblock to our framework's efficacy.
- **p. 5 / IV. RESULTS - extractive body cue:** AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts).
- **p. 6 / IV. RESULTS - extractive body cue:** GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Embodiment/environment | GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video. | hardware/simulator version and reset protocol | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Dataset/benchmark | To evaluate the merits of our IK parametrization for constrained planning, we consider a task where the two arms must move an object around a set of shelves, while avoiding collisions. | role, split, size and leakage | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Metric | (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown). | definition, denominator, direction and uncertainty | p. 6 (IV. RESULTS), p. 1 (Figure/Table caption), p. 5 (IV. RESULTS) |
| Baseline/ablation | We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal for extending GCS to this class of problems. | fair input/data/compute/action matching | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the ...
- **p. 5 / IV. RESULTS - extractive body cue:** Paths marked with an asterisk were not collision-free.
- **p. 5 / IV. RESULTS - extractive body cue:** Plans from the trajectory optimization baseline also had slight collisions with obstacles.
- **p. 6 / IV. RESULTS - extractive body cue:** (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown).
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Robot configurations sampled from various IRIS regions. average path length and planning time. We set a maximum planning time of 10 minutes for ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 planning 문제를 이해하기 위해 읽는다. 본문은 Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms.를 문제로 두고, Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
