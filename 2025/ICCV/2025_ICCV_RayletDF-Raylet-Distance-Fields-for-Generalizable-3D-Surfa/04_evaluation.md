# Evaluation - RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Evaluation on 3D Gaussians), p. 6 (4.1. Evaluation on 3D Gaussians), p. 5 (4. Experiments), p. 5 (4.1. Evaluation on 3D Gaussians), p. 7 (4.4. Ablations), p. 7 (4.4. Ablations)): From the results, we can see that: • When training/testing on ARKitScenes, ScanNet/ ScanNet++ datasets in domain, our method achieves the best accuracy, outperforming the second best method RayDF by ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** Datasets: Our method is evaluated on four real-world datasets based on the available train/test splits: 1) ScanNet [16] consisting of 1201 and 100 scenes for ...
- **p. 6 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** In particular, we use our model well-trained on ScanNet/ScanNet++ where T is chosen as 5 during training, and then directly evaluate on the test splits ...
- **p. 6 / 4.2. Evaluation on Point Clouds - extractive PDF cue:** For example, when trained on ARKitScenes or ScanNet/ScanNet++, our method achieves {0.067, 0.130} meters in ADE on the novel MultiScan dataset respectively, while the baselines ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** Qualitative results for different number of raylet samples per ray when evaluating on the test split of ARKitScenes.
- **p. 5 / 4.1. Evaluation on 3D Gaussians - extractive PDF cue:** After that, we evaluate the trained model on the test sets of ScanNet/ScanNet++, ARKitScenes, and MultiScan. • Group 2: We train our method from scratch ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** the trained model is evaluated on unseen datasets as shown in Tables 5&6.
- **p. 5 / 4. Experiments - extractive PDF cue:** In addition, we also evaluate the reconstructed 3D meshes, reporting Accuracy, Completion, Precision, Recall, Chamfer-L1 distance, Normal Consistency, and F-scores with a threshold of 5cm.
- **p. 5 / 4. Experiments - extractive PDF cue:** We report the per raysurface absolute distance error (ADE) in meters across all test images, and other four commonly used metrics [57] including Root Mean ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Evaluation on 3D Gaussians (p. 5); 4.2. Evaluation on Point Clouds (p. 6); 4.3. Evaluation on Raylet Sampling in Testing (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Evaluation on 3D Gaussians | EMPIRICAL / REAL-ROBOT OR HARDWARE | From the results, we can see that: • When training/testing on ARKitScenes, ScanNet/ ScanNet++ datasets in domain, our method achieves the best accuracy, outperforming ... | p. 6 (4.1. Evaluation on 3D Gaussians) |
| 4.1. Evaluation on 3D Gaussians | EMPIRICAL / REAL-ROBOT OR HARDWARE | Essentially, this is because our learned raylet distance representations capture the local surface geometric patterns which tend to be generalizable at various scenes. • ... | p. 6 (4.1. Evaluation on 3D Gaussians) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition, we also evaluate the reconstructed 3D meshes, reporting Accuracy, Completion, Precision, Recall, Chamfer-L1 distance, Normal Consistency, and F-scores with a threshold of ... | p. 5 (4. Experiments) |
| 4.1. Evaluation on 3D Gaussians | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results & Analysis: Table 1 compares the quantitative results of all methods for estimating distance values of all query rays from test views. | p. 5 (4.1. Evaluation on 3D Gaussians) |
| 4.4. Ablations | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results of all ablated models on ScanNet/ScanNet++. | p. 7 (4.4. Ablations) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** Datasets: Our method is evaluated on four real-world datasets based on the available train/test splits: 1) ScanNet [16] consisting of 1201 and 100 scenes for ...
- **p. 6 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** In particular, we use our model well-trained on ScanNet/ScanNet++ where T is chosen as 5 during training, and then directly evaluate on the test splits ...
- **p. 6 / 4.2. Evaluation on Point Clouds - extractive PDF cue:** For example, when trained on ARKitScenes or ScanNet/ScanNet++, our method achieves {0.067, 0.130} meters in ADE on the novel MultiScan dataset respectively, while the baselines ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** Qualitative results for different number of raylet samples per ray when evaluating on the test split of ARKitScenes.
- **p. 5 / 4.1. Evaluation on 3D Gaussians - extractive PDF cue:** After that, we evaluate the trained model on the test sets of ScanNet/ScanNet++, ARKitScenes, and MultiScan. • Group 2: We train our method from scratch ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** the trained model is evaluated on unseen datasets as shown in Tables 5&6.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We train all methods on the large-scale ARKitScene dataset and then directly test them on the unseen ScanNet++ dataset. Our RayletDF shows superior ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. An illustration of raylets and raylet distances. and its starting point is sampled (or located) near the sur- face of a shape. The ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle block shows the raylet distance field module, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Raylet sampling on virtual balls of point clouds. The prediction D is fully supervised using ℓ1 loss, and the ground truth distance values ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative results of all methods for ray surface distance estimation. † indicates the scale is aligned with ground truth depth. test on →ARKitScenes ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative results of 3D meshes reconstructed from estimated ray surface distances. Our model is trained on Scannet/++ dataset. test on →ARKitScenes test on ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative results of estimated ray-surface distances from 3D point clouds. test on →ARKitScenes test on →ScanNet/ScanNet++ test on →MultiScan ADE↓RMSE↓Abs-Rel↓Sq-Rel↓ δ ↑ ADE↓RMSE↓Abs-Rel↓Sq-Rel↓ ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Qualitative results for different number of raylet samples per ray when evaluating on the test split of ScanNet/ScanNet++. (train samples: T = 5) ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets: Our method is evaluated on four real-world datasets based on the available train/test splits: 1) ScanNet [16] consisting of 1201 and 100 scenes ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 6 (4.3. Evaluation on Raylet Sampling in Testing) |
| Task/environment | In particular, we use our model well-trained on ScanNet/ScanNet++ where T is chosen as 5 during training, and then directly evaluate on the test ... | reset, timeout, object/scene variation | p. 6 (4.3. Evaluation on Raylet Sampling in Testing), p. 6 (4.2. Evaluation on Point Clouds) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.5. Sampling Raylets for Training and Test), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In addition, we also evaluate the reconstructed 3D meshes, reporting Accuracy, Completion, Precision, Recall, Chamfer-L1 distance, Normal Consistency, and F-scores with a threshold of ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| We report the per raysurface absolute distance error (ADE) in meters across all test images, and other four commonly used metrics [57] including Root ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| This means that our newly introduced raylet distance field has its clear advantage over existing ray-based representations. • When evaluating all methods across new ... | definition/direction/unit from same section | p. 6 (4.1. Evaluation on 3D Gaussians) |
| Regarding the raylet distance field in Equation 4, we remove the confidence score, and the subsequent multi-raylet blender turns to simply average out multiple ... | definition/direction/unit from same section | p. 7 (4.4. Ablations) |
| We can see that, similar to the analysis in Section 4.1, our method demonstrates clearly better reconstruction accuracy on the in-domain datasets. | definition/direction/unit from same section | p. 6 (4.2. Evaluation on Point Clouds) |
| (12) Removing the prediction of confidence score sl. | definition/direction/unit from same section | p. 7 (4.4. Ablations) |
| Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle block shows the raylet distance field ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 2. An illustration of raylets and raylet distances. and its starting point is sampled (or located) near the sur- face of a shape. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baselines: We choose 5 representative groups of methods as our baselines: 1) the state-of-the-art per-scene optimization based 3D Gaussians splatting methods GOF [74] and ... | comparison identity and matched condition | p. 5 (4. Experiments) |
| Figure 1. We train all methods on the large-scale ARKitScene dataset and then directly test them on the unseen ScanNet++ dataset. Our RayletDF shows ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Most notably, we achieve an outstanding generalization ability when evaluating on unseen datasets, clearly surpassing two strong baselines. | comparison identity and matched condition | p. 6 (4.2. Evaluation on Point Clouds) |
| For a fair comparison, the four feed-forward generalizable baselines MVSGaussian [35], Pointersect [8], RayDF [36], and PFGS [59] are all trained with the same ... | comparison identity and matched condition | p. 5 (4.1. Evaluation on 3D Gaussians) |
| For example, when trained on ARKitScenes or ScanNet/ScanNet++, our method achieves {0.067, 0.130} meters in ADE on the novel MultiScan dataset respectively, while the ... | comparison identity and matched condition | p. 6 (4.2. Evaluation on Point Clouds) |
| Figure 6. Qualitative results of our method and baselines for 3D surface reconstruction on multiple datasets. All methods are trained on point clouds. 25623 | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To evaluate the effectiveness of each module and the sensitivity of hyperparameters, we conduct the following ablations on the merged ScanNet/ScanNet++ dataset, and the ... | component/input/data sensitivity | p. 7 (4.4. Ablations) |
| In this ablation, the hyperparameter T is chosen as {1, 5, 10, 20}. | component/input/data sensitivity | p. 7 (4.4. Ablations) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are: • We propose a generic pipeline for explicit 3D surface reconstruction from either point clouds or 3D Gaussians. • We introduce ... | From the results, we can see that: • When training/testing on ARKitScenes, ScanNet/ ScanNet++ datasets in domain, our method achieves the best accuracy, outperforming ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Evaluation on 3D Gaussians), p. 6 (4.1. Evaluation on 3D Gaussians), p. 5 (4. Experiments), p. 5 (4.1. Evaluation on 3D Gaussians), p. 7 (4.4. Ablations), p. 7 (4.4. Ablations) |
| Primary metric/result | Essentially, this is because our learned raylet distance representations capture the local surface geometric patterns which tend to be generalizable at various scenes. • ... | numeric claim only at cited anchor | p. 6 (4.1. Evaluation on 3D Gaussians) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive PDF cue:** Datasets: Our method is evaluated on four real-world datasets based on the available train/test splits: 1) ScanNet [16] consisting of 1201 and 100 scenes for ...
- **p. 6 / 4.1. Evaluation on 3D Gaussians - extractive PDF cue:** From the results, we can see that: • When training/testing on ARKitScenes, ScanNet/ ScanNet++ datasets in domain, our method achieves the best accuracy, outperforming the ...
- **p. 6 / 4.1. Evaluation on 3D Gaussians - extractive PDF cue:** This means that our newly introduced raylet distance field has its clear advantage over existing ray-based representations. • When evaluating all methods across new datasets, ...
- **p. 6 / 4.2. Evaluation on Point Clouds - extractive PDF cue:** For example, when trained on ARKitScenes or ScanNet/ScanNet++, our method achieves {0.067, 0.130} meters in ADE on the novel MultiScan dataset respectively, while the baselines ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle block shows the raylet distance field ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Remarkably, thanks to the learned local raylet features, it exhibits excellent generalizability to new and unseen scenes in testing, while all baselines fail to ... | p. 7 (5. Conclusion) |
| body limitation/failure cue | This validates the generalizability and robustness of our simple design. | p. 7 (4.3. Evaluation on Raylet Sampling in Testing) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Given a specific 3D scene P as input, if it is a raw point cloud, for a specific query ray r, we sample multiple ... | p. 4 (3.5. Sampling Raylets for Training and Test) |
| Regarding our designed multi-raylet blender in Section 3.4, the single hyperparameter T of this module can be different in training and test phase, allowing ... | p. 6 (4.3. Evaluation on Raylet Sampling in Testing) |
| In this ablation, the hyperparameter T is chosen as {1, 5, 10, 20}. | p. 7 (4.4. Ablations) |
| For the raylet feature extractor, in Equation 3, the hyperparameter K is chosen as {1, 5, 10, 20}. | p. 7 (4.4. Ablations) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of our proposed pipeline. The leftmost block shows the raylet feature extractor module, the middle block shows the raylet distance field module, ...
- **p. 7 / 5. Conclusion - extractive PDF cue:** Remarkably, thanks to the learned local raylet features, it exhibits excellent generalizability to new and unseen scenes in testing, while all baselines fail to do ...
- **p. 7 / 4.3. Evaluation on Raylet Sampling in Testing - extractive PDF cue:** This validates the generalizability and robustness of our simple design.

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 6 (4.3. Evaluation on Raylet Sampling in Testing), p. 6 (4.2. Evaluation on Point Clouds), p. 7 (4.3. Evaluation on Raylet Sampling in Testing), p. 5 (4.1. Evaluation on 3D Gaussians), p. 7 (4.3. Evaluation on Raylet Sampling in Testing), metrics p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on 3D Gaussians), p. 7 (4.4. Ablations), p. 6 (4.2. Evaluation on Point Clouds), p. 7 (4.4. Ablations), baselines p. 5 (4. Experiments), p. 1 (Figure/Table caption), p. 6 (4.2. Evaluation on Point Clouds), p. 5 (4.1. Evaluation on 3D Gaussians), p. 6 (4.2. Evaluation on Point Clouds), p. 8 (Figure/Table caption), results p. 6 (4.1. Evaluation on 3D Gaussians), p. 6 (4.1. Evaluation on 3D Gaussians), p. 5 (4. Experiments), p. 5 (4.1. Evaluation on 3D Gaussians), p. 7 (4.4. Ablations), p. 7 (4.4. Ablations).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
