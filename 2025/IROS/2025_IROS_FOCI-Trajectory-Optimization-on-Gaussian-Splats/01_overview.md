# FOCI: Trajectory Optimization on Gaussian Splats

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2505.08510.
> PDF retrieval source: https://arxiv.org/pdf/2505.08510. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Gaussian Splatting
- Official paper: https://arxiv.org/abs/2505.08510
- Full-text retrieval: https://arxiv.org/pdf/2505.08510
- Code/Project: https://rffr.leggedrobotics.com/works/foci/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two functions - as a proxy measure for ...를 문제로 두고, In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods.
- **p. 1 / Abstract - extractive body cue:** Leveraging the spatial information encoded in 3DGS, this work proposes FOCI (Field Overlap Collision Integral), an algorithm that is able to optimize trajectories directly on ...
- **p. 1 / Abstract - extractive body cue:** FOCI leverages a novel and interpretable collision formulation for 3DGS using the notion of the overlap integral between Gaussians.
- **p. 1 / Abstract - extractive body cue:** Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment ...
- **p. 1 / Abstract - extractive body cue:** This not only has desirable computational properties, but also allows for orientation-aware planning, allowing the robot to pass through very tight and narrow spaces.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although some steps have been taken in this direction [3], [4], [5], the huge number of Gaussians a scene can have, together with the specific ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work are therefore summarized as follows: • A novel collision measure between Gaussian Splats based on the overlap integral between Gaussians. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 3 / III. METHOD - extractive body cue:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.
- **p. 6 / Method - extractive body cue:** Runtime We evaluate the performance of our method by comparing the runtimes of the Casadi optimization on a single CPU core, multiple CPU cores, and ...
- **p. 3 / III. METHOD - extractive body cue:** The spline can then be evaluated with x(s′) =  1 s′ s′2 s′3 1 6   1 4 1 0 -3 0 3 ...
- **p. 4 / III. METHOD - extractive body cue:** The optimization problem is then solved via the interior point method (IPOPT) [28] with the custom overlap integral functor.
- **p. 4 / III. METHOD - extractive body cue:** Instead of directly constraining samples of the respective derivatives of the spline along the trajectory, we leverage the convex hull property of splines.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the velocity and acceleration control points, to guarantee constraint satisfaction along ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (III. METHOD), p. 6 (Method) |
| State/latent | Since, spline, segment, lies, within, convex, hull, control, points, enough, constrain, norm | geometry, map, object/relationship state | p. 4 (III. METHOD), p. 6 (Method), p. 3 (III. METHOD) |
| Output/action | In comparisons with similar methods (Table III, Figure 7) we are able to surpass the speed of traditional methods such as RRT* on large complex scenes, while having similar time performance to ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (Method), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Objective/outcome | We minimize the weighted sum of the obstacle cost, the jerk along the trajectory, and the distance of the final point to the goal with weights ω1 = 0.1, ω2 = 40 ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work are therefore summarized as follows: • A novel collision measure between Gaussian Splats based on the overlap integral between Gaussians. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 3 / III. METHOD - extractive body cue:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.
- **p. 6 / Method - extractive body cue:** Runtime We evaluate the performance of our method by comparing the runtimes of the Casadi optimization on a single CPU core, multiple CPU cores, and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation) |
| Embodiment/environment | Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning time for ... | hardware/simulator version and reset protocol | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation) |
| Dataset/benchmark | In this section, we evaluate our algorithm by applying it to planning problems in different environments represented by 3DGS. | role, split, size and leakage | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), p. 4 (IV. EXPERIMENTS) |
| Metric | As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free. | definition, denominator, direction and uncertainty | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), p. 6 (Figure/Table caption) |
| Baseline/ablation | Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one robot Gaussian. The "serial" method is on a single CPU ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. LIMITATIONS - extractive body cue:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.
- **p. 7 / V. LIMITATIONS - extractive body cue:** This means that when computing the overlap integral over the environment, flat regions with text or patterns have a slightly higher collision cost than
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free.
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can plan collision-free trajectories through splats that were created directly from the real-world environments.

## Why Read It

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two functions - as a proxy measure for ...를 문제로 두고, In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
