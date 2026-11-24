# Masked Autoencoders for Point Cloud Self-supervised Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.06604.
> PDF retrieval source: https://arxiv.org/pdf/2203.06604. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ECCV
- Authors: Yatian Pang, Wenxiao Wang, Francis E. H. Tay, Wei Liu, Yonghong Tian, Li Yuan
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/2203.06604
- Full-text retrieval: https://arxiv.org/pdf/2203.06604
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Point-MAE는 점군의 많은 국소 패치를 가리고 보이는 패치에서 가려진 점 좌표를 복원하는 방식으로 표현을 사전학습한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=1)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Self-supervised learning learns latent features from unlabeled data instead of building representations based on human-defined annotations.
- **p. 1 / 1 Introduction - extractive body cue:** It is usually done by designing a pretext task to pre-train the model, then fine-tune on downstream tasks.
- **p. 1 / 1 Introduction - extractive body cue:** Relying less on labeled data, self-supervised learning has significantly advanced natural language processing (NLP) [11,4,32,33] and computer ⋆Corresponding author
- **p. 2 / 1 Introduction - extractive body cue:** Among them, masked autoencoding [17,49,2], illustrated in Figure 1, is a promising scheme for both languages and images.
- **p. 2 / 1 Introduction - extractive body cue:** It randomly masks a portion of input data and adopts an autoencoder to reconstruct explicit features (e.g., pixels) or implicit features (e.g., discrete tokens) corresponding ...
- **p. 3 / 1 Introduction - extractive body cue:** To this end, we first analyze the main challenges of introducing masked autoencoding for point cloud from the following aspects: (i) Lack of a unified ...
- **p. 3 / 1 Introduction - extractive body cue:** In other words, if being masked, the points that contain high-density information is more difficult to be recovered in the reconstruction task.

## Core Idea

- **p. 5 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows: (1) We propose a novel scheme of masked autoencoders for point cloud selfsupervised learning, addressing key issues ...
- **p. 4 / 1 Introduction - extractive body cue:** Driven by the analysis, we propose a novel self-supervised learning framework for Point cloud by designing a neat and efficient scheme of Masked AutoEncoders, termed ...
- **p. 4 / 1 Introduction - extractive body cue:** As shown in Figure 3, our Point-MAE mainly consists of a point cloud masking and embedding module, and an autoencoder.
- **p. 2 / 1 Introduction - extractive body cue:** As masked parts do not provide data information, this reconstruction task enables the autoencoder to learn high-level latent features from unmasked parts.
- **p. 5 / 1 Introduction - extractive body cue:** (2) We show with our approach, a simple architecture that is entirely based on standard Transformers can surpass dedicated Transformer models from supervised learning.
- **p. 1 / 4 Tencent Data Platform - extractive body cue:** Then, a standard Transformer based autoencoder, with an asymmetric design and a shifting mask tokens operation, learns high-level latent features from unmasked point patches, aiming ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, BERT [11] in NLP and MAE [17] in computer vision both apply masked autoencoding and adopt a standard Transformer architecture as autoencoder's backbone ...
- **p. 3 / 1 Introduction - extractive body cue:** Different from previous methods that use dedicated Transformers or adopt extra non-Transformers models to assist (such as Point-BERT [54] uses an extra DGCNN [44]), we ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (3) From the perspective of multimodal learning, our work inspires that unified architectures for languages and especially images, such as masked autoencoders, are also applicable for point cloud, when equipped with a ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (1 Introduction), p. 1 (4 Tencent Data Platform) |
| State/latent | perspective, multimodal, learning, inspires, unified, architectures, languages, especially, images, masked, autoencoders, applicable | geometry, map, object/relationship state | p. 5 (1 Introduction), p. 1 (4 Tencent Data Platform), p. 4 (1 Introduction) |
| Output/action | Concretely, we divide the input point cloud into irregular point patches and randomly mask them at a high ratio. | point map, pose, scene graph, affordance 또는 query result | p. 1 (4 Tencent Data Platform), p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Objective/outcome | Furthermore, our work inspires the feasibility of applying unified architectures from languages and images to the point cloud. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (4 Tencent Data Platform) |

## Main Claims and Actual Contribution

- 인코더에는 보이는 패치만 넣고 마스크 토큰은 디코더에 추가하는 비대칭 구조로 좌표 복원을 학습한다. [PDF 4쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=4) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=7)
- 실측 ScanObjectNN과 CAD 기반 ModelNet40의 분류, 소수 예시 분류에서 사전학습한 표현을 비교했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136620591.pdf#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (4 Experiments), p. 14 (2.60 93.19 Random) |
| Embodiment/environment | 4.2 Downstream Tasks Object Classification on Real-World Dataset In SSL for point cloud, one of the main concerns is to design a model with high generalization capability. | hardware/simulator version and reset protocol | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | Object Classification on clean objects dataset We evaluate our pre-trained model on ModelNet40 [46] for object classification. | role, split, size and leakage | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Metric | We conduct experiments using two masking strategy with different masking ratios (%), and report pre-train loss (× 1000) as well as fine-tune accuracy (%). | definition, denominator, direction and uncertainty | p. 13 (4 Experiments), p. 12 (4 Experiments), p. 14 (2.60 93.19 Random) |
| Baseline/ablation | Furthermore, our method speeds up pre-training by 1.7× compared to Point-BERT [54]. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 2.60 93.19 Random - extractive body cue:** The leakage of location information makes the reconstruction task less challenging, and the model cannot learn latent features well, leading to worse fine-tune performance.
- **p. 13 / 4 Experiments - extractive body cue:** Our segmentation head is relatively simple and does not use any propagating operation or DGCNN [44].
- **p. 14 / 2.60 93.19 Random - extractive body cue:** The performance degrades largely with low making ratios and also degrades slightly if the masking ratio is too high.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (4 Tencent Data Platform)이다.
