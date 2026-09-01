# Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2403.02751.
> PDF retrieval source: https://arxiv.org/pdf/2403.02751. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, Navigation, Gaussian Splatting
- Official paper: https://arxiv.org/abs/2403.02751
- Full-text retrieval: https://arxiv.org/pdf/2403.02751
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the scene, making them impractical for ...를 문제로 두고, The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • We develop ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation.
- **p. 1 / Abstract - extractive body cue:** Splat-Nav consists of two components: 1) Splat-Plan, a safe planning module, and 2) Splat-Loc, a robust vision-based pose estimation module.
- **p. 1 / Abstract - extractive body cue:** Splat-Plan builds a safeby-construction polytope corridor through the map based on mathematically rigorous collision constraints and then constructs a B´ezier curve trajectory through this corridor.
- **p. 1 / Abstract - extractive body cue:** Splat-Loc provides real-time recursive state estimates given only an RGB feed from an on-board camera, leveraging the point-cloud representation inherent in GSplat scenes.
- **p. 1 / Abstract - extractive body cue:** Working together, these modules give robots the ability to recursively re-plan smooth and safe trajectories to goal locations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Similarly, we find that Splat-Loc is more accurate, faster, and fails less often compared to baselines.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce Splat-Nav, a pipeline for drone navigation in GSplat maps with a monocular camera.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Additionally, the proposed system enables both open-loop trajectory generation and closed-loop re-planning.
- **p. 4 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Now, we present Splat-Plan, our planner for GSplat maps.
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** We propose to solve maxs∈[0,1] K(s) using Algorithm 1.
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** While there are many ways one could convert the ellipsoidal representation into a conservative occupancy grid, we propose the following method that is parallelizable and ...
- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** (7f) Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a trajectory that can ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for i ←0 to k do // Test ... | camera/depth stream, pose, map와 language goal | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 1 (I. INTRODUCTION) |
| State/latent | Algorithm, Bisection, Search, Input, number, iterations, Output, maximal, estimator, Initialize, lower, upper | robot pose, free-space/semantic map와 local goal | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | Splat-Nav comprises a lightweight pose estimation module, Splat-Loc, coupled with a planning module, Splat-Plan, to enable safe navigation from RGB-only (monocular) camera observations, as illustrated in Figure 1. | collision-free trajectory 또는 velocity command | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | 4) Spline Optimization: Given the safe flight corridor represented as P polytopes and initial and final configurations (x0, xf), we compute a set of P B´ezier curves (parametrized by M + 1 ... | goal reach, safety, localization error와 replanning latency | p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce Splat-Nav, a pipeline for drone navigation in GSplat maps with a monocular camera.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Additionally, the proposed system enables both open-loop trajectory generation and closed-loop re-planning.
- **p. 4 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Now, we present Splat-Plan, our planner for GSplat maps.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate.
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level of ...
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** The GS-Loc algorithm achieves the lowest accuracy and requires the greatest computation time, unlike Colored-ICP, Splat-Loc-SIFT, and Splat-Loc-Glue, which achieve much-higher accuracy with a rotation ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS) |
| Embodiment/environment | Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, Flightroom, and Old Union. | hardware/simulator version and reset protocol | p. 10 (VI. EXPERIMENTS), p. 10 (VI. EXPERIMENTS) |
| Dataset/benchmark | In the simulated tests, we represent the robot using balls of various sizes in order to generate interesting trajectories due to the fact that the simulated scenes are not trained in metric ... | role, split, size and leakage | p. 10 (VI. EXPERIMENTS), p. 10 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 12 (VI. EXPERIMENTS) |
| Metric | We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation time (C.T.) per frame, and the overall success rate (S.R.). | definition, denominator, direction and uncertainty | p. 11 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 14 (VI. EXPERIMENTS) |
| Baseline/ablation | Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full scene geometry. | fair input/data/compute/action matching | p. 11 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 12 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate.
- **p. 16 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless regions of the scene where the PnP-RANSAC ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation. In Splat-Plan ...
- **p. 15 / VII. CONCLUSION - extractive body cue:** Splat-Nav consists of a guaranteed-safe planning module Splat-Plan, which allows for real-time planning (> 2 Hz) by leveraging the ellipsoidal representation inherent in GSplats for ...
- **p. 17 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Given a test point x∗and the jth ellipsoid in the collision test set G∗, we can use our collision test (Corollary 2) to derive these ...
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** All other methods have failures, other than NeRF-Nav by virtue of it being an end-to-end optimization method.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the scene, making them impractical for ...를 문제로 두고, The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • We develop ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
