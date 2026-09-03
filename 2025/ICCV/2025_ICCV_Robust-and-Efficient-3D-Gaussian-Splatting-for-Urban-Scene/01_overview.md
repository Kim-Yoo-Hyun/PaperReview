# Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, its *Corresponding author explicit representation introduces scalability challenges, as spatial complexity increases with scene size.를 문제로 두고, The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale scene reconstruction. • A controllable LO ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a framework that enables fast reconstruction and real-time rendering of urban-scale scenes while maintaining robustness against appearance variations across multi-view captures.
- **p. 1 / Abstract - extractive body cue:** Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency.
- **p. 1 / Abstract - extractive body cue:** A controllable level-of-detail (LOD) strategy explicitly regulates Gaussian density under a user-defined budget, enabling efficient training and rendering while maintaining high visual fidelity.
- **p. 1 / Abstract - extractive body cue:** The appearance transformation module mitigates the negative effects of appearance inconsistencies across images while enabling flexible adjustments.
- **p. 1 / Abstract - extractive body cue:** Additionally, we utilize enhancement modules, such as depth regularization, scale regularization, and antialiasing, to improve reconstruction fidelity.
- **p. 1 / 1. Introduction - extractive body cue:** However, its *Corresponding author explicit representation introduces scalability challenges, as spatial complexity increases with scene size.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** Experimental results demonstrate that our method outperform existing methods in terms of reconstruction quality, resource efficiency, and rendering speed, enabling the reconstruction of arbitrarily large ...
- **p. 3 / 3.3. In-Partition Prioritized Densification - extractive body cue:** To solve this problem, as shown in Figure 2 we propose a distance-related threshold for each Gaussian: τi = ˆτmin
- **p. 4 / 3.4.1. Controllable Detail Level Generation - extractive body cue:** Experiments show that our method achieves higher quality than compression-based method while enabling faster completion by utilizing low-resolution images and a smaller budget for lower ...
- **p. 6 / 3.6. Loss of Individual Partition Training - extractive body cue:** The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3).
- **p. 5 / 3.5.1. Appearance Transform Module - extractive body cue:** We propose a fine-grained appearance transform module that assigns embeddings to both individual images and each 3D Gaussian independently.
- **p. 5 / 3.5.1. Appearance Transform Module - extractive body cue:** To prevent the model from unnecessarily overusing transparency to fit color variations, we introduce an additional regularization term for the opacity offset, restricting transparency changes ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For an unselected image Ii, the 3D point cloud of the scene is projected onto its image plane, and compute its convex hull area Vi. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail) |
| State/latent | unselected, image, point, cloud, scene, projected, onto, plane, compute, convex, hull, area | geometry, map, object/relationship state | p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail), p. 4 (3.5. Quality Enhancements) |
| Output/action | (a) Obtain the 3D point cloud and its corresponding 2D feature points through estimating camera poses by SfM. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.4. Controllable Level-of-detail), p. 4 (3.5. Quality Enhancements), p. 5 (3.5.1. Appearance Transform Module) |
| Objective/outcome | By optimizing the attributes of the Gaussians and carrying out densification to minimize this loss, 3DGS ultimately fulfills its goal of reconstructing the target scene. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Preliminary), p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.2. Scale Regularization) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** Experimental results demonstrate that our method outperform existing methods in terms of reconstruction quality, resource efficiency, and rendering speed, enabling the reconstruction of arbitrarily large ...
- **p. 3 / 3.3. In-Partition Prioritized Densification - extractive body cue:** To solve this problem, as shown in Figure 2 we propose a distance-related threshold for each Gaussian: τi = ˆτmin
- **p. 4 / 3.4.1. Controllable Detail Level Generation - extractive body cue:** Experiments show that our method achieves higher quality than compression-based method while enabling faster completion by utilizing low-resolution images and a smaller budget for lower ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** This model significantly improves all three quality metrics across all scenes.
- **p. 6 / 4.2. Results - extractive body cue:** This underscores our method's ability to achieve high-fidelity reconstructions of urban-scale scenes.
- **p. 6 / 4.2. Results - extractive body cue:** For quality-related metrics (SSIM, PSNR, and LPIPS), the results indicate that our method outperforms others.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.4. Ablation Study), p. 6 (4.2. Results) |
| Embodiment/environment | Notably, we also conducted validation using Building scene from Mega-NeRF [42] as well as Residences, Sci-Art and Campus scenes from UrbanScene3D [17], with results provided in the supplementary materials E.2. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 7 (4.3. LOD Generation) |
| Dataset/benchmark | We use three detail levels for these scenes. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 7 (4.3. LOD Generation), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study) |
| Metric | The only exception is the Rubble scene, where the LPIPS score matches that of CityGaussian. | definition, denominator, direction and uncertainty | p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.3. LOD Generation) |
| Baseline/ablation | Compared to other LOD-enabled methods, our method consistently outperforms previous approaches across all three quality-related metrics. | fair input/data/compute/action matching | p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.4. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future work could explore incremental switching mechanisms for smoother transitions and improved resource efficiency.
- **p. 8 / 5. Conclusion - extractive body cue:** Enhancing robustness to pose inaccuracies is thus an important future direction.
- **p. 6 / 4.2. Results - extractive body cue:** Meanwhile, the FPS does not experience a significant decline and consistently ranks as either the best or second-best, making real-time rendering entirely feasible.
- **p. 7 / 4.3. LOD Generation - extractive body cue:** However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an upper limit, and the scene may not ...
- **p. 6 / 4.2. Results - extractive body cue:** Meanwhile, the quality experiences only minimal degradation.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, its *Corresponding author explicit representation introduces scalability challenges, as spatial complexity increases with scene size.를 문제로 두고, The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale scene reconstruction. • A controllable LO ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.1. Appearance Transform Module) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
