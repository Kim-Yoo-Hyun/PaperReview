# Method - 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05642.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method)): In order to improve the open vocabulary capability of our model, we propose significant changes to the P3Former architecture, as well as two new loss functions.

## Method Body Digest

- **p. 5 / 3 Method - extractive PDF cue:** In order to improve the open vocabulary capability of our model, we propose significant changes to the P3Former architecture, as well as two new loss ...
- **p. 7 / 3 Method - extractive PDF cue:** We propose an additional training loss which forces our predicted object-level class embeddings to be similar to the CLIP embeddings within their corresponding masks after ...
- **p. 4 / 3 Method - extractive PDF cue:** Then we provide detailed descriptions of the model architecture as well as the proposed loss functions.
- **p. 5 / 3 Method - extractive PDF cue:** However, we found that this simple extension leads to poor performance in our experiments, and in this work we propose several new features to improve ...
- **p. 7 / 3 Method - extractive PDF cue:** Besides the two standard loss functions, we propose two simple yet effective losses to apply distillation from the CLIP model at different levels.
- **p. 8 / 3 Method - extractive PDF cue:** For the Text CLIP encoder, we use CLIP [39] with ViT-L/14 [45] backbone, following other state-of-the-art open vocabulary works [35].
- **p. 8 / 3 Method - extractive PDF cue:** To target these issues, we propose the voxel-level distillation loss to explicitly learn voxel-level CLIP features, which do not depend on any labels and can ...
- **p. 7 / 3 Method - extractive PDF cue:** 3.3 Loss Function Closed-set panoptic segmentation models [47] are typically optimized with objective functions consisting of a classification loss Lcls and a mask prediction loss ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: - We present the first approach for 3D open-vocabulary panoptic segmentation in autonomous driving. - We propose two novel ...
- **p. 6 / 3 Method - extractive PDF cue:** To take advantage of the benefits of separating things queries and stuff queries, we propose to predict the base stuff classes with a fixed set ...
- **p. 8 / 3 Method - extractive PDF cue:** Combining LO with LV enables segmenting novel things and novel stuff objects simultaneously.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive PDF cue:** In order to improve the open vocabulary capability of our model, we propose significant changes to the P3Former architecture, as well as two new loss ...
- **p. 7 / 3 Method - extractive PDF cue:** We propose an additional training loss which forces our predicted object-level class embeddings to be similar to the CLIP embeddings within their corresponding masks after ...
- **p. 4 / 3 Method - extractive PDF cue:** Then we provide detailed descriptions of the model architecture as well as the proposed loss functions.
- **p. 5 / 3 Method - extractive PDF cue:** However, we found that this simple extension leads to poor performance in our experiments, and in this work we propose several new features to improve ...
- **p. 7 / 3 Method - extractive PDF cue:** Besides the two standard loss functions, we propose two simple yet effective losses to apply distillation from the CLIP model at different levels.
- **p. 8 / 3 Method - extractive PDF cue:** For the Text CLIP encoder, we use CLIP [39] with ViT-L/14 [45] backbone, following other state-of-the-art open vocabulary works [35].
- **p. 8 / 3 Method - extractive PDF cue:** To target these issues, we propose the voxel-level distillation loss to explicitly learn voxel-level CLIP features, which do not depend on any labels and can ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In order to improve the open vocabulary capability of our model, we propose significant changes to the P3Former architecture, as well as ... | p. 5 (3 Method), p. 7 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We propose an additional training loss which forces our predicted object-level class embeddings to be similar to the CLIP embeddings within their ... | p. 7 (3 Method), p. 4 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then we provide detailed descriptions of the model architecture as well as the proposed loss functions. | p. 4 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive PDF cue:** 3.3 Loss Function Closed-set panoptic segmentation models [47] are typically optimized with objective functions consisting of a classification loss Lcls and a mask prediction loss ...
- **p. 7 / 3 Method - extractive PDF cue:** We follow P3Former [47] for these two losses: the classification loss Lcls optimizes the focal loss [30] between the class predictions and the category labels, ...
- **p. 4 / 3 Method - extractive PDF cue:** 1, and the two proposed loss functions are illustrated in Fig.
- **p. 5 / 3 Method - extractive PDF cue:** In order to improve the open vocabulary capability of our model, we propose significant changes to the P3Former architecture, as well as two new loss ...
- **p. 8 / 3 Method - extractive PDF cue:** However, this loss is still susceptible to noisy or low quality mask scores, and we found that larger weights for this loss can disrupt training.
- **p. 8 / 3 Method - extractive PDF cue:** To target these issues, we propose the voxel-level distillation loss to explicitly learn voxel-level CLIP features, which do not depend on any labels and can ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | LiDAR, encoder, model, takes, unordered, points, input, extracts, per-point, features, mainly, consists, multimodal, feature | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | LiDAR, encoder, model, takes, unordered, points, input, extracts, per-point, features | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, present, first, open-vocabulary, panoptic, segmentation, autonomous, driving | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Loss, Function, Closed-set, panoptic, segmentation, models, typically, optimized, objective, functions | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive PDF cue:** The LiDAR encoder is a model which takes an unordered set of points as input and extracts per-point features.
- **p. 5 / 3 Method - extractive PDF cue:** 1 and mainly consists of multimodal feature fusion, a segmentation head, and input text embeddings for open-vocabulary classification.
- **p. 6 / 3 Method - extractive PDF cue:** The segmentation head is a transformer [45] model that takes the LiDAR-Vision fused feature as input to produce panoptic segmentation results.
- **p. 6 / 3 Method - extractive PDF cue:** Finally, the learned per-voxel LiDAR features and frozen per-voxel vision CLIP features are concatenated together to be used as input into the transformer decoder in ...
- **p. 8 / 3 Method - extractive PDF cue:** For the Text CLIP encoder, we use CLIP [39] with ViT-L/14 [45] backbone, following other state-of-the-art open vocabulary works [35].
- **p. 8 / 3 Method - extractive PDF cue:** 3.4 Implementation Details For the LiDAR encoder and segmentation head, we follow the implementation of the state-of-the-art closed-set 3D panoptic segmentation method P3Former [47].
- **p. 4 / 3 Method - extractive PDF cue:** 3.1 Problem Definition In 3D panoptic segmentation, the goal is to annotate every point in a point cloud.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We set the initial learning rate as 0.0008 with a multi-step decay schedule. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We use all key frames with panoptic labels in the training set(28130 frames) to train the model. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We use all key frames with panoptic labels in the training set(28130 frames) to train the model. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3 Method - extractive PDF cue:** We propose an additional training loss which forces our predicted object-level class embeddings to be similar to the CLIP embeddings within their corresponding masks after ...
- **p. 9 / 4 Experiments - extractive PDF cue:** The models are trained for 40 epochs, and we use the checkpoint of the last epoch for evaluation.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** order, improve, open, vocabulary, capability, model, significant, changes, P3Former, architecture, well, loss, functions, additional, training, forces, predicted, object-level, class, embeddings.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The nuScenes dataset [4] is a public benchmark for autonomous driving. | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | 4.3 Main Results Since there are no existing methods for the 3D open-vocabulary panoptic segmentation task, we mainly compare with three methods ... | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Robot query / planning handoff | Our method significantly outperforms | p. 10 (4 Experiments), p. 11 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive PDF cue:** We use the same splits in the main comparison with prior methods, and provide the results of more variations in the ablation studies and supplementary ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 4.1 Experimental Setting Following the state-of-the-art closed-set 3D panoptic segmentation work [27,40, 42,47,52,58], we conduct experiments and ablation studies on the nuScenes [4] and SemanticKITTI ...
- **p. 10 / 4 Experiments - extractive PDF cue:** In summary, this baseline provides a comparison against our proposed method without the multimodal feature fusion module, the unified segmentation head, and the distillation losses.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Impact of each component. We evaluate the impact of each component using the base/novel split in Tab. 1. We observe that each component ...
- **p. 14 / 5 Conclusion - extractive PDF cue:** We experimentally verified that simply extending the 2D open-vocabulary segmentation method into 3D does not yield good performance, and demonstrated that our proposed model design ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), objective p. 7 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 8 (3 Method), p. 8 (3 Method), temporal p. 9 (4 Experiments), p. 9 (4 Experiments), p. 3 (2 Related Work), p. 3 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
