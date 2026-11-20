# SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/oral/71166.
> PDF retrieval source: https://openreview.net/pdf/04fc204cb3233c6ac9f5867e72c861a9e835bc65.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Jing Wu, Jianhua Wu, Jiayi Guan, Jiahong Chen, Jinghui Lu, Hangjun Ye, Bingzhao Gao, Long Chen
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://icml.cc/virtual/2026/oral/71166
- Full-text retrieval: https://arxiv.org/pdf/2608.01899.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The aforementioned analysis highlights an unresolved core challenge: how to enhance the spatial intelligence of VLMs without extra 3D prior inputs or third-party spatial encoders, while preserving their general-purpose capabilities.를 문제로 두고, Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM vision tokens, eliminating reliance on sensor-based or ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning.
- **p. 1 / Abstract - extractive body cue:** Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs' general-purpose capabilities after spatial fine-tuning.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a parameter-efficient Spatio-vision Language Models (SpatioLM), that enhances spa
- **p. 1 / Abstract - extractive body cue:** Concretely, we design a plug-and-play and non-invasive spatiovision module that elicits the spatial knowledge inherent in VLMs.
- **p. 1 / Abstract - extractive body cue:** Furthermore, we innovatively leverage pseudo depth and camera information as supervision to guide the model in learning physically coherent representations.
- **p. 2 / 1. Introduction - extractive body cue:** The aforementioned analysis highlights an unresolved core challenge: how to enhance the spatial intelligence of VLMs without extra 3D prior inputs or third-party spatial encoders, ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle this core challenge, this work proposes a Spatiovision Language Model (SpatioLM), whose overall architecture is illustrated in Fig.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM ...
- **p. 3 / 3. Method - extractive body cue:** We propose SpatioLM, a unified framework that enhances VLMs with general physical spatial intelligence.
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...
- **p. 2 / 1. Introduction - extractive body cue:** Without modifying the core structure of the base VLM, SpatioLM enables flexible activation or deactivation during the inference phase, thereby enhancing the base VLM with ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** This mechanism allows the model to separately model fine-grained geometry within each frame and global geometric relationships across frames.
- **p. 5 / 3.3. Loss Design - extractive body cue:** The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- **p. 5 / 3.3. Loss Design - extractive body cue:** To align the SV-Block features with robust 3D representations, we apply Vision Token Supervision (VTS) by distilling them toward the latent features of a pretrained ...
- **p. 3 / 3.1. Problem definition and notation - extractive body cue:** During training, SpatioLM additionally predicts dense geometric outputs Y g = ( ¯D, ¯R), (2) where ¯D and ¯R serve as the pseudo-labels for the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 원문 대조: 모델 입력은 visual sequence X^v와 textual instruction X^t의 쌍이다. X^v는 T×H×W×3 RGB 입력이며 T=1은 image, T>1은 video를 뜻한다. Depth와 camera ray map은 뒤의 학습 supervision으로 구분된다. ([PDF p. 3](https://arxiv.org/pdf/2608.01899#page=3), §3.1 Problem definition and notation, Eq. (1)) | RGB image/video + text; extra 3D 입력으로 혼동하지 않음 | [PDF p. 3](https://arxiv.org/pdf/2608.01899#page=3), §3.1 Problem definition and notation, Eq. (1) |
| State/latent | input, sequence, model, defined, following, tuple, format, where, denotes, visual, images, videos | geometry, map, object/relationship state | p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 2 (1. Introduction) |
| Output/action | Subsequently, we fuse the extracted Hg i with the output of the vision-language tokens by the j-th LM block, which then serves as input to the (j+1)-th LM Block. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Spatio-Vision Module), p. 2 (1. Introduction), p. 3 (3.1. Problem definition and notation) |
| Objective/outcome | The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Loss Design), p. 3 (3.2. Spatio-Vision Module), p. 5 (3.3. Loss Design) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM ...
- **p. 3 / 3. Method - extractive body cue:** We propose SpatioLM, a unified framework that enhances VLMs with general physical spatial intelligence.
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...
- **p. 2 / 1. Introduction - extractive body cue:** Without modifying the core structure of the base VLM, SpatioLM enables flexible activation or deactivation during the inference phase, thereby enhancing the base VLM with ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** This mechanism allows the model to separately model fine-grained geometry within each frame and global geometric relationships across frames.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SpatioLM, a parameter-efficient framework that improves spatial intelligence in VLMs without extra 3D prior inputs or external spatial encoders. SpatioLM achieves ...
- **p. 7 / 4.2.1. SPATIAL PERCEPTION - extractive body cue:** It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on a ...
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** Its overall performance remains on par with the baseline and even improves on certain benchmarks (e.g., +12% on VideoMMMU).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 7 (4.2.1. SPATIAL PERCEPTION) |
| Embodiment/environment | To ensure rigorous evaluation and prevent data leakage, all training samples are strictly sourced from the official training splits of the respective datasets, reserving the validation and test splits exclusively for evaluation. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | In contrast, SpatialMLLM exhibits a substantial decline in general benchmarks, with reductions ranging from 23% to 67%. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Evaluation on General Capabilities), p. 7 (4.3. Evaluation on General Capabilities) |
| Metric | ScanQA is evaluated with BLEU-1 (B1), BLEU-4 (B4), METEOR (M), ROUGE-L (R), and CIDEr (C), while SQA3D uses exact match accuracy (E1) and its refined variant (ER1). | definition, denominator, direction and uncertainty | p. 7 (4.2.2. SPATIAL UNDERSTANDING), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 8 (Figure/Table caption) |
| Baseline/ablation | It significantly outperforms strong baselines on both single-image and multi-image metric depth, attains the highest accuracy on DA-2K, and demonstrates more stable generalization on a range of depth-related reasoning tasks. | fair input/data/compute/action matching | p. 7 (4.2.1. SPATIAL PERCEPTION), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5. Conclusion - extractive body cue:** Despite the effectiveness of SpatioLM, several limitations remain.
- **p. 9 / 5. Conclusion - extractive body cue:** Impact Statement Addressing the critical limitation of multimodal large models in visual spatial reasoning, this work proposes SpatioLM, a parameter-efficient spatial VLMs that enhances spatial ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 15. Failure consistency analysis on VSI-Bench. Consistency denotes the ratio of shared failures over SpatioLM failures. Task Type Ours Fail Base Fail Shared Consistency ...
- **p. 7 / 4.3. Evaluation on General Capabilities - extractive body cue:** Results indicate that, despite large-scale training targeted at spatial intelligence, the performance degradation of SpatioLM on general tasks is considerably smaller than that of baseline ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8. Visualization samples of our spatial perception benchmarks. The first row shows ground-truth single-image metric depth (MD-S), and the second row shows multi-image metric ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The aforementioned analysis highlights an unresolved core challenge: how to enhance the spatial intelligence of VLMs without extra 3D prior inputs or third-party spatial encoders, while preserving their general-purpose capabilities.를 문제로 두고, Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM vision tokens, eliminating reliance on sensor-based or ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design), p. 3 (3. Method), p. 3 (3.1. Problem definition and notation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
