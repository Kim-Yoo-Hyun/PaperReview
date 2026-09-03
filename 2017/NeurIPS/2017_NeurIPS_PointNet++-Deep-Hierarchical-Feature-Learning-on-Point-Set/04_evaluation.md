# Evaluation - PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1706.02413; PDF retrieval source: https://arxiv.org/pdf/1706.02413. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4 Experiments), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 14 (Figure/Table caption), p. 5 (4 Experiments), p. 6 (Figure/Table caption)): Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet [20].

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive body cue:** We use five fold cross validation to acquire classification accuracy on this dataset. • ScanNet: 1513 scanned and reconstructed indoor scenes.
- **p. 5 / 4 Experiments - extractive body cue:** Datasets We evaluate on four datasets ranging from 2D objects (MNIST [11]), 3D objects (ModelNet40 [31] rigid object, SHREC15 [12] non-rigid object) to real 3D ...
- **p. 5 / 4 Experiments - extractive body cue:** In MNIST, we see a relative 60.8% and 34.6% error rate reduction 1See supplementary for more details on network architecture and experiment preparation.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Point cloud with random point dropout. Right: Curve showing advantage of our density adaptive strategy in dealing with non-uniform density. DP means ...
- **p. 5 / 4 Experiments - extractive body cue:** Object classification is evaluated by accuracy.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Scannet labeling accuracy. To validate that our approach is suitable for large scale point cloud analysis, we also evaluate on semantic scene labeling ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Effects of neighborhood choices. Evaluation metric is classification accuracy (%) on ModelNet 40 test set. C.3 Effect of Randomness in Farthest Point Sampling. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Visualization of a scan captured from a Structure Sensor (left: RGB; right: point cloud). One issue that still remains is how to generate ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 5); B Details in Experiments (p. 11); B.3 MNIST and ModelNet40 Experiment Details (p. 12); B.4 ScanNet Experiment Details (p. 12); B.5 SHREC15 Experiment Details (p. 12); C More Experiments (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet [20]. | p. 5 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: Left: Point cloud with random point dropout. Right: Curve showing advantage of our density adaptive strategy in dealing with non-uniform density. DP ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2: Illustration of our hierarchical feature learning architecture and its application for set segmentation and classification using points in 2D Euclidean space as ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6: Effects of randomness in FPS (using ModelNet40). C.4 Time and Space Complexity. Table 7 summarizes comparisons of time and space cost between ... | p. 14 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Object classification is evaluated by accuracy. | p. 5 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive body cue:** We use five fold cross validation to acquire classification accuracy on this dataset. • ScanNet: 1513 scanned and reconstructed indoor scenes.
- **p. 5 / 4 Experiments - extractive body cue:** Datasets We evaluate on four datasets ranging from 2D objects (MNIST [11]), 3D objects (ModelNet40 [31] rigid object, SHREC15 [12] non-rigid object) to real 3D ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Visualization of a scan captured from a Structure Sensor (left: RGB; right: point cloud). One issue that still remains is how to generate ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of our hierarchical feature learning architecture and its application for set segmentation and classification using points in 2D Euclidean space as an ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: (a) Multi-scale grouping (MSG); (b) Multi- resolution grouping (MRG). As discussed earlier, it is common that a point set comes with non- uniform ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: MNIST digit classification.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: ModelNet40 shape classification. 1024 points 512 points 256 points 128 points
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Point cloud with random point dropout. Right: Curve showing advantage of our density adaptive strategy in dealing with non-uniform density. DP means ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Scannet labeling accuracy. To validate that our approach is suitable for large scale point cloud analysis, we also evaluate on semantic scene labeling ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Scannet labeling results. [20] cap- tures the overall layout of the room correctly but fails to discover the furniture. Our ap- proach, in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use five fold cross validation to acquire classification accuracy on this dataset. • ScanNet: 1513 scanned and reconstructed indoor scenes. | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Task/environment | Datasets We evaluate on four datasets ranging from 2D objects (MNIST [11]), 3D objects (ModelNet40 [31] rigid object, SHREC15 [12] non-rigid object) to real ... | reset, timeout, object/scene variation | p. 5 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 3 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In MNIST, we see a relative 60.8% and 34.6% error rate reduction 1See supplementary for more details on network architecture and experiment preparation. | definition/direction/unit from same section | p. 5 (4 Experiments) |
| Figure 4: Left: Point cloud with random point dropout. Right: Curve showing advantage of our density adaptive strategy in dealing with non-uniform density. DP ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Object classification is evaluated by accuracy. | definition/direction/unit from same section | p. 5 (4 Experiments) |
| Figure 5: Scannet labeling accuracy. To validate that our approach is suitable for large scale point cloud analysis, we also evaluate on semantic scene ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 5: Effects of neighborhood choices. Evaluation metric is classification accuracy (%) on ModelNet 40 test set. C.3 Effect of Randomness in Farthest Point ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 1: Visualization of a scan captured from a Structure Sensor (left: RGB; right: point cloud). One issue that still remains is how to ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: Illustration of our hierarchical feature learning architecture and its application for set segmentation and classification using points in 2D Euclidean space as ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 6: Scannet labeling results. [20] cap- tures the overall layout of the room correctly but fails to discover the furniture. Our ap- proach, ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Scannet labeling accuracy. To validate that our approach is suitable for large scale point cloud analysis, we also evaluate on semantic scene ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 6: Effects of randomness in FPS (using ModelNet40). C.4 Time and Space Complexity. Table 7 summarizes comparisons of time and space cost between ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5: Effects of neighborhood choices. Evaluation metric is classification accuracy (%) on ModelNet 40 test set. C.3 Effect of Randomness in Farthest Point ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 6: Effects of randomness in FPS (using ModelNet40). C.4 Time and Space Complexity. Table 7 summarizes comparisons of time and space cost between ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Figure 2: Illustration of our hierarchical feature learning architecture and its application for set segmentation and classification using points in 2D Euclidean space as ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce a hierarchical neural network, named as PointNet++, to process a set of points sampled in a metric space in a hierarchical fashion. | Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet [20]. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4 Experiments), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 14 (Figure/Table caption), p. 5 (4 Experiments), p. 6 (Figure/Table caption) |
| Primary metric/result | Figure 4: Left: Point cloud with random point dropout. Right: Curve showing advantage of our density adaptive strategy in dealing with non-uniform density. DP ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiments - extractive body cue:** We follow the experiment setting in [5] and use 1201 scenes for training, 312 scenes for test.
- **p. 5 / 4 Experiments - extractive body cue:** 4.1 Point Set Classification in Euclidean Metric Space We evaluate our network on classifying point clouds sampled from both 2D (MNIST) and 3D (ModleNet40) Euclidean ...
- **p. 5 / 4 Experiments - extractive body cue:** In default we use 512 points for MNIST and 1024 points for ModelNet40.
- **p. 5 / 4 Experiments - extractive body cue:** In last row (ours normal) in Table 2, we use face normals as additional point features, where we also use more points (N = 5000) ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Point Feature Propagation for Set Segmentation In set abstraction layer, the original point set is subsampled.
- **p. 5 / 3 Method - extractive body cue:** In a feature propagation level, we propagate point features from Nl × (d + C) points to Nl-1 points where Nl-1 and Nl (with Nl ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6: Scannet labeling results. [20] cap- tures the overall layout of the room correctly but fails to discover the furniture. Our ap- proach, ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Note that PointNet (vanilla) in Table 2 is the the version in [20] that does not use transformation networks, which is equivalent to our ... | p. 5 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| SSG (ablated PointNet++ with single scale grouping in each level) fails to generalize to sparse sampling density while SSG+DP amends the problem by randomly ... | p. 6 (Method) |
| PointNet layer uses a mini-PointNet to encode local region patterns into feature vectors. | p. 3 (3 Method) |
| Ball query finds all points that are within a radius to the query point (an upper limit of K is set in implementation). | p. 3 (3 Method) |
| Each local region in the output is abstracted by its centroid and local feature that encodes the centroid's neighborhood. | p. 4 (3 Method) |
| [14] extracts geodesic moments as shape features and use a stacked sparse autoencoder to digest these features to predict shape category. | p. 7 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Scannet labeling results. [20] cap- tures the overall layout of the room correctly but fails to discover the furniture. Our ap- proach, in ...
- **p. 5 / 4 Experiments - extractive body cue:** Note that PointNet (vanilla) in Table 2 is the the version in [20] that does not use transformation networks, which is equivalent to our hierarchical ...

- **Evidence anchors reviewed:** datasets p. 5 (4 Experiments), p. 5 (4 Experiments), metrics p. 5 (4 Experiments), p. 6 (Figure/Table caption), p. 5 (4 Experiments), p. 6 (Figure/Table caption), p. 13 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), results p. 5 (4 Experiments), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 14 (Figure/Table caption), p. 5 (4 Experiments), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
