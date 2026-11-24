# DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Jingyi Pan, Dan Xu, Qiong Luo
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf)

## Why This Paper Is Here

DiGA3D는 여러 시점에서 가려진 영역을 채울 때 확산 모델이 만든 외관과 형상이 하나의 장면에 일치하도록 단계적으로 전파한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Developing a unified pipeline that enables users to remove, re-texture, or replace objects in a versatile manner is crucial for text-guided 3D inpainting.
- **p. 1 / Abstract - extractive body cue:** However, there are still challenges in performing multiple 3D inpainting tasks within a unified framework: 1) Single reference inpainting methods lack robustness when dealing with ...
- **p. 1 / Abstract - extractive body cue:** To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in ...
- **p. 1 / Abstract - extractive body cue:** First, DiGA3D develops a robust strategy for selecting multiple reference views to reduce errors during propagation.
- **p. 1 / Abstract - extractive body cue:** Next, DiGA3D designs an Attention Feature Propagation (AFP) mechanism that propagates attention features from the selected reference views to other views via diffusion models to ...
- **p. 1 / 1. Introduction - extractive body cue:** This limitation becomes particularly evident when inpainting regions require significant geometric changes.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. ter is conducted independently.
- **p. 2 / 1. Introduction - extractive body cue:** Thus, our method offers a coarse-to-fine pipeline that can effectively bridge consistent 2D appearance and 3D geometry, enabling versatile 3D inpainting.
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** Prior to employing AFP, we introduce a robust strategy for selecting the reference views.
- **p. 4 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** Therefore, we propose a texture-geometry guided SDS (TG-SDS) loss within the latent space of ControlNet [42].
- **p. 3 / 3.1. Preliminary - extractive body cue:** In the coarse stage, we employ DDIM Inversion [33] to generate deterministic latents, which are then used to produce coarsely consistent inpainting results with a ...
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** To propagate the inpainted appearance from reference views, we first integrate a self-attention mechanism [40] to extract attention features from each view, as shown in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The outputs of AFP are the inpainted image Ii and the depth map Di estimated by the monocular depth estimator [30] ˜D. | conditioning observation와 noisy/intermediate sample | p. 3 (3.2. Problem formulation and overview), p. 3 (3.2. Problem formulation and overview) |
| State/latent | outputs, AFP, inpainted, image, depth, estimated, monocular, estimator, texture-geometry, warping, texture, jective | latent/noise variable와 conditional distribution | p. 3 (3.2. Problem formulation and overview), p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss) |
| Output/action | The outputs of texture-geometry warping are the texture map C′ i and the depth map D′ i. jective is to inpaint the 3D Gaussians based on these text prompts. | generated sample, action chunk 또는 trajectory | p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (1. Introduction) |
| Objective/outcome | The 3D Gaussians G are optimized with all properties by minimizing the photometric loss and depth loss: \b e gi n {split} \m at h cal {L}_{rgb} & = (1- \lambda )\mathcal ... | distribution fit, multimodality, sample quality와 latency | p. 5 (3.5. Optimization), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview) |

## Main Claims and Actual Contribution

- 복수의 참조 뷰를 선택해 인페인팅 오류 확산을 줄이고, 질감과 기하를 함께 다루는 점수 증류 손실로 장면을 정제한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=5)
- 물체 제거를 포함한 3D 인페인팅 과제에서 결과를 비교하고 참조 뷰 및 손실 설계가 채워진 영역에 미치는 영향을 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study) |
| Embodiment/environment | We evaluate our versatile 3D inpainting methods in three different datasets with multi-view images from feed-forward and 360 degrees: 1) SPIn-NeRF dataset [25] provide 10 scenes that each scene includes 60 images ... | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal) |
| Dataset/benchmark | For the CLIPdir scores, we averaged the scores across six scenes from the SPIn-NeRF [25] and MipNeRF360 [1] datasets. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal), p. 7 (4.3.2. Object Re-Texturing), p. 5 (4.1. Experimental Setup) |
| Metric | We find that our methods achieve relatively high scores compared to other approaches, demonstrating that they can generate more realistic and relevant objects with text prompts. | definition, denominator, direction and uncertainty | p. 7 (4.3.3. Object Replacement), p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Baseline/ablation | We compared our method with four baselines, i.e., SPIn-NeRF [25], NeRFiller [38], MVIP-NeRF [7], and GScream [37]. | fair input/data/compute/action matching | p. 6 (4.1. Experimental Setup), p. 7 (4.3.1. Object Removal), p. 6 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3.1. Object Removal - extractive body cue:** While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary), p. 4 (3.4. Texture-Geometry Guided SDS Loss)이다.
