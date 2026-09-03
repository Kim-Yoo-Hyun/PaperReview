# Evaluation - GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (Figure/Table caption), p. 1 (Body text (section not recovered)), p. 11 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are given in Appendix. Training and Evaluation. ...

## Evaluation Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- **p. 1 / 1 Introduction - extractive body cue:** Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular research ...
- **p. 2 / 1 Introduction - extractive body cue:** 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets.
- **p. 2 / 1 Introduction - extractive body cue:** NVS methods typically represent 3D scenes implicitly [28, 42] or explicitly [4, 16] based on multiple 2D views and corresponding camera poses.
- **p. 4 / 1 Introduction - extractive body cue:** Li et al. - Evaluations on the public datasets demonstrate that the proposed method improves rendering quality compared to state-of-the-art Gaussian Splatting methods.
- **p. 3 / 1 Introduction - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) [18] has gained significant attention in the community, which shows that the rendering speed in high-quality NVS tasks can be ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are given ...
- **p. 2 / 1 Introduction - extractive body cue:** Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased mesh ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are ... | p. 13 (Figure/Table caption) |
| Body text (section not recovered) | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | p. 1 (Body text (section not recovered)) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Comparison of rendering on the Replica dataset. The position and orientation of viewpoints used in training and evaluation are illustrated in Appendix. ... | p. 11 (Figure/Table caption) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | To address the heavy computational burden and intensive memory consumption, recent improvements have been made using sparse volumes [21], hash tables [27], and hierarchical ... | p. 2 (1 Introduction) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased ... | p. 2 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 1 / Body text (section not recovered) - extractive body cue:** Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- **p. 1 / 1 Introduction - extractive body cue:** Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular research ...
- **p. 2 / 1 Introduction - extractive body cue:** 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets.
- **p. 2 / 1 Introduction - extractive body cue:** NVS methods typically represent 3D scenes implicitly [28, 42] or explicitly [4, 16] based on multiple 2D views and corresponding camera poses.
- **p. 4 / 1 Introduction - extractive body cue:** Li et al. - Evaluations on the public datasets demonstrate that the proposed method improves rendering quality compared to state-of-the-art Gaussian Splatting methods.
- **p. 3 / 1 Introduction - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) [18] has gained significant attention in the community, which shows that the rendering speed in high-quality NVS tasks can be ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method shows ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Geometry-aware strategies of our GeoGaussian. In smoothly connected areas, the parameterization of thin Gaussians contains clear geometry meanings in the mean vector and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 3: Comparisons of novel view rendering on public datasets. At some challenging viewpoints having bigger differences in translation and orientation motions compared with training ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Comparison of different solutions for novel view rendering on the Replica dataset, GeoGaussian is fed by point clouds, initial camera poses, and monocular ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 4. Similarly, we use only 10% of the training dataset for training, referred to as R1 (10%). It is important to note that the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Comparison of rendering on the Replica dataset. The position and orientation of viewpoints used in training and evaluation are illustrated in Appendix. Evaluation ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident in ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 3: Rendering performance comparison on the TUM RGB-D datasets. 4.5

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | embodiment, simulator version and control stack | p. 1 (Body text (section not recovered)), p. 1 (1 Introduction) |
| Task/environment | Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular ... | reset, timeout, object/scene variation | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (1 Introduction), p. 1 (Body text (section not recovered)) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased ... | definition/direction/unit from same section | p. 2 (1 Introduction) |
| Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Through the learning rate and direction, the Gaussian map undergoes densification for continuous training. | definition/direction/unit from same section | p. 3 (1 Introduction) |
| Fig. 2: Geometry-aware strategies of our GeoGaussian. In smoothly connected areas, the parameterization of thin Gaussians contains clear geometry meanings in the mean vector ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 2: Comparison of rendering on the Replica dataset. The position and orientation of viewpoints used in training and evaluation are illustrated in Appendix. ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( [8,18]) shows better performance in terms of training speed and rendering quality. | definition/direction/unit from same section | p. 1 (1 Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Li et al. - Evaluations on the public datasets demonstrate that the proposed method improves rendering quality compared to state-of-the-art Gaussian Splatting methods. | comparison identity and matched condition | p. 4 (1 Introduction) |
| Fig. 3: Comparisons of novel view rendering on public datasets. At some challenging viewpoints having bigger differences in translation and orientation motions compared with ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 2: Comparison of rendering on the Replica dataset. The position and orientation of viewpoints used in training and evaluation are illustrated in Appendix. ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | comparison identity and matched condition | p. 1 (Body text (section not recovered)) |
| Compared to learning-based mesh methods, NeRF [25] proposes a continuous volumetric function representation using a multi-layer perceptron (MLP), which produces high-quality renderings with impressive ... | comparison identity and matched condition | p. 2 (1 Introduction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The step is supported by accumulating the gradient descent direction of the origin's position µ, and then the component of the direction that is ... | component/input/data sensitivity | p. 3 (1 Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully ... | Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (Figure/Table caption), p. 1 (Body text (section not recovered)), p. 11 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Primary metric/result | Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | numeric claim only at cited anchor | p. 1 (Body text (section not recovered)) |

- Numeric sentences retained from the body:
- **p. 3 / 1 Introduction - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) [18] has gained significant attention in the community, which shows that the rendering speed in high-quality NVS tasks can be ...
- **p. 3 / 1 Introduction - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) [18] has gained significant attention in the community, which shows that the rendering speed in high-quality NVS tasks can be ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This degradation significantly affects the rendering quality of novel views that deviate significantly from the viewpoints in the training data. | p. 1 (Body text (section not recovered)) |
| body limitation/failure cue | However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation ... | p. 2 (1 Introduction) |
| body limitation/failure cue | Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident ... | p. 12 (Figure/Table caption) |

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

- **p. 1 / Body text (section not recovered) - extractive body cue:** This degradation significantly affects the rendering quality of novel views that deviate significantly from the viewpoints in the training data.
- **p. 2 / 1 Introduction - extractive body cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident in ...

- **Evidence anchors reviewed:** datasets p. 1 (Body text (section not recovered)), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), metrics p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (Figure/Table caption), p. 3 (1 Introduction), p. 5 (Figure/Table caption), p. 11 (Figure/Table caption), baselines p. 4 (1 Introduction), p. 9 (Figure/Table caption), p. 11 (Figure/Table caption), p. 12 (Figure/Table caption), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), results p. 13 (Figure/Table caption), p. 1 (Body text (section not recovered)), p. 11 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
