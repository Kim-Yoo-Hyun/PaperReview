# FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While generalizable reconstruction models[5, 23, 57] address sparse-view reconstruction using learned priors in a feed-forward manner, they still require accurate camera parameters, sidestepping a fundamental challenge in real-world app ...를 문제로 두고, We introduce FreeSplatter, a feed-forward reconstruction framework that jointly predicts pixel-wise Gaussians from uncalibrated sparse-view images and estimates their camera parameters.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Sparse-view reconstruction models typically require precise camera poses, yet obtaining these parameters from sparse-view images remains challenging.
- **p. 1 / Abstract - extractive body cue:** We introduce FreeSplatter, a scalable feed-forward framework that generates high-quality 3D Gaussians from uncalibrated sparse-view images while estimating camera parameters within seconds.
- **p. 1 / Abstract - extractive body cue:** Our approach employs a streamlined transformer architecture where self-attention blocks facilitate information exchange among multi-view image tokens, decoding them into pixel-aligned 3D Gaussian primitives within ...
- **p. 1 / Abstract - extractive body cue:** This representation enables both high-fidelity 3D modeling and efficient camera parameter estimation using off-the-shelf solvers.
- **p. 1 / Abstract - extractive body cue:** We develop two specialized variants-for object-centric and scene-level reconstruction-trained on comprehensive datasets.
- **p. 1 / 1. Introduction - extractive body cue:** While generalizable reconstruction models[5, 23, 57] address sparse-view reconstruction using learned priors in a feed-forward manner, they still require accurate camera parameters, sidestepping a fundamental ...
- **p. 2 / 1. Introduction - extractive body cue:** Despite their pioneering contributions, their approaches suffer from inefficient volume rendering and limited resolution, hampering training efficiency and scalability to complex scenes.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We introduce FreeSplatter, a feed-forward reconstruction framework that jointly predicts pixel-wise Gaussians from uncalibrated sparse-view images and estimates their camera parameters.
- **p. 7 / 0.027 Method - extractive body cue:** Qualitative comparisons in Figure 4 reveal superior detail preservation by our method, particularly evident in text rendering (4th column), while competitors exhibit blurring artifacts.
- **p. 2 / 1. Introduction - extractive body cue:** Despite their pioneering contributions, their approaches suffer from inefficient volume rendering and limited resolution, hampering training efficiency and scalability to complex scenes.
- **p. 7 / 0.027 Method - extractive body cue:** Our end-to-end training approach enables joint optimization of Gaussian parameters, resulting in superior visual fidelity on both ScanNet++ and CO3Dv2 datasets (Figure 5).
- **p. 3 / 3.2. Model Architecture - extractive body cue:** These maps enable novel view synthesis and camera parameter recovery through iterative optimization.
- **p. 5 / 3.3. Training Details - extractive body cue:** The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm ...
- **p. 8 / 4.5. Applications in 3D AIGC - extractive body cue:** In our supplementary material (Section 2.4), we provide comprehensive image-to3D generation results across a range of multi-view diffusion models, demonstrating that FreeSplatter achieves superior reconstruction ...
- **p. 3 / 3.2. Model Architecture - extractive body cue:** As Figure 2 shows, FreeSplatter adopts a transformer architecture inspired by GS-LRM [65].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input Images Ours (Render w/ pred. poses) PF-LRM (Render w/ pred. poses) Novel G.T. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Model Architecture), p. 8 (4.5. Applications in 3D AIGC) |
| State/latent | Input, Images, Ours, Render, pred, poses, PF-LRM, Novel, supplementary, material, Section, provide | geometry, map, object/relationship state | p. 4 (3.2. Model Architecture), p. 8 (4.5. Applications in 3D AIGC), p. 3 (3.2. Model Architecture) |
| Output/action | In our supplementary material (Section 2.4), we provide comprehensive image-to3D generation results across a range of multi-view diffusion models, demonstrating that FreeSplatter achieves superior reconstruction performance compared to ... | point map, pose, scene graph, affordance 또는 query result | p. 8 (4.5. Applications in 3D AIGC), p. 3 (3.2. Model Architecture), p. 3 (3. Method) |
| Objective/outcome | The overall training objective is: \mathca l { L } = \m a thcal {L} _ {\mathrm {render}} + \lambda _\mathrm {a} \cdot \mathcal {L}_\mathrm {align} + \1_\mathrm {t\le T_\mathrm {max}} \lambda ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Training Details), p. 5 (3.3. Training Details), p. 3 (3.2. Model Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We introduce FreeSplatter, a feed-forward reconstruction framework that jointly predicts pixel-wise Gaussians from uncalibrated sparse-view images and estimates their camera parameters.
- **p. 7 / 0.027 Method - extractive body cue:** Qualitative comparisons in Figure 4 reveal superior detail preservation by our method, particularly evident in text rendering (4th column), while competitors exhibit blurring artifacts.
- **p. 2 / 1. Introduction - extractive body cue:** Despite their pioneering contributions, their approaches suffer from inefficient volume rendering and limited resolution, hampering training efficiency and scalability to complex scenes.
- **p. 7 / 0.027 Method - extractive body cue:** Our end-to-end training approach enables joint optimization of Gaussian parameters, resulting in superior visual fidelity on both ScanNet++ and CO3Dv2 datasets (Figure 5).
- **p. 3 / 3.2. Model Architecture - extractive body cue:** These maps enable novel view synthesis and camera parameter recovery through iterative optimization.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation and ...
- **p. 5 / 4. Experiments - extractive body cue:** Please refer to the supplementary material for additional implementation details and experimental results.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Scene-level performance is assessed on the test splits of ScanNet++[62] and CO3Dv2 [37].

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 5 (4. Experiments) |
| Embodiment/environment | FreeSplatterS leverages a diverse training set comprising BlendedMVS [61], ScanNet++[62], and CO3Dv2[37]-a subset of DUSt3R's [51] training data encompassing outdoor scenes, indoor environments, and real-world objects. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Settings), p. 5 (4. Experiments) |
| Dataset/benchmark | Scene-level performance is assessed on the test splits of ScanNet++[62] and CO3Dv2 [37]. | role, split, size and leakage | p. 5 (4.1. Experimental Settings), p. 5 (4. Experiments), p. 6 (4.1. Experimental Settings), p. 6 (4.2. Sparse-view Reconstruction) |
| Metric | Table 5. Ablation Study on Model Architecture. The results are evaluated on the GSO dataset with FreeSplatter-O. uate pose estimation performance using both rotation and translation metrics: relative rotation error (RRE) in ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (4.1. Experimental Settings), p. 5 (Figure/Table caption) |
| Baseline/ablation | Prior pose-free object reconstruction approaches like LEAP [26] exhibits limited generalization due to its small-scale training, while PF-LRM [49] is highly relevant and serves as our baseline for both object-level reconstruction and ... | fair input/data/compute/action matching | p. 6 (4.2. Sparse-view Reconstruction), p. 5 (4.1. Experimental Settings), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Sparse-view Reconstruction on PF-LRM's Evaluation Datasets. FreeSplatter-O synthesizes significantly better visual details than PF-LRM. The 1st row is from the GSO dataset, while ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Sparse-view Reconstruction on GSO dataset. * indi- cates that ground truth camera poses are used as input. at other pixels remain unconstrained. Besides, ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While generalizable reconstruction models[5, 23, 57] address sparse-view reconstruction using learned priors in a feed-forward manner, they still require accurate camera parameters, sidestepping a fundamental challenge in real-world app ...를 문제로 두고, We introduce FreeSplatter, a feed-forward reconstruction framework that jointly predicts pixel-wise Gaussians from uncalibrated sparse-view images and estimates their camera parameters.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Training Details), p. 8 (4.5. Applications in 3D AIGC), p. 3 (3.2. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
