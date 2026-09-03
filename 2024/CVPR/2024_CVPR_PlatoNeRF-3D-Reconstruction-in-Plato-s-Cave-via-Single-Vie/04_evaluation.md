# Evaluation - PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Results), p. 7 (4.2. Results), p. 5 (3.3. Implementation Details), p. 5 (4. Experiments), p. 6 (4.1. Datasets), p. 8 (4.3. Ablations)): PlatoNeRF method achieves competitive performance.

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets - extractive body cue:** We create datasets of four scenes of a room with either a chair, bunny, dragon, or occluded bunny in a chair, shown in Fig.
- **p. 5 / 4. Experiments - extractive body cue:** We validate our method on the task of 3D reconstruction across several scenes.
- **p. 6 / 4.1. Datasets - extractive body cue:** The dataset captures a simple indoor scene, shown in Fig.
- **p. 8 / 4.3. Ablations - extractive body cue:** 4.3.2 Ambient Light and Low Albedo Backgrounds In real-world settings, there may be high ambient light or low scene albedo, both of which make detection ...
- **p. 6 / 4.1. Datasets - extractive body cue:** We use a dataset of single-photon lidar data captured by Henley et al.
- **p. 7 / 4.3. Ablations - extractive body cue:** All ablations are done on the chair scene.
- **p. 7 / 4.2. Results - extractive body cue:** (a) Captured scene (stars are illumination spots), (b) BF Lidar result, (c) PlatoNeRF result.
- **p. 8 / 4.3. Ablations - extractive body cue:** The non-planar scene contains curved background walls.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.3. Implementation Details (p. 5); 4. Experiments (p. 5); 4.1. Datasets (p. 5); 4.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | PlatoNeRF method achieves competitive performance. | p. 7 (4.2. Results) |
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Due to our use of an implicit representation, we achieve much smoother results than BF Lidar. | p. 7 (4.2. Results) |
| 3.3. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | After 25,000 iterations, when an accurate initial estimate of the virtual detector xp is obtained, we set β to 1/6,000 in most experiments to ... | p. 5 (3.3. Implementation Details) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Then, we share our results, comparisons, and ablations on spatial and temporal resolution, ambient light, low-albedo backgrounds, non-planar backgrounds, and number of illumination points. | p. 5 (4. Experiments) |
| 4.1. Datasets | EMPIRICAL / REAL-ROBOT OR HARDWARE | We provide qualitative results for predicted depth on both train and novel test views, comparing our method, BF Lidar [7], and S3-NeRF [44] to ... | p. 6 (4.1. Datasets) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets - extractive body cue:** We create datasets of four scenes of a room with either a chair, bunny, dragon, or occluded bunny in a chair, shown in Fig.
- **p. 5 / 4. Experiments - extractive body cue:** We validate our method on the task of 3D reconstruction across several scenes.
- **p. 6 / 4.1. Datasets - extractive body cue:** The dataset captures a simple indoor scene, shown in Fig.
- **p. 8 / 4.3. Ablations - extractive body cue:** 4.3.2 Ambient Light and Low Albedo Backgrounds In real-world settings, there may be high ambient light or low scene albedo, both of which make detection ...
- **p. 6 / 4.1. Datasets - extractive body cue:** We use a dataset of single-photon lidar data captured by Henley et al.
- **p. 7 / 4.3. Ablations - extractive body cue:** All ablations are done on the chair scene.
- **p. 7 / 4.2. Results - extractive body cue:** (a) Captured scene (stars are illumination spots), (b) BF Lidar result, (c) PlatoNeRF result.
- **p. 8 / 4.3. Ablations - extractive body cue:** The non-planar scene contains curved background walls.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. PlatoNeRF. We propose PlatoNeRF: a method to recover scene geometry from a single view using two-bounce signals captured by a single-photon lidar. (a) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Problem Definition. We use a lidar system containing a SPAD at position xs and a pulsed laser at position xl. The SPAD view ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Method. PlatoNeRF learns 3D scene geometry from single-view two-bounce lidar time of flight, modeled with NeRF. Our method consists of three steps. (a) ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Depth evaluation. We compare PlatoNeRF to both lidar- and RGB-based single-view 3D reconstruction methods, BF Lidar [7] and S3-NeRF [44], respectively. Depth metrics ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative Depth Results. We provide qualitative results for predicted depth on both train and novel test views, comparing our method, BF Lidar [7], ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Point Cloud Evaluation. We compute the Chamfer dis- tance between the point clouds generated by each method. Metrics are averaged over all four ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Real-World Results. (a) Captured scene (stars are illumi- nation spots), (b) BF Lidar result, (c) PlatoNeRF result. Our method yields similar results as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablations on Lidar Sensor. Lidars on consumer devices have lower spatial- and temporal-resolution than research-grade lidars. We ablate the impact of these sensor ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We create datasets of four scenes of a room with either a chair, bunny, dragon, or occluded bunny in a chair, shown in Fig. | embodiment, simulator version and control stack | p. 5 (4.1. Datasets), p. 5 (4. Experiments) |
| Task/environment | We validate our method on the task of 3D reconstruction across several scenes. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4.1. Datasets) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use L1 depth error to evaluate our method for 3D reconstruction, as done in past work [14, 19, 44]. | definition/direction/unit from same section | p. 6 (4.2. Results) |
| We find that depth error for BF Lidar degrades more than PlatoNeRF. | definition/direction/unit from same section | p. 7 (4.3. Ablations) |
| We empirically validate that PlatoNeRF is able to handle ambient light in the scene, while S3-NeRF depth error increases. | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| While depth is visually similar for different temporal resolutions, the error maps indicate increasing displacement of the chair. | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| We compute the Chamfer distance between the point clouds generated by each method. | definition/direction/unit from same section | p. 6 (4.1. Datasets) |
| First, we introduce the simulated datasets that we make available to accelerate future work in learning-based methods for single-photon lidars. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| 1, and Chamfer distance is reported in Tab. | definition/direction/unit from same section | p. 7 (4.2. Results) |
| Then, (5) can be computed by thresholding the confidence map to yield the binary shadow mask. | definition/direction/unit from same section | p. 5 (3.3. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5. Real-World Results. (a) Captured scene (stars are illumi- nation spots), (b) BF Lidar result, (c) PlatoNeRF result. Our method yields similar results ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| (2) and (3) are ablated in comparison to S3-NeRF to highlight the fundamental advantages of using lidar compared to RGB when measuring shadows. | comparison identity and matched condition | p. 7 (4.3. Ablations) |
| Then, we share our results, comparisons, and ablations on spatial and temporal resolution, ambient light, low-albedo backgrounds, non-planar backgrounds, and number of illumination points. | comparison identity and matched condition | p. 5 (4. Experiments) |
| BF Lidar's output is one point cloud (PC) for visible and one for occluded geometry, which we combine for our comparisons. | comparison identity and matched condition | p. 6 (4.2. Results) |
| S3-NeRF reconstructs both the object casting shadows and all other background scene geometry, making it a suitable comparison. | comparison identity and matched condition | p. 6 (4.2. Results) |
| For our illumination spot ablation, we reduce Figure 6. | comparison identity and matched condition | p. 8 (4.3. Ablations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Then, we share our results, comparisons, and ablations on spatial and temporal resolution, ambient light, low-albedo backgrounds, non-planar backgrounds, and number of illumination points. | component/input/data sensitivity | p. 5 (4. Experiments) |
| We compare our work with two methods, one that uses two-bounce lidar for single-view 3D reconstruction without learning and one that uses shadows measured ... | component/input/data sensitivity | p. 6 (4.2. Results) |
| All ablations are done on the chair scene. | component/input/data sensitivity | p. 7 (4.3. Ablations) |
| For our illumination spot ablation, we reduce Figure 6. | component/input/data sensitivity | p. 8 (4.3. Ablations) |
| Quantitative results for these ablations are reported in Tab. | component/input/data sensitivity | p. 8 (4.3. Ablations) |
| Table 3. Ablations on Lidar Sensor. Lidars on consumer devices have lower spatial- and temporal-resolution than research-grade lidars. We ablate the impact of these ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of three steps. | PlatoNeRF method achieves competitive performance. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Results), p. 7 (4.2. Results), p. 5 (3.3. Implementation Details), p. 5 (4. Experiments), p. 6 (4.1. Datasets), p. 8 (4.3. Ablations) |
| Primary metric/result | Due to our use of an implicit representation, we achieve much smoother results than BF Lidar. | numeric claim only at cited anchor | p. 7 (4.2. Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Datasets - extractive body cue:** For each scene, we heuristically choose N =16 points in the left and right parts of the scene, corresponding to the left and right walls, ...
- **p. 6 / 4.1. Datasets - extractive body cue:** Our scene is measured using a 512×512 SPAD with a temporal resolution of 128 ps (3.84 cm).
- **p. 6 / 4.1. Datasets - extractive body cue:** The scene is captured with a 200×200 pixel sensor with an instrument Table 2.
- **p. 7 / 4.3. Ablations - extractive body cue:** Ambient Light L1 Depth (m) Intensity Ours S3-NeRF 0 0.0862 0.1178 4 0.0794 0.3080 Scene Albedo L1 Depth (m) Albedo Ours S3-NeRF 0× less 0.0862 ...
- **p. 7 / 4.3. Ablations - extractive body cue:** Resulting spatial resolutions are 128×128, 64×64, and 32×32.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method has a couple limitations. | p. 8 (5. Conclusion) |
| body limitation/failure cue | In contrast, lidar-based methods, such as PlatoNeRF, are fundamentally more robust to these low signal-to-noise (SNR) and signal-to-background (SBR) scenarios. | p. 8 (4.3. Ablations) |
| body limitation/failure cue | First, we introduce the simulated datasets that we make available to accelerate future work in learning-based methods for single-photon lidars. | p. 5 (4. Experiments) |
| body limitation/failure cue | In general, PlatoNeRF produces smoother depth, but small floaters are noticeable, especially in the nearby floor region, which is an area for future work. | p. 7 (4.2. Results) |
| body limitation/failure cue | We also note that, as in the original work, we train S3-NeRF with RGB images rendered with only one bounce, as we found it ... | p. 7 (4.2. Results) |
| body limitation/failure cue | Table 1. Depth evaluation. We compare PlatoNeRF to both lidar- and RGB-based single-view 3D reconstruction methods, BF Lidar [7] and S3-NeRF [44], respectively. Depth ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training. | p. 5 (3.3. Implementation Details) |
| (1) can be computed using camera matrices and (2) is assumed to be calibrated. | p. 5 (3.3. Implementation Details) |
| We compute the Chamfer distance between the point clouds generated by each method. | p. 6 (4.1. Datasets) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Our method has a couple limitations.
- **p. 8 / 4.3. Ablations - extractive body cue:** In contrast, lidar-based methods, such as PlatoNeRF, are fundamentally more robust to these low signal-to-noise (SNR) and signal-to-background (SBR) scenarios.
- **p. 5 / 4. Experiments - extractive body cue:** First, we introduce the simulated datasets that we make available to accelerate future work in learning-based methods for single-photon lidars.
- **p. 7 / 4.2. Results - extractive body cue:** In general, PlatoNeRF produces smoother depth, but small floaters are noticeable, especially in the nearby floor region, which is an area for future work.
- **p. 7 / 4.2. Results - extractive body cue:** We also note that, as in the original work, we train S3-NeRF with RGB images rendered with only one bounce, as we found it does ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Depth evaluation. We compare PlatoNeRF to both lidar- and RGB-based single-view 3D reconstruction methods, BF Lidar [7] and S3-NeRF [44], respectively. Depth metrics ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Datasets), p. 5 (4. Experiments), p. 6 (4.1. Datasets), p. 8 (4.3. Ablations), p. 6 (4.1. Datasets), p. 7 (4.3. Ablations), metrics p. 6 (4.2. Results), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations), p. 8 (4.3. Ablations), p. 6 (4.1. Datasets), p. 5 (4. Experiments), baselines p. 7 (Figure/Table caption), p. 7 (4.3. Ablations), p. 5 (4. Experiments), p. 6 (4.2. Results), p. 6 (4.2. Results), p. 8 (4.3. Ablations), results p. 7 (4.2. Results), p. 7 (4.2. Results), p. 5 (3.3. Implementation Details), p. 5 (4. Experiments), p. 6 (4.1. Datasets), p. 8 (4.3. Ablations).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
