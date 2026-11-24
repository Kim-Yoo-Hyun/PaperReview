# SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Yue Li, Qi Ma, Runyi Yang, Huapeng Li, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Ender Konukoglu, Theo Gevers, Luc Van Gool, Martin R. Oswald, Danda Pani Paudel
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, Vision-Language, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf)

## Why This Paper Is Here

SceneSplat은 실내 장면의 가우시안 파라미터를 직접 입력으로 받아 장면을 넘나드는 3차원 의미 표현을 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recognizing arbitrary or previously unseen categories is essential for comprehensive real-world 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** Currently, all existing methods rely on 2D or textual modalities during training or together at inference.
- **p. 1 / Abstract - extractive body cue:** This highlights the clear absence of a model capable of processing 3D data alone for learning semantics end-to-end, along with the necessary data to train ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, 3D Gaussian Splatting (3DGS) has emerged as the de facto standard for 3D scene representation across various vision tasks.
- **p. 1 / Abstract - extractive body cue:** However, effectively integrating semantic reasoning into 3DGS in a generalizable manner remains an open challenge.
- **p. 2 / 1. Introduction - extractive body cue:** This highlights a key limitation: the absence of a robust model for processing 3D data end-to-end for semantic learning, along with the lack of sufficient ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this gap, current methods resort to multi-modality fusion, distilling knowledge from 2D vision-language models into 3D data.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose GaussSSL, a self-supervised learning scheme that unlocks rich 3D feature learning from unlabeled scenes.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** We propose to mitigate the decoder collapse issues by multitask reconstruction LMGM, as coding rate regularization stabilizes only the hierarchical encoder.
- **p. 4 / 4. Methodology - extractive body cue:** Building upon the SceneSplat-7K dataset, we carry out both vision-language 3DGS pretraining, which enables openvocabulary scene understanding, and self-supervised pretraining, which regularizes the latent space ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** 4.2, the precomputed language feature enables effective knowledge distillation.
- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels.
- **p. 5 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** To enforce feature similarity in Euclidean space, we use L2 loss: \ m ath c al {L }_{ 2 } = \ frac {1}{/\mathcal {V}/} ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (5) The output tokens ˆ Tm are mapped to the input Gaussian space with the reconstruction projector ˆGm = Φ( ˆTm) ∈RN′×F . | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4.3. Self Supervised Pretraining), p. 2 (1. Introduction) |
| State/latent | output, tokens, mapped, input, Gaussian, space, reconstruction, projector, SceneSplat, introduces, DGS, encoder | geometry, map, object/relationship state | p. 5 (4.3. Self Supervised Pretraining), p. 2 (1. Introduction), p. 4 (4.2. Vision-Language 3DGS Pretraining) |
| Output/action | SceneSplat introduces a 3DGS encoder that takes as input the parameters of a Gaussian-splat scene (center, scale, color, opacity) and outputs semantic features in a per-primitive manner, in a single forward pass. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining) |
| Objective/outcome | The cosine similarity loss minimizes the angular difference be4964 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.3. Self Supervised Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining) |

## Main Claims and Actual Contribution

- 기존 실내 스캔 자료를 공통 가우시안 표현으로 재구성해 SceneSplat-7K를 만들고 주석 없는 장면에도 적용할 자기지도 학습을 제시한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=5)
- 가우시안 공간의 의미 분할과 개방 어휘 장면 이해를 비교하고 사전학습과 입력 표현의 영향을 확인했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

SceneSplat-7K의 7,916개 장면은 일곱 기존 실내 자료에서 구축한 가우시안 표현이다. 주석이 없는 장면을 자기지도 학습에 활용하며, 평가 단위는 장면의 의미 예측이다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf#page=4)

## Explicit Limitations and Failure Boundary

- **p. 8 / 5.3. Further Statistical Evaluation - extractive body cue:** Low PSNRs usually come out of blurry input images, poor Gaussian centers optimization, and insufficient scene coverage, where the 3DGS parameters cannot resolve the scene ...
- **p. 7 / 5.3. Further Statistical Evaluation - extractive body cue:** Although the collected labels are not perfect, large-scale pretraining can filter noise and learn meaningful patterns.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining)이다.
