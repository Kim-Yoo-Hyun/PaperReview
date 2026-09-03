# CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Therefore, enhancing 3D perception via 3DGS models has become an urgent challenge to address.를 문제로 두고, Overall, our contributions are summarized as follows: • We propose CLIP-GS, a simple yet effective framework for encoding 3DGS into features, leveraging a contrastive learning paradigm for multimodal per-taining. • We develop ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent works in 3D multimodal learning have made remarkable progress.
- **p. 1 / Abstract - extractive body cue:** However, typically 3D multimodal models are only capable of handling point clouds.
- **p. 1 / Abstract - extractive body cue:** Compared to the emerging 3D representation technique, 3D Gaussian Splatting (3DGS), the spatially sparse point cloud cannot depict the texture information of 3D objects, resulting ...
- **p. 1 / Abstract - extractive body cue:** This limitation constrains the potential of point cloud-based 3D multimodal representation learning.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present CLIPGS, a novel multimodal representation learning framework grounded in 3DGS.
- **p. 2 / 1. Introduction - extractive body cue:** Therefore, enhancing 3D perception via 3DGS models has become an urgent challenge to address.
- **p. 2 / 1. Introduction - extractive body cue:** Apart from the architectural design, the limited availability of 3DGS poses a significant challenge.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are summarized as follows: • We propose CLIP-GS, a simple yet effective framework for encoding 3DGS into features, leveraging a contrastive learning ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce a multimodal representation learning method leveraging 3DGS, termed CLIP-GS.
- **p. 3 / 4. Methodology - extractive body cue:** We introduce the feature extraction process from 3DGS, detailed in Sec.
- **p. 3 / 4. Methodology - extractive body cue:** We present CLIP-GS, a unified 3D pretraining framework for large-scale 3D representation learning by aligning 3DGS embeddings with the text-image aligned embeddings.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** In response, we propose the image voting loss (Limg).
- **p. 7 / Method - extractive body cue:** 5). • Baseline: We use the point cloud-based method, Uni3D [63], as the baseline model (1st row), and extract the P and C attributes of ...
- **p. 8 / Method - extractive body cue:** loss learns effective 3DGS and image alignment representation, further enhancing performance to establish stateof-the-art benchmarks (last row).
- **p. 8 / Method - extractive body cue:** 7, exploring the effectiveness of initializing transformer layers in CLIP-GS with either 2D pretraining models or point cloud pretraining models.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Here, position and color attributes (P & C) are extracted and input into a point cloud encoder, as detailed in [63]. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (4.1. Feature Extraction), p. 7 (Method) |
| State/latent | Here, position, color, attributes, extracted, input, point, cloud, encoder, detailed, Baseline, cloud-based | geometry, map, object/relationship state | p. 3 (4.1. Feature Extraction), p. 7 (Method), p. 8 (Method) |
| Output/action | 5). • Baseline: We use the point cloud-based method, Uni3D [63], as the baseline model (1st row), and extract the P and C attributes of gaussian points from 3DGS to simulate the ... | point map, pose, scene graph, affordance 또는 query result | p. 7 (Method), p. 8 (Method), p. 4 (4.2. Multi-model Alignment) |
| Objective/outcome | We also introduce a novel loss function, termed image voting loss, to guide the convergence of gradient optimization. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (4. Methodology), p. 8 (Method), p. 8 (Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are summarized as follows: • We propose CLIP-GS, a simple yet effective framework for encoding 3DGS into features, leveraging a contrastive learning ...
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce a multimodal representation learning method leveraging 3DGS, termed CLIP-GS.
- **p. 3 / 4. Methodology - extractive body cue:** We introduce the feature extraction process from 3DGS, detailed in Sec.
- **p. 3 / 4. Methodology - extractive body cue:** We present CLIP-GS, a unified 3D pretraining framework for large-scale 3D representation learning by aligning 3DGS embeddings with the text-image aligned embeddings.
- **p. 4 / 4.2. Multi-model Alignment - extractive body cue:** In response, we propose the image voting loss (Limg).
- **p. 5 / 5.2. Zero-Shot 3D Classification - extractive body cue:** CLIP-GS demonstrates a comprehensive improvement over existing zero-shot 3D classification models, achieving a performance boost of + 0.8, + 0.5 on Objaverse-GS and ModelNet-GS, respectively.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Comparison between point cloud reconstruction and 3D Gaussian Splatting (3DGS) reconstruction. (b) The 3DGS approach outperforms point cloud methods across multiple 3D ...
- **p. 5 / 5.1. Multimodal Retrieval - extractive body cue:** Our CLIP-GS outperforms point cloudbased methods across all retrieval tasks by a large margin.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (5.2. Zero-Shot 3D Classification), p. 1 (Figure/Table caption) |
| Embodiment/environment | 3 to construct the ModelNet-GS dataset. | hardware/simulator version and reset protocol | p. 5 (5.2. Zero-Shot 3D Classification), p. 5 (5.1. Multimodal Retrieval) |
| Dataset/benchmark | 3 to construct the ModelNet-GS dataset. | role, split, size and leakage | p. 5 (5.2. Zero-Shot 3D Classification), p. 5 (5.1. Multimodal Retrieval) |
| Metric | In line with [8], we measure performance using Top1 average accuracy and standard deviation, 4674 | definition, denominator, direction and uncertainty | p. 5 (5.3. Few-Shot 3D Classification), p. 5 (5.2. Zero-Shot 3D Classification), p. 7 (Figure/Table caption) |
| Baseline/ablation | Comparisons with state-of-the-art methods. | fair input/data/compute/action matching | p. 5 (5.1. Multimodal Retrieval), p. 1 (Figure/Table caption), p. 5 (5.1. Multimodal Retrieval) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** In this paper, we introduce CLIP-GS, a multimodal representation learning framework that aligns language, images, and 3DGS into a unified feature space.
- **p. 8 / 6. Conclusion - extractive body cue:** We also explore an efficient approach for generating 3DGS, rendered images, and text triplets.
- **p. 8 / 6. Conclusion - extractive body cue:** CLIP-GS achieves state-of-the-art performance across various 3D perception tasks including multimodal retrieval, zero-shot 3D classification, and few-shot 3D classification.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Therefore, enhancing 3D perception via 3DGS models has become an urgent challenge to address.를 문제로 두고, Overall, our contributions are summarized as follows: • We propose CLIP-GS, a simple yet effective framework for encoding 3DGS into features, leveraging a contrastive learning paradigm for multimodal per-taining. • We develop ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (4. Methodology), p. 4 (4.2. Multi-model Alignment), p. 7 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
