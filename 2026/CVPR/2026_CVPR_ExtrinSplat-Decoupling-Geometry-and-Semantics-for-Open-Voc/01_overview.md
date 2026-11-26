# ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Jiayu Ding, Xinpeng Liu, Zhiyi Pan, Shiqiang Long, Ge Li
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, semantic, retrieval, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

ExtrinSplat은 3차원 Gaussian마다 의미 특징을 저장하는 대신 물체 그룹에 텍스트 설명을 연결해 열린 어휘 질의를 처리한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge.
- **p. 1 / Abstract - extractive body cue:** Mainstream methods, built on an embedding paradigm, suffer from three key flaws: (i) geometry-semantic inconsistency, where points, rather than objects, serve as the semantic basis, ...
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we introduce ExtrinSplat, a framework built on the extrinsic paradigm that decouples geometry from semantics.
- **p. 1 / Abstract - extractive body cue:** Instead of embedding features, ExtrinSplat clusters Gaussians into multi-granularity, overlapping 3D object groups.
- **p. 1 / 1. Introduction - extractive body cue:** Open-vocabulary 3D scene understanding enables the parsing of 3D scenes with arbitrary natural language queries, moving beyond the limitations of predefined categories to offer enhanced ...
- **p. 1 / 1. Introduction - extractive body cue:** The primary challenge in this domain lies in finding an efficient and effective 3D scene representation.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose the extrinsic paradigm, a distinct, decoupled and layered architecture.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose ExtrinSplat, a new framework realizing the extrinsic paradigm, which efficiently decouples 3D geometry and semantics through ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose the extrinsic paradigm, a distinct, decoupled and layered architecture.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input.
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** We present ExtrinSplat, a training-free framework that realizes the extrinsic paradigm by decoupling 3D geometry from semantics, as shown in Fig.
- **p. 5 / 3.3. Object-level Grouping - extractive body cue:** (b) Our method (via semantic distillation): We leverage DAM2SAM to track a single instance.
- **p. 4 / 3.3. Object-level Grouping - extractive body cue:** Specifically, for each group, we first identify the object's high-confidence core via mask back-projection, then refine its boundaries by identifying and excluding ambiguous points with ...
- **p. 3 / 3.1. Overall Architecture - extractive body cue:** Then, the instance feature extraction stage (§3.4) uses a VLM to generate textual hypotheses for each object group.
- **p. 7 / 2) Baselines. We compare our method with several recent - extractive body cue:** Method Ramen Teatime Figurines Waldo Mean 2D Methods LEGaussians 46.0 60.3 40.8 39.4 46.6 LangSplat 51.2 65.1 44.7 44.5 51.4 Feature-3DGS 43.7 58.8 40.5 39.6 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our method takes an optimized 3DGS scene representation and its corresponding image sequence as input. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Overall Architecture), p. 5 (3.3. Object-level Grouping) |
| State/latent | takes, optimized, DGS, scene, representation, corresponding, image, sequence, input, Mainstream, direct, extraction | geometry, map, object/relationship state | p. 3 (3.1. Overall Architecture), p. 5 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture) |
| Output/action | (a) Mainstream method (via direct extraction): All object masks, typically generated by SAM, are used to directly extract CLIP image features. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture), p. 4 (3.2. Data Preparation) |
| Objective/outcome | This design minimizes the requirements for perfect input data (see Appendix for details). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Data Preparation), p. 5 (3.4. Instance Feature Extraction), p. 6 (2) Baselines. We compare our method with several recent) |

## Main Claims and Actual Contribution

- 여러 크기의 겹치는 Gaussian 그룹을 만들고 시각언어모델이 생성한 설명을 외부 색인으로 연결한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=5)
- 열린 어휘 물체 선택·의미 분할 정확도와 장면 적응 시간·저장 비용을 함께 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | Given a text query as input, the task is to produce multi-view renderings of the semantically corresponding 3D instance(s). | hardware/simulator version and reset protocol | p. 5 (4.1. Open-Vocabulary Object Selection in 3D Space) |
| Dataset/benchmark | Given a text query as input, the task is to produce multi-view renderings of the semantically corresponding 3D instance(s). | role, split, size and leakage | p. 5 (4.1. Open-Vocabulary Object Selection in 3D Space) |
| Metric | Figure 1. Overview of our method. (a) Multi-view 2D segmentation masks are first extracted from the input scene. (b) Based on these masks, our method lifts the objects into 3D point groups ... | definition, denominator, direction and uncertainty | p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Baseline/ablation | Table 5. Ablation on feature extraction. We compare VLM-based text distillation against CLIP image baselines. Case Feature Source View Aggregation mIoU↑ #1 Image | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** Despite its strong performance, our method has certain limitations: 1) The accuracy of our object-level grouping can be compromised by substantially inaccurate initial segmentation masks ...
- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** Addressing these issues remains a promising direction for future work.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results on object selection from the LERF dataset. OpenGaussian fails to separate nearby objects or maintain sharp boundaries, while Dr.Splat struggles to ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. Object-level Grouping), p. 3 (3.1. Overall Architecture)이다.
