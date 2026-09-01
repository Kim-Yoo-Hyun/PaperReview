# Evaluation - LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2411.12185; PDF retrieval source: https://arxiv.org/pdf/2411.12185. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT)): 8 highlights that even with cross-modal radar data, accurate localization is consistently achieved using Gaussian maps.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or even ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** 5: Comparison of trajectories using different SLAM algorithms on four sequences of NTU4DRadLM dataset. algorithm which integrates vision, LiDAR, and IMU data, is used as ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Due to the challenge of maintaining photometric consistency in long-distance outdoor scenes, we segmented the low-speed, kilometers-long scenarios as several shorter sequences.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** We intercepted a closed-loop sequence of the hku park 00 data from the handheld scanning dataset provided by R3Live [26], which includes 1280×1024 images at ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** For the sequence cp from NTU4DRadLM dataset, we first constructed the Gaussian map based on camera and LiDAR data using our LiV-GS, then relocalized radar ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** To evaluate trajectory error, we used the open-source tool rpg trajectory evaluation [25] to compute both Absolute Trajectory Error (ATE) and Relative Error (RE), measuring ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** The ATE RMSE is directly used to measure localization accuracy and the image quality of each algorithm is calculated by normalizing the composite score: Image ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** In addition, the bottom two rows in Table III show a minimal rending difference between the outcomes from LiVGS odometry and ground truth, which further ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENT (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | 8 highlights that even with cross-modal radar data, accurate localization is consistently achieved using Gaussian maps. | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | The ATE RMSE is directly used to measure localization accuracy and the image quality of each algorithm is calculated by normalizing the composite score: ... | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the experiments, we evaluate LiV-GS and compare it against other SOTA algorithms from three aspects: localization accuracy, rendering quality, and the reliability of ... | p. 5 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | As the trajectory accuracy, LiV-GS is compared with the established point cloudsbased geometric SLAM algorithm HDL graph SLAM [27], image feature-based visual SLAM algorithm ... | p. 5 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | 6: Comparison of Rendering Results. | p. 6 (IV. EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or even ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** 5: Comparison of trajectories using different SLAM algorithms on four sequences of NTU4DRadLM dataset. algorithm which integrates vision, LiDAR, and IMU data, is used as ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Due to the challenge of maintaining photometric consistency in long-distance outdoor scenes, we segmented the low-speed, kilometers-long scenarios as several shorter sequences.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** We intercepted a closed-loop sequence of the hku park 00 data from the handheld scanning dataset provided by R3Live [26], which includes 1280×1024 images at ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** For the sequence cp from NTU4DRadLM dataset, we first constructed the Gaussian map based on camera and LiDAR data using our LiV-GS, then relocalized radar ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** To evaluate trajectory error, we used the open-source tool rpg trajectory evaluation [25] to compute both Absolute Trajectory Error (ATE) and Relative Error (RE), measuring ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of the system: The SLAM system comprises a tracking and optimization process that together support the visual representation of the Gaussian map. ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Relationship between Density and weight: Gaus- sians based on only color supervision result in isotropic and sparse Gaussians (top left). Regions with dense ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Effect of Normal Restriction: Top: Ellipsoid vi- sualization. Middle: Render images. Bottom: Magnified details of the render. The left comparison (in red) illustrates ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Effect of Splitting via conditional Gaussian con- straints (CGC). Our approach enhances the representation of Gaussians for objects in the images that lack ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Comparison of trajectories using different SLAM algorithms on four sequences of NTU4DRadLM dataset. algorithm which integrates vision, LiDAR, and IMU data, is used ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Comparison of Rendering Results.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Comparison of performance metrics and system runtime. FPS is calculated as the ratio of the total number of processed frames to the total ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 8: Visualization of cross-modal mmWave radar lo- calization trajectory. mmWave radar localization on the Gaussian map. Unlike LiDAR, the point clouds of mm-Wave radar ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Task/environment | 5: Comparison of trajectories using different SLAM algorithms on four sequences of NTU4DRadLM dataset. algorithm which integrates vision, LiDAR, and IMU data, is used ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The ATE RMSE is directly used to measure localization accuracy and the image quality of each algorithm is calculated by normalizing the composite score: ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| In addition, the bottom two rows in Table III show a minimal rending difference between the outcomes from LiVGS odometry and ground truth, which ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| 7a and 7b, LiV-GS simultaneously reaches state-of-the-art performance in both accuracy and rendering quality with a running speed of 7.98 FPS, showing its potential ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| However, in high-speed sequence loop2, the accuracy of LiVGS is slightly lower than NeRF-LOAM due to larger displacement between the consecutive frames and sparse ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| In the experiments, we evaluate LiV-GS and compare it against other SOTA algorithms from three aspects: localization accuracy, rendering quality, and the reliability of ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| To evaluate trajectory error, we used the open-source tool rpg trajectory evaluation [25] to compute both Absolute Trajectory Error (ATE) and Relative Error (RE), ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| Fig. 3: Effect of Normal Restriction: Top: Ellipsoid vi- sualization. Middle: Render images. Bottom: Magnified details of the render. The left comparison (in red) ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 1: Overview of the system: The SLAM system comprises a tracking and optimization process that together support the visual representation of the Gaussian ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For rendering evaluation, the optimized viewpoints from each algorithm were extracted and compared against the actual images using metrics of SSIM, PSNR[dB], and LPIPS. | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| As the trajectory accuracy, LiV-GS is compared with the established point cloudsbased geometric SLAM algorithm HDL graph SLAM [27], image feature-based visual SLAM algorithm ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| Evaluation between performance and runtime To further estimate the tradeoff between efficiency and performance of LiV-GS, we compared the relationship between runtime and previously ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |
| 7a and 7b, LiV-GS simultaneously reaches state-of-the-art performance in both accuracy and rendering quality with a running speed of 7.98 FPS, showing its potential ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |
| 6: Comparison of Rendering Results. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| Fig. 3: Effect of Normal Restriction: Top: Ellipsoid vi- sualization. Middle: Render images. Bottom: Magnified details of the render. The left comparison (in red) ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3: Effect of Normal Restriction: Top: Ellipsoid vi- sualization. Middle: Render images. Bottom: Magnified details of the render. The left comparison (in red) ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 4: Effect of Splitting via conditional Gaussian con- straints (CGC). Our approach enhances the representation of Gaussians for objects in the images that ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To the end, we introduce LiV-GS, a SLAM framework that uses 3D Gaussian spatial representations to seamlessly integrate LiDAR and camera images. | 8 highlights that even with cross-modal radar data, accurate localization is consistently achieved using Gaussian maps. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Primary metric/result | The ATE RMSE is directly used to measure localization accuracy and the image quality of each algorithm is calculated by normalizing the composite score: ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** Implementation Details LiDAR and image data were synchronized using timestamps, and the trajectories obtained by the R3Live [26] 0 20 40 60 80 x [m] ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** All of the algorithms were run on a desktop with an NVIDIA RTX 4090 GPU.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Datasets To effectively evaluate our LiV-GS, we utilized the opensource large-scale dataset NTU4DRadLM, which includes the data collected by three different types of sensors: LivoxHorizon ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** For the cp sequence, we used the first 2400 LiDAR-camera aligned images, covering approximately 230 meters.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** For the garden and nyl sequences, we selected 2100 and 2400 images respectively from both the beginning and end of each sequence, with each segment ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Additionally, for the Loop2 sequence recorded on a human-driving vehicle platform, we selected 300 frames covering about 250 meters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this looped sequence, our LiV-GS still performs well but its performance falls behind some other algorithms occasionally. | p. 7 (IV. EXPERIMENT) |
| body limitation/failure cue | MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or ... | p. 6 (IV. EXPERIMENT) |
| body limitation/failure cue | Fig. 8: Visualization of cross-modal mmWave radar lo- calization trajectory. mmWave radar localization on the Gaussian map. Unlike LiDAR, the point clouds of mm-Wave ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Our method does not use the IMU data. | p. 6 (IV. EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All of the algorithms were run on a desktop with an NVIDIA RTX 4090 GPU. | p. 5 (IV. EXPERIMENT) |
| To evaluate trajectory error, we used the open-source tool rpg trajectory evaluation [25] to compute both Absolute Trajectory Error (ATE) and Relative Error (RE), ... | p. 5 (IV. EXPERIMENT) |
| 7: Comparison of performance metrics and system runtime. | p. 7 (IV. EXPERIMENT) |
| With the back-end configured with five-keyframe optimization at a time, the average runtime of the pose optimization and map update modules are 0.04 ms ... | p. 7 (IV. EXPERIMENT) |
| (4) The regularization term would be multiplied by a hyperparameter for adjustment, aims to reinforce the alignment of normals. | p. 3 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** In this looped sequence, our LiV-GS still performs well but its performance falls behind some other algorithms occasionally.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or even ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 8: Visualization of cross-modal mmWave radar lo- calization trajectory. mmWave radar localization on the Gaussian map. Unlike LiDAR, the point clouds of mm-Wave radar ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Our method does not use the IMU data.

- **PDF anchors reviewed:** datasets p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), metrics p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), baselines p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 3 (Figure/Table caption), results p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
