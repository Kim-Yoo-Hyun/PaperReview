# GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 mains limited due to the lack of proper geometry priors.를 문제로 두고, Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily accessible 3D point clouds with supervisions from ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric ...
- **p. 1 / Abstract - extractive body cue:** Existing methods have explored predicting point maps as geometric references for inferring Gaussian primitives, while the unreliable estimated geometries may lead to poor generations.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily accessible 3D point clouds, naturally ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we design a textguided Gaussian growing scheme that leverages a multiview diffusion model to synthesize consistent appearances from input point clouds for supervision.
- **p. 1 / Abstract - extractive body cue:** To mitigate artifacts caused by fusing neighboring views, we constrain novel views generated at non-preset camera poses identified in overlapping regions across different views.
- **p. 2 / 1. Introduction - extractive body cue:** mains limited due to the lack of proper geometry priors.
- **p. 2 / 1. Introduction - extractive body cue:** The overlapping regions across different generated views often cause artifacts due to challenges in fusing Gaussian primitives.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily ...
- **p. 2 / 1. Introduction - extractive body cue:** Bridging the gap between point cloud geometries and 3D Gaussian Splatting appearances, we introduce a novel perspective that rethinks Gaussian generation by growing 3D Gaussians ...
- **p. 3 / 3. Method - extractive body cue:** We present GaussianGrow, a novel generative model for 3D Gaussian Splatting by learning to grow 3D Gaussians from 3D point cloud geometries.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** Our method begins by identifying critical overlap regions where the inconsistencies are most pronounced.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** A spatial Gaussian inpainting strategy is also used to diffuse appearance from optimized Gaussians to the hard-to-observe ones. we propose a dense-view generation framework that ...
- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** To systematically identify the unseen regions, we propose a visibility-based optimization approach that predicts camera poses observing the largest invisible regions in the point cloud.
- **p. 5 / 3.2. Appearance Generation - extractive body cue:** Our optimization strategy follows a two-phase approach that first addresses the six cardinal views V = {vi}6 i=1 before focusing on overlap regions.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** To optimize these poses for enhanced appearance generation, we make them learnable through an optimization strategy that enforces alignment between the normal vectors of intersecting ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | UDF Field Multi-View Diffusion Stable Diffusion ControlNet "Black and Red Dragon" Depth Map Input Point Clouds Normal Maps Position Maps Primary View Pose Optimization for Overlap Regions Overlap Detection Stage 1: Appearance ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Appearance Generation), p. 3 (3.1. Preliminary Preparation) |
| State/latent | UDF, Field, Multi-View, Diffusion, Stable, ControlNet, Black, Red, Dragon, Depth, Map, Input | geometry, map, object/relationship state | p. 4 (3.2. Appearance Generation), p. 3 (3.1. Preliminary Preparation), p. 6 (3.3. Iterative Inpainting and Refinement) |
| Output/action | To extract comprehensive geometric information from the input point cloud, we compute three geometric representation maps: depth, normal, and position maps, each serving a distinct purpose in our pipeline. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminary Preparation), p. 6 (3.3. Iterative Inpainting and Refinement), p. 3 (3. Method) |
| Objective/outcome | This differentiable formulation enables efficient gradient descent optimization of learnable camera poses, enabling the systematic discovery of viewpoints that reveal largest unseen regions of the object. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.3. Iterative Inpainting and Refinement), p. 3 (3.1. Preliminary Preparation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily ...
- **p. 2 / 1. Introduction - extractive body cue:** Bridging the gap between point cloud geometries and 3D Gaussian Splatting appearances, we introduce a novel perspective that rethinks Gaussian generation by growing 3D Gaussians ...
- **p. 3 / 3. Method - extractive body cue:** We present GaussianGrow, a novel generative model for 3D Gaussian Splatting by learning to grow 3D Gaussians from 3D point cloud geometries.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** Our method begins by identifying critical overlap regions where the inconsistencies are most pronounced.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** A spatial Gaussian inpainting strategy is also used to diffuse appearance from optimized Gaussians to the hard-to-observe ones. we propose a dense-view generation framework that ...
- **p. 7 / 4.2. Text-to-3D Generation - extractive body cue:** Moreover, applying the geometry of LGM to GaussianGrow also achieves significantly better performance by replacing the appearance of LGM with GaussianGrow.
- **p. 7 / 4.2. Text-to-3D Generation - extractive body cue:** The results demonstrate that GaussianGrow significantly outperforms previous methods in terms of appearance generation, and a stronger geometric setting leads to better generation quality.
- **p. 6 / 4. Experiments - extractive body cue:** In this section, we present a comprehensive evaluation of GaussianGrow's performance across multiple scenarios.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Text-to-3D Generation), p. 7 (4.2. Text-to-3D Generation) |
| Embodiment/environment | To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974 | hardware/simulator version and reset protocol | p. 7 (4.3. Point to Gaussian Generation), p. 7 (4.2. Text-to-3D Generation) |
| Dataset/benchmark | Quantitative comparison on the Objaverse dataset. | role, split, size and leakage | p. 7 (4.3. Point to Gaussian Generation), p. 7 (4.2. Text-to-3D Generation), p. 6 (4. Experiments), p. 6 (4.1. Text-Guided Visual Synthesis) |
| Metric | For quantitative evaluation, we employ three complementary metrics: Fr´echet Inception Distance (FID) [19] and Kernel Inception Distance (KID ×10-3) [3] to assess image quality, while the alignment between generated content and textual ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Text-Guided Visual Synthesis), p. 7 (4.2. Text-to-3D Generation), p. 7 (4.1. Text-Guided Visual Synthesis) |
| Baseline/ablation | The retrieve-based GaussianGrow "Ours+Uni3D" achieves the best performance across all evaluation metrics, while the generative-based version "Ours+LGM" also achieves comparable performance compared to the state-of-the-art method DiffSplat. | fair input/data/compute/action matching | p. 7 (4.2. Text-to-3D Generation), p. 7 (4.1. Text-Guided Visual Synthesis), p. 8 (4.3. Point to Gaussian Generation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Spatial Inpainting. Due to noises and uneven density in the raw point cloud data, some points may remain difficult to observe after image ...
- **p. 7 / 4.3. Point to Gaussian Generation - extractive body cue:** To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974
- **p. 8 / 4.3. Point to Gaussian Generation - extractive body cue:** These scans present challenging characteristics including noise and varying point densities.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** 4, using only the six cardinal views leads to clear degradation across all metrics, while adding four views focused on key overlap regions yields the ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 mains limited due to the lack of proper geometry priors.를 문제로 두고, Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily accessible 3D point clouds with supervisions from ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), p. 3 (3.2. Appearance Generation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
