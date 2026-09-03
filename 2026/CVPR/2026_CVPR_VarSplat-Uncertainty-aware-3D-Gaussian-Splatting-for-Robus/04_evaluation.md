# Evaluation - VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies)): VarSplat achieves the highest accuracy with robustness on large motion camera.

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** In this section, we evaluate VarSplat against existing baselines on both synthetic and real-world datasets.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves competitive results on both synthetic and real-world datasets.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For fair comparison on ScanNet with common baselines [15, 45, 48], we report results on six scenes.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Rendering performance on 3 datasets.
- **p. 8 / 4.3. Ablation studies - extractive body cue:** Uncertainty ablation on ScanNet (scene0181).
- **p. 8 / 4.3. Ablation studies - extractive body cue:** Visualization of challenging conditions (scene0169 ScanNet).
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves the highest accuracy with robustness on large motion camera.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We compute L1 on rendered depth and the F1 score against ground truth mesh vertices as in [51, 52].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Quantitative Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Quantitative Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | VarSplat achieves the highest accuracy with robustness on large motion camera. | p. 6 (4.2. Quantitative Evaluation) |
| 4.2. Quantitative Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | On ScanNet, VarSplat consistently achieves best performance against both neural implicit and 3DGS baselines. | p. 6 (4.2. Quantitative Evaluation) |
| 4.2. Quantitative Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | VarSplat achieves competitive results on both synthetic and real-world datasets. | p. 7 (4.2. Quantitative Evaluation) |
| 4.3. Ablation studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Learning and rendering variance raises computation cost, with corresponding improvements in tracking performance. | p. 8 (4.3. Ablation studies) |
| 4.2. Quantitative Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | VarSplat achieves the best overall, showing robustness to noisy indoor scenes. | p. 7 (4.2. Quantitative Evaluation) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** In this section, we evaluate VarSplat against existing baselines on both synthetic and real-world datasets.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves competitive results on both synthetic and real-world datasets.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For fair comparison on ScanNet with common baselines [15, 45, 48], we report results on six scenes.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Rendering performance on 3 datasets.
- **p. 8 / 4.3. Ablation studies - extractive body cue:** Uncertainty ablation on ScanNet (scene0181).
- **p. 8 / 4.3. Ablation studies - extractive body cue:** Visualization of challenging conditions (scene0169 ScanNet).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. VarSplat. Given RGB-D inputs, each 3D Gaussian jointly learns position, orientation, scale, color, opacity, and appearance variance σ2. During mapping, σ2 is optimized ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. VarSplat architecture. During mapping, each 3D Gaussian jointly learns position, appearance, and variance σ2. The per-splat variances are composited into per-pixel uncertainty V ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Tracking Performance on Replica [33] (ATE RMSE ↓ [cm]). UC indicates uncertainty. The results are highlighted as best , second and third . ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Tracking Performance on ScanNet++ (ATE RMSE ↓ [cm]). VarSplat achieves the highest accuracy with robustness on large motion camera.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Tracking Performance on TUM-RGBD (ATE RMSE ↓ [cm]). UC indicates uncertainty. VarSplat outperforms both 3DGS and NeRF baselines. *Photo-SLAM [11] use ORB-SLAM3 fea- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Tracking Performance on ScanNet. UC indicates uncer- tainty. VarSplat achieves the best overall, showing robustness to noisy indoor scenes.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Reconstruction Performance on Replica. VarSplat achieve third-best result after Loopy-SLAM and LoopSplat, show- ing that variance regularization preserves mesh quality.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Rendering performance on 3 datasets. VarSplat achieves competitive results on both synthetic and real-world datasets. Gray indicates evaluation on submaps rather than global ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this section, we evaluate VarSplat against existing baselines on both synthetic and real-world datasets. | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 7 (4.2. Quantitative Evaluation) |
| Task/environment | VarSplat achieves competitive results on both synthetic and real-world datasets. | reset, timeout, object/scene variation | p. 7 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 3 (3. Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.2. Mapping), p. 4 (3.2. Mapping) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| VarSplat achieves the highest accuracy with robustness on large motion camera. | definition/direction/unit from same section | p. 6 (4.2. Quantitative Evaluation) |
| We compute L1 on rendered depth and the F1 score against ground truth mesh vertices as in [51, 52]. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| These results also show that using the per-pixel uncertainty map to regularize the photometric loss does not degrade mesh reconstruction quality. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Evaluation) |
| Learning and rendering variance raises computation cost, with corresponding improvements in tracking performance. | definition/direction/unit from same section | p. 8 (4.3. Ablation studies) |
| With depth, uncertainty focuses on textureless areas with depth holes and stays low on well constrained surfaces, avoiding overconfidence on glossy areas. | definition/direction/unit from same section | p. 8 (4.3. Ablation studies) |
| Figure 2. VarSplat architecture. During mapping, each 3D Gaussian jointly learns position, appearance, and variance σ2. The per-splat variances are composited into per-pixel uncertainty ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1. VarSplat. Given RGB-D inputs, each 3D Gaussian jointly learns position, orientation, scale, color, opacity, and appearance variance σ2. During mapping, σ2 is ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Rendering performance on 3 datasets. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| VarSplat outperforms both 3DGS and NeRF baselines. *Photo-SLAM [11] use ORB-SLAM3 features [2] for tracking and loop closure. | comparison identity and matched condition | p. 6 (4.2. Quantitative Evaluation) |
| For fair comparison on ScanNet with common baselines [15, 45, 48], we report results on six scenes. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| We conduct all ablation studies on six ScanNet scenes. | comparison identity and matched condition | p. 7 (4.3. Ablation studies) |
| Without it, pose estimation on noisy regions can cause jitter and long-range drifts. | comparison identity and matched condition | p. 7 (4.3. Ablation studies) |
| Uncertainty ablation on ScanNet (scene0181). | comparison identity and matched condition | p. 8 (4.3. Ablation studies) |
| Per-pixel uncertainty with vs. without depth on TUMRGBD (fr1/desk2). | comparison identity and matched condition | p. 8 (4.3. Ablation studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3. Uncertainty ablation on ScanNet (scene0181). Without uncertainty, tracking jitters, loop detection has long-range drift, and registration ghosts submaps. With VarSplat enabled, the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Effect of uncertainty on pose estimation. | component/input/data sensitivity | p. 7 (4.2. Quantitative Evaluation) |
| 90.4), indicating tighter alignment without surface inflation. | component/input/data sensitivity | p. 6 (4.2. Quantitative Evaluation) |
| Moreover, we conduct ablation studies of the proposed uncertainty model, measuring its impact on tracking, registration, and loop detection. | component/input/data sensitivity | p. 6 (4. Experiments) |
| We conduct all ablation studies on six ScanNet scenes. | component/input/data sensitivity | p. 7 (4.3. Ablation studies) |
| Per-pixel uncertainty with vs. without depth on TUMRGBD (fr1/desk2). | component/input/data sensitivity | p. 8 (4.3. Ablation studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to ... | VarSplat achieves the highest accuracy with robustness on large motion camera. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies) |
| Primary metric/result | On ScanNet, VarSplat consistently achieves best performance against both neural implicit and 3DGS baselines. | numeric claim only at cited anchor | p. 6 (4.2. Quantitative Evaluation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** Neural Implicit Fields NICE-SLAM [52] ✗ 0.97 1.31 1.07 0.88 1.00 1.06 1.10 1.13 1.06 ESLAM [14] ✗ 0.71 0.70 0.52 0.57 0.55 0.58 0.72 ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Neural Implicit Fields Co-SLAM [38] ✗ 7.1 11.1 9.4 5.9 11.8 7.1 8.7 NICE-SLAM [52] ✗ 12.0 14.0 7.9 10.9 13.4 6.2 10.7 ESLAM [14] ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Dataset Replica [33] TUM [35] ScanNet [4] Method PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** Method Mapping Mapping Tracking Tracking ATE /fr(s) /iter(ms) /fr(s) /iter(ms) RMSE NICE-SLAM [52] 5.8 90.6 8.1 20.8 0.97 Point-SLAM [28] 28.7 93.1 7.1 29.0 0.61 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and future works are provided in Supplementary Material. | p. 8 (5. Conclusion) |
| body limitation/failure cue | These results also show that using the per-pixel uncertainty map to regularize the photometric loss does not degrade mesh reconstruction quality. | p. 7 (4.2. Quantitative Evaluation) |
| body limitation/failure cue | Across four datasets, this integration achieves robust and competitive-to-superior performance. | p. 8 (5. Conclusion) |
| body limitation/failure cue | On ScanNet++, VarSplat improves ATE RMSE by about 18% over the second best method and ensures robustness in long sequences where others like SplaTAM ... | p. 6 (4.2. Quantitative Evaluation) |
| body limitation/failure cue | Figure 1. VarSplat. Given RGB-D inputs, each 3D Gaussian jointly learns position, orientation, scale, color, opacity, and appearance variance σ2. During mapping, σ2 is ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | VarSplat achieves the highest accuracy with robustness on large motion camera. | p. 6 (4.2. Quantitative Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Perframe runtime is computed as total optimization time divided by the sequence length. | p. 7 (4.2. Quantitative Evaluation) |
| Implementation details and additional results are provided in the Supplementary Material. | p. 6 (4. Experiments) |
| We compute L1 on rendered depth and the F1 score against ground truth mesh vertices as in [51, 52]. | p. 6 (4.1. Experimental Setup) |
| Runtime on Replica/Room0 using A100 80GB. | p. 7 (4.2. Quantitative Evaluation) |
| As shown in Table 10, VarSplat achieve competitive runtime with recent 3DGS-SLAM systems. | p. 8 (4.3. Ablation studies) |
| (5) Therefore, we can obtain expected per-splat variance and color by alpha blending, similar to how we compute perpixel color in Eq. | p. 3 (3.1. Per-pixel uncertainty rendering) |
| The variance of splats Var  E[X/Z]  is then computed using second moment of a distribution and Eq. | p. 4 (3.1. Per-pixel uncertainty rendering) |
| The first keyframe seeds Gaussians by backprojecting depth points, and subsequent frames expand coverage by adding Gaussians in unobserved regions or merging overlapping ones. | p. 4 (3.2. Mapping) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations and future works are provided in Supplementary Material.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** These results also show that using the per-pixel uncertainty map to regularize the photometric loss does not degrade mesh reconstruction quality.
- **p. 8 / 5. Conclusion - extractive body cue:** Across four datasets, this integration achieves robust and competitive-to-superior performance.
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** On ScanNet++, VarSplat improves ATE RMSE by about 18% over the second best method and ensures robustness in long sequences where others like SplaTAM fail ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. VarSplat. Given RGB-D inputs, each 3D Gaussian jointly learns position, orientation, scale, color, opacity, and appearance variance σ2. During mapping, σ2 is optimized ...
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** VarSplat achieves the highest accuracy with robustness on large motion camera.

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments), p. 7 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies), p. 8 (4.3. Ablation studies), metrics p. 6 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies), p. 8 (4.3. Ablation studies), p. 4 (Figure/Table caption), baselines p. 6 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Ablation studies), p. 7 (4.3. Ablation studies), p. 8 (4.3. Ablation studies), p. 8 (4.3. Ablation studies), results p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies), p. 7 (4.2. Quantitative Evaluation), p. 8 (4.3. Ablation studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
