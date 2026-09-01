# Evaluation - FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Quantitative Results), p. 8 (4.5. Runtime Analysis), p. 7 (4.3. Quantitative Results), p. 5 (4. Experimental Results), p. 6 (4.1.1. Datasets), p. 8 (Figure/Table caption)): The results reveal that FROSS achieves the highest performance among all baseline methods with much lower processing latency.

## Evaluation Body Digest

- **p. 5 / 4.1.1. Datasets - extractive PDF cue:** 3DSSG augments the base dataset with object attributes, hierarchical category labels, and directed edges that describe inter-object semantic relationships such as ‘standing on,' ‘attached to,' ...
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** Although Replica encompasses only 18 scenes, which precludes its use for training purposes, it serves as an effective evaluation benchmark.
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** In the evaluation of FROSS, seven scenes serve as validation environments for hyperparameter optimization, while the remaining 11 scenes function as performance assessment platforms.
- **p. 5 / 4.1.1. Datasets - extractive PDF cue:** The 3DSSG dataset [31] extends 3RScan [30], which encompasses 1,482 scans of indoor environments with their corresponding RGB-D image sequences, 3D meshes, and dense instance ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Performance comparison of 3D SSG generation methods on the 3DSSG dataset and the end-to-end latency without environmental mapping reported in their original literature, along with ...
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** Qualitative comparison between FROSS and Wu [35] on the 3DSSG dataset.
- **p. 8 / 4.5. Runtime Analysis - extractive PDF cue:** Det. refers to the object detection model RT-DETR [21, 44], while Rel.
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** Errors are marked in red, with ground truth label shown in parentheses.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experimental Results (p. 5); 4.1. Evaluation Setup (p. 5); 4.1.1. Datasets (p. 5); 4.1.4. Evaluation Metrics (p. 6); 4.2. Implementation Details (p. 6); 4.3. Quantitative Results (p. 7); 4.4. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results reveal that FROSS achieves the highest performance among all baseline methods with much lower processing latency. | p. 7 (4.3. Quantitative Results) |
| 4.5. Runtime Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to the previous methods for online real-time 3D SSG generation methods [16, 34, 35], FROSS demonstrates significantly reduced end-to-end latency and increased FPS, ... | p. 8 (4.5. Runtime Analysis) |
| 4.3. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Kim's baseline [16] achieves similar object recall to FROSS due to the same 2D SG generation pipeline. | p. 7 (4.3. Quantitative Results) |
| 4. Experimental Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Moreover, the effectiveness of our approach is further demonstrated through qualitative results in Section 4.4. | p. 5 (4. Experimental Results) |
| 4.1.1. Datasets | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the evaluation of FROSS, seven scenes serve as validation environments for hyperparameter optimization, while the remaining 11 scenes function as performance assessment platforms. | p. 6 (4.1.1. Datasets) |

## Dataset / Benchmark Role

- **p. 5 / 4.1.1. Datasets - extractive PDF cue:** 3DSSG augments the base dataset with object attributes, hierarchical category labels, and directed edges that describe inter-object semantic relationships such as ‘standing on,' ‘attached to,' ...
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** Although Replica encompasses only 18 scenes, which precludes its use for training purposes, it serves as an effective evaluation benchmark.
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** In the evaluation of FROSS, seven scenes serve as validation environments for hyperparameter optimization, while the remaining 11 scenes function as performance assessment platforms.
- **p. 5 / 4.1.1. Datasets - extractive PDF cue:** The 3DSSG dataset [31] extends 3RScan [30], which encompasses 1,482 scans of indoor environments with their corresponding RGB-D image sequences, 3D meshes, and dense instance ...
- **p. 7 / 4.2. Implementation Details - extractive PDF cue:** Performance comparison of 3D SSG generation methods on the 3DSSG dataset and the end-to-end latency without environmental mapping reported in their original literature, along with ...
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** Qualitative comparison between FROSS and Wu [35] on the 3DSSG dataset.
- **p. 8 / 4.5. Runtime Analysis - extractive PDF cue:** Det. refers to the object detection model RT-DETR [21, 44], while Rel.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce FROSS, an online real-time 3D semantic scene graph generation method that leverages and integrates 2D scene graphs. FROSS represents objects as ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. An overview of the FROSS framework: (a) The process initiates with object detection via RT-DETR [44] from an RGB-D image and its associated ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Illustration of the object merging process using the proposed algorithm described in Section 3.4. (a) Starting with an input image, a set of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Performance comparison of 3D SSG generation methods on the 3DSSG dataset and the end-to-end latency without envi- ronmental mapping reported in their original ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparison between FROSS and Wu [35] on the 3DSSG dataset. Only representative objects are visualized. Errors are marked in red, with ground ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Runtime analysis of the key components of FROSS. Obj. Det. refers to the object detection model RT-DETR [21, 44], while Rel. Ext. corresponds ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Analysis of FROSS with predicted and ground truth 2D SGs as input on both the 3DSSG and ReplicaSSG datasets. ‘w/ GT' denotes the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Performance comparison of FROSS with the predicted and the ground truth camera trajectories as input on the Repli- caSSG dataset. Please note that ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3DSSG augments the base dataset with object attributes, hierarchical category labels, and directed edges that describe inter-object semantic relationships such as ‘standing on,' ‘attached ... | embodiment, simulator version and control stack | p. 5 (4.1.1. Datasets), p. 6 (4.1.1. Datasets) |
| Task/environment | Although Replica encompasses only 18 scenes, which precludes its use for training purposes, it serves as an effective evaluation benchmark. | reset, timeout, object/scene variation | p. 6 (4.1.1. Datasets), p. 6 (4.1.1. Datasets) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.3. Lifting 2D SG to 3D), p. 3 (3.2. Overview of Framework) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.1. Problem Definition) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Errors are marked in red, with ground truth label shown in parentheses. | definition/direction/unit from same section | p. 7 (4.3. Quantitative Results) |
| In contrast, IMP [36] employs a voting mechanism for object classification, while VGfM [9] uses a basic recurrent neural network, which may restrict their ... | definition/direction/unit from same section | p. 7 (4.3. Quantitative Results) |
| (a) Starting with an input image, a set of objects with predicted categories and bounding boxes is generated. | definition/direction/unit from same section | p. 5 (4.1.1. Datasets) |
| Moreover, the effectiveness of our approach is further demonstrated through qualitative results in Section 4.4. | definition/direction/unit from same section | p. 5 (4. Experimental Results) |
| Object recall quantifies the proportion of ground truth instances matched to predictions with correct category labels. | definition/direction/unit from same section | p. 6 (4.1.4. Evaluation Metrics) |
| Note that a more detailed explanation of the utilized recall metric is offered in the supplementary materials (Section 6). | definition/direction/unit from same section | p. 6 (4.1.4. Evaluation Metrics) |
| Table 5. Recall on the validation split of the 3DSSG dataset with different Hellinger distance thresholds. Threshold δd 0.6 0.65 0.7 0.75 0.8 | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 4. Performance comparison of FROSS with the predicted and the ground truth camera trajectories as input on the Repli- caSSG dataset. Please note ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Section 4.1 introduces the datasets, baseline SSG generation methods, and evaluation metrics. | comparison identity and matched condition | p. 5 (4. Experimental Results) |
| We evaluated FROSS on the 3DSSG dataset against several baseline methods for SSG generation. | comparison identity and matched condition | p. 6 (4.1.2. Baseline Methods) |
| Kim's 3D object representation and merging mechanism are integrated into FROSS for its baseline implementation, while other baseline implementations follow [35]1. | comparison identity and matched condition | p. 6 (4.1.2. Baseline Methods) |
| Kim's baseline [16] achieves similar object recall to FROSS due to the same 2D SG generation pipeline. | comparison identity and matched condition | p. 7 (4.3. Quantitative Results) |
| The results reveal that FROSS achieves the highest performance among all baseline methods with much lower processing latency. | comparison identity and matched condition | p. 7 (4.3. Quantitative Results) |
| Compared to the previous methods for online real-time 3D SSG generation methods [16, 34, 35], FROSS demonstrates significantly reduced end-to-end latency and increased FPS, ... | comparison identity and matched condition | p. 8 (4.5. Runtime Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We further provide runtime analyses on the ReplicaSSG dataset in Section 4.5, along with additional ablation studies in Section 4.6. | component/input/data sensitivity | p. 5 (4. Experimental Results) |
| In the ablation studies, we investigate the impact of using ground truth 2D SGs and camera trajectories on the ReplicaSSG dataset. | component/input/data sensitivity | p. 6 (4.1.2. Baseline Methods) |
| As FROSS generates predictions without explicit point cloud output, we establish evaluation metrics using backprojected 3D points. | component/input/data sensitivity | p. 6 (4.1.3. Matching Object Predictions to Ground Truth) |
| Figure 1. We introduce FROSS, an online real-time 3D semantic scene graph generation method that leverages and integrates 2D scene graphs. FROSS represents objects ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| The impact of estimated trajectories are further analyzed via ablation studies in Section 4.6.2. | component/input/data sensitivity | p. 7 (4.2. Implementation Details) |
| Performance comparison of 3D SSG generation methods on the 3DSSG dataset and the end-to-end latency without environmental mapping reported in their original literature, along ... | component/input/data sensitivity | p. 7 (4.2. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of the paper can be summarized as follows: • We introduce FROSS, an innovative methodology for online real-time generation of 3D ... | The results reveal that FROSS achieves the highest performance among all baseline methods with much lower processing latency. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Quantitative Results), p. 8 (4.5. Runtime Analysis), p. 7 (4.3. Quantitative Results), p. 5 (4. Experimental Results), p. 6 (4.1.1. Datasets), p. 8 (Figure/Table caption) |
| Primary metric/result | Compared to the previous methods for online real-time 3D SSG generation methods [16, 34, 35], FROSS demonstrates significantly reduced end-to-end latency and increased FPS, ... | numeric claim only at cited anchor | p. 8 (4.5. Runtime Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** Specifically, the original 160 object categories map to 20 categories from NYUv2 [23], while seven of the 26 predicate categories remain.
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** Although Replica encompasses only 18 scenes, which precludes its use for training purposes, it serves as an effective evaluation benchmark.
- **p. 6 / 4.1.1. Datasets - extractive PDF cue:** In the evaluation of FROSS, seven scenes serve as validation environments for hyperparameter optimization, while the remaining 11 scenes function as performance assessment platforms.
- **p. 7 / 4.5. Runtime Analysis - extractive PDF cue:** The metrics represent averages across 14,400 frames from four ReplicaSSG test scenes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, its merging mechanism fails to suppress duplicate detections, which hinders relationship aggregation and leads to significantly lower relationship and predicate recall. | p. 7 (4.3. Quantitative Results) |
| body limitation/failure cue | This substantiates the advantages of lifting scene graphs from 2D images over direct point cloud reasoning [31, 34, 35], as point clouds can sometimes ... | p. 7 (4.3. Quantitative Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Section 4.2 presents the implementation details. | p. 5 (4. Experimental Results) |
| We further provide runtime analyses on the ReplicaSSG dataset in Section 4.5, along with additional ablation studies in Section 4.6. | p. 5 (4. Experimental Results) |
| The dataset splits and label mapping are available in the released code. | p. 6 (4.1.1. Datasets) |
| Predicate recall computes the proportion of correctly classified predicates between detected objects, regardless of the object classes. | p. 6 (4.1.4. Evaluation Metrics) |
| Our implementation applies a confidence threshold of 0.7 for object filtering and retains only the top ten relationships per 2D SG. | p. 7 (4.2. Implementation Details) |
| All hyperparameters were determined through grid search evaluation on the validation split, with particular emphasis on relationship recall optimization. | p. 7 (4.2. Implementation Details) |
| This process involves two key steps: (1) the conversion of object bounding boxes to 2D Gaussians, and (2) their subsequent back-projection into 3D space ... | p. 3 (3.3. Lifting 2D SG to 3D) |
| Merging (Section 3.4) CNN Backbone & Encoder Self-Attention Layer 0 Self-Attention Layer 1 Self-Attention Layer N Hidden Layers Self-Attention Features RT-DETR Detected Objects EGTR ... | p. 4 (3.3. Lifting 2D SG to 3D) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** However, its merging mechanism fails to suppress duplicate detections, which hinders relationship aggregation and leads to significantly lower relationship and predicate recall.
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** This substantiates the advantages of lifting scene graphs from 2D images over direct point cloud reasoning [31, 34, 35], as point clouds can sometimes present ...

- **PDF anchors reviewed:** datasets p. 5 (4.1.1. Datasets), p. 6 (4.1.1. Datasets), p. 6 (4.1.1. Datasets), p. 5 (4.1.1. Datasets), p. 7 (4.2. Implementation Details), p. 7 (4.3. Quantitative Results), metrics p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 5 (4.1.1. Datasets), p. 5 (4. Experimental Results), p. 6 (4.1.4. Evaluation Metrics), p. 6 (4.1.4. Evaluation Metrics), baselines p. 5 (4. Experimental Results), p. 6 (4.1.2. Baseline Methods), p. 6 (4.1.2. Baseline Methods), p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 8 (4.5. Runtime Analysis), results p. 7 (4.3. Quantitative Results), p. 8 (4.5. Runtime Analysis), p. 7 (4.3. Quantitative Results), p. 5 (4. Experimental Results), p. 6 (4.1.1. Datasets), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
