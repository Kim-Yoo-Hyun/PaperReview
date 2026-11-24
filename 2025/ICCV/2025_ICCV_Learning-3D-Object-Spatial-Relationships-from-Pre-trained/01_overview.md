# Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Sangwon Baik, Hyeonwoo Kim, Hanbyul Joo
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf)

## Why This Paper Is Here

이 연구는 2D 확산 모델의 합성 영상에서 물체 쌍의 3D 상대 배치를 얻어 물체 사이에 가능한 공간 관계의 분포를 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a method for learning 3D spatial relationships between object pairs, referred to as object-object spatial relationships (OOR), by leveraging synthetically generated 3D samples ...
- **p. 1 / Abstract - extractive body cue:** We hypothesize that images synthesized by 2D diffusion models inherently capture realistic OOR cues, enabling efficient collection of a 3D dataset to learn OOR for ...
- **p. 1 / Abstract - extractive body cue:** Our approach synthesizes diverse images that capture plausible OOR cues, which we then uplift into 3D samples.
- **p. 1 / Abstract - extractive body cue:** Leveraging our diverse collection of 3D samples for the object pairs, we train a score-based OOR diffusion model to learn the distribution of their relative ...
- **p. 1 / Abstract - extractive body cue:** Additionally, we extend our pairwise OOR to multi-object OOR by enforcing consistency across pairwise relations and preventing object collisions.
- **p. 1 / 1. Introduction - extractive body cue:** While some are constrained by physical laws (e.g., objects can rest on others but cannot float in mid-air), many arise from functional usage, reflecting how ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we present an approach to learn 3D object spatial relationships from synthetically generated 3D samples capturing plausible OORs.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: (1) We formulate a novel representation for object-object spatial relationships (OOR); (2) We introduce an effective pipeline ...
- **p. 3 / 3.2. 3D OOR Samples Generation - extractive body cue:** We present a novel pipeline that synthesizes diverse 3D samples by leveraging pre-trained 2D diffusion models and an advanced 3D uplifting process.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive experiments, we demonstrate the robustness of our method across various object-object spatial relationships.
- **p. 3 / 3.1. Formulating Object-Object Relationship - extractive body cue:** The frontal side, typically the most observable view, faces the z-axis, although our method accommodates any canonical orientation.
- **p. 3 / 3.2. 3D OOR Samples Generation - extractive body cue:** We use an offthe-shelf text-to-image model [2] to generate images that are aligned to the OOR context in text prompt c.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive body cue:** To account for the shape deviations, we use several template meshes as candidates and select the best via DINO features [7, 41].
- **p. 5 / 3.3. OOR Diffusion - extractive body cue:** The model architecture and training process of our OOR diffusion are shown in Fig.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive body cue:** Then, we lift pixel features to obtain 3D point features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As the output of SfM, we obtain the 3D point cloud P = {Pj}N j=1, Pj ∈R3, and their corresponding 2D keypoints, {pk j }mj k=1, pk j ∈R2, where N denotes ... | conditioning observation와 noisy/intermediate sample | p. 3 (3.2. 3D OOR Samples Generation), p. 3 (3.2. 3D OOR Samples Generation) |
| State/latent | output, SfM, obtain, point, cloud, corresponding, keypoints, where, denotes, number, points, j-th | latent/noise variable와 conditional distribution | p. 3 (3.2. 3D OOR Samples Generation), p. 3 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation) |
| Output/action | Given an image containing the OOR cues for the object pair, we produce pseudo-multi-view images using an off-the-shelf novel view synthesis method, SV3D [61], which synthesizes circular multi-views from a single image ... | generated sample, action chunk 또는 trajectory | p. 3 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation) |
| Objective/outcome | The inconsistency loss minimizes the variance among OOR cues for the same object from different base object paths. | distribution fit, multimodality, sample quality와 latency | p. 5 (3.3. OOR Diffusion), p. 3 (3.1. Formulating Object-Object Relationship), p. 3 (3.2. 3D OOR Samples Generation) |

## Main Claims and Actual Contribution

- 두 물체가 함께 등장하는 영상을 생성해 3D 배치 표본으로 변환하고 상대 변환 분포를 점수 기반 확산 모델로 학습한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=4)
- 쌍별 관계의 일관성과 충돌 제약을 이용해 여러 물체를 배치하고, 공간 관계 생성과 장면 배치 예에서 결과를 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4. Experiments), p. 7 (4.1. Pairwise OOR Generation) |
| Embodiment/environment | We evaluate 20 scenes where 3 to 5 objects have spatial relations with each other. | hardware/simulator version and reset protocol | p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.3. Applications of OOR) |
| Dataset/benchmark | We evaluate our method and the baselines on a total of 150 scenes derived from 30 category pairs with 5 scenes generated per prompt. | role, split, size and leakage | p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.3. Applications of OOR), p. 6 (4.1. Pairwise OOR Generation), p. 6 (4.1. Pairwise OOR Generation) |
| Metric | 2 further demonstrates the superiority of our method, especially in the case of VLM score and user study. | definition, denominator, direction and uncertainty | p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.2. Multi-object OOR Generation), p. 6 (4.1. Pairwise OOR Generation) |
| Baseline/ablation | In contrast, our OOR diffusion demonstrates superior sampling capabilities compared to the baselines, leveraging its effective learning of 8423 | fair input/data/compute/action matching | p. 6 (4.1. Pairwise OOR Generation), p. 7 (4.1. Pairwise OOR Generation), p. 6 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Pairwise OOR Generation - extractive body cue:** However, due to the inherent limitation of estimating 3D information without direct 3D data, it lacks fine-grained control.
- **p. 7 / 4.2. Multi-object OOR Generation - extractive body cue:** 7, GraphDreamer often fails to capture OOR (e.g., "A knife cuts an apple.").
- **p. 7 / 4.2. Multi-object OOR Generation - extractive body cue:** Since SMC and SceneTeller cannot be directly extended to multi-object OOR using only pairwise OOR data, we compare our model to another baseline GraphDreamer [13], ...
- **p. 8 / 4.3. Applications of OOR - extractive body cue:** (a) adding random noise to the original scene and then rearranging it.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion)이다.
