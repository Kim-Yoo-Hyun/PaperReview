# MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, 2DGS still cannot effectively model surfaces when ambient lighting changes.를 문제로 두고, To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure 1c).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Novel view synthesis (NVS) and surface reconstruction (SR) are essential tasks in 3D Gaussian Splatting (3DGS).
- **p. 1 / Abstract - extractive body cue:** Despite recent progress, these tasks are often addressed independently, with GS-based rendering methods struggling under diverse light conditions and failing to produce accurate surfaces, while ...
- **p. 1 / Abstract - extractive body cue:** This raises a central question: must rendering and reconstruction always involve a trade-off?
- **p. 1 / Abstract - extractive body cue:** To address this, we propose MGSR, a 2D/3D Mutual-boosted Gaussian Splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy.
- **p. 1 / Abstract - extractive body cue:** MGSR introduces two branches-one based on 2DGS and the other on 3DGS.
- **p. 1 / 1. Introduction - extractive body cue:** However, 2DGS still cannot effectively model surfaces when ambient lighting changes.
- **p. 1 / 1. Introduction - extractive body cue:** However, despite the effectiveness of illumination decomposition in rendering, these methods are time-consuming and still struggle to achieve meaningful mesh extraction due to inherent limitations ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure ...
- **p. 2 / 1. Introduction - extractive body cue:** The input consists of multi-view images captured from various camera positions and angles, under significantly varying light conditions.
- **p. 3 / 3.1. Overview - extractive body cue:** MGSR is a 2D/3D mutual-boosted framework that consists of two branches: improved 3DGS branch (Section 3.2) and 2DGS branch (Section 3.3).
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the 3D module L3D ...
- **p. 6 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** Specifically, as one branch reaches convergence, it will initiate our alternating optimization process first.
- **p. 5 / 3.4. Alternating optimization of 2D & 3D Gaussians - extractive body cue:** In the alternating optimization stage, the loss function of 2DGS branch will be promoted to: L2D = Lrender-m +λ3(γLn +λ4Ln-TV-m)+λ5Ld-TV-m, (13) where γ is the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2D Gaussians Normals Images Depths 2D-GS Branch Ref-images Ref-map × + Trans-images 3D Gaussians 3D-GS Branch Depths Mutual-boosted Supervision NVS SR Inputs under Various Light Conditions MGSR Pipeline Output Warm-up Warm-up Figure ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Illumination decomposition with 3DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |
| State/latent | Gaussians, Normals, Images, Depths, D-GS, Branch, Ref-images, Ref-map, Trans-images, Mutual-boosted, Supervision, NVS | geometry, map, object/relationship state | p. 4 (3.2. Illumination decomposition with 3DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |
| Output/action | Input images NeuS2 2D-GS GOF MGSR (Ours) Coffee MuscleCar Figure 5. | point map, pose, scene graph, affordance 또는 query result | p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 2 (1. Introduction) |
| Objective/outcome | The total loss Ltotal of the alternating optimization is: Ltotal = w2DL2D + w3DL3D + wdepth-mutualLZ, (15) where the losses of the 3D module L3D and the 2D module L2D are calculated ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 5 (3.3. Surface reconstruction with 2DGS), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure ...
- **p. 2 / 1. Introduction - extractive body cue:** The input consists of multi-view images captured from various camera positions and angles, under significantly varying light conditions.
- **p. 3 / 3.1. Overview - extractive body cue:** MGSR is a 2D/3D mutual-boosted framework that consists of two branches: improved 3DGS branch (Section 3.2) and 2DGS branch (Section 3.3).
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...
- **p. 8 / 4.2. Results - extractive body cue:** MGSR, supported by an auto-stop warm-up strategy, outperforms GOF and achieves a comparable speed with 2DGS.
- **p. 7 / 4.2. Results - extractive body cue:** MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Visual comparisons on the Shiny Blender dataset [21]. other hand, a depth loss between 2DGS and 3DGS branches is introduced to improve the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 2 (Figure/Table caption), p. 8 (4.2. Results) |
| Embodiment/environment | DTU [7] is a large MVS dataset, where some scenes feature unfavorable light conditions for surface reconstruction, such as overexposure, underexposure, and metallic reflections. | hardware/simulator version and reset protocol | p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics) |
| Dataset/benchmark | Ablations of loss weights (Models A-F), iterations of mutual-boosted optimization (Models G-J), bidrectional BP and auto-stop warm-up strategy (Models K-L) on OmniObject3D dataset. | role, split, size and leakage | p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results), p. 6 (4.1. Datasets and evaluation metrics) |
| Metric | We utilize SSIM and PSNR to evaluate the rendering quality, while reconstruction accuracy is validated by 10K sampled points with Normal Consistency (NC) and Chamfer Distance (CD) measurements. | definition, denominator, direction and uncertainty | p. 6 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results), p. 7 (4.2. Results) |
| Baseline/ablation | MGSR visually outperforms all baselines, resulting in the best NC, with smooth surfaces and accurate color modeling. | fair input/data/compute/action matching | p. 7 (4.2. Results), p. 6 (4.1. Datasets and evaluation metrics), p. 7 (4.2. Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Results - extractive body cue:** To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, which fail to capture surface holes or ...
- **p. 8 / 6. Conclusion - extractive body cue:** A possible way for addressing this issue is to incorporate exposure compensation for input images, which we will investigate as a future work.
- **p. 6 / 4.1. Datasets and evaluation metrics - extractive body cue:** Due to the limitation of CD, we mainly focus on NC metric, which aligns better 27300
- **p. 7 / 4.2. Results - extractive body cue:** Previous GS-based methods fail to effectively reconstruct glass or mirror surfaces, resulting in damaged and inaccurate surfaces.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, 2DGS still cannot effectively model surfaces when ambient lighting changes.를 문제로 두고, To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure 1c).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
