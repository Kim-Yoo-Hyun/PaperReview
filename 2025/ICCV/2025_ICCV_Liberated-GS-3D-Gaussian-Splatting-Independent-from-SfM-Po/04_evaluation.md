# Evaluation - Liberated-GS: 3D Gaussian Splatting Independent from SfM Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Comparison), p. 7 (4.2. Comparison), p. 6 (4.2. Comparison), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 4 (Figure/Table caption)): Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To validate the effectiveness of our method, extensive qualitative and quantitative comparison experiments are conducted on three real-world datasets, including two benchmark datasets (Mip-NeRF360 [5] ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The number of pre-training steps is set to 5000 for indoor datasets and 10000 for outdoor datasets to achieve a roughly accurate scene structure.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Comparison of runtime between our pipeline and COLMAP on Scene03 (300 images, 1237×658 resolution) from OMMO [25] dataset.
- **p. 7 / 4.2. Comparison - extractive body cue:** Qualitative Comparisons of different methods on Mip-NeRF360 [5], Tanks and Temples [22] and OMMO [25] Datasets.
- **p. 8 / 4.2. Comparison - extractive body cue:** Ablation for proposed components in our framework on Mip-NeRF360 [5] dataset.
- **p. 6 / 4.2. Comparison - extractive body cue:** Similarly, RAIN-GS [18], despite its new initialization strategy, struggles to address detail loss from insufficient initial points and produces lower geometric quality compared to SfM-initialized ...
- **p. 8 / 4.2. Comparison - extractive body cue:** 6, our method recovers more details in scenes where depth estimation confidence is high (e.g., indoor scenes) and effectively mitigates artifacts and reconstruction errors caused ...
- **p. 6 / 4.2. Comparison - extractive body cue:** 3DGS with random initialization suffers from more artifacts and geometric inaccuracies due to significant errors in the random initial points.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds. | p. 6 (4.2. Comparison) |
| 4.2. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method significantly outperforms other methods, producing visually reliable results with sharper details. | p. 7 (4.2. Comparison) |
| 4.2. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | This quantitatively validates that our approach achieves superior rendering and geometry results even without additional high-quality point clouds. | p. 6 (4.2. Comparison) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that separate affine transformation provides a depth prior that is more consistent with the scene scale, while the ensembled depth yields ... | p. 8 (4.3. Ablation Study) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in the second row, depth alignment enhances scene geometry and visual details by leveraging a more accurate depth prior, resulting in a ... | p. 8 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To validate the effectiveness of our method, extensive qualitative and quantitative comparison experiments are conducted on three real-world datasets, including two benchmark datasets (Mip-NeRF360 [5] ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The number of pre-training steps is set to 5000 for indoor datasets and 10000 for outdoor datasets to achieve a roughly accurate scene structure.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Comparison of runtime between our pipeline and COLMAP on Scene03 (300 images, 1237×658 resolution) from OMMO [25] dataset.
- **p. 7 / 4.2. Comparison - extractive body cue:** Qualitative Comparisons of different methods on Mip-NeRF360 [5], Tanks and Temples [22] and OMMO [25] Datasets.
- **p. 8 / 4.2. Comparison - extractive body cue:** Ablation for proposed components in our framework on Mip-NeRF360 [5] dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Novel View Synthesis Comparison. We propose a novel Gaussian Splatting initialization pipeline to address the degradation in novel view rendering quality caused by ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our method. First, we propose an effective depth alignment method to establish high-quality geometry priors, as described in Sec. 3.2. We ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Point Cloud from different depths. We compare the point cloud from different depths for single view and multiple views. (a) Rendered Depth from ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Unbiased Depth Rendering. Illustration of depth ren- dering with the alpha-blending method and our unbiased method. This implies that the resulting coarse Gaussian ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5. Visual comparison of depth maps and reprojected points with the standard alpha-blending method and our unbiased alpha- blending method. tion Gi, this problem ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quatitative Comparison on Mip-NeRF360 [5], Tanks and Temples [22] Datasets and OMMO [25] Datasets. Colmap- Free 3DGS* indicates the model trained with ground-truth ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative Comparisons of different methods on Mip-NeRF360 [5], Tanks and Temples [22] and OMMO [25] Datasets. We conduct comparisons with original SfM-initialized 3DGS, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Applying our initialization method to different 3D Gaussian Splatting Models on OMMO [25] dataset. Init Methods Mini-Splatting [11] 3DGS-MCMC [21] 3DGS [20] PSNR↑ ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To validate the effectiveness of our method, extensive qualitative and quantitative comparison experiments are conducted on three real-world datasets, including two benchmark datasets (Mip-NeRF360 ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | The number of pre-training steps is set to 5000 for indoor datasets and 10000 for outdoor datasets to achieve a roughly accurate scene structure. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 8 (4.3. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3. Method), p. 5 (3.2. Effective Depth Alignment) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.3. Progressive Segmented Initialization), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Similarly, RAIN-GS [18], despite its new initialization strategy, struggles to address detail loss from insufficient initial points and produces lower geometric quality compared to ... | definition/direction/unit from same section | p. 6 (4.2. Comparison) |
| 6, our method recovers more details in scenes where depth estimation confidence is high (e.g., indoor scenes) and effectively mitigates artifacts and reconstruction errors ... | definition/direction/unit from same section | p. 8 (4.2. Comparison) |
| 3DGS with random initialization suffers from more artifacts and geometric inaccuracies due to significant errors in the random initial points. | definition/direction/unit from same section | p. 6 (4.2. Comparison) |
| Our method demonstrates superior performance compared to existing point-free methods and the original 3DGS across all metrics. | definition/direction/unit from same section | p. 7 (4.2. Comparison) |
| The first , second , and third best performances are highlighted in red, orange, and yellow, respectively. | definition/direction/unit from same section | p. 7 (4.2. Comparison) |
| The edge-aware depth erosion strategy is applied across all experiments. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Figure 4. Unbiased Depth Rendering. Illustration of depth ren- dering with the alpha-blending method and our unbiased method. This implies that the resulting coarse ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3. Point Cloud from different depths. We compare the point cloud from different depths for single view and multiple views. (a) Rendered Depth ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds. | comparison identity and matched condition | p. 6 (4.2. Comparison) |
| Similarly, RAIN-GS [18], despite its new initialization strategy, struggles to address detail loss from insufficient initial points and produces lower geometric quality compared to ... | comparison identity and matched condition | p. 6 (4.2. Comparison) |
| Our method significantly outperforms other methods, producing visually reliable results with sharper details. | comparison identity and matched condition | p. 7 (4.2. Comparison) |
| Our method demonstrates superior performance compared to existing point-free methods and the original 3DGS across all metrics. | comparison identity and matched condition | p. 7 (4.2. Comparison) |
| Ablation for proposed components in our framework on Mip-NeRF360 [5] dataset. | comparison identity and matched condition | p. 8 (4.2. Comparison) |
| Ablation for different depths used for initialization on Mip-NeRF360 [5] dataset. | comparison identity and matched condition | p. 8 (4.2. Comparison) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation for proposed components in our framework on Mip-NeRF360 [5] dataset. | component/input/data sensitivity | p. 8 (4.2. Comparison) |
| This quantitatively validates that our approach achieves superior rendering and geometry results even without additional high-quality point clouds. | component/input/data sensitivity | p. 6 (4.2. Comparison) |
| Ablation for different depths used for initialization on Mip-NeRF360 [5] dataset. | component/input/data sensitivity | p. 8 (4.2. Comparison) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of our method are as follows. • We propose Librated-GS, a novel initialization approach to eliminate the reliance on SfM points of ... | Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Comparison), p. 7 (4.2. Comparison), p. 6 (4.2. Comparison), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 4 (Figure/Table caption) |
| Primary metric/result | Our method significantly outperforms other methods, producing visually reliable results with sharper details. | numeric claim only at cited anchor | p. 7 (4.2. Comparison) |

- Numeric sentences retained from the body:
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Comparison of runtime between our pipeline and COLMAP on Scene03 (300 images, 1237×658 resolution) from OMMO [25] dataset.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Finally, we conduct a runtime analysis on Scene03, which contains 300 images at a resolution of 1237×658, covering the entire pipeline.
- **p. 6 / 3.3. Progressive Segmented Initialization - extractive body cue:** We uniformly sample 10% of the total back-projected 3D points and train a coarse 3DGS model for 1000 steps without performing densification.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, since [14] does not account for scale when utilizing monocular depth to estimate camera poses and generate 3D points, directly using the ground-truth ... | p. 6 (4.2. Comparison) |
| body limitation/failure cue | Depth PSNR↑ SSIM↑ LPIPS↓ Ensembled Depth 27.588 0.822 0.187 Aligned Depth 27.524 0.818 0.189 Estimated Depth 27.390 0.816 0.191 Rendered Depth 26.596 0.708 0.201 ... | p. 8 (4.2. Comparison) |
| body limitation/failure cue | Our initialization does not interfere with subsequent optimization. | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | Figure 1. Novel View Synthesis Comparison. We propose a novel Gaussian Splatting initialization pipeline to address the degradation in novel view rendering quality caused ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Point Cloud from different depths. We compare the point cloud from different depths for single view and multiple views. (a) Rendered Depth ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are conducted on a single RTX4090 GPU. | p. 6 (4.1. Experimental Setup) |
| The number of pre-training steps is set to 5000 for indoor datasets and 10000 for outdoor datasets to achieve a roughly accurate scene structure. | p. 6 (4.1. Experimental Setup) |
| As our method does not modify the refinement stage, its runtime remains comparable to the original pipeline. | p. 8 (4.3. Ablation Study) |
| Comparison of runtime between our pipeline and COLMAP on Scene03 (300 images, 1237×658 resolution) from OMMO [25] dataset. | p. 8 (4.3. Ablation Study) |
| As highlighted in RAINGS [18], the sparse-large-variance (SLV) initialization enables effective signal prediction within few training steps. | p. 3 (3.2. Effective Depth Alignment) |
| Previous works [9, 14, 43] typically utilize alphablending to compute the depth at pixel u as Eq. | p. 4 (3.2. Effective Depth Alignment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Comparison - extractive body cue:** Additionally, since [14] does not account for scale when utilizing monocular depth to estimate camera poses and generate 3D points, directly using the ground-truth poses ...
- **p. 8 / 4.2. Comparison - extractive body cue:** Depth PSNR↑ SSIM↑ LPIPS↓ Ensembled Depth 27.588 0.822 0.187 Aligned Depth 27.524 0.818 0.189 Estimated Depth 27.390 0.816 0.191 Rendered Depth 26.596 0.708 0.201 segmented ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Our initialization does not interfere with subsequent optimization.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Novel View Synthesis Comparison. We propose a novel Gaussian Splatting initialization pipeline to address the degradation in novel view rendering quality caused by ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Point Cloud from different depths. We compare the point cloud from different depths for single view and multiple views. (a) Rendered Depth from ...

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Ablation Study), p. 7 (4.2. Comparison), p. 8 (4.2. Comparison), metrics p. 6 (4.2. Comparison), p. 8 (4.2. Comparison), p. 6 (4.2. Comparison), p. 7 (4.2. Comparison), p. 7 (4.2. Comparison), p. 8 (4.3. Ablation Study), baselines p. 6 (4.2. Comparison), p. 6 (4.2. Comparison), p. 7 (4.2. Comparison), p. 7 (4.2. Comparison), p. 8 (4.2. Comparison), p. 8 (4.2. Comparison), results p. 6 (4.2. Comparison), p. 7 (4.2. Comparison), p. 6 (4.2. Comparison), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
