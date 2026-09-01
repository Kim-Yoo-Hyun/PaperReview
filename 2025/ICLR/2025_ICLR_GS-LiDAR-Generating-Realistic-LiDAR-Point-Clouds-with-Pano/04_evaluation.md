# Evaluation - GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RMaRBE9s2H; PDF retrieval source: https://openreview.net/pdf/a7ebe3e9ae8605b40c3a104d0b74ef8ce5d5750e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 1 (Figure/Table caption), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT)): As illustrated in Figure 6 and Figure 7, GS-LiDAR achieves significantly better visual quality in simulated depth and intensity maps compared to competitors.

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** For the nuScenes dataset, the LiDAR system uses 32 beams with a 40-degree vertical FOV and a 20Hz acquisition frequency.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** 4.1 EXPERIMENT SETUP Datasets We conduct extensive experiments on both dynamic and static scenes using the KITTI360 (Liao et al., 2022) and nuScenes (Caesar et ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** 4.2 EVALUATION ON STATIC SCENES Table 1 provides the quantitative results for static scenes in KITTI-360 dataset across all methods.
- **p. 10 / 4 EXPERIMENT - extractive PDF cue:** 4.3 EVALUATION ON DYNAMIC SCENES To further validate the effectiveness of GS-LiDAR, we conduct LiDAR synthesis evaluations on dynamic scenes from the KITTI-360 and nuScenes ...
- **p. 10 / 4 EXPERIMENT - extractive PDF cue:** For the nuScenes dataset, as shown in Table 3, GS-LiDAR also showcases notable performance, with a 2.5% reduction in chamfer distance for simulated point cloud, ...
- **p. 14 / A.2 EXPERIMENTS ON WAYMO DATASET - extractive PDF cue:** We additionally conducted experiments on sequences selected by PVG (Chen et al., 2023a) from the Waymo (Sun et al., 2020) dataset.
- **p. 14 / A.2 EXPERIMENTS ON WAYMO DATASET - extractive PDF cue:** Since methods like LiDAR4D (Zheng et al., 2024) have not been implemented on the Waymo dataset, we only report our own results in Table 5.
- **p. 15 / A.2 EXPERIMENTS ON WAYMO DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 5: Metrics on Waymo dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 8); A.2 EXPERIMENTS ON WAYMO DATASET (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | As illustrated in Figure 6 and Figure 7, GS-LiDAR achieves significantly better visual quality in simulated depth and intensity maps compared to competitors. | p. 10 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | Additionally, the ray-drop refinement technique improves the accuracy of the ray-drop mask, resulting in substantial gains in the metrics for simulated depth and intensity. | p. 10 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | GS-LiDAR outperforms the competitors on most metrics. | p. 9 (4 EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 1: GS-LiDAR achieves superior LiDAR simulation quality for novel view synthesis while maintaining fast training and rendering speed. | p. 1 (Figure/Table caption) |
| 4 EXPERIMENT | EMPIRICAL / SIMULATION | We also provide the results on the Waymo (Sun et al., 2020) dataset in Appendix A.2. | p. 8 (4 EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** For the nuScenes dataset, the LiDAR system uses 32 beams with a 40-degree vertical FOV and a 20Hz acquisition frequency.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** 4.1 EXPERIMENT SETUP Datasets We conduct extensive experiments on both dynamic and static scenes using the KITTI360 (Liao et al., 2022) and nuScenes (Caesar et ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** 4.2 EVALUATION ON STATIC SCENES Table 1 provides the quantitative results for static scenes in KITTI-360 dataset across all methods.
- **p. 10 / 4 EXPERIMENT - extractive PDF cue:** 4.3 EVALUATION ON DYNAMIC SCENES To further validate the effectiveness of GS-LiDAR, we conduct LiDAR synthesis evaluations on dynamic scenes from the KITTI-360 and nuScenes ...
- **p. 10 / 4 EXPERIMENT - extractive PDF cue:** For the nuScenes dataset, as shown in Table 3, GS-LiDAR also showcases notable performance, with a 2.5% reduction in chamfer distance for simulated point cloud, ...
- **p. 14 / A.2 EXPERIMENTS ON WAYMO DATASET - extractive PDF cue:** We additionally conducted experiments on sequences selected by PVG (Chen et al., 2023a) from the Waymo (Sun et al., 2020) dataset.
- **p. 14 / A.2 EXPERIMENTS ON WAYMO DATASET - extractive PDF cue:** Since methods like LiDAR4D (Zheng et al., 2024) have not been implemented on the Waymo dataset, we only report our own results in Table 5.
- **p. 15 / A.2 EXPERIMENTS ON WAYMO DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 5: Metrics on Waymo dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: GS-LiDAR achieves superior LiDAR simulation quality for novel view synthesis while maintaining fast training and rendering speed.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of the GS-LiDAR framework: GS-LiDAR is based on 2D Gaussian primitives with periodic vibration properties, allowing for dynamic modeling of position and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Our LiDAR coordinate system and two ways of depth rendering. The mean depth refers to the weighted average of each depth using the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Panoramic Gaussian rasterization details. (a) Our method employs tile-based sorting and rendering. For panoramic ray maps, we first transform the epipolar coordinate system ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Comparison of 3D LiDAR point cloud. GS-LiDAR produces a more cohesive LiDAR point cloud compared to LiDAR-NeRF (Tao et al., 2023) and LiDAR4D ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: State-of-the-art comparison on KITTI-360 Static Scene Sequence. We color the top results as best and second best .
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: State-of-the-art comparison on KITTI-360 dataset. We color the top results as best and second best .
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: State-of-the-art comparison on nuScenes dataset. The notations are consistent with the KITTI-360 Table 2 above.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the nuScenes dataset, the LiDAR system uses 32 beams with a 40-degree vertical FOV and a 20Hz acquisition frequency. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Task/environment | 4.1 EXPERIMENT SETUP Datasets We conduct extensive experiments on both dynamic and static scenes using the KITTI360 (Liao et al., 2022) and nuScenes (Caesar ... | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (3 METHOD), p. 4 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 8 (3 METHOD), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 7: Comparison of the rendered intensity map with competitors. Metrics We employ a comprehensive set of evaluation metrics for assessing point cloud, depth, ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Method Point Cloud Depth Intensity CD↓ F-score↑ RMSE↓ MedAE↓ LPIPS↓ SSIM↑ PSNR↑ RMSE↓ MedAE↓ LPIPS↓ SSIM↑ PSNR↑ GS-LiDAR (Ours) 0.2382 0.9055 5.8925 0.0198 0.0708 ... | definition/direction/unit from same section | p. 15 (A.2 EXPERIMENTS ON WAYMO DATASET) |
| For the KITTI-360 dataset, as shown in Table 2, our method demonstrates superior performance, achieving a 0.3% reduction in chamfer distance for simulated point ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| Additionally, the ray-drop refinement technique improves the accuracy of the ray-drop mask, resulting in substantial gains in the metrics for simulated depth and intensity. | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| Published as a conference paper at ICLR 2025 Figure 6: Comparison of the rendered depth map with competitors. | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| The first two rows depict the depth maps, while the subsequent two rows illustrate the intensity maps. | definition/direction/unit from same section | p. 15 (A.2 EXPERIMENTS ON WAYMO DATASET) |
| Figure 4: Panoramic Gaussian rasterization details. (a) Our method employs tile-based sorting and rendering. For panoramic ray maps, we first transform the epipolar coordinate ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 2: Overview of the GS-LiDAR framework: GS-LiDAR is based on 2D Gaussian primitives with periodic vibration properties, allowing for dynamic modeling of position ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Additionally, we compare our results with the perscene optimized reconstruction method NKSR (Huang et al., 2023), LiDAR-NeRF (Tao et al., 2023) and the state-of-the-art ... | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| GS-LiDAR outperforms the competitors on most metrics. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| As illustrated in Figure 6 and Figure 7, GS-LiDAR achieves significantly better visual quality in simulated depth and intensity maps compared to competitors. | comparison identity and matched condition | p. 10 (4 EXPERIMENT) |
| Table 1: State-of-the-art comparison on KITTI-360 Static Scene Sequence. We color the top results as best and second best . | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 5: Comparison of 3D LiDAR point cloud. GS-LiDAR produces a more cohesive LiDAR point cloud compared to LiDAR-NeRF (Tao et al., 2023) and ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3: State-of-the-art comparison on nuScenes dataset. The notations are consistent with the KITTI-360 Table 2 above. | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Published as a conference paper at ICLR 2025 Table 4: Ablation studies on various components of GS-LiDAR. | component/input/data sensitivity | p. 10 (4 EXPERIMENT) |
| 4.4 ABLATION STUDY We provide quantitative ablation studies on various components of GS-LiDAR in Table 4. | component/input/data sensitivity | p. 10 (4 EXPERIMENT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Published as a conference paper at ICLR 2025 Our contributions are summarized as follows: (1) We propose GS-LiDAR, a novel differentiable framework for generating ... | As illustrated in Figure 6 and Figure 7, GS-LiDAR achieves significantly better visual quality in simulated depth and intensity maps compared to competitors. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 1 (Figure/Table caption), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Primary metric/result | Additionally, the ray-drop refinement technique improves the accuracy of the ray-drop mask, resulting in substantial gains in the metrics for simulated depth and intensity. | numeric claim only at cited anchor | p. 10 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** The KITTI-360 dataset employs a 64-beam LiDAR with a vertical field of view (FOV) of 26.4 degrees and an acquisition frequency of 10Hz.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Following LiDAR4D (Zheng et al., 2024), we select 51 consecutive frames as a single scene and hold out 4 samples at 10-frame intervals for novel ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** For the nuScenes dataset, the LiDAR system uses 32 beams with a 40-degree vertical FOV and a 20Hz acquisition frequency.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** To ensure consistency with KITTI-360, we maintain a sampling frequency of 10Hz.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** All experiments are conducted on a single NVIDIA RTX A6000 GPU, with a total of 30,000 iterations, taking approximately 1.5 hours to produce the final ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** The rendering speed reaches up to 11 frames per second (FPS).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation details We randomly sample 1 × 106 LiDAR points for point initialization. | p. 9 (4 EXPERIMENT) |
| All experiments are conducted on a single NVIDIA RTX A6000 GPU, with a total of 30,000 iterations, taking approximately 1.5 hours to produce the ... | p. 9 (4 EXPERIMENT) |
| The 2D covariance matrix Σ′ of the projected Gaussian primitive in camera coordinates is computed as: Σ′ = JW ΣW ⊤J⊤. | p. 4 (3 METHOD) |
| Given the pixel coordinates of a point on the range image (ξ, η), the corresponding radian angles can be computed using the following equation: ... | p. 5 (3 METHOD) |
| (11) By multiplying (sin θ sin ϕ, -cos θ, sin θ cos ϕ, 0) on both sides, the distance r can be computed as: ... | p. 6 (3 METHOD) |
| (b) During pixel rendering, the α and depth are computed by calculating the intersection between the ray and the Gaussian primitive. the ray angles ... | p. 6 (3 METHOD) |
| To achieve this, we align the rendered normal map N with the pseudo-normal map ˜ N, which is computed from the gradients of the ... | p. 8 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 14 (A.2 EXPERIMENTS ON WAYMO DATASET), metrics p. 9 (Figure/Table caption), p. 15 (A.2 EXPERIMENTS ON WAYMO DATASET), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 15 (A.2 EXPERIMENTS ON WAYMO DATASET), baselines p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 1 (Figure/Table caption), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
