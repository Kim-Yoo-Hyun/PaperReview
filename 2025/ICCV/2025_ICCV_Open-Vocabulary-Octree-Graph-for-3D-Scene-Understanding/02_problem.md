# Problem - Open-Vocabulary Octree-Graph for 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Point clouds are unordered discrete coordinates that require considerable storage space, making existing methods inefficient to deploy on embodied agents with limited storage resources.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Open-vocabulary 3D scene understanding is indispensable for embodied agents.
- **p. 1 / Abstract - extractive PDF cue:** Recent works leverage pretrained vision-language models (VLMs) for object segmentation and project them to point clouds to build 3D maps.
- **p. 1 / Abstract - extractive PDF cue:** Despite progress, a point cloud is a set of unordered coordinates that requires substantial storage space and does not directly convey occupancy information or spatial ...
- **p. 1 / Abstract - extractive PDF cue:** To address these issues, we propose Octree-Graph, a novel scene representation for open-vocabulary 3D scene understanding.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, a Chronological Group-wise Segment Merging (CGSM) strategy and an Instance Feature Aggregation (IFA) algorithm are first designed to get 3D instances and corresponding semantic ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Point clouds are unordered discrete coordinates that require considerable storage space, making existing methods inefficient to deploy on embodied agents with limited storage resources.
- **p. 1 / 1. Introduction - extractive PDF cue:** Moreover, point clouds lack explicit representation of occupancy information and spatial connectivity which are critical for downstream tasks, e.g., path planning and text-based object retrieval.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Point clouds are unordered discrete coordinates that require considerable storage space, making existing methods inefficient to deploy on embodied agents with limited ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | First, given input images, 2D proposals are segmented via an off-the-shelf segmenter, and corresponding visual-language features are extracted by pretrained VLMs. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | First, given, input, images, proposals, segmented, off-the-shelf, segmenter, corresponding, visual-language | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Given, RGB-D, sequence, camera, poses, mainstream, methods, leverage | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: First, given, input, images, proposals, segmented, off-the-shelf, segmenter, corresponding, visual-language | p. 2 (1. Introduction), p. 4 (3.3. Chronological Group-wise Segment Merging), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, Octree-Graph, open-vocabulary, scene, understanding, efficiently | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.3. Chronological Group-wise Segment Merging) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.3. Quantitative Comparison), p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Moreover, point clouds lack explicit representation of occupancy information and spatial connectivity which are critical for downstream tasks, e.g., path planning and text-based object retrieval.
- **p. 2 / 1. Introduction - extractive PDF cue:** To alleviate these problems, we propose Octree-Graph as shown in Fig.
- **p. 2 / 1. Introduction - extractive PDF cue:** Unlike existing works that directly average features as a result, we simultaneously consider the representativeness and distinctiveness of a feature during the fusion process.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.3. Chronological Group-wise Segment Merging), p. 4 (3.5. Octree-Graph Construction and Applications), p. 4 (3.5. Octree-Graph Construction and Applications)): Our contributions are summarized as follows. • We propose the Octree-Graph for open-vocabulary 3D scene understanding, which efficiently depicts objects' occupancies, semantics, and relations, benefiting several downstream tasks. • We ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To alleviate these problems, we propose Octree-Graph as shown in Fig.
- **p. 3 / 3.3. Chronological Group-wise Segment Merging - extractive PDF cue:** To this end, we propose a Chronological Group-wise Segment Merging (CGSM) strategy with semantic-guided under-segment filtering and a dynamic threshold decay strategy.
- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** The node Ni consists of correlated semantics ns i (e.g., captions and features), center nc i, and adaptive-octree no i .
- **p. 4 / 3.5. Octree-Graph Construction and Applications - extractive PDF cue:** Furthermore, we propose an adaptive-octree to depict the occupancy information of each object, which acts as a node of the Octree-Graph.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | We also analyze the impact of hyper-parameter I, and the results in Rows 3-5 show that our method ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 4 (3.3. Chronological Group-wise Segment Merging), p. 1 (1. Introduction), p. 4 (3.5. Octree-Graph Construction and Applications). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 4 (3.3. Chronological Group-wise Segment Merging), p. 1 (1. Introduction), p. 4 (3.5. Octree-Graph Construction and Applications), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
