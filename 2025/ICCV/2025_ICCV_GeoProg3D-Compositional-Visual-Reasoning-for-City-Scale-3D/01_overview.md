# GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Shunsuke Yasuki, Taiki Miyanishi, Nakamasa Inoue, Shuhei Kurita, Koya Sakamoto, Daichi Azuma, Masato Taki, Yutaka Matsuo
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf)

## Why This Paper Is Here

GeoProg3D는 도시 규모 3D 장면에 대한 복합 언어 질문을 거리·방향·고도·랜드마크를 이용한 공간 연산으로 나누어 푼다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The advancement of 3D language fields has enabled intuitive interactions with 3D scenes via natural language.
- **p. 1 / Abstract - extractive body cue:** However, existing approaches are typically limited to smallscale environments, lacking the scalability and compositional reasoning capabilities necessary for large, complex urban settings.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we propose GeoProg3D, a visual programming framework that enables natural language-driven interactions with city-scale highfidelity 3D scenes.
- **p. 1 / Abstract - extractive body cue:** GeoProg3D consists of two key components: (i) a Geography-aware City-scale 3D Language Field (GCLF) that leverages a memory-efficient hierarchical 3D model to handle large-scale data, ...
- **p. 1 / Abstract - extractive body cue:** Our framework employs large language models (LLMs) as reasoning engines to dynamically combine GV-APIs and operate GCLF, effectively supporting diverse geographic vision tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: Since existing methods ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive body cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive body cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks via image ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | summary, contributions, threefold, GeoProg3D, framework, compositional, reasoning, over, city-scale, language, fields, where | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Dataset construction and statistics) |
| Output/action | However, intuitive and efficient interaction with these detailed 3D city models using natural language remains largely unexplored. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 6 (4.3. Dataset construction and statistics) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 계층적 3D 언어 장과 지리·시각 연산 API를 만들고 언어 모델이 필요한 연산을 조합한 프로그램을 생성하도록 했다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=6)
- GeoEval3D에서 공간 관계 판단, 수량, 거리 등 질의 유형별로 정확도 또는 측정 오차를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results) |
| Embodiment/environment | The dataset B = {(Di, Qi)}S i=1 consists of pairs multi-view image sets Di and task sets Qi, where S is the number of outdoor scenes. | hardware/simulator version and reset protocol | p. 6 (4. GeoEval3D Dataset), p. 6 (4. GeoEval3D Dataset) |
| Dataset/benchmark | We perform experiments on five scenes across the two datasets: four scenes from GoogleEarth and one scene from UrbanScene3D. | role, split, size and leakage | p. 6 (4. GeoEval3D Dataset), p. 6 (4. GeoEval3D Dataset), p. 7 (5.1. Evaluation metrics), p. 7 (5.2. Experimental results) |
| Metric | Localization accuracy is measured at an IoU threshold of 0.15. | definition, denominator, direction and uncertainty | p. 7 (5.1. Evaluation metrics), p. 7 (5.1. Evaluation metrics), p. 8 (5.2. Experimental results) |
| Baseline/ablation | We observed that GCLF outperforms baselines on GoogleEarth. | fair input/data/compute/action matching | p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 8 (5.2. Experimental results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent ...
- **p. 8 / 5.2. Experimental results - extractive body cue:** Ablation study of different Geographical Vision APIs. itative examples and failure cases.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** Note that MES-H and CMP are not evaluated in UrbanScene3D because Ground Truth for height cannot be obtained.
- **p. 7 / 5.2. Experimental results - extractive body cue:** These results demonstrate the limitations of localization using 3D language fields alone in 3D urban scenes and the effectiveness of GV-APIs and visual programming in ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 7 (5.2. Experimental results), p. 5 (Figure/Table caption), p. 8 (5.2. Experimental results)이다.
