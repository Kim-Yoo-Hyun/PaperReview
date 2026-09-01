# Evaluation - RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation), p. 8 (4.4. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (4.3. Occupancy State Estimation)): With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in SSIM score.

## Evaluation Body Digest

- **p. 6 / 4.3. Occupancy State Estimation - extractive PDF cue:** Image synthesis and geometry reconstruction evaluation on Boreas dataset [7].
- **p. 6 / 4.3. Occupancy State Estimation - extractive PDF cue:** Two snowy scenes are excluded from geometry evaluation due to LiDAR inaccuracy.
- **p. 8 / 4.5. Adverse Weather and Lighting Conditions - extractive PDF cue:** In the rain and night scenes, the camera is either blurred due to raindrops or has limited visibility due to low illumination.
- **p. 7 / 4.4. Ablation Studies - extractive PDF cue:** Ablation studies on scene reconstruction.
- **p. 7 / 4.4. Ablation Studies - extractive PDF cue:** Scene Reconstruction RMSE↓ R-CD↓ Acc.↑ Init Occ.
- **p. 8 / 4.5. Adverse Weather and Lighting Conditions - extractive PDF cue:** In the snow scene, the LiDAR point cloud exhibits significant artifacts caused by snowfall.
- **p. 6 / 4.3. Occupancy State Estimation - extractive PDF cue:** To assess the quality of occupancy estimation, we report the RMSE, Relative Chamfer Distance (R-CD), and Accuracy.
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** Also, the occupancy map supervision improves 3× RadarSplat reconstruction accuracy.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Novel Radar View Rendering | SYSTEM / EVALUATION SCOPE UNRESOLVED | With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in ... | p. 6 (4.2. Novel Radar View Rendering) |
| 4.3. Occupancy State Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | The results indicate that RadarSplat achieves accurate 3D reconstruction similar to LiDAR, by taking only 2D noisy radar images as input. | p. 7 (4.3. Occupancy State Estimation) |
| 4.3. Occupancy State Estimation | SYSTEM / EVALUATION SCOPE UNRESOLVED | The proposed method outperforms Radar Fields across all metrics, achieving better reconstruction by reducing RMSE by 1.22 m and improving accuracy more than 1.5× ... | p. 7 (4.3. Occupancy State Estimation) |
| 4.4. Ablation Studies | SYSTEM / EVALUATION SCOPE UNRESOLVED | Also, the occupancy map supervision improves 3× RadarSplat reconstruction accuracy. | p. 8 (4.4. Ablation Studies) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. RadarSplat enables radar 2D-to-3D scene reconstruction, image synthesis, and occupancy estimation. RadarSplat outperforms the state-of-the-art neural rendering method [5] both qualitatively and ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.3. Occupancy State Estimation - extractive PDF cue:** Image synthesis and geometry reconstruction evaluation on Boreas dataset [7].
- **p. 6 / 4.3. Occupancy State Estimation - extractive PDF cue:** Two snowy scenes are excluded from geometry evaluation due to LiDAR inaccuracy.
- **p. 8 / 4.5. Adverse Weather and Lighting Conditions - extractive PDF cue:** In the rain and night scenes, the camera is either blurred due to raindrops or has limited visibility due to low illumination.
- **p. 7 / 4.4. Ablation Studies - extractive PDF cue:** Ablation studies on scene reconstruction.
- **p. 7 / 4.4. Ablation Studies - extractive PDF cue:** Scene Reconstruction RMSE↓ R-CD↓ Acc.↑ Init Occ.
- **p. 8 / 4.5. Adverse Weather and Lighting Conditions - extractive PDF cue:** In the snow scene, the LiDAR point cloud exhibits significant artifacts caused by snowfall.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. RadarSplat enables radar 2D-to-3D scene reconstruction, image synthesis, and occupancy estimation. RadarSplat outperforms the state-of-the-art neural rendering method [5] both qualitatively and quantitatively ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. System Overview. RadarSplat takes radar images and poses as input. The preprocessing step includes noise detection and initial occupancy mapping. The multipath source ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Three types of radar noise of scanning radar highlighted in a raw radar image in polar space (bottom) and Cartesian space (top). The ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Range-power signal and its FFT of a radar azimuth beam with multipath effects. The constant and peak magnitude in the FFT results are ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Multipath modeling and denoising. The multipath effect is modeled by peak frequency and source power reflection and attenu- ation. The denoising method removes ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used in ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Modeling spectral leakage in the radar-power signal. (a) Ideal range FFT. (b) Practical range FFT with spectral leakage. (c) Practical range FFT sharpened ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Image synthesis and geometry reconstruction evaluation on Boreas dataset [7]. Image synthesis is evaluated from unseen views, and geometry reconstruction is evaluated against ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Image synthesis and geometry reconstruction evaluation on Boreas dataset [7]. | embodiment, simulator version and control stack | p. 6 (4.3. Occupancy State Estimation), p. 6 (4.3. Occupancy State Estimation) |
| Task/environment | Two snowy scenes are excluded from geometry evaluation due to LiDAR inaccuracy. | reset, timeout, object/scene variation | p. 6 (4.3. Occupancy State Estimation), p. 8 (4.5. Adverse Weather and Lighting Conditions) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.6. Training Losses), p. 6 (3.5.2. Rendering with Azimuth Projection) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Multipath and Saturation Noise Detection), p. 4 (3.2. Multipath and Saturation Noise Detection) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To assess the quality of occupancy estimation, we report the RMSE, Relative Chamfer Distance (R-CD), and Accuracy. | definition/direction/unit from same section | p. 6 (4.3. Occupancy State Estimation) |
| Also, the occupancy map supervision improves 3× RadarSplat reconstruction accuracy. | definition/direction/unit from same section | p. 8 (4.4. Ablation Studies) |
| Accuracy is computed using a 0.5 m threshold. | definition/direction/unit from same section | p. 6 (4.3. Occupancy State Estimation) |
| The proposed method outperforms Radar Fields across all metrics, achieving better reconstruction by reducing RMSE by 1.22 m and improving accuracy more than 1.5× ... | definition/direction/unit from same section | p. 7 (4.3. Occupancy State Estimation) |
| A 0.5 probability threshold is then applied to the output of both RadarSplat and Radar Fields to generate the final occupancy map for evaluation. | definition/direction/unit from same section | p. 7 (4.3. Occupancy State Estimation) |
| To further demonstrate the robustness of RadarSplat under various weather conditions, Figure 13 illustrates novel view rendering and occupancy maps in snow, rain, and ... | definition/direction/unit from same section | p. 8 (4.5. Adverse Weather and Lighting Conditions) |
| Figure 5. Multipath modeling and denoising. The multipath effect is modeled by peak frequency and source power reflection and attenu- ation. The denoising method ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 3. Three types of radar noise of scanning radar highlighted in a raw radar image in polar space (bottom) and Cartesian space (top). ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in ... | comparison identity and matched condition | p. 6 (4.2. Novel Radar View Rendering) |
| Our method better synthesizes multipath and noise effects compared to the baseline. | comparison identity and matched condition | p. 7 (4.3. Occupancy State Estimation) |
| Our method provides clear and noise-free occupancy estimation compared to the baseline. radar noise in challenging conditions. | comparison identity and matched condition | p. 7 (4.3. Occupancy State Estimation) |
| Figure 1. RadarSplat enables radar 2D-to-3D scene reconstruction, image synthesis, and occupancy estimation. RadarSplat outperforms the state-of-the-art neural rendering method [5] both qualitatively and ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Ablation studies on image synthesis. | comparison identity and matched condition | p. 8 (4.4. Ablation Studies) |
| In this study, we compare with results with and without spectral leakage modeling (Sec. | comparison identity and matched condition | p. 8 (4.4. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 12. Ablation studies on image synthesis. RadarSplat fails to model multipath effects when disabling the proposed multipath modeling. Radar- Splat also fails to ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 5. Multipath modeling and denoising. The multipath effect is modeled by peak frequency and source power reflection and attenu- ation. The denoising method ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 3. Ablation studies on scene reconstruction. 27602 | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To account for radar noise, we propose a noise detection method (Sec. | With the correct noise modeling and rendering, our proposed method outperforms state-of-the-art, Radar Fields, by +3.4 PSNR and achieves more than 2.6× better in ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation), p. 8 (4.4. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (4.3. Occupancy State Estimation) |
| Primary metric/result | The results indicate that RadarSplat achieves accurate 3D reconstruction similar to LiDAR, by taking only 2D noisy radar images as input. | numeric claim only at cited anchor | p. 7 (4.3. Occupancy State Estimation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Following [5], we select every 5 frames as the test frame to create a traintest split.
- **p. 6 / 4.2. Novel Radar View Rendering - extractive PDF cue:** The radar image rendering speed reaches 4.5 FPS on an NVIDIA A6000 GPU.
- **p. 4 / 3.2. Multipath and Saturation Noise Detection - extractive PDF cue:** First, we apply FFT to all azimuth beams: X[k] = F{x[n]} = N-1 X n=0 x[n]e-j 2π N kn, (2) where x[n] represents the range-power ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation. | p. 6 (4.2. Novel Radar View Rendering) |
| body limitation/failure cue | RadarSplat also fails to model other noises when disabling the proposed noise probability. reconstruction. | p. 8 (4.4. Ablation Studies) |
| body limitation/failure cue | This enables radar inverse rendering for radar signal decomposition, high-fidelity radar data synthesis, and robust noise-free occupancy prediction. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Three types of radar noise of scanning radar highlighted in a raw radar image in polar space (bottom) and Cartesian space (top). ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. System Overview. RadarSplat takes radar images and poses as input. The preprocessing step includes noise detection and initial occupancy mapping. The multipath ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Accuracy is computed using a 0.5 m threshold. | p. 6 (4.3. Occupancy State Estimation) |
| The radar image rendering speed reaches 4.5 FPS on an NVIDIA A6000 GPU. | p. 6 (4.2. Novel Radar View Rendering) |
| For the Radar Fields occupancy estimation, we follow the original implementation, integrating occupancy along the elevation axis. | p. 7 (4.3. Occupancy State Estimation) |
| The denoising process is illustrated in Figure 5, with the pseudo-code provided in the supplementary material. | p. 5 (3.4. Denoising and Occupancy Map Pre-processing) |
| Instead, we compute the power return ratio, σi, by considering an additional noise probability term, ηi: σi = ρi · min(αi + ηi, 1) ... | p. 5 (3.5. Radar Gaussian Splatting) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Novel Radar View Rendering - extractive PDF cue:** In contrast, Radar Fields fails to model the noise, resulting in noticeable performance degradation.
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** RadarSplat also fails to model other noises when disabling the proposed noise probability. reconstruction.
- **p. 8 / 5. Conclusion - extractive PDF cue:** This enables radar inverse rendering for radar signal decomposition, high-fidelity radar data synthesis, and robust noise-free occupancy prediction.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Our proposed radar image denoising method preserves rich information while remaining robust to multipath effects. In contrast, the dynamic threshold approach used in ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Three types of radar noise of scanning radar highlighted in a raw radar image in polar space (bottom) and Cartesian space (top). The ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. System Overview. RadarSplat takes radar images and poses as input. The preprocessing step includes noise detection and initial occupancy mapping. The multipath source ...

- **PDF anchors reviewed:** datasets p. 6 (4.3. Occupancy State Estimation), p. 6 (4.3. Occupancy State Estimation), p. 8 (4.5. Adverse Weather and Lighting Conditions), p. 7 (4.4. Ablation Studies), p. 7 (4.4. Ablation Studies), p. 8 (4.5. Adverse Weather and Lighting Conditions), metrics p. 6 (4.3. Occupancy State Estimation), p. 8 (4.4. Ablation Studies), p. 6 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation), p. 8 (4.5. Adverse Weather and Lighting Conditions), baselines p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation), p. 1 (Figure/Table caption), p. 8 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies), results p. 6 (4.2. Novel Radar View Rendering), p. 7 (4.3. Occupancy State Estimation), p. 7 (4.3. Occupancy State Estimation), p. 8 (4.4. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (4.3. Occupancy State Estimation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
