# DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This limitation becomes particularly evident when inpainting regions require significant geometric changes.를 문제로 두고, In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently propagate appearance and geometry in a coarse-to-fine ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. ter is conducted independently.
- **p. 2 / 1. Introduction - extractive body cue:** Thus, our method offers a coarse-to-fine pipeline that can effectively bridge consistent 2D appearance and 3D geometry, enabling versatile 3D inpainting.
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** Prior to employing AFP, we introduce a robust strategy for selecting the reference views.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Our method achieves clear improvements in PSNR and obtains better scores in most metrics.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** By integrating DDIM inversion and AFP within the 2D inpainter, we achieve a notable 0.21 improvement in PSNR, indicating significant enhancements.
- **p. 7 / 4.3.1. Object Removal - extractive body cue:** While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable score in this metric and show significant ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This limitation becomes particularly evident when inpainting regions require significant geometric changes.를 문제로 두고, In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently propagate appearance and geometry in a coarse-to-fine ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary), p. 4 (3.4. Texture-Geometry Guided SDS Loss) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
