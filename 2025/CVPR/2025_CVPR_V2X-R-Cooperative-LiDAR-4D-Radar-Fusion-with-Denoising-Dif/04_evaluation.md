# Evaluation - V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 7 (5.3. Benchmark Analysis), p. 7 (5.3. Benchmark Analysis), p. 1 (Figure/Table caption)): Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the performance un- der different weather conditions. ...

## Evaluation Body Digest

- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive body cue:** Performance comparison under different real-world weather on K-Radar dataset.
- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive body cue:** We further conducted experiments on the K-Radar single-agent real-world dataset.
- **p. 6 / 5.2. Benchmark Models - extractive body cue:** Experimental 3D object detection results of various cooperative LiDAR-based methods on the validation and testing of our V2X-R dataset in different IoU (0.3,0.5,0.7).
- **p. 3 / 3.4. Adverse Weather Simulation - extractive body cue:** To analyze the performance under adverse weather conditions on our V2X-R dataset, we applied fog [8] and snow [9] simulations to the LiDAR point clouds ...
- **p. 3 / 3.1. Simulator Selection - extractive body cue:** However, since CARLA lacks vehicleto-everything (V2X) communication and cooperative driving capabilities, we used OpenCDA [53] integrated with CARLA, a cooperative simulation platform that supports multiple ...
- **p. 6 / 5.2. Benchmark Models - extractive body cue:** We implement various state-of-the-art 3D object detectors on the V2X-R dataset, including different numbers of agents and different modalities.
- **p. 7 / 5.3. Benchmark Analysis - extractive body cue:** We also pioneered the exploration of cooperative 4D radarbased methods on the V2X dataset.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive body cue:** The pipeline of constructed cooperative LiDAR-4D radar fusion for weather-robust 3D object detection.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 2.2. Cooperative Perception Datasets (p. 3); 3. V2X-R Dataset (p. 3); 5. Experiments (p. 6); 5.1. Experimental Details and Metrics (p. 6); 5.2. Benchmark Models (p. 6); 5.3. Benchmark Analysis (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D ... | p. 2 (Figure/Table caption) |
| 5.4. Multi-modal Diffusion Denoising Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although MDD inevitably introduces an additional inference time of 32 ms, it significantly improves weather robustness and still maintains real-time (about 20 FPS). | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| 5.3. Benchmark Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 4, by comparing with Tables 2 and 3, it can be observed that almost all cooperative LiDAR-4D radar fusion models ... | p. 7 (5.3. Benchmark Analysis) |
| 5.3. Benchmark Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates ... | p. 7 (5.3. Benchmark Analysis) |

## Dataset / Benchmark Role

- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive body cue:** Performance comparison under different real-world weather on K-Radar dataset.
- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive body cue:** We further conducted experiments on the K-Radar single-agent real-world dataset.
- **p. 6 / 5.2. Benchmark Models - extractive body cue:** Experimental 3D object detection results of various cooperative LiDAR-based methods on the validation and testing of our V2X-R dataset in different IoU (0.3,0.5,0.7).
- **p. 3 / 3.4. Adverse Weather Simulation - extractive body cue:** To analyze the performance under adverse weather conditions on our V2X-R dataset, we applied fog [8] and snow [9] simulations to the LiDAR point clouds ...
- **p. 3 / 3.1. Simulator Selection - extractive body cue:** However, since CARLA lacks vehicleto-everything (V2X) communication and cooperative driving capabilities, we used OpenCDA [53] integrated with CARLA, a cooperative simulation platform that supports multiple ...
- **p. 6 / 5.2. Benchmark Models - extractive body cue:** We implement various state-of-the-art 3D object detectors on the V2X-R dataset, including different numbers of agents and different modalities.
- **p. 7 / 5.3. Benchmark Analysis - extractive body cue:** We also pioneered the exploration of cooperative 4D radarbased methods on the V2X dataset.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive body cue:** The pipeline of constructed cooperative LiDAR-4D radar fusion for weather-robust 3D object detection.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The advantages of the dense 4D radar point cloud in multi-agent view. Including weather robustness, fewer spatial er- rors, Doppler information, and geometric ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D radar ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Sensor configuration details of our V2X-R dataset. 0 0.1 0.2 0.3 0.4 0.5 15
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. 4D radar point cloud occupancy rate (a) and number of points (b) within the ground truth bounding boxes for radial distance from ego ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. The pipeline of constructed cooperative LiDAR-4D radar fusion for weather-robust 3D object detection. The fusion pipeline (a) is first fed with multi-modal point ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of LiDAR point cloud under foggy (simu- lated) weather before and after multi-agent communication. After multi-agent communication, the LiDAR point cloud has ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Experimental 3D object detection results of various coop- erative LiDAR-based methods on the validation and testing of our V2X-R dataset in different IoU ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Experimental 3D object detection results of various co- operative 4D Radar-based methods on the validation and testing of our V2X-R dataset in different ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Performance comparison under different real-world weather on K-Radar dataset. | embodiment, simulator version and control stack | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Task/environment | We further conducted experiments on the K-Radar single-agent real-world dataset. | reset, timeout, object/scene variation | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 6 (5.2. Benchmark Models) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)), p. 4 (4.2. Fusion Pipeline) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| As shown in Table 6, our MDD module demonstrates significant performance improvements in real-world adverse weather, with 3D mAP gains of 5.20% and 5.97% ... | definition/direction/unit from same section | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Experimental 3D object detection results of various cooperative LiDAR-based methods on the validation and testing of our V2X-R dataset in different IoU (0.3,0.5,0.7). | definition/direction/unit from same section | p. 6 (5.2. Benchmark Models) |
| To intuitively compare the performance in normal weather differences between modalities, the cooperative LiDAR-4D radar fusion 3D object detectors we implemented in the benchmark ... | definition/direction/unit from same section | p. 6 (5.2. Benchmark Models) |
| The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates ... | definition/direction/unit from same section | p. 7 (5.3. Benchmark Analysis) |
| Figure 1. The advantages of the dense 4D radar point cloud in multi-agent view. Including weather robustness, fewer spatial er- rors, Doppler information, and ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| As shown in Table 3, the performance of 4D radar-based models is generally lower than that of LiDAR-based models in Table 2. | definition/direction/unit from same section | p. 7 (5.3. Benchmark Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We implement various state-of-the-art 3D object detectors on the V2X-R dataset, including different numbers of agents and different modalities. | comparison identity and matched condition | p. 6 (5.2. Benchmark Models) |
| As shown in Table 4, by comparing with Tables 2 and 3, it can be observed that almost all cooperative LiDAR-4D radar fusion models ... | comparison identity and matched condition | p. 7 (5.3. Benchmark Analysis) |
| Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates ... | comparison identity and matched condition | p. 7 (5.3. Benchmark Analysis) |
| Table 6. The 3D mAP performance comparison on K-Radar [30] dataset. Adverse represents average results under various adverse weather, including overcast, fog, rain, sleet, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluated the effect of each component, as shown in Table 7. | component/input/data sensitivity | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. | component/input/data sensitivity | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized in three key points: • We present V2X-R, the first simulated V2X dataset that not only includes LiDAR, cameras, ... | Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 7 (5.3. Benchmark Analysis), p. 7 (5.3. Benchmark Analysis), p. 1 (Figure/Table caption) |
| Primary metric/result | Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / 3.2. Sensor configuration - extractive body cue:** As described in Table 1, each Connected Autonomous Vehicle (CAV) and Infrastructure is equipped with four cameras; a 64-channel LiDAR sensor featuring a detection range ...
- **p. 3 / 3.2. Sensor configuration - extractive body cue:** The Sensors Details 4x Camera 4 units RGB,Positions: (2.5,0,1.0,0),(0.0,0.3,1.8,100), (0.0,-0.3,1.8,-100), (-2.0,0.0,1.5,180) 1x LiDAR 64 channels,120m range, -25◦to 2◦vertical FOV, 0.02 noise standard deviation, 20 Hz ...
- **p. 3 / 3.2. Sensor configuration - extractive body cue:** 4D radar point cloud occupancy rate (a) and number of points (b) within the ground truth bounding boxes for radial distance from ego vehicles. vehicle ...
- **p. 3 / 3.2. Sensor configuration - extractive body cue:** Finally, based on the above configuration, our V2XR contains a total of 12,079 scenarios with 37,727 frames of LiDAR and 4D radar point clouds, 150,908 ...
- **p. 6 / 5.1. Experimental Details and Metrics - extractive body cue:** We used 8,084/829/3,166 frames for training/ validation/ testing in our V2X-R dataset, ensuring there is no overlap in the intersection of the training/validation/testing sets.
- **p. 6 / 5.1. Experimental Details and Metrics - extractive body cue:** We set the broadcast range among CAVs to be 70 meters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This can be attributed to the significantly lower resolution of 4D radar than LiDAR, which is a limitation hindering the independent use of 4D ... | p. 7 (5.3. Benchmark Analysis) |
| body limitation/failure cue | The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates ... | p. 7 (5.3. Benchmark Analysis) |
| body limitation/failure cue | Figure 1. The advantages of the dense 4D radar point cloud in multi-agent view. Including weather robustness, fewer spatial er- rors, Doppler information, and ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Moreover, we propose the MDD module to tackle dense noise in collaborative conditions. | p. 8 (6. Conclusion and Discussion) |
| body limitation/failure cue | A compelling research direction is the full utilization of multi-agent and multi-modal information for robust 3D object detection. | p. 8 (6. Conclusion and Discussion) |
| body limitation/failure cue | The input noisy LiDAR features are first subjected to a diffusion process, followed by T step denoising process with weather-robust 4D radar features as ... | p. 4 (3.4. Adverse Weather Simulation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Although MDD inevitably introduces an additional inference time of 32 ms, it significantly improves weather robustness and still maintains real-time (about 20 FPS). | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Fusing 4D radar and LiDAR is expected to improve the perThis CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (1. Introduction) |
| The entire pipeline consists of four stages: 1) Encode by each agent. | p. 2 (1. Introduction) |
| 4(a), subsequent fusion consists of four stages: 1) Encode by agent. | p. 4 (4.2. Fusion Pipeline) |
| We feed X into a agent-shared encoder Gθ to obtain features for each agent and modality as: | p. 4 (4.2. Fusion Pipeline) |
| (7) For the final output after T denoising steps, the Uθ generates the denoised clear LiDAR feature ˜ FL A = F0. | p. 5 (A Finit ←FL) |
| We explored two implementations that extend the existing mature fusion to cooperative LiDAR-4D radar fusion: (a) Single-Agent Multi-Modal to Multi-Agent MultiModal (SA2MA). | p. 5 (3) Modal fusion. The weather-induced noisy LiDAR fea) |
| All hyperparameters are detailed in the supplementary material. | p. 6 (4.4. Loss Function) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.3. Benchmark Analysis - extractive body cue:** This can be attributed to the significantly lower resolution of 4D radar than LiDAR, which is a limitation hindering the independent use of 4D radar ...
- **p. 7 / 5.3. Benchmark Analysis - extractive body cue:** The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates that ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The advantages of the dense 4D radar point cloud in multi-agent view. Including weather robustness, fewer spatial er- rors, Doppler information, and geometric ...
- **p. 8 / 6. Conclusion and Discussion - extractive body cue:** Moreover, we propose the MDD module to tackle dense noise in collaborative conditions.
- **p. 8 / 6. Conclusion and Discussion - extractive body cue:** A compelling research direction is the full utilization of multi-agent and multi-modal information for robust 3D object detection.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive body cue:** The input noisy LiDAR features are first subjected to a diffusion process, followed by T step denoising process with weather-robust 4D radar features as conditions ...

- **Evidence anchors reviewed:** datasets p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 6 (5.2. Benchmark Models), p. 3 (3.4. Adverse Weather Simulation), p. 3 (3.1. Simulator Selection), p. 6 (5.2. Benchmark Models), metrics p. 8 (Figure/Table caption), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 6 (5.2. Benchmark Models), p. 6 (5.2. Benchmark Models), p. 7 (5.3. Benchmark Analysis), p. 1 (Figure/Table caption), baselines p. 6 (5.2. Benchmark Models), p. 7 (5.3. Benchmark Analysis), p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (5.3. Benchmark Analysis), p. 8 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 7 (5.3. Benchmark Analysis), p. 7 (5.3. Benchmark Analysis), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
