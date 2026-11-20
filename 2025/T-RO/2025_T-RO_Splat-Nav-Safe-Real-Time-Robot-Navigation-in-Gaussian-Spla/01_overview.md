# Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); reviewed full-text source: https://arxiv.org/abs/2403.02751.
> PDF retrieval source: https://arxiv.org/pdf/2403.02751. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / T-RO (IEEE Transactions on Robotics; journal article)
- Publication: volume 41, pages 2765–2784; DOI `10.1109/TRO.2025.3552348`
- Authors: Timothy Chen, Ola Shorinwa, Joseph Bruno, Aiden Swann, Javier Yu, Weijia Zeng, Keiko Nagami, Philip Dames, Mac Schwager
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, Navigation, Gaussian Splatting
- Official paper: https://api.crossref.org/works/10.1109/tro.2025.3552348
- Preprint: https://arxiv.org/abs/2403.02751 (first submitted 2024-03-05; v3 2025-01-11)
- Full-text retrieval: https://arxiv.org/pdf/2403.02751
- Code/Project: https://chengine.github.io/splatnav/
- Conference presentation: IROS 2025, reported by the [author laboratory](https://sites.temple.edu/trail/publications/) separately from T-RO publication. Its linked [conference program](https://ras.papercept.net/conferences/conferences/IROS25/program/IROS25_ContentListWeb_3.html) could not be retrieved in this pass; oral/poster format remains unverified.
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- Metadata audit: 2026-10-23, publisher-deposited [Crossref DOI metadata](https://api.crossref.org/works/10.1109/TRO.2025.3552348), author laboratory, arXiv and linked project/code checked. DOI resolves to IEEE; its page requires a browser verification challenge. This correction preserves the earlier arXiv full-text analysis and user reading status; it is not a new journal-body review. [Correction record](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/SPLAT_NAV_METADATA_2026-10-23.md).

## Why This Paper Is Here

문제 관련 발췌 — NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the scene, making them impractical for ...

방법 관련 발췌 — The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • We develop ...

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the scene, making them impractical for ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Lastly, we examine the performance of the pose estimation algorithms in problems with a larger error in the initial estimate of the pose, with δR = 30◦and δt = 0.5 ... (p. 11, VI. EXPERIMENTS).
- **Explicit failure boundary:** More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. (p. 12, VI. EXPERIMENTS).
