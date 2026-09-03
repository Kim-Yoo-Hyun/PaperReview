# Method - SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology), p. 3 (3.1. Multimodal 3D Representation), p. 6 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation)): To address this, we introduce the Fusion Alignment Module, which explicitly associates key visual features in the scene with the textual description, ensuring a clear correspondence between the 2D rendered ...

## Method Body Digest

- **p. 5 / 3.3. Fusion Alignment Module - extractive body cue:** To address this, we introduce the Fusion Alignment Module, which explicitly associates key visual features in the scene with the textual description, ensuring a clear ...
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** Finally, the 2D-VLM outputs the target object's ID, which is then used to retrieve its 3D bounding box from the OLT , providing the final, ...
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.
- **p. 3 / 3.1. Multimodal 3D Representation - extractive body cue:** To tackle this problem, in this work, we propose a hybrid representation that combines "2D rendered images" and "text-based 3D spatial descriptions".
- **p. 6 / 3.3. Fusion Alignment Module - extractive body cue:** (7) By aligning the visual features in the image with the spatial information in the text, the proposed Fusion Alignment Module effectively reduces ambiguity and ...
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** The rendered images offer a 2D perspective of the 3D scene, allowing the model to capture visual features such as color, shape, texture, and relative ...
- **p. 5 / 3.2. Perspective Adaptation Module - extractive body cue:** 3 (e), filtering out irrelevant information enhances localization accuracy by reducing interpretive confusion within the model.
- **p. 2 / 1. Introduction - extractive body cue:** ies [55, 60] attempt to reduce 3D-specific training requirements by reformatting 3D scenes and text descriptions for large language models (LLMs) [38, 39], but these ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce SeeGround, a training-free solution for zero-shot 3DVG.
- **p. 2 / 1. Introduction - extractive body cue:** Considering that 2D-VLMs cannot process 3D data directly, we introduce a cross-modal alignment representation that enables 2D-VLMs to interpret 3D scenes.
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.

## Source Evidence Cues

- **p. 5 / 3.3. Fusion Alignment Module - extractive body cue:** To address this, we introduce the Fusion Alignment Module, which explicitly associates key visual features in the scene with the textual description, ensuring a clear ...
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** Finally, the 2D-VLM outputs the target object's ID, which is then used to retrieve its 3D bounding box from the OLT , providing the final, ...
- **p. 3 / 3. Methodology - extractive body cue:** (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations.
- **p. 3 / 3.1. Multimodal 3D Representation - extractive body cue:** To tackle this problem, in this work, we propose a hybrid representation that combines "2D rendered images" and "text-based 3D spatial descriptions".
- **p. 6 / 3.3. Fusion Alignment Module - extractive body cue:** (7) By aligning the visual features in the image with the spatial information in the text, the proposed Fusion Alignment Module effectively reduces ambiguity and ...
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** The rendered images offer a 2D perspective of the 3D scene, allowing the model to capture visual features such as color, shape, texture, and relative ...
- **p. 5 / 3.2. Perspective Adaptation Module - extractive body cue:** 3 (e), filtering out irrelevant information enhances localization accuracy by reducing interpretive confusion within the model.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address this, we introduce the Fusion Alignment Module, which explicitly associates key visual features in the scene with the textual description, ... | p. 5 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Finally, the 2D-VLM outputs the target object's ID, which is then used to retrieve its 3D bounding box from the OLT , ... | p. 4 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | (1) In this work, we propose a novel method for 3DVG that integrates 2D-VLM with spatially enriched 3D scene representations. | p. 3 (3. Methodology), p. 3 (3.1. Multimodal 3D Representation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | attempt, reduce, D-specific, training, requirements, reformatting, scenes, text, descriptions, large, language, models, LLMs, methods | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | attempt, reduce, D-specific, training, requirements, reformatting, scenes, text, descriptions, large | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, follows, introduce, SeeGround, training-free, solution, zero-shot, DVG, Considering, D-VLMs | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** ies [55, 60] attempt to reduce 3D-specific training requirements by reformatting 3D scenes and text descriptions for large language models (LLMs) [38, 39], but these ...
- **p. 3 / 3.1. Multimodal 3D Representation - extractive body cue:** However, prior 3D scene representations - such as point clouds [14, 40], voxels [29], and implicit representations [22] - are not directly compatible with the ...
- **p. 3 / 3. Methodology - extractive body cue:** The goal is to output a directed 3D bounding box (bbox) of object o that identifies the target object's location and dimensions.
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** The image with prompts, along with the spatial descriptions and query, is then input into the 2D-VLM for precise localization of the target object.
- **p. 4 / 3.1. Multimodal 3D Representation - extractive body cue:** Formally, the 3D scene is represented as: (I, T ) = F (S, Q, OLT ) , (3) where F takes the 3D scene S, ...
- **p. 5 / 3.3. Fusion Alignment Module - extractive body cue:** Although the 2D rendered images and text-based spatial descriptions provide substantial spatial information for SeeGround, directly inputting text and images without explicit (a) Bird's Eye ...
- **p. 2 / 1. Introduction - extractive body cue:** The images are rendered using query-driven dynamic viewpoints, simulating relevant observation angles, and capturing object details and spatial context.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The overall framework is illustrated in Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This representation allows our framework to align the rich visual features from 2D renderings with the spatial context from 3D scene descriptions. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, introduce, Fusion, Alignment, Module, explicitly, associates, visual, features, scene, textual, description, ensuring, clear, correspondence, between, rendered, image, text-based, spatial.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We use two popular benchmark datasets to evaluate our 3DVG approach. | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Semantic / temporal fusion | 1 compares methods on the ScanRefer dataset. our method outperforms other zero-shot methods [55, 60] and the weakly supervised WS-3DVG [50], achieving ... | p. 6 (4.2. Comparative Study), p. 7 (4.2. Comparative Study) |
| Robot query / planning handoff | Our method achieves 46.1% accuracy on Nr3D, which is a 18.2% improvement over the previous zero-shot baseline, ZSVG3D [60] (39.0%). | p. 7 (4.2. Comparative Study), p. 7 (4.2. Comparative Study) |

## Failure and Ablation Link

- **p. 7 / 4.2. Comparative Study - extractive body cue:** Ablation study on different components in our framework on Nr3D [1]. "3D Pos.": 3D object coordinates; "Layout": Scene layout; "Texture": Object color/texture; "FAM": Fusion Alignment ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Ablation studies are conducted on the Nr3D validation set [1].
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Ablation study on using (a) different projection methods (ours vs.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** In contrast, LLM performance degrades without the anchor.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. An example of the robustness of the proposed frame- work in identifying the ‘cabinet' by leveraging visual context, even when key information (‘printers' ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** ZSVG3D [60] projects object centers onto a 2D image and uses predefined functions to infer spatial relations, but this approach lacks flexibility, omits visual cues, ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Bird's Eye View, though comprehensive, cannot adjust to the query and misses key spatial details like object orientation and height.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation), p. 3 (3. Methodology), p. 3 (3.1. Multimodal 3D Representation), p. 6 (3.3. Fusion Alignment Module), p. 4 (3.1. Multimodal 3D Representation), objective 본문 anchor 없음, temporal p. 3 (3. Methodology), p. 3 (3. Methodology), p. 4 (3.1. Multimodal 3D Representation), p. 5 (3.2. Perspective Adaptation Module), p. 7 (4.3. Ablation Study), p. 7 (4.2. Comparative Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
