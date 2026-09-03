# NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, NeRF, semantic, alignment, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To overcome these challenges, we propose a novel NeRF-Guided 3DGS (NG-GS) segmentation framework, aiming to achieve model continuity at object boundaries.를 문제로 두고, With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with MRHE to generate spatially smooth and multi-scale ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in 3D Gaussian Splatting (3DGS) have enabled highly efficient and photorealistic novel view synthesis.
- **p. 1 / Abstract - extractive body cue:** However, segmenting objects accurately in 3DGS remains challenging due to the discrete nature of Gaussian representations, which often leads to aliasing and artifacts at object ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce NG-GS, a novel framework for high-quality object segmentation in 3DGS that explicitly addresses boundary discretization.
- **p. 1 / Abstract - extractive body cue:** Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis.
- **p. 1 / Abstract - extractive body cue:** We then apply radial basis function (RBF) interpolation to construct a spatially continuous feature field, enhanced by multi-resolution hash encoding for efficient multi-scale representation.
- **p. 1 / 1. Introduction - extractive body cue:** To overcome these challenges, we propose a novel NeRF-Guided 3DGS (NG-GS) segmentation framework, aiming to achieve model continuity at object boundaries.
- **p. 1 / 1. Introduction - extractive body cue:** Some existing methods [11, 37] directly remove the mutated boundary Gaussian distribution.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with ...
- **p. 1 / 1. Introduction - extractive body cue:** To overcome these challenges, we propose a novel NeRF-Guided 3DGS (NG-GS) segmentation framework, aiming to achieve model continuity at object boundaries.
- **p. 1 / 1. Introduction - extractive body cue:** (a) Mask (b) Mutated (c) Continuation (d) Our method Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** Experimental results reveal that our method consistently outperforms all compared baselines across all metrics on three benchmarks.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive body cue:** By this way, we construct a query set Pquery = {qi,k}, which consists of Nrow·Ncol·K query points.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive body cue:** Through RBF interpolation, the discrete Gaussian features are fused into continuous features f inter, which are then fed into the NeRF module to reinforce spatial ...
- **p. 3 / 4. Method - extractive body cue:** To efficiently encode multi-scale spatial information, we incorporate multi-resolution hash encoding (MRHE), which enhances the representation capacity while maintaining computational efficiency. • NeRF-GS Joint Optimization: ...
- **p. 3 / 4. Method - extractive body cue:** A joint optimization strategy is employed, where alignment loss and spatial continuity loss are used to harmonize the outputs of 3DGS and NeRF.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with MRHE to generate spatially smooth and multi-scale ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 5 (4.2. NeRF-GS Joint Optimization) |
| State/latent | NG-GS, framework, make, following, main, contributions, develop, continuous, feature, field, construction, module | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 5 (4.2. NeRF-GS Joint Optimization), p. 3 (3.1. NeRF) |
| Output/action | These parameters dynamically adjust the hidden layers based on external conditions. ˆh(l) = ReLU  γ(l) ⊙h(l) + β(l) , (14) where ⊙is the element-wise product, h(l) is the original activation vector ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (4.2. NeRF-GS Joint Optimization), p. 3 (3.1. NeRF), p. 3 (4. Method) |
| Objective/outcome | The gradient smoothness loss function achieves visual smoothness by minimizing the magnitude of color gradients, thereby penalizing abrupt color variations. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4.2. NeRF-GS Joint Optimization), p. 5 (4.2. NeRF-GS Joint Optimization), p. 3 (4. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with ...
- **p. 1 / 1. Introduction - extractive body cue:** To overcome these challenges, we propose a novel NeRF-Guided 3DGS (NG-GS) segmentation framework, aiming to achieve model continuity at object boundaries.
- **p. 1 / 1. Introduction - extractive body cue:** (a) Mask (b) Mutated (c) Continuation (d) Our method Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** Experimental results reveal that our method consistently outperforms all compared baselines across all metrics on three benchmarks.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive body cue:** By this way, we construct a query set Pquery = {qi,k}, which consists of Nrow·Ncol·K query points.
- **p. 7 / 5.3. Qualitative Results - extractive body cue:** Red bounding boxes highlight key areas where our method has achieved significant improvements in boundary segmentation and spatial continuity.
- **p. 7 / 5.4. Computational Efficiency Analysis - extractive body cue:** Our method achieves similar computational efficiency to COB-GS and outperforms other maskbased methods in both training and inference efficiency.
- **p. 6 / 5.2. Quantitative Results - extractive body cue:** The quantitative results (Table 1-Table 3) show that our method outperforms all baselines across all metrics on the NVOS, LERF-OVS, and ScanNet datasets.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.3. Qualitative Results), p. 7 (5.4. Computational Efficiency Analysis) |
| Embodiment/environment | NVOS consists of eight scenes picked from the LLFF [21] dataset. | hardware/simulator version and reset protocol | p. 6 (5.1. Implementation Details), p. 6 (5.1. Implementation Details) |
| Dataset/benchmark | Qualitative result on NVOS and LERF-OVS datasets. | role, split, size and leakage | p. 6 (5.1. Implementation Details), p. 6 (5.1. Implementation Details), p. 7 (5.2. Quantitative Results), p. 7 (5.4. Computational Efficiency Analysis) |
| Metric | However, their segmentation accuracy is limited for complex scenes. | definition, denominator, direction and uncertainty | p. 7 (5.4. Computational Efficiency Analysis), p. 8 (5.5. Ablation Studies), p. 1 (Figure/Table caption) |
| Baseline/ablation | The proposed method is compared against a range of state-of-the-art baselines, which are categorized into mask-based and feedforward-based approaches. | fair input/data/compute/action matching | p. 6 (5.1. Implementation Details), p. 6 (5.2. Quantitative Results), p. 7 (5.4. Computational Efficiency Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Addressing current limitations, our future directions include extending the framework to dynamic scenes and real-time interactive applications, further bridging the gap between representation learning and ...
- **p. 8 / 5.6. Hyper-parameter Analysis - extractive body cue:** It is shown that τ=0.6 achieves the best balance between maintaining structural integrity and controlling background noise, resulting in excellent visual coherence and detail preservation.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To overcome these challenges, we propose a novel NeRF-Guided 3DGS (NG-GS) segmentation framework, aiming to achieve model continuity at object boundaries.를 문제로 두고, With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with MRHE to generate spatially smooth and multi-scale ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.1. Edge Gaussian Continuity), p. 3 (4. Method), p. 3 (4. Method), p. 4 (4.1. Edge Gaussian Continuity) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
