# Method - 3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1910.02527; PDF retrieval source: https://arxiv.org/pdf/1910.02527. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (C S1), p. 4 (4. Constructing the 3D Scene Graph), p. 4 (3. 3D Scene Graph Structure), p. 2 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction)): The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images.

## Method Body Digest

- **p. 3 / C S1 - extractive body cue:** The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images.
- **p. 4 / 4. Constructing the 3D Scene Graph - extractive body cue:** In our experiments (Section 5), we used the best reported performing Mask RCNN network [18] and got results only for detections with a confidence score ...
- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 2 / 1. Introduction - extractive body cue:** To construct the 3D Scene Graph, we combine stateof-the-art algorithms in a mainly automatic approach to semantic recognition.
- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...
- **p. 2 / 1. Introduction - extractive body cue:** Semantic repositories use different representations, such as object class and natural language captions.
- **p. 3 / C S1 - extractive body cue:** (a) Input to the method is a 3D mesh model with registered panoramic images.
- **p. 4 / 4. Constructing the 3D Scene Graph - extractive body cue:** Having RGB panoramas as input gives the opportunity to formulate a framing approach that samples rectilinear images from them with the objective to maximize detection ...

## Design Rationale

- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 2 / 1. Introduction - extractive body cue:** This gives free computation for various attributes and relationships. • We propose a two-step robustification approach to optimizing semantic recognition using imperfect existing detectors, which ...
- **p. 1 / 1. Introduction - extractive body cue:** 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.

## Source Evidence Cues

- **p. 3 / C S1 - extractive body cue:** The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images.
- **p. 4 / 4. Constructing the 3D Scene Graph - extractive body cue:** In our experiments (Section 5), we used the best reported performing Mask RCNN network [18] and got results only for detections with a confidence score ...
- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 2 / 1. Introduction - extractive body cue:** To construct the 3D Scene Graph, we combine stateof-the-art algorithms in a mainly automatic approach to semantic recognition.
- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...
- **p. 2 / 1. Introduction - extractive body cue:** Semantic repositories use different representations, such as object class and natural language captions.
- **p. 3 / C S1 - extractive body cue:** (a) Input to the method is a 3D mesh model with registered panoramic images.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The Gibson database [44], consists of several hundreds of 3D mesh models with registered panoramic images. | p. 3 (C S1), p. 4 (4. Constructing the 3D Scene Graph) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | In our experiments (Section 5), we used the best reported performing Mask RCNN network [18] and got results only for detections with ... | p. 4 (4. Constructing the 3D Scene Graph), p. 4 (3. 3D Scene Graph Structure) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and ... | p. 4 (3. 3D Scene Graph Structure), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...
- **p. 4 / 4. Constructing the 3D Scene Graph - extractive body cue:** Having RGB panoramas as input gives the opportunity to formulate a framing approach that samples rectilinear images from them with the objective to maximize detection ...
- **p. 3 / C S1 - extractive body cue:** [4] employ Mask R-CNN trained on the COCOStuff dataset to acquire initial object instance segmentation masks that are subsequently verified and updated by users.
- **p. 2 / 1. Introduction - extractive body cue:** Each constraint provides more robust final results and consistent semantic output.
- **p. 2 / 1. Introduction - extractive body cue:** Beginning from 2D, we gradually aggregate information in 3D using two constraints: framing and multi-view consistency.
- **p. 3 / C S1 - extractive body cue:** Although most approaches focus solely on manual labor, some employ automation to minimize the amount of human interaction with the data and provide faster turnaround.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Constructing the 3D Scene Graph), p. 3 (C S1).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, typical, output, scanners, consists, mesh, models, registered, RGB, panoramas, corresponding, camera, parameters, data | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | input, typical, output, scanners, consists, mesh, models, registered, RGB, panoramas | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | input, typical, output, scanners, consists, mesh, models, registered, RGB, panoramas | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | alleviate, devise, semi-automatic, framework, employs, existing, detection, methods, enhances, them | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The input to our method is the typical output of 3D scanners and consists of 3D mesh models, registered RGB panoramas and the corresponding camera ...
- **p. 5 / 4. Constructing the 3D Scene Graph - extractive body cue:** To aggregate the casted votes, we formulate a weighted majority voting scheme based on how close an observation point is to a surface, following the ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we articulate that 3D space is more stable and invariant, yet connected to images and other pixel and non-pixel output domains (e.g. ...
- **p. 2 / 1. Introduction - extractive body cue:** changes as possible, and (b) easily and deterministically connected to various output ports that different domains and tasks require, such as images or videos.
- **p. 5 / 4. Constructing the 3D Scene Graph - extractive body cue:** gin by densely sampling rectilinear images on the panorama with different yaw (ψ), pitch (θ) and Field of View (FoV) camera parameters, with the goal ...
- **p. 3 / C S1 - extractive body cue:** (a) Input to the method is a 3D mesh model with registered panoramic images.
- **p. 4 / 3. 3D Scene Graph Structure - extractive body cue:** The final layer introduces cameras as part of the graph: each camera location is a node in 3D and a possible observation (e.g., an RGB ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Graph structures are also commonly used in human-object interaction tasks [39] and other spatiotemporal problems [20], creating connections among nodes within and ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Each step is done by 2 users independently for cross checking. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** To alleviate this we devise a semi-automatic framework that employs existing detection methods and enhances them using two main constraints: I. framing of query images ...
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** For more details on implementation and training/testing we refer the reader to Mask R-CNN [18] and Detectron [1].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Gibson, database, consists, several, hundreds, mesh, models, registered, panoramic, images, experiments, Section, best, reported, performing, Mask, RCNN, network, only, detections.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The semantic categories used come from the COCO dataset [33] for objects, MINC [8] for materials, and DTD [12] for textures. | p. 6 (5.1. Dataset Statistics), p. 6 (5.2. Evaluation of Automated Pipeline) |
| Global / local decision | Baselines: We compare the following approaches in 2D: • Mask R-CNN [18]: We run Mask R-CNN on 6 rectilinear images sampled on ... | p. 6 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline) |
| Motion execution / recovery | Similar improvements can be seen in the case of 3D (Figure 7). | p. 7 (5.2. Evaluation of Automated Pipeline), p. 6 (5.2. Evaluation of Automated Pipeline) |

## Failure and Ablation Link

- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** Mask R-CNN with framing (c) was able to remove the tree detections and recuperate a missed toilet that is highly occluded.
- **p. 7 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** Mask R-CNN with framing and multi-view consistency (d) further removed the painted vase and bed reflection, achieving results very close to the ground truth.
- **p. 8 / 5.3. 2D Scene Graph Prediction - extractive body cue:** Since our semantic information resides in 3D space, we can infer the full extents of object occlusions without additional annotations and in a fully automatically ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera. Elements are nodes in the graph and have ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Constructing the 3D Scene Graph. (a) Input to the method is a 3D mesh model with registered panoramic images. (b) Each panorama is ...
- **p. 6 / 5.2. Evaluation of Automated Pipeline - extractive body cue:** It is pre-trained on ImageNet-5K and fine-tuned on COCO.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Semantic statistics for bed: (a) Number of object instances in buildings. (b) Distribution of its surface coverage. (c) Nearest object instance in 3D ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (C S1), p. 4 (4. Constructing the 3D Scene Graph), p. 4 (3. 3D Scene Graph Structure), p. 2 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction), objective p. 1 (Abstract), p. 4 (4. Constructing the 3D Scene Graph), p. 3 (C S1), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (C S1), temporal p. 2 (2. Related Work), p. 7 (5.2. Evaluation of Automated Pipeline), p. 7 (5.2. Evaluation of Automated Pipeline), p. 8 (5.3. 2D Scene Graph Prediction), p. 1 (Abstract), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
