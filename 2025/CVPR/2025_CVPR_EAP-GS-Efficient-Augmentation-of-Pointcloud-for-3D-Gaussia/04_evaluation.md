# Evaluation - EAP-GS: Efficient Augmentation of Pointcloud for 3D Gaussian Splatting in Few-shot Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Ablation Studies), p. 2 (Figure/Table caption), p. 7 (4.2. Experimental Results), p. 1 (Figure/Table caption), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies)): APA significantly improves the overall number and distribution of initial points, resulting in more accurate and reasonable scene geometry.

## Evaluation Body Digest

- **p. 6 / 4.1. Dataset and Implementation Details - extractive PDF cue:** We evaluated our method on all scenes of the LLFF [21] and Mip-NeRF360 dataset [1].
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** For fair comparison, all methods were trained with the same training data and hardware.
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Quantitative results on LLFF and Mip-NeRF360 datasets.
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Methods LLFF Dataset Mip-NeRF360 Dataset PSNR SSIM LPIPS Time (min) Number PSNR SSIM LPIPS Time (min) Number 3DGS 14.63 0.4374 0.3425 11.98 379k 16.06 0.3997 ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** We evalute the effect of each component of EAP-GS on the LLFF dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** 4, each component of our method improves the reconstruction metrics for the LLFF dataset.
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Best score and second-best score are in red and orange respectively.
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Additionally, the sparse pointcloud might have a large error when scale matching the relative depth.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Dataset and Implementation Details (p. 6); 4.2. Experimental Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | APA significantly improves the overall number and distribution of initial points, resulting in more accurate and reasonable scene geometry. | p. 7 (4.3. Ablation Studies) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Reconstruction results by original 3DGS with six training views. Left column: unsatisfying reconstruciton (c) from inadequate pointcloud (a). Right column: fine reconstruciton ... | p. 2 (Figure/Table caption) |
| 4.2. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves leading scores across all metrics while using fewer Gaussians and requiring less computation time. | p. 7 (4.2. Experimental Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Comparison of the FSGS [41] and our proposed EAP-GS with 12 training views. With Attentional Pointcloud Augmenta- tion technique, our method generates ... | p. 1 (Figure/Table caption) |
| 4.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, each component of our method improves the reconstruction metrics for the LLFF dataset. | p. 8 (4.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Dataset and Implementation Details - extractive PDF cue:** We evaluated our method on all scenes of the LLFF [21] and Mip-NeRF360 dataset [1].
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** For fair comparison, all methods were trained with the same training data and hardware.
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Quantitative results on LLFF and Mip-NeRF360 datasets.
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Methods LLFF Dataset Mip-NeRF360 Dataset PSNR SSIM LPIPS Time (min) Number PSNR SSIM LPIPS Time (min) Number 3DGS 14.63 0.4374 0.3425 11.98 379k 16.06 0.3997 ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** We evalute the effect of each component of EAP-GS on the LLFF dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** 4, each component of our method improves the reconstruction metrics for the LLFF dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Comparison of the FSGS [41] and our proposed EAP-GS with 12 training views. With Attentional Pointcloud Augmenta- tion technique, our method generates significantly ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Reconstruction results by original 3DGS with six training views. Left column: unsatisfying reconstruciton (c) from inadequate pointcloud (a). Right column: fine reconstruciton (d) ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Pipeline of the EAP-GS. We utilize the original 3DGS in the reconstruction stage and it can be easily replaced by other optimization methods. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Relationship between scene complexity and density distribution. (a) zoom-in of a smooth region with its 2D spectrum on the right; (b) zoom-in of ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative Comparison on LLFF and Mip-NeRF360 datasets. We demonstrate testing view reconstruction by 3DGS [14], DRGS [6], FSGS [41], CoR-GS [36] and our ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative results on LLFF and Mip-NeRF360 datasets. Best score and second-best score are in red and orange respec- tively. The results of each ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Advantage of incorporating APA into various meth- ods. Quantitative metric comparison of original version and the version incorporating APA for different methods. LLFF ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Advantage of incorporating APA into various meth- ods. Visualization of testing view reconstructions from different 3DGS-based optimization methods after incorporating APA.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluated our method on all scenes of the LLFF [21] and Mip-NeRF360 dataset [1]. | embodiment, simulator version and control stack | p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.2. Experimental Results) |
| Task/environment | For fair comparison, all methods were trained with the same training data and hardware. | reset, timeout, object/scene variation | p. 6 (4.2. Experimental Results), p. 7 (4.2. Experimental Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.2. Attentional Pointcloud Augmentation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.2. Attentional Pointcloud Augmentation), p. 4 (3.1. Preliminary) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Best score and second-best score are in red and orange respectively. | definition/direction/unit from same section | p. 7 (4.2. Experimental Results) |
| Additionally, the sparse pointcloud might have a large error when scale matching the relative depth. | definition/direction/unit from same section | p. 7 (4.2. Experimental Results) |
| Pointcloud Augmentation increases the number of initial points, providing better initialization and enhancing the stability and accuracy of subsequent optimization. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Attention mechanism allows the augmentation process to focus more on pointcloud generation in regions with complex structure but sparse pointcloud distribution, enriching reconstruction details, ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Figure 2. Reconstruction results by original 3DGS with six training views. Left column: unsatisfying reconstruciton (c) from inadequate pointcloud (a). Right column: fine reconstruciton ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Across all scenes, our method stands out and produces more accurate geometry (e.g., iron pail in the Garden). | definition/direction/unit from same section | p. 6 (4.2. Experimental Results) |
| For baseline methods, we maintained their original training strategies and reported both the time cost and the number of Gaussian kernels generated in reconstruction. | definition/direction/unit from same section | p. 6 (4.1. Dataset and Implementation Details) |
| Figure 1. Comparison of the FSGS [41] and our proposed EAP-GS with 12 training views. With Attentional Pointcloud Augmenta- tion technique, our method generates ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We configured COLMAP [28] with the same parameters as FSGS for the initialization of various baselines. | comparison identity and matched condition | p. 6 (4.1. Dataset and Implementation Details) |
| For baseline methods, we maintained their original training strategies and reported both the time cost and the number of Gaussian kernels generated in reconstruction. | comparison identity and matched condition | p. 6 (4.1. Dataset and Implementation Details) |
| On the other hand, our results confirm that DetectorfreeSfM is more effective at extracting 2D feature points in texture-poor areas (e.g., white marble) compared ... | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| The reconstruction results of various methods with and without APA in Tab. | comparison identity and matched condition | p. 7 (4.2. Experimental Results) |
| Ablation study on proposed components. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| Ablation study on different initialization. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4. Ablation study on proposed components. We evalute the effect of each component of EAP-GS on the LLFF dataset. Pointcloud Attention PSNR SSIM ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 3. Ablation study on different initialization. We compare all metrics on the LLFF dataset initialized by COLMAP [28] and DetectorfreeSfM [11] methods with ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The reconstruction results of various methods with and without APA in Tab. | component/input/data sensitivity | p. 7 (4.2. Experimental Results) |
| We conducted ablation studies to assess the impact of our APA technique and the DetectorfreeSfM [11] method. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Figure 3. Pipeline of the EAP-GS. We utilize the original 3DGS in the reconstruction stage and it can be easily replaced by other optimization ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Therefore, we propose a pointcloud generation method specifically designed for 3DGS initialization, which significantly increases the number of initial points. | APA significantly improves the overall number and distribution of initial points, resulting in more accurate and reasonable scene geometry. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Ablation Studies), p. 2 (Figure/Table caption), p. 7 (4.2. Experimental Results), p. 1 (Figure/Table caption), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |
| Primary metric/result | Figure 2. Reconstruction results by original 3DGS with six training views. Left column: unsatisfying reconstruciton (c) from inadequate pointcloud (a). Right column: fine reconstruciton ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Lacking a method to limit the error may be a limitation Figure 7. | p. 8 (5. Discussion) |
| body limitation/failure cue | This issue is primarily due to data incompleteness, and a potential approach to further enhance performance would be to incorporate prior knowledge or generative ... | p. 8 (5. Discussion) |
| body limitation/failure cue | Similar results are obtained for unknown camera-poses though we did not report here because of space limitation. | p. 7 (4.2. Experimental Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In contrast, DRGS mitigates training time through an early-stop strategy, but this may lead to insufficient training. | p. 7 (4.2. Experimental Results) |
| All experiments were conducted on a single NVIDIA TITAN RTX GPU. | p. 6 (4.1. Dataset and Implementation Details) |
| Further implementation details are provided in the supplementary. | p. 6 (4.1. Dataset and Implementation Details) |
| In comparison, our augmented pointcloud inherently encodes depth information, providing a good guidance for Gaussian generation. | p. 7 (4.2. Experimental Results) |
| For each image rendering, the loss function relative to the ground truth (GT) can be computed directly as: \m a th c al {L}_ ... | p. 4 (3.1. Preliminary) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Discussion - extractive PDF cue:** Lacking a method to limit the error may be a limitation Figure 7.
- **p. 8 / 5. Discussion - extractive PDF cue:** This issue is primarily due to data incompleteness, and a potential approach to further enhance performance would be to incorporate prior knowledge or generative models ...
- **p. 7 / 4.2. Experimental Results - extractive PDF cue:** Similar results are obtained for unknown camera-poses though we did not report here because of space limitation.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), metrics p. 7 (4.2. Experimental Results), p. 7 (4.2. Experimental Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 2 (Figure/Table caption), p. 6 (4.2. Experimental Results), baselines p. 6 (4.1. Dataset and Implementation Details), p. 6 (4.1. Dataset and Implementation Details), p. 7 (4.3. Ablation Studies), p. 7 (4.2. Experimental Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), results p. 7 (4.3. Ablation Studies), p. 2 (Figure/Table caption), p. 7 (4.2. Experimental Results), p. 1 (Figure/Table caption), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
