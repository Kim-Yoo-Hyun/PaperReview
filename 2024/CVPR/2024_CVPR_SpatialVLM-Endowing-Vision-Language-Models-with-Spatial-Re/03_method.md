# Method - SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.12168; PDF retrieval source: https://arxiv.org/pdf/2401.12168. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3. SpatialVLM), p. 2 (1. Introduction), p. 6 (3.3. Learning Spatial Reasoning), p. 5 (3.1. Spatial Grounding from 2D Images), p. 4 (3.1. Spatial Grounding from 2D Images), p. 6 (3.3. Learning Spatial Reasoning)): Concretely, we design a comprehensive data generation framework which first leverages off-the-shelf computer vision models including open-vocabulary detection, metric depth estimation, semantic segmentation and objectcentric captioning ...

## Method Body Digest

- **p. 4 / 3. SpatialVLM - extractive PDF cue:** Concretely, we design a comprehensive data generation framework which first leverages off-the-shelf computer vision models including open-vocabulary detection, metric depth estimation, semantic segmentation and objectcentric ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.
- **p. 6 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** Direct Spatial Reasoning is defined as following, a Vision-Language Model takes as input an image I and a query Q of a spatial task, and ...
- **p. 5 / 3.1. Spatial Grounding from 2D Images - extractive PDF cue:** SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities Object-centric Contexts Extraction from 2D Images In order to extract object-centric spatial contexts from 2D images, we ...
- **p. 4 / 3.1. Spatial Grounding from 2D Images - extractive PDF cue:** Therefore, as the first step in our data synthesis pipeline, we adopt a CLIP-based open-vocabulary classification model to classify all images and rule out those ...
- **p. 6 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** We then train our model using a mixture of the original PaLM-E dataset and our dataset, with 5% of tokens dedicated to spatial reasoning tasks.
- **p. 2 / 1. Introduction - extractive PDF cue:** Vision language models (VLMs) have made significant progress in recent years across a variety of tasks including image captioning, visual question answering (VQA), embodied planning, ...
- **p. 2 / 1. Introduction - extractive PDF cue:** For example, a spatial reasoning-imbued VLM can be used as a better general-purpose reward annotator [54] and success detector [19].

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are: • We endow VLMs quantitative spatial reasoning capability, which is a fundamental capability of humans.
- **p. 4 / 3. SpatialVLM - extractive PDF cue:** To equip VLMs with both qualitatively and quantitatively spatial reasoning capabilities, we propose to generate a large-scale spatial VQA dataset, which is used to train ...

## Source Evidence Cues

- **p. 4 / 3. SpatialVLM - extractive PDF cue:** Concretely, we design a comprehensive data generation framework which first leverages off-the-shelf computer vision models including open-vocabulary detection, metric depth estimation, semantic segmentation and objectcentric ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.
- **p. 6 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** Direct Spatial Reasoning is defined as following, a Vision-Language Model takes as input an image I and a query Q of a spatial task, and ...
- **p. 5 / 3.1. Spatial Grounding from 2D Images - extractive PDF cue:** SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities Object-centric Contexts Extraction from 2D Images In order to extract object-centric spatial contexts from 2D images, we ...
- **p. 4 / 3.1. Spatial Grounding from 2D Images - extractive PDF cue:** Therefore, as the first step in our data synthesis pipeline, we adopt a CLIP-based open-vocabulary classification model to classify all images and rule out those ...
- **p. 6 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** We then train our model using a mixture of the original PaLM-E dataset and our dataset, with 5% of tokens dedicated to spatial reasoning tasks.
- **p. 2 / 1. Introduction - extractive PDF cue:** Vision language models (VLMs) have made significant progress in recent years across a variety of tasks including image captioning, visual question answering (VQA), embodied planning, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Concretely, we design a comprehensive data generation framework which first leverages off-the-shelf computer vision models including open-vocabulary detection, metric depth estimation, semantic ... | p. 4 (3. SpatialVLM), p. 2 (1. Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning ... | p. 2 (1. Introduction), p. 6 (3.3. Learning Spatial Reasoning) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Direct Spatial Reasoning is defined as following, a Vision-Language Model takes as input an image I and a query Q of a ... | p. 6 (3.3. Learning Spatial Reasoning), p. 5 (3.1. Spatial Grounding from 2D Images) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1. Introduction - extractive PDF cue:** For example, a spatial reasoning-imbued VLM can be used as a better general-purpose reward annotator [54] and success detector [19].
- **p. 2 / 1. Introduction - extractive PDF cue:** Such capability not only gives it common sense knowledge about object sizes but also makes it useful as a open-vocabulary reward annotator for rearrangement tasks.
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive PDF cue:** Such visual question-answer pairs can be easily mixed together with other captioning or question answering datasets and use the same training objectives.
- **p. 7 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** In this example, with the help of an LLM orchestrating SpatialVLM, the system is able to answer questions like "Does the blue coke can, the ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.2. Large-Scale Spatial Reasoning VQA Dataset), p. 7 (3.3. Learning Spatial Reasoning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Direct, Spatial, Reasoning, defined, following, Vision-Language, Model, takes, input, image, query, task, output, answer | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Direct, Spatial, Reasoning, defined, following, Vision-Language, Model, takes, input, image | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | system, called, SpatialVLM, enables, data, generation, training, VLMs, enhance, spatial | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | example, spatial, reasoning-imbued, VLM, better, general-purpose, reward, annotator, success, detector | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** Direct Spatial Reasoning is defined as following, a Vision-Language Model takes as input an image I and a query Q of a spatial task, and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Vision language models (VLMs) have made significant progress in recent years across a variety of tasks including image captioning, visual question answering (VQA), embodied planning, ...
- **p. 5 / 3.1. Spatial Grounding from 2D Images - extractive PDF cue:** SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities Object-centric Contexts Extraction from 2D Images In order to extract object-centric spatial contexts from 2D images, we ...
- **p. 6 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive PDF cue:** The answers to the questions are obtained through appropriate functions that we develop, which take as input the segmented point clouds and 3D bounding boxes ...
- **p. 2 / 1. Introduction - extractive PDF cue:** While VLMs are powerful general-purpose models for a wide range of tasks, most state-of-the-art VLMs still struggle with spatial reasoning, i.e. tasks that require understanding ...
- **p. 5 / 3.2. Large-Scale Spatial Reasoning VQA Dataset - extractive PDF cue:** This property allows us to do template-based generation, an approach commonly adopted by instruction tuning works [64].
- **p. 4 / 3. SpatialVLM - extractive PDF cue:** To equip VLMs with both qualitatively and quantitatively spatial reasoning capabilities, we propose to generate a large-scale spatial VQA dataset, which is used to train ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 0 1 2 3 4 5 6 7 Image Index 0.0 0.2 0.4 0.6 Values (m) Distance from grasp Predicted Gripper-Coke Distance ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To study this, we start at the 110k training step and branch into two training runs, one with the ViT frozen, the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose a system called SpatialVLM that enables data generation and training of VLMs to enhance their spatial reasoning capabilities.
- **p. 6 / 3.3. Learning Spatial Reasoning - extractive PDF cue:** We then train our model using a mixture of the original PaLM-E dataset and our dataset, with 5% of tokens dedicated to spatial reasoning tasks.
- **p. 8 / 4. Experiments - extractive PDF cue:** An encoder-decoder VLM trained on multi-lingual corpora, it shows state-of-the-art performance on captioning and visual-question answering tasks.
- **p. 10 / 4.2. Effect of Spatial VQA Data to General VQA - extractive PDF cue:** We train both models for 70k steps, and evaluate percentages of answers from both models that fall into various ranges of the ground truth value ...
- **p. 4 / 3.1. Spatial Grounding from 2D Images - extractive PDF cue:** Semantic Filtering While internet-scale image-captioning datasets have been widely used in VLM training [12], many images in these datasets are not suitable for synthesizing spatial ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Concretely, design, comprehensive, data, generation, framework, first, leverages, off-the-shelf, computer, vision, models, including, open-vocabulary, detection, metric, depth, estimation, semantic, segmentation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | It shows state-of-the-art performance in OKVQA benchmark, as well as being capable of robot planning tasks. | p. 8 (4. Experiments), p. 9 (4.2. Effect of Spatial VQA Data to General VQA) |
| Semantic / temporal fusion | To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained ... | p. 7 (4. Experiments), p. 8 (4. Experiments) |
| Robot query / planning handoff | Our approach SpatialVLM achieves significantly higher success rate than all baselines, achieving inrange results on almost half of the questions. | p. 9 (4.1. Spatial VQA performance), p. 8 (4.1. Spatial VQA performance) |

## Failure and Ablation Link

- **p. 8 / 4. Experiments - extractive PDF cue:** Due to the shared network architecture and training procedure with SpatialVLM, vanilla PaLM 2-E naturally serves as the baseline to study the effect of generated ...
- **p. 10 / 4.2. Effect of Spatial VQA Data to General VQA - extractive PDF cue:** Effect of Visual Transformer (ViT) Encoder in Spatial Reasoning Does a frozen ViT (trained on contrastive objective) encode enough information to perform spatial reasoning?
- **p. 7 / 4. Experiments - extractive PDF cue:** To verify whether VLM's limitation in spatial reasoning is a data problem, we choose the following state-of-the-art VLMs as baselines, all trained on mixtures in ...
- **p. 8 / 4. Experiments - extractive PDF cue:** We used PaLI-X 55B variant in our experiments.
- **p. 9 / 4.2. Effect of Spatial VQA Data to General VQA - extractive PDF cue:** We compared our model with the vanilla PaLM 2-E trained without the spatial VQA dataset on general VQA benchmarks, and as summarized in Table.
- **p. 9 / 4.2. Effect of Spatial VQA Data to General VQA - extractive PDF cue:** This seem to suggest that VLMs are generally underfitting in the distribution of tasks close to spatial reasoning, and can benefit from spatial VQA supervisions ...
- **p. 10 / 4.2. Effect of Spatial VQA Data to General VQA - extractive PDF cue:** A PaLM 2-E model trained with SpatialVLM data improves VQA v2 performance by 2.4% compared to a model with the same number of parameters, but ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3. SpatialVLM), p. 2 (1. Introduction), p. 6 (3.3. Learning Spatial Reasoning), p. 5 (3.1. Spatial Grounding from 2D Images), p. 4 (3.1. Spatial Grounding from 2D Images), p. 6 (3.3. Learning Spatial Reasoning), objective p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.2. Large-Scale Spatial Reasoning VQA Dataset), p. 7 (3.3. Learning Spatial Reasoning), temporal p. 9 (4.1. Spatial VQA performance), p. 10 (4.2. Effect of Spatial VQA Data to General VQA), p. 10 (4.4. Effect of Noisy Quantitative Spatial Answers), p. 11 (4.5. Spatial Reasoning Unlocks Novel Applications), p. 11 (4.5. Spatial Reasoning Unlocks Novel Applications), p. 5 (3.1. Spatial Grounding from 2D Images).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
