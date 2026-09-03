# Problem - SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Visual Grounding (3DVG) aims to locate objects in 3D scenes based on textual descriptions, essential for applications like augmented reality and robotics.
- **p. 1 / Abstract - extractive body cue:** Traditional 3DVG approaches rely on annotated 3D datasets and predefined object categories, limiting scalability and adaptability.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we introduce SeeGround, a zero-shot 3DVG framework leveraging 2D Vision-Language Models (VLMs) trained on largescale 2D data.
- **p. 1 / Abstract - extractive body cue:** SeeGround represents 3D scenes as a hybrid of query-aligned rendered images and spatially enriched text descriptions, bridging the gap between 3D data and 2D-VLMs input ...
- **p. 1 / Abstract - extractive body cue:** We propose two modules: the Perspective Adaptation Module, which dynamically selects viewpoints for query-relevant image rendering, and the Fusion Alignment Module, which integrates 2D images ...
- **p. 2 / 1. Introduction - extractive body cue:** This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details.
- **p. 2 / 1. Introduction - extractive body cue:** However, when textual descriptions and images are processed separately by 2D-VLMs, the model cannot associate 3D spatial information from text to the object in the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This approach avoids redundancy in multi-view methods and limitations of bird's-eye views, which lack height and orientation details. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | ies [55, 60] attempt to reduce 3D-specific training requirements by reformatting 3D scenes and text descriptions for large language models (LLMs) [38, ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | attempt, reduce, D-specific, training, requirements, reformatting, scenes, text, descriptions, large | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | goal, output, directed, bounding, bbox, object, identifies, target | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: attempt, reduce, D-specific, training, requirements, reformatting, scenes, text, descriptions, large | p. 2 (1. Introduction), p. 3 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology) |
| Decision / output variable | geometry/map/query r; body terms: contributions, follows, introduce, SeeGround, training-free, solution, zero-shot, DVG | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.2. Comparative Study), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, when textual descriptions and images are processed separately by 2D-VLMs, the model cannot associate 3D spatial information from text to the object in the ...
- **p. 1 / 1. Introduction - extractive body cue:** Previous research has focused on specific scenarios, where models [5, 19, 41, 52, 59, 62, 63] are trained on small-scale datasets, limiting their scalability and ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 4 (3.2. Perspective Adaptation Module)): Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.

- **p. 2 / 1. Introduction - extractive body cue:** Considering that 2D-VLMs cannot process 3D data directly, we introduce a cross-modal alignment representation that enables 2D-VLMs to interpret 3D scenes.
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.
- **p. 3 / 3. Methodology - extractive body cue:** This representation allows our framework to align the rich visual features from 2D renderings with the spatial context from 3D scene descriptions.
- **p. 4 / 3.2. Perspective Adaptation Module - extractive body cue:** To meet these needs, we propose a query-driven dynamic scene rendering method that aligns the rendered viewpoint with the query description, capturing more scene details, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Bird's Eye View, though comprehensive, cannot adjust to the query and misses key spatial details like object orientation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Current viewpoint selection strategies also fall short in handling complex scenarios like "when the window is on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. Overview of the SeeGround framework. We first use a 2D-VLM to interpret the query, identifying both ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 3 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology), p. 4 (3.1. Multimodal 3D Representation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology), p. 4 (3.1. Multimodal 3D Representation), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
