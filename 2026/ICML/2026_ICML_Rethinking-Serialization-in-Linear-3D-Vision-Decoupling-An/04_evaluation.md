# Evaluation - Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=MSVQM8Ub2y; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/328620. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), p. 7 (4.3. Analysis and Ablation), p. 8 (4.4. Efficiency Analysis)): Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance.

## Evaluation Body Digest

- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 94.21 ...
- **p. 8 / 4.3. Analysis and Ablation - extractive PDF cue:** In the current setting, the separation is clear: the two indoor scene datasets have substantially smaller normalized distances than ScanObjectNN, and their best-performing modes are ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate AnIsoNet on three benchmarks spanning different geometric regimes: (1) S3DIS (Armeni et al., 2016) Area 5: Dense indoor scenes with approximately 100K points ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Dense-scene datasets (S3DIS and ScanNetV2) use Identity Mode, whereas the sparse-object dataset ScanObjectNN uses Morton Mode.
- **p. 6 / 4.2. Main Results - extractive PDF cue:** In contrast to the dense-scene benchmarks, this sparse-object setting benefits from retaining a lightweight spatial prior through Morton serialization when local geometric context is limited.
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Cross-regime validation of dataset-level mode selection.
- **p. 8 / 4.3. Analysis and Ablation - extractive PDF cue:** Dataset ˆσk Best mode S3DIS 0.0060 Identity ScanNetV2 0.0042 Identity ScanObjectNN 0.0251 Morton
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** (2) ScanNetV2 (Dai et al., 2017): Large-scale indoor dataset with 1,513 annotated 3D scans.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Main Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Efficiency Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance. | p. 8 (4.4. Efficiency Analysis) |
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | AnIsoNet achieves strong performance among linear-complexity methods. | p. 6 (4.1. Experimental Setup) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | AnIsoNet achieves 94.21% overall accuracy, the best result among the compared linear architectures without external pre-training. | p. 6 (4.2. Main Results) |
| 4.3. Analysis and Ablation | EMPIRICAL / SOURCE-REPORTED EVALUATION | AnIsoNet outperforms recent MLP and SSM baselines. | p. 7 (4.3. Analysis and Ablation) |
| 4.3. Analysis and Ablation | EMPIRICAL / SOURCE-REPORTED EVALUATION | This indicates that GISA provides the larger gain in this dense-scene setting, while LAGM still contributes a consistent improvement. | p. 7 (4.3. Analysis and Ablation) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 94.21 ...
- **p. 8 / 4.3. Analysis and Ablation - extractive PDF cue:** In the current setting, the separation is clear: the two indoor scene datasets have substantially smaller normalized distances than ScanObjectNN, and their best-performing modes are ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate AnIsoNet on three benchmarks spanning different geometric regimes: (1) S3DIS (Armeni et al., 2016) Area 5: Dense indoor scenes with approximately 100K points ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Dense-scene datasets (S3DIS and ScanNetV2) use Identity Mode, whereas the sparse-object dataset ScanObjectNN uses Morton Mode.
- **p. 6 / 4.2. Main Results - extractive PDF cue:** In contrast to the dense-scene benchmarks, this sparse-object setting benefits from retaining a lightweight spatial prior through Morton serialization when local geometric context is limited.
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Cross-regime validation of dataset-level mode selection.
- **p. 8 / 4.3. Analysis and Ablation - extractive PDF cue:** Dataset ˆσk Best mode S3DIS 0.0060 Identity ScanNetV2 0.0042 Identity ScanObjectNN 0.0251 Morton
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** (2) ScanNetV2 (Dai et al., 2017): Large-scale indoor dataset with 1,513 annotated 3D scans.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Architectural comparison of our method with serialization-based methods. Existing SSM/mamba methods force 3D point clouds into 1D sequences (top), introducing artificial or- dering ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our AnIsoNet framework. (a) LAGM (Local Anisotropy Geometric Modeling) shows a representative hierarchical architecture; the number of stages is dataset-specific. Each ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Semantic segmentation results on S3DIS Area 5. AnIsoNet achieves strong performance among linear-complexity methods.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Semantic segmentation results on ScanNetV2. Methods marked with † use external pre-training data. ∗Best among meth- ods without pre-training. Underline denotes second-best without ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative comparison on ScanObjectNN (PB T50 RS). AnIsoNet outperforms recent MLP and SSM baselines.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Decoupling analysis on S3DIS. ∆is measured relative to the Sphere+MLP baseline. LAGM GISA mIoU (%) ∆ Sphere MLP
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Feature-response visualization on S3DIS for the same query point. (a) Input. (b) Identity Mode produces more con- centrated feature-similarity responses on semantically consistent ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Cross-regime validation of dataset-level mode selection. Dense scenes prefer Identity Mode, while sparse objects benefit from spatial serialization.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 ... | embodiment, simulator version and control stack | p. 7 (4.3. Analysis and Ablation), p. 8 (4.3. Analysis and Ablation) |
| Task/environment | In the current setting, the separation is clear: the two indoor scene datasets have substantially smaller normalized distances than ScanObjectNN, and their best-performing modes ... | reset, timeout, object/scene variation | p. 8 (4.3. Analysis and Ablation), p. 5 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.1. Overview), p. 5 (3.1. Overview) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance. | definition/direction/unit from same section | p. 8 (4.4. Efficiency Analysis) |
| Its latency is not the lowest in the table-PointMamba is faster per forward pass-but AnIsoNet offers a stronger accuracy-resource trade-off, combining clearly better accuracy ... | definition/direction/unit from same section | p. 8 (4.4. Efficiency Analysis) |
| AnIsoNet achieves 94.21% overall accuracy, the best result among the compared linear architectures without external pre-training. | definition/direction/unit from same section | p. 6 (4.2. Main Results) |
| Because our claim concerns robustness rather than strict permutation invariance, we directly test the task-relevant notion of robustness by perturbing the inference-time input order ... | definition/direction/unit from same section | p. 7 (4.3. Analysis and Ablation) |
| Table 13. ScanObjectNN per-class accuracy. Comparison between Morton Mode (Ours) and Identity Mode. Morton serialization provides spatial priors that benefit most categories. | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Table 11. S3DIS Area 5 per-class mIoU. Comparison of different configurations. Identity Mode with ellipsoidal encoding achieves the best results. Note: Beam class has ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| AnIsoNet achieves strong performance among linear-complexity methods. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| (b) Identity Mode produces more concentrated feature-similarity responses on semantically consistent regions. | definition/direction/unit from same section | p. 7 (4.3. Analysis and Ablation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Relative to linear-complexity baselines, it outperforms PCM (Zhang et al., 2025) by 3.0% and Sonata (lin.) by 10.3%. | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| AnIsoNet outperforms recent MLP and SSM baselines. | comparison identity and matched condition | p. 7 (4.3. Analysis and Ablation) |
| Compared with PTv3, it is 1.0% higher on the validation split without external pre-training. | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| Its latency is not the lowest in the table-PointMamba is faster per forward pass-but AnIsoNet offers a stronger accuracy-resource trade-off, combining clearly better accuracy ... | comparison identity and matched condition | p. 8 (4.4. Efficiency Analysis) |
| Decoupling analysis on S3DIS. ∆is measured relative to the Sphere+MLP baseline. | comparison identity and matched condition | p. 7 (4.3. Analysis and Ablation) |
| AnIsoNet (red triangle) attains 82.62% mIoU with 12.2M parameters, outperforming larger models like PTv3 (46.2M, 73.4%) and PCM (38.5M, 79.6%). | comparison identity and matched condition | p. 8 (4.4. Efficiency Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2. Overview of our AnIsoNet framework. (a) LAGM (Local Anisotropy Geometric Modeling) shows a representative hierarchical architecture; the number of stages is dataset-specific. ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Underline denotes second-best without pre-training. | component/input/data sensitivity | p. 6 (4.2. Main Results) |
| Compared with PTv3, it is 1.0% higher on the validation split without external pre-training. | component/input/data sensitivity | p. 6 (4.2. Main Results) |
| Replacing the spherical local encoding with the ellipsoidal variant improves the baseline from 73.48% to 74.44% (+0.96%), while adding GISA alone yields a larger ... | component/input/data sensitivity | p. 7 (4.3. Analysis and Ablation) |
| Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 ... | component/input/data sensitivity | p. 7 (4.3. Analysis and Ablation) |
| Its latency is not the lowest in the table-PointMamba is faster per forward pass-but AnIsoNet offers a stronger accuracy-resource trade-off, combining clearly better accuracy ... | component/input/data sensitivity | p. 8 (4.4. Efficiency Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation. | Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), p. 7 (4.3. Analysis and Ablation), p. 8 (4.4. Efficiency Analysis) |
| Primary metric/result | AnIsoNet achieves strong performance among linear-complexity methods. | numeric claim only at cited anchor | p. 6 (4.1. Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Method Venue Type mIoU (%) PointNet++ (Qi et al., 2017b) NeurIPS'17 MLP 53.5 Point Trans.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** All experiments are conducted on a single NVIDIA RTX 3090 GPU.
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** On dense S3DIS, Identity Mode outperforms both Morton and Hilbert by about 8 points, showing that additional geometry-driven serialization is harmful when local neighborhoods are ...
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** On sparse ScanObjectNN, Morton Mode improves over Identity by 1.70 points, indicating that an explicit spatial prior becomes beneficial when local geometry alone is insufficient.
- **p. 8 / 4.3. Analysis and Ablation - extractive PDF cue:** Input order mIoU Original 78.47 Reverse 78.43 Lexicographic 78.69 Morton 78.39 Hilbert 78.65 Random × 5 78.49 ± 0.12 Chunk shuffle × 5 78.46 ± ...
- **p. 8 / 4.4. Efficiency Analysis - extractive PDF cue:** 0 20 40 60 80 100 120 Parameters (M) 68 70 72 74 76 78 80 82 S3DIS Area 5 mIoU (%) PointNeXt-S NeurIPS 2022 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A mismatched mode therefore causes noticeable degradation rather than collapse. | p. 7 (4.3. Analysis and Ablation) |
| body limitation/failure cue | Because our claim concerns robustness rather than strict permutation invariance, we directly test the task-relevant notion of robustness by perturbing the inference-time input order ... | p. 7 (4.3. Analysis and Ablation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Its latency is not the lowest in the table-PointMamba is faster per forward pass-but AnIsoNet offers a stronger accuracy-resource trade-off, combining clearly better accuracy ... | p. 8 (4.4. Efficiency Analysis) |
| All experiments are conducted on a single NVIDIA RTX 3090 GPU. | p. 6 (4.1. Experimental Setup) |
| Our encoder follows DeLA (Chen et al., 2023) with ellipsoidal spectral encoding. | p. 6 (4.1. Experimental Setup) |
| Method Type mIoU Params FLOPs Latency GPU (%) (M) (G) (ms) PTv3 Trans. | p. 8 (4.4. Efficiency Analysis) |
| LAGM (Local Anisotropy Geometric Modeling): Encodes local micro-structure using direction-sensitive spectral encoding, independent of any global ordering. | p. 3 (3.1. Overview) |
| GISA (Global Isotropy Semantic Aggregation): Aggregates global context through a unified decoder that supports two dataset-level modes: Identity Mode, which uses the default preprocessing/loading ... | p. 3 (3.1. Overview) |
| In our current implementation, the GISA mode is configured at the dataset level rather than predicted per sample. | p. 4 (3.1. Overview) |
| Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a). | p. 4 (3.1. Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** A mismatched mode therefore causes noticeable degradation rather than collapse.
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Because our claim concerns robustness rather than strict permutation invariance, we directly test the task-relevant notion of robustness by perturbing the inference-time input order on ...

- **PDF anchors reviewed:** datasets p. 7 (4.3. Analysis and Ablation), p. 8 (4.3. Analysis and Ablation), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), metrics p. 8 (4.4. Efficiency Analysis), p. 8 (4.4. Efficiency Analysis), p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), p. 13 (Figure/Table caption), p. 13 (Figure/Table caption), baselines p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), p. 6 (4.2. Main Results), p. 8 (4.4. Efficiency Analysis), p. 7 (4.3. Analysis and Ablation), p. 8 (4.4. Efficiency Analysis), results p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation), p. 7 (4.3. Analysis and Ablation), p. 8 (4.4. Efficiency Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
