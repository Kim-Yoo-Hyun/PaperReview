# E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This fundamental gap introduces several limitations on the robustness and accuracy of current pose-free approaches.를 문제로 두고, To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The emergence of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS) has advanced novel view synthesis (NVS).
- **p. 1 / Abstract - extractive body cue:** These methods, however, require high-quality RGB inputs and accurate corresponding poses, limiting robustness under real-world conditions such as fast camera motion or adverse lighting.
- **p. 1 / Abstract - extractive body cue:** Event cameras, which capture brightness changes at each pixel with high temporal resolution and wide dynamic range, enable precise sensing of dynamic scenes and offer ...
- **p. 1 / Abstract - extractive body cue:** However, existing event-based NVS methods either assume known poses or rely on depth estimation models that are bounded by their initial observations, failing to generalize ...
- **p. 1 / Abstract - extractive body cue:** We present E2EGS, a pose-free framework operating solely on event streams.
- **p. 2 / 1. Introduction - extractive body cue:** This fundamental gap introduces several limitations on the robustness and accuracy of current pose-free approaches.
- **p. 1 / 1. Introduction - extractive body cue:** To address this limitation, IncEventGS [11] was introduced as a pose-free approach that follows simultaneous localization and mapping (SLAM) principles.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams.
- **p. 2 / 1. Introduction - extractive body cue:** By initializing Gaussians along detected edges and applying edge-weighted losses throughout optimization, our framework prioritizes geometric constraints over texture matching, enabling accurate pose estimation and ...
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive body cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- **p. 5 / 3.3. Edge-guided Gaussian initialization - extractive body cue:** Our method achieves superior reconstruction quality solely using event data. † denotes no depth supervision and ∗denotes that the method uses camera poses obtained through ...
- **p. 1 / 1. Introduction - extractive body cue:** The high temporal resolution of event cameras enables precise capture of rapid scene dynamics, motivating numerous studies in trajectory estimation [10, 16, 20] and event-based ...
- **p. 4 / 3.1. Framework overview - extractive body cue:** This edgeaware initialization and optimization jointly refine the 3D Gaussian representation and camera trajectory, enabling robust pose estimation and high-quality reconstruction even in extended real-world ...
- **p. 4 / 3.1. Framework overview - extractive body cue:** During reconstruction, an edge-guided loss spatially weights the photometric error based on edge confidence, prioritizing optimization at geometrically salient boundaries (Sec.
- **p. 3 / 3.1. Framework overview - extractive body cue:** We adopt 3DGS [13] as our scene representation, where each Gaussian primitive is parameterized by center position µ ∈R3, covariance Σ ∈R3×3, opacity o, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These volumetric representation methods typically take camera poses and 2D views as input, leveraging multiview images to learn implicit or explicit 3D scene representations. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 4 (3.2. Robust edge detection with patch-based tem) |
| State/latent | volumetric, representation, methods, typically, take, camera, poses, views, input, leveraging, multiview, images | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 4 (3.2. Robust edge detection with patch-based tem), p. 1 (1. Introduction) |
| Output/action | Edges with incorrectly estimated depth in previous frames can be identified and removed based on their inconsistency with current observations, ensuring only geometrically consistent edges guide subsequent Gaussian initialization and re ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Robust edge detection with patch-based tem), p. 1 (1. Introduction), p. 3 (3.1. Framework overview) |
| Objective/outcome | During reconstruction, an edge-guided loss spatially weights the photometric error based on edge confidence, prioritizing optimization at geometrically salient boundaries (Sec. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1. Framework overview), p. 3 (3.1. Framework overview), p. 4 (3.2. Robust edge detection with patch-based tem) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams.
- **p. 2 / 1. Introduction - extractive body cue:** By initializing Gaussians along detected edges and applying edge-weighted losses throughout optimization, our framework prioritizes geometric constraints over texture matching, enabling accurate pose estimation and ...
- **p. 5 / 3.4. Edge-guided 3D reconstruction - extractive body cue:** To leverage detected edges during reconstruction, we introduce an edge-guided loss that spatially weights the reconstruction error based on edge confidence.
- **p. 5 / 3.3. Edge-guided Gaussian initialization - extractive body cue:** Our method achieves superior reconstruction quality solely using event data. † denotes no depth supervision and ∗denotes that the method uses camera poses obtained through ...
- **p. 1 / 1. Introduction - extractive body cue:** The high temporal resolution of event cameras enables precise capture of rapid scene dynamics, motivating numerous studies in trajectory estimation [10, 16, 20] and event-based ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine details such as ...
- **p. 6 / 4.2. Quantitative evaluations - extractive body cue:** On synthetic Replica scenes, our edge-guided approach achieves sub-millimeter accuracy across all scenes.
- **p. 7 / 4.4. Ablation study - extractive body cue:** 3 shows the progressive improvement when adding our components to IncEventGS†.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative evaluations) |
| Embodiment/environment | IncEventGS† fails to reconstruct recognizable figurines and produces distorted scenes due to severe trajectory drift. | hardware/simulator version and reset protocol | p. 6 (4.3. Qualitative evaluations), p. 5 (4.1. Experiment settings) |
| Dataset/benchmark | 1 shows reconstruction quality on synthetic scenes. | role, split, size and leakage | p. 6 (4.3. Qualitative evaluations), p. 5 (4.1. Experiment settings), p. 5 (4.2. Quantitative evaluations), p. 6 (4.3. Qualitative evaluations) |
| Metric | Our edge-guided loss spatially weights reconstruction error by edge confidence, enabling rapid structure establishment and substantially clearer boundaries at convergence. | definition, denominator, direction and uncertainty | p. 7 (4.4. Ablation study), p. 6 (4.3. Qualitative evaluations), p. 5 (4.2. Quantitative evaluations) |
| Baseline/ablation | Our method produces sharper boundaries and cleaner surfaces compared with baselines. | fair input/data/compute/action matching | p. 7 (4.3. Qualitative evaluations), p. 6 (4.2. Quantitative evaluations), p. 5 (4.2. Quantitative evaluations) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Impact of trajectory error on reconstruction quality. (a) Ground truth. (b) IncEventGS exhibits multiple failure modes: spatial misalignment causing viewpoint shifts and blurred ...
- **p. 8 / 5. Conclusion - extractive body cue:** Adaptive edge extraction methods that respond to local event statistics could address this limitation.
- **p. 6 / 4.2. Quantitative evaluations - extractive body cue:** On real-world TUM-VIE sequences, IncEventGS† suffers from catastrophic failure due to the lack of geometric constraints in random initialization, causing pose optimization to converge to ...
- **p. 6 / 4.3. Qualitative evaluations - extractive body cue:** IncEventGS exhibits various failure modes in regions highlighted by red boxes, including wavelike artifacts in texture-less regions, missing fine details such as textures and patterns, ...
- **p. 7 / 4.3. Qualitative evaluations - extractive body cue:** IncEventGS shows failures including wave-like artifacts, missing details, and indistinct boundaries.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Edge-guided reconstruction framework. Our pipeline extracts robust edges from consecutive event maps (Sec. 3.2), initializes edge-aware Gaussians (Sec. 3.3), and applies edge-guided losses ...
- **p. 5 / 4.2. Quantitative evaluations - extractive body cue:** Without edge guidance, photometric error from event noise uniformly affects 3D reconstruction, causing optimization process to receive 4926

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This fundamental gap introduces several limitations on the robustness and accuracy of current pose-free approaches.를 문제로 두고, To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Edge-guided 3D reconstruction), p. 4 (3.1. Framework overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
