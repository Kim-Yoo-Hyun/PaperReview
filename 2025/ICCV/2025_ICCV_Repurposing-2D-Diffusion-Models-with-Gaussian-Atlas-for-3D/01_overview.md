# Repurposing 2D Diffusion Models with Gaussian Atlas for 3D Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, such models have significant limitations especially when trained solely on 3D data, as high-quality 3D data is relatively scarce compared to 2D images.를 문제로 두고, To summarize, our major contributions are three-fold: (i) We present a large-scale dataset, GaussianVerse, consisting of 205,737 high-quality 3D Gaussian fittings for diverse objects sampled from Sketchfab [43]; (ii) We propose a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in text-to-image diffusion models have been driven by the increasing availability of paired 2D data.
- **p. 1 / Abstract - extractive body cue:** However, the development of 3D diffusion models has been hindered by the scarcity of high-quality 3D data, resulting in less competitive performance compared to their ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose repurposing pre-trained 2D diffusion models for 3D object generation.
- **p. 1 / Abstract - extractive body cue:** We introduce Gaussian Atlas, a novel representation that utilizes dense 2D grids, enabling the fine-tuning of 2D diffusion models to generate 3D Gaussians.
- **p. 1 / Abstract - extractive body cue:** Our approach demonstrates successful transfer learning from a pre-trained 2D diffusion model to a 2D manifold flattened from 3D structures.
- **p. 1 / 1. Introduction - extractive body cue:** However, such models have significant limitations especially when trained solely on 3D data, as high-quality 3D data is relatively scarce compared to 2D images.
- **p. 1 / 1. Introduction - extractive body cue:** We show that these Gaussian atlases facilitate transfer of the prior knowledge This ICCV paper is the Open Access version, provided by the Computer Vision ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our major contributions are three-fold: (i) We present a large-scale dataset, GaussianVerse, consisting of 205,737 high-quality 3D Gaussian fittings for diverse objects sampled ...
- **p. 1 / 1. Introduction - extractive body cue:** To fully harness the capabilities of these 2D diffusion models, we introduce Gaussian Atlas, a novel 2D representation of 3D Gaussians.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a fresh perspective that repurposes 2D diffusion models for 3D generation through direct fine-tuning.
- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive body cue:** In this section, we introduce a novel approach that transforms unorganized Gaussians in the 3D space to a dense 2D representation, namely Gaussian Atlas, making ...
- **p. 2 / 3. GaussianVerse - extractive body cue:** In this section, we present GaussianVerse, a large-scale dataset containing high-quality 3D Gaussian fittings for a wide range of 3D objects.
- **p. 1 / Abstract - extractive body cue:** We introduce Gaussian Atlas, a novel representation that utilizes dense 2D grids, enabling the fine-tuning of 2D diffusion models to generate 3D Gaussians.
- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive body cue:** To make 3D Gaussians compatible with 2D diffusion models, we propose Gaussian Atlas, a 2D representation of 3D Gaussians.
- **p. 5 / 5. 2D Diffusion for 3D Gaussian Generation - extractive body cue:** The VAE decoder then upsamples the generated latent back to the original RGB space.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To summarize, our major contributions are three-fold: (i) We present a large-scale dataset, GaussianVerse, consisting of 205,737 high-quality 3D Gaussian fittings for diverse objects sampled from Sketchfab [43]; (ii) We propose a ... | conditioning observation와 noisy/intermediate sample | p. 2 (1. Introduction), p. 3 (3. GaussianVerse) |
| State/latent | summarize, major, contributions, three-fold, present, large-scale, dataset, GaussianVerse, consisting, high-quality, Gaussian, fittings | latent/noise variable와 conditional distribution | p. 2 (1. Introduction), p. 3 (3. GaussianVerse), p. 3 (3. GaussianVerse) |
| Output/action | A 2D image C can be rendered from properly structured 3D Gaussians through ω-blending: Cω = ! j=1 cjεω j j→1 " k=1 (1 ↑εω k ), (1) where ϑ is the ... | generated sample, action chunk 또는 trajectory | p. 3 (3. GaussianVerse), p. 3 (3. GaussianVerse), p. 4 (4. Formulating 3D Gaussians as 2D Atlas) |
| Objective/outcome | We optimize per-object 3D Gaussians by minimizing photometric losses against multi-view RGB renderings: ϱ↑ rgbLrgb + ϱ↑ ssimLssim + ϱ↑ lpipsLlpips + ϱ↑ regR, (2) where Lrgb represents the color space L1 ... | distribution fit, multimodality, sample quality와 latency | p. 3 (3. GaussianVerse), p. 1 (1. Introduction), p. 4 (3. GaussianVerse) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our major contributions are three-fold: (i) We present a large-scale dataset, GaussianVerse, consisting of 205,737 high-quality 3D Gaussian fittings for diverse objects sampled ...
- **p. 1 / 1. Introduction - extractive body cue:** To fully harness the capabilities of these 2D diffusion models, we introduce Gaussian Atlas, a novel 2D representation of 3D Gaussians.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a fresh perspective that repurposes 2D diffusion models for 3D generation through direct fine-tuning.
- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive body cue:** In this section, we introduce a novel approach that transforms unorganized Gaussians in the 3D space to a dense 2D representation, namely Gaussian Atlas, making ...
- **p. 2 / 3. GaussianVerse - extractive body cue:** In this section, we present GaussianVerse, a large-scale dataset containing high-quality 3D Gaussian fittings for a wide range of 3D objects.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. User study results. Our method outperforms state-of- the-art methods [57, 60] in user preferences regarding generation quality and alignment with text prompts. > ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Finetuning from a pretrained 2D diffusion model leads to faster generalization. Top: 3D generations at different training checkpoints from finetuning (top row) and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | However, text-to-3D generation presents greater challenges due to two key reasons: (i) the scarcity of large-scale datasets with 3D models comparable to those in 2D, as creating and annotating high-quality, textured 3D ... | hardware/simulator version and reset protocol | p. 4 (4. Formulating 3D Gaussians as 2D Atlas), p. 3 (3. GaussianVerse) |
| Dataset/benchmark | metal handle house model light box roof table stone character toy sword cube robot rock cartoon hat gun sphere hole Total number of 3DGS fittings = 205,737 d b c Occurrences Number ... | role, split, size and leakage | p. 4 (4. Formulating 3D Gaussians as 2D Atlas), p. 3 (3. GaussianVerse), p. 3 (3. GaussianVerse), p. 4 (3. GaussianVerse) |
| Metric | Figure 6. Additional qualitative results. Our method effectively repurposes 2D diffusion models for high-quality 3D contents. The generated Gaussian atlases are presented in the order from top left to bottom right: 3D ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Baseline/ablation | Figure 7. User study results. Our method outperforms state-of- the-art methods [57, 60] in user preferences regarding generation quality and alignment with text prompts. > 2, 500 valid responses. As shown in ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 3 (3. GaussianVerse) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive body cue:** However, unstructured Gaussians in 3D space cannot be directly passed to 2D models, which require inputs X to have: (i) only 2 spatial dimensions; (ii) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative Comparisons. Our 3D generations exhibit the highest quality, minimal artifacts, and the best alignment with text prompts. In contrast, DreamGaussian [46], LGM ...
- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive body cue:** As a result, diffusion models are not able to capture the irregular patterns and fail to generate meaningful contents.
- **p. 5 / 5. 2D Diffusion for 3D Gaussian Generation - extractive body cue:** By injecting Gaussian noise to the latents, F can be trained through self-supervised denoising via v-parameterization [39]: Ldiff = El0,z,t # ≃⇐ltz ↑⇐ltF(lt, t)≃2$ , ...
- **p. 5 / 4. Formulating 3D Gaussians as 2D Atlas - extractive body cue:** In the diffusion model training stage (section 5), we leverage the transformed 2D Gaussian atlases to repurpose a pretrained latent diffusion model (the 2D UNet ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, such models have significant limitations especially when trained solely on 3D data, as high-quality 3D data is relatively scarce compared to 2D images.를 문제로 두고, To summarize, our major contributions are three-fold: (i) We present a large-scale dataset, GaussianVerse, consisting of 205,737 high-quality 3D Gaussian fittings for diverse objects sampled from Sketchfab [43]; (ii) We propose a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Formulating 3D Gaussians as 2D Atlas), p. 1 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
