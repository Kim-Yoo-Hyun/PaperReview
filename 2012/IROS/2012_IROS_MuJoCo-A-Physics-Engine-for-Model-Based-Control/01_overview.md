# MuJoCo: A Physics Engine for Model-Based Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/IROS.2012.6386109.
> PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. Reading tracker status/evidence was not changed.

- Year/Venue: 2012 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, simulation, Physics Engine, Control
- Official paper: https://doi.org/10.1109/IROS.2012.6386109
- Full-text retrieval: https://doi.org/10.1109/IROS.2012.6386109
- Code/Project: https://mujoco.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 simulation 문제를 이해하기 위해 읽는다. 본문은 However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.를 문제로 두고, This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality constraints.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We describe a new physics engine tailored to model-based control.
- **p. 1 / Abstract - extractive body cue:** Multi-joint dynamics are represented in generalized coordinates and computed via recursive algorithms.
- **p. 1 / Abstract - extractive body cue:** Contact responses are computed via efficient new algorithms we have developed, based on the modern velocity-stepping approach which avoids the difficulties with spring-dampers.
- **p. 1 / Abstract - extractive body cue:** Models are specified using either a high-level C++ API or an intuitive XML file format.
- **p. 1 / Abstract - extractive body cue:** A built-in compiler transforms the user model into an optimized data structure used for runtime computation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.
- **p. 1 / I. INTRODUCTION - extractive body cue:** What is less obvious however is that, in the context of control optimization, these requirements become so demanding that none of the existing physics engines ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- **p. 6 / III. MODELING - extractive body cue:** A MuJoCo model consists of one or several kinematic trees, which can have f1oating bases including isolated objects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing physics engines can be used to test controllers that are already designed.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As Sims [7] pointed out, if the physics engine allows cheating the optimization algorithm will find a way to exploit it - and produce a ...
- **p. 7 / III. MODELING - extractive body cue:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** We start with notation and smooth dynamics which are fairly standard, then explain the contact simulation algorithms in more detail, followed by computational complexity and ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates  inertia matrix ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control inputs, optional activation states (used to model ... | simulated state, geometry, contact와 control input | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION) |
| State/latent | tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around, geoms, Actuator | dynamics/contact state 또는 learned simulator representation | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | These observations indicated that we need a new engine, representing the state in joint coordinates and simulating contacts in ways that are related to LCP but better. | simulation step, trajectory 또는 environment query | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (III. MODELING) |
| Objective/outcome | Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates  inertia matrix in generalized coordinates b "bias" forces: Coriolis, ... | physical plausibility, speed, reproducibility와 task utility | p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 7 (III. MODELING) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- **p. 6 / III. MODELING - extractive body cue:** A MuJoCo model consists of one or several kinematic trees, which can have f1oating bases including isolated objects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing physics engines can be used to test controllers that are already designed.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As Sims [7] pointed out, if the physics engine allows cheating the optimization algorithm will find a way to exploit it - and produce a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps.
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Each iteration involves factorization of a -by-matrix; this could potentially be improved using Hessian-free methods.
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** Of course violations should be difficult to achieve, i.e. the inferred control force should be large in the corresponding subspace.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state) |
| Embodiment/environment | It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | hardware/simulator version and reset protocol | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION) |
| Dataset/benchmark | However in the presence of branch-induced sparsity typical in robotics these algorithms are not much faster than the present approach [4]. | role, split, size and leakage | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION), p. 5 (5) Integrate numerically to obtain the next state), p. 6 (III. MODELING) |
| Metric | Furthermore the pyramid approximation introduces errors. | definition, denominator, direction and uncertainty | p. 4 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state) |
| Baseline/ablation | Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in the absence of contacts or equality constraints. | fair input/data/compute/action matching | p. 7 (IV. TIMING TESTS), p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state) |

## Explicit Limitations and Failure Boundary

- **p. 3 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the ...
- **p. 3 / 5) Integrate numerically to obtain the next state - extractive body cue:** In the tangent plane we have vF parallel to fF ­ vFfF® ≤0 (5) °°fF°° ≤N The first line means that if there is slip ...
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual).
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a distance ...
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** Instead it computes the desired next-state velocity v∗ which would result if penetrations decayed like criticallydamped springs (similar to equality-constraint violations) and there was no ...
- **p. 7 / III. MODELING - extractive body cue:** Their primary use in the engine is collision detection as well as tendon wrapping.
- **p. 7 / III. MODELING - extractive body cue:** Collision detection uses dedicated pair-wise functions when possible, and otherwise defaults to a general-purpose convex collider (implemented by libccd).

## Why Read It

Planning and control의 simulation 문제를 이해하기 위해 읽는다. 본문은 However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.를 문제로 두고, This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality constraints.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (III. MODELING), p. 2 (II. ALGORITHMIC FOUNDATIONS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
