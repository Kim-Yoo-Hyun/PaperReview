# LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00024.
> PDF retrieval source: https://openreview.net/attachment?id=KhjlXNbYea&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00024
- PDF title variant: LangOcc: Self-Supervised Open Vocabulary Occupancy Estimation via Volume Rendering [원문 표제면](https://arxiv.org/pdf/2407.17310v2#page=1) · [공식 서지](https://api.crossref.org/works/10.1109/3dv66043.2025.00024)
- Preprint PDF: https://arxiv.org/pdf/2407.17310
- Full-text retrieval at original review: https://openreview.net/attachment?id=KhjlXNbYea&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

LangOcc는 카메라 영상만으로 3차원 점유와 언어에 정렬된 특징을 학습해 사전 정의한 클래스 밖의 물체도 질의할 수 있게 한다. [PDF 1쪽](https://arxiv.org/pdf/2407.17310v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The 3D occupancy estimation task has become an important challenge in the area of vision-based autonomous driving recently.
- **p. 1 / Abstract - extractive body cue:** However, most existing camera-based methods rely on costly 3D voxel labels or LiDAR scans for training, limiting their practicality and scalability.
- **p. 1 / Abstract - extractive body cue:** Moreover, most methods are tied to a predefined set of classes which they can detect.
- **p. 1 / Abstract - extractive body cue:** In this work we present a novel approach for open vocabulary occupancy estimation called LangOcc, that is trained only via camera images, and can detect ...
- **p. 1 / Abstract - extractive body cue:** In particular, we distill the knowledge of the strong vision-language aligned encoder CLIP into a 3D occupancy model via differentiable volume rendering.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing 3D occupancy estimation methods rely on expensive 3D ground-truth labels [15, 25, 50].
- **p. 1 / 1. Introduction - extractive body cue:** These limitations hinder the adaptability and flexibility of autonomous systems in comprehending diverse and evolving environments.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations of ...
- **p. 1 / 1. Introduction - extractive body cue:** In summary, our contributions are: • Open vocabulary occupancy: A novel vision-only architecture to model arbitrary geometries and semantics by aligning the semantic feature space ...
- **p. 2 / 1. Introduction - extractive body cue:** Our model generalizes to estimate geometry and semantics in a zero-shot manner, without per-scene optimization like NeRF-approaches. • Feature subspace learning: In addition we introduce ...
- **p. 4 / 3.3. Volume Rendering Supervision - extractive body cue:** As a loss function, we propose the Cosine Similarity Guided MSE, which is a combination of the cosine similarity loss and the mean-squared error loss ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** (9) The dataset consists of just a few text prompts, enabling the training of U within seconds.
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like CLIP imposes a ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** Prior to training of our proposed model, we train a single linear transformation U ∈RL×L′ that maps from the original feature space L to the ...
- **p. 3 / 3.2. Model Architecture - extractive body cue:** 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During inference, the model just takes the 2D images as input and outputs the scene geometry and 3D vision-language features. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision) |
| State/latent | During, inference, model, just, takes, images, input, outputs, scene, geometry, vision-language, features | geometry, map, object/relationship state | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture) |
| Output/action | 3.3.) ℒ𝑙𝑎𝑛𝑔 2D vision-language features Volume Render (CLIP) Image Encoder Input images Reducer Feature Subspace Learning (Sec. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture), p. 3 (3.2. Model Architecture) |
| Objective/outcome | We have found that the MSE loss function has a much easier-tooptimize loss landscape, while the cosine similarity gives a better notion of how close the embeddings are in the CLIP space. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 2 (3.1. Problem Definition) |

## Main Claims and Actual Contribution

- 복셀 특징을 다시 영상으로 렌더링해 CLIP 특징과 맞추면서 명시적인 3차원 기하 정답 없이 장면 표현을 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2407.17310v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2407.17310v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2407.17310v2#page=5)
- Occ3D-nuScenes에서 열린 어휘 점유와 고정 클래스 의미 점유를 평가하고 시간 범위에 따른 성능을 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2407.17310v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2407.17310v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2407.17310v2#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.5. Ablations), p. 6 (4.3. 3D Open Vocabulary Retrieval) |
| Embodiment/environment | For zero-shot occupancy estimation, we evaluate on the widely known Occ3D-nuScenes benchmark [41], which provides semantic voxel labels for the nuScenes dataset. | hardware/simulator version and reset protocol | p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description) |
| Dataset/benchmark | We evaluate our approach against other recent approaches on the Occ3D-nuScenes dataset [41] and show the results in Tab. | role, split, size and leakage | p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 6 (4.2. Implementation Details) |
| Metric | LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any photometric losses or explicit depth supervision. | definition, denominator, direction and uncertainty | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 6 (4.1. Dataset and Task Description) |
| Baseline/ablation | As is visible, our method outperforms both baselines, even though we use just vision-based supervision. | fair input/data/compute/action matching | p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** As mentioned above, the reducer U finishes training within a second and thus does not impose any notable overhead.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Feature Subspace Learning), p. 3 (3.2. Model Architecture)이다.
