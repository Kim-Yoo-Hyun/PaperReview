# Evaluation - Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=bjtuHOb3vN; PDF retrieval source: https://openreview.net/pdf/8310d4c5a6346eaadb420914138e1711121a0ff8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 6 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study)): Rh-3DGS achieves the best results on both tables.

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We evaluate Rh-3DGS on three benchmarks: (i) LERF (Kerr et al., 2023), multi-view scenes with maskbased open-vocabulary queries; (ii) 3D-OVS (Liu et al., 2023), a ...
- **p. 6 / 5. Experiments - extractive body cue:** We first describe the experimental setup, including datasets, baselines, and evaluation metrics.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Quantitative mIoU(%) and mBIoU(%) results on the LERF dataset.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Quantitative PSNR, SSIM and LPIPS results on the LERF dataset.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** We benchmark inference rendering (RGB + semantic) on LERF figurines at 1280 × 720 on an RTX 4090.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** Lpix provides the main gain, Lmean alone is beneficial but smaller, and the full VFM objective performs best.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For ScanNet, we report mIoU and mAcc (mean per-class accuracy).
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For LERF and 3D-OVS, we report mIoU and mBIoU (IoU computed on boundary bands around contours).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.2. Quantitative Results (p. 6); 5.3. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Rh-3DGS achieves the best results on both tables. | p. 6 (5.2. Quantitative Results) |
| 5.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Rh-3DGS again achieves the best performance. | p. 7 (5.2. Quantitative Results) |
| 5.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Rh-3DGS achieves the best results across all splits. | p. 7 (5.2. Quantitative Results) |
| 5.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The full model (VCD+VFM+LIC) achieves the best performance (81.62 mIoU, 58.11 mBIoU). | p. 8 (5.4. Ablation Study) |
| 5.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also observe consistent improvements in rendering metrics. | p. 6 (5.2. Quantitative Results) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We evaluate Rh-3DGS on three benchmarks: (i) LERF (Kerr et al., 2023), multi-view scenes with maskbased open-vocabulary queries; (ii) 3D-OVS (Liu et al., 2023), a ...
- **p. 6 / 5. Experiments - extractive body cue:** We first describe the experimental setup, including datasets, baselines, and evaluation metrics.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Quantitative mIoU(%) and mBIoU(%) results on the LERF dataset.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Quantitative PSNR, SSIM and LPIPS results on the LERF dataset.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** We benchmark inference rendering (RGB + semantic) on LERF figurines at 1280 × 720 on an RTX 4090.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** Lpix provides the main gain, Lmean alone is beneficial but smaller, and the full VFM objective performs best.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Motivation on LERF (teatime, "bag of cookies"). Baseline 3DGS produces boundary bleeding and multi-view in- consistent masks under occlusion and mixed-depth rays (b-c). ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Empirical evidence of the Euclidean-hyperspherical mismatch on the baseline model. Region Pre-norm ∥s∥2 Ang. dev. All 0.957 16.16
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative mIoU(%) and mBIoU(%) results on the LERF dataset.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Quantitative PSNR, SSIM and LPIPS results on the LERF
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Quantitative mIoU(%) and mBIoU(%) results on the 3D- OVS dataset.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Quantitative mIoU(%) and mAcc(%) results on the Scan- Net dataset.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Ablation on LERF (figurines). Cfg (VCD/VFM/LIC) mIoU mBIoU FPS Mem.(GB) ✗✗✗ 60.56

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate Rh-3DGS on three benchmarks: (i) LERF (Kerr et al., 2023), multi-view scenes with maskbased open-vocabulary queries; (ii) 3D-OVS (Liu et al., 2023), ... | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Task/environment | We first describe the experimental setup, including datasets, baselines, and evaluation metrics. | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 7 (5.2. Quantitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For ScanNet, we report mIoU and mAcc (mean per-class accuracy). | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| For LERF and 3D-OVS, we report mIoU and mBIoU (IoU computed on boundary bands around contours). | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Figure 3. Open-vocabulary inference and evaluation with Rh-3DGS. Given a text prompt, we compute pixel-wise similarity between the CLIP text embedding and the rendered ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Rh-3DGS again achieves the best performance. | definition/direction/unit from same section | p. 7 (5.2. Quantitative Results) |
| The full model (VCD+VFM+LIC) achieves the best performance (81.62 mIoU, 58.11 mBIoU). | definition/direction/unit from same section | p. 8 (5.4. Ablation Study) |
| This shows that VCD persistently suppresses unreliable supervision near occlusion and mixed-depth regions, rather than only becoming calibrated after convergence. | definition/direction/unit from same section | p. 8 (5.4. Ablation Study) |
| Figure 7. Scene editing with the learned 3D semantic field. We show the original renderings, the localized semantic region, and the edited renderings from ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 8. Sensitivity to loss weights on LERF (figurines). We sweep λVFM and λLIC and report mIoU. The best region is around our default ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared with the strongest baseline, Rh-3DGS improves mIoU from 76.07 to 82.07 and mBIoU from 55.45 to 67.66. | comparison identity and matched condition | p. 6 (5.2. Quantitative Results) |
| Compared to the baseline (328.59 FPS, 2.65 GB), all components add only 8.2% FPS drop and 0.58 GB memory, while improving mIoU by +21.06 ... | comparison identity and matched condition | p. 8 (5.4. Ablation Study) |
| We first describe the experimental setup, including datasets, baselines, and evaluation metrics. | comparison identity and matched condition | p. 6 (5. Experiments) |
| Baseline methods often produce boundary bleeding and scattered activations. | comparison identity and matched condition | p. 7 (5.3. Qualitative Results) |
| VCD alone improves the baseline (65.37 vs. | comparison identity and matched condition | p. 8 (5.4. Ablation Study) |
| Figure 1. Motivation on LERF (teatime, "bag of cookies"). Baseline 3DGS produces boundary bleeding and multi-view in- consistent masks under occlusion and mixed-depth rays ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 8. Sensitivity to loss weights on LERF (figurines). We sweep λVFM and λLIC and report mIoU. The best region is around our default ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Figure 7. Scene editing with the learned 3D semantic field. We show the original renderings, the localized semantic region, and the edited renderings from ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Finally, we conduct ablation studies to analyze the impact of each component. | component/input/data sensitivity | p. 6 (5. Experiments) |
| All variants use the same training schedule, teacher, resolution, and evaluation protocol. | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |
| Table 10. Ablation of VCD weight components on LERF (figurines). Wop Wedge Wvar mIoU ↑ ✓ ✓ ✓ | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| We ablate each component on LERF (figurines). | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose Visibility-Calibrated Distillation (VCD). | Rh-3DGS achieves the best results on both tables. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 6 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study) |
| Primary metric/result | Rh-3DGS again achieves the best performance. | numeric claim only at cited anchor | p. 7 (5.2. Quantitative Results) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We implement all methods in PyTorch and train on a single NVIDIA GeForce RTX 4090 GPU.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** 6, the full model runs at 301.64 FPS with 3.23 GB peak memory.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** Compared to the baseline (328.59 FPS, 2.65 GB), all components add only 8.2% FPS drop and 0.58 GB memory, while improving mIoU by +21.06 and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Future work will extend to dynamic scenes, multi-teacher distillation, and more efficient implementations. | p. 9 (6. Conclusion) |
| body limitation/failure cue | 9, activating LIC from the beginning is less effective because pseudoinstances are unstable in the early stage. | p. 8 (5.4. Ablation Study) |
| body limitation/failure cue | We present Rh-3DGS for robust open-vocabulary 3D semantics in 3D Gaussian Splatting. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Rh-3DGS localizes semantic regions with clean boundaries under clutter and occlusion. sions and mixed-depth rays. | p. 9 (6. Conclusion) |
| body limitation/failure cue | Rh-3DGS gest that our semantic training does not hurt radiance-field reconstruction. | p. 7 (5.2. Quantitative Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Full hyperparameters and schedules are deferred to App. | p. 6 (5.1. Experimental Setup) |
| We implement all methods in PyTorch and train on a single NVIDIA GeForce RTX 4090 GPU. | p. 6 (5.1. Experimental Setup) |
| Implementation note: we keep the rasterizer unchanged; hyperspherical geometry is used only in the distillation objective. | p. 3 (4.1. Problem Formulation and Notation) |
| We compute the expected depth ¯Dv,u = D(1) v,u Av,u+ϵ and ray variance Varv,u =  D(2) v,u Av,u+ϵ -¯D2 v,u  +, used ... | p. 3 (4.1. Problem Formulation and Notation) |
| We attach a semantic latent to each Gaussian and use a lightweight decoder to map it to the teacher space (D ≫d) during rendering. | p. 4 (4.2. Overview) |
| Rh-3DGS addresses it with three modules: (1) VCD computes a stop-gradient pixel reliability weight wv(u) from rasterization statistics (e.g., accumulated opacity and depth moments) ... | p. 4 (4.2. Overview) |
| Implementation details are provided in App. | p. 5 (4.3. Visibility-Calibrated Distillation (VCD)) |
| We compute view-wise robust Fr´echet means for teacher and rendered features, µt v = arg minµ P u ¯wv,uρδ(d(˜zv,u, µ)) and µs v = ... | p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a ...
- **p. 9 / 6. Conclusion - extractive body cue:** Future work will extend to dynamic scenes, multi-teacher distillation, and more efficient implementations.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** 9, activating LIC from the beginning is less effective because pseudoinstances are unstable in the early stage.
- **p. 8 / 6. Conclusion - extractive body cue:** We present Rh-3DGS for robust open-vocabulary 3D semantics in 3D Gaussian Splatting.
- **p. 9 / 6. Conclusion - extractive body cue:** Rh-3DGS localizes semantic regions with clean boundaries under clutter and occlusion. sions and mixed-depth rays.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Rh-3DGS gest that our semantic training does not hurt radiance-field reconstruction.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments), p. 7 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), metrics p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 9 (Figure/Table caption), p. 7 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), baselines p. 6 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 6 (5. Experiments), p. 7 (5.3. Qualitative Results), p. 8 (5.4. Ablation Study), p. 1 (Figure/Table caption), results p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 6 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
