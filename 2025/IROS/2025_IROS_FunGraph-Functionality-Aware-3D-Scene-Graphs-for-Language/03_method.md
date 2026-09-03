# Method - FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.07909; PDF retrieval source: https://arxiv.org/pdf/2503.07909. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD)): The process consists of three phases: • Detection: Instance segmentation of entities captured in the images and feature extraction. • Node creation: Multi-view geometric and semantic feature merging. • Edge ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** The process consists of three phases: • Detection: Instance segmentation of entities captured in the images and feature extraction. • Node creation: Multi-view geometric and ...
- **p. 3 / III. METHOD - extractive body cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 5 / III. METHOD - extractive body cue:** As a general-purpose semantic segmentation model we use SAM2 [14], and as VLM GPT-4o [43].
- **p. 4 / III. METHOD - extractive body cue:** After each successful merge, the point cloud of node n is denoised using DBSCAN and downsampled to reduce redundancy, and then the semantic features are ...
- **p. 4 / III. METHOD - extractive body cue:** Each object is associated with a label c[i] j and semantic features f [i] j extracted using the CLIP model from the bounding-box cropped image.
- **p. 2 / III. METHOD - extractive body cue:** For example, we want a cabinet to have a direct relationship with its knobs, enhancing the scene graph with information about the object's possible interactions.
- **p. 3 / III. METHOD - extractive body cue:** Because cm-resolution LiDARs are not detailed enough and mm-resolution 3D scanners are cost-prohibitive in many robotic applications, we assume a collection of registered RGB-D observations ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One use of this representation is affordance grounding, in which unconstrained language queries produce the relation to the functional elements required to fulfill a task ...

## Design Rationale

- **p. 3 / III. METHOD - extractive body cue:** 3 provides an overview of our method.
- **p. 3 / III. METHOD - extractive body cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 4 / III. METHOD - extractive body cue:** Overview of our functionality-aware 3D scene graph generation pipeline, which consists of three stages: (1) Detection, where instance segmentation and feature extraction are performed to ...

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** The process consists of three phases: • Detection: Instance segmentation of entities captured in the images and feature extraction. • Node creation: Multi-view geometric and ...
- **p. 3 / III. METHOD - extractive body cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 5 / III. METHOD - extractive body cue:** As a general-purpose semantic segmentation model we use SAM2 [14], and as VLM GPT-4o [43].
- **p. 4 / III. METHOD - extractive body cue:** After each successful merge, the point cloud of node n is denoised using DBSCAN and downsampled to reduce redundancy, and then the semantic features are ...
- **p. 4 / III. METHOD - extractive body cue:** Each object is associated with a label c[i] j and semantic features f [i] j extracted using the CLIP model from the bounding-box cropped image.
- **p. 2 / III. METHOD - extractive body cue:** For example, we want a cabinet to have a direct relationship with its knobs, enhancing the scene graph with information about the object's possible interactions.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The process consists of three phases: • Detection: Instance segmentation of entities captured in the images and feature extraction. • Node creation: ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, ... | p. 3 (III. METHOD), p. 5 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | As a general-purpose semantic segmentation model we use SAM2 [14], and as VLM GPT-4o [43]. | p. 5 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** Because cm-resolution LiDARs are not detailed enough and mm-resolution 3D scanners are cost-prohibitive in many robotic applications, we assume a collection of registered RGB-D observations ...
- **p. 4 / III. METHOD - extractive body cue:** After each successful merge, the point cloud of node n is denoised using DBSCAN and downsampled to reduce redundancy, and then the semantic features are ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, consists, series, RGB-D, observations, corresponding, camera, poses, Because, cm-resolution, LiDARs, detailed, enough, mm-resolution | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | input, consists, series, RGB-D, observations, corresponding, camera, poses, Because, cm-resolution | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | provides, overview, input, consists, series, RGB-D, observations, corresponding, camera, poses | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Because, cm-resolution, LiDARs, detailed, enough, mm-resolution, scanners, cost-prohibitive, many, robotic | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** The input to the proposed method consists of a series of RGB-D observations, I = {I1, I2, . . . , IN}, and corresponding camera ...
- **p. 3 / III. METHOD - extractive body cue:** Because cm-resolution LiDARs are not detailed enough and mm-resolution 3D scanners are cost-prohibitive in many robotic applications, we assume a collection of registered RGB-D observations ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One use of this representation is affordance grounding, in which unconstrained language queries produce the relation to the functional elements required to fulfill a task ...
- **p. 2 / III. METHOD - extractive body cue:** For example, we want a cabinet to have a direct relationship with its knobs, enhancing the scene graph with information about the object's possible interactions.
- **p. 4 / III. METHOD - extractive body cue:** Overview of our functionality-aware 3D scene graph generation pipeline, which consists of three stages: (1) Detection, where instance segmentation and feature extraction are performed to ...
- **p. 4 / III. METHOD - extractive body cue:** For each image, each o[i] mj ∈O[i] m is compared to the nodes' point cloud in the graph representing objects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a result, even state-of-the-art object detectors struggle with low detection accuracy in both 2D and 3D.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Since there are also no other pretrained detectors for this task, our first step is to produce data for our own model. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Functionality Aware 3D Scene Graph Generation In the past few years, a clear methodology has emerged as a framework for generating a ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Further, we compare these models on a variant dataset, which we compute using the slicing-aided hyper inference (SAHI) mechanism [46], and refer to it as ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We note that the exact numerical results are difficult to compare, as [5] does not release either the model checkpoints or the full train/test split.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** process, consists, three, phases, Detection, Instance, segmentation, entities, captured, images, feature, extraction, Node, creation, Multi-view, geometric, semantic, merging, Edge, Relationship.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The train-validation split of the dataset is 80/20, with the split ensuring that train and validation images come from different scenes. | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Global / local decision | As a baseline, we run YOLO-Worldv8.2 [40] and Grounding Dino [41] in a zero-shot fashion. | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Motion execution / recovery | Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that ... | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Further, we compare these models on a variant dataset, which we compute using the slicing-aided hyper inference (SAHI) mechanism [46], and refer to it as ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Note that we retain all functional element detections, even without object associations, to avoid penalizing scores when parent objects are undetected.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To further emphasize the correlation between 2D detection quality and 3D segmentation performance, we conducted an ablation study to relate the metrics from the previous ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Label Refinement Ablation Study As described in Section III-B, the first detection of functional elements only associates them with their affordance label.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Next, we fine-tune YOLOv11 [44] and RT-DETR [45] on the standard dataset.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. An example of a generated 3D scene graph and its application. The model represents both object and functional element nodes linked through intra-object ...
- **p. 7 / VI. CONCLUSIONS - extractive body cue:** It does not rely on segmenting a pre-existing highquality point cloud, which makes it also suitable for robotics applications with affordable RGB-D sensing.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), objective p. 3 (III. METHOD), p. 4 (III. METHOD), temporal p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORK), p. 2 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
