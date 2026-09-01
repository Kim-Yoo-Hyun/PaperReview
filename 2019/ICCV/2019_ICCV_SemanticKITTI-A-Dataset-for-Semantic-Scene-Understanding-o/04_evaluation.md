# Evaluation - SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.01416; PDF retrieval source: https://arxiv.org/pdf/1904.01416. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Multiple Scan Experiments), p. 8 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 4 (3.1. Labeling Process), p. 4 (4.1. Single Scan Experiments), p. 6 (4.2. Multiple Scan Experiments)): In this task, we allow methods to exploit information from a sequence of multiple past scans to improve the segmentation of the current scan.

## Evaluation Body Digest

- **p. 3 / 3. The SemanticKITTI Dataset - extractive PDF cue:** The dataset is publicly available through a benchmark website and we provide only the training set with ground truth labels and perform the test set ...
- **p. 3 / 3. The SemanticKITTI Dataset - extractive PDF cue:** Our dataset is based on the odometry dataset of the KITTI Vision Benchmark [19] showing inner city traffic, residential areas, but also highway scenes and ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** However, a dataset combining the scale of a synthetic dataset and usage of real-world data is still missing.
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** [49], our dataset for the scene completion task is a voxelized representation of the 3D scene.
- **p. 4 / 3.2. Dataset Statistics - extractive PDF cue:** The unbalanced count of classes is common for datasets captured in natural environments and some classes will be always under-represented, since they do not occur ...
- **p. 4 / 3.1. Labeling Process - extractive PDF cue:** We explicitly did not use bounding boxes or other available annotations for the KITTI dataset, since we want to ensure that the labeling is consistent ...
- **p. 6 / 4.2. Multiple Scan Experiments - extractive PDF cue:** In this task, we allow methods to exploit information from a sequence of multiple past scans to improve the segmentation of the current scan.
- **p. 6 / 4.2. Multiple Scan Experiments - extractive PDF cue:** For each method, we show in the upper part of the row the IoU for non-moving (unshaded) and in the lower part of the row ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3. The SemanticKITTI Dataset (p. 3); 3.2. Dataset Statistics (p. 4); 4. Evaluation of Semantic Segmentation (p. 4); 4.1. Single Scan Experiments (p. 4); 4.2. Multiple Scan Experiments (p. 6); 5. Evaluation of Semantic Scene Completion (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Multiple Scan Experiments | BENCHMARK / DATASET | In this task, we allow methods to exploit information from a sequence of multiple past scans to improve the segmentation of the current scan. | p. 6 (4.2. Multiple Scan Experiments) |
| 5. Evaluation of Semantic Scene Completion | BENCHMARK / DATASET | This has minimal impact on the performance, but significantly speeds up the training time due to faster preprocessing [18]. | p. 8 (5. Evaluation of Semantic Scene Completion) |
| 5. Evaluation of Semantic Scene Completion | BENCHMARK / DATASET | However, the usage of the best semantic segmentation directly working on the point cloud slightly outperforms SSCNet on semantic scene completion (TS3D + DarkNet53Seg). | p. 8 (5. Evaluation of Semantic Scene Completion) |
| 3.1. Labeling Process | BENCHMARK / DATASET | We provided regular feedback to the annotators to improve the quality and accuracy of labels. | p. 4 (3.1. Labeling Process) |
| 4.1. Single Scan Experiments | BENCHMARK / DATASET | To assess the labeling performance, we rely on the commonly applied mean Jaccard Index or mean intersectionover-union (mIoU) metric [15] over all classes, given ... | p. 4 (4.1. Single Scan Experiments) |

## Dataset / Benchmark Role

- **p. 3 / 3. The SemanticKITTI Dataset - extractive PDF cue:** The dataset is publicly available through a benchmark website and we provide only the training set with ground truth labels and perform the test set ...
- **p. 3 / 3. The SemanticKITTI Dataset - extractive PDF cue:** Our dataset is based on the odometry dataset of the KITTI Vision Benchmark [19] showing inner city traffic, residential areas, but also highway scenes and ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** However, a dataset combining the scale of a synthetic dataset and usage of real-world data is still missing.
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** [49], our dataset for the scene completion task is a voxelized representation of the 3D scene.
- **p. 4 / 3.2. Dataset Statistics - extractive PDF cue:** The unbalanced count of classes is common for datasets captured in natural environments and some classes will be always under-represented, since they do not occur ...
- **p. 4 / 3.1. Labeling Process - extractive PDF cue:** We explicitly did not use bounding boxes or other available annotations for the KITTI dataset, since we want to ensure that the labeling is consistent ...
- **p. 6 / 4.2. Multiple Scan Experiments - extractive PDF cue:** In this task, we allow methods to exploit information from a sequence of multiple past scans to improve the segmentation of the current scan.
- **p. 6 / 4.2. Multiple Scan Experiments - extractive PDF cue:** For each method, we show in the upper part of the row the IoU for non-moving (unshaded) and in the lower part of the row ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Our dataset provides dense annotations for each scan of all sequences from the KITTI Odometry Benchmark [19]. Here, we show multiple scans aggregated ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1: Overview of other point cloud datasets with semantic annotations. Ours is by far the largest dataset with sequential information. 1Number of scans for ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Single scan (top) and multiple superimposed scans with labels (bottom). Also shown is a moving car in the center of the image resulting ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Label distribution. The number of labeled points per class and the root categories for the classes are shown. For movable classes, we also ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Single scan results (19 classes) for all baselines on sequences 11 to 21 (test set). All methods were trained on sequences 00 to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: IoU vs. distance to the sensor. Another reason is that the point clouds generated by Li- DAR are relatively sparse, especially as the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: IoU results using a sequence of multiple past scans (in %). Shaded cells correspond to the IoU of the moving classes, while unshaded ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Left: Visualization of the incomplete input for the semantic scene completion benchmark. Note that we show the labels only for better visualization, but ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset is publicly available through a benchmark website and we provide only the training set with ground truth labels and perform the test ... | embodiment, simulator version and control stack | p. 3 (3. The SemanticKITTI Dataset), p. 3 (3. The SemanticKITTI Dataset) |
| Task/environment | Our dataset is based on the odometry dataset of the KITTI Vision Benchmark [19] showing inner city traffic, residential areas, but also highway scenes ... | reset, timeout, object/scene variation | p. 3 (3. The SemanticKITTI Dataset), p. 7 (5. Evaluation of Semantic Scene Completion) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 7 (Approach), p. 6 (Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| [49] and compute the IoU for the task of scene completion, which only classifies a voxel as being occupied or empty, i.e., ignoring the ... | definition/direction/unit from same section | p. 7 (5. Evaluation of Semantic Scene Completion) |
| Due to Completion Semantic Scene (IoU) Completion (mIoU) SSCNet [49] 29.83 9.53 TS3D [18] 29.81 9.54 TS3D [18] + DarkNet53Seg 24.99 10.19 TS3D [18] ... | definition/direction/unit from same section | p. 8 (5. Evaluation of Semantic Scene Completion) |
| Figure 4: IoU vs. distance to the sensor. Another reason is that the point clouds generated by Li- DAR are relatively sparse, especially as ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 9: Results for scene completion and class-wise results for semantic scene completion (in %). G. Qualitative Results Figure 8 shows qualitative results for ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| For each method, we show in the upper part of the row the IoU for non-moving (unshaded) and in the lower part of the ... | definition/direction/unit from same section | p. 6 (4.2. Multiple Scan Experiments) |
| Table 4: IoU results using a sequence of multiple past scans (in %). Shaded cells correspond to the IoU of the moving classes, while ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 8: IoU results using a sequence of multiple past scans (in %). Scene Completion Semantic Scene Completion | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| We provided regular feedback to the annotators to improve the quality and accuracy of labels. | definition/direction/unit from same section | p. 4 (3.1. Labeling Process) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| However, the usage of the best semantic segmentation directly working on the point cloud slightly outperforms SSCNet on semantic scene completion (TS3D + DarkNet53Seg). | comparison identity and matched condition | p. 8 (5. Evaluation of Semantic Scene Completion) |
| Due to Completion Semantic Scene (IoU) Completion (mIoU) SSCNet [49] 29.83 9.53 TS3D [18] 29.81 9.54 TS3D [18] + DarkNet53Seg 24.99 10.19 TS3D [18] ... | comparison identity and matched condition | p. 8 (5. Evaluation of Semantic Scene Completion) |
| Compared to image-based annotation, the annotation process with point clouds is more complex, since the annotator often needs to change the viewpoint. | comparison identity and matched condition | p. 4 (3.1. Labeling Process) |
| Table 2: Single scan results (19 classes) for all baselines on sequences 11 to 21 (test set). All methods were trained on sequences 00 ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 7: Approach statistics. ∗in number of epochs means that it was started from the pretrained weights of the single scan version. while being ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| We evaluate DarkNet53Seg and TangentConv, since these approaches can deal with a larger number of points without downsampling of the point clouds and could ... | comparison identity and matched condition | p. 6 (4.2. Multiple Scan Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate DarkNet53Seg and TangentConv, since these approaches can deal with a larger number of points without downsampling of the point clouds and could ... | component/input/data sensitivity | p. 6 (4.2. Multiple Scan Experiments) |
| Early approaches addressed the task of scene completion either without predicting semantics [16], thereby not providing a holistic understanding of the scene, or by ... | component/input/data sensitivity | p. 7 (5. Evaluation of Semantic Scene Completion) |
| In the first approach, we apply SSCNet [49] without the flipped TSDF as input feature. | component/input/data sensitivity | p. 8 (5. Evaluation of Semantic Scene Completion) |
| Note that we show the labels only for better visualization, but the real input is a single raw voxel grid without any labels. | component/input/data sensitivity | p. 8 (5. Evaluation of Semantic Scene Completion) |
| Table 7: Approach statistics. ∗in number of epochs means that it was started from the pretrained weights of the single scan version. while being ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are: • We present a point-wise annotated dataset of point cloud sequences with an unprecedented number of classes and ... | In this task, we allow methods to exploit information from a sequence of multiple past scans to improve the segmentation of the current scan. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Multiple Scan Experiments), p. 8 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 4 (3.1. Labeling Process), p. 4 (4.1. Single Scan Experiments), p. 6 (4.2. Multiple Scan Experiments) |
| Primary metric/result | This has minimal impact on the performance, but significantly speeds up the training time due to faster preprocessing [18]. | numeric claim only at cited anchor | p. 8 (5. Evaluation of Semantic Scene Completion) |

- Numeric sentences retained from the body:
- **p. 4 / 3.1. Labeling Process - extractive PDF cue:** An annotator needs on average 4.5 hours per tile, when labeling residential areas corresponding to the most complex encountered scenery, and needs on average 1.5 ...
- **p. 4 / 3.1. Labeling Process - extractive PDF cue:** In summary, the whole dataset comprises 518 tiles and over 1 400 hours of labeling effort have been invested with additional 10 -60 minutes verification ...
- **p. 4 / 3.2. Dataset Statistics - extractive PDF cue:** The class motorcyclist only occurs rarely, but still more than 100 000 points are annotated.
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** We select a volume of 51.2 m ahead of the car, 25.6 m to every side and 6.4 m in height with a voxel resolution ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work, we plan to provide also instance-level annotation over the whole sequence, i.e., we want to distinguish different objects in a scan, ... | p. 8 (6. Conclusion and Outlook) |
| body limitation/failure cue | Existing point cloud datasets cannot be used to address this task, as they do not allow for aggregating labeled point clouds that are sufficiently ... | p. 7 (5. Evaluation of Semantic Scene Completion) |
| body limitation/failure cue | Due to Completion Semantic Scene (IoU) Completion (mIoU) SSCNet [49] 29.83 9.53 TS3D [18] 29.81 9.54 TS3D [18] + DarkNet53Seg 24.99 10.19 TS3D [18] ... | p. 8 (5. Evaluation of Semantic Scene Completion) |
| body limitation/failure cue | Figure 7: Qualitative results for the semantic scene completion approach TS3D + DarkNet53Seg + SATNet. Left: Input volume. Middle: Network prediction. Right: Ground truth. ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | In the case of our proposed dataset, the car carrying the LiDAR moves past 3D objects in the scene and thereby records their backsides, ... | p. 7 (5. Evaluation of Semantic Scene Completion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This has minimal impact on the performance, but significantly speeds up the training time due to faster preprocessing [18]. | p. 8 (5. Evaluation of Semantic Scene Completion) |
| Approach num. parameters train time inference time (million)  GPU hours epoch   seconds point cloud  PointNet 3 4 0.5 PointNet++ 6 ... | p. 6 (Approach) |
| The evaluation metric for this task is still the same as in the single scan case, i.e., we evaluate the mean IoU of the ... | p. 6 (4.2. Multiple Scan Experiments) |
| To compute which voxels belong to the occluded space, we check for every pose of the car which voxels are visible to the sensor ... | p. 7 (5. Evaluation of Semantic Scene Completion) |
| [49] and compute the IoU for the task of scene completion, which only classifies a voxel as being occupied or empty, i.e., ignoring the ... | p. 7 (5. Evaluation of Semantic Scene Completion) |
| Other works experimented with new encoder-decoder CNN architectures as well as improving the loss term by adding adversarial loss components [58]. | p. 8 (5. Evaluation of Semantic Scene Completion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion and Outlook - extractive PDF cue:** In future work, we plan to provide also instance-level annotation over the whole sequence, i.e., we want to distinguish different objects in a scan, but ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** Existing point cloud datasets cannot be used to address this task, as they do not allow for aggregating labeled point clouds that are sufficiently dense ...
- **p. 8 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** Due to Completion Semantic Scene (IoU) Completion (mIoU) SSCNet [49] 29.83 9.53 TS3D [18] 29.81 9.54 TS3D [18] + DarkNet53Seg 24.99 10.19 TS3D [18] + ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 7: Qualitative results for the semantic scene completion approach TS3D + DarkNet53Seg + SATNet. Left: Input volume. Middle: Network prediction. Right: Ground truth. Due ...
- **p. 7 / 5. Evaluation of Semantic Scene Completion - extractive PDF cue:** In the case of our proposed dataset, the car carrying the LiDAR moves past 3D objects in the scene and thereby records their backsides, which ...

- **PDF anchors reviewed:** datasets p. 3 (3. The SemanticKITTI Dataset), p. 3 (3. The SemanticKITTI Dataset), p. 7 (5. Evaluation of Semantic Scene Completion), p. 7 (5. Evaluation of Semantic Scene Completion), p. 4 (3.2. Dataset Statistics), p. 4 (3.1. Labeling Process), metrics p. 7 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 6 (Figure/Table caption), p. 16 (Figure/Table caption), p. 6 (4.2. Multiple Scan Experiments), p. 7 (Figure/Table caption), baselines p. 8 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 4 (3.1. Labeling Process), p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), p. 6 (4.2. Multiple Scan Experiments), results p. 6 (4.2. Multiple Scan Experiments), p. 8 (5. Evaluation of Semantic Scene Completion), p. 8 (5. Evaluation of Semantic Scene Completion), p. 4 (3.1. Labeling Process), p. 4 (4.1. Single Scan Experiments), p. 6 (4.2. Multiple Scan Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
