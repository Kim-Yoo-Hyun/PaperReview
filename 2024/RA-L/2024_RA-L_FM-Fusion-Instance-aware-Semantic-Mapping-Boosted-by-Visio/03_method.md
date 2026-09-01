# Method - FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2402.04555; PDF retrieval source: https://arxiv.org/pdf/2402.04555. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (6 Method), p. 6 (6 Method), p. 7 (6 Method), p. 7 (6 Method)): The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.

## Method Body Digest

- **p. 6 / 6 Method - extractive PDF cue:** The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.
- **p. 6 / 6 Method - extractive PDF cue:** Our instance refinement module merges over-segmented instances caused by inconsistent instance masks at changed viewpoints.
- **p. 7 / 6 Method - extractive PDF cue:** We consider those limitations of foundation models.
- **p. 7 / 6 Method - extractive PDF cue:** One of the reasons is that foundation models preserve strong generalization ability.
- **p. 6 / 6 Method - extractive PDF cue:** Since Kimera updates the label measurements with a manually assigned likelihood probability and ignores the similarity score provided by GroundingDINO, it is easier to be ...
- **p. 7 / 6 Method - extractive PDF cue:** Hence, our statistical label likelihood can be used across domains.
- **p. 7 / 6 Method - extractive PDF cue:** RAM-Grounded-SAM maintains a similar label likelihood matrix across the image distribution.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** GroundingDINO [6], the latest State-of-the-Arts (SOTA) openset object detection network, reads a text prompt and performs Manuscript received: October 24, 2023; Accepted: January, 1, 2024.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To address such challenges, we propose a probabilistic label fusion method following the Bayes filter algorithm.
- **p. 6 / 6 Method - extractive PDF cue:** Compared with Kimera using RAM-GroundedSAM, our method achieved +15.6 mAP50.

## Source Evidence Cues

- **p. 6 / 6 Method - extractive PDF cue:** The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.
- **p. 6 / 6 Method - extractive PDF cue:** Our instance refinement module merges over-segmented instances caused by inconsistent instance masks at changed viewpoints.
- **p. 7 / 6 Method - extractive PDF cue:** We consider those limitations of foundation models.
- **p. 7 / 6 Method - extractive PDF cue:** One of the reasons is that foundation models preserve strong generalization ability.
- **Detected method headings:** 6 Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study. | p. 6 (6 Method), p. 6 (6 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Our instance refinement module merges over-segmented instances caused by inconsistent instance masks at changed viewpoints. | p. 6 (6 Method), p. 7 (6 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We consider those limitations of foundation models. | p. 7 (6 Method), p. 7 (6 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 6 Method - extractive PDF cue:** Since Kimera updates the label measurements with a manually assigned likelihood probability and ignores the similarity score provided by GroundingDINO, it is easier to be ...
- **p. 7 / 6 Method - extractive PDF cue:** Hence, our statistical label likelihood can be used across domains.
- **p. 7 / 6 Method - extractive PDF cue:** RAM-Grounded-SAM maintains a similar label likelihood matrix across the image distribution.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 6 (6 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | GroundingDINO, latest, State-of-the-Arts, SOTA, openset, object, detection, network, reads, text, prompt, performs, Manuscript, received | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | GroundingDINO, latest, State-of-the-Arts, SOTA, openset, object, detection, network, reads, text | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | incrementally, fuses, object, detections, foundation, models, instance-aware, semantic, address, challenges | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Since, Kimera, updates, label, measurements, manually, assigned, likelihood, probability, ignores | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** GroundingDINO [6], the latest State-of-the-Arts (SOTA) openset object detection network, reads a text prompt and performs Manuscript received: October 24, 2023; Accepted: January, 1, 2024.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The SLAM modules generate a camera pose and a global volumetric map.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our main contributions are: • An approach to fuse the object detections from visionlanguage foundation models into an instance-aware semantic map.
- **p. 6 / 6 Method - extractive PDF cue:** We further fused instance volume with a global volumetric map.
- **p. 6 / 6 Method - extractive PDF cue:** 8: The reconstructed instance map using RAM-Grounded-SAM in ScanNet scene0011, scene0435 and scene0633 (from top to bottom).
- **p. 7 / 6 Method - extractive PDF cue:** The images are from ScanNet scene0329.
- **p. 7 / 6 Method - extractive PDF cue:** More results can be found in our supplementary video.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | 1: Our system reads a sequence of RGB-D frames. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Cluster-All is applied as a post-processing step on the reconstructed semantic map from Kimera. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The global TSDF map is integrated for every RGBD frame, while our method and all baselines run in every 10 frames to ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** rest, ScanNet, experiment, focus, evaluating, module, through, ablation, study, instance, refinement, merges, over-segmented, instances, caused, inconsistent, masks, changed, viewpoints, consider.
- **Relevant PDF headings:** 6 Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We chose the public dataset ScanNet and SceneNN to evaluate the semantic mapping quality. | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |
| Global / local decision | We compared our method with Kimera 2 and a selfimplemented Fusion++. | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |
| Motion execution / recovery | Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores. | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 10: An image of object detection from Ablation-B and our method are shown in (a) and (b). The labels incorporated by text prompt augmentation ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 11: Reconstructions in SceneNN 096. False semantic and over-segmented instances are highlighted in red circles. So far, the system run offline. As shown in ...
- **p. 5 / V. EXPERIMENT - extractive PDF cue:** We evaluated a pre-trained Mask R-CNN and a fine-tuned Mask R-CNN.
- **p. 5 / V. EXPERIMENT - extractive PDF cue:** The pre-trained one is trained in COCO instance segmentation dataset, while we also fine-tuned it using ScanNet dataset.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 8: The reconstructed instance map using RAM-Grounded-SAM in ScanNet scene0011, scene0435 and scene0633 (from top to bottom). The falsely predicted semantic classes in (a) ...
- **p. 7 / 6 Method - extractive PDF cue:** As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (6 Method), p. 6 (6 Method), p. 7 (6 Method), p. 7 (6 Method), objective p. 6 (6 Method), p. 7 (6 Method), p. 7 (6 Method), temporal p. 1 (I. INTRODUCTION), p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 7 (6 Method), p. 7 (6 Method), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
