# SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D visual grounding, zero-shot, open-vocabulary
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details.를 문제로 두고, Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Visual Grounding (3DVG) aims to locate objects in 3D scenes based on textual descriptions, essential for applications like augmented reality and robotics.
- **p. 1 / Abstract - extractive body cue:** Traditional 3DVG approaches rely on annotated 3D datasets and predefined object categories, limiting scalability and adaptability.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we introduce SeeGround, a zero-shot 3DVG framework leveraging 2D Vision-Language Models (VLMs) trained on largescale 2D data.
- **p. 1 / Abstract - extractive body cue:** SeeGround represents 3D scenes as a hybrid of query-aligned rendered images and spatially enriched text descriptions, bridging the gap between 3D data and 2D-VLMs input ...
- **p. 1 / Abstract - extractive body cue:** We propose two modules: the Perspective Adaptation Module, which dynamically selects viewpoints for query-relevant image rendering, and the Fusion Alignment Module, which integrates 2D images ...
- **p. 2 / 1. Introduction - extractive body cue:** This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details.
- **p. 2 / 1. Introduction - extractive body cue:** However, when textual descriptions and images are processed separately by 2D-VLMs, the model cannot associate 3D spatial information from text to the object in the ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.
- **p. 2 / 1. Introduction - extractive body cue:** Considering that 2D-VLMs cannot process 3D data directly, we introduce a cross-modal alignment representation that enables 2D-VLMs to interpret 3D scenes.
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.
- **p. 3 / 3. Methodology - extractive body cue:** This representation allows our framework to align the rich visual features from 2D renderings with the spatial context from 3D scene descriptions.
- **p. 4 / 3.2. Perspective Adaptation Module - extractive body cue:** To meet these needs, we propose a query-driven dynamic scene rendering method that aligns the rendered viewpoint with the query description, capturing more scene details, ...
- **p. 5 / 3.3. Fusion Alignment Module - extractive body cue:** To address this, we introduce the Fusion Alignment Module, which explicitly associates key visual features in the scene with the textual description, ensuring a clear ...
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** Finally, the 2D-VLM outputs the target object's ID, which is then used to retrieve its 3D bounding box from the OLT , providing the final, ...
- **p. 3 / 3.1. Multimodal 3D Representation - extractive body cue:** To tackle this problem, in this work, we propose a hybrid representation that combines "2D rendered images" and "text-based 3D spatial descriptions".

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | ies [55, 60] attempt to reduce 3D-specific training requirements by reformatting 3D scenes and text descriptions for large language models (LLMs) [38, 39], but these methods primarily rely on text input, neglecting ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3.1. Multimodal 3D Representation) |
| State/latent | attempt, reduce, D-specific, training, requirements, reformatting, scenes, text, descriptions, large, language, models | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology) |
| Output/action | However, prior 3D scene representations - such as point clouds [14, 40], voxels [29], and implicit representations [22] - are not directly compatible with the input format required by 2D-VLM. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology), p. 4 (3.1. Multimodal 3D Representation) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.
- **p. 2 / 1. Introduction - extractive body cue:** Considering that 2D-VLMs cannot process 3D data directly, we introduce a cross-modal alignment representation that enables 2D-VLMs to interpret 3D scenes.
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.
- **p. 3 / 3. Methodology - extractive body cue:** This representation allows our framework to align the rich visual features from 2D renderings with the spatial context from 3D scene descriptions.
- **p. 4 / 3.2. Perspective Adaptation Module - extractive body cue:** To meet these needs, we propose a query-driven dynamic scene rendering method that aligns the rendered viewpoint with the query description, capturing more scene details, ...
- **p. 7 / 4.2. Comparative Study - extractive body cue:** Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%).
- **p. 7 / 4.2. Comparative Study - extractive body cue:** While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential for ...
- **p. 6 / 4.2. Comparative Study - extractive body cue:** 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and the weakly supervised WS-3DVG [50], achieving competitive results with ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study) |
| Embodiment/environment | We use two popular benchmark datasets to evaluate our 3DVG approach. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Dataset/benchmark | Finally, high-quality rendering provides clearer information about object boundaries, textures, and colors, helping models more accurately identify and distinguish objects, Our current use of point clouds from the dataset limits renderi ... | role, split, size and leakage | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), p. 7 (4.2. Comparative Study) |
| Metric | While fully supervised methods like MCLN [41] and ConcreteNet [47] achieve higher accuracy, our proposed SeeGround framework demonstrates competitive zero-shot performance, highlighting its potential for scalable, annotation-free 3D gro ... | definition, denominator, direction and uncertainty | p. 7 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study) |
| Baseline/ablation | 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and the weakly supervised WS-3DVG [50], achieving competitive results with supervised methods. | fair input/data/compute/action matching | p. 6 (4.2. Comparative Study), p. 7 (4.2. Comparative Study), p. 7 (4.3. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Ablation Study - extractive body cue:** ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Bird's Eye View, though comprehensive, cannot adjust to the query and misses key spatial details like object orientation and height.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Current viewpoint selection strategies also fall short in handling complex scenarios like "when the window is on the left" or "upon entering from the door".
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both the target object (e.g., "laptop") and a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Visualization of scene details from different viewpoints. The Bird's Eye View (a) captures the entire scene layout but lacks object-specific detail, while the ...
- **p. 7 / 4.2. Comparative Study - extractive body cue:** In the Easy and Hard categories, our method reaches 54.5% and 38.3%, showing robustness across varying scene complexities.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details.를 문제로 두고, Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
