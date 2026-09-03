# DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, despite incorporating geometric priors, InstantSplat lacks corresponding optimization in 3DGS, undermining the abundant priors.를 문제로 두고, To address these challenges, we introduce DroneSplat, a robust 3D gaussian splatting framework tailored for inthe-wild drone imagery.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Drones have become essential tools for reconstructing wild scenes due to their outstanding maneuverability.
- **p. 1 / Abstract - extractive body cue:** Recent advances in radiance field methods have achieved remarkable rendering quality, providing a new avenue for 3D reconstruction from drone imagery.
- **p. 1 / Abstract - extractive body cue:** However, dynamic distractors in wild environments challenge the static scene assumption in radiance fields, while limited view constraints hinder the accurate capture of underlying scene ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce DroneSplat, a novel framework designed for robust 3D reconstruction from in-the-wild drone imagery.
- **p. 1 / Abstract - extractive body cue:** Our method adaptively adjusts masking thresholds by integrating local-global segmentation heuristics with statistical approaches, enabling precise identification and elimination of dynamic distractors in static scenes.
- **p. 2 / 1. Introduction - extractive body cue:** However, despite incorporating geometric priors, InstantSplat lacks corresponding optimization in 3DGS, undermining the abundant priors.
- **p. 2 / 1. Introduction - extractive body cue:** However, applying NeRF or 3DGS to in-the-wild drone imagery presents several challenges for high-quality 3D reconstruction (Figure 2).

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DroneSplat, a robust 3D gaussian splatting framework tailored for inthe-wild drone imagery.
- **p. 2 / 1. Introduction - extractive body cue:** For the issue of viewpoint sparsity, our framework employs a multi-view stereo model to provide rich geometric priors by predicting dense 3D points.
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...
- **p. 7 / Method - extractive body cue:** Our method outperforms baseline methods on scenes with various numbers of dynamic distractors, while Ours(COLMAP) leading the rest.
- **p. 1 / 1. Introduction - extractive body cue:** Recently, radiance field methods, such as NeRF [23] and 3D Gaussian Splatting (3DGS) [11], have shown remarkable potential in 3D representation and novel view synthesis.
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** For each image Ii in the training set I, we use the segmentation model S to obtain S(Ii) = {m1 i , m2 i , ...
- **p. 5 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Specifically, we select a center point and four edge points of mj k as point prompts, which are then input into Segment Anything Model v2 ...
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** The training loss can be defined as follows: \m a thcal {L} = (1-\lambda _{dssim})\mathcal {M}\mathcal {L}_{\text {L1}} + \lambda _{dssim}\mathcal {M}\mathcal {L}_{\text {D-SSIM}} \label ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a few posed drone imagery of a wild scene, our goal is to identify and eliminate dynamic distractors. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking) |
| State/latent | Given, posed, drone, imagery, wild, scene, goal, identify, eliminate, dynamic, distractors, Specifically | geometry, map, object/relationship state | p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 7 (Method) |
| Output/action | Specifically, we select a center point and four edge points of mj k as point prompts, which are then input into Segment Anything Model v2 to initiate tracking. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.2. Adaptive Local-Global Masking), p. 7 (Method), p. 8 (Method) |
| Objective/outcome | 3DGS is optimized by a combination of D-SSIM [36] and L1 loss computed from the rendered color and the ground truth color: \m a thcal {L} = (1-\lambda _{dssim})\mathcal {L}_{\text {L1}} + ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Preliminaries), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 3 (3.2. Adaptive Local-Global Masking) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DroneSplat, a robust 3D gaussian splatting framework tailored for inthe-wild drone imagery.
- **p. 2 / 1. Introduction - extractive body cue:** For the issue of viewpoint sparsity, our framework employs a multi-view stereo model to provide rich geometric priors by predicting dense 3D points.
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...
- **p. 7 / Method - extractive body cue:** Our method outperforms baseline methods on scenes with various numbers of dynamic distractors, while Ours(COLMAP) leading the rest.
- **p. 1 / 1. Introduction - extractive body cue:** Recently, radiance field methods, such as NeRF [23] and 3D Gaussian Splatting (3DGS) [11], have shown remarkable potential in 3D representation and novel view synthesis.
- **p. 6 / 4.2. Comparison - extractive body cue:** Our method achieves the highest quantitative results, effectively eliminating dynamic distractors while preserving static details.
- **p. 6 / 4.2. Comparison - extractive body cue:** As shown in Figure 6 and Figure 7, our approach outperforms all baseline method on both DroneSplat(dynamic) datatset and NeRF On-the-go dataset.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 11. The ablations of Voxel-guided 3DGS on the Drone- splat(static) and UrbanScene3D dataset. The 1st , 2nd and 3rd best results are highlighted. 11, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (4.2. Comparison), p. 6 (4.2. Comparison) |
| Embodiment/environment | The On-the-go dataset [29] includes multiple casually captured scenes with varying ratios of occlusions. | hardware/simulator version and reset protocol | p. 6 (4.1. Setups), p. 6 (4.1. Setups) |
| Dataset/benchmark | The On-the-go dataset [29] includes multiple casually captured scenes with varying ratios of occlusions. | role, split, size and leakage | p. 6 (4.1. Setups), p. 6 (4.1. Setups) |
| Metric | Figure 1. Given a set of drone imagery, our method effectively eliminates the impact of dynamic distractors on the static scenes (e.g., vehicles driving on the road). The right side of the ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 6 (4.2. Comparison), p. 6 (4.2. Comparison) |
| Baseline/ablation | As shown in Figure 6 and Figure 7, our approach outperforms all baseline method on both DroneSplat(dynamic) datatset and NeRF On-the-go dataset. | fair input/data/compute/action matching | p. 6 (4.2. Comparison), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusions - extractive body cue:** We present DroneSplat, a novel framework for robust 3D reconstruction from in-the-wild drone imagery.
- **p. 8 / 5. Conclusions - extractive body cue:** Experimental evaluations across diverse datasets demonstrate the superiority and robustness of our approach over previous methods.
- **p. 6 / 4.2. Comparison - extractive body cue:** While RobustNeRF and NeRF On-the-go successfully remove distractors, they fail to retain fine details.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Given a set of drone imagery, our method effectively eliminates the impact of dynamic distractors on the static scenes (e.g., vehicles driving on ...
- **p. 6 / 4.1. Setups - extractive body cue:** The On-the-go dataset [29] includes multiple casually captured scenes with varying ratios of occlusions.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, despite incorporating geometric priors, InstantSplat lacks corresponding optimization in 3DGS, undermining the abundant priors.를 문제로 두고, To address these challenges, we introduce DroneSplat, a robust 3D gaussian splatting framework tailored for inthe-wild drone imagery.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Adaptive Local-Global Masking), p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
