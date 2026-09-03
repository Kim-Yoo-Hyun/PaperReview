# Evaluation - GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.3. Rendering Evaluation), p. 1 (Figure/Table caption), p. 7 (4.4. Runtime Analysis)): Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on average at 8.34 FPS.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison.
- **p. 6 / 4.3. Rendering Evaluation - extractive body cue:** This excellent rendering performance is attributed to the efficient 3D Gaussian rendering pipeline and can be further applied to real-time downstream tasks, such as VR ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The selected three subsets of TUM-RGBD datasets are used for localization.
- **p. 6 / 4.2. Evaluation of Localization and Mapping - extractive body cue:** 2 compares GS-SLAM with the other SLAM systems in TUM-RGBD dataset.
- **p. 7 / 4.3. Rendering Evaluation - extractive body cue:** The render visualization results on the Replica dataset of the proposed GS-SLAM and SOTA methods.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** We perform the ablation of GS-SLAM on the Replica dataset #Room0 subset to evaluate the effectiveness of coarse-to-fine tracking, and expansion mapping strategy.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** For localization, we use the absolute trajectory (ATE, cm) error [33] to measure the accuracy of the estimated camera poses.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** For mesh reconstruction, we use the 2D Depth L1 (cm) [55], the Precision (P, %), Recall (R, %), and F-score with a threshold of 1 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Evaluation of Localization and Mapping (p. 6); 4.3. Rendering Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Evaluation of Localization and Mapping | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on ... | p. 6 (4.2. Evaluation of Localization and Mapping) |
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results illustrate that the expansion strategy can significantly improve the tracking and mapping perTable 4. | p. 7 (4.5. Ablation Study) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 6. Rendering performance on Replica dataset. We outperform existing dense neural RGB-D methods on the commonly reported rendering metrics. Note that GS-SLAM achieves ... | p. 8 (Figure/Table caption) |
| 4.3. Rendering Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that GS-SLAM achieves the best performance Table 3. | p. 6 (4.3. Rendering Evaluation) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. The illustration of the proposed GS-SLAM. It first uti- lizes the 3D Gaussian representation and differentiable splatting rasterization pipeline in SLAM, achieving ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison.
- **p. 6 / 4.3. Rendering Evaluation - extractive body cue:** This excellent rendering performance is attributed to the efficient 3D Gaussian rendering pipeline and can be further applied to real-time downstream tasks, such as VR ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The selected three subsets of TUM-RGBD datasets are used for localization.
- **p. 6 / 4.2. Evaluation of Localization and Mapping - extractive body cue:** 2 compares GS-SLAM with the other SLAM systems in TUM-RGBD dataset.
- **p. 7 / 4.3. Rendering Evaluation - extractive body cue:** The render visualization results on the Replica dataset of the proposed GS-SLAM and SOTA methods.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** We perform the ablation of GS-SLAM on the Replica dataset #Room0 subset to evaluate the effectiveness of coarse-to-fine tracking, and expansion mapping strategy.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The illustration of the proposed GS-SLAM. It first uti- lizes the 3D Gaussian representation and differentiable splatting rasterization pipeline in SLAM, achieving real-time ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and use the rendered RGB-D image for inverse ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of the proposed adaptive 3D Gaussian ex- pansion strategy. GS-SLAM inhibits the low-quality 3D Gaussian floaters in the current frustum according to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Tracking comparison (ATE RMSE [cm]) of the proposed method vs. the SOTA methods on the Replica dataset. The running speed of methods in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Tracking ATE [cm] on TUM-RGBD [33]. Our method achieves a comparable performance among the neural vSLAMs. ⇤ denotes the reproduced results by running ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Reconstruction comparison of the proposed method vs. the SOTA methods on Replica dataset.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Reconstruction performance comparation of the pro- posed GS-SLAM and SOTA methods on the Replica dataset. 19600
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. The render visualization results on the Replica dataset of the proposed GS-SLAM and SOTA methods. GS-SLAM can generate much more high-quality and realistic ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 6 (4.3. Rendering Evaluation) |
| Task/environment | This excellent rendering performance is attributed to the efficient 3D Gaussian rendering pipeline and can be further applied to real-time downstream tasks, such as ... | reset, timeout, object/scene variation | p. 6 (4.3. Rendering Evaluation), p. 5 (4.1. Experimental Setup) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For localization, we use the absolute trajectory (ATE, cm) error [33] to measure the accuracy of the estimated camera poses. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| For mesh reconstruction, we use the 2D Depth L1 (cm) [55], the Precision (P, %), Recall (R, %), and F-score with a threshold of ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| For Recall and F1 scores, GS-SLAM performs comparably to the second best method CoSLAM [41]. | definition/direction/unit from same section | p. 6 (4.2. Evaluation of Localization and Mapping) |
| Figure 7. Bi-criteria figure of tracking/render performance and system FPS on Replica #Office0. ping and accurate camera pose estimation, striking a bet- ter speed-accuracy ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 8. Ablation of the coarse-to-fine tracking strategy on Replica #Room0. Setting #Room0 ATE# Depth L1# Precision" Recall " F1" PSNR" SSIM" LPIPS# Coarse | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| It is noticeable that the second best method, Point-SLAM [27] runs at 0.42 FPS, which is 20⇥slower than our method, indicating that GS-SLAM achieves ... | definition/direction/unit from same section | p. 6 (4.2. Evaluation of Localization and Mapping) |
| Effect of our expansion strategy for mapping. | definition/direction/unit from same section | p. 7 (4.5. Ablation Study) |
| Note that Point-SLAM uses extra memory dynamic radius to improve performance (mark as †). | definition/direction/unit from same section | p. 7 (4.4. Runtime Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3 report the mapping evaluation results of our method with other current state-of-the-art visual SLAM methods. | comparison identity and matched condition | p. 6 (4.2. Evaluation of Localization and Mapping) |
| Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on ... | comparison identity and matched condition | p. 6 (4.2. Evaluation of Localization and Mapping) |
| Despite this, we still achieve a 20 ⇥faster FPS compared to the similar point-based method Point-SLAM [27]. | comparison identity and matched condition | p. 7 (4.4. Runtime Analysis) |
| 5 illustrate the runtime and memory usage of GS-SLAM and the state-of-the-art methods on the Replica and TUM-RGBD, respectively. | comparison identity and matched condition | p. 7 (4.4. Runtime Analysis) |
| Table 6. Rendering performance on Replica dataset. We outperform existing dense neural RGB-D methods on the commonly reported rendering metrics. Note that GS-SLAM achieves ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison. | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We perform the ablation of GS-SLAM on the Replica dataset #Room0 subset to evaluate the effectiveness of coarse-to-fine tracking, and expansion mapping strategy. | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| 7 shows the ablation of our proposed expansion strategy for mapping. | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| Table 8. Ablation of the coarse-to-fine tracking strategy on Replica #Room0. Setting #Room0 ATE# Depth L1# Precision" Recall " F1" PSNR" SSIM" LPIPS# Coarse | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. Rendering and mesh visualization of the adaptive 3D Gaussian expansion ablation on Replica #Room0. (a) Tracking performance (b) Render performance | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting ... | Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.3. Rendering Evaluation), p. 1 (Figure/Table caption), p. 7 (4.4. Runtime Analysis) |
| Primary metric/result | The results illustrate that the expansion strategy can significantly improve the tracking and mapping perTable 4. | numeric claim only at cited anchor | p. 7 (4.5. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** GS-SLAM is implemented in Python using the PyTorch framework, incorporating CUDA code for Gaussian splatting and trained on a desktop PC with a 5.50GHz Intel ...
- **p. 6 / 4.2. Evaluation of Localization and Mapping - extractive body cue:** Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on average ...
- **p. 6 / 4.2. Evaluation of Localization and Mapping - extractive body cue:** It is noticeable that the second best method, Point-SLAM [27] runs at 0.42 FPS, which is 20⇥slower than our method, indicating that GS-SLAM achieves a ...
- **p. 6 / 4.2. Evaluation of Localization and Mapping - extractive body cue:** The running speed of methods in the upper part is lower than 5 FPS, ⇤denotes the reproduced results by running officially released code.
- **p. 6 / 6.1 Method - extractive body cue:** NICE-SLAM [55] 4.3 31.7 3.9 13.3 Vox-Fusion⇤[48] 3.5 1.5 26.0 10.3 CoSLAM [41] 2.7 1.9 2.6 2.4 ESLAM [11] 2.3 1.1 2.4 2.0 Point-SLAM 2.6 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work. | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and use the rendered RGB-D image for ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | We further evaluate the rendering performance using the peak signal-to-noise ratio (PSNR), SSIM [43], and LPIPS [52] by following [27]. | p. 5 (4.1. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| GS-SLAM is implemented in Python using the PyTorch framework, incorporating CUDA code for Gaussian splatting and trained on a desktop PC with a 5.50GHz ... | p. 5 (4.1. Experimental Setup) |
| To be fair, we run all the methods on a dataset 10 times and report the average results. | p. 5 (4.1. Experimental Setup) |
| The running speed of methods in the upper part is lower than 5 FPS, ⇤denotes the reproduced results by running officially released code. | p. 6 (4.2. Evaluation of Localization and Mapping) |
| Our method achieves a comparable performance among the neural vSLAMs. ⇤ denotes the reproduced results by running officially released code. | p. 6 (4.2. Evaluation of Localization and Mapping) |
| Runtime and memory usage on Replica #Room0. | p. 7 (4.5. Ablation Study) |
| Note that we do not use any neural network decoder in our system, which results in the zero learnable parameter. | p. 7 (4.4. Runtime Analysis) |
| After projecting 3D Gaussians to the image plane, the color of one pixel is rendered by sorting the Gaussians in depth order and performing ... | p. 3 (3.1. 3D Gaussian Scene Representation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and use the rendered RGB-D image for inverse ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We further evaluate the rendering performance using the peak signal-to-noise ratio (PSNR), SSIM [43], and LPIPS [52] by following [27].

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 6 (4.3. Rendering Evaluation), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.3. Rendering Evaluation), p. 7 (4.5. Ablation Study), metrics p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Evaluation of Localization and Mapping), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation of Localization and Mapping), baselines p. 6 (4.2. Evaluation of Localization and Mapping), p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.4. Runtime Analysis), p. 7 (4.4. Runtime Analysis), p. 8 (Figure/Table caption), p. 5 (4.1. Experimental Setup), results p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.3. Rendering Evaluation), p. 1 (Figure/Table caption), p. 7 (4.4. Runtime Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
