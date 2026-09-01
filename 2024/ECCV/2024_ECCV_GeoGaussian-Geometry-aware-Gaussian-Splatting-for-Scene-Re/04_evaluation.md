# Evaluation - GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (2) Splitting), p. 2 (Figure/Table caption)): After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to further improve the geometry of the ...

## Evaluation Body Digest

- **p. 7 / 2) Splitting - extractive PDF cue:** By jointly optimizing the normal alignment and depth consistency of the Gaussian point tangent space in the neighborhood, we can obtain Gaussian points with a ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method shows ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Geometry-aware strategies of our GeoGaussian. In smoothly connected areas, the parameterization of thin Gaussians contains clear geometry meanings in the mean vector and ...
- **p. 7 / 2) Splitting - extractive PDF cue:** Following the strategy of 3DGS [18], the goal of our designed loss functions is to create correct geometry and adjust incorrectly positioned Gaussians.
- **p. 7 / 2) Splitting - extractive PDF cue:** After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to further ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 2) Splitting | SYSTEM / EVALUATION SCOPE UNRESOLVED | After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to ... | p. 7 (2) Splitting) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 2) Splitting - extractive PDF cue:** By jointly optimizing the normal alignment and depth consistency of the Gaussian point tangent space in the neighborhood, we can obtain Gaussian points with a ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method shows ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Geometry-aware strategies of our GeoGaussian. In smoothly connected areas, the parameterization of thin Gaussians contains clear geometry meanings in the mean vector and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | By jointly optimizing the normal alignment and depth consistency of the Gaussian point tangent space in the neighborhood, we can obtain Gaussian points with ... | embodiment, simulator version and control stack | p. 7 (2) Splitting) |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 2: Geometry-aware strategies of our GeoGaussian. In smoothly connected areas, the parameterization of thin Gaussians contains clear geometry meanings in the mean vector ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Following the strategy of 3DGS [18], the goal of our designed loss functions is to create correct geometry and adjust incorrectly positioned Gaussians. | definition/direction/unit from same section | p. 7 (2) Splitting) |
| After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to ... | definition/direction/unit from same section | p. 7 (2) Splitting) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We then utilize the K-NN algorithm to detect the eight nearest neighbors around G , which are passed through a lter to remove outliers ... | component/input/data sensitivity | p. 7 (2) Splitting) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully ... | After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (2) Splitting), p. 2 (Figure/Table caption) |
| Primary metric/result | Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 2) Splitting - extractive PDF cue:** Due to our thin Gaussian representation, the new position  i+1 lies on the plane established by the normal and position vectors of Gi  ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Recently, 3D Gaussian Splatting (3DGS) [18] has gained significant attention in the community, which shows that the rendering speed in high-quality NVS tasks can be ...
- **p. 7 / 2) Splitting - extractive PDF cue:** Due to our thin Gaussian representation, the new position  i+1 lies on the plane established by the normal and position vectors of Gi  ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Through the learning rate and direction, the Gaussian map undergoes densification for continuous training. | p. 3 (1 Introduction) |
| GeoGaussian 3 spite a significant reduction in training time with these methods, improving rendering efficiency is still a pressing requirement for applications such as ... | p. 3 (1 Introduction) |
| Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular ... | p. 1 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method shows ...

- **PDF anchors reviewed:** datasets p. 7 (2) Splitting), metrics p. 2 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (2) Splitting), p. 7 (2) Splitting), baselines p. 2 (Figure/Table caption), results p. 7 (2) Splitting), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
