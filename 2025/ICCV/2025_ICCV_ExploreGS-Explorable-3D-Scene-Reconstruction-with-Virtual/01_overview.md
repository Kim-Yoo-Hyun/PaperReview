# ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Minsu Kim, Subin Jeon, In Cho, Mijin Yoo, Seon Joo Kim
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

ExploreGS는 입력 시점 밖에서도 탐색할 수 있는 장면을 가상 카메라와 확산 사전분포로 복원한다.

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
- **PDF p. 4, Fig. 2(c) (DOC-QA2 원문 대조):** 원래 training viewpoints와 diffusion으로 보강한 virtual viewpoints를 함께 사용해 scene을 추가 최적화한다. 뒤에 붙었던 숫자·기호는 인접 Fig. 3의 정보량 도식에서 섞인 것으로 이 문장에서 제거했다.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then, we determine the boundary of reconstructable scene based on the input observations and identify occupied regions for virtual viewpoints samplings. | conditioning observation와 noisy/intermediate sample | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization) |
| State/latent | Then, determine, boundary, reconstructable, scene, input, observations, identify, occupied, regions, virtual, viewpoints | latent/noise variable와 conditional distribution | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 2 (1. Introduction) |
| Output/action | As previously discussed, reconstructing content beyond this bounding box is highly challenging, as it lacks grounding in the input observations and increasingly resembles unconstrained content generation, which is beyond the scope of ... | generated sample, action chunk 또는 trajectory | p. 3 (3.2. Scene initialization), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: Trn = {V G l }L l=1. | distribution fit, multimodality, sample quality와 latency | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 4 (3.3. Virtual view sampling) |

## Main Claims and Actual Contribution

- 점유 지도를 이용해 새로운 카메라 시점을 샘플링한다.
- 가상 관측을 3D 가우시안 장면 복원에 사용한다.

[저자 원문](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.2. Scene initialization), p. 3 (3.1. Overview), p. 4 (3.3. Virtual view sampling)이다.
