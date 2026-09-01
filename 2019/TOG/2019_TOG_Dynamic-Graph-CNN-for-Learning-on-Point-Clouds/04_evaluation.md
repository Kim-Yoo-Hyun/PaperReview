# Evaluation - Dynamic Graph CNN for Learning on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1801.07829; PDF retrieval source: https://arxiv.org/pdf/1801.07829. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 8 (4 EVALUATION), p. 8 (4 EVALUATION), p. 10 (4 EVALUATION), p. 10 (4 EVALUATION)): Our model achieves the best results on this dataset.

## Evaluation Body Digest

- **p. 8 / 4 EVALUATION - extractive PDF cue:** The dataset contains 16,881 3D shapes from 16 object categories, annotated with 50 parts in total.
- **p. 8 / 4 EVALUATION - extractive PDF cue:** We extend our EdgeConv model architectures for part segmentation task on ShapeNet part dataset [Yi et al.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** Our model achieves the best results on this dataset.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** The dataset contains 12,311 meshed CAD models from 40 categories.
- **p. 9 / 4 EVALUATION - extractive PDF cue:** This dataset includes 3D scan point clouds for 6 indoor areas including 272 rooms in total.
- **p. 9 / 4 EVALUATION - extractive PDF cue:** We evaluate our model on Stanford Large-Scale 3D Indoor Spaces Dataset (S3DIS) [Armeni et al.
- **p. 10 / 4 EVALUATION - extractive PDF cue:** Mean overall IoU accuracy PointNet (baseline) [Qi et al.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** Mean Overall Class Accuracy Accuracy 3DShapeNets [Wu et al.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EVALUATION (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model achieves the best results on this dataset. | p. 7 (4 EVALUATION) |
| 4 EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster. | p. 7 (4 EVALUATION) |
| 4 EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Using more points further improves the overall accuracy by 0.6%. | p. 8 (4 EVALUATION) |
| 4 EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Explicitly centralizing each patch by using the concatenation of xi and xi -xj leads to about 0.5% improvement for overall accuracy. | p. 8 (4 EVALUATION) |
| 4 EVALUATION | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that the segmentation results of turbines are improved when more points are included. | p. 10 (4 EVALUATION) |

## Dataset / Benchmark Role

- **p. 8 / 4 EVALUATION - extractive PDF cue:** The dataset contains 16,881 3D shapes from 16 object categories, annotated with 50 parts in total.
- **p. 8 / 4 EVALUATION - extractive PDF cue:** We extend our EdgeConv model architectures for part segmentation task on ShapeNet part dataset [Yi et al.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** Our model achieves the best results on this dataset.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** The dataset contains 12,311 meshed CAD models from 40 categories.
- **p. 9 / 4 EVALUATION - extractive PDF cue:** This dataset includes 3D scan point clouds for 6 indoor areas including 272 rooms in total.
- **p. 9 / 4 EVALUATION - extractive PDF cue:** We evaluate our model on Stanford Large-Scale 3D Indoor Spaces Dataset (S3DIS) [Armeni et al.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Point cloud segmentation using the proposed neural network. Bottom: schematic neural network architecture. Top: Structure of the feature spaces produced at different layers ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Left: Computing an edge feature, eij (top), from a point pair, xi and xj (bottom). In this example, hΘ() is instantiated using a ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3. Model architectures: The model architectures used for classification (top branch) and segmentation (bottom branch). The classification model takes as input n points, calculates ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison to existing methods. The per-point weight wi in [Atzmon et al. 2018] effectively is computed in the first layer and could be ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Structure of the feature spaces produced at different stages of our shape classification neural network architecture, visualized as the distance between the red ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Classification results on ModelNet40. 4.2 Model Complexity We use the ModelNet40 [Wu et al. 2015] classification experiment to compare the complexity of our ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Complexity, forward time, and accuracy of different models more efficient. The number of points in each experiment is also 1024 in this section. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Effectiveness of different components. CENT denotes centraliza- tion, DYN denotes dynamical graph recomputation, and MPOINTS denotes experiments with 2048 points .

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset contains 16,881 3D shapes from 16 object categories, annotated with 50 parts in total. | embodiment, simulator version and control stack | p. 8 (4 EVALUATION), p. 8 (4 EVALUATION) |
| Task/environment | We extend our EdgeConv model architectures for part segmentation task on ShapeNet part dataset [Yi et al. | reset, timeout, object/scene variation | p. 8 (4 EVALUATION), p. 7 (4 EVALUATION) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Mean overall IoU accuracy PointNet (baseline) [Qi et al. | definition/direction/unit from same section | p. 10 (4 EVALUATION) |
| Mean Overall Class Accuracy Accuracy 3DShapeNets [Wu et al. | definition/direction/unit from same section | p. 7 (4 EVALUATION) |
| Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster. | definition/direction/unit from same section | p. 7 (4 EVALUATION) |
| Using more points further improves the overall accuracy by 0.6%. | definition/direction/unit from same section | p. 8 (4 EVALUATION) |
| Solomon Model size(MB) Time(ms) Accuracy(%) PointNet (Baseline) [Qi et al. | definition/direction/unit from same section | p. 8 (4 EVALUATION) |
| For each set, from left to right: PointNet, ours and ground truth. the mean IoU versus "keep ratio" is shown. | definition/direction/unit from same section | p. 9 (4 EVALUATION) |
| Left: The mean IoU (%) improves when the ratio of kept points increases. | definition/direction/unit from same section | p. 10 (4 EVALUATION) |
| Fig. 3. Model architectures: The model architectures used for classification (top branch) and segmentation (bottom branch). The classification model takes as input n points, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster. | comparison identity and matched condition | p. 7 (4 EVALUATION) |
| 2018] - 92.3 Ours (baseline) 88.9 91.7 Ours 90.2 92.9 Ours (2048 points) 90.7 93.5 Table 2. | comparison identity and matched condition | p. 7 (4 EVALUATION) |
| Solomon Model size(MB) Time(ms) Accuracy(%) PointNet (Baseline) [Qi et al. | comparison identity and matched condition | p. 8 (4 EVALUATION) |
| 2017b] and PointNet baseline, where additional point features (local point density, local curvature and normal) are used to construct handcrafted features and then fed ... | comparison identity and matched condition | p. 9 (4 EVALUATION) |
| Mean overall IoU accuracy PointNet (baseline) [Qi et al. | comparison identity and matched condition | p. 10 (4 EVALUATION) |
| Table 1. Comparison to existing methods. The per-point weight wi in [Atzmon et al. 2018] effectively is computed in the first layer and could ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The network architecture used for the classification task is shown in Figure 3 (top branch without spatial transformer network). | component/input/data sensitivity | p. 7 (4 EVALUATION) |
| Effectiveness of different components. | component/input/data sensitivity | p. 8 (4 EVALUATION) |
| Fig. 2. Left: Computing an edge feature, eij (top), from a point pair, xi and xj (bottom). In this example, hΘ() is instantiated using ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better ... | Our model achieves the best results on this dataset. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 8 (4 EVALUATION), p. 8 (4 EVALUATION), p. 10 (4 EVALUATION), p. 10 (4 EVALUATION) |
| Primary metric/result | Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster. | numeric claim only at cited anchor | p. 7 (4 EVALUATION) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EVALUATION - extractive PDF cue:** For each model, 1,024 points are uniformly sampled from the mesh faces; the point cloud is rescaled to fit into the unit sphere.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** All the experiments are performed with point clouds that contain 1024 points except last row.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** We further test out model with 2048 points.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** The k used for 2048 points is 40 to maintain the same density.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** 2018] uses additional augmentation techniques like randomly sampling 1024 points out of 1200 points during both training and testing.
- **p. 7 / 4 EVALUATION - extractive PDF cue:** 2018] - 92.3 Ours (baseline) 88.9 91.7 Ours 90.2 92.9 Ours (2048 points) 90.7 93.5 Table 2.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This confirms our hypothesis that for certain density, with large k the Euclidean distance fails to approximate geodesic distance, destroying the geometry of each ... | p. 8 (4 EVALUATION) |
| body limitation/failure cue | We further evaluate the robustness of our model (trained on 1,024 points with k = 20) to point cloud density. | p. 8 (4 EVALUATION) |
| body limitation/failure cue | Our model is robust to partial data. | p. 9 (4 EVALUATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The batch size is 32 and the momentum is 0.9. | p. 7 (4 EVALUATION) |
| We use SGD with learning rate 0.1, and we reduce the learning rate until 0.001 using cosine annealing [Loshchilov and Hutter 2017]. | p. 7 (4 EVALUATION) |
| A distributed training scheme is further implemented on two NVIDIA TITAN X GPUs to maintain the training batch size. | p. 8 (4 EVALUATION) |
| We follow the same evaluation scheme as PointNet: The IoU of a shape is computed by averaging the IoUs of different parts occurring in ... | p. 8 (4 EVALUATION) |
| As shown in Figure 8, we take one red point from a source point cloud and compute its distance in feature space to points ... | p. 9 (4 EVALUATION) |
| We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better ... | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 EVALUATION - extractive PDF cue:** This confirms our hypothesis that for certain density, with large k the Euclidean distance fails to approximate geodesic distance, destroying the geometry of each patch.
- **p. 8 / 4 EVALUATION - extractive PDF cue:** We further evaluate the robustness of our model (trained on 1,024 points with k = 20) to point cloud density.
- **p. 9 / 4 EVALUATION - extractive PDF cue:** Our model is robust to partial data.

- **PDF anchors reviewed:** datasets p. 8 (4 EVALUATION), p. 8 (4 EVALUATION), p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 9 (4 EVALUATION), p. 9 (4 EVALUATION), metrics p. 10 (4 EVALUATION), p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 8 (4 EVALUATION), p. 8 (4 EVALUATION), p. 9 (4 EVALUATION), baselines p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 8 (4 EVALUATION), p. 9 (4 EVALUATION), p. 10 (4 EVALUATION), p. 6 (Figure/Table caption), results p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 8 (4 EVALUATION), p. 8 (4 EVALUATION), p. 10 (4 EVALUATION), p. 10 (4 EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
