# Problem - E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): This fundamental gap introduces several limitations on the robustness and accuracy of current pose-free approaches.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The emergence of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS) has advanced novel view synthesis (NVS).
- **p. 1 / Abstract - extractive PDF cue:** These methods, however, require high-quality RGB inputs and accurate corresponding poses, limiting robustness under real-world conditions such as fast camera motion or adverse lighting.
- **p. 1 / Abstract - extractive PDF cue:** Event cameras, which capture brightness changes at each pixel with high temporal resolution and wide dynamic range, enable precise sensing of dynamic scenes and offer ...
- **p. 1 / Abstract - extractive PDF cue:** However, existing event-based NVS methods either assume known poses or rely on depth estimation models that are bounded by their initial observations, failing to generalize ...
- **p. 1 / Abstract - extractive PDF cue:** We present E2EGS, a pose-free framework operating solely on event streams.
- **p. 2 / 1. Introduction - extractive PDF cue:** This fundamental gap introduces several limitations on the robustness and accuracy of current pose-free approaches.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address this limitation, IncEventGS [11] was introduced as a pose-free approach that follows simultaneous localization and mapping (SLAM) principles.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This fundamental gap introduces several limitations on the robustness and accuracy of current pose-free approaches. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | These volumetric representation methods typically take camera poses and 2D views as input, leveraging multiview images to learn implicit or explicit 3D ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | volumetric, representation, methods, typically, take, camera, poses, views, input, leveraging | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Despite, remarkable, success, approaches, fundamentally, assume, high-quality, input | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: volumetric, representation, methods, typically, take, camera, poses, views, input, leveraging | p. 1 (1. Introduction), p. 4 (3.2. Robust edge detection with patch-based tem), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: overcome, limitations, event-toedge, Gaussian, splatting, E2EGS, pose-free, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Edge-guided 3D reconstruction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: During, reconstruction, edge-guided, loss, spatially, weights, photometric, error | p. 4 (3.1. Framework overview), p. 5 (3.4. Edge-guided 3D reconstruction), p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.3. Edge-guided Gaussian initialization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Robust edge detection with patch-based tem), p. 5 (3.4. Edge-guided 3D reconstruction), p. 5 (3.4. Edge-guided 3D reconstruction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.4. Ablation study), p. 6 (4.3. Qualitative evaluations), p. 5 (4.2. Quantitative evaluations) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** To address this limitation, IncEventGS [11] was introduced as a pose-free approach that follows simultaneous localization and mapping (SLAM) principles.
- **p. 1 / 1. Introduction - extractive PDF cue:** This assumption makes them vulnerable to common real-world challenges, such as motion blur and adverse lighting conditions that frequently occur during rapid camera movements or ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, existing methods fail to effectively leverage these two complementary aspects together.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Edge-guided 3D reconstruction), p. 5 (3.3. Edge-guided Gaussian initialization), p. 1 (1. Introduction)): To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams.

- **p. 2 / 1. Introduction - extractive PDF cue:** By initializing Gaussians along detected edges and applying edge-weighted losses throughout optimization, our framework prioritizes geometric constraints over texture matching, enabling accurate pose estimation and ...
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive PDF cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- **p. 5 / 3.3. Edge-guided Gaussian initialization - extractive PDF cue:** Our method achieves superior reconstruction quality solely using event data. † denotes no depth supervision and ∗denotes that the method uses camera poses obtained through ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The high temporal resolution of event cameras enables precise capture of rapid scene dynamics, motivating numerous studies in trajectory estimation [10, 16, 20] and event-based ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Figure 4. Impact of trajectory error on reconstruction quality. (a) Ground truth. (b) IncEventGS exhibits multiple failure modes: ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Adaptive edge extraction methods that respond to local event statistics could address this limitation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | On real-world TUM-VIE sequences, IncEventGS† suffers from catastrophic failure due to the lack of geometric constraints in random ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | IncEventGS exhibits various failure modes in regions highlighted by red boxes, including wavelike artifacts in texture-less regions, missing ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 4 (3.2. Robust edge detection with patch-based tem), p. 1 (1. Introduction), p. 3 (3.1. Framework overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 4 (3.2. Robust edge detection with patch-based tem), p. 1 (1. Introduction), p. 3 (3.1. Framework overview), objective p. 4 (3.1. Framework overview), p. 5 (3.4. Edge-guided 3D reconstruction), p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.3. Edge-guided Gaussian initialization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
