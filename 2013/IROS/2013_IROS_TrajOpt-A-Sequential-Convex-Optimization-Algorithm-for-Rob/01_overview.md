# TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1310.7730.
> PDF retrieval source: https://arxiv.org/pdf/1310.7730. Reading tracker status/evidence was not changed.

- Year/Venue: 2013 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, motion planning, trajectory optimization, collision avoidance
- Official paper: https://arxiv.org/abs/1310.7730
- Full-text retrieval: https://arxiv.org/pdf/1310.7730
- Code/Project: https://rll.berkeley.edu/trajopt/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional motion planning problems.를 문제로 두고, Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem that is solved at each optimization iteration.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a new optimization-based approach for robotic motion planning among obstacles.
- **p. 1 / Abstract - extractive body cue:** Like CHOMP, our algorithm can be used to find collision-free trajectories from na¨ıve, straight-line initializations that might be in collision.
- **p. 1 / Abstract - extractive body cue:** At the core of our approach are (i) A sequential convex optimization procedure, which penalizes collisions with a hinge loss and increases the penalty coefficients ...
- **p. 1 / Abstract - extractive body cue:** (ii) An efficient formulation of the no-collisions constraint that directly considers continuous-time safety Our algorithm is implemented in a software package called TrajOpt.
- **p. 1 / Abstract - extractive body cue:** We report results from a series of experiments comparing TrajOpt with CHOMP and randomized planners from OMPL, with regard to planning time and path quality.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional motion planning problems.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, in addition to providing a revised and extended version of our work [43], (i) we describe an extension to the algorithm described ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This parametrization is provided by the Lie algebra se(3), which is defined as the tangent vector space at the identity of SE(3), and, informally, consists ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This distortion can severely slow down an optimization algorithm, by reducing the neighborhood where local (first and second-order) approximations are good.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** The termination conditions we used for the optimization were (i) maximum of 40 iterations, (ii) minimum merit function improvement ratio of 10-4, (iii) minimum trust ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Let S and G denote the start and goal states for a planning problem.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Let S and G denote the start and goal states for a planning problem. | start/goal, map, dynamics와 successor/operator description | p. 8 (V. MOTION PLANNING BENCHMARK), p. 1 (I. INTRODUCTION) |
| State/latent | Let, denote, start, goal, states, planning, problem, Trajectory, optimization, fundamental, optimal, control | path, trajectory, symbolic state 또는 task-motion decision | p. 8 (V. MOTION PLANNING BENCHMARK), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | Trajectory optimization is fundamental in optimal control where the objective is to solve for a trajectory encoded as a sequence of states and controls that optimizes a given objective subject to constraints ... | feasible action sequence 또는 minimum-cost plan | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | Note that even though we initialize with tucked arms, the optimization typically untucks the arms to improve the cost. | path cost, goal reachability, feasibility와 computation | p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 5 (A. Sequential Convex Optimization over SE(3)) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This parametrization is provided by the Lie algebra se(3), which is defined as the tangent vector space at the identity of SE(3), and, informally, consists ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms shooting ...
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Note that even though we initialize with tucked arms, the optimization typically untucks the arms to improve the cost.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** TrajOpt with multiple initializations outperformed the other approaches in both sets of problems.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption) |
| Embodiment/environment | Left and center: two of the scenes used for the arm planning benchmark. | hardware/simulator version and reset protocol | p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK) |
| Dataset/benchmark | For collision checking, we took the convex hull of the geometry of each link of the robot, where each link is made of one or more meshes. | role, split, size and leakage | p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 9 (VI. PHYSICAL EXPERIMENTS) |
| Metric | Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. | definition, denominator, direction and uncertainty | p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 11 (Figure/Table caption) |
| Baseline/ablation | We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems. | fair input/data/compute/action matching | p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK) |

## Explicit Limitations and Failure Boundary

- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A and a static object B, for 0 ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in Sec.
- **p. 14 / XI. CONCLUSION - extractive body cue:** At the core of our approach is the use of sequential convex optimization with ℓ1 penalty terms for satisfying constraints, an efficient formulation of the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Hinge penalty for collisions a user-defined distance dcheck between them where dcheck > dsafe, and formulate the collision penalty based on these pairs. ...
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** After finding a collision-free configuration W of this sort, we initialized with the trajectory SWG as described above.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** We used the Bullet collision checker [7] for convex-convex collision queries.

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional motion planning problems.를 문제로 두고, Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem that is solved at each optimization iteration.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
