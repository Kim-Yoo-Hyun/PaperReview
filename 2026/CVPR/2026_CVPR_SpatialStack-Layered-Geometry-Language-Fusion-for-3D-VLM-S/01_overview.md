# SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Jian Zhang, Shijie Zhou, Bangya Liu, Achuta Kadambi, Zhiwen Fan
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: geometry, VLM, spatial reasoning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

SpatialStack은 기하 인코더의 여러 층에서 얻은 특징을 시각언어모형의 여러 깊이에 결합해 영상의 공간 관계를 추론한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large vision-language models (VLMs) still struggle with reliable 3D spatial reasoning, a core capability for embodied and physical AI systems.
- **p. 1 / Abstract - extractive body cue:** This limitation arises from their inability to capture fine-grained 3D geometry and spatial relationships.
- **p. 1 / Abstract - extractive body cue:** While recent efforts have introduced multi-view geometry transformers into VLMs, they typically fuse only the deep-layer features from vision and geometry encoders, discarding rich hierarchical ...
- **p. 1 / Abstract - extractive body cue:** To overcome this, we propose SpatialStack, a general hierarchical fusion framework that progressively aligns vision, geometry, and language representations across the model hierarchy.
- **p. 1 / Abstract - extractive body cue:** Moving beyond conventional late-stage vision-geometry fusion, SpatialStack stacks and synchronizes multi-level geometric features with the language backbone, enabling the model to capture both local geometric ...
- **p. 2 / 1. Introduction - extractive body cue:** Noticing these limitations of conventional VLMs, many recent works still prioritize image-level semantic alignment over the understanding of spatial and geometric structures [17, 32, 37].
- **p. 2 / 1. Introduction - extractive body cue:** Bridging this gap requires unifying geometric awareness with vision-language reasoning within a single framework, which is a key step toward reliable spatial intelligence.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions as follows: • We present the first systematic analysis of how fusion layers across vision encoders, geometry encoders, and LLM decoders ...
- **p. 2 / 1. Introduction - extractive body cue:** Building on these insights, we introduce SpatialStack, a general hierarchical fusion framework that integrates multi-level geometric features into multimodal LLMs.
- **p. 8 / Model - extractive body cue:** 5 shows that our method maintains robust general capabilities while specializing in spatial-temporal tasks, confirming no catastrophic forgetting.
- **p. 8 / Model - extractive body cue:** 4, our two versions of SpatialStack surpass all baselines of similar scale and same base models on both 2D and 3D subsets, demonstrating the benefits ...
- **p. 8 / Model - extractive body cue:** (%) Proprietary Models (API) GPT-4o [14] 74.8 83.0 78.9 Open-source Models Mini-Gemini-HD-34B [22] 71.5 79.2 75.4 LLaVA-NeXT-34B [19] 73.0 74.8 73.9 Cambrian-1-34B [40] 74.0 79.7 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | An initial line of work sought to compensate for these weaknesses by integrating explicit geometric inputs (e.g., precomputed point clouds or depth maps) into VLMs. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | initial, line, sought, compensate, weaknesses, integrating, explicit, geometric, inputs, precomputed, point, clouds | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Despite remarkable progress in large vision-language models (VLMs), reliable spatial reasoning remains challenging, as these models often fail to effectively encode 3D geometry and spatial relationships and to associate them with langua ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 서로 다른 층의 기하 신호를 대응하는 언어 처리 단계로 보내고 기하 입력의 깊이와 조합을 분석한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=5)
- VSI-Bench 등 공간 이해 평가에서 질의 유형별 성능과 기하 특징을 주입하는 설계의 효과를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption) |
| Embodiment/environment | VLM-3R reformulates spatial question-answer pairs in a VSI-Bench-style format, producing diverse reasoning tasks such as relative direction, object counting, and absolute distance estimation from real-world 3D-annotated scenes. | hardware/simulator version and reset protocol | p. 7 (5.1. Training), p. 7 (5.2. Evaluation) |
| Dataset/benchmark | We describe our training setup in Sec. | role, split, size and leakage | p. 7 (5.1. Training), p. 7 (5.2. Evaluation), p. 6 (5. Experiments) |
| Metric | Following the official protocol, we report mean MCA accuracy and Mean Relative Accuracy for NA across confidence thresholds C = 0.5, 0.55, . . . , 0.95. | definition, denominator, direction and uncertainty | p. 7 (5.2. Evaluation), p. 6 (Figure/Table caption), p. 7 (5.1. Training) |
| Baseline/ablation | Table 4. Comparison on CV-Bench. Built on Qwen2.5, SpatialStack-4B outperforms its base model alongside VG-LLM and Cambrian-S. Scaling to Qwen3.5, SpatialStack-5B further im- proves upon its baseline to set a new state-of-the-art. | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 7 (5.2. Evaluation), p. 6 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** We introduced SpatialStack, a hierarchical fusion framework bridging the gap between vision, geometry, and language for robust 3D spatial reasoning.
- **p. 7 / 5.2. Evaluation - extractive body cue:** Notably, despite lacking route-planning data during training, it still surpasses all open-source systems on this task, demonstrating robust zero-shot generalization for highlevel spatial reasoning.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. General Capabilities Evaluation. Our SpatialStack-5B maintains robust general multimodal and spatial-temporal reason- ing capabilities, demonstrating no catastrophic forgetting. Evaluation on CV-Bench. To assess ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 8 (Model), p. 7 (5.2. Evaluation), p. 5 (Figure/Table caption)이다.
