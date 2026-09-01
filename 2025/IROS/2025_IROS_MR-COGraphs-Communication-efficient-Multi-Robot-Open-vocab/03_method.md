# Method - MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2412.18381; PDF retrieval source: https://arxiv.org/pdf/2412.18381. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD)): 1, this section first outlines the map representation of the COGraph, followed by an introduction to the three key modules: 1) feature-object nodes and edges generation, which constructs the COGraph ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** 1, this section first outlines the map representation of the COGraph, followed by an introduction to the three key modules: 1) feature-object nodes and edges ...
- **p. 4 / III. METHOD - extractive PDF cue:** These features are then used to train the encoder and decoder, which are optimized to effectively compress and reconstruct high-dimensional features.
- **p. 4 / III. METHOD - extractive PDF cue:** 2) Training Process: We train the feature encoder and decoder using images from the ImageNet dataset [31], which contains over 80,000 images across 1,000 categories.
- **p. 3 / III. METHOD - extractive PDF cue:** COGraphs Representation The proposed COGraph consists of the robot name, nodes, and edges.
- **p. 5 / III. METHOD - extractive PDF cue:** Place recognition is then performed by iteratively calculating the feature similarity between each received node and nodes in the local COGraph.
- **p. 5 / III. METHOD - extractive PDF cue:** 1) Place Recognition: The feature decoder trained in Section III-C is used to recover each node's semantic feature f 3D i′,512 in received COGraphs.
- **p. 4 / III. METHOD - extractive PDF cue:** Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as existing image formats, ...
- **p. 4 / III. METHOD - extractive PDF cue:** The loss function combines L2 loss and cosine similarity loss between the original feature f raw i,512 and the reconstructed 512-dimensional features f decode i,512 ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To fulfill the requirements above, we propose a Communication-efficient Multi-Robot Open-vocabulary 3D Scene Graphs-based Mapping (MR-COGraphs) System with the following contributions: • A data-efficient open-vocabulary ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** 1, we propose a graph-structured open-vocabulary representation called COGraph (detailed in Section III-A).
- **p. 3 / III. METHOD - extractive PDF cue:** COGraphs Representation The proposed COGraph consists of the robot name, nodes, and edges.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** 1, this section first outlines the map representation of the COGraph, followed by an introduction to the three key modules: 1) feature-object nodes and edges ...
- **p. 4 / III. METHOD - extractive PDF cue:** These features are then used to train the encoder and decoder, which are optimized to effectively compress and reconstruct high-dimensional features.
- **p. 4 / III. METHOD - extractive PDF cue:** 2) Training Process: We train the feature encoder and decoder using images from the ImageNet dataset [31], which contains over 80,000 images across 1,000 categories.
- **p. 3 / III. METHOD - extractive PDF cue:** COGraphs Representation The proposed COGraph consists of the robot name, nodes, and edges.
- **p. 5 / III. METHOD - extractive PDF cue:** Place recognition is then performed by iteratively calculating the feature similarity between each received node and nodes in the local COGraph.
- **p. 5 / III. METHOD - extractive PDF cue:** 1) Place Recognition: The feature decoder trained in Section III-C is used to recover each node's semantic feature f 3D i′,512 in received COGraphs.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | 1, this section first outlines the map representation of the COGraph, followed by an introduction to the three key modules: 1) feature-object ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | These features are then used to train the encoder and decoder, which are optimized to effectively compress and reconstruct high-dimensional features. | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | 2) Training Process: We train the feature encoder and decoder using images from the ImageNet dataset [31], which contains over 80,000 images ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive PDF cue:** Comparison of the original and decoded features when the encoder and decoder are trained on household-related images from ImageNet. same way as existing image formats, ...
- **p. 4 / III. METHOD - extractive PDF cue:** The loss function combines L2 loss and cosine similarity loss between the original feature f raw i,512 and the reconstructed 512-dimensional features f decode i,512 ...
- **p. 5 / III. METHOD - extractive PDF cue:** We evaluate all candidate translations ti,i′ from matching pairs and select the one that maximizes the number of merged nodes.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | back, projection, conducted, images, depth, poses, derived, SLAM, observation, conduct, further, experimental, evaluations, Section | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | back, projection, conducted, images, depth, poses, derived, SLAM, observation, conduct | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | fulfill, requirements, above, Communication-efficient, Multi-Robot, Open-vocabulary, Scene, Graphs-based, Mapping, MR-COGraphs | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Comparison, original, decoded, features, when, encoder, decoder, trained, household-related, images | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - extractive PDF cue:** 3D back projection is conducted using FO images, depth images, and poses derived from SLAM.
- **p. 4 / III. METHOD - extractive PDF cue:** Based on this observation, we conduct further experimental evaluations in Section IV-B.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** III-D) Segmentation Model depth seg-image Robot 1 COGraph-3 COGraph-512 Sensors COGraphs Representation (Sec.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Firstly, each robot generates the nodes and edges of its local COGraph utilizing the output of the Simultaneous Localization and Mapping (SLAM) module and the ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** For instance, in an open-vocabulary point cloud map, each point is linked to a high-dimensional feature vector [9].
- **p. 3 / III. METHOD - extractive PDF cue:** These FO images can be transmitted in the
- **p. 3 / III. METHOD - extractive PDF cue:** COGraphs Representation The proposed COGraph consists of the robot name, nodes, and edges.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | 2, given a sequence of RGB-D images, we run an open-vocabulary segmentation model to obtain the segmented objects in each frame. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We determine whether the semantic point clouds pck in a sequence of frames belong to the same object by analyzing the information ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Experiments in Section IV are conducted on a desktop PC equipped with an Intel I7-13700 CPU and an Nvidia RTX 4080 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - extractive PDF cue:** These features are then used to train the encoder and decoder, which are optimized to effectively compress and reconstruct high-dimensional features.
- **p. 4 / III. METHOD - extractive PDF cue:** 2) Training Process: We train the feature encoder and decoder using images from the ImageNet dataset [31], which contains over 80,000 images across 1,000 categories.
- **p. 5 / III. METHOD - extractive PDF cue:** 1) Place Recognition: The feature decoder trained in Section III-C is used to recover each node's semantic feature f 3D i′,512 in received COGraphs.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** The training parameters are set as follows: epochs = 5000, batch size = 1920, and learning rate = 0.0001.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** section, first, outlines, representation, COGraph, followed, introduction, three, modules, feature-object, nodes, edges, generation, constructs, highdimensional, features, data-driven, feature, compression, where.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Map Merging Evaluation 1) Dataset: Since the Replica dataset lacks multi-room scenes suitable for collaborative mapping [22] (only apartment2 is available), we ... | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Global / local decision | Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Motion execution / recovery | Compared to baseline methods, our approach not only maintains high accuracy and query success rates but also ensures realtime performance in the ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We also test COGraph-512, a variant of our method without feature compression.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** This demonstrates that our method effectively reduces communication data volume without compromising mapping performance.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Since our text queries do not include complex negation or multi-step affordances, we run ConceptGraphs without GPT.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Compared to a merging approach without feature compression, the increase in translation estimation error is minimal.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** 5a, we compare the performance of the three encoding configurations with raw-clip, which directly uses the 512-dimensional CLIP feature without encoding and decoding process.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Overview of the MR-COGraphs Framework. to the classes of objects annotated in the training datasets [6]. In contrast, open-vocabulary maps are not constrained ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** demonstrate that our feature compression process does not compromise the object finding rate and query success rate across the three evaluated scenes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), objective p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), temporal p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (IV. EXPERIMENTS), p. 2 (II. RELATED WORK), p. 3 (III. METHOD), p. 4 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
