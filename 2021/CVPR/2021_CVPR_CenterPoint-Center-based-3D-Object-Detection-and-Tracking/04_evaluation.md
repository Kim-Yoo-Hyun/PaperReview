# Evaluation - CenterPoint: Center-based 3D Object Detection and Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.11275; PDF retrieval source: https://arxiv.org/pdf/2006.11275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), p. 12 (Figure/Table caption), p. 7 (5.2. Ablation studies), p. 7 (5.2. Ablation studies), p. 5 (5.1. Main Results)): More importantly, our model significantly outperforms all other submissions under the neural planar metric (PKL), a hidden metric evaluated by the organizers after our leaderboard submission.

## Evaluation Body Digest

- **p. 5 / 5. Experiments - extractive body cue:** CenterPoint-Voxel uses a (0.1m, 0.1m, 0.15m) voxel size following PV-RCNN [44] while CenterPoint-Pillar uses a grid size of (0.32m, 0.32m). nuScenes Dataset. nuScenes [6] contains ...
- **p. 5 / 5. Experiments - extractive body cue:** We evaluate CenterPoint on Waymo Open Dataset and nuScenes dataset.
- **p. 7 / 5.2. Ablation studies - extractive body cue:** We think the reason is that the nuScenes dataset uses 32 lanes Lidar, which produces about 30k Lidar points per frame, about 1 6 of ...
- **p. 7 / 5.2. Ablation studies - extractive body cue:** We also divide the dataset into three splits: small, medium, and large, and each split contains 1 3 of the overall ground truth boxes.
- **p. 6 / 5.1. Main Results - extractive body cue:** [10] 55.0 17533 33216 950 Ours 63.8 18612 22928 760 Table 4: State-of-the-art comparisons for 3D tracking on nuScenes test set.
- **p. 6 / 5.1. Main Results - extractive body cue:** Method mAP↑ NDS↑ PKL↓ WYSIWYG [23] 35.0 41.9 1.14 PointPillars [28] 40.1 55.0 1.00 CVCNet [7] 55.3 64.4 0.92 PointPainting [49] 46.4 58.1 0.89 PMPNet ...
- **p. 8 / 5.2. Ablation studies - extractive body cue:** Detector Tracker AMOTA↑AMOTP↓Ttrack Ttot CenterPoint-Voxel Point 63.7 0.606 1ms 62ms CBGS [67] Point 59.8 0.682 1ms > 182ms CenterPoint-Voxel M-KF 60.0 0.765 73ms 135ms CBGS ...
- **p. 8 / 5.2. Ablation studies - extractive body cue:** To compare with prior work that did not evaluate on Waymo test, we also report results on the Waymo validation split in Table 11.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Main Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | More importantly, our model significantly outperforms all other submissions under the neural planar metric (PKL), a hidden metric evaluated by the organizers after our ... | p. 6 (5.1. Main Results) |
| 5.1. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our velocity-based closest distance matching described in Section 4 significantly outperforms the official tracking baseline in the Waymo paper [48], which uses a Kalman-filter ... | p. 6 (5.1. Main Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 14: Ablation studies for 3D detection on nuScenes validation. entries in the NeurIPS 2020 nuScenes detection challenge. In this section, we describe the ... | p. 12 (Figure/Table caption) |
| 5.2. Ablation studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also compare with RoIAlign, which densely samples 6 × 6 points in the RoI [44, 46], our center-based feature aggregation achieved comparable performance ... | p. 7 (5.2. Ablation studies) |
| 5.2. Ablation studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | To understand where the improvements are from, we further show the performance breakdown on different subsets based on object sizes and orientation angles on ... | p. 7 (5.2. Ablation studies) |

## Dataset / Benchmark Role

- **p. 5 / 5. Experiments - extractive body cue:** CenterPoint-Voxel uses a (0.1m, 0.1m, 0.15m) voxel size following PV-RCNN [44] while CenterPoint-Pillar uses a grid size of (0.32m, 0.32m). nuScenes Dataset. nuScenes [6] contains ...
- **p. 5 / 5. Experiments - extractive body cue:** We evaluate CenterPoint on Waymo Open Dataset and nuScenes dataset.
- **p. 7 / 5.2. Ablation studies - extractive body cue:** We think the reason is that the nuScenes dataset uses 32 lanes Lidar, which produces about 30k Lidar points per frame, about 1 6 of ...
- **p. 7 / 5.2. Ablation studies - extractive body cue:** We also divide the dataset into three splits: small, medium, and large, and each split contains 1 3 of the overall ground truth boxes.
- **p. 6 / 5.1. Main Results - extractive body cue:** [10] 55.0 17533 33216 950 Ours 63.8 18612 22928 760 Table 4: State-of-the-art comparisons for 3D tracking on nuScenes test set.
- **p. 6 / 5.1. Main Results - extractive body cue:** Method mAP↑ NDS↑ PKL↓ WYSIWYG [23] 35.0 41.9 1.14 PointPillars [28] 40.1 55.0 1.00 CVCNet [7] 55.3 64.4 0.92 PointPainting [49] 46.4 58.1 0.89 PMPNet ...
- **p. 8 / 5.2. Ablation studies - extractive body cue:** Detector Tracker AMOTA↑AMOTP↓Ttrack Ttot CenterPoint-Voxel Point 63.7 0.606 1ms 62ms CBGS [67] Point 59.8 0.682 1ms > 182ms CenterPoint-Voxel M-KF 60.0 0.765 73ms 135ms CBGS ...
- **p. 8 / 5.2. Ablation studies - extractive body cue:** To compare with prior work that did not evaluate on Waymo test, we also report results on the Waymo validation split in Table 11.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We present a center-based framework to represent, detect and track objects. Previous anchor-based methods use axis-aligned anchors with respect to ego-vehicle coordinate. When ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our CenterPoint framework. We rely on a standard 3D backbone that extracts map-view feature representation from Lidar point-clouds. Then, a 2D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: State-of-the-art comparisons for 3D detection on Waymo test set. We show the mAP and mAPH for both level 1 and level 2 benchmarks.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: State-of-the-art comparisons for 3D detection on nuScenes test set. We show the nuScenes detection score (NDS), and mean Average Precision (mAP). Difficulty
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: State-of-the-art comparisons for 3D tracking on Waymo test set. We show MOTA, and MOTP. ↑is for higher better and ↓is for lower better. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4: State-of-the-art comparisons for 3D tracking on nuScenes test set. We show AMOTA, the number of false positives (FP), false negatives (FN), id switches ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 5: Comparison between anchor-based and center- based methods for 3D detection on Waymo validation. We show the per-calss and average LEVEL 2 mAPH. Encoder
- **p. 6 / Figure/Table caption - extractive body cue:** Table 6: Comparison between anchor-based and center- based methods for 3D detection on nuScenes validation. We show mean average precision (mAP) and nuScenes detection score ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | CenterPoint-Voxel uses a (0.1m, 0.1m, 0.15m) voxel size following PV-RCNN [44] while CenterPoint-Pillar uses a grid size of (0.32m, 0.32m). nuScenes Dataset. nuScenes [6] ... | embodiment, simulator version and control stack | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Task/environment | We evaluate CenterPoint on Waymo Open Dataset and nuScenes dataset. | reset, timeout, object/scene variation | p. 5 (5. Experiments), p. 7 (5.2. Ablation studies) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 2: Overview of our CenterPoint framework. We rely on a standard 3D backbone that extracts map-view feature representation from Lidar point-clouds. Then, a ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| For 3D detection, the main metrics are mean Average Precision (mAP) [13] and nuScenes detection score (NDS). | definition/direction/unit from same section | p. 5 (5. Experiments) |
| The official 3D detection evaluation metrics include the standard 3D bounding box mean average precision (mAP) and mAP weighted by heading accuracy (mAPH). | definition/direction/unit from same section | p. 5 (5. Experiments) |
| There are two sources of improvements: 1) we model the object motion with a learned point velocity, rather than modeling 3D bounding box dynamic ... | definition/direction/unit from same section | p. 8 (5.2. Ablation studies) |
| On Waymo, we follow the state-ofthe-art PV-RCNN [44] to set the anchor hyper-parameters: we use two anchors per-locations with 0°and 90°; The positive/ negative ... | definition/direction/unit from same section | p. 6 (5.2. Ablation studies) |
| We compare bird-eye view and 3D voxel features using LEVEL 2 mAPH on Waymo validation. ment with multiple center features gives a large accuracy ... | definition/direction/unit from same section | p. 7 (5.2. Ablation studies) |
| Our model displays a consistent performance improvement over all categories and shows more significant improvements in small categories (+5.6 mAP for traffic cone) and ... | definition/direction/unit from same section | p. 6 (5.1. Main Results) |
| Effects of different feature components In our two-stage CenterPoint model, we only use features from the 2D CNN feature map. | definition/direction/unit from same section | p. 7 (5.2. Ablation studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our velocity-based closest distance matching described in Section 4 significantly outperforms the official tracking baseline in the Waymo paper [48], which uses a Kalman-filter ... | comparison identity and matched condition | p. 6 (5.1. Main Results) |
| [10] 55.0 17533 33216 950 Ours 63.8 18612 22928 760 Table 4: State-of-the-art comparisons for 3D tracking on nuScenes test set. | comparison identity and matched condition | p. 6 (5.1. Main Results) |
| [24] 63.6 AFDet [14] 63.7 CVCNet [7] 65.2 Pillar-OD [52] 69.8 72.5 PV-RCNN [44] 74.4 73.8 61.4 53.4 CenterPoint-Pillar(ours) 76.1 75.5 76.1 65.1 CenterPoint-Voxel(ours) ... | comparison identity and matched condition | p. 8 (5.2. Ablation studies) |
| On nuScenes (Table 2), our model outperforms the last-year challenge winner CBGS [67] with multi-scale inputs and multi-model ensemble by 5.2% mAP and 2.2% ... | comparison identity and matched condition | p. 5 (5.1. Main Results) |
| Here, we compare with two voxel feature extraction baselines: Voxel-Set Abstraction. | comparison identity and matched condition | p. 7 (5.2. Ablation studies) |
| Our centerbased detectors perform much better than the anchor-based baseline when the box is rotated or deviates from the average box size, demonstrating the ... | comparison identity and matched condition | p. 7 (5.2. Ablation studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Methods Vehicle Pedestrian Runtime BEV Feature 68.3 65.3 77ms w/ VSA [44] 68.3 65.2 98ms w/ RBF Interpolation [20,41] 68.4 65.7 89ms Table 10: ... | component/input/data sensitivity | p. 7 (5.2. Ablation studies) |
| Effects of different feature components In our two-stage CenterPoint model, we only use features from the 2D CNN feature map. | component/input/data sensitivity | p. 7 (5.2. Ablation studies) |
| More importantly, our tracking is a simple nearest neighbor matching without any hidden-state computation. | component/input/data sensitivity | p. 8 (5.2. Ablation studies) |
| Detector Tracker AMOTA↑AMOTP↓Ttrack Ttot CenterPoint-Voxel Point 63.7 0.606 1ms 62ms CBGS [67] Point 59.8 0.682 1ms > 182ms CenterPoint-Voxel M-KF 60.0 0.765 73ms 135ms ... | component/input/data sensitivity | p. 8 (5.2. Ablation studies) |
| Figure 2: Overview of our CenterPoint framework. We rely on a standard 3D backbone that extracts map-view feature representation from Lidar point-clouds. Then, a ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Table 14: Ablation studies for 3D detection on nuScenes validation. entries in the NeurIPS 2020 nuScenes detection challenge. In this section, we describe the ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based ... | More importantly, our model significantly outperforms all other submissions under the neural planar metric (PKL), a hidden metric evaluated by the organizers after our ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), p. 12 (Figure/Table caption), p. 7 (5.2. Ablation studies), p. 7 (5.2. Ablation studies), p. 5 (5.1. Main Results) |
| Primary metric/result | Our velocity-based closest distance matching described in Section 4 significantly outperforms the official tracking baseline in the Waymo paper [48], which uses a Kalman-filter ... | numeric claim only at cited anchor | p. 6 (5.1. Main Results) |

- Numeric sentences retained from the body:
- **p. 5 / 5. Experiments - extractive body cue:** The point-clouds are captured with a 64 lanes Lidar, which produces about 180k Lidar points every 0.1s.
- **p. 5 / 5. Experiments - extractive body cue:** Each sequence is approximately 20-second long, with a Lidar frequency of 20 FPS.
- **p. 5 / 5. Experiments - extractive body cue:** The dataset provides calibrated vehicle pose information for each Lidar frame but only provides box annotations every ten frames (0.5s). nuScenes uses a 32 lanes ...
- **p. 6 / 5.1. Main Results - extractive body cue:** Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on top of detection.
- **p. 7 / 5.2. Ablation studies - extractive body cue:** Tproposal Trefine VoxelNet First Stage 66.5 62.7 71ms + Box Center 68.0 64.9 71ms 5ms + Surface Center 68.3 65.3 71ms 6ms Dense Sampling 68.2 ...
- **p. 7 / 5.2. Ablation studies - extractive body cue:** Methods Vehicle Pedestrian Runtime BEV Feature 68.3 65.3 77ms w/ VSA [44] 68.3 65.2 98ms w/ RBF Interpolation [20,41] 68.4 65.7 89ms Table 10: Ablation ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on top of detection. | p. 6 (5.1. Main Results) |
| body limitation/failure cue | Two-stage refinement does not bring an improvement over the single-stage CenterPoint model on nuScenes in our experiments. | p. 7 (5.2. Ablation studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The inference times are measured on an Intel Core i7 CPU and a Titan RTX GPU. | p. 5 (5. Experiments) |
| During inference, we run the second stage on the top 500 predictions after Non-Maxima Suppression (NMS). | p. 5 (5. Experiments) |
| Encoder Method mAP NDS VoxelNet Anchor-based 52.6 63.0 Center-based 56.4 64.8 PointPillars Anchor-based 46.2 59.1 Center-based 50.3 60.2 Table 6: Comparison between anchor-based and ... | p. 6 (5.1. Main Results) |
| Two-stage refineEncoder Method Vehicle Ped. | p. 7 (5.2. Ablation studies) |
| As is shown in Table 5, on Waymo dataset, simply switching from anchors to our centers gives 4.3 mAPH and 4.5 mAPH improvements for ... | p. 7 (5.2. Ablation studies) |
| For both baselines, we combine bird-eye view features with voxel features using their official implementations. | p. 8 (5.2. Ablation studies) |
| At training time, only ground truth centers are supervised using an L1 regression loss. | p. 4 (4. CenterPoint) |
| At inference time, we use this offset to associate current detections to past ones in a greedy fashion. | p. 4 (4. CenterPoint) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.1. Main Results - extractive body cue:** Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on top of detection.
- **p. 7 / 5.2. Ablation studies - extractive body cue:** Two-stage refinement does not bring an improvement over the single-stage CenterPoint model on nuScenes in our experiments.

- **Evidence anchors reviewed:** datasets p. 5 (5. Experiments), p. 5 (5. Experiments), p. 7 (5.2. Ablation studies), p. 7 (5.2. Ablation studies), p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), metrics p. 4 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 8 (5.2. Ablation studies), p. 6 (5.2. Ablation studies), p. 7 (5.2. Ablation studies), baselines p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), p. 8 (5.2. Ablation studies), p. 5 (5.1. Main Results), p. 7 (5.2. Ablation studies), p. 7 (5.2. Ablation studies), results p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), p. 12 (Figure/Table caption), p. 7 (5.2. Ablation studies), p. 7 (5.2. Ablation studies), p. 5 (5.1. Main Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
