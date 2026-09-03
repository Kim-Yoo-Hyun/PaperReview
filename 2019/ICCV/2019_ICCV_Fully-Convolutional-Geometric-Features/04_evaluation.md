# Evaluation - Fully Convolutional Geometric Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_ICCV_2019/papers/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (6. Experiments), p. 8 (Figure/Table caption), p. 5 (6.2. Evaluation Metrics), p. 5 (6.3. 3D Match Benchmark), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption)): We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses.

## Evaluation Body Digest

- **p. 4 / 6.1. Datasets and Training - extractive body cue:** This training set contains 11 sequences, which we split into train/val/test sets as follows: sequence 0 to 5 for training, sequence 7 to 8 for ...
- **p. 4 / 6.1. Datasets and Training - extractive body cue:** For indoor data, we use the standard 3D Match dataset [36].
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** For the outdoor dataset, we use the Relative Translation Error and the Relative Rotation Error.
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** Thus, they are indirect measures, but we follow Yew and Lee [34] for outdoor dataset evaluation.
- **p. 4 / 6. Experiments - extractive body cue:** We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses.
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** Specifically, the registration recall uses the following error metric between estimated fragments {i, j}, and corresponding pose estimation ˆTi,j to define a true positive: ERMSE ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Feature-match recall with respect to inlier ratio threshold τ2 (left) and inlier distance accuracy tolerance τ1 (right). The vertical lines are τ2 = ...
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** The Relative Translation Error (RTE) and Relative Rotation Error (RRE) measure the registration errors of features used for RANSAC.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Implementation (p. 4); 6. Experiments (p. 4); 6.1. Datasets and Training (p. 4); 6.2. Evaluation Metrics (p. 5); 6.3. 3D Match Benchmark (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | p. 4 (6. Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6: Results on the KITTI dataset. Relative Trans- lation Error (RTE) and Relative Rotation Error (RRE) af- ter RANSAC on FCGF trained with ... | p. 8 (Figure/Table caption) |
| 6.2. Evaluation Metrics | EMPIRICAL / SOURCE-REPORTED EVALUATION | As noted in several works [1, 7, 6, 17], recall is more important than precision since it is possible to improve precision with better ... | p. 5 (6.2. Evaluation Metrics) |
| 6.3. 3D Match Benchmark | EMPIRICAL / SOURCE-REPORTED EVALUATION | FCGF outperforms all hand-crafted features and PointNet-based methods by a large margin and marginally outperforms a recent 3Dconvolution-based method [11]. | p. 5 (6.3. 3D Match Benchmark) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Feature match recall of the hardest-triplet loss with various hardest-negative and random triplet ratios (Hardest- Negative triplets (HN) and Random Triplets (RT) ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 6.1. Datasets and Training - extractive body cue:** This training set contains 11 sequences, which we split into train/val/test sets as follows: sequence 0 to 5 for training, sequence 7 to 8 for ...
- **p. 4 / 6.1. Datasets and Training - extractive body cue:** For indoor data, we use the standard 3D Match dataset [36].
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** For the outdoor dataset, we use the Relative Translation Error and the Relative Rotation Error.
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** Thus, they are indirect measures, but we follow Yew and Lee [34] for outdoor dataset evaluation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Feature-match recall [6, 7] and speed in log scale on the 3DMatch benchmark [36]. Our approach is the most accurate and the fastest. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: We use a ResUNet architecture. The white blocks indicate input and output layers. Each block is character- ized by three parameters: kernel size, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Sampling and negative-mining strategy for each method. Traditional contrastive and triplet losses use random sampling. Our hardest-contrastive and hardest-triplet losses use the hardest ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Feature-match recall with respect to inlier ratio threshold τ2 (left) and inlier distance accuracy tolerance τ1 (right). The vertical lines are τ2 = ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Color-coded features overlaid on selected fragment pairs. The 32-dimensional FCGF features for each pair of point clouds are mapped to a scalar space ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Color-coded FCGF features for pairs of KITTI LIDAR scans that are 10m apart. FCGF features from downsampled LIDAR scans are mapped to a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Feature-match recall at τ1 = 0.1, τ2 = 0.05 [6] on 3DMatch [33]. FMR and STD indicate the Feature Match Recall and its ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Hardest-contrastive loss feature match recall with different feature dimensionality on 3DMatch. OOM de- notes Out Of Memory under the same hyperparameters. tance thresholds, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This training set contains 11 sequences, which we split into train/val/test sets as follows: sequence 0 to 5 for training, sequence 7 to 8 ... | embodiment, simulator version and control stack | p. 4 (6.1. Datasets and Training), p. 4 (6.1. Datasets and Training) |
| Task/environment | For indoor data, we use the standard 3D Match dataset [36]. | reset, timeout, object/scene variation | p. 4 (6.1. Datasets and Training), p. 5 (6.2. Evaluation Metrics) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (5. Implementation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 8 (6.7. Runtime), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6: Results on the KITTI dataset. Relative Trans- lation Error (RTE) and Relative Rotation Error (RRE) af- ter RANSAC on FCGF trained with ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | definition/direction/unit from same section | p. 4 (6. Experiments) |
| Specifically, the registration recall uses the following error metric between estimated fragments {i, j}, and corresponding pose estimation ˆTi,j to define a true positive: ... | definition/direction/unit from same section | p. 5 (6.2. Evaluation Metrics) |
| Figure 4: Feature-match recall with respect to inlier ratio threshold τ2 (left) and inlier distance accuracy tolerance τ1 (right). The vertical lines are τ2 ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| The Relative Translation Error (RTE) and Relative Rotation Error (RRE) measure the registration errors of features used for RANSAC. | definition/direction/unit from same section | p. 5 (6.2. Evaluation Metrics) |
| Table 1: Feature-match recall at τ1 = 0.1, τ2 = 0.05 [6] on 3DMatch [33]. FMR and STD indicate the Feature Match Recall and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1: Feature-match recall [6, 7] and speed in log scale on the 3DMatch benchmark [36]. Our approach is the most accurate and the ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| FCGF features from downsampled LIDAR scans are mapped to a scalar space using t-SNE [31] and colorized with the Spectral color map. | definition/direction/unit from same section | p. 6 (6.3. 3D Match Benchmark) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | comparison identity and matched condition | p. 4 (6. Experiments) |
| Note that FCGF is 32-dimensional while most state-of-the-art methods have higher dimensionality. | comparison identity and matched condition | p. 5 (6.3. 3D Match Benchmark) |
| FCGF outperforms all hand-crafted features and PointNet-based methods by a large margin and marginally outperforms a recent 3Dconvolution-based method [11]. | comparison identity and matched condition | p. 5 (6.3. 3D Match Benchmark) |
| Table 3: Feature match recall of the hardest-triplet loss with various hardest-negative and random triplet ratios (Hardest- Negative triplets (HN) and Random Triplets (RT) ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We found rotation augmentation to be a simple (SO(3) multiplication) and effective way to make FCGF invariant to relative camera pose change. | component/input/data sensitivity | p. 5 (6.1. Datasets and Training) |
| If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset. | component/input/data sensitivity | p. 5 (6.1. Datasets and Training) |
| We use hash-based filtering to efficiently remove false negatives from the hard negative mining step to implement I(i, ji). | component/input/data sensitivity | p. 4 (5. Implementation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we propose metric learning losses for fully-convolutional feature learning. | We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (6. Experiments), p. 8 (Figure/Table caption), p. 5 (6.2. Evaluation Metrics), p. 5 (6.3. 3D Match Benchmark), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Table 6: Results on the KITTI dataset. Relative Trans- lation Error (RTE) and Relative Rotation Error (RRE) af- ter RANSAC on FCGF trained with ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 6.1. Datasets and Training - extractive body cue:** We train the networks for 100 epochs using Stochastic Gradient Descent starting with learning rate 0.1 with a Exponential learning rate schedule with γ = ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration. | p. 8 (7. Conclusion) |
| body limitation/failure cue | Next, we find the hardest negatives for all positive pairs and filter out the hardest negatives that fall within the vicinity of positive pairs ... | p. 4 (5. Implementation) |
| body limitation/failure cue | First, we create a matrix P that contains the indices of positive pairs (i, j) as well as an additional matrix Pdt that contains ... | p. 4 (5. Implementation) |
| body limitation/failure cue | If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset. | p. 5 (6.1. Datasets and Training) |
| body limitation/failure cue | However, it does not measure the quality of feature when used within a reconstruction system. | p. 5 (6.2. Evaluation Metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All these preprocessing steps can be parallelized in data-loading parallel processes and consume a fraction of the training time. | p. 4 (5. Implementation) |
| We train the networks for 100 epochs using Stochastic Gradient Descent starting with learning rate 0.1 with a Exponential learning rate schedule with γ ... | p. 5 (6.1. Datasets and Training) |
| We use an Intel i7 10-core 3.0GHz CPU (i7-6950) and an Nvidia Titan-X Pascal GPU to measure FCGF runtime. | p. 8 (6.7. Runtime) |
| We used batch size 4 for all experiments and analysis. | p. 5 (6.1. Datasets and Training) |
| As the input to the network requires unique coordinates C and corresponding features F, we first downsample the input point cloud using a fast ... | p. 4 (5. Implementation) |
| Kitchen Hotel 1 Lab Study room Figure 5: Color-coded features overlaid on selected fragment pairs. | p. 6 (6.3. 3D Match Benchmark) |
| Pair 1 Pair 2 Pair 3 Pair 4 Figure 6: Color-coded FCGF features for pairs of KITTI LIDAR scans that are 10m apart. | p. 6 (6.3. 3D Match Benchmark) |
| The hardest-contrastive loss outperforms random triplets, hardest-triplet, and contrastive loss. "norm." denotes the normalized feature. easily, we varied the number of hardest-negatives and random ... | p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Conclusion - extractive body cue:** An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.
- **p. 4 / 5. Implementation - extractive body cue:** Next, we find the hardest negatives for all positive pairs and filter out the hardest negatives that fall within the vicinity of positive pairs by ...
- **p. 4 / 5. Implementation - extractive body cue:** First, we create a matrix P that contains the indices of positive pairs (i, j) as well as an additional matrix Pdt that contains all ...
- **p. 5 / 6.1. Datasets and Training - extractive body cue:** If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset.
- **p. 5 / 6.2. Evaluation Metrics - extractive body cue:** However, it does not measure the quality of feature when used within a reconstruction system.

- **Evidence anchors reviewed:** datasets p. 4 (6.1. Datasets and Training), p. 4 (6.1. Datasets and Training), p. 5 (6.2. Evaluation Metrics), p. 5 (6.2. Evaluation Metrics), metrics p. 8 (Figure/Table caption), p. 4 (6. Experiments), p. 5 (6.2. Evaluation Metrics), p. 6 (Figure/Table caption), p. 5 (6.2. Evaluation Metrics), p. 7 (Figure/Table caption), baselines p. 4 (6. Experiments), p. 5 (6.3. 3D Match Benchmark), p. 5 (6.3. 3D Match Benchmark), p. 7 (Figure/Table caption), results p. 4 (6. Experiments), p. 8 (Figure/Table caption), p. 5 (6.2. Evaluation Metrics), p. 5 (6.3. 3D Match Benchmark), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
