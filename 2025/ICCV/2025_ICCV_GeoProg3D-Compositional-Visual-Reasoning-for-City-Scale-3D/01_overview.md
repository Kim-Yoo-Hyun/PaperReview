# GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: Since existing methods primarily focus on indoor scenes, the highfidel ...를 문제로 두고, In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks via image ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform ...
- **p. 2 / 1. Introduction - extractive body cue:** To validate the effectiveness, we introduce novel tasks designed to assess urban-scale geographic visual reasoning capabilities and present GeoEval3D, a benchmark dataset specifically developed for ...
- **p. 6 / 4.1. Task Definition - extractive body cue:** The task set Qi = {(qk, ak)}Ki k=1 consists of pairs of queries qk and the corresponding ground truth answers ak.
- **p. 7 / 5.2. Experimental results - extractive body cue:** GeoProg3D further improved accuracy on both GoolgeEarth and UrbanScene3D.
- **p. 7 / 5.2. Experimental results - extractive body cue:** These results underscore the superior performance of GeoProg3D in estimating quantities within large-scale 3D scenes and highlight the effectiveness of the program-based inference procedures.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. ICE and instruction prompt. form height by identifying horizontal planes from Gaussian variance directions, while 6) applies clustering to filter out noisy activations ...
- **p. 8 / 5.2. Experimental results - extractive body cue:** Lastly, omitting the LargestSeg module affected the CMP performance, reducing the score to 44.74.
- **p. 8 / 5.2. Experimental results - extractive body cue:** The results in Table 7 show the significance of each component in maximizing the model's performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, when extending conventional 3D language fields for large-scale urban 3D scenes, two fundamental difficulties emerge: (1) Scalability for city-scale 3D data: Since existing methods primarily focus on indoor scenes, the highfidel ...를 문제로 두고, In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can perform various 3D geographic vision tasks via image ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 5 (Figure/Table caption), p. 8 (5.2. Experimental results) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
