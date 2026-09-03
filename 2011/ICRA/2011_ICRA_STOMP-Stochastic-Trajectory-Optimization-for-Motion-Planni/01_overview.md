# STOMP: Stochastic Trajectory Optimization for Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980280.
> PDF retrieval source: https://whiteoak.umd.edu/roswiki/attachments/Papers%282f%29ICRA2011_Kalakrishnan/kalakrishnan_icra2011.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, motion planning, trajectory optimization, stochastic optimization
- Official paper: https://doi.org/10.1109/ICRA.2011.5980280
- Full-text retrieval: https://whiteoak.umd.edu/roswiki/attachments/Papers%282f%29ICRA2011_Kalakrishnan/kalakrishnan_icra2011.pdf
- Code/Project: https://moveit.github.io/moveit_tutorials/doc/stomp_planner/stomp_planner_tutorial.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 We present a new approach to motion planning using a stochastic trajectory optimization framework.를 문제로 두고, In this paper, we present a new approach to motion planning that can deal with general constraints.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a new approach to motion planning using a stochastic trajectory optimization framework.
- **p. 1 / Abstract - extractive body cue:** The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated ...
- **p. 1 / Abstract - extractive body cue:** A cost function based on a combination of obstacle and smoothness cost is optimized in each iteration.
- **p. 1 / Abstract - extractive body cue:** No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the approach both in simulation and on a mobile manipulation system for unconstrained and constrained tasks.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a new approach to motion planning that can deal with general constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach involves stochastic trajectory optimization using a series of noisy trajectories.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** This allows us to optimize arbitrary costs q(˜θ) for which derivatives are not available, or are non-differentiable or non-smooth.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We address the design of a cost function that allows planning for obstacle avoidance, optimization of task constraints, and minimization of joint torques.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** In order to keep the notation simple, we first derive the algorithm for a 1-dimensional trajectory; this naturally extends later to multiple dimensions.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 3) Torque costs: Given a suitable dynamics model of the robot, we can compute the feed-forward torque required at each joint to track the desired ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 1) Obstacle costs: We use an obstacle cost function similar to that used in previous work on optimizationbased motion planning [9].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we propose an estimated gradient formulated as follows: ... | start/goal, map, dynamics와 successor/operator description | p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION) |
| State/latent | Inspired, previous, probability, matching, literature, well, recent, areas, path, integral, reinforcement, learning | path, trajectory, symbolic state 또는 task-motion decision | p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM) |
| Output/action | Domestic and retail scenarios, in particular, will have lots of cases where constraint satisfaction may be a prime goal, e.g. carrying a glass of water. | feasible action sequence 또는 minimum-cost plan | p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |
| Objective/outcome | We treat motion planning as an optimization problem, to search for a smooth trajectory that minimizes costs corresponding to collisions and constraints. | path cost, goal reachability, feasibility와 computation | p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a new approach to motion planning that can deal with general constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach involves stochastic trajectory optimization using a series of noisy trajectories.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** This allows us to optimize arbitrary costs q(˜θ) for which derivatives are not available, or are non-differentiable or non-smooth.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We address the design of a cost function that allows planning for obstacle avoidance, optimization of task constraints, and minimization of joint torques.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** The execution times are comparable, even though CHOMP usually requires more iterations to achieve success.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** The exploration noise magnitude for STOMP, and the gradient descent step size for CHOMP were both tuned to achieve good performance without instability.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Hence, performance will vary depending on the initial

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Embodiment/environment | We conduct experiments on a simulation of the Willow Garage PR2 robot in a simulated world, followed by a demonstration of performance on the real robot. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | STOMP is an algorithm that performs local optimization, i.e. it finds a locally optimum trajectory rather than a global one. | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Metric | Success in this scenario implies the generation of a collision-free trajectory. | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 4 (V. EXPERIMENTS) |
| Baseline/ablation | (a) Plan obtained without torque minimization: arm is stretched. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** (c) Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of the gripper.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** STOMP produced a collision-free trajectory in all (a) (b) (c) Fig.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Success in this scenario implies the generation of a collision-free trajectory.
- **p. 3 / 5) Update θ ←θ + δθ - extractive body cue:** An additional advantage is that no gradient step-size parameter is required; the only open parameter in this algorithm is the magnitude of the exploration noise.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** Additionally, since the convex combination of noise is smoothed through the M matrix, the resulting updated trajectory smoothly touches the joint limit as opposed to ...

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 We present a new approach to motion planning using a stochastic trajectory optimization framework.를 문제로 두고, In this paper, we present a new approach to motion planning that can deal with general constraints.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 3 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 5 (V. EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
