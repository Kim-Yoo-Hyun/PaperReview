# SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address outliers that cannot be aligned accurately due to depth discrepancies, we propose a Semantic Outlier Alignment step.를 문제로 두고, Our method, SPARS3R, can reliably render details in the foreground and background with accurate poses.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent efforts in Gaussian-Splat-based Novel View Synthesis can achieve photorealistic rendering; however, such capability is limited in sparse-view scenarios due to sparse initialization and over-fitting ...
- **p. 1 / Abstract - extractive body cue:** Recent progress in depth estimation and alignment can provide dense point cloud using few views; however, the resulting pose accuracy is suboptimal.
- **p. 1 / Abstract - extractive body cue:** In this work, we present SPARS3R, which combines the advantages of accurate pose estimation from Structure-from-Motion and dense point cloud from depth estimation.
- **p. 1 / Abstract - extractive body cue:** To this end, SPARS3R first performs a Global Fusion Alignment process that maps a prior dense point cloud to a sparse point cloud from Structure-from-Motion ...
- **p. 1 / Abstract - extractive body cue:** RANSAC is applied during this process to distinguish inliers and outliers.
- **p. 2 / 1. Introduction - extractive body cue:** To address outliers that cannot be aligned accurately due to depth discrepancies, we propose a Semantic Outlier Alignment step.
- **p. 2 / 1. Introduction - extractive body cue:** In practice, camera calibration obtained from multi-view depth alignment is often suboptimal due to the difficulties in estimating an accurate depth map.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Our method, SPARS3R, can reliably render details in the foreground and background with accurate poses.
- **p. 2 / 1. Introduction - extractive body cue:** To address sparse point cloud initialization and pose inaccuracy in sparse-view NVS, we propose SPARS3R.
- **p. 2 / 1. Introduction - extractive body cue:** To address outliers that cannot be aligned accurately due to depth discrepancies, we propose a Semantic Outlier Alignment step.
- **p. 3 / 3.2.1. Global Fusion Alignment - extractive body cue:** To construct a better point cloud prior, we propose to align MASt3R's point cloud with that from a SfM pipeline, which is more reliable based ...
- **p. 4 / 3.2.2. Semantic Outlier Alignment - extractive body cue:** Based on the observation that geometric inconsistencies between χ and sX tend to occur between objects and not within objects, we introduce an Interactive Segmentation ...
- **p. 5 / 3.2.3. Gaussian Optimization - extractive body cue:** Here we use Splatfacto, developed under the NeRFStudio framework [49]; the Gaussian optimization loss is: \la be l {E q :training _lo ss} \begin {gathered} ...
- **p. 3 / 3.2. SPARS3R - extractive body cue:** Firstly, SPARS3R performs SfM based on image correspondences, either from MASt3R [29] or other feature matching methods.
- **p. 3 / 3.1. Preliminary - extractive body cue:** X Y Z Global Fusion Alignment Semantic Outlier Alignment !𝑋!"#$$ 𝜒%#&& 𝜒!"#$$ !𝑋%#&& Gaussian Optimization MASt3R COLMAP Matching 𝜒 !𝑋 Interactive Segmentation Model Figure 2.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given K ą 2 input images, DUSt3R [52] aggregates across all pairwise pointmap predictions by globally aligning pairwise pointmaps into a unified point cloud χ. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Preliminary), p. 2 (3.1. Preliminary) |
| State/latent | Given, input, images, DUSt3R, aggregates, across, pairwise, pointmap, predictions, globally, aligning, pointmaps | geometry, map, object/relationship state | p. 3 (3.1. Preliminary), p. 2 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| Output/action | DUSt3R [52] is a two-view depth estimation method that produces dense 3D point clouds from image pairs. | point map, pose, scene graph, affordance 또는 query result | p. 2 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.2.2. Semantic Outlier Alignment) |
| Objective/outcome | Here we use Splatfacto, developed under the NeRFStudio framework [49]; the Gaussian optimization loss is: \la be l {E q :training _lo ss} \begin {gathered} \mathcal {L} = \lambda _1 \/ \tilde ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2.3. Gaussian Optimization), p. 4 (3.2.1. Global Fusion Alignment), p. 3 (3.1. Preliminary) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** Our method, SPARS3R, can reliably render details in the foreground and background with accurate poses.
- **p. 2 / 1. Introduction - extractive body cue:** To address sparse point cloud initialization and pose inaccuracy in sparse-view NVS, we propose SPARS3R.
- **p. 2 / 1. Introduction - extractive body cue:** To address outliers that cannot be aligned accurately due to depth discrepancies, we propose a Semantic Outlier Alignment step.
- **p. 3 / 3.2.1. Global Fusion Alignment - extractive body cue:** To construct a better point cloud prior, we propose to align MASt3R's point cloud with that from a SfM pipeline, which is more reliable based ...
- **p. 4 / 3.2.2. Semantic Outlier Alignment - extractive body cue:** Based on the observation that geometric inconsistencies between χ and sX tend to occur between objects and not within objects, we introduce an Interactive Segmentation ...
- **p. 5 / 4.1. Sparse NVS Evaluation - extractive body cue:** 1, these two improvements enhance camera alignment accuracy in both rotation and translation.
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** InstantSplat [14] uses DUSt3R's [52] dense point cloud and pose estimation and attempts to improve accuracy through a training pose optimization approach similar to BARF ...
- **p. 5 / 4.1. Sparse NVS Evaluation - extractive body cue:** Improvements over Procrustes Alignment baseline in average rotation error ER and translation error ET .

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.1. Sparse NVS Evaluation), p. 6 (4.2. Ablation Studies) |
| Embodiment/environment | Quantitative comparison of different NVS methods on 12 views on three popular benchmark datasets, totaling 24 scenes. | hardware/simulator version and reset protocol | p. 7 (4.3. Quantitative and Visual Evaluation), p. 5 (4. Experiments) |
| Dataset/benchmark | For this dataset, we follow the test set outlined in MipNeRF360 [2] and uniformly sample 12 images from the original training set to construct a sparse-view set. | role, split, size and leakage | p. 7 (4.3. Quantitative and Visual Evaluation), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.2. Ablation Studies) |
| Metric | Quantitative evaluation of pose accuracy across three datasets, Relative Translation Error (RPEt) and Relative Rotation Error (RPEr) [62] are calculated based on the normalized poses. | definition, denominator, direction and uncertainty | p. 6 (4.2. Ablation Studies), p. 3 (Figure/Table caption), p. 6 (4.2. Ablation Studies) |
| Baseline/ablation | Figure 4. Visual comparisons of different NVS methods on 12 views on Mip-NeRF 360 [2] dataset. Zooming in on the visualizations is recommended to show differences in detail. More visualizations for other ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 6 (4.1. Sparse NVS Evaluation), p. 5 (4.1. Sparse NVS Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Limitations - extractive body cue:** While SPARS3R significantly improves upon previous SoTA, there are also several limitations worth noting.
- **p. 8 / 5. Conclusion - extractive body cue:** We also introduce several improvements in the evaluation process to better represent the practical limitations in sparse-view registration and reconstruction.
- **p. 5 / 4. Experiments - extractive body cue:** Since sparse-view registration can be unstable due to limited pairs, we perform multiple SfMs and pick the outcome that maximizes successful triangulation per image.
- **p. 6 / 4.2. Ablation Studies - extractive body cue:** While it brings down the errors in some cases, such training pose optimization strategy does not work as well in more challenging datasets like Mip-NeRF ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Quantitative comparison of 3 and 6 views on Tanks & Temples and MVImgNet datasets. implicit and explicit scene representations. Specifically, 3DGS leverages SfM ...
- **p. 5 / 4.1. Sparse NVS Evaluation - extractive body cue:** Notably, it provides a robust assessment of rendering image quality under moderate pose shift, which frequently occurs in the realistic sparse-view 26814
- **p. 6 / 4.1. Sparse NVS Evaluation - extractive body cue:** Further details on DSIM's robustness as an evaluation metric are provided in the supplementary materials.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address outliers that cannot be aligned accurately due to depth discrepancies, we propose a Semantic Outlier Alignment step.를 문제로 두고, Our method, SPARS3R, can reliably render details in the foreground and background with accurate poses.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Preliminary), p. 5 (3.2.3. Gaussian Optimization) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
