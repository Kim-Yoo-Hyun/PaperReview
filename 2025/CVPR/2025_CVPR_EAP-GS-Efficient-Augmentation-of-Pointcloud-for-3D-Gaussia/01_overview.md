# EAP-GS: Efficient Augmentation of Pointcloud for 3D Gaussian Splatting in Few-shot Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In practice, a sufficient number of images are often difficult to obtain due to various limitations.를 문제로 두고, Therefore, we propose a pointcloud generation method specifically designed for 3DGS initialization, which significantly increases the number of initial points.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3DGS) has shown impressive performance in 3D scene reconstruction.
- **p. 1 / Abstract - extractive body cue:** However, it suffers from severe degradation when the number of training views is limited, resulting in blur and floaters.
- **p. 1 / Abstract - extractive body cue:** Many works have been devoted to standardize the optimization process of 3DGS through regularization techniques.
- **p. 1 / Abstract - extractive body cue:** However, we identify that inadequate initialization is a critical issue overlooked by current studies.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose EAP-GS, a method to enhance initialization for fast, accurate, and stable few-shot scene reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** In practice, a sufficient number of images are often difficult to obtain due to various limitations.
- **p. 2 / 1. Introduction - extractive body cue:** With a lack of coherence between Gaussians , their attributes can only be optimized individually via image supervision.

## Core Idea

- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** Therefore, we propose a pointcloud generation method specifically designed for 3DGS initialization, which significantly increases the number of initial points.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • A key insight that inadequate initialization can lead to poor performance in few-shot optimization, which is ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose an easy-to-implement attentional pointcloud augmentation technique to improve the accuracy of 3DGS reconstruction.
- **p. 4 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** The input to reconstruction stage consists of the n scene views I = {Ii ∈RH×W/i = 1, ..., n} and 16501
- **p. 4 / 3. Method - extractive body cue:** 3.2, we present an Attentional Pointcloud Augmentation technique to effectively increase the number of initial points and harmonize the overall pointcloud density distribution of the ...
- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** In this work, we implement our algorithm based on DetectorfreeSfM [11], which leverages a detector-free matcher to enhance feature extraction in texture-poor scenarios.
- **p. 4 / 3.1. Preliminary - extractive body cue:** The optimization process involves splatting 3D Gaussian into the image domain, sorting the N 2D Gaussians on the pixel by depth, and then calculating the ...
- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** Specifically, based on the pointcloud density distribution in the view Ii, we delineate an attention region Mi: \ ma t hbf {M} _i = \mathbf ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | After a new image registration, bundle adjustment is performed to refine the parameters of camera pose Pi and 3D point X to minimizes the reprojection error and filter observations with large errors: ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.2. Attentional Pointcloud Augmentation) |
| State/latent | After, image, registration, bundle, adjustment, performed, refine, parameters, camera, pose, point, minimizes | geometry, map, object/relationship state | p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.2. Attentional Pointcloud Augmentation), p. 5 (3.2. Attentional Pointcloud Augmentation) |
| Output/action | The input to reconstruction stage consists of the n scene views I = {Ii ∈RH×W/i = 1, ..., n} and 16501 | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Attentional Pointcloud Augmentation), p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.1. Preliminary) |
| Objective/outcome | It is important to note that without sufficient supervised views to provide constraints, simply using this 3D feature point generation mechanism may degrade reconstruction results in certain regions of the scene. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.1. Preliminary), p. 5 (3.2. Attentional Pointcloud Augmentation) |

## Main Claims and Actual Contribution

- **p. 5 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** Therefore, we propose a pointcloud generation method specifically designed for 3DGS initialization, which significantly increases the number of initial points.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • A key insight that inadequate initialization can lead to poor performance in few-shot optimization, which is ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose an easy-to-implement attentional pointcloud augmentation technique to improve the accuracy of 3DGS reconstruction.
- **p. 4 / 3.2. Attentional Pointcloud Augmentation - extractive body cue:** The input to reconstruction stage consists of the n scene views I = {Ii ∈RH×W/i = 1, ..., n} and 16501
- **p. 4 / 3. Method - extractive body cue:** 3.2, we present an Attentional Pointcloud Augmentation technique to effectively increase the number of initial points and harmonize the overall pointcloud density distribution of the ...
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** APA significantly improves the overall number and distribution of initial points, resulting in more accurate and reasonable scene geometry.
- **p. 7 / 4.2. Experimental Results - extractive body cue:** Our method achieves leading scores across all metrics while using fewer Gaussians and requiring less computation time.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison of the FSGS [41] and our proposed EAP-GS with 12 training views. With Attentional Pointcloud Augmenta- tion technique, our method generates significantly ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Ablation Studies), p. 2 (Figure/Table caption) |
| Embodiment/environment | We evaluated our method on all scenes of the LLFF [21] and Mip-NeRF360 dataset [1]. | hardware/simulator version and reset protocol | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.2. Experimental Results) |
| Dataset/benchmark | Quantitative results on LLFF and Mip-NeRF360 datasets. | role, split, size and leakage | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 7 (4.2. Experimental Results) |
| Metric | Best score and second-best score are in red and orange respectively. | definition, denominator, direction and uncertainty | p. 7 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | We configured COLMAP [28] with the same parameters as FSGS for the initialization of various baselines. | fair input/data/compute/action matching | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.1. Dataset and Implementation Details), p. 7 (4.3. Ablation Studies) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Discussion - extractive body cue:** Lacking a method to limit the error may be a limitation Figure 7.
- **p. 8 / 5. Discussion - extractive body cue:** This issue is primarily due to data incompleteness, and a potential approach to further enhance performance would be to incorporate prior knowledge or generative models ...
- **p. 7 / 4.2. Experimental Results - extractive body cue:** Similar results are obtained for unknown camera-poses though we did not report here because of space limitation.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In practice, a sufficient number of images are often difficult to obtain due to various limitations.를 문제로 두고, Therefore, we propose a pointcloud generation method specifically designed for 3DGS initialization, which significantly increases the number of initial points.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.1. Preliminary), p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.1. Preliminary) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
