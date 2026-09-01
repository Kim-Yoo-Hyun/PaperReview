# Evaluation - MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=efDNv5XvVo; PDF retrieval source: https://openreview.net/pdf/804e98743d0bf960af90c596755d72e4736d2c39.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments)): On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts LPIPS and DSIM by 33.8% and ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs-one with single appearance and two with ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Sparse Mip-NeRF 360 Dataset [33] contains 4 outdoor and 4 indoor scenes with a complex central object or area and a detailed background.
- **p. 22 / A.1.2 Comparison with prior benchmark - extractive PDF cue:** Additionally, our dataset contains scenes with 360-degree coverage by perspective cameras, whereas Phototourism is covered by face-forward images.
- **p. 8 / 4 Experiments - extractive PDF cue:** 4.4 Comparisons Table 2: Quantitative Comparison on sparse Mip-NeRF 360 dataset; bold numbers are the best, underscored second best.
- **p. 8 / 4 Experiments - extractive PDF cue:** In the Wild GT Pose Method LPIPSÓ DSIMÓ PSNRÒ SSIMÒ LPIPSÓ DSIMÓ DRGS[23] 0.588 0.273 19.16 0.516 0.544 0.253 DNGS[9] 0.503 0.193 19.79 0.588 0.466 ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 5 present results on these benchmarks.
- **p. 9 / 4 Experiments - extractive PDF cue:** On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts LPIPS ...
- **p. 22 / A.1 Sparse unbounded drone dataset - extractive PDF cue:** (a) Sunny (b) Snowy (c) Cloudy (d) Low-light Figure 6: Dataset visualizations

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); A.1 Sparse unbounded drone dataset (p. 22); A.1.2 Comparison with prior benchmark (p. 22); A.2 Experiments and visualizations (p. 22); A.3 Implementation details (p. 24); A.6 In-the-wild evaluation (p. 26); A.6.2 Evaluation metrics (p. 27).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We identify that incorporating our semantic depth alignment initialization significantly improved the metrics with 0.8 dB in PSNR, 0.046 in SSIM, -0.031 in LPIPS, ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | All proposed components are complementary, and the best results are achieved when combined. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Visualizations of rendering with different point cloud initializations. dense point cloud, usually millions of points. To utilize DUSt3R points, we align them ... | p. 23 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7: Experiments in 12-view setting, where each appearance has 3 images. MS-GS continues to outperform other methods. The metrics are reported as the ... | p. 25 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs-one with single appearance and two with ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Sparse Mip-NeRF 360 Dataset [33] contains 4 outdoor and 4 indoor scenes with a complex central object or area and a detailed background.
- **p. 22 / A.1.2 Comparison with prior benchmark - extractive PDF cue:** Additionally, our dataset contains scenes with 360-degree coverage by perspective cameras, whereas Phototourism is covered by face-forward images.
- **p. 8 / 4 Experiments - extractive PDF cue:** 4.4 Comparisons Table 2: Quantitative Comparison on sparse Mip-NeRF 360 dataset; bold numbers are the best, underscored second best.
- **p. 8 / 4 Experiments - extractive PDF cue:** In the Wild GT Pose Method LPIPSÓ DSIMÓ PSNRÒ SSIMÒ LPIPSÓ DSIMÓ DRGS[23] 0.588 0.273 19.16 0.516 0.544 0.253 DNGS[9] 0.503 0.193 19.79 0.588 0.466 ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 5 present results on these benchmarks.
- **p. 9 / 4 Experiments - extractive PDF cue:** On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts LPIPS ...
- **p. 22 / A.1 Sparse unbounded drone dataset - extractive PDF cue:** (a) Sunny (b) Snowy (c) Cloudy (d) Low-light Figure 6: Dataset visualizations

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: With 20 input views, DNGS and FSGS produce overly smooth rendering in regions lacking support from sparse point cloud initialization. For scenes with ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our depth prior initialization of MS-GS. Semantic masks and corresponding SfM point depth within each mask are obtained through our SfM-prompted ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of our multi-view geometry-guided supervision of MS-GS. Initialized from our proposed dense point cloud, we first create virtual views between training cameras. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Ablation studies on different components of MS-GS. The metrics are reported as the average on the Sparse Unbounded drone dataset; bold numbers are ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Novel view synthesis results when components are added sequentially. Please zoom in if possible for better visualization. 4.3
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative Comparison on sparse Mip-NeRF 360 dataset; bold numbers are the best, underscored second best. We only evaluate LPIPS and DSIM for in-the-wild ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative Comparison on sparse unbounded drone dataset. Methods: renders each test view with the appearance embedding taken from the training image that is ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Quantitative Comparison on sparse Phototourism dataset. Methods; optimize appearance embedding on the left half of the test image and evaluate on the other ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs-one with single appearance and two ... | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | Sparse Mip-NeRF 360 Dataset [33] contains 4 outdoor and 4 indoor scenes with a complex central object or area and a detailed background. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 22 (A.1.2 Comparison with prior benchmark) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although SparseGS and FSGS improve the rendering quality through floater pruning, score distillation regularization, and the densification strategy. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The metrics are reported as the average on the Sparse Unbounded drone dataset; bold numbers are the best, underscored second best. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| 4.4 Comparisons Table 2: Quantitative Comparison on sparse Mip-NeRF 360 dataset; bold numbers are the best, underscored second best. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Without sufficient constraints, the appearance-affine head and uncertainty weighting in WildGaussians can absorb photometric error instead of correcting structures, leaving as off-view aliasing and ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| A previous approach [11] has tried to perform re-triangulation based on known train poses, but does not account for pose inaccuracy. | definition/direction/unit from same section | p. 26 (A.6 In-the-wild evaluation) |
| This analysis indicates that DSIM is an appropriate metric for in-the-wild evaluations: it avoids over-penalising inevitable alignment errors while still capturing real perceptual degradation. | definition/direction/unit from same section | p. 28 (A.6.2 Evaluation metrics) |
| Figure 9: Error maps after alignment. Brighter means higher error. A.2.2 Edge cases (a) GT (b) Render (c) GT (d) Render | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Figure 12: Illustration of Coordinate Alignment. We first compute the transformation M ˚ between train cameras in two coordinate systems Cref train and Cinput ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| We refer to 3DGS augmented with multi-appearance capabilities using per-image embeddings and Gaussian feature embeddings as the baseline and report its metrics in the ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| The baseline introduced in our ablation study Section 4.3 uses the same Splatfacto model. | comparison identity and matched condition | p. 24 (A.3 Implementation details) |
| Figure 8: Visualizations of rendering with different point cloud initializations. dense point cloud, usually millions of points. To utilize DUSt3R points, we align them ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Table 7: Experiments in 12-view setting, where each appearance has 3 images. MS-GS continues to outperform other methods. The metrics are reported as the ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| 4.1 Datasets We evaluate the performance of MS-GS and current SoTA methods on three real-world scenes with sparse inputs-one with single appearance and two ... | comparison identity and matched condition | p. 7 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 Ablation Study We conduct an ablation study to validate the effectiveness of our method in Table 1 and Fig. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Without sufficient constraints, the appearance-affine head and uncertainty weighting in WildGaussians can absorb photometric error instead of correcting structures, leaving as off-view aliasing and ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| While recent methods leverage uncertainty masks to remove transients and allow other observations to fill in the blank, often no other observations exist under ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Table 1: Ablation studies on different components of MS-GS. The metrics are reported as the average on the Sparse Unbounded drone dataset; bold numbers ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| The baseline introduced in our ablation study Section 4.3 uses the same Splatfacto model. | component/input/data sensitivity | p. 24 (A.3 Implementation details) |
| Figure 10: As MS-GS favors more accurate local alignment, areas without dense initialization can introduce artifacts in (a) and (b). Specular highlights can be ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic ... | On the sparse unbounded-drone dataset, our approach significantly outperforms the SoTA methods with improvements of 2.54 dB in PSNR, 0.089 in SSIM, and cuts ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments) |
| Primary metric/result | We identify that incorporating our semantic depth alignment initialization significantly improved the metrics with 0.8 dB in PSNR, 0.046 in SSIM, -0.031 in LPIPS, ... | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 24 / A.3 Implementation details - extractive PDF cue:** The appearance MLP consists of 3 layers of 64 hidden units.
- **p. 24 / A.3 Implementation details - extractive PDF cue:** The appearance MLP consists of 3 layers of 64 hidden units.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Specific techniques have to be developed to solve these limitations, which we leave as future work. | p. 9 (4 Experiments) |
| body limitation/failure cue | We identify that one of the limitations of 3DGS-based methods in sparse-view synthesis is the sparse point cloud initialization. | p. 10 (6 Conclusion) |
| body limitation/failure cue | 5 Limitations First, MS-GS is not designed for handling transient objects, which is especially difficult under sparse views due to increased uncertainty and ambiguities ... | p. 9 (4 Experiments) |
| body limitation/failure cue | Jointly, MS-GS offers a robust solution under challenges of limited viewpoints and varying appearances that naturally arise in real-world data. | p. 10 (6 Conclusion) |
| body limitation/failure cue | A previous approach [11] has tried to perform re-triangulation based on known train poses, but does not account for pose inaccuracy. | p. 26 (A.6 In-the-wild evaluation) |
| body limitation/failure cue | This analysis indicates that DSIM is an appropriate metric for in-the-wild evaluations: it avoids over-penalising inevitable alignment errors while still capturing real perceptual degradation. | p. 28 (A.6.2 Evaluation metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We strongly encourage the readers to inspect the supplement for more details and analysis on the in-the-wild evaluation, metrics, and implementation. | p. 7 (4 Experiments) |
| 4.2 Evaluation and Implementation Most sparse-view synthesis methods [34, 3, 4, 6, 7, 8, 5, 9] assume ground-truth (GT) camera poses, i.e., calibration with ... | p. 7 (4 Experiments) |
| Computation In the Wild GT Pose Method GPU hrs. | p. 9 (4 Experiments) |
| Furthermore, our design is lightweight, requiring >3× less GPU time for training over Wild-GS and rendering at 300+ FPS. | p. 9 (4 Experiments) |
| Results are obtained with the NVIDIA RTX A5500 GPU. | p. 24 (A.3 Implementation details) |
| The same hyperparameters are maintained throughout the experiments. | p. 24 (A.3 Implementation details) |
| (2) While this formulation can be efficiently computed to construct a very dense point cloud, such a point cloud will be very noisy. | p. 5 (3 Method) |
| A feature fusion network MLPθ takes these two appearance components to decode the RGB colors of 3D Gaussians c P RNˆ3 : c " ... | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive PDF cue:** Specific techniques have to be developed to solve these limitations, which we leave as future work.
- **p. 10 / 6 Conclusion - extractive PDF cue:** We identify that one of the limitations of 3DGS-based methods in sparse-view synthesis is the sparse point cloud initialization.
- **p. 9 / 4 Experiments - extractive PDF cue:** 5 Limitations First, MS-GS is not designed for handling transient objects, which is especially difficult under sparse views due to increased uncertainty and ambiguities in ...
- **p. 10 / 6 Conclusion - extractive PDF cue:** Jointly, MS-GS offers a robust solution under challenges of limited viewpoints and varying appearances that naturally arise in real-world data.
- **p. 26 / A.6 In-the-wild evaluation - extractive PDF cue:** A previous approach [11] has tried to perform re-triangulation based on known train poses, but does not account for pose inaccuracy.
- **p. 28 / A.6.2 Evaluation metrics - extractive PDF cue:** This analysis indicates that DSIM is an appropriate metric for in-the-wild evaluations: it avoids over-penalising inevitable alignment errors while still capturing real perceptual degradation.

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 22 (A.1.2 Comparison with prior benchmark), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), metrics p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 26 (A.6 In-the-wild evaluation), p. 28 (A.6.2 Evaluation metrics), baselines p. 9 (4 Experiments), p. 8 (4 Experiments), p. 24 (A.3 Implementation details), p. 23 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments), results p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 23 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
