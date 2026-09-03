# Problem - DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary)): This limitation becomes particularly evident when inpainting regions require significant geometric changes.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Developing a unified pipeline that enables users to remove, re-texture, or replace objects in a versatile manner is crucial for text-guided 3D inpainting.
- **p. 1 / Abstract - extractive body cue:** However, there are still challenges in performing multiple 3D inpainting tasks within a unified framework: 1) Single reference inpainting methods lack robustness when dealing with ...
- **p. 1 / Abstract - extractive body cue:** To tackle these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline that leverages diffusion models to propagate consistent appearance and geometry in ...
- **p. 1 / Abstract - extractive body cue:** First, DiGA3D develops a robust strategy for selecting multiple reference views to reduce errors during propagation.
- **p. 1 / Abstract - extractive body cue:** Next, DiGA3D designs an Attention Feature Propagation (AFP) mechanism that propagates attention features from the selected reference views to other views via diffusion models to ...
- **p. 1 / 1. Introduction - extractive body cue:** This limitation becomes particularly evident when inpainting regions require significant geometric changes.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation becomes particularly evident when inpainting regions require significant geometric changes. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | The outputs of AFP are the inpainted image Ii and the depth map Di estimated by the monocular depth estimator [30] ˜D. | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | outputs, AFP, inpainted, image, depth, estimated, monocular, estimator, texture-geometry, warping | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | process, rendered, images, along, projected, warped, texture, maps | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: outputs, AFP, inpainted, image, depth, estimated, monocular, estimator, texture-geometry, warping | p. 3 (3.2. Problem formulation and overview), p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: summary, contributions, outlined, follows, introduce, DiGA3D, versatile, inpainting | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Texture-Geometry Guided SDS Loss) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Gaussians, optimized, properties, minimizing, photometric, loss, depth, split | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 5 (3.4. Texture-Geometry Guided SDS Loss) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss) |
| Success / guarantee | sample quality, diversity and latency | p. 7 (4.3.3. Object Replacement), p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 2 / 1. Introduction - extractive body cue:** to-fine manner that utilizes 3D Gaussian Splatting (3DGS) to leverage diffusion priors for propagating appearance and geometry across multiple views.
- **p. 3 / 3.2. Problem formulation and overview - extractive body cue:** We define the problem of versatile 3D inpainting using 3DGS as follows: Given a pretrained 3D Gaussians G, a positive prompt Tp, a negative prompt ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Text-to-3D has seen significant advancements by optimizing a 3D representation using a 2D pre-trained image diffusion prior ϵϕ, based on Score Distillation Sampling (SDS) [27].

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (1. Introduction), p. 4 (3.3. Multi-view Consistent Image Inpainting)): In summary, our key contributions can be outlined as follows: • We introduce DiGA3D, a versatile 3D inpainting pipeline that leverages diffusion models to consistently propagate appearance and geometry in ...

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DiGA3D, a novel and versatile 3D inpainting pipeline with a coarseThis ICCV paper is the Open Access version, provided ...
- **p. 5 / 3.4. Texture-Geometry Guided SDS Loss - extractive body cue:** For each scene, we present two novel views to compare the rendering quality and multi-view consistency with the existing state-of-the-art methods. ter is conducted independently.
- **p. 2 / 1. Introduction - extractive body cue:** Thus, our method offers a coarse-to-fine pipeline that can effectively bridge consistent 2D appearance and 3D geometry, enabling versatile 3D inpainting.
- **p. 4 / 3.3. Multi-view Consistent Image Inpainting - extractive body cue:** Prior to employing AFP, we introduce a robust strategy for selecting the reference views.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | While our rendering results exhibit some limitations in the masked LPIPS compared to GScream, we achieve a comparable ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.2. Problem formulation and overview), p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Problem formulation and overview), p. 3 (3.1. Preliminary), interface p. 3 (3.2. Problem formulation and overview), p. 3 (3.2. Problem formulation and overview), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 2 (1. Introduction), objective p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 4 (3.2. Problem formulation and overview), p. 4 (3.4. Texture-Geometry Guided SDS Loss), p. 5 (3.4. Texture-Geometry Guided SDS Loss), p. 5 (3.4. Texture-Geometry Guided SDS Loss).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
