# Evaluation - BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.13542; PDF retrieval source: https://arxiv.org/pdf/2205.13542. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption)): Consequently, BEVFusion can achieve the same performance with much smaller resolution for the camera inputs, resulting in significantly lower MACs.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate our method on nuScenes [59] and Waymo [60], which are large-scale datasets for 3D perception with >40k annotated scenes.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop GPU.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate BEVFusion for camera-LiDAR fusion on 3D object detection and BEV map segmentation, covering both geometric- and semantic-oriented tasks.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Our framework can be easily extended to support other types of sensors (such as radars and event-based cameras) and other 3D perception tasks (such as ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We use the mean average precision (mAP) across 10 foreground classes and the nuScenes detection score (NDS) as our detection metrics.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** As different classes may have overlappings (e.g. car-parking area is also drivable), we evaluate the binary segmentation performance for each class separately and select the ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: BEVFusion unifies camera and LiDAR features in a shared BEV space instead of mapping one modality to the other. It preserves camera's semantic ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., sparser ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 7 Results (p. 3); IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Consequently, BEVFusion can achieve the same performance with much smaller resolution for the camera inputs, resulting in significantly lower MACs. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | III: BEVFusion outperforms the state-of-the-art multi-sensor fusion methods by 13.6% on BEV map segmentation on nuScenes (val) with consistent improvements across different categories. | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1: BEVFusion unifies camera and LiDAR features in a shared BEV space instead of mapping one modality to the other. It preserves camera's ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 2: BEVFusion extracts features from multi-modal inputs and converts them into a shared bird's-eye view (BEV) space efficiently using view transformations. It fuses ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate our method on nuScenes [59] and Waymo [60], which are large-scale datasets for 3D perception with >40k annotated scenes.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop GPU.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate BEVFusion for camera-LiDAR fusion on 3D object detection and BEV map segmentation, covering both geometric- and semantic-oriented tasks.
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Our framework can be easily extended to support other types of sensors (such as radars and event-based cameras) and other 3D perception tasks (such as ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: BEVFusion unifies camera and LiDAR features in a shared BEV space instead of mapping one modality to the other. It preserves camera's semantic ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: BEVFusion extracts features from multi-modal inputs and converts them into a shared bird's-eye view (BEV) space efficiently using view transformations. It fuses the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Camera-to-BEV transformation (a) is the key step to perform sensor fusion in the unified BEV space. Existing implementation is extremely slow and takes ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., sparser ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on nuScenes [59] and Waymo [60], which are large-scale datasets for 3D perception with >40k annotated scenes. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop GPU. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the mean average precision (mAP) across 10 foreground classes and the nuScenes detection score (NDS) as our detection metrics. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| As different classes may have overlappings (e.g. car-parking area is also drivable), we evaluate the binary segmentation performance for each class separately and select ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1: BEVFusion unifies camera and LiDAR features in a shared BEV space instead of mapping one modality to the other. It preserves camera's ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We evaluate BEVFusion for camera-LiDAR fusion on 3D object detection and BEV map segmentation, covering both geometric- and semantic-oriented tasks. | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| BEVFusion outperforms the previous state-of-the-art multi-modal detector, DeepFusion [3] with 60% of input frames. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| III: BEVFusion outperforms the state-of-the-art multi-sensor fusion methods by 13.6% on BEV map segmentation on nuScenes (val) with consistent improvements across different categories. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We use a single model without any test-time augmentation for both val and test results. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup. | Consequently, BEVFusion can achieve the same performance with much smaller resolution for the camera inputs, resulting in significantly lower MACs. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Primary metric/result | III: BEVFusion outperforms the state-of-the-art multi-sensor fusion methods by 13.6% on BEV map segmentation on nuScenes (val) with consistent improvements across different categories. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 3 / 7 Results - extractive PDF cue:** 0 20 40 500ms Interval Reduction: 22.1× Precomputation: 1.9× 4.8ms 12.0ms 45.1ms 136.8ms 512.1ms 2127.3ms 1/16 FPN 1/8 FPN 1/4 FPN : Stored to DRAM ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We downsample camera images to 256×704 and voxelize the LiDAR point cloud with 0.075m (for detection) and 0.1m (for segmentation).
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | On the one hand, the LiDARto-BEV projection flattens the sparse LiDAR features along the height dimension, thus does not create geometric distortion in Figure ... | p. 3 (A C) |
| body limitation/failure cue | Our method could potentially benefit from more accurate depth estimation (e.g., supervising the view transformer with groundtruth depth [42], [53]), which we leave for ... | p. 4 (A C) |
| body limitation/failure cue | This kernel removes the dependency between outputs (thus does not require multi-level tree reduction) and avoids writing the partial sums to the DRAM, reducing ... | p. 4 (A C) |
| body limitation/failure cue | IV: BEVFusion is robust under different lighting and weather conditions, significantly boosting the performance single-modality models under challenging rainy(+10.7) and nighttime(+12.8) scenes. | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We also measure the single-inference #MACs and latency on an RTX3090 GPU for all opensource methods. | p. 5 (IV. EXPERIMENTS) |
| As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop GPU. | p. 5 (IV. EXPERIMENTS) |
| Given different sensory inputs, we first apply modality-specific encoders to extract their features. | p. 2 (III. METHOD) |
| We then apply the convolution-based BEV encoder to the unified BEV features to alleviate the local misalignment between different features. | p. 2 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / A C - extractive PDF cue:** On the one hand, the LiDARto-BEV projection flattens the sparse LiDAR features along the height dimension, thus does not create geometric distortion in Figure 1a.
- **p. 4 / A C - extractive PDF cue:** Our method could potentially benefit from more accurate depth estimation (e.g., supervising the view transformer with groundtruth depth [42], [53]), which we leave for future ...
- **p. 4 / A C - extractive PDF cue:** This kernel removes the dependency between outputs (thus does not require multi-level tree reduction) and avoids writing the partial sums to the DRAM, reducing the ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** IV: BEVFusion is robust under different lighting and weather conditions, significantly boosting the performance single-modality models under challenging rainy(+10.7) and nighttime(+12.8) scenes.

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (IV. EXPERIMENTS), baselines p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), results p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
