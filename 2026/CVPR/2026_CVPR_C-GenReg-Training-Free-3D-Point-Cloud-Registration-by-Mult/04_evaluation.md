# Evaluation - C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 6 (4.2. Method Evaluation), p. 8 (Figure/Table caption), p. 2 (4. We achieve SOTA zero-shot results across indoor RGB-D), p. 6 (4.1. Experimental Settings)): Although this comparison is not strictly fair, since C-GenReg relies solely on 3D point cloud inputs, it is noteworthy that C-GenReg achieves comparable results to ZeroMatch and even outperforms PointMBF.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** For outdoor evaluation, we employ the Waymo Open Dataset [24], which contains large-scale LiDAR scans, and serves as a generalization benchmark for outdoor registration tasks.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** We evaluate our method on two benchmark types: indoor datasets captured by depth sensors and outdoor dataset acquired by LiDAR.
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** To evaluate cross-dataset generalization, we benchmark all methods on the ScanNet indoor registration benchmarks (Tab.
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** Rotation and translation accuracy (% of pairs within RRE/RTE thresholds in deg and cm respectively) and mean/median error on the ScanNet Hard and ScanNet SuperGlue ...
- **p. 2 / 4. We achieve SOTA zero-shot results across indoor RGB-D - extractive PDF cue:** benchmarks (3DMatch, ScanNet) and, for the first time, demonstrate a generative registration framework that successfully operates on real outdoor LiDAR data (Waymo).
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** For each benchmark, we report both the mean and median values of these errors, as well as the registration accuracy - the percentage of registration ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Features Fusion Accuracy ↑ Error ↓ Accuracy ↑ Error ↓ 5 10
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** Best results are in bold. achieves superior rotation accuracy, demonstrating the benefit of our probabilistic fusion.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. We achieve SOTA zero-shot results across indoor RGB-D (p. 2); 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6); 4.2. Method Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Method Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although this comparison is not strictly fair, since C-GenReg relies solely on 3D point cloud inputs, it is noteworthy that C-GenReg achieves comparable results ... | p. 7 (4.2. Method Evaluation) |
| 4.2. Method Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Best results are in bold. achieves superior rotation accuracy, demonstrating the benefit of our probabilistic fusion. | p. 7 (4.2. Method Evaluation) |
| 4.2. Method Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite this, C-GenReg achieves the best overall performance across most rotation and translation metrics. | p. 6 (4.2. Method Evaluation) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4. Ablation Study on the 3DMatch Benchmark. Top: impact of different Vision Foundation Models (no geometric features or fusion). Bottom: impact of geometric ... | p. 8 (Figure/Table caption) |
| 4. We achieve SOTA zero-shot results across indoor RGB-D | EMPIRICAL / SOURCE-REPORTED EVALUATION | benchmarks (3DMatch, ScanNet) and, for the first time, demonstrate a generative registration framework that successfully operates on real outdoor LiDAR data (Waymo). | p. 2 (4. We achieve SOTA zero-shot results across indoor RGB-D) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** For outdoor evaluation, we employ the Waymo Open Dataset [24], which contains large-scale LiDAR scans, and serves as a generalization benchmark for outdoor registration tasks.
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** We evaluate our method on two benchmark types: indoor datasets captured by depth sensors and outdoor dataset acquired by LiDAR.
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** To evaluate cross-dataset generalization, we benchmark all methods on the ScanNet indoor registration benchmarks (Tab.
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** Rotation and translation accuracy (% of pairs within RRE/RTE thresholds in deg and cm respectively) and mean/median error on the ScanNet Hard and ScanNet SuperGlue ...
- **p. 2 / 4. We achieve SOTA zero-shot results across indoor RGB-D - extractive PDF cue:** benchmarks (3DMatch, ScanNet) and, for the first time, demonstrate a generative registration framework that successfully operates on real outdoor LiDAR data (Waymo).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. C-GenReg: A training-free point cloud registration frame- work. The pipeline operates in two parallel branches: (1) Generated- RGB Branch - a World Foundation ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. C-GenReg Overview: A training-free, zero-shot point cloud registration framework with two parallel branches. (1) Generated-RGB Branch - source and target point clouds are ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. C-GenReg qualitative example on 3DMatch. Generated source and target images with a subset of matched points (color-coded correspondences), and the corresponding matches visualized ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific VFM ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. 3DMatch Benchmark. Rotation and translation accuracy (% of pairs within RRE/RTE thresholds in deg and cm respectively) and mean/median error across different methods. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. ScanNet Benchmarks. Rotation and translation accuracy (% of pairs within RRE/RTE thresholds in deg and cm respectively) and mean/median error on the ScanNet ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Waymo Outdoor Registration Benchmark. Rotation (deg) and translation (m) accuracy/error. Best results are in bold. achieves superior rotation accuracy, demonstrating the benefit of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation Study on the 3DMatch Benchmark. Top: impact of different Vision Foundation Models (no geometric features or fusion). Bottom: impact of geometric feature ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For outdoor evaluation, we employ the Waymo Open Dataset [24], which contains large-scale LiDAR scans, and serves as a generalization benchmark for outdoor registration ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Task/environment | We evaluate our method on two benchmark types: indoor datasets captured by depth sensors and outdoor dataset acquired by LiDAR. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Settings), p. 7 (4.2. Method Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2. C-GenReg - Overview), p. 4 (3.2. C-GenReg - Overview) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each benchmark, we report both the mean and median values of these errors, as well as the registration accuracy - the percentage of ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Rotation (deg) and translation (m) accuracy/error. | definition/direction/unit from same section | p. 7 (4.2. Method Evaluation) |
| Features Fusion Accuracy ↑ Error ↓ Accuracy ↑ Error ↓ 5 10 | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Best results are in bold. achieves superior rotation accuracy, demonstrating the benefit of our probabilistic fusion. | definition/direction/unit from same section | p. 7 (4.2. Method Evaluation) |
| Figure 3. C-GenReg qualitative example on 3DMatch. Generated source and target images with a subset of matched points (color-coded correspondences), and the corresponding matches ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| benchmarks (3DMatch, ScanNet) and, for the first time, demonstrate a generative registration framework that successfully operates on real outdoor LiDAR data (Waymo). | definition/direction/unit from same section | p. 2 (4. We achieve SOTA zero-shot results across indoor RGB-D) |
| Despite this, C-GenReg achieves the best overall performance across most rotation and translation metrics. | definition/direction/unit from same section | p. 6 (4.2. Method Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| CGenReg is compared against both the hand-crafted descriptor FPFH [22] and several state-of-the-art (SOTA) learning-based baselines, including GeoTransformer [20], FCGF [4], Predator [11], RoITr ... | comparison identity and matched condition | p. 6 (4.2. Method Evaluation) |
| Although this comparison is not strictly fair, since C-GenReg relies solely on 3D point cloud inputs, it is noteworthy that C-GenReg achieves comparable results ... | comparison identity and matched condition | p. 7 (4.2. Method Evaluation) |
| It reduces the mean RTE by nearly half compared to GeoTransformer and consistently 3009 | comparison identity and matched condition | p. 6 (4.2. Method Evaluation) |
| In particular, it ranks first or second on most of the metrics, with GPCR slightly outperforming in median RRE and mean RTE. | comparison identity and matched condition | p. 7 (4.2. Method Evaluation) |
| Table 4. Ablation Study on the 3DMatch Benchmark. Top: impact of different Vision Foundation Models (no geometric features or fusion). Bottom: impact of geometric ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| All models in the pipeline are kept frozen with their publicly released pretrained weights, without any additional fine-tuning. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| We perform an extensive ablation studies to analyze the contribution of each component in the C-GenReg pipeline. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Table 4. Ablation Study on the 3DMatch Benchmark. Top: impact of different Vision Foundation Models (no geometric features or fusion). Bottom: impact of geometric ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| For reference, we additionally report C-GenReg-Oracle, which replaces the generated RGB with the real RGB input to provide an empirical upper bound on our ... | component/input/data sensitivity | p. 7 (4.2. Method Evaluation) |
| Figure 2. C-GenReg Overview: A training-free, zero-shot point cloud registration framework with two parallel branches. (1) Generated-RGB Branch - source and target point clouds ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g. | Although this comparison is not strictly fair, since C-GenReg relies solely on 3D point cloud inputs, it is noteworthy that C-GenReg achieves comparable results ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 6 (4.2. Method Evaluation), p. 8 (Figure/Table caption), p. 2 (4. We achieve SOTA zero-shot results across indoor RGB-D), p. 6 (4.1. Experimental Settings) |
| Primary metric/result | Best results are in bold. achieves superior rotation accuracy, demonstrating the benefit of our probabilistic fusion. | numeric claim only at cited anchor | p. 7 (4.2. Method Evaluation) |

- Numeric sentences retained from the body:
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** We follow the ScanNet Hard protocol introduced in [12, 13], where source and target frames are 50 frames apart, resulting in significantly lower overlap.
- **p. 7 / 4.2. Method Evaluation - extractive PDF cue:** We sample 1,500 registration pairs from the validation split, selecting frame pairs at least 50 frames apart and within 30m based on ground-truth ego motion.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additional implementation details including runtime analysis are provided in the supplementary material. | p. 6 (4.1. Experimental Settings) |
| Since GPCR code is unavailable, it is excluded from this comparison. | p. 7 (4.2. Method Evaluation) |
| Generated source and target images with a subset of matched points (color-coded correspondences), and the corresponding matches visualized on the input point clouds. | p. 4 (3.2. C-GenReg - Overview) |
| In parallel, the geometric branch encodes the raw point clouds using a pretrained registration-oriented 3D feature extractor, yielding complementary geometric descriptors. | p. 4 (3.2. C-GenReg - Overview) |
| MASt3R operates on pairs of source and target images through a cross-attention-based decoder, where the extracted features for each image are conditioned on the ... | p. 5 (3.3. Generated-RGB Branch) |
| To approximate the modality-specific correspondence posterior Pr(Mij/Sm ij ), where m∈{geo,img}, we first compute the source-target feature similarity matrices for each modality and then ... | p. 5 (3.5. Match-then-Fuse Probabilistic Fusion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific VFM ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 2 (4. We achieve SOTA zero-shot results across indoor RGB-D), metrics p. 6 (4.1. Experimental Settings), p. 7 (4.2. Method Evaluation), p. 8 (4.3. Ablation Studies), p. 7 (4.2. Method Evaluation), p. 4 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 6 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 6 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 8 (Figure/Table caption), results p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 6 (4.2. Method Evaluation), p. 8 (Figure/Table caption), p. 2 (4. We achieve SOTA zero-shot results across indoor RGB-D), p. 6 (4.1. Experimental Settings).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
