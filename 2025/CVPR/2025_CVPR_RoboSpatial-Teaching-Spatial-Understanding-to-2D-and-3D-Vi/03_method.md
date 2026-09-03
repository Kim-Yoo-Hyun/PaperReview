# Method - RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.2. Dataset Generation), p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.1. Spatial Relationships), p. 6 (Model), p. 6 (Model)): To ensure that models learn from visual grounding rather than linguistic priors, we use deterministic templates that avoid ambiguity and minimize reliance on commonsense.

## Method Body Digest

- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** To ensure that models learn from visual grounding rather than linguistic priors, we use deterministic templates that avoid ambiguity and minimize reliance on commonsense.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** Stage 1: 3D Spatial Relation Extraction The first stage involves extracting spatial relationships between objects or between objects and free space, based on 3D geometry.
- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** This supervision helps models more accurately resolve references during spatial reasoning and is included during training.
- **p. 4 / 3.1. Spatial Relationships - extractive body cue:** Configuration enables robots to understand and interpret the relative positioning of objects, which is crucial for directing navigation, manipulation, and interaction within complex environments.
- **p. 6 / Model - extractive body cue:** As a result, reported scores represent a conservative estimate of each model's spatial understanding.
- **p. 6 / Model - extractive body cue:** Bolded number is the best result for the column. ordinate predictions, we evaluate whether the model's predicted 3D location lies within the convex hull of ...
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** For each spatial configuration task, we evaluate all visible object pairs that appear uniquely in the image, avoiding duplicate instances to minimize ambiguity.
- **p. 5 / 3.2. Dataset Generation - extractive body cue:** The final answer is a list of 2D (x, y) image coordinates that satisfy the spatial context constraint.

## Design Rationale

- **p. 4 / 3.2. Dataset Generation - extractive body cue:** The output is a spatial reasoning dataset D, where each entry di = hIi, qi, ai, lii consists of an image Ii, a question qi, ...
- **p. 1 / 1. Introduction - extractive body cue:** This illustration demonstrates how a model trained on ROBOSPATIAL enables human-aligned spatial reasoning within the correct reference frame, supporting task grounding, planning, and detection for ...
- **p. 4 / 3.1. Spatial Relationships - extractive body cue:** Configuration enables robots to understand and interpret the relative positioning of objects, which is crucial for directing navigation, manipulation, and interaction within complex environments.

## Source Evidence Cues

- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** To ensure that models learn from visual grounding rather than linguistic priors, we use deterministic templates that avoid ambiguity and minimize reliance on commonsense.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** Stage 1: 3D Spatial Relation Extraction The first stage involves extracting spatial relationships between objects or between objects and free space, based on 3D geometry.
- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** This supervision helps models more accurately resolve references during spatial reasoning and is included during training.
- **p. 4 / 3.1. Spatial Relationships - extractive body cue:** Configuration enables robots to understand and interpret the relative positioning of objects, which is crucial for directing navigation, manipulation, and interaction within complex environments.
- **p. 6 / Model - extractive body cue:** As a result, reported scores represent a conservative estimate of each model's spatial understanding.
- **p. 6 / Model - extractive body cue:** Bolded number is the best result for the column. ordinate predictions, we evaluate whether the model's predicted 3D location lies within the convex hull of ...
- **Detected method headings:** 3. Approach (p. 4); Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To ensure that models learn from visual grounding rather than linguistic priors, we use deterministic templates that avoid ambiguity and minimize reliance ... | p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.2. Dataset Generation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Stage 1: 3D Spatial Relation Extraction The first stage involves extracting spatial relationships between objects or between objects and free space, based ... | p. 4 (3.2. Dataset Generation), p. 5 (3.2.3. Question-Answer Generation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | This supervision helps models more accurately resolve references during spatial reasoning and is included during training. | p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.1. Spatial Relationships) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Dataset Generation - extractive body cue:** For each spatial configuration task, we evaluate all visible object pairs that appear uniquely in the image, avoiding duplicate instances to minimize ambiguity.
- **p. 5 / 3.2. Dataset Generation - extractive body cue:** The final answer is a list of 2D (x, y) image coordinates that satisfy the spatial context constraint.
- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** To ensure that models learn from visual grounding rather than linguistic priors, we use deterministic templates that avoid ambiguity and minimize reliance on commonsense.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.2. Dataset Generation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | pipeline, takes, input, scene, dataset, contains, RGB, images, camera, poses, extrinsic, intrinsic, parameters, oriented | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | pipeline, takes, input, scene, dataset, contains, RGB, images, camera, poses | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | output, spatial, reasoning, dataset, where, entry, hIi, consists, image, question | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | spatial, configuration, task, evaluate, visible, object, pairs, appear, uniquely, image | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Dataset Generation - extractive body cue:** The pipeline takes as input a scene dataset Ds that contains RGB images, camera poses (both extrinsic and intrinsic parameters), and oriented 3D bounding box ...
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** The output is a spatial reasoning dataset D, where each entry di = hIi, qi, ai, lii consists of an image Ii, a question qi, ...
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, a critical limitation of existing VLM training datasets is their inability to capture reference frame understanding (ref. frame) - the way we interpret spatial ...
- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** Context questions produce a list of valid 2D coordinates in image space.
- **p. 5 / 3.2. Dataset Generation - extractive body cue:** The final answer is a list of 2D (x, y) image coordinates that satisfy the spatial context constraint.
- **p. 1 / 1. Introduction - extractive body cue:** The rise of vision-language models (VLMs) has opened new opportunities for agents to interpret and act upon the visual world using natural language.
- **p. 6 / Model - extractive body cue:** Results of existing 2D/3D VLMs on a held-out validation split (ROBOSPATIAL-Val) of images and scans.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Is the frame in front of the window? | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Pinpoint several points within the vacant space situated in front of the frame. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.2.3. Question-Answer Generation - extractive body cue:** This supervision helps models more accurately resolve references during spatial reasoning and is included during training.
- **p. 3 / Dataset - extractive body cue:** We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial reasoning, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ensure, models, learn, visual, grounding, rather, linguistic, priors, deterministic, templates, avoid, ambiguity, minimize, reliance, commonsense, Stage, Spatial, Relation, Extraction, first.
- **Relevant PDF headings:** 3. Approach (p. 4); Model (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate ... | p. 3 (Dataset), p. 2 (Dataset) |
| Semantic / temporal fusion | We evaluate the following VLMs: LLaVA-NeXT [35] and RoboPoint [62], both with and without ROBOSPATIAL training; and two strong baselines, Molmo [9] ... | p. 8 (4.3. Real Robot Experiments), p. 3 (Dataset) |
| Robot query / planning handoff | Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, ... | p. 2 (Dataset), p. 8 (4.3. Real Robot Experiments) |

## Failure and Ablation Link

- **p. 5 / 4.1. Setup - extractive body cue:** (See Appendix for ablation experiments.)
- **p. 8 / 4.3. Real Robot Experiments - extractive body cue:** We evaluate the following VLMs: LLaVA-NeXT [35] and RoboPoint [62], both with and without ROBOSPATIAL training; and two strong baselines, Molmo [9] and GPT-4o [42].
- **p. 8 / 4.3. Real Robot Experiments - extractive body cue:** It also demonstrates sensitivity to object scale, as in the task "place in front of the orange juice box," where the model places the object ...
- **p. 2 / Dataset - extractive body cue:** However, these models lack understanding of real-world constraints, such as inferring object-centric reference frames for perspectiveinvariant reasoning, or accounting for the space required to place ...
- **p. 5 / 4.1. Setup - extractive body cue:** We evaluate models in both zero-shot and fine-tuned settings, using ROBOSPATIAL to fine-tune opensource models.
- **p. 7 / 4.1.4. Out-of-Domain Evaluation - extractive body cue:** Two models shown: SL (SpaceLLaVA [5]) and RP (RoboPoint [62]); the -FT suffix indicates fine-tuning on ROBOSPATIAL.
- **p. 3 / Dataset - extractive body cue:** tages for 3D models, differences in pretraining data and base LLM architectures among models render the comparison inconclusive.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.2. Dataset Generation), p. 5 (3.2.3. Question-Answer Generation), p. 4 (3.1. Spatial Relationships), p. 6 (Model), p. 6 (Model), objective p. 4 (3.2. Dataset Generation), p. 5 (3.2. Dataset Generation), p. 5 (3.2.3. Question-Answer Generation), temporal p. 7 (4.1.4. Out-of-Domain Evaluation), p. 7 (4.1.4. Out-of-Domain Evaluation), p. 1 (Abstract), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Dataset), p. 2 (Dataset).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The pipeline takes as input a scene dataset Ds that contains RGB images, camera poses (both extrinsic and intrinsic parameters), and oriented 3D bounding box annotations with semantic object labels. (p. 4, 3.2. Dataset Generation).
- **Objective/update evidence:** The final answer is a list of 2D (x, y) image coordinates that satisfy the spatial context constraint. (p. 5, 3.2. Dataset Generation).
- **Temporal/runtime evidence:** Is the frame in front of the window? (p. 7, 4.1.4. Out-of-Domain Evaluation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
