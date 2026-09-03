# Method - CenterPoint: Center-based 3D Object Detection and Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.11275; PDF retrieval source: https://arxiv.org/pdf/2006.11275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 5 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction), p. 4 (4. CenterPoint)): The 3D encoder then pools these features into its primary feature representation.

## Method Body Digest

- **p. 3 / 3. Preliminaries - extractive body cue:** The 3D encoder then pools these features into its primary feature representation.
- **p. 3 / 3. Preliminaries - extractive body cue:** A point-based network [40] then extracts features for all points inside a bin.
- **p. 4 / 4. CenterPoint - extractive body cue:** Then, a 2D CNN architecture detection head finds object centers and regress to full 3D bounding boxes using center features.
- **p. 5 / 4.1. Two-Stage CenterPoint - extractive body cue:** For box regression, the model predicts a refinement on top of first stage proposals, and we train the model with L1 loss.
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].
- **p. 4 / 4. CenterPoint - extractive body cue:** At inference time, we use this offset to associate current detections to past ones in a greedy fashion.
- **p. 1 / Abstract - extractive body cue:** On the Waymo Open Dataset, CenterPoint outperforms all previous single model method by a large margin and ranks first among all Lidar-only submissions.
- **p. 4 / 4. CenterPoint - extractive body cue:** CenterPoint combines all heatmap and regression losses in one common objective and jointly optimizes them.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 ...
- **p. 3 / 3. Preliminaries - extractive body cue:** We introduce a novel center-based detection head but rely on existing 3D backbones (VoxelNet or PointPillars).
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].

## Source Evidence Cues

- **p. 3 / 3. Preliminaries - extractive body cue:** The 3D encoder then pools these features into its primary feature representation.
- **p. 3 / 3. Preliminaries - extractive body cue:** A point-based network [40] then extracts features for all points inside a bin.
- **p. 4 / 4. CenterPoint - extractive body cue:** Then, a 2D CNN architecture detection head finds object centers and regress to full 3D bounding boxes using center features.
- **p. 5 / 4.1. Two-Stage CenterPoint - extractive body cue:** For box regression, the model predicts a refinement on top of first stage proposals, and we train the model with L1 loss.
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].
- **p. 4 / 4. CenterPoint - extractive body cue:** At inference time, we use this offset to associate current detections to past ones in a greedy fashion.
- **p. 1 / Abstract - extractive body cue:** On the Waymo Open Dataset, CenterPoint outperforms all previous single model method by a large margin and ranks first among all Lidar-only submissions.
- **Detected method headings:** 4.2. Architecture (p. 5); A. Tracking algorithm (p. 11); Method (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The 3D encoder then pools these features into its primary feature representation. | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | A point-based network [40] then extracts features for all points inside a bin. | p. 3 (3. Preliminaries), p. 4 (4. CenterPoint) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then, a 2D CNN architecture detection head finds object centers and regress to full 3D bounding boxes using center features. | p. 4 (4. CenterPoint), p. 5 (4.1. Two-Stage CenterPoint) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4. CenterPoint - extractive body cue:** CenterPoint combines all heatmap and regression losses in one common objective and jointly optimizes them.
- **p. 4 / 4.1. Two-Stage CenterPoint - extractive body cue:** The training is supervised with a binary cross entropy loss: Lscore = -It log(ˆIt) -(1 -It) log(1 -ˆIt) (2) 4
- **p. 2 / 1. Introduction - extractive body cue:** It recovers the lost local geometric information due to striding and a limited receptive field, and brings a decent performance boost with minor cost.
- **p. 3 / 3. Preliminaries - extractive body cue:** Without loss of generality, we use an egocentric coordinate system with sensor at (0, 0, 0) and yaw= 0.
- **p. 5 / 4.1. Two-Stage CenterPoint - extractive body cue:** For box regression, the model predicts a refinement on top of first stage proposals, and we train the model with L1 loss.
- **p. 2 / 1. Introduction - extractive body cue:** The center-based representation has several key advantages: First, unlike bounding boxes, points have no intrinsic orientation.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4. CenterPoint), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 5 (4.1. Two-Stage CenterPoint), p. 3 (4. CenterPoint).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, input, image, predicts, heatmap, classes, output, backbone, network, map-view, feature-map, width, length, channels | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | takes, input, image, predicts, heatmap, classes, output, backbone, network, map-view | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | marked, differences, between, detection, made, transfer, ideas, Anchor-based, Center-based, Figure | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | CenterPoint, combines, heatmap, regression, losses, common, objective, jointly, optimizes, them | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Preliminaries - extractive body cue:** It takes an input image and predicts a w × h heatmap ˆY ∈[0, 1]w×h×K for each of K classes.
- **p. 3 / 3. Preliminaries - extractive body cue:** The output of a backbone network is a map-view feature-map M ∈RW ×L×F of width W and length L with F channels in a map-view ...
- **p. 4 / 4. CenterPoint - extractive body cue:** The velocity estimate is special, as it requires two input map-views the current and previous time-step.
- **p. 4 / 4.1. Two-Stage CenterPoint - extractive body cue:** For each point, we extract a feature using bilinear interpolation from the backbone map-view output M.
- **p. 1 / 1. Introduction - extractive body cue:** Strong 3D perception is a core ingredient in many stateof-the-art driving systems [1, 50].
- **p. 1 / 1. Introduction - extractive body cue:** Second, the resulting output is a threedimensional box that is often not well aligned with any global coordinate frame.
- **p. 2 / 1. Introduction - extractive body cue:** For 3D tracking, our model performs at 63.8 AMOTA outperforming the prior state-of-the-art by 8.8 AMOTA on nuScenes.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each sequence is approximately 20-second long, with a Lidar frequency of 20 FPS. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our end-to-end 3D detection and tracking system runs near real-time, with 11 FPS on Waymo and 16 FPS on nuScenes. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each sequence is approximately 20-second long, with a Lidar frequency of 20 FPS. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Two-Stage CenterPoint - extractive body cue:** For box regression, the model predicts a refinement on top of first stage proposals, and we train the model with L1 loss.
- **p. 4 / 4. CenterPoint - extractive body cue:** At inference time, we use this offset to associate current detections to past ones in a greedy fashion.
- **p. 5 / 5. Experiments - extractive body cue:** The inference times are measured on an Intel Core i7 CPU and a Titan RTX GPU.
- **p. 5 / 5. Experiments - extractive body cue:** During inference, we run the second stage on the top 500 predictions after Non-Maxima Suppression (NMS).
- **p. 4 / 4. CenterPoint - extractive body cue:** At training time, only ground truth centers are supervised using an L1 regression loss.
- **p. 4 / 4. CenterPoint - extractive body cue:** At inference time, we use this offset to associate current detections to past ones in a greedy fashion.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** encoder, then, pools, features, primary, feature, representation, point-based, network, extracts, points, inside, CNN, architecture, detection, head, finds, object, centers, regress.
- **Relevant PDF headings:** 4.2. Architecture (p. 5); A. Tracking algorithm (p. 11); Method (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | CenterPoint-Voxel uses a (0.1m, 0.1m, 0.15m) voxel size following PV-RCNN [44] while CenterPoint-Pillar uses a grid size of (0.32m, 0.32m). nuScenes Dataset. ... | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Semantic / temporal fusion | Our velocity-based closest distance matching described in Section 4 significantly outperforms the official tracking baseline in the Waymo paper [48], which uses ... | p. 6 (5.1. Main Results), p. 6 (5.1. Main Results) |
| Robot query / planning handoff | More importantly, our model significantly outperforms all other submissions under the neural planar metric (PKL), a hidden metric evaluated by the organizers ... | p. 6 (5.1. Main Results), p. 6 (5.1. Main Results) |

## Failure and Ablation Link

- **p. 7 / 5.2. Ablation studies - extractive body cue:** Methods Vehicle Pedestrian Runtime BEV Feature 68.3 65.3 77ms w/ VSA [44] 68.3 65.2 98ms w/ RBF Interpolation [20,41] 68.4 65.7 89ms Table 10: Ablation ...
- **p. 7 / 5.2. Ablation studies - extractive body cue:** Effects of different feature components In our two-stage CenterPoint model, we only use features from the 2D CNN feature map.
- **p. 8 / 5.2. Ablation studies - extractive body cue:** More importantly, our tracking is a simple nearest neighbor matching without any hidden-state computation.
- **p. 8 / 5.2. Ablation studies - extractive body cue:** Detector Tracker AMOTA↑AMOTP↓Ttrack Ttot CenterPoint-Voxel Point 63.7 0.606 1ms 62ms CBGS [67] Point 59.8 0.682 1ms > 182ms CenterPoint-Voxel M-KF 60.0 0.765 73ms 135ms CBGS ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our CenterPoint framework. We rely on a standard 3D backbone that extracts map-view feature representation from Lidar point-clouds. Then, a 2D ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 14: Ablation studies for 3D detection on nuScenes validation. entries in the NeurIPS 2020 nuScenes detection challenge. In this section, we describe the details ...
- **p. 6 / 5.1. Main Results - extractive body cue:** Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on top of detection.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 5 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction), p. 4 (4. CenterPoint), objective p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 5 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction), temporal p. 5 (5. Experiments), p. 2 (1. Introduction), p. 5 (5. Experiments), p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), p. 7 (5.2. Ablation studies).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
