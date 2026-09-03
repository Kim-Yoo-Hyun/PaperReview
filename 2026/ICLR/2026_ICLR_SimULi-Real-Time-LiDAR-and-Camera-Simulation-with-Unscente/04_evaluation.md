# Evaluation - SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=osxP6FafPZ; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247739. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption)): Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all values of ⇀d, and renders LiDAR ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We perform experiments on all four scenes of the Waymo Interp. benchmark (Huang et al., 2023) and follow the suggested protocol of holding out every ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We measure reconstruction on the same PandaSet scenes as SplatAD (Hess et al., 2025) and novel view synthesis on both PandaSet and the Waymo Dynamic ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** RMSE↑ RayDrop→ CD ↑ MP/s→ MR/s→ OmniRe (Chen et al., 2025) 25.13 0.757 0.351 0.425 0.113 - - 1.126 53.19 - StreetGS (Yan et al., ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We validate the effectiveness of our method on two commonly used AV datasets across cameraonly, LiDAR-only, and joint camera-LiDAR baselines.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We further measure SplatAD (Hess et al., 2025), NeuRAD (Tonderski et al., 2024) and neurad-studio's UniSim (Yang et al., 2023b) implementation as joint camera-LiDAR baselines, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Although our camera rendering builds upon 3DGUT (Wu et al., 2025b), the improvements in our pipeline (anchoring, appearance variation, environment map) improve rendering quality by ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We list the median absolute depth error, mean relative depth accuracy, and chamfer distance of LiDAR predictions in meters, and intensity and ray drop accuracy ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** It outperforms LiDAR-RT (Zhou et al., 2025), which solely targets LiDAR reconstruction, on all metrics except ray drop accuracy (for which LiDAR-RT uses a U-Net ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all ... | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | It outperforms LiDAR-RT (Zhou et al., 2025), which solely targets LiDAR reconstruction, on all metrics except ray drop accuracy (for which LiDAR-RT uses a ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Visually, SimULi outperforms all methods by >2dB PSNR, and is best or nearly-best across all other metrics. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Bilateral grids and environment maps improve camera quality to different degrees. | p. 10 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2: Method Overview. We model the scene as a dynamic graph (Ost et al., 2021) and pa- rameterize the background and each actor ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We perform experiments on all four scenes of the Waymo Interp. benchmark (Huang et al., 2023) and follow the suggested protocol of holding out every ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We measure reconstruction on the same PandaSet scenes as SplatAD (Hess et al., 2025) and novel view synthesis on both PandaSet and the Waymo Dynamic ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** RMSE↑ RayDrop→ CD ↑ MP/s→ MR/s→ OmniRe (Chen et al., 2025) 25.13 0.757 0.351 0.425 0.113 - - 1.126 53.19 - StreetGS (Yan et al., ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We validate the effectiveness of our method on two commonly used AV datasets across cameraonly, LiDAR-only, and joint camera-LiDAR baselines.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We further measure SplatAD (Hess et al., 2025), NeuRAD (Tonderski et al., 2024) and neurad-studio's UniSim (Yang et al., 2023b) implementation as joint camera-LiDAR baselines, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Although our camera rendering builds upon 3DGUT (Wu et al., 2025b), the improvements in our pipeline (anchoring, appearance variation, environment map) improve rendering quality by ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: SimULi. We design a factorized 3D Gaussian representation that encodes camera and LiDAR information into separate sets of 3D Gaussians joined via nearest-neighbor ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Method Overview. We model the scene as a dynamic graph (Ost et al., 2021) and pa- rameterize the background and each actor with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: LiDAR Tiling. As the measurement pattern of commonly used LiDAR sensors (Xiao et al., 2021) is irregular (left), rendering with equally spaced tiles ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Depth Supervision. Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss. As cross-sensor data is not ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Waymo Interp. SimULi renders the fastest, outperforms all baselines by >2dB PSNR, and gives better depth reconstruction than LiDAR-only LiDAR-RT (Zhou et al., ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for upsampling (Yang et al., 2023b; Tonderski et ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Waymo Dynamic. As with static reconstruction (Table 1), we render the fastest and report best or next-best results across every camera and LiDAR ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We perform experiments on all four scenes of the Waymo Interp. benchmark (Huang et al., 2023) and follow the suggested protocol of holding out ... | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Task/environment | We measure reconstruction on the same PandaSet scenes as SplatAD (Hess et al., 2025) and novel view synthesis on both PandaSet and the Waymo ... | reset, timeout, object/scene variation | p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 METHOD), p. 7 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We list the median absolute depth error, mean relative depth accuracy, and chamfer distance of LiDAR predictions in meters, and intensity and ray drop ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| It outperforms LiDAR-RT (Zhou et al., 2025), which solely targets LiDAR reconstruction, on all metrics except ray drop accuracy (for which LiDAR-RT uses a ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 4: Depth Supervision. Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss. As cross-sensor data is ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 1: SimULi. We design a factorized 3D Gaussian representation that encodes camera and LiDAR information into separate sets of 3D Gaussians joined via ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We also ablate the bilateral grids and environment map used to improve camera rendering. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| We compare our factorized model to the alternative of encoding all sensors into a single particle set and vary the strength of LiDAR depth ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Figure 2: Method Overview. We model the scene as a dynamic graph (Ost et al., 2021) and pa- rameterize the background and each actor ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 5. Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| To measure against the widest possible set of baselines, we first measure novel view synthesis on static scenes used to evaluate prior work (Huang ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| We outperform all prior work by a wide margin, improving upon the second-best method (SplatAD) by >1dB PSNR while rendering camera views 60% faster. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Table 1: Waymo Interp. SimULi renders the fastest, outperforms all baselines by >2dB PSNR, and gives better depth reconstruction than LiDAR-only LiDAR-RT (Zhou et ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Compared to SplatAD (Hess et al., 2025), the method closest to ours, we improve PSNR by 0.4-1.7 dB without relying on CNNs for view ... | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| We validate the effectiveness of our method on two commonly used AV datasets across cameraonly, LiDAR-only, and joint camera-LiDAR baselines. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate image quality through PSNR, SSIM (Wang et al., 2004), and the AlexNet variant of LPIPS (Zhang et al., 2018). | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Compared to SplatAD (Hess et al., 2025), the method closest to ours, we improve PSNR by 0.4-1.7 dB without relying on CNNs for view ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Table 5: Ablations. NVS metrics averaged across PandaSet. | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| We validate the efficacy of our components in Sec. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios. | Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | It outperforms LiDAR-RT (Zhou et al., 2025), which solely targets LiDAR reconstruction, on all metrics except ray drop accuracy (for which LiDAR-RT uses a ... | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / 3 METHOD - extractive body cue:** We then compute an azimuth tile count such that the beam count per tile differs at most by 8 samples (right).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for upsampling (Yang et al., 2023b; Tonderski ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | The choice M = 32, Nε = 16 gives the best LiDAR rendering speed (note that does not affect quality). | p. 10 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 7, SimULi renders the fastest (as measured on an A40 GPU) and compares favorably to camera-LiDAR and LiDAR-only (Zhou et al., 2025) baselines. | p. 9 (4 EXPERIMENTS) |
| We further measure SplatAD (Hess et al., 2025), NeuRAD (Tonderski et al., 2024) and neurad-studio's UniSim (Yang et al., 2023b) implementation as joint camera-LiDAR ... | p. 9 (4 EXPERIMENTS) |
| We encode camera and LiDAR attributes into separate unordered sets Gc and Gl of semi-transparent 3D Gaussian particles (Kerbl et al., 2023). | p. 4 (3 METHOD) |
| We associate 3rd-order spherical harmonics coefficients SHc ↑R48 to camera Gaussians to encode view-dependent color, and SHl ↑R48 to LiDAR Gaussians for view-dependent intensity ... | p. 4 (3 METHOD) |
| We then compute an azimuth tile count such that the beam count per tile differs at most by 8 samples (right). | p. 5 (3 METHOD) |
| We compute the normalized CDF of elevation angles using a predefined histogram bin count and set elevation tiling boundaries at angles where the CDF ... | p. 5 (3 METHOD) |
| We provide pseudo-code in Procedure 1. | p. 6 (3 METHOD) |
| We finally compute the azimuth tile count and the maximum point count per tile constraint M. | p. 6 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for upsampling (Yang et al., 2023b; Tonderski et ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The choice M = 32, Nε = 16 gives the best LiDAR rendering speed (note that does not affect quality).

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), metrics p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), baselines p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), results p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
