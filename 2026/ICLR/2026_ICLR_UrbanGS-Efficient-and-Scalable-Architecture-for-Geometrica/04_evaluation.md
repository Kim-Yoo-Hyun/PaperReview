# Evaluation - UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=L3utaw6SD9; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248058. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENTS)): Quantitative results reveal consistent improvements across all evaluation metrics, with notable gains in F1-score (from 0.453 to 0.503) and PSNR (from 24.59 to 26.44), validating the critical importance of this ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We compare our method with existing surface reconstruction approaches on the GauU-Scene datasets (Xiong et al., 2024).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Ground Truth 2DGS VCR-GauS Ours CityGS-X CityGS-v2 College Campus Morden Village Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Methods Residence Russian Building Modern Building P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ NeuS ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Method PSNR↑ SSIM↑ LPIPS↓ F1↑ w/o D-Normal 25.02 0.743 0.215 0.463 w/o Depth Consistency 24.59 0.792 0.201 0.453 w/o Geometry-Aware Confidence 26.02 0.795 0.163 0.493 ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** Since the Mill-19 (Yu et al., 2022), UrbanScene3D (Lin et al., 2022), and GauU-Scene (Xiong et al., 2024) datasets contain thousands of high-resolution images, we ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 5, we conduct ablation studies on each component of the Depth-Consistent D-Normal Regularization, demonstrating that its introduction significantly enhances both rendering quality and geometric accuracy ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 3, when compared with other large-scale scene algorithms, our method requires lower computational costs while achieving better rendering quality and geometric accuracy.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The 7k step is applied after the scene has roughly formed and the Gaussian distribution starts to stabilize, consistent with the behavior observed in 3DGS ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); A IMPLEMENTATION DETAILS (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitative results reveal consistent improvements across all evaluation metrics, with notable gains in F1-score (from 0.453 to 0.503) and PSNR (from 24.59 to 26.44), ... | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, our method achieves state-ofthe-art performance among both neural implicit baselines and recent 3DGS-based city-scale methods. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | UrbanGS consistently achieves state-of-the-art performance, attaining the highest PSNR and SSIM in building scenes and reducing LPIPS by 0.006 over CityGS (Liu et al., ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that our SAGP is more effective at preserving the original geometric quality (higher F1 score) while significantly reducing the number of ... | p. 10 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Experimental results on the Rubble dataset (Yu et al., 2022) demonstrate that the proposed method outperforms comparative approaches in terms of PSNR ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We compare our method with existing surface reconstruction approaches on the GauU-Scene datasets (Xiong et al., 2024).
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Ground Truth 2DGS VCR-GauS Ours CityGS-X CityGS-v2 College Campus Morden Village Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Methods Residence Russian Building Modern Building P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ NeuS ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Method PSNR↑ SSIM↑ LPIPS↓ F1↑ w/o D-Normal 25.02 0.743 0.215 0.463 w/o Depth Consistency 24.59 0.792 0.201 0.453 w/o Geometry-Aware Confidence 26.02 0.795 0.163 0.493 ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** Since the Mill-19 (Yu et al., 2022), UrbanScene3D (Lin et al., 2022), and GauU-Scene (Xiong et al., 2024) datasets contain thousands of high-resolution images, we ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 5, we conduct ablation studies on each component of the Depth-Consistent D-Normal Regularization, demonstrating that its introduction significantly enhances both rendering quality and geometric accuracy ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 3, when compared with other large-scale scene algorithms, our method requires lower computational costs while achieving better rendering quality and geometric accuracy.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The 7k step is applied after the scene has roughly formed and the Gaussian distribution starts to stabilize, consistent with the behavior observed in 3DGS ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose UrbanGS, a scalable framework for high-fidelity large-scale scene reconstruc- tion. Left: It reconstructs complex urban environments from multi-view RGB images, capturing ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: UrbanGS training pipeline and core components. (a) Training Pipeline: Starting from coarse global Gaussians, we apply spatially adaptive Gaussian pruning to obtain compact ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparisons on the Mill19 (Yu et al., 2022) and UrbanScene3D (Lin et al., 2022) datasets for novel view synthesis. ↑indicates higher is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative results of ours and other methods in image rendering on Mill-19 (Yu et al., 2022) and Urbanscene3D (Lin et al., 2022). Ground ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene dataset (Xiong et al., 2024). 4.2 MAIN RESULTS Novel View Synthesis. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Under the GauU-Scene dataset (Lin et al., 2022), comparison of Large-Scale Scene Mod- eling Methods, the best result for specific metrics under each ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Experimental results on the Rubble dataset (Yu et al., 2022) demonstrate that the proposed method outperforms comparative approaches in terms of PSNR while ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We compare our method with existing surface reconstruction approaches on the GauU-Scene datasets (Xiong et al., 2024). | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | Ground Truth 2DGS VCR-GauS Ours CityGS-X CityGS-v2 College Campus Morden Village Figure 4: Qualitative mesh and texture comparison between SOTA and our method on ... | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In particular, compared with CityGS-X, our approach attains higher F1 scores across all scenes by improving recall while maintaining comparable precision. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| The results demonstrate that our SAGP is more effective at preserving the original geometric quality (higher F1 score) while significantly reducing the number of ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Quantitative results reveal consistent improvements across all evaluation metrics, with notable gains in F1-score (from 0.453 to 0.503) and PSNR (from 24.59 to 26.44), ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| 3, when compared with other large-scale scene algorithms, our method requires lower computational costs while achieving better rendering quality and geometric accuracy. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| As shown in Table 2, our method achieves state-ofthe-art performance among both neural implicit baselines and recent 3DGS-based city-scale methods. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Methods Residence Russian Building Modern Building P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ P ↑ R ↑ F1 ↑ ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| To obtain the final mesh, we employ Open3D's volumetric TSDF fusion method, which integrates rendered depth maps and corresponding camera poses to construct a ... | definition/direction/unit from same section | p. 15 (A IMPLEMENTATION DETAILS) |
| Figure 1: We propose UrbanGS, a scalable framework for high-fidelity large-scale scene reconstruc- tion. Left: It reconstructs complex urban environments from multi-view RGB images, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene dataset (Xiong et al., 2024). 4.2 MAIN RESULTS Novel View ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Method Rendering Quality Geometric Quality Training Statistics PSNR↑ SSIM↑ LPIPS↓ P↑ R↑ F1↑ GS (M)↓ Time↓ Size↓ Mem↓ Baseline 22.54 0.778 0.231 0.532 0.501 ... | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| As shown in Table 2, our method achieves state-ofthe-art performance among both neural implicit baselines and recent 3DGS-based city-scale methods. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 3, when compared with other large-scale scene algorithms, our method requires lower computational costs while achieving better rendering quality and geometric accuracy. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| We first establish a Baseline that employs neither our SAGP nor any partitioning strategy. | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| Figure 5: Experimental results on the Rubble dataset (Yu et al., 2022) demonstrate that the proposed method outperforms comparative approaches in terms of PSNR ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Method PSNR↑ SSIM↑ LPIPS↓ F1↑ w/o D-Normal 25.02 0.743 0.215 0.463 w/o Depth Consistency 24.59 0.792 0.201 0.453 w/o Geometry-Aware Confidence 26.02 0.795 0.163 ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Method Rendering Quality Geometric Quality Training Statistics PSNR↑ SSIM↑ LPIPS↓ P↑ R↑ F1↑ GS (M)↓ Time↓ Size↓ Mem↓ Baseline 22.54 0.778 0.231 0.532 0.501 ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| The top three results are highlighted with red, orange, and yellow backgrounds, respectively. † denotes results obtained without the decoupled appearance encoding. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| 3, we present quantitative and qualitative evaluations of large-scale scene reconstruction methods with and without geometric optimization. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| The surface is then extracted using the Marching Cubes algorithm at the zero-level isosurface, enabling direct reconstruction of 3D geometry without relying on intermediate ... | component/input/data sensitivity | p. 15 (A IMPLEMENTATION DETAILS) |
| When constructing the coarse global Gaussian model, we apply an initial, simple pruning rule to remove obviously redundant Gaussians, reduce memory, and obtain a ... | component/input/data sensitivity | p. 15 (A IMPLEMENTATION DETAILS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing ... | Quantitative results reveal consistent improvements across all evaluation metrics, with notable gains in F1-score (from 0.453 to 0.503) and PSNR (from 24.59 to 26.44), ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | As shown in Table 2, our method achieves state-ofthe-art performance among both neural implicit baselines and recent 3DGS-based city-scale methods. | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 5, our method only takes 2 hours and 10 minutes to complete the training on the Rubble (Lin et al., 2022), which is significantly faster ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Qualitative results in Figure F show that rendered views remain visually consistent across different weight combinations, with no catastrophic failures even for suboptimal settings. | p. 25 (C SUPPLEMENTATION TO THE PARTITIONING STRATEGY) |
| body limitation/failure cue | Figure 1: We propose UrbanGS, a scalable framework for high-fidelity large-scale scene reconstruc- tion. Left: It reconstructs complex urban environments from multi-view RGB images, ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | This discrepancy highlights a limitation of current geometry optimization objectives when applied to background regions lacking clear geometric structure. | p. 23 (C SUPPLEMENTATION TO THE PARTITIONING STRATEGY) |
| body limitation/failure cue | E LIMITATIONS Although UrbanGS demonstrates advantages in large-scale reconstruction, it still exhibits certain limitations. | p. 26 (C SUPPLEMENTATION TO THE PARTITIONING STRATEGY) |
| body limitation/failure cue | Additionally, the method primarily focuses on static environments and does not explicitly model dynamic objects commonly found in urban scenes. | p. 26 (C SUPPLEMENTATION TO THE PARTITIONING STRATEGY) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We compare the training time of our method with that of existing methods. | p. 9 (4 EXPERIMENTS) |
| The results demonstrate that our SAGP is more effective at preserving the original geometric quality (higher F1 score) while significantly reducing the number of ... | p. 10 (4 EXPERIMENTS) |
| The derivation of the D-Normal from the rendered depth involves two sequential steps. | p. 5 (3.1 PRELIMINARIES) |
| Subsequently, the horizontal and vertical finite differences are computed between adjacent points in this back-projected point cloud; the D-Normal is then obtained by calculating ... | p. 5 (3.1 PRELIMINARIES) |
| Within each cell, we compute the t-th percentile Gaussian volume ϑ(t) local and normalize individual volumes via a sub-linear transform: wv,i = | p. 6 (3.1 PRELIMINARIES) |
| Specifically, we compute per-view scale and shift parameters by robustly fitting the monocular depth maps to the sparse COLMAP depth values at valid 2D-3D ... | p. 6 (3.1 PRELIMINARIES) |
| The combined score is given by Si = ϕi · τi · wv,i, (15) which eliminates the need for manually tuned weighting hyperparameters-a detailed ... | p. 7 (3.1 PRELIMINARIES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method produced invalid numerical results, while "FAIL" denotes ...
- **p. 25 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** Qualitative results in Figure F show that rendered views remain visually consistent across different weight combinations, with no catastrophic failures even for suboptimal settings.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose UrbanGS, a scalable framework for high-fidelity large-scale scene reconstruc- tion. Left: It reconstructs complex urban environments from multi-view RGB images, capturing ...
- **p. 23 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** This discrepancy highlights a limitation of current geometry optimization objectives when applied to background regions lacking clear geometric structure.
- **p. 26 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** E LIMITATIONS Although UrbanGS demonstrates advantages in large-scale reconstruction, it still exhibits certain limitations.
- **p. 26 / C SUPPLEMENTATION TO THE PARTITIONING STRATEGY - extractive body cue:** Additionally, the method primarily focuses on static environments and does not explicitly model dynamic objects commonly found in urban scenes.

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 15 (A IMPLEMENTATION DETAILS), p. 10 (4 EXPERIMENTS), metrics p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), results p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
