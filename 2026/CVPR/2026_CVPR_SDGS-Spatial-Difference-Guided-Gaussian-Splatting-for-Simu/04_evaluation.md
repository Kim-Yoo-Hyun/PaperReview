# Evaluation - SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.3. Ablation Study), p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.2.3. Performance Analysis), p. 6 (4.1.3. Evaluation Metrics), p. 6 (4.1. Experiment Setup)): 2, across three complex scenarios, while our method exhibits marginally lower overall tracking accuracy compared to the baseline approaches, it achieves a substantial improvement in computational efficiency.

## Evaluation Body Digest

- **p. 6 / 4.1.2. Datasets - extractive PDF cue:** To analyze our method under controllable settings, we construct a SD-Replica dataset by simulating the hybrid pixel camera's sampling process on the Replica [15] scenes.
- **p. 6 / 4.1.3. Evaluation Metrics - extractive PDF cue:** For tracking accuracy, we adopt the Root Mean Square Error (RMSE) of Absolute Trajectory Error (ATE), following standard camera 6-DoF pose estimation benchmarks.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** And a semi-isotropic loss can help tracking accuracy for scenes with sharp edges like fr1/desk and fr2/xyz, however it slightly reduces tracking accuracy in fr3/office ...
- **p. 7 / 4.2.2. Deblurring Metrics - extractive PDF cue:** RMSE ATE[cm] on the TUM-RGBD dataset.
- **p. 7 / 4.2.2. Deblurring Metrics - extractive PDF cue:** Reconstruction results on the stereo-Tianmouc dataset.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We conduct the ablation study of image pyramids and semiisotropic loss on TUM-RGBD dataset.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive PDF cue:** Under fast and extreme motion, our approach demonstrates significant advantages, while other methods based on dense RGB frames suffer from motion blur and rapid error ...
- **p. 7 / 4.2.1. Tracking Accuracy - extractive PDF cue:** We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the stereo ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Experiment Setup (p. 6); 4.1.2. Datasets (p. 6); 4.1.3. Evaluation Metrics (p. 6); 4.2. Experiment Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2.1. Tracking Accuracy | EMPIRICAL / SIMULATION | 2, across three complex scenarios, while our method exhibits marginally lower overall tracking accuracy compared to the baseline approaches, it achieves a substantial improvement ... | p. 7 (4.2.1. Tracking Accuracy) |
| 4.3. Ablation Study | EMPIRICAL / SIMULATION | We can see that a pyramid strategy can significantly improve system's tracking accuracy under long sequences like fr3/office. | p. 8 (4.3. Ablation Study) |
| 4.2.1. Tracking Accuracy | EMPIRICAL / SIMULATION | 1, under low-speed motion, our method achieves tracking accuracy comparable to the baselines. | p. 7 (4.2.1. Tracking Accuracy) |
| 4.2.3. Performance Analysis | EMPIRICAL / SIMULATION | 4, our sparse edge-guided tracking framework achieves the highest frame rate among all compared methods, while maintaining competitive accuracy. | p. 8 (4.2.3. Performance Analysis) |
| 4.1.3. Evaluation Metrics | EMPIRICAL / SIMULATION | We evaluate our method from three perspectives: tracking accuracy, deblurring quality, and computational efficiency. | p. 6 (4.1.3. Evaluation Metrics) |

## Dataset / Benchmark Role

- **p. 6 / 4.1.2. Datasets - extractive PDF cue:** To analyze our method under controllable settings, we construct a SD-Replica dataset by simulating the hybrid pixel camera's sampling process on the Replica [15] scenes.
- **p. 6 / 4.1.3. Evaluation Metrics - extractive PDF cue:** For tracking accuracy, we adopt the Root Mean Square Error (RMSE) of Absolute Trajectory Error (ATE), following standard camera 6-DoF pose estimation benchmarks.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** And a semi-isotropic loss can help tracking accuracy for scenes with sharp edges like fr1/desk and fr2/xyz, however it slightly reduces tracking accuracy in fr3/office ...
- **p. 7 / 4.2.2. Deblurring Metrics - extractive PDF cue:** RMSE ATE[cm] on the TUM-RGBD dataset.
- **p. 7 / 4.2.2. Deblurring Metrics - extractive PDF cue:** Reconstruction results on the stereo-Tianmouc dataset.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We conduct the ablation study of image pyramids and semiisotropic loss on TUM-RGBD dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Differential rasterization and reconstructed sparse map: elongated Gaussians are used as an efficient primitive to represent scene geometry and to perform camera pose ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for efficient ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. (a) Hybrid pixel layout, which offers color and high- frame-rate spatial difference in one sensor. (b) RGB and spatial difference comparison under high ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment. With ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 5. (a) Binary SD image. (b) Euclidean distance transform (in pixels); warmer colors indicate larger distance to the nearest edge, cooler colors indicate smaller ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. Mutually exclusive supervision. Note that it is shown in the rendered image and distorted into sensor domain as in Fig. 3a, each RGB ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Tracking error (RMSE ATE [cm]) on stereo-Tianmouc. ∗Outer pose estimators. † Sim(3) alignment.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. RMSE ATE[cm] on the TUM-RGBD dataset.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To analyze our method under controllable settings, we construct a SD-Replica dataset by simulating the hybrid pixel camera's sampling process on the Replica [15] ... | embodiment, simulator version and control stack | p. 6 (4.1.2. Datasets), p. 6 (4.1.3. Evaluation Metrics) |
| Task/environment | For tracking accuracy, we adopt the Root Mean Square Error (RMSE) of Absolute Trajectory Error (ATE), following standard camera 6-DoF pose estimation benchmarks. | reset, timeout, object/scene variation | p. 6 (4.1.3. Evaluation Metrics), p. 8 (4.3. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 5 (3.2.2. Tracking) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For tracking accuracy, we adopt the Root Mean Square Error (RMSE) of Absolute Trajectory Error (ATE), following standard camera 6-DoF pose estimation benchmarks. | definition/direction/unit from same section | p. 6 (4.1.3. Evaluation Metrics) |
| Under fast and extreme motion, our approach demonstrates significant advantages, while other methods based on dense RGB frames suffer from motion blur and rapid ... | definition/direction/unit from same section | p. 7 (4.2.1. Tracking Accuracy) |
| We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the ... | definition/direction/unit from same section | p. 7 (4.2.1. Tracking Accuracy) |
| We can see that a pyramid strategy can significantly improve system's tracking accuracy under long sequences like fr3/office. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| 4, our sparse edge-guided tracking framework achieves the highest frame rate among all compared methods, while maintaining competitive accuracy. | definition/direction/unit from same section | p. 8 (4.2.3. Performance Analysis) |
| We evaluate our method from three perspectives: tracking accuracy, deblurring quality, and computational efficiency. | definition/direction/unit from same section | p. 6 (4.1.3. Evaluation Metrics) |
| Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 4. SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3, on SD-Replica room0, we consistently outperform the baseline MonoGS-RGBD in terms of PSNR, SSIM, and LPIPS. | comparison identity and matched condition | p. 7 (4.2.2. Deblurring Metrics) |
| 2, across three complex scenarios, while our method exhibits marginally lower overall tracking accuracy compared to the baseline approaches, it achieves a substantial improvement ... | comparison identity and matched condition | p. 7 (4.2.1. Tracking Accuracy) |
| 4, our sparse edge-guided tracking framework achieves the highest frame rate among all compared methods, while maintaining competitive accuracy. | comparison identity and matched condition | p. 8 (4.2.3. Performance Analysis) |
| Ablation on TUM-RGBD (RMSE ATE [cm]). w/o = without; w/ = with; Pyr. = pyramid; Semi-iso = semi-isotropic. | comparison identity and matched condition | p. 8 (4.2.3. Performance Analysis) |
| Figure 3. (a) Hybrid pixel layout, which offers color and high- frame-rate spatial difference in one sensor. (b) RGB and spatial difference comparison under ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation on TUM-RGBD (RMSE ATE [cm]). w/o = without; w/ = with; Pyr. = pyramid; Semi-iso = semi-isotropic. | component/input/data sensitivity | p. 8 (4.2.3. Performance Analysis) |
| We conduct the ablation study of image pyramids and semiisotropic loss on TUM-RGBD dataset. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues ... | 2, across three complex scenarios, while our method exhibits marginally lower overall tracking accuracy compared to the baseline approaches, it achieves a substantial improvement ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.3. Ablation Study), p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.2.3. Performance Analysis), p. 6 (4.1.3. Evaluation Metrics), p. 6 (4.1. Experiment Setup) |
| Primary metric/result | We can see that a pyramid strategy can significantly improve system's tracking accuracy under long sequences like fr3/office. | numeric claim only at cited anchor | p. 8 (4.3. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1.1. System Setup - extractive PDF cue:** The RGB stream is recorded at 30 FPS, while the differential output is synchronously recorded at 757 FPS with a dynamic range over 100 dB.
- **p. 6 / 3.4.2. SD-guided Mutually Exclusive RGB Supervision - extractive PDF cue:** We then apply 2×2 average pooling to form a H 2 × W 2 grid, and construct a chessboard-sampled grid as in Fig.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | By combining emerging hybrid pixel cameras, we not only maintain robust tracking accuracy under extreme motions where other methods fail, but also reconstruct dense ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Our system balances tracking robustness, high-fidelity reconstruction, and system efficiency. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | We evaluate our method on three datasets to verify both the robustness and generalization ability: SD-Replica Datasets. | p. 6 (4.1.2. Datasets) |
| body limitation/failure cue | We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the ... | p. 7 (4.2.1. Tracking Accuracy) |
| body limitation/failure cue | Method Input tianmouc/slow tianmouc/fast tianmouc/extreme Average Gaussian-SLAM RGB 4.60 fail fail - SplaTAM 6.52 fail fail - MonoGS-RGBD 3.32 24.52 fail - WildGS-SLAM∗† 2.01 ... | p. 7 (4.2.2. Deblurring Metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are conducted on an NVIDIA RTX 5880 Ada (48 GB) GPU and an AMD Ryzen Threadripper PRO 5975WX (32 cores) CPU. | p. 6 (4.1.1. System Setup) |
| Specifically, we apply depth-aware motion blur along the camera trajectory to the RGB sequence and generate SD data that mimics the hybrid pixel sensor's ... | p. 6 (4.1.2. Datasets) |
| We further evaluate the runtime efficiency and model sparsity of our system on the TUM RGB-D dataset. | p. 8 (4.2.3. Performance Analysis) |
| It is worth noting that with a Levenberg-Marquardt (LM) style second-order optimizer, our method is able to run at 8.61 total FPS with an ... | p. 8 (4.2.3. Performance Analysis) |
| In this work, we adopt a first-order spatial difference (SD) as our edge descriptor, which can be efficiently computed by the following operator: | p. 3 (3.1.1. Sparse Edge Descriptor) |
| Leveraging hardware SD signals, we use SD as a prior to mitigate defocus and motion blur in RGB sequences. | p. 5 (3.4.2. SD-guided Mutually Exclusive RGB Supervision) |
| Instead, we run a pyramidal Lucas-Kanade (LK) [11] search constrained along the epipolar line, which exploits the high information content of SD edges and ... | p. 5 (3.2.2. Tracking) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** By combining emerging hybrid pixel cameras, we not only maintain robust tracking accuracy under extreme motions where other methods fail, but also reconstruct dense maps ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Our system balances tracking robustness, high-fidelity reconstruction, and system efficiency.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for efficient ...
- **p. 6 / 4.1.2. Datasets - extractive PDF cue:** We evaluate our method on three datasets to verify both the robustness and generalization ability: SD-Replica Datasets.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive PDF cue:** We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the stereo ...
- **p. 7 / 4.2.2. Deblurring Metrics - extractive PDF cue:** Method Input tianmouc/slow tianmouc/fast tianmouc/extreme Average Gaussian-SLAM RGB 4.60 fail fail - SplaTAM 6.52 fail fail - MonoGS-RGBD 3.32 24.52 fail - WildGS-SLAM∗† 2.01 8.21 ...

- **PDF anchors reviewed:** datasets p. 6 (4.1.2. Datasets), p. 6 (4.1.3. Evaluation Metrics), p. 8 (4.3. Ablation Study), p. 7 (4.2.2. Deblurring Metrics), p. 7 (4.2.2. Deblurring Metrics), p. 8 (4.3. Ablation Study), metrics p. 6 (4.1.3. Evaluation Metrics), p. 7 (4.2.1. Tracking Accuracy), p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.3. Ablation Study), p. 8 (4.2.3. Performance Analysis), p. 6 (4.1.3. Evaluation Metrics), baselines p. 7 (4.2.2. Deblurring Metrics), p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.2.3. Performance Analysis), p. 8 (4.2.3. Performance Analysis), p. 3 (Figure/Table caption), results p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.3. Ablation Study), p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.2.3. Performance Analysis), p. 6 (4.1.3. Evaluation Metrics), p. 6 (4.1. Experiment Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
