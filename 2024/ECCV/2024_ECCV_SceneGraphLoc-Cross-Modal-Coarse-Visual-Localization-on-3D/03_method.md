# Method - SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered))): The training phase is represented by orange arrows, while blue arrows denote the inference phase.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** With images, SceneGraphLoc achieves performance close to that of state-of-the-art techniques depending on large image databases, while requiring three orders-of-magnitude less storage and operating orders-of-magnitude ...
- **p. 2 / 1 Introduction - extractive body cue:** The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas ...
- **p. 2 / 1 Introduction - extractive body cue:** In the inference phase, the task involves assigning the correct scene graph to a given query image from a selection of multiple graphs, achieved by ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Given these modalities, the proposed method SceneGraphLoc learns a fixed-sized embedding for each node (i.e., representing object instances) in the scene graph, enabling effective matching ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.
- **p. 3 / 1 Introduction - extractive body cue:** The primary contributions of this paper are as follows: 1.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** With images, SceneGraphLoc achieves performance close to that of state-of-the-art techniques depending on large image databases, while requiring three orders-of-magnitude less storage and operating orders-of-magnitude ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The training phase is represented by orange arrows, while blue arrows denote the inference phase. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are ... | p. 2 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation. | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas ...
- **p. 2 / 1 Introduction - extractive body cue:** In the inference phase, the task involves assigning the correct scene graph to a given query image from a selection of multiple graphs, achieved by ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | introduce, task, localizing, input, image, within, multi-modal, reference, represented, collection, scene, graphs, Given, modalities | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | introduce, task, localizing, input, image, within, multi-modal, reference, represented, collection | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | enables, creation, small, efficient, databases, significantly, accelerates, coarse, localization, process | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | objective, learn, embeddings, graph, image, positive, pair, drawn, closer, whereas | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section not recovered) - extractive body cue:** We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Given these modalities, the proposed method SceneGraphLoc learns a fixed-sized embedding for each node (i.e., representing object instances) in the scene graph, enabling effective matching ...
- **p. 3 / 1 Introduction - extractive body cue:** SceneGraphLoc, a new method for the coarse localization of an input image given a reference map represented by a database of 3D scene graphs.
- **p. 2 / 1 Introduction - extractive body cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 2 / 1 Introduction - extractive body cue:** Cross-modal approaches, such as [100,142], which attempt to bridge different types of data, often restrict their scope to connecting two modalities at a time (e.g., ...
- **p. 3 / 1 Introduction - extractive body cue:** With images, SceneGraphLoc achieves performance close to that of state-of-theart image-based methods while requiring three orders-of-magnitude less storage and operating orders-of-magnitude faster.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | ScanNet encompasses 1613 monocular sequences of room-scale 3D scenes, offering 3D mesh reconstructions alongside the RGBD frame sequences utilized for the reconstructions. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Conversely, in the temporal scenario, the scene graph is derived from a sequence captured at a different temporal stage than the query, ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 10 / 4 Experiments - extractive body cue:** These methods offer advanced performance but demand significant storage for image descriptors and exhibit slower inference times.
- **p. 11 / 4 Experiments - extractive body cue:** Additionally, we will report the inference time and storage requirements.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, phase, represented, orange, arrows, while, blue, denote, inference, challenge, current, state-of-the-art, image-based, coarse, localization, methods, AnyLoc, dependency, extensive, image.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and ... | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Global / local decision | For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet [63] and AnyLoc [55]. | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Motion execution / recovery | SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly. | p. 12 (4 Experiments), p. 13 (4 Experiments) |

## Failure and Ablation Link

- **p. 12 / 4 Experiments - extractive body cue:** Also, the storage of SceneGraphLoc with and without images is the same due to its design of distilling knowledge into fixed-sized embeddings.
- **p. 13 / 4 Experiments - extractive body cue:** OpenMask3D attains an accuracy comparable to our proposed method without incorporating the image modality.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Ablation study performed on the val. split of 3RScan [123], analysing map modalities (P - point cloud, I - image, A - attributes, ...
- **p. 10 / 4 Experiments - extractive body cue:** Both methods were fine-tuned on our dataset for accurate comparison.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), objective p. 2 (1 Introduction), p. 2 (1 Introduction), temporal p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 8 (2 Related Work), p. 10 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
