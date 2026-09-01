# Method - FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Overview of Framework), p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework), p. 5 (3.4. Merging 3D SSGs), p. 5 (3.4. Merging 3D SSGs)): This RTDETR object detector is a state-of-the-art real-time detection model, which preserves intermediate self-attention features for subsequent relationship extraction.

## Method Body Digest

- **p. 3 / 3.2. Overview of Framework - extractive PDF cue:** This RTDETR object detector is a state-of-the-art real-time detection model, which preserves intermediate self-attention features for subsequent relationship extraction.
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** Merging (Section 3.4) CNN Backbone & Encoder Self-Attention Layer 0 Self-Attention Layer 1 Self-Attention Layer N Hidden Layers Self-Attention Features RT-DETR Detected Objects EGTR Relationship ...
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** (b) The EGTR model [12] extracts inter-object relationships through utilization of preserved self-attention features from RT-DETR.
- **p. 3 / 3.2. Overview of Framework - extractive PDF cue:** These local graphs are then integrated into a global SSG through the proposed merging algorithm that is described in detail in Section 3.4.
- **p. 5 / 3.4. Merging 3D SSGs - extractive PDF cue:** The algorithm merges nodes with Hellinger distances below the threshold δd and adds unmerged nodes to Vglobal as new objects.
- **p. 5 / 3.4. Merging 3D SSGs - extractive PDF cue:** Objects detected from diverse angular perspectives and spatial positions receive proportionally higher weights, thus mitigating viewpoint bias and ensuring robust threedimensional representation.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** For our 2D SG generation model, we employ EGTR [12] with RT-DETRv2-M [21, 44] as the object detection backbone.
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** Given a sequence of input images, the primary objective is to construct a 3D SSG G of the target environment.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** The main contributions of the paper can be summarized as follows: • We introduce FROSS, an innovative methodology for online real-time generation of 3D SSGs.
- **p. 1 / 1. Introduction - extractive PDF cue:** We introduce FROSS, an online real-time 3D semantic scene graph generation method that leverages and integrates 2D scene graphs.
- **p. 2 / 1. Introduction - extractive PDF cue:** FROSS demonstrates superior performance and significantly faster processing speeds compared to existing baseline methods. • We propose a new merging algorithm based on Gaussian distributions ...

## Source Evidence Cues

- **p. 3 / 3.2. Overview of Framework - extractive PDF cue:** This RTDETR object detector is a state-of-the-art real-time detection model, which preserves intermediate self-attention features for subsequent relationship extraction.
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** Merging (Section 3.4) CNN Backbone & Encoder Self-Attention Layer 0 Self-Attention Layer 1 Self-Attention Layer N Hidden Layers Self-Attention Features RT-DETR Detected Objects EGTR Relationship ...
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** (b) The EGTR model [12] extracts inter-object relationships through utilization of preserved self-attention features from RT-DETR.
- **p. 3 / 3.2. Overview of Framework - extractive PDF cue:** These local graphs are then integrated into a global SSG through the proposed merging algorithm that is described in detail in Section 3.4.
- **p. 5 / 3.4. Merging 3D SSGs - extractive PDF cue:** The algorithm merges nodes with Hellinger distances below the threshold δd and adds unmerged nodes to Vglobal as new objects.
- **p. 5 / 3.4. Merging 3D SSGs - extractive PDF cue:** Objects detected from diverse angular perspectives and spatial positions receive proportionally higher weights, thus mitigating viewpoint bias and ensuring robust threedimensional representation.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** For our 2D SG generation model, we employ EGTR [12] with RT-DETRv2-M [21, 44] as the object detection backbone.
- **Detected method headings:** 3. Methodology (p. 3); 4.1.2. Baseline Methods (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | This RTDETR object detector is a state-of-the-art real-time detection model, which preserves intermediate self-attention features for subsequent relationship extraction. | p. 3 (3.2. Overview of Framework), p. 4 (3.3. Lifting 2D SG to 3D) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Merging (Section 3.4) CNN Backbone & Encoder Self-Attention Layer 0 Self-Attention Layer 1 Self-Attention Layer N Hidden Layers Self-Attention Features RT-DETR Detected ... | p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | (b) The EGTR model [12] extracts inter-object relationships through utilization of preserved self-attention features from RT-DETR. | p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** Given a sequence of input images, the primary objective is to construct a 3D SSG G of the target environment.
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** (4) The naive definition alone is insufficient since the original equation is inherently designed for projection from 3D to 2D space.
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** Simply inverting the equation results in a 3D Gaussian that lacks variance information along the depth axis, as the 2D covariance matrix does not capture ...
- **p. 5 / 3.4. Merging 3D SSGs - extractive PDF cue:** The Hellinger distance HD(i, j) between Gaussian distributions N(µi, Σi) and N(µj, Σj) is quantified through the following equation, wherein BD(i, j) represents the Bhattacharyya ...
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** Furthermore, the algorithm must be able to maintain online processing capabilities to update G continuously whenever new image data becomes available.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** All hyperparameters were determined through grid search evaluation on the validation split, with particular emphasis on relationship recall optimization.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3.1. Problem Definition), p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D), p. 5 (3.4. Merging 3D SSGs), p. 3 (3.1. Problem Definition).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Merging, Section, CNN, Backbone, Encoder, Self-Attention, Layer, Hidden, Layers, Features, RT-DETR, Detected, Objects, EGTR | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Merging, Section, CNN, Backbone, Encoder, Self-Attention, Layer, Hidden, Layers, Features | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, introduce, FROSS, innovative, methodology, online, real-time | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Given, sequence, input, images, primary, objective, construct, SSG, target, environment | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** Merging (Section 3.4) CNN Backbone & Encoder Self-Attention Layer 0 Self-Attention Layer 1 Self-Attention Layer N Hidden Layers Self-Attention Features RT-DETR Detected Objects EGTR Relationship ...
- **p. 3 / 3.2. Overview of Framework - extractive PDF cue:** This RTDETR object detector is a state-of-the-art real-time detection model, which preserves intermediate self-attention features for subsequent relationship extraction.
- **p. 2 / 1. Introduction - extractive PDF cue:** This observation motivates an alternative approach for online and real-time 3D SSG generation: inferring 2D SGs from images and subsequently lifting them into 3D space, ...
- **p. 3 / 3.1. Problem Definition - extractive PDF cue:** Given a sequence of input images, the primary objective is to construct a 3D SSG G of the target environment.
- **p. 1 / 1. Introduction - extractive PDF cue:** 3D seChair Cabinet TV TV Above Under Chair Cabinet Near TV Chair Cabinet Merge Input Image Sequence 3D Semantic Scene Graph Lift Objects to 3D ...
- **p. 2 / 1. Introduction - extractive PDF cue:** A fundamental insight for generating 3D SSGs emerges from the observation that precise object pose and shape information is not essential.
- **p. 4 / 3.3. Lifting 2D SG to 3D - extractive PDF cue:** An overview of the FROSS framework: (a) The process initiates with object detection via RT-DETR [44] from an RGB-D image and its associated camera pose.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Compared to the previous methods for online real-time 3D SSG generation methods [16, 34, 35], FROSS demonstrates significantly reduced end-to-end latency and ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Although several studies [34, 35] have developed methods for incremental point cloud reconstruction and segmentation to achieve online and real-time 3D SSG ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** RTDETR, object, detector, state-of-the-art, real-time, detection, model, preserves, intermediate, self-attention, features, subsequent, relationship, extraction, Merging, Section, CNN, Backbone, Encoder, Layer.
- **Relevant PDF headings:** 3. Methodology (p. 3); 4.1.2. Baseline Methods (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | 3DSSG augments the base dataset with object attributes, hierarchical category labels, and directed edges that describe inter-object semantic relationships such as ‘standing ... | p. 5 (4.1.1. Datasets), p. 6 (4.1.1. Datasets) |
| Global / local decision | Section 4.1 introduces the datasets, baseline SSG generation methods, and evaluation metrics. | p. 5 (4. Experimental Results), p. 6 (4.1.2. Baseline Methods) |
| Motion execution / recovery | The results reveal that FROSS achieves the highest performance among all baseline methods with much lower processing latency. | p. 7 (4.3. Quantitative Results), p. 8 (4.5. Runtime Analysis) |

## Failure and Ablation Link

- **p. 5 / 4. Experimental Results - extractive PDF cue:** We further provide runtime analyses on the ReplicaSSG dataset in Section 4.5, along with additional ablation studies in Section 4.6.
- **p. 6 / 4.1.2. Baseline Methods - extractive PDF cue:** In the ablation studies, we investigate the impact of using ground truth 2D SGs and camera trajectories on the ReplicaSSG dataset.
- **p. 6 / 4.1.3. Matching Object Predictions to Ground Truth - extractive PDF cue:** As FROSS generates predictions without explicit point cloud output, we establish evaluation metrics using backprojected 3D points.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce FROSS, an online real-time 3D semantic scene graph generation method that leverages and integrates 2D scene graphs. FROSS represents objects as ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** The impact of estimated trajectories are further analyzed via ablation studies in Section 4.6.2.
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Performance comparison of 3D SSG generation methods on the 3DSSG dataset and the end-to-end latency without environmental mapping reported in their original literature, along with ...
- **p. 8 / 4.5. Runtime Analysis - extractive PDF cue:** Runtime analysis of the key components of FROSS.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.2. Overview of Framework), p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework), p. 5 (3.4. Merging 3D SSGs), p. 5 (3.4. Merging 3D SSGs), objective p. 3 (3.1. Problem Definition), p. 4 (3.3. Lifting 2D SG to 3D), p. 4 (3.3. Lifting 2D SG to 3D), p. 5 (3.4. Merging 3D SSGs), p. 3 (3.1. Problem Definition), p. 7 (4.2. Implementation Details), temporal p. 8 (4.5. Runtime Analysis), p. 2 (1. Introduction), p. 3 (2.2. Online 3D Semantic Scene Graph Generation), p. 8 (5. Conclusion), p. 1 (1. Introduction), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
