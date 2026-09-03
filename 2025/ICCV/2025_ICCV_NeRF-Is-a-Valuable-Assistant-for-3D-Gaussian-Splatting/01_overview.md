# NeRF Is a Valuable Assistant for 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, NeRF, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, the weak correlation between discrete Gaussians results in a lack of smooth spatial transitions [7, 8, 40], which negatively affects the visual quality of the rendered outputs.를 문제로 두고, To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties to address 3DGS inherent limitations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce NeRF-GS, a novel framework that jointly optimizes Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS).
- **p. 1 / Abstract - extractive body cue:** This framework leverages the inherent continuous spatial representation of NeRF to mitigate several limitations of 3DGS, including sensitivity to Gaussian initialization, limited spatial awareness, and ...
- **p. 1 / Abstract - extractive body cue:** In NeRF-GS, we revisit the design of 3DGS and progressively align its spatial features with NeRF, enabling both representations to be optimized within the same ...
- **p. 1 / Abstract - extractive body cue:** We further address the formal distinctions between the two approaches by optimizing residual vectors for both implicit features and Gaussian positions to enhance the personalized ...
- **p. 1 / Abstract - extractive body cue:** Experimental results on benchmark datasets show that NeRF-GS surpasses existing methods and achieves state-of-the-art performance.
- **p. 1 / 1. Introduction - extractive body cue:** Moreover, the weak correlation between discrete Gaussians results in a lack of smooth spatial transitions [7, 8, 40], which negatively affects the visual quality of ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose explicitly modeling their discrepancies by optimizing residual vectors for both features and positions to personalize and enhance 3DGS performance.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive body cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive body cue:** (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along with a volume ...
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive body cue:** (11) For dual-branch collaborative loss, we use L1 norm Lrgb joint to constrain the rendered pixel values along GS-Rays in the NeRF branch with corresponding ...
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive body cue:** NeRF requires dense sampling and network queries, which preclude rendering an entire image in a single pass like in 3DGS.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Moreover, the weak correlation between discrete Gaussians results in a lack of smooth spatial transitions [7, 8, 40], which negatively affects the visual quality of the rendered outputs. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | Moreover, weak, correlation, between, discrete, Gaussians, lack, smooth, spatial, transitions, negatively, affects | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | To address this, we propose explicitly modeling their discrepancies by optimizing residual vectors for both features and positions to personalize and enhance 3DGS performance. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.3. Joint Optimization in Dual-branch) |
| Objective/outcome | (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along with a volume regularization Lvol gs [35] to minimize Gaussian ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 4 (4.3. Joint Optimization in Dual-branch) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this, we propose explicitly modeling their discrepancies by optimizing residual vectors for both features and positions to personalize and enhance 3DGS performance.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive body cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.
- **p. 5 / 5.2. Comparison - extractive body cue:** Notably, compared to other methods that incorporate NeRF-like concepts, such as VDGS and Hash-GS, NeRF-GS achieves even more substantial improvements.
- **p. 5 / 5.2. Comparison - extractive body cue:** Comparative results are shown in Table 1, where our approach significantly outperforms the vanilla 3DGS model and other state-of-the-art methods across PSNR, SSIM, and LPIPS ...
- **p. 8 / 5.4. Ablation Studies - extractive body cue:** The ablation results in Table 4 indicate that our proposed initialization significantly outperforms the alternatives.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. NeRF-GS establishes a bridge of communication be- tween NeRF and 3DGS, leveraging information sharing, modeling of distinct characteristics, and joint optimization to enable ...
- **p. 6 / 5.2. Comparison - extractive body cue:** Remarkably, NeRF-GS achieves performance comparable to or even surpassing the SplatField method, which is specifically designed for sparse-view set26235

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (5.2. Comparison), p. 5 (5.2. Comparison) |
| Embodiment/environment | We report experimental results on real-world datasets, including Mip-NeRF360 (all 9 scenes) [5], Tanks&Temples [29] DeepBlending [23], and the Blender dataset [41]. | hardware/simulator version and reset protocol | p. 5 (5.1. Implementation Details), p. 5 (5.1. Implementation Details) |
| Dataset/benchmark | Qualitative comparison on real-world datasets. | role, split, size and leakage | p. 5 (5.1. Implementation Details), p. 5 (5.1. Implementation Details), p. 6 (5.2. Comparison), p. 6 (5.2. Comparison) |
| Metric | Errors introduced during NeRF pre-training and inherent disparities between NeRF and 3DGS can impede the GS branch's ability to effectively model a 3D scene from NeRF-shared information. | definition, denominator, direction and uncertainty | p. 7 (5.3. Qualitative Analysis of NeRF-GS), p. 8 (5.4. Ablation Studies), p. 5 (5.1. Implementation Details) |
| Baseline/ablation | Comparative results are shown in Table 1, where our approach significantly outperforms the vanilla 3DGS model and other state-of-the-art methods across PSNR, SSIM, and LPIPS metrics. | fair input/data/compute/action matching | p. 5 (5.2. Comparison), p. 5 (5.2. Comparison), p. 6 (5.2. Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Conclusion - extractive body cue:** These strategies effectively address several limitations of 3DGS, including initialization dependency, limited spatial awareness, insufficient Gaussian sphere correlation, and overfitting in sparse-view scenes.
- **p. 6 / 5.2. Comparison - extractive body cue:** Our method demonstrates a significant advantage over 3DGS and its variants, achieving a more faithful representation of scene details. validating NeRF-GS as a robust framework ...
- **p. 7 / 5.3. Qualitative Analysis of NeRF-GS - extractive body cue:** When associations between two branches are directly removed, such as feature sharing, loss constraints during joint training, etc., the NeRF-GS shows large visual quality degradation.
- **p. 8 / 5.4. Ablation Studies - extractive body cue:** Removing mutual constraints between branch outputs leads to performance degradation.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Moreover, the weak correlation between discrete Gaussians results in a lack of smooth spatial transitions [7, 8, 40], which negatively affects the visual quality of the rendered outputs.를 문제로 두고, To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties to address 3DGS inherent limitations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
