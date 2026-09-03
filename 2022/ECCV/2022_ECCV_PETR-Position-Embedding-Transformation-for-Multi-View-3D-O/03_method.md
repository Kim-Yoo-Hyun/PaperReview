# Method - PETR: Position Embedding Transformation for Multi-View 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.05625; PDF retrieval source: https://arxiv.org/pdf/2203.05625. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method)): Object queries, generated from query generator, are updated through the interaction with 3D position-aware features in transformer decoder.

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** Object queries, generated from query generator, are updated through the interaction with 3D position-aware features in transformer decoder.
- **p. 7 / 3 Method - extractive body cue:** In each decoder layer, object queries interact with 3D position-aware features through the multi-head attention and feed-forward network.
- **p. 5 / 3 Method - extractive body cue:** Then 2D image features and 3D coordinates are injected to proposed 3D position encoder to generate the 3D position-aware features.
- **p. 6 / 3 Method - extractive body cue:** Given the 2D features F 2d and 3D coordinates P 3d, the P 3d is first feed into a multi-layer perception (MLP) network and transformed ...
- **p. 6 / 3 Method - extractive body cue:** Finally, we flatten the 3D position-aware features as the key component of transformer decoder.
- **p. 7 / 3 Method - extractive body cue:** Decoder: For the decoder network, we follow the standard transformer decoder in DETR [4], which includes L decoder layers.
- **p. 8 / 3 Method - extractive body cue:** Suppose that σ is the optimal assignment function, then the loss for 3D object detection can be summarized as: \la bel {eq5 } \begin {alig ...
- **p. 7 / 3 Method - extractive body cue:** 3.5 Head and Loss The detection head mainly includes two branches for classification and regression.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To summarize, our contributions are: - We propose a simple and elegant framework, termed PETR, for multi-view 3D object detection.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, DETR [4] has gained remarkable attention due to its contribution on end-to-end object detection.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a simple and elegant framework based on DETR [4] for 3D object detection.

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** Object queries, generated from query generator, are updated through the interaction with 3D position-aware features in transformer decoder.
- **p. 7 / 3 Method - extractive body cue:** In each decoder layer, object queries interact with 3D position-aware features through the multi-head attention and feed-forward network.
- **p. 5 / 3 Method - extractive body cue:** Then 2D image features and 3D coordinates are injected to proposed 3D position encoder to generate the 3D position-aware features.
- **p. 6 / 3 Method - extractive body cue:** Given the 2D features F 2d and 3D coordinates P 3d, the P 3d is first feed into a multi-layer perception (MLP) network and transformed ...
- **p. 6 / 3 Method - extractive body cue:** Finally, we flatten the 3D position-aware features as the key component of transformer decoder.
- **p. 7 / 3 Method - extractive body cue:** Decoder: For the decoder network, we follow the standard transformer decoder in DETR [4], which includes L decoder layers.
- **p. 8 / 3 Method - extractive body cue:** Suppose that σ is the optimal assignment function, then the loss for 3D object detection can be summarized as: \la bel {eq5 } \begin {alig ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Object queries, generated from query generator, are updated through the interaction with 3D position-aware features in transformer decoder. | p. 5 (3 Method), p. 7 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In each decoder layer, object queries interact with 3D position-aware features through the multi-head attention and feed-forward network. | p. 7 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then 2D image features and 3D coordinates are injected to proposed 3D position encoder to generate the 3D position-aware features. | p. 5 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** 3.5 Head and Loss The detection head mainly includes two branches for classification and regression.
- **p. 8 / 3 Method - extractive body cue:** 8 Liu et al. adopt the focal loss [25] for classification and L1 loss for 3D bounding box regression.
- **p. 8 / 3 Method - extractive body cue:** Suppose that σ is the optimal assignment function, then the loss for 3D object detection can be summarized as: \la bel {eq5 } \begin {alig ...
- **p. 7 / 3 Method - extractive body cue:** The updated object queries from the decoder are input to the detection head and predict the probability of object classes as well as the 3D ...
- **p. 5 / 3 Method - extractive body cue:** Object queries, generated from query generator, are updated through the interaction with 3D position-aware features in transformer decoder.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, images, views, input, backbone, network, multi-view, image, features, convolution, layer, dimension, reduction, Then | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, images, views, input, backbone, network, multi-view, image, features, convolution | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, simple, elegant, framework, termed, PETR, multi-view, object, detection | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Head, Loss, detection, mainly, includes, branches, classification, regression, Liu, adopt | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Method - extractive body cue:** Given the images I = {Ii ∈R3×HI×WI, i = 1, 2, . . . , N} from N views, the images are input to the ...
- **p. 5 / 3 Method - extractive body cue:** The multi-view images are input to the backbone network (e.g.
- **p. 6 / 3 Method - extractive body cue:** The multi-view 2D image features are input to a 1 × 1 convolution layer for dimension reduction.
- **p. 2 / 1 Introduction - extractive body cue:** Then 2D image features extracted from backbone and 3D coordinates are input to a simple 3D position encoder to produce the 3D position-aware features.
- **p. 4 / 3 Method - extractive body cue:** The 3D features are further input to the transformer decoder and interact with the object queries, generated from query generator.
- **p. 6 / 3 Method - extractive body cue:** Finally, the 3D position-aware features are flattened and serve as the input of the transformer decoder.
- **p. 7 / 3 Method - extractive body cue:** Then the coordinates of 3D anchor points are input to a small MLP network with two linear layers and generate the initial object queries Q0.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Thus, building an end-to-end 3D object detection framework without the online 2D-to-3D transformation and feature sampling is still a remaining problem. ⋆ | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Each scene has 20s video frames and is fully annotated with 3D bounding boxes every 0.5s. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each scene has 20s video frames and is fully annotated with 3D bounding boxes every 0.5s. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4 Experiments - extractive body cue:** All experiments are trained for 24 epochs (2x schedule) on 8 Tesla V100 GPUs with a batch size of 8.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Object, queries, generated, query, generator, updated, through, interaction, position-aware, features, transformer, decoder, layer, interact, multi-head, attention, feed-forward, network, Then, image.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1 Datasets and Metrics We validate our method on nuScenes benchmark [3]. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Semantic / temporal fusion | It achieves state-of-the-art performance and can serve as a strong baseline for future research. | p. 14 (4 Experiments), p. 12 (4 Experiments) |
| Robot query / planning handoff | Our method also achieves the best performance on both NDS and mAP. | p. 9 (4 Experiments), p. 9 (4 Experiments) |

## Failure and Ablation Link

- **p. 11 / 4 Experiments - extractive body cue:** Depth Range (xmin, ymin, zmin, xmax, ymax, zmax) UD LID NDS↑mAP↑mATE↓ (1,51.2) (-51.2, -51.2, -10.0, 51.2, 51.2, 10.0) ✓ 0.352 0.303 0.862 (1,51.2) (-51.2, -51.2, ...
- **p. 12 / 4 Experiments - extractive body cue:** 5(c) shows the effect of different anchor points to generate queries.
- **p. 12 / 4 Experiments - extractive body cue:** Here we first explore the effect of the multi-layer perception (MLP) that converts the 3D coordinates into 3D position embedding.
- **p. 11 / 4 Experiments - extractive body cue:** All the experiments are conducted using single-level C5 feature of ResNet-50 backbone without the CBGS [57].
- **p. 9 / 4 Experiments - extractive body cue:** The results of FCOS3D and PGD are fine-tuned and tested with test time augmentation.
- **p. 14 / 4 Experiments - extractive body cue:** Finally, we provide some failure cases (see Fig.
- **p. 14 / 4 Experiments - extractive body cue:** We mark the failure cases by red and green circles.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), objective p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 7 (3 Method), p. 5 (3 Method), temporal p. 1 (1 Introduction), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 1 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
