# Evaluation - TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7983_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07983.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 12 (4 Experiments), p. 9 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments)): Table 4: Performance comparison of depth synthesis from novel views between the proposed method and baseline on the nuScenes dataset. that our approach significantly surpasses 3D-GS in the depth synthesis ...

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive PDF cue:** Datasets: Our experimental evaluations are conducted on two of the most widely-used datasets in autonomous driving research: the Waymo Open Dataset [22] and the nuScenes ...
- **p. 10 / 4 Experiments - extractive PDF cue:** The nuScenes dataset, a large-scale public resource for autonomous driving research, includes data from an array of sensors: six cameras, one LiDAR, five RADARs, GPS, ...
- **p. 10 / 4 Experiments - extractive PDF cue:** To comprehensively evaluate and compare the detail synthesis capabilities, we train and assess our methods and all baselines using full-resolution images, i.e., 1920×1280 for the ...
- **p. 11 / 4 Experiments - extractive PDF cue:** 5: Visual comparison of image synthesis from novel views on nuScenes dataset.
- **p. 12 / 4 Experiments - extractive PDF cue:** More visualization results are provided in the supplementary material project website 3 Evaluation on nuScenes Dataset: We conducted further comprehensive evaluations comparing our method with ...
- **p. 9 / 4 Experiments - extractive PDF cue:** For our experiments, we selected six challenging recording sequences from this dataset, utilizing surrounding views captured by three cameras and corresponding data
- **p. 11 / 4 Experiments - extractive PDF cue:** Evaluation on Waymo Open Dataset: We evaluated the proposed method by comparing it with the baseline on the Waymo Open dataset.
- **p. 12 / 4 Experiments - extractive PDF cue:** We can see that TCLC-GS renders more clear and accurate RGB images than the 3D-GS, especially on roadside objects and in distant areas viewed from ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: Performance comparison of depth synthesis from novel views between the proposed method and baseline on the nuScenes dataset. that our approach significantly ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 7: Ablation study of the proposed method on the Waymo dataset. the primary baseline 3D-GS, are detailed in Table 3 and Table 4 ... | p. 13 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Sequence 3D-GS [11] AbsRel↓/RMSE↓/RMSElog↓ TCLC-GS AbsRel↓/RMSE↓/RMSElog↓ Scene-0008 0.31/9.97/0.47 0.07/4.27/0.12 Scene-0051 0.47/8.68/0.60 0.05/2.21/0.07 Scene-0058 0.35/10.48/0.55 0.06/4.23/0.11 Scene-0062 0.32/8.22/0.39 0.04/4.03/0. ... | p. 12 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4: Visual comparison of image and depth synthesis from novel front-left, front, and front-right surrounding views on the Waymo dataset. Row 1: 3D-GS ... | p. 9 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The performance comparison of image and depth synthesis from novel views, relative to the main baseline, is detailed in Table 1 and Table 2 ... | p. 11 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive PDF cue:** Datasets: Our experimental evaluations are conducted on two of the most widely-used datasets in autonomous driving research: the Waymo Open Dataset [22] and the nuScenes ...
- **p. 10 / 4 Experiments - extractive PDF cue:** The nuScenes dataset, a large-scale public resource for autonomous driving research, includes data from an array of sensors: six cameras, one LiDAR, five RADARs, GPS, ...
- **p. 10 / 4 Experiments - extractive PDF cue:** To comprehensively evaluate and compare the detail synthesis capabilities, we train and assess our methods and all baselines using full-resolution images, i.e., 1920×1280 for the ...
- **p. 11 / 4 Experiments - extractive PDF cue:** 5: Visual comparison of image synthesis from novel views on nuScenes dataset.
- **p. 12 / 4 Experiments - extractive PDF cue:** More visualization results are provided in the supplementary material project website 3 Evaluation on nuScenes Dataset: We conducted further comprehensive evaluations comparing our method with ...
- **p. 9 / 4 Experiments - extractive PDF cue:** For our experiments, we selected six challenging recording sequences from this dataset, utilizing surrounding views captured by three cameras and corresponding data
- **p. 11 / 4 Experiments - extractive PDF cue:** Evaluation on Waymo Open Dataset: We evaluated the proposed method by comparing it with the baseline on the Waymo Open dataset.
- **p. 12 / 4 Experiments - extractive PDF cue:** We can see that TCLC-GS renders more clear and accurate RGB images than the 3D-GS, especially on roadside objects and in distant areas viewed from ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Left: Original 3D-GS [11] based methods directly initialize 3D Gaussians by 3D LiDAR points; Right: Our TCLC-GS enriches the geometry and appearance attributes ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: The pipeline of TCLC-GS: We first merge all the LiDAR sweeps together, and then build a hierarchical octree implicit feature grid using the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3: Visualization of our colorized 3D mesh and dense depths. Row 1: rendered dense surrounding depth images given the camera pose within the 3D ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visual comparison of image and depth synthesis from novel front-left, front, and front-right surrounding views on the Waymo dataset. Row 1: 3D-GS images; ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Performance comparison of image synthesis from novel views between the proposed method and baseline on the Waymo dataset. Sequence 3D-GS [11] AbsRel↓/RMSE↓/RMSElog↓ TCLC-GS ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Performance comparison of depth synthesis from novel views between the proposed method and baseline on the Waymo dataset. from five LiDAR sweeps. Each ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visual comparison of image synthesis from novel views on nuScenes dataset. Row 1: 3D-GS; Row 2: TCLC-GS; Row 3: GT. Sequence 3D-GS [11] ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Performance comparison of image synthesis from novel views between the proposed method and baseline on the nuScenes dataset. depth evaluation, are obtained by ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets: Our experimental evaluations are conducted on two of the most widely-used datasets in autonomous driving research: the Waymo Open Dataset [22] and the ... | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | The nuScenes dataset, a large-scale public resource for autonomous driving research, includes data from an array of sensors: six cameras, one LiDAR, five RADARs, ... | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 Methodology), p. 7 (3 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Methodology), p. 6 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Similarly as the previous research [3,30], we choose three widely-used benchmark metrics, i.e., Absolute Relative Difference (AbsRel), Root Mean Squared Error (RMSE) and Root ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| The performance comparison of image and depth synthesis from novel views, relative to the main baseline, is detailed in Table 1 and Table 2 ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| The significant improvement in depth synthesis performance can be attributed to the robust supervision provided by the rendered dense depths derived from the generated ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| 26.87/0.86/0.25 28.13/0.90/0.18 Average 26.36/0.82/0.28 28.11/0.86/0.22 Table 1: Performance comparison of image synthesis from novel views between the proposed method and baseline on the Waymo ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Furthermore, Table 5 shows that our method exceeds a broader array of baselines in average performance across these same metrics (PSNR, SSIM, and LPIPS) ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| For a visual perspective, the comparison results of image synthesis from novel surrounding views are illustrated in Fig. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Table 7: Ablation study of the proposed method on the Waymo dataset. the primary baseline 3D-GS, are detailed in Table 3 and Table 4 ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Fig. 3: Visualization of our colorized 3D mesh and dense depths. Row 1: rendered dense surrounding depth images given the camera pose within the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 7: Ablation study of the proposed method on the Waymo dataset. the primary baseline 3D-GS, are detailed in Table 3 and Table 4 ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| 26.87/0.86/0.25 28.13/0.90/0.18 Average 26.36/0.82/0.28 28.11/0.86/0.22 Table 1: Performance comparison of image synthesis from novel views between the proposed method and baseline on the Waymo ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Additional comparisons of image synthesis from novel views against a broader range of baselines are depicted in Table 5. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Baselines: We selected 3D-GS [11], which utilizes LiDAR points to directly initialize 3D Gaussians, as our primary baseline for comparison. | comparison identity and matched condition | p. 11 (4 Experiments) |
| To comprehensively evaluate and compare the detail synthesis capabilities, we train and assess our methods and all baselines using full-resolution images, i.e., 1920×1280 for ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| Here, TCLC-GS is observed to render denser and sharper depths compared to 3D-GS, especially in areas further away in the front, front-left, and front-right ... | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7: Ablation study of the proposed method on the Waymo dataset. the primary baseline 3D-GS, are detailed in Table 3 and Table 4 ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 9: The comparison running-time analysis on the nuScenes dataset. TCLC-GS without colorized 3D mesh, initializing 3D Gaussian using 3D mesh without color information; ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present visualization examples of the colorized 3D mesh and dense depths generated by our method in Fig. | Table 4: Performance comparison of depth synthesis from novel views between the proposed method and baseline on the nuScenes dataset. that our approach significantly ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 12 (4 Experiments), p. 9 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Primary metric/result | Table 7: Ablation study of the proposed method on the Waymo dataset. the primary baseline 3D-GS, are detailed in Table 3 and Table 4 ... | numeric claim only at cited anchor | p. 13 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive PDF cue:** Each sequence consists of approximately 100 frames, and we use a random one of every tenth frame as a test frame and the remaining for ...
- **p. 10 / 4 Experiments - extractive PDF cue:** In each sequence, which comprises roughly 40 frames, we randomly select one of every fifth frame as a test frame and utilize the rest for ...
- **p. 10 / 4 Experiments - extractive PDF cue:** To comprehensively evaluate and compare the detail synthesis capabilities, we train and assess our methods and all baselines using full-resolution images, i.e., 1920×1280 for the ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Sequence 3D-GS [11] PSNR↑/SSIM↑/LPIPS↓ TCLC-GS PSNR↑/SSIM↑/LPIPS↓ Scene-0008 25.32/0.82/0.26 26.41/0.85/0.22 Scene-0051 25.84/0.85/0.25 26.78/0.86/0.23 Scene-0058 24.71/0.81/0.27 26.45/0.88/0.20 Scene-0062 25.91/0.87/0.22 27.47/0.89/0.1 ...
- **p. 12 / 4 Experiments - extractive PDF cue:** Sequence 3D-GS [11] AbsRel↓/RMSE↓/RMSElog↓ TCLC-GS AbsRel↓/RMSE↓/RMSElog↓ Scene-0008 0.31/9.97/0.47 0.07/4.27/0.12 Scene-0051 0.47/8.68/0.60 0.05/2.21/0.07 Scene-0058 0.35/10.48/0.55 0.06/4.23/0.11 Scene-0062 0.32/8.22/0.39 0.04/4.03/0. ...
- **p. 13 / 13 Method - extractive PDF cue:** PSNR↑SSIM↑LPIPS↓ NeRF [17] 26.24 0.87 0.47 NeRF-W [16] 26.92 0.89 0.42 Instant-NGP [18] 26.77 0.88 0.40 Point-NeRF [27] 26.26 0.87 0.45 NPLF [20] 25.62 0.88 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 3: Visualization of our colorized 3D mesh and dense depths. Row 1: rendered dense surrounding depth images given the camera pose within the ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Metrics: Following the previous research [5,15,20,28,31], our image synthesis evaluation employs three widely-used benchmark metrics, i.e., peak signal-tonoise ratio (PSNR), structural similarity index measure ... | p. 10 (4 Experiments) |
| body limitation/failure cue | The significant improvement in depth synthesis performance can be attributed to the robust supervision provided by the rendered dense depths derived from the generated ... | p. 12 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The TCLCGS framework is composed of two primary learning components: 1) the octree implicit feature with SDF and RGB decoders (Fig. | p. 4 (3 Methodology) |
| For a query point p, we compute its feature vector Fi(p) by trilinear interpolating its corresponding features at octree node corners. | p. 5 (3 Methodology) |
| The implicit features can be further decoded into signed distance values (SDFs) and RGB colors through a shallow dual-branch MLP decoder. | p. 5 (3 Methodology) |
| Each of these points is then used to retrieve octree implicit features, which are then fed into a dual-branch decoder. | p. 6 (3 Methodology) |
| Subsequently, we generate a colorized 3D mesh M in the form of a triangle mesh by marching cubes [14] based on the decoder predicted ... | p. 6 (3 Methodology) |
| Additionally, to enhance training robustness, we use very shallow MLPs to encode the c and Fi(v) before their integration into the 3D Gaussians. | p. 8 (3 Methodology) |
| The covariance matrix Σ′ in camera coordinates is computed by, \ Sigma ' = JE \Sigma E^TJ^T, \label {eq:9} (8) where E refers to ... | p. 8 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3: Visualization of our colorized 3D mesh and dense depths. Row 1: rendered dense surrounding depth images given the camera pose within the 3D ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Metrics: Following the previous research [5,15,20,28,31], our image synthesis evaluation employs three widely-used benchmark metrics, i.e., peak signal-tonoise ratio (PSNR), structural similarity index measure (SSIM), ...
- **p. 12 / 4 Experiments - extractive PDF cue:** The significant improvement in depth synthesis performance can be attributed to the robust supervision provided by the rendered dense depths derived from the generated accurate ...

- **PDF anchors reviewed:** datasets p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), metrics p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), baselines p. 13 (Figure/Table caption), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), results p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 12 (4 Experiments), p. 9 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
