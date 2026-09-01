# Evaluation - DepthSSC: Monocular 3D Semantic Scene Completion via Depth-Spatial Alignment and Voxel Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Robustness experiment), p. 3 (Figure/Table caption), p. 8 (4.4. Robustness experiment), p. 7 (Figure/Table caption)): The addition of the dynamic resolution in GAV also contributes significantly to the final performance. ing intensities into the depth input, defined as N(0, σ2), where σ represents different noise ...

## Evaluation Body Digest

- **p. 2 / 44.89 IoU on the SemanticKITTI benchmark (hidden - extractive PDF cue:** test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to ...
- **p. 8 / 4.4. Robustness experiment - extractive PDF cue:** Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the corresponding baselines are ...
- **p. 8 / 4.4. Robustness experiment - extractive PDF cue:** Methods VoxFormer-S MonoScene DepthSSC Range (m) 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m IoU (%) 55.45 46.36 38.76 54.65 44.70 37.87 59.37 49.47 ...
- **p. 7 / 4.4. Robustness experiment - extractive PDF cue:** To evaluate the robustness of the ST-GF module under depth input errors, we simulate errors in depth measurements by artificially introducing Gaussian noise with vary2160
- **p. 8 / 4.4. Robustness experiment - extractive PDF cue:** We present the results for various distance intervals (12.8 meters, 25.6 meters, and 51.2 meters) and furnish metrics for both geometric evaluation (IoU) and semantic ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels in ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Pipeline of the DepthSSC. The process begins with a backbone extracting 2D features from input images, followed by the projection of these 2D ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Workflow of the Spatially-Transformed Graph Fusion (ST-GF) Module. The ST-GF module corrects spatial misalignments by predicting a 3D affine transformation matrix Θijk. Voxels ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 44.89 IoU on the SemanticKITTI benchmark (hidden (p. 2); 4.4. Robustness experiment (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Robustness experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The addition of the dynamic resolution in GAV also contributes significantly to the final performance. ing intensities into the depth input, defined as N(0, ... | p. 8 (4.4. Robustness experiment) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Pipeline of the DepthSSC. The process begins with a backbone extracting 2D features from input images, followed by the projection of these ... | p. 3 (Figure/Table caption) |
| 4.4. Robustness experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The best performance is highlighted in bold. | p. 8 (4.4. Robustness experiment) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (val set). The best results compared to the ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / 44.89 IoU on the SemanticKITTI benchmark (hidden - extractive PDF cue:** test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels to ...
- **p. 8 / 4.4. Robustness experiment - extractive PDF cue:** Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the corresponding baselines are ...
- **p. 8 / 4.4. Robustness experiment - extractive PDF cue:** Methods VoxFormer-S MonoScene DepthSSC Range (m) 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m IoU (%) 55.45 46.36 38.76 54.65 44.70 37.87 59.37 49.47 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels in ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Pipeline of the DepthSSC. The process begins with a backbone extracting 2D features from input images, followed by the projection of these 2D ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Workflow of the Spatially-Transformed Graph Fusion (ST-GF) Module. The ST-GF module corrects spatial misalignments by predicting a 3D affine transformation matrix Θijk. Voxels ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (val set). The best results compared to the corresponding ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the corresponding ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative comparison on SSCBench-KITTI- 360 [14]. We present the results for various distance intervals (12.8 meters, 25.6 meters, and 51.2 meters) and furnish ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation and alternative methods evaluation. The ta- ble compares the performance of ablation studies and alternative methods on SemanticKITTI [1]. ST-GF shows stronger ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Robustness evaluation under noisy depth inputs. This table shows the performance degradation in mIoU under increas- ing depth noise levels. Our ST-GF module ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels ... | embodiment, simulator version and control stack | p. 2 (44.89 IoU on the SemanticKITTI benchmark (hidden), p. 8 (4.4. Robustness experiment) |
| Task/environment | Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the corresponding baselines ... | reset, timeout, object/scene variation | p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Methods VoxFormer-S MonoScene DepthSSC Range (m) 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m 12.8m 25.6m 51.2m IoU (%) 55.45 46.36 38.76 54.65 44.70 37.87 59.37 ... | definition/direction/unit from same section | p. 8 (4.4. Robustness experiment) |
| To evaluate the robustness of the ST-GF module under depth input errors, we simulate errors in depth measurements by artificially introducing Gaussian noise with ... | definition/direction/unit from same section | p. 7 (4.4. Robustness experiment) |
| We present the results for various distance intervals (12.8 meters, 25.6 meters, and 51.2 meters) and furnish metrics for both geometric evaluation (IoU) and ... | definition/direction/unit from same section | p. 8 (4.4. Robustness experiment) |
| Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Pipeline of the DepthSSC. The process begins with a backbone extracting 2D features from input images, followed by the projection of these ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Workflow of the Spatially-Transformed Graph Fusion (ST-GF) Module. The ST-GF module corrects spatial misalignments by predicting a 3D affine transformation matrix Θijk. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Quantitative comparison against RGB-inferred baselines and the state-of-the-art monocular SSC method on SemanticKITTI [1] (hidden test set).The best results compared to the corresponding baselines ... | comparison identity and matched condition | p. 8 (4.4. Robustness experiment) |
| Experiment Type Params (M) FLOPs (G) SemanticKITTI Methods (Ablation/Alternative) IoU ↑ mIoU ↑ Ours Full Model 85.46 628.34 45.97 14.59 w/o Dynamic Resolution Ablation ... | comparison identity and matched condition | p. 8 (4.4. Robustness experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation and alternative methods evaluation. | component/input/data sensitivity | p. 8 (4.4. Robustness experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| test set), surpassing the latest approaches. • We introduce the Spatially-Transformed Graph Fusion module, which facilitates the spatial transformation and feature fusion from voxels ... | The addition of the dynamic resolution in GAV also contributes significantly to the final performance. ing intensities into the depth input, defined as N(0, ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Robustness experiment), p. 3 (Figure/Table caption), p. 8 (4.4. Robustness experiment), p. 7 (Figure/Table caption) |
| Primary metric/result | Figure 2. Pipeline of the DepthSSC. The process begins with a backbone extracting 2D features from input images, followed by the projection of these ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 4.4. Robustness experiment - extractive PDF cue:** We present the results for various distance intervals (12.8 meters, 25.6 meters, and 51.2 meters) and furnish metrics for both geometric evaluation (IoU) and semantic ...
- **p. 4 / 3.2. Spatially-Transformed Graph Fusion - extractive PDF cue:** Let πm ijk represent the probability of voxel q′ ijk belonging to cluster m: πm ijk = exp(-αd(q′ ijk, µm)) PM n=1 exp(-αd(q′ ijk, µn)) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | By integrating the Spatially-Transformed Graph Fusion (ST-GF) module and Geometrically-aware Voxelization, DepthSSC dynamically adjusts voxel resolutions based on the geometric complexity of 3D space, ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Table 5. Robustness evaluation under noisy depth inputs. This table shows the performance degradation in mIoU under increas- ing depth noise levels. Our ST-GF ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | To evaluate the robustness of the ST-GF module under depth input errors, we simulate errors in depth measurements by artificially introducing Gaussian noise with ... | p. 7 (4.4. Robustness experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Given the transformed voxels q′ ijk, we perform the following steps. | p. 4 (3.2. Spatially-Transformed Graph Fusion) |
| For each voxel q′ ijk, compute the Euclidean distance to its neighboring voxels: d(q′ ijk, q′ i′j′k′) = q (xi -xi′)2 + (yj -yj′)2 ... | p. 4 (3.2. Spatially-Transformed Graph Fusion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** By integrating the Spatially-Transformed Graph Fusion (ST-GF) module and Geometrically-aware Voxelization, DepthSSC dynamically adjusts voxel resolutions based on the geometric complexity of 3D space, addressing ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Robustness evaluation under noisy depth inputs. This table shows the performance degradation in mIoU under increas- ing depth noise levels. Our ST-GF module ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Goal of Our Approach. Demonstrates DepthSSC's su- periority in handling complex 3D environments for semantic scene completion. Contrasted with VoxFormer, DepthSSC excels in ...
- **p. 7 / 4.4. Robustness experiment - extractive PDF cue:** To evaluate the robustness of the ST-GF module under depth input errors, we simulate errors in depth measurements by artificially introducing Gaussian noise with vary2160

- **PDF anchors reviewed:** datasets p. 2 (44.89 IoU on the SemanticKITTI benchmark (hidden), p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment), metrics p. 8 (4.4. Robustness experiment), p. 7 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 8 (4.4. Robustness experiment), p. 8 (4.4. Robustness experiment), results p. 8 (4.4. Robustness experiment), p. 3 (Figure/Table caption), p. 8 (4.4. Robustness experiment), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
