# Method - Grounded 3D-Aware Spatial Vision-Language Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2.2. Grounding in the 2D Plane), p. 4 (2.2.2. Implicit 2D Grounding), p. 4 (2.2.2. Implicit 2D Grounding), p. 5 (2.4. Data Construction and Composition), p. 3 (2.1. Foundational Spatial VLM), p. 5 (Method)): We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.

## Method Body Digest

- **p. 3 / 2.2. Grounding in the 2D Plane - extractive PDF cue:** We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** The model first predicts coordinates, then encodes the predicted region to obtain its embedding, which is inserted back into the ongoing sequence before the next ...
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** Our stream-based grounding can be viewed abstractly as analogous to a twostep process, i.e., first grounding entities with a VLM, and then performing region-conditioned reasoning ...
- **p. 5 / 2.4. Data Construction and Composition - extractive PDF cue:** Our training data is composed of publicly available sources: 97K grounded CoT samples, 780K 3D detection samples from Omni3D [32] and EmbodiedScan [56], and 272K ...
- **p. 3 / 2.1. Foundational Spatial VLM - extractive PDF cue:** Overall, the single-view formulation provides a strong spatially-structured feature space for both regionlevel interaction and text-aligned representation.
- **p. 5 / Method - extractive PDF cue:** Together, region-prompt grounding, structured 3D box representation, intrinsic normalization, and scalable training signals address both linguistic and geometric ambiguities of monocular 3D grounding.
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** This token is detached from the computation graph (i.e., no gradient flows through it) but serves as a strong conditional cue for subsequent token prediction.
- **p. 4 / 2.3. Monocular 3D Grounding via Region Prompt - extractive PDF cue:** To ensure consistency across datasets, we standardize orientations by selecting the rotation variant that minimizes the angular deviation between the local PCA axes of the ...

## Design Rationale

- **p. 3 / 2.2. Grounding in the 2D Plane - extractive PDF cue:** We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these limitations, we introduce (GR3D), a spatial VLM that integrates grounding as a core mechanism for learning spatial representations.
- **p. 3 / 2. Method - extractive PDF cue:** Building on this foundation, we introduce explicit and implicit 2D grounding (Sec.

## Source Evidence Cues

- **p. 3 / 2.2. Grounding in the 2D Plane - extractive PDF cue:** We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model.
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** The model first predicts coordinates, then encodes the predicted region to obtain its embedding, which is inserted back into the ongoing sequence before the next ...
- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** Our stream-based grounding can be viewed abstractly as analogous to a twostep process, i.e., first grounding entities with a VLM, and then performing region-conditioned reasoning ...
- **p. 5 / 2.4. Data Construction and Composition - extractive PDF cue:** Our training data is composed of publicly available sources: 97K grounded CoT samples, 780K 3D detection samples from Omni3D [32] and EmbodiedScan [56], and 272K ...
- **p. 3 / 2.1. Foundational Spatial VLM - extractive PDF cue:** Overall, the single-view formulation provides a strong spatially-structured feature space for both regionlevel interaction and text-aligned representation.
- **p. 5 / Method - extractive PDF cue:** Together, region-prompt grounding, structured 3D box representation, intrinsic normalization, and scalable training signals address both linguistic and geometric ambiguities of monocular 3D grounding.
- **Detected method headings:** 2. Method (p. 3); Method (p. 5); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model. | p. 3 (2.2. Grounding in the 2D Plane), p. 4 (2.2.2. Implicit 2D Grounding) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The model first predicts coordinates, then encodes the predicted region to obtain its embedding, which is inserted back into the ongoing sequence ... | p. 4 (2.2.2. Implicit 2D Grounding), p. 4 (2.2.2. Implicit 2D Grounding) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our stream-based grounding can be viewed abstractly as analogous to a twostep process, i.e., first grounding entities with a VLM, and then ... | p. 4 (2.2.2. Implicit 2D Grounding), p. 5 (2.4. Data Construction and Composition) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** This token is detached from the computation graph (i.e., no gradient flows through it) but serves as a strong conditional cue for subsequent token prediction.
- **p. 4 / 2.3. Monocular 3D Grounding via Region Prompt - extractive PDF cue:** To ensure consistency across datasets, we standardize orientations by selecting the rotation variant that minimizes the angular deviation between the local PCA axes of the ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (2.2.2. Implicit 2D Grounding).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, input, instruction, model, generates, response, chain-ofthought, CoT, fashion, framework, naturally, extends, single-view, multi-view | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, input, instruction, model, generates, response, chain-ofthought, CoT, fashion, framework | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | introduce, explicit, implicit, forms, grounding, designed, strengthen, spatial, reasoning, capacity | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | token, detached, computation, graph, gradient, flows, through, serves, strong, conditional | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2.2.2. Implicit 2D Grounding - extractive PDF cue:** Given an input instruction, the model generates its response in a chain-ofthought (CoT) fashion.
- **p. 3 / 2.1. Foundational Spatial VLM - extractive PDF cue:** Our framework naturally extends from single-view to multi-view inputs by embedding all image tokens with depth- and pixel-based positional cues in a unified spatial feature ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Without reliable spatial grounding, the link between high-level instructions and physical interaction remains brittle, limiting the scalability of VLMs toward real-world embodied perception and control.
- **p. 2 / 1. Introduction - extractive PDF cue:** Vision-language models (VLMs) have rapidly evolved into general-purpose perception-language systems [1-8], capable of understanding scenes, following open-ended instructions, and supporting diverse multimodal tasks.
- **p. 3 / 2.1. Foundational Spatial VLM - extractive PDF cue:** The base NVILA encoder extracts dense visual tokens from an RGB image for single-view inputs.
- **p. 4 / 2.3. Monocular 3D Grounding via Region Prompt - extractive PDF cue:** Each 3D bounding box is expressed in a unified, language-based format compatible with 2D HTML-style outputs, eliminating the need for task-specific heads.
- **p. 5 / 2.4. Data Construction and Composition - extractive PDF cue:** To construct the implicit grounding corpus, we start from RefSpatial [23], which includes 2D samples from OpenImages [53], 3D video data from CA-1M [54], and ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The model first predicts coordinates, then encodes the predicted region to obtain its embedding, which is inserted back into the ongoing sequence ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The first view is processed exactly as in the single-view case, and all subsequent views are transformed into the first-frame coordinate system. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2.4. Data Construction and Composition - extractive PDF cue:** Our training data is composed of publicly available sources: 97K grounded CoT samples, 780K 3D detection samples from Omni3D [32] and EmbodiedScan [56], and 272K ...
- **p. 5 / Method - extractive PDF cue:** Together, region-prompt grounding, structured 3D box representation, intrinsic normalization, and scalable training signals address both linguistic and geometric ambiguities of monocular 3D grounding.
- **p. 6 / 3.1. Implementation Details - extractive PDF cue:** During this stage, we freeze the visual encoder and train the remaining modules.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, explicit, implicit, forms, grounding, designed, strengthen, spatial, reasoning, capacity, vision-language, model, first, predicts, coordinates, then, encodes, predicted, region, obtain.
- **Relevant PDF headings:** 2. Method (p. 3); Method (p. 5); Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The Omni3D dataset is highly imbalanced [44], with far fewer outdoor training samples compared to indoor scenes. | p. 7 (3.5. Analysis and Ablation Study), p. 6 (3.2. 3D Object Detection) |
| Semantic / temporal fusion | 4, where our model outperforms all VLM baselines. | p. 6 (3.2. 3D Object Detection), p. 6 (3.2. 3D Object Detection) |
| Robot query / planning handoff | Compared with vision specialists, our model achieves competitive results overall and delivers notably better performance on indoor datasets. | p. 6 (3.2. 3D Object Detection), p. 6 (3.3. Visual Question Answering) |

## Failure and Ablation Link

- **p. 8 / 3.5. Analysis and Ablation Study - extractive PDF cue:** Ablation study on the key components of GR3D-8B. "PT" denotes pretraining, "2D→3D" denotes 2D grounding followed by 3D prediction, and "Cam" denotes using normalized intrinsics. ...
- **p. 7 / 3.5. Analysis and Ablation Study - extractive PDF cue:** We further analyze the effect of pointmap reconstruction as an auxiliary task for 3D detection.
- **p. 6 / 3. Experiments - extractive PDF cue:** 3.5 provides additional analysis and ablation studies of the model's 3D detection performance.
- **p. 6 / 3.3. Visual Question Answering - extractive PDF cue:** We evaluate two variants of our model: one after spatial pre-training and one after CoT finetuning.
- **p. 7 / 3.5. Analysis and Ablation Study - extractive PDF cue:** Without this normalization, the model may lead to small but noticeable localization offsets in the predicted 3D boxes.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Results on the BLINK-Depth benchmark for point-level region spatial understanding. Left: comparison with VLM base- lines. Right: visualization of one sample. Our method ...
- **p. 6 / 3.2. 3D Object Detection - extractive PDF cue:** This makes its 3D predictions unstable under changes in image size.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2.2. Grounding in the 2D Plane), p. 4 (2.2.2. Implicit 2D Grounding), p. 4 (2.2.2. Implicit 2D Grounding), p. 5 (2.4. Data Construction and Composition), p. 3 (2.1. Foundational Spatial VLM), p. 5 (Method), objective p. 4 (2.2.2. Implicit 2D Grounding), p. 4 (2.3. Monocular 3D Grounding via Region Prompt), temporal p. 4 (2.2.2. Implicit 2D Grounding), p. 3 (2.1. Foundational Spatial VLM), p. 3 (2.1. Foundational Spatial VLM), p. 4 (2.3. Monocular 3D Grounding via Region Prompt), p. 6 (3.2. 3D Object Detection), p. 7 (3.5. Analysis and Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
