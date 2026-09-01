# Problem - Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.02751; PDF retrieval source: https://arxiv.org/pdf/2403.02751. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the scene, making them impractical for ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation.
- **p. 1 / Abstract - extractive body cue:** Splat-Nav consists of two components: 1) Splat-Plan, a safe planning module, and 2) Splat-Loc, a robust vision-based pose estimation module.
- **p. 1 / Abstract - extractive body cue:** Splat-Plan builds a safeby-construction polytope corridor through the map based on mathematically rigorous collision constraints and then constructs a B´ezier curve trajectory through this corridor.
- **p. 1 / Abstract - extractive body cue:** Splat-Loc provides real-time recursive state estimates given only an RGB feed from an on-board camera, leveraging the point-cloud representation inherent in GSplat scenes.
- **p. 1 / Abstract - extractive body cue:** Working together, these modules give robots the ability to recursively re-plan smooth and safe trajectories to goal locations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Similarly, we find that Splat-Loc is more accurate, faster, and fails less often compared to baselines.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Algorithm, Bisection, Search, Input, number, iterations, Output, maximal, estimator, Initialize | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Given, incoming, RGB, frame, Splat-Loc, performs, Perspective-n-Point, PnP | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Algorithm, Bisection, Search, Input, number, iterations, Output, maximal, estimator, Initialize | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: contributions, follows, develop, fast, polytope, corridor, generation, algorithm | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Spline, Optimization, Given, safe, flight, corridor, represented, polytopes | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES) |
| Success / guarantee | goal reach with collision-free execution | p. 11 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 14 (VI. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** Similarly, we find that Splat-Loc is more accurate, faster, and fails less often compared to baselines.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We use a language-embedded GSplat to enable open-vocabulary specification of goal locations like "go to the microwave." of the existing localization module or used as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The latter is important in long trajectories, where existing onboard localization may drift or be subject to noise, impacting the overall safety of the executed ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. PLANNING WITH SAFE POLYTOPES)): The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce Splat-Nav, a pipeline for drone navigation in GSplat maps with a monocular camera.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Additionally, the proposed system enables both open-loop trajectory generation and closed-loop re-planning.
- **p. 4 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Now, we present Splat-Plan, our planner for GSplat maps.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
