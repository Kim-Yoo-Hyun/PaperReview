# Problem - SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=osxP6FafPZ; PDF retrieval source: https://openreview.net/pdf/ef221d27302d56bbadab6a1b5f71203b078ccc4f.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): However, this comes at the cost of limitations inherent to the rasterization paradigm.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Rigorous testing of autonomous robots, such as self-driving vehicles, is essential to ensure their safety in real-world deployments.
- **p. 1 / ABSTRACT - extractive PDF cue:** This requires building highfidelity simulators to test scenarios beyond those that can be safely or exhaustively collected in the real-world.
- **p. 1 / ABSTRACT - extractive PDF cue:** Existing neural rendering methods based on NeRF and 3DGS hold promise but suffer from low rendering speeds or can only render pinhole camera models, hindering ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Multi-sensor simulation poses additional challenges as existing methods handle cross-sensor inconsistencies by favoring the quality of one modality at the expense of others.
- **p. 1 / ABSTRACT - extractive PDF cue:** To overcome these limitations, we propose SimULi, the first method capable of rendering arbitrary camera models and LiDAR data in real-time.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, this comes at the cost of limitations inherent to the rasterization paradigm.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** As they are optimized to match real-world observations, they also exhibit a smaller domain gap compared to traditional artist-generated simulators.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, this comes at the cost of limitations inherent to the rasterization paradigm. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3.4 OPTIMIZATION We jointly optimize the camera particles Gc, LiDAR particles Gl, bilateral grids A, and the environment map by sampling a ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | OPTIMIZATION, jointly, optimize, camera, particles, LiDAR, bilateral, grids, environment, sampling | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | derive, automated, strategy, takes, elevation, angles, input, computes | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: OPTIMIZATION, jointly, optimize, camera, particles, LiDAR, bilateral, grids, environment, sampling | p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD) |
| Decision / output variable | geometry/map/query r; body terms: high-fidelity, efficient, reconstruction, pipeline, enables, joint, camera, LiDAR | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: minimize, reconstruction, loss, anchoring, encourages, camera, Gaussians, near | p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** As they are optimized to match real-world observations, they also exhibit a smaller domain gap compared to traditional artist-generated simulators.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHOD), p. 2 (1 INTRODUCTION)): In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2026 Contributions.
- **p. 5 / 3 METHOD - extractive PDF cue:** Particle Contributions and Response.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | The choice M = 32, Nε = 16 gives the best LiDAR rendering speed (note that does not ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 7 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 7 (3 METHOD), objective p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
