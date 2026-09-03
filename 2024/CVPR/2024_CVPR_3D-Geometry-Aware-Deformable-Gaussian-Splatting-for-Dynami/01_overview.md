# 3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In addressing the above challenges, one common strategy is to represent the dynamic scenes as a combination of a static canonical field and a deformation model [11, 16, 17, 27, 33, 34, ...를 문제로 두고, Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. • We propose to use continuous 6D ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a 3D geometry-aware deformable Gaussian Splatting method for dynamic view synthesis.
- **p. 1 / Abstract - extractive body cue:** Existing neural radiance fields (NeRF) based solutions learn the deformation in an implicit manner, which cannot incorporate 3D scene geometry.
- **p. 1 / Abstract - extractive body cue:** Therefore, the learned deformation is not necessarily geometrically coherent, which results in unsatisfactory dynamic view synthesis and 3D dynamic reconstruction.
- **p. 1 / Abstract - extractive body cue:** Recently, 3D Gaussian Splatting provides a new representation of the 3D scene, building upon which the 3D geometry could be exploited in learning the complex ...
- **p. 1 / Abstract - extractive body cue:** Specifically, the scenes are represented as a collection of 3D Gaussian, where each 3D Gaussian is optimized to move and rotate over time to model ...
- **p. 1 / 1. Introduction - extractive body cue:** In addressing the above challenges, one common strategy is to represent the dynamic scenes as a combination of a static canonical field and a deformation ...
- **p. 2 / 1. Introduction - extractive body cue:** However, this strategy has a limited cover range of local areas and cannot work at a later training stage.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. ...
- **p. 3 / 3. Method - extractive body cue:** Our method mainly consists of two core components: the Gaussian canonical field is used to learn the reconstruction of static scenes, while the deformation field ...
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.
- **p. 1 / 1. Introduction - extractive body cue:** Geometric information exploited by different methods. a) Early dynamic NeRF methods such as DNeRF[37] directly encode the coordinate p of the sample point as input ...
- **p. 2 / 1. Introduction - extractive body cue:** The Gaussian canonical field consists of 3D Gaussian distributions and a geometry-aware feature learning network.
- **p. 5 / 3.5. Optimization - extractive body cue:** To optimize the model, we use the photometric loss, and a motion loss, and also adapt the density control from 3DGS [21] with our modifications.
- **p. 5 / 3.5. Optimization - extractive body cue:** The photometric loss consists of the L1 loss and structural similarity loss LD-SSIM between the rendered image ˆCt and ground truth image Ct.
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Compared with the quaternion representation used in 3D-GS, the 6D rotation representation can benefit our method in estimating the deformation of each Gaussian from canonical ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Taking V as input, we perform sparse 3D U-Net to aggregate local features (dubbed as Fv ∈RM×C) of the point clouds. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method) |
| State/latent | Taking, input, perform, sparse, U-Net, aggregate, local, features, dubbed, point, clouds, Given | geometry, map, object/relationship state | p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method), p. 1 (1. Introduction) |
| Output/action | Given a set of images or monocular video of a dynamic scene with frames with corresponding time labels and known camera intrinsic and extrinsic parameters, our goal is to synthesize a novel ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | Gaussian Canonical Field Deformation Field RGB Gradient 𝑓𝑡 -1(Δ𝑥𝑡, Δ𝑟𝑡, Δ𝑠𝑡) (𝑥𝑡,𝑐, 𝑟𝑡,𝑠𝑡, o) 𝑓𝑡(Δ𝑥𝑡, Δ𝑟𝑡,Δ𝑠𝑡) Deformation Transformation Inverse Deformation Transformation Loss Density Control Figure 3. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Rasterization), p. 5 (3.5. Optimization), p. 3 (3. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. ...
- **p. 3 / 3. Method - extractive body cue:** Our method mainly consists of two core components: the Gaussian canonical field is used to learn the reconstruction of static scenes, while the deformation field ...
- **p. 4 / 3.2. Gaussian Canonical Field - extractive body cue:** Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.
- **p. 1 / 1. Introduction - extractive body cue:** Geometric information exploited by different methods. a) Early dynamic NeRF methods such as DNeRF[37] directly encode the coordinate p of the sample point as input ...
- **p. 2 / 1. Introduction - extractive body cue:** The Gaussian canonical field consists of 3D Gaussian distributions and a geometry-aware feature learning network.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Compared with the results (dubbed as "PointNet feat." and "Plane feat.") in Table 4, it can be observed that our method achieves significant performance gains.
- **p. 7 / 4.3. Quantitative Results - extractive body cue:** On average, our method significantly improves PSNR compared with static Gaussian, 3D-GS.
- **p. 7 / 4.3. Quantitative Results - extractive body cue:** It can be observed that our method achieves good performance compared with other state-of-the-art methods.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.5. Ablation Study), p. 7 (4.3. Quantitative Results) |
| Embodiment/environment | The synthetic dataset D-NeRF [37] contains 8 dynamic scenes, including Hell Warrior, Mutant, Hook, Bouncing Balls, Lego, T-Rex, Stand Up, and Jumping Jacks. | hardware/simulator version and reset protocol | p. 6 (4.1. Dataset), p. 6 (4.1. Dataset) |
| Dataset/benchmark | We further compare our method with some highly related works on the real scene dataset proposed by [34]. | role, split, size and leakage | p. 6 (4.1. Dataset), p. 6 (4.1. Dataset), p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results) |
| Metric | In Table 4, quaternion demonstrates an obvious performance drop, which proves the effectiveness of the 6D representation. | definition, denominator, direction and uncertainty | p. 8 (4.5. Ablation Study), p. 6 (4.2. Implementation Details), p. 7 (4.4. Visualization Results) |
| Baseline/ablation | It can be observed that our method achieves good performance compared with other state-of-the-art methods. | fair input/data/compute/action matching | p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 6 (4.3. Quantitative Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** We addressed the limitations of existing approaches from two perspectives: 1) we introduced 3D sparse convolution to extract local structural information effectively and efficiently for ...
- **p. 7 / 4.4. Visualization Results - extractive body cue:** Since 3D-DS cannot model dynamic scenes, the quality of the point cloud is poor.
- **p. 7 / 4.3. Quantitative Results - extractive body cue:** Since it inherently cannot model the deformation of the dynamic scene, 3D-GS performs poorly in dynamic view synthesis.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** In Table 4, canonical DC shows a performance drop, as the canonical 3D Gaussian alone cannot reflect the over/under reconstruction information at all timestamps for ...
- **p. 6 / 4.2. Implementation Details - extractive body cue:** For the D-NeRF dataset, which does not provide point clouds, we randomly initialize 150000 points.
- **p. 6 / 4.1. Dataset - extractive body cue:** Following previous works [21], we report three evaluation metrics, including Peak Signal-to-Noise Ratio (PSNR), Structural Similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) [66].

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In addressing the above challenges, one common strategy is to represent the dynamic scenes as a combination of a static canonical field and a deformation model [11, 16, 17, 27, 33, 34, ...를 문제로 두고, Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. • We propose to use continuous 6D ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Preliminary), p. 4 (3.2. Gaussian Canonical Field) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
