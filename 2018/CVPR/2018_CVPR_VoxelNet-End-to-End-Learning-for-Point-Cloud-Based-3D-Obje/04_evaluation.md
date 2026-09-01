# Evaluation - VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1711.06396; PDF retrieval source: https://arxiv.org/pdf/1711.06396. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.1. Evaluation on KITTI Validation Set), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 8 (4.1. Evaluation on KITTI Validation Set), p. 5 (2.3. Efficient Implementation), p. 2 (Figure/Table caption)): Specifically, using only LiDAR, VoxelNet significantly outperforms the

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive PDF cue:** We evaluate VoxelNet on the KITTI 3D object detection benchmark [11] which contains 7,481 training images/point clouds and 7,518 test images/point clouds, covering three categories: ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Since the ground truth for the test set is not available and the access to the test server is limited, we conduct comprehensive evaluation using ...
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive PDF cue:** We would like to note that [21] reported 88.9%, 77.3%, and 72.7% for easy, moderate, and hard levels respectively, but these results are obtained based ...
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive PDF cue:** We would like to note that many of the other leading methods listed in KITTI benchmark use both RGB images and LiDAR point clouds whereas ...
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive PDF cue:** The inference time for the VoxelNet is 225ms where the voxel input feature computation takes 5ms, feature learning net takes 20ms, convolutional middle layers take ...
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive PDF cue:** Evaluation in 3D Compared to the bird's eye view detection, which requires only accurate localization of objects in the 2D plane, 3D detection is a ...
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive PDF cue:** The IoU threshold is the same for both bird's eye view and full 3D evaluation.
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive PDF cue:** Metrics We follow the official KITTI evaluation protocol, where the IoU threshold is 0.7 for class Car and is 0.5 for class Pedestrian and Cyclist.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 2.3. Efficient Implementation (p. 5); 4. Experiments (p. 6); 4.1. Evaluation on KITTI Validation Set (p. 7); 4.2. Evaluation on KITTI Test Set (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Evaluation on KITTI Validation Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, using only LiDAR, VoxelNet significantly outperforms the | p. 7 (4.1. Evaluation on KITTI Validation Set) |
| 4.1. Evaluation on KITTI Validation Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the class Car, VoxelNet significantly outperforms all other approaches in AP across all difficulty levels. | p. 7 (4.1. Evaluation on KITTI Validation Set) |
| 4.2. Evaluation on KITTI Test Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | VoxelNet, significantly outperforms the previously published state-of-the-art [5] in all the tasks (bird's eye view and 3D detection) and all difficulties. | p. 8 (4.2. Evaluation on KITTI Test Set) |
| 4.1. Evaluation on KITTI Validation Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | HC-baseline achieves similar accuracy to the MV [5] method. | p. 8 (4.1. Evaluation on KITTI Validation Set) |
| 2.3. Efficient Implementation | EMPIRICAL / SOURCE-REPORTED EVALUATION | To further improve the memory/compute efficiency it is possible to only store a limited number of voxels (K) and ignore points coming from voxels ... | p. 5 (2.3. Efficient Implementation) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive PDF cue:** We evaluate VoxelNet on the KITTI 3D object detection benchmark [11] which contains 7,481 training images/point clouds and 7,518 test images/point clouds, covering three categories: ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Since the ground truth for the test set is not available and the access to the test server is limited, we conduct comprehensive evaluation using ...
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive PDF cue:** We would like to note that [21] reported 88.9%, 77.3%, and 72.7% for easy, moderate, and hard levels respectively, but these results are obtained based ...
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive PDF cue:** We would like to note that many of the other leading methods listed in KITTI benchmark use both RGB images and LiDAR point clouds whereas ...
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive PDF cue:** The inference time for the VoxelNet is 225ms where the voxel input feature computation takes 5ms, feature learning net takes 20ms, convolutional middle layers take ...
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive PDF cue:** Evaluation in 3D Compared to the bird's eye view detection, which requires only accurate localization of objects in the 2D plane, 3D detection is a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. VoxelNet directly operates on the raw point cloud (no need for feature engineering) and produces the 3D detection re- sults using a single ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. VoxelNet architecture. The feature learning network takes a raw point cloud as input, partitions the space into voxels, and transforms points within each ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Voxel feature encoding layer. point cloud is sparse and has highly variable point density throughout the space. Therefore, after grouping, a voxel will ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Region proposal network architecture. each fi with ˜f to form the point-wise concatenated feature as f out i = [f T i ,˜f ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Illustration of efficient implementation. mensions ∆l, ∆w, ∆h, and the rotation ∆θ, which are com- puted as: ∆x = xg c -xa c ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance comparison in bird's eye view detection: average precision (in %) on KITTI validation set.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Performance comparison in 3D detection: average precision (in %) on KITTI validation set. and a validation set, which results in 3,712 data samples ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Qualitative results. For better visualization 3D boxes detected using LiDAR are projected on to the RGB images. state-of-the-art method MV (BV+FV+RGB) [5] based ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate VoxelNet on the KITTI 3D object detection benchmark [11] which contains 7,481 training images/point clouds and 7,518 test images/point clouds, covering three ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Task/environment | Since the ground truth for the test set is not available and the access to the test server is limited, we conduct comprehensive evaluation ... | reset, timeout, object/scene variation | p. 6 (4. Experiments), p. 7 (4.1. Evaluation on KITTI Validation Set) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 4 (2.1. VoxelNet Architecture) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (2.1. VoxelNet Architecture), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The IoU threshold is the same for both bird's eye view and full 3D evaluation. | definition/direction/unit from same section | p. 7 (4.1. Evaluation on KITTI Validation Set) |
| Metrics We follow the official KITTI evaluation protocol, where the IoU threshold is 0.7 for class Car and is 0.5 for class Pedestrian and ... | definition/direction/unit from same section | p. 7 (4.1. Evaluation on KITTI Validation Set) |
| HC-baseline achieves similar accuracy to the MV [5] method. | definition/direction/unit from same section | p. 8 (4.1. Evaluation on KITTI Validation Set) |
| For each class, detection outcomes are evaluated based on three difficulty levels: easy, moderate, and hard, which are determined according to the object size, ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| As shown, VoxelNet provides highly accurate 3D bounding boxes in all categories. | definition/direction/unit from same section | p. 8 (4.2. Evaluation on KITTI Test Set) |
| Figure 1. VoxelNet directly operates on the raw point cloud (no need for feature engineering) and produces the 3D detection re- sults using a ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. VoxelNet architecture. The feature learning network takes a raw point cloud as input, partitions the space into voxels, and transforms points within ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| HC-baseline also achieves satisfactory performance compared to the state-of-the-art [5], which shows that our base region proposal network (RPN) is effective. | comparison identity and matched condition | p. 7 (4.1. Evaluation on KITTI Validation Set) |
| VoxelNet, significantly outperforms the previously published state-of-the-art [5] in all the tasks (bird's eye view and 3D detection) and all difficulties. | comparison identity and matched condition | p. 8 (4.2. Evaluation on KITTI Test Set) |
| Figure 6. Qualitative results. For better visualization 3D boxes detected using LiDAR are projected on to the RGB images. state-of-the-art method MV (BV+FV+RGB) [5] ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Specifically, using only LiDAR, VoxelNet significantly outperforms the | comparison identity and matched condition | p. 7 (4.1. Evaluation on KITTI Validation Set) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| • We propose a novel end-to-end trainable deep architecture for point-cloud-based 3D detection, VoxelNet, that directly operates on sparse 3D points and avoids information ... | Specifically, using only LiDAR, VoxelNet significantly outperforms the | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.1. Evaluation on KITTI Validation Set), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 8 (4.1. Evaluation on KITTI Validation Set), p. 5 (2.3. Efficient Implementation), p. 2 (Figure/Table caption) |
| Primary metric/result | For the class Car, VoxelNet significantly outperforms all other approaches in AP across all difficulty levels. | numeric claim only at cited anchor | p. 7 (4.1. Evaluation on KITTI Validation Set) |

- Numeric sentences retained from the body:
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive PDF cue:** The inference time for the VoxelNet is 225ms where the voxel input feature computation takes 5ms, feature learning net takes 20ms, convolutional middle layers take ...
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive PDF cue:** Performance evaluation on KITTI test set. and region proposal net takes 30ms on a TitanX GPU and 1.7Ghz CPU.
- **p. 5 / 2.2. Loss Function - extractive PDF cue:** Voxel Input Feature Buffer Voxel Coordinate Buffer K T 7 Sparse Tensor K 3 1 Voxel-wise Feature K C 1 Point Cloud Indexing Memory Copy ...
- **p. 5 / 3.1. Network Details - extractive PDF cue:** We choose a voxel size of vD = 0.4, vH = 0.2, vW = 0.2 meters, which leads to D′ = 10, H′ = 400, ...
- **p. 6 / 3.1. Network Details - extractive PDF cue:** Unlike [5], we use only one anchor size, la = 3.9, wa = 1.6, ha = 1.56 meters, centered at za c = -1.0 meters ...
- **p. 6 / 3.1. Network Details - extractive PDF cue:** We use anchor size la = 0.8, wa = 0.6, ha = 1.73 meters centered at za c = -0.6 meters with 0 and 90 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work includes extending VoxelNet for joint LiDAR and image based end-to-end 3D detection to further improve detection and localization accuracy. | p. 8 (5. Conclusion) |
| body limitation/failure cue | For each class, detection outcomes are evaluated based on three difficulty levels: easy, moderate, and hard, which are determined according to the object size, ... | p. 6 (4. Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During training, we use stochastic gradient descent (SGD) with learning rate 0.01 for the first 150 epochs and decrease the learning rate to 0.001 ... | p. 6 (3.1. Network Details) |
| After the voxel input buffer is constructed, the stacked VFE only involves point level and voxel level dense operations which can be computed on ... | p. 5 (2.3. Efficient Implementation) |
| Performance evaluation on KITTI test set. and region proposal net takes 30ms on a TitanX GPU and 1.7Ghz CPU. | p. 8 (4.2. Evaluation on KITTI Test Set) |
| The inference time for the VoxelNet is 225ms where the voxel input feature computation takes 5ms, feature learning net takes 20ms, convolutional middle layers ... | p. 8 (4.2. Evaluation on KITTI Test Set) |
| In this section, we explain the implementation details of the VoxelNet and the training procedure. | p. 5 (3. Training Details) |
| We first compute the local mean as the centroid of all the points in V, denoted as (vx, vy, vz). | p. 3 (2.1. VoxelNet Architecture) |
| Next, each ˆpi is transformed through the fully connected network (FCN) into a feature space, where we can aggregate information from the point features ... | p. 3 (2.1. VoxelNet Architecture) |
| All non-empty voxels are encoded in the same way and they share the same set of parameters in FCN. | p. 4 (2.1. VoxelNet Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work includes extending VoxelNet for joint LiDAR and image based end-to-end 3D detection to further improve detection and localization accuracy.
- **p. 6 / 4. Experiments - extractive PDF cue:** For each class, detection outcomes are evaluated based on three difficulty levels: easy, moderate, and hard, which are determined according to the object size, occlusion ...

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 7 (4.1. Evaluation on KITTI Validation Set), metrics p. 7 (4.1. Evaluation on KITTI Validation Set), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.1. Evaluation on KITTI Validation Set), p. 6 (4. Experiments), p. 8 (4.2. Evaluation on KITTI Test Set), p. 1 (Figure/Table caption), baselines p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 8 (Figure/Table caption), p. 7 (4.1. Evaluation on KITTI Validation Set), results p. 7 (4.1. Evaluation on KITTI Validation Set), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 8 (4.1. Evaluation on KITTI Validation Set), p. 5 (2.3. Efficient Implementation), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
