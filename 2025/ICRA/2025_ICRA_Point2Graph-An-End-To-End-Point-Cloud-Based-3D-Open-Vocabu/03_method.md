# Method - Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.10350v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 5 (III. METHODOLOGY)): To obtain open-vocabulary features for each room, inspired by the approach in [8], we use the CLIP visual encoder to extract embeddings from the images.

## Method Body Digest

- **p. 4 / III. METHODOLOGY - extractive body cue:** To obtain open-vocabulary features for each room, inspired by the approach in [8], we use the CLIP visual encoder to extract embeddings from the images.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Specically, the model takes as input both the ltered 3D point cloud and a textual description and retrieves the appropriate object label by identifying the ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** A region detection module is then applied to segment the scene into individual rooms.
- **p. 3 / III. METHODOLOGY - extractive body cue:** These objects are then processed with a text query in an open-vocabulary 3D object classication module to obtain segmented and labeled objects.
- **p. 2 / III. METHODOLOGY - extractive body cue:** In this section, we present our design of Point2Graph, which builds a compact and enriched open-vocabulary 3D scene graph with solely 3D scene model input.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Using the Voronoi planner, we are able to generate the Voronoi navigation map.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Then, argmax and majority voting are applied to get the type for each room.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Next, we construct a cosine similarity matrix between the K representative features and the text features from CLIP and take the argmax along the category ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Generally speaking, our framework consists of a room segmentation and classication module and an object detection and classication module.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Object-Level Detection and Classication After getting the segmentation result for each room, our approach mainly consists of two steps, where the rst step deals with ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** In this section, we present our design of Point2Graph, which builds a compact and enriched open-vocabulary 3D scene graph with solely 3D scene model input.

## Source Evidence Cues

- **p. 4 / III. METHODOLOGY - extractive body cue:** To obtain open-vocabulary features for each room, inspired by the approach in [8], we use the CLIP visual encoder to extract embeddings from the images.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Specically, the model takes as input both the ltered 3D point cloud and a textual description and retrieves the appropriate object label by identifying the ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** A region detection module is then applied to segment the scene into individual rooms.
- **p. 3 / III. METHODOLOGY - extractive body cue:** These objects are then processed with a text query in an open-vocabulary 3D object classication module to obtain segmented and labeled objects.
- **p. 2 / III. METHODOLOGY - extractive body cue:** In this section, we present our design of Point2Graph, which builds a compact and enriched open-vocabulary 3D scene graph with solely 3D scene model input.
- **p. 5 / III. METHODOLOGY - extractive body cue:** Using the Voronoi planner, we are able to generate the Voronoi navigation map.
- **Detected method headings:** III. METHODOLOGY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To obtain open-vocabulary features for each room, inspired by the approach in [8], we use the CLIP visual encoder to extract embeddings ... | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Specically, the model takes as input both the ltered 3D point cloud and a textual description and retrieves the appropriate object label ... | p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | A region detection module is then applied to segment the scene into individual rooms. | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHODOLOGY - extractive body cue:** Then, argmax and majority voting are applied to get the type for each room.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Next, we construct a cosine similarity matrix between the K representative features and the text features from CLIP and take the argmax along the category ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, input, point, cloud, segmented, slices, along, z-axis, slice, projected, onto, occupancy, grid, denoted | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | First, input, point, cloud, segmented, slices, along, z-axis, slice, projected | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Generally, speaking, framework, consists, room, segmentation, classi, cation, module, object | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Then, argmax, majority, voting, applied, type, room, Next, construct, cosine | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive body cue:** First, the input point cloud is segmented into N slices along the z-axis, with each slice projected onto an occupancy grid map denoted as Gk, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Compared with existing methods [8], [9], our proposed Point2Graph framework solely use the scene point cloud as input to generate open-vocabulary 3D scene graph.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Specically, the model takes as input both the ltered 3D point cloud and a textual description and retrieves the appropriate object label by identifying the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, the point clouds created from a Building Information Model (BIM) or LiDAR sensors often lack the RGB-D images and their pose data [13], ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** In this section, we present our design of Point2Graph, which builds a compact and enriched open-vocabulary 3D scene graph with solely 3D scene model input.
- **p. 3 / III. METHODOLOGY - extractive body cue:** 3: Generation of border-enhanced density map: The process begins by segmenting the point cloud into N layers, each of which is projected into a grid ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** For each proposed 3D bounding box, we extract and crop the corresponding point cloud for each object from the original room point cloud denoted as ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | This step ensures that only the regions consistently identied across most layers are considered as wall boundaries. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Object-Level Detection and Classication After getting the segmentation result for each room, our approach mainly consists of two steps, where the rst ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** obtain, open-vocabulary, features, room, inspired, CLIP, visual, encoder, extract, embeddings, images, Speci, cally, model, takes, input, ltered, point, cloud, textual.
- **Relevant PDF headings:** III. METHODOLOGY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Evaluation for Object Detection and Classication We conducted our experiments on the widely-used ScanNetv2 [45] indoor point cloud dataset, which consists of ... | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Global / local decision | We compared our method to RoomFormer [28], the current SOTA in learning-based algorithms, and the room segmentation techniques employed in HOV-SG [8], ... | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Motion execution / recovery | In our experimental results, shown in TABLE I, by generating a border-enhanced density map before input to RoomFormer, our approach achieved 12% ... | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5: Overview of the 3D open-vocabulary detection pipeline: It consists of two stages: (1) detection and localization using class-agnostic bounding boxes and DBSCAN ltering ...
- **p. 6 / V. CONCLUSION - extractive body cue:** Nevertheless, Point2Graph has its limitations.
- **p. 6 / V. CONCLUSION - extractive body cue:** In conclusion, this work presents the Point2Graph framework, which addresses the limitations of current openvocabulary 3D scene graph generation methods by eliminating the need for ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Our proposed "Snap-Lookup" pipeline, which incorporates room visual features into type inference, can differentiate between various types of rooms that contain the same objects-something text-only ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), objective p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), temporal p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (IV. EXPERIMENTAL RESULTS), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
