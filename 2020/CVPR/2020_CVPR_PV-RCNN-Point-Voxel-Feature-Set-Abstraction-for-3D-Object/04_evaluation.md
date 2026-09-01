# Evaluation - PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.13192; PDF retrieval source: https://arxiv.org/pdf/1912.13192. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption)): Table 4. Recall of different proposal generation networks on the car class at moderate difficulty level of the KITTI val split set. For the most important 3D object detection benchmark ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** It annotated the objects in the full 360◦field instead of 90◦in KITTI dataset.
- **p. 7 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** For the most important 3D object detection benchmark of the car class, our method outperforms previous state-of-theart methods with remarkable margins, i.e. increasing the mAP ...
- **p. 8 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** Performance comparison on the Waymo Open Dataset (version 1.0 released in August, 2019) with 202 validation sequences for the vehicle detection.
- **p. 8 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** Performance comparison on the Waymo Open Dataset (version 1.2 released in March 2020) with 202 validation sequences for three categories. †: re-implemented by ourselves with ...
- **p. 6 / 4. Experiments - extractive PDF cue:** 4.2) and the newly introduced large-scale Waymo Open Dataset [20, 40] (Sec.
- **p. 7 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** To conduct evaluation on the test set with the KITTI official test server, the model is trained with 80% of all available train+val data and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Performance comparison on the moderate level car class of KITTI val split with mAP calculated by 11 recall positions. mentation [34] to randomly ...
- **p. 8 / 4.3. 3D Detection on the Waymo Open Dataset - extractive PDF cue:** The results show that our method achieves remarkably better mAP on all distance ranges of interest, where the maximum gain is 9.19% for the 3D ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. 3D Detection on the KITTI Dataset (p. 7); 4.3. 3D Detection on the Waymo Open Dataset (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Recall of different proposal generation networks on the car class at moderate difficulty level of the KITTI val split set. For the ... | p. 7 (Figure/Table caption) |
| 4.3. 3D Detection on the Waymo Open Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | The results show that our method achieves remarkably better mAP on all distance ranges of interest, where the maximum gain is 9.19% for the ... | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |
| 4.2. 3D Detection on the KITTI Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | For 3D detection and bird-view detection of cyclist, our methods outperforms previous LiDAR-only methods with large margins on the moderate and hard difficulty levels ... | p. 7 (4.2. 3D Detection on the KITTI Dataset) |
| 4.3. 3D Detection on the Waymo Open Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown in Table 5, our method also achieves superior performance in terms of mAPH, which demonstrates that our model predicted accurate heading direction ... | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Our proposed PV-RCNN framework deeply integrates both the voxel-based and the PointNet-based networks via a two- step strategy including the voxel-to-keypoint 3D ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** It annotated the objects in the full 360◦field instead of 90◦in KITTI dataset.
- **p. 7 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** For the most important 3D object detection benchmark of the car class, our method outperforms previous state-of-theart methods with remarkable margins, i.e. increasing the mAP ...
- **p. 8 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** Performance comparison on the Waymo Open Dataset (version 1.0 released in August, 2019) with 202 validation sequences for the vehicle detection.
- **p. 8 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** Performance comparison on the Waymo Open Dataset (version 1.2 released in March 2020) with 202 validation sequences for three categories. †: re-implemented by ourselves with ...
- **p. 6 / 4. Experiments - extractive PDF cue:** 4.2) and the newly introduced large-scale Waymo Open Dataset [20, 40] (Sec.
- **p. 7 / 4.2. 3D Detection on the KITTI Dataset - extractive PDF cue:** To conduct evaluation on the test set with the KITTI official test server, the model is trained with 80% of all available train+val data and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Our proposed PV-RCNN framework deeply integrates both the voxel-based and the PointNet-based networks via a two- step strategy including the voxel-to-keypoint 3D scene ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The overall architecture of our proposed PV-RCNN. The raw point clouds are first voxelized to feed into the 3D sparse convolution based encoder ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Illustration of Predicted Keypoint Weighting module. maps. Hence, the keypoint feature for pi is further enriched by concatenating all its associated features f ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Illustration of RoI-grid pooling module. Rich context information of each 3D RoI is aggregated by the set abstraction operation with multiple receptive fields. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance comparison on the KITTI test set. The results are evaluated by the mean Average Precision with 40 recall positions.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Performance comparison on the moderate level car class of KITTI val split with mAP calculated by 11 recall positions. mentation [34] to randomly ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Performance on the KITTI val split set with mAP calcu- lated by 40 recall positions for car class.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Recall of different proposal generation networks on the car class at moderate difficulty level of the KITTI val split set. For the most ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It annotated the objects in the full 360◦field instead of 90◦in KITTI dataset. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 7 (4.2. 3D Detection on the KITTI Dataset) |
| Task/environment | For the most important 3D object detection benchmark of the car class, our method outperforms previous state-of-theart methods with remarkable margins, i.e. increasing the ... | reset, timeout, object/scene variation | p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.2. 3D Detection on the KITTI Dataset) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. Performance comparison on the moderate level car class of KITTI val split with mAP calculated by 11 recall positions. mentation [34] to ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| The results show that our method achieves remarkably better mAP on all distance ranges of interest, where the maximum gain is 9.19% for the ... | definition/direction/unit from same section | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |
| For the proposal refinement stage, we randomly sample 128 proposals with 1:1 ratio for positive and negative proposals, where a proposal is considered as ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Method PointRCNN [25] STD [37] PV-RCNN (Ours) Recall (IoU=0.7) 74.8 76.8 85.5 Table 4. | definition/direction/unit from same section | p. 7 (4.2. 3D Detection on the KITTI Dataset) |
| Difficulty Method 3D mAP (IoU=0.7) 3D mAPH (IoU=0.7) BEV mAP (IoU=0.7) BEV mAPH (IoU=0.7) Overall 0-30m 30-50m 50m-Inf Overall 0-30m 30-50m 50m-Inf Overall 0-30m ... | definition/direction/unit from same section | p. 8 (4.2. 3D Detection on the KITTI Dataset) |
| Table 9. Effects of predicted keypoint weighting module, RoI-grid pooling module and IoU-guided confidence prediction. keypoints by the new proposed voxel set abstraction layer, ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 1. Our proposed PV-RCNN framework deeply integrates both the voxel-based and the PointNet-based networks via a two- step strategy including the voxel-to-keypoint 3D ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The cosine annealing learning rate strategy is adopted for the learning rate decay. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We hope it could set up a strong baseline on the Waymo Open Dataset for future works. | comparison identity and matched condition | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |
| 4.1) and compare with previous state-of-the-art methods on both the highly competitive KITTI dataset [4] (Sec. | comparison identity and matched condition | p. 6 (4. Experiments) |
| We compare PV-RCNN with state-of-the-art methods on both the val split and the test split on the online learderboard. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Similarly, as shown in Table 2, our method outperforms previous stateof-the-art methods with large margins. | comparison identity and matched condition | p. 7 (4.2. 3D Detection on the KITTI Dataset) |
| For 3D detection and bird-view detection of cyclist, our methods outperforms previous LiDAR-only methods with large margins on the moderate and hard difficulty levels ... | comparison identity and matched condition | p. 7 (4.2. 3D Detection on the KITTI Dataset) |
| Hard RPN Baseline ✓ 90.46 80.87 77.30 Pool from Encoder ✓ ✓ 91.88 82.86 80.52 PV-RCNN ✓ ✓ ✓ 92.57 84.83 82.69 Table 7. | comparison identity and matched condition | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.4, we conduct extensive ablation studies to investigate each component of PV-RCNN to validate our design. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Effects of different feature components for VSA module. our proposed framework on various datasets. | component/input/data sensitivity | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a novel 3D object detection framework, PVRCNN (Illustrated in Fig. | Table 4. Recall of different proposal generation networks on the car class at moderate difficulty level of the KITTI val split set. For the ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Primary metric/result | The results show that our method achieves remarkably better mAP on all distance ranges of interest, where the maximum gain is 9.19% for the ... | numeric claim only at cited anchor | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** There are 7, 481 training samples and 7, 518 test samples, where the training samples are generally divided into the train split (3, 712 samples) ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For the KITTI dataset, we train the entire network with the batch size 24, learning rate 0.01 for 80 epochs on 8 GTX 1080 Ti ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For the Waymo Open Dataset, we train the entire network with batch size 64, learning rate 0.01 for 30 epochs on 32 GTX 1080 Ti ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We hope it could set up a strong baseline on the Waymo Open Dataset for future works. | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For the Waymo Open Dataset, we train the entire network with batch size 64, learning rate 0.01 for 30 epochs on 32 GTX 1080 ... | p. 6 (4.1. Experimental Setup) |
| The cosine annealing learning rate strategy is adopted for the learning rate decay. | p. 6 (4.1. Experimental Setup) |
| Hard RPN Baseline ✓ 90.46 80.87 77.30 Pool from Encoder ✓ ✓ 91.88 82.86 80.52 PV-RCNN ✓ ✓ ✓ 92.57 84.83 82.69 Table 7. | p. 8 (4.3. 3D Detection on the Waymo Open Dataset) |
| Performance comparison on the Waymo Open Dataset (version 1.2 released in March 2020) with 202 validation sequences for three categories. †: re-implemented by ourselves ... | p. 8 (4.2. 3D Detection on the KITTI Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. 3D Detection on the Waymo Open Dataset - extractive PDF cue:** We hope it could set up a strong baseline on the Waymo Open Dataset for future works.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.2. 3D Detection on the KITTI Dataset), p. 6 (4. Experiments), p. 7 (4.2. 3D Detection on the KITTI Dataset), metrics p. 7 (Figure/Table caption), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 6 (4.1. Experimental Setup), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.2. 3D Detection on the KITTI Dataset), p. 9 (Figure/Table caption), baselines p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 6 (4. Experiments), p. 6 (4.1. Experimental Setup), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), results p. 7 (Figure/Table caption), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 7 (4.2. 3D Detection on the KITTI Dataset), p. 8 (4.3. 3D Detection on the Waymo Open Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
