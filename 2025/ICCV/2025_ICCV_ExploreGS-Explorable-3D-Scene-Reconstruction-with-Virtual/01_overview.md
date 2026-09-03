# ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.를 문제로 두고, In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering of 3DGS, video diffusion priors to complete missing ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in novel view synthesis (NVS) have enabled real-time rendering with 3D Gaussian Splatting (3DGS).
- **p. 1 / Abstract - extractive body cue:** However, existing methods struggle with artifacts and missing regions when rendering from viewpoints that deviate from the training trajectory, limiting seamless scene exploration.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose a 3DGS-based pipeline that generates additional training views to enhance reconstruction.
- **p. 1 / Abstract - extractive body cue:** We introduce an information-gain-driven virtual camera placement strategy to maximize scene coverage, followed by video diffusion priors to refine rendered results.
- **p. 1 / Abstract - extractive body cue:** Fine-tuning 3D Gaussians with these enhanced views significantly improves reconstruction quality.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.
- **p. 2 / 1. Introduction - extractive body cue:** The key challenges of explorable scene reconstruction lie in determining the optimal placement of virtual viewpoints.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering of ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce ExploreGS, a pipeline that enables explorable scene reconstruction using diffusion priors and 3DGS.
- **p. 3 / 3.2. Scene initialization - extractive body cue:** To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.
- **p. 3 / 3.3. Virtual view sampling - extractive body cue:** After initializing the target scene, our method utilizes video diffusion priors to supplement the missing information from 27044
- **p. 1 / 1. Introduction - extractive body cue:** This advancement has been further accelerated by recent 3D Gaussian Splatting (3DGS) [11], which enables highquality rendering in real-time.
- **p. 3 / 3.1. Overview - extractive body cue:** NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: Trn = {V ...
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (b) Based on the optimized 3DGS and training viewpoints, we generate virtual camera trajectories, and enhance the rendered views using our diffusion-based enhancement model.
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (c) Finally, the scene is further optimized using both the original training viewpoints and the newly generated virtual viewpoints.  - 1 1 1 - ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then, we determine the boundary of reconstructable scene based on the input observations and identify occupied regions for virtual viewpoints samplings. | conditioning observation와 noisy/intermediate sample | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization) |
| State/latent | Then, determine, boundary, reconstructable, scene, input, observations, identify, occupied, regions, virtual, viewpoints | latent/noise variable와 conditional distribution | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 2 (1. Introduction) |
| Output/action | As previously discussed, reconstructing content beyond this bounding box is highly challenging, as it lacks grounding in the input observations and increasingly resembles unconstrained content generation, which is beyond the scope of ... | generated sample, action chunk 또는 trajectory | p. 3 (3.2. Scene initialization), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: Trn = {V G l }L l=1. | distribution fit, multimodality, sample quality와 latency | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 4 (3.3. Virtual view sampling) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering of ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce ExploreGS, a pipeline that enables explorable scene reconstruction using diffusion priors and 3DGS.
- **p. 3 / 3.2. Scene initialization - extractive body cue:** To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.
- **p. 3 / 3.3. Virtual view sampling - extractive body cue:** After initializing the target scene, our method utilizes video diffusion priors to supplement the missing information from 27044
- **p. 1 / 1. Introduction - extractive body cue:** This advancement has been further accelerated by recent 3D Gaussian Splatting (3DGS) [11], which enables highquality rendering in real-time.
- **p. 6 / 5.2. Results - extractive body cue:** Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in PSNR ...
- **p. 7 / 5.2. Results - extractive body cue:** See the supplementary materials for additional results.
- **p. 7 / 5.2. Results - extractive body cue:** Although ViewExtrapolator [19] utilizes a video diffusion prior and thereby shows competitive performance compared to 3DGS variants, it underperforms in challenging scenarios.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5.2. Results), p. 7 (5.2. Results) |
| Embodiment/environment | To address the lack of an appropriate benchmark for scene exploration, we introduce WildExplore, a new dataset comprising four indoor and four outdoor scenes. | hardware/simulator version and reset protocol | p. 6 (4.1. WildExplore), p. 6 (4.2. Curated Nerfbusters) |
| Dataset/benchmark | Qualitative comparison on the curated Nerfbusters dataset. | role, split, size and leakage | p. 6 (4.1. WildExplore), p. 6 (4.2. Curated Nerfbusters), p. 7 (5.2. Results), p. 8 (5.3. Ablation study) |
| Metric | TopK vs BottomK Finetuning Curated Nerfbusters Image level Pixel level PSNR↑ SSIM↑ LPIPS↓ Distance [21] - 15.00 0.427 0.443 - Scale [21] 16.18 0.476 0.442 Distance Scale 15.27 0.432 0.440 - - ... | definition, denominator, direction and uncertainty | p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), p. 6 (4.2. Curated Nerfbusters) |
| Baseline/ablation | 6 show qualitative comparisons among our method and baseline methods. | fair input/data/compute/action matching | p. 7 (5.2. Results), p. 6 (5.2. Results), p. 7 (5.2. Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** In addition, extending the scene bounding box to cover a large scale scene would be an interesting avenue for the future work.
- **p. 8 / 5.3. Ablation study - extractive body cue:** Gridbased approach often fails to maximize information gain, as it includes the gain from free space, resulting in redundant viewpoint selections.

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 This limitation stems from missing information, since optimization-based approaches cannot synthesize contents beyond the observed data.를 문제로 두고, In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering of 3DGS, video diffusion priors to complete missing ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Scene initialization), p. 3 (3.1. Overview), p. 4 (3.3. Virtual view sampling), p. 4 (3.3. Virtual view sampling) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
