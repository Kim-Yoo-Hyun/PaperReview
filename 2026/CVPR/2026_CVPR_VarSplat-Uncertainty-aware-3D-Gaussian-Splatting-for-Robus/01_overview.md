# VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.를 문제로 두고, In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render differentiable per-pixel uncertainty map V while maintaining ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Simultaneous Localization and Mapping (SLAM) with 3D Gaussian Splatting (3DGS) enables fast, differentiable rendering and high-fidelity reconstruction across diverse realworld scenes.
- **p. 1 / Abstract - extractive body cue:** However, existing 3DGS-SLAM approaches handle measurement reliability implicitly, making pose estimation and global alignment susceptible to drift in lowtexture regions, transparent surfaces, or areas with ...
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.
- **p. 1 / Abstract - extractive body cue:** By using the law of total variance with alpha compositing, we then render differentiable per-pixel uncertainty map via efficient, singlepass rasterization.
- **p. 1 / Abstract - extractive body cue:** This map guides tracking, submap registration, and loop detection toward focusing on reliable regions and contributes to more stable optimization.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 2 / 1. Introduction - extractive body cue:** Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render ...
- **p. 3 / 3. Method - extractive body cue:** To address these issues, we introduce a novel uncertainty quantification pipeline based on per-pixel uncertainty map rendering.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 4 / 3.1. Per-pixel uncertainty rendering - extractive body cue:** By sharing the same single-pass rasterization as color and depth, V enables efficient, online, in-the-loop reliability estimation.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive body cue:** Ltrack = X λc  f wp⊙∥ˆI -I∥1  +(1-λc)∥ˆD-D∥1 (17) where 0 ≤λc ≤1 balances the contribution between photometric and geometric losses, and f ...
- **p. 4 / 3.2. Mapping - extractive body cue:** To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar.
- **p. 4 / 3.2. Mapping - extractive body cue:** For color supervision, we use a weighted combination of L1 and SSIM [16], while depth loss is L1 between rendered and ground-truth depth.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive body cue:** Thanks to the explicit representation and the parallel optimization of poses and Gaussian parameters, we can simultaneously freeze the variance during tracking and registration, while ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | VarSplat is an RGB-D SLAM approach that jointly estimates camera poses and incrementally updates 3D Gaussian Splatting (3DGS) map from input frames, following the general pipeline of [48, 51]. | camera/depth stream, pose, map와 language goal | p. 3 (3. Method), p. 3 (3. Method) |
| State/latent | VarSplat, RGB-D, SLAM, jointly, estimates, camera, poses, incrementally, updates, Gaussian, Splatting, DGS | robot pose, free-space/semantic map와 local goal | p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Mapping) |
| Output/action | However, pose estimation through photometric optimization can suffer from unreliable observations in low-texture regions, reflective surfaces, and areas near depth discontinuities, which can destabilize this process and potential drift. | collision-free trajectory 또는 velocity command | p. 3 (3. Method), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping) |
| Objective/outcome | Therefore, optimizing a pure photometric loss for pose refinement can lead to unstable gradients. | goal reach, safety, localization error와 replanning latency | p. 5 (3.3. Downstream Pose Estimation), p. 5 (3.2. Mapping), p. 4 (3.2. Mapping) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render ...
- **p. 3 / 3. Method - extractive body cue:** To address these issues, we introduce a novel uncertainty quantification pipeline based on per-pixel uncertainty map rendering.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 4 / 3.1. Per-pixel uncertainty rendering - extractive body cue:** By sharing the same single-pass rasterization as color and depth, V enables efficient, online, in-the-loop reliability estimation.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive body cue:** Ltrack = X λc  f wp⊙∥ˆI -I∥1  +(1-λc)∥ˆD-D∥1 (17) where 0 ≤λc ≤1 balances the contribution between photometric and geometric losses, and f ...
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves the highest accuracy with robustness on large motion camera.
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** On ScanNet, VarSplat consistently achieves best performance against both neural implicit and 3DGS baselines.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves competitive results on both synthetic and real-world datasets.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation) |
| Embodiment/environment | In this section, we evaluate VarSplat against existing baselines on both synthetic and real-world datasets. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 7 (4.2. Quantitative Evaluation) |
| Dataset/benchmark | For fair comparison on ScanNet with common baselines [15, 45, 48], we report results on six scenes. | role, split, size and leakage | p. 6 (4. Experiments), p. 7 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation) |
| Metric | VarSplat achieves the highest accuracy with robustness on large motion camera. | definition, denominator, direction and uncertainty | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation) |
| Baseline/ablation | VarSplat outperforms both 3DGS and NeRF baselines. *Photo-SLAM [11] use ORB-SLAM3 features [2] for tracking and loop closure. | fair input/data/compute/action matching | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Ablation studies) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations and future works are provided in Supplementary Material.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** These results also show that using the per-pixel uncertainty map to regularize the photometric loss does not degrade mesh reconstruction quality.
- **p. 8 / 5. Conclusion - extractive body cue:** Across four datasets, this integration achieves robust and competitive-to-superior performance.
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** On ScanNet++, VarSplat improves ATE RMSE by about 18% over the second best method and ensures robustness in long sequences where others like SplaTAM fail ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. VarSplat. Given RGB-D inputs, each 3D Gaussian jointly learns position, orientation, scale, color, opacity, and appearance variance σ2. During mapping, σ2 is optimized ...
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves the highest accuracy with robustness on large motion camera.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves the best overall, showing robustness to noisy indoor scenes.

## Why Read It

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.를 문제로 두고, In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render differentiable per-pixel uncertainty map V while maintaining ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation), p. 5 (3.3. Downstream Pose Estimation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
