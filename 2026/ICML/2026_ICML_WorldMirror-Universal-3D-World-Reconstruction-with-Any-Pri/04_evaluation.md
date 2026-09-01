# Evaluation - WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HFNJOpXHfm; PDF retrieval source: https://openreview.net/pdf/d37648c3826e3031b270765b6a36790ab19140f8.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.4. Ablation Study), p. 15 (Figure/Table caption), p. 17 (Figure/Table caption)): 3 shows substantial improvements over existing methods, demonstrating that multi-task learning with shared representations can outperform specialized single-task approaches.

## Evaluation Body Digest

- **p. 7 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** We evaluate point map reconstruction on scene-level datasets, including 7-Scenes (Shotton et al., 2013), NRGBD (Azinovi´c et al., 2022) and objectlevel dataset DTU (Jensen et ...
- **p. 7 / 5. Experiments - extractive PDF cue:** Results are averaged on 7-Scenes, NRGBD, and DTU datasets.
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** Results are averaged over ETH3D and DTU datasets with 10 views as input. ‘Single token' offers both superior performance and high efficiency.
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** We introduce a multi-resolution benchmark on DL3DV (Ling et al., 2024) following FLARE (Zhang et al., 2025) to fairly compare methods with different input resolutions ...
- **p. 6 / 5. Experiments - extractive PDF cue:** We evaluate WorldMirror on comprehensive tasks: point map reconstruction, camera pose estimation, surface normal 6
- **p. 7 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** 1, our method without priors already surpasses VGGT and π3, with 10.4% and 17.8% accuracy gains on 7-Scenes and DTU.
- **p. 7 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** Following (Bae & Davison, 2024), we evaluate on iBims-1 (Koch et al., 2018), NYUv2 (Silberman et al., 2012), and ScanNet (Dai et al., 2017), reporting ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 13. Ablation study comparing our decoupled training strategy against joint training. Lower is better for all error metrics (↓); higher is better for PSNR ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Evaluation on Different Tasks (p. 7); 5.2. Evaluation on Different Input Configurations (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Evaluation on Different Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3 shows substantial improvements over existing methods, demonstrating that multi-task learning with shared representations can outperform specialized single-task approaches. | p. 8 (5.1. Evaluation on Different Tasks) |
| 5.1. Evaluation on Different Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | Incorporating priors further improves results; using all priors yields 58.1% and 53.1% accuracy gains on 7-Scenes and NRGBD over our no-prior baseline, demonstrating effective ... | p. 7 (5.1. Evaluation on Different Tasks) |
| 5.1. Evaluation on Different Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, our method achieves superior zero-shot performance on RealEstate10K and TUM-dynamics, while remaining competitive on Sintel despite limited outdoor dynamic scenes data involved in ... | p. 7 (5.1. Evaluation on Different Tasks) |
| 5.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our experiments reveal that the single token approach achieves better performance for embedding both camera poses and intrinsics, suggesting that a compact global representation ... | p. 8 (5.4. Ablation Study) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 10. Novel view synthesis results on MatrixCity (Li et al., 2023) using 100, 150, and 200 input views. WorldMirror consistently outperforms prior feed-forward ... | p. 15 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** We evaluate point map reconstruction on scene-level datasets, including 7-Scenes (Shotton et al., 2013), NRGBD (Azinovi´c et al., 2022) and objectlevel dataset DTU (Jensen et ...
- **p. 7 / 5. Experiments - extractive PDF cue:** Results are averaged on 7-Scenes, NRGBD, and DTU datasets.
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** Results are averaged over ETH3D and DTU datasets with 10 views as input. ‘Single token' offers both superior performance and high efficiency.
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** We introduce a multi-resolution benchmark on DL3DV (Ling et al., 2024) following FLARE (Zhang et al., 2025) to fairly compare methods with different input resolutions ...
- **p. 6 / 5. Experiments - extractive PDF cue:** We evaluate WorldMirror on comprehensive tasks: point map reconstruction, camera pose estimation, surface normal 6

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. WorldMirror is a feed-forward 3D reconstruction model that takes images with optional priors (depth, intrinsics, poses) and produces point clouds, 3DGS, cameras, depth, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of WorldMirror. Our framework employs Multi-modal Tokenization to encode all inputs (images, optional priors including intrinsics, camera poses, and depth maps) into ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Feed-Forward 3D Gaussians Predicted by WorldMirror with In-The-Wild Inputs. Besides real photos, our method generalizes well to AI-created videos spanning diverse styles. dropped ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Point map Reconstruction on 7-Scenes, NRGBD, and DTU. We report the performance of WorldMirror under different input configurations. Best and second best results ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Camera Pose Estimation on RealEstate10K, Sintel, and TUM-dynamics. All datasets are excluded from the training set, except that RealEstate10K was included for CUT3R ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Surface Normal Estimation on ScanNet, NYUv2, and iBims-1. We compare with both regression-based and diffusion-based surface normal estimation approaches. Best and second best ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Multi-resolution novel view synthesis evaluation on DL3DV. ∗denotes using the pose-free optimization (Ye et al., 2024a) for fair comparison with non-pose-free baselines (Xu ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative Comparisons of Novel View Synthesis. We compare with FLARE and AnySplat on RealEstate10K and DL3DV. The first four columns correspond to the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate point map reconstruction on scene-level datasets, including 7-Scenes (Shotton et al., 2013), NRGBD (Azinovi´c et al., 2022) and objectlevel dataset DTU (Jensen ... | embodiment, simulator version and control stack | p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5. Experiments) |
| Task/environment | Results are averaged on 7-Scenes, NRGBD, and DTU datasets. | reset, timeout, object/scene variation | p. 7 (5. Experiments), p. 8 (5.1. Evaluation on Different Tasks) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1, our method without priors already surpasses VGGT and π3, with 10.4% and 17.8% accuracy gains on 7-Scenes and DTU. | definition/direction/unit from same section | p. 7 (5.1. Evaluation on Different Tasks) |
| Following (Bae & Davison, 2024), we evaluate on iBims-1 (Koch et al., 2018), NYUv2 (Silberman et al., 2012), and ScanNet (Dai et al., 2017), ... | definition/direction/unit from same section | p. 7 (5.1. Evaluation on Different Tasks) |
| Table 13. Ablation study comparing our decoupled training strategy against joint training. Lower is better for all error metrics (↓); higher is better for ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 14. Sensitivity analysis on the prior dropout probability p. Performance is reported under both no-prior and all-prior inference conditions. Lower is better for ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| We evaluate WorldMirror on comprehensive tasks: point map reconstruction, camera pose estimation, surface normal 6 | definition/direction/unit from same section | p. 6 (5. Experiments) |
| As demonstrated, WorldMirror consistently outperforms both methods across most conditions. | definition/direction/unit from same section | p. 8 (5.3. Comparison with Prior-guided Methods) |
| 6 illustrates how different priors contribute to reconstruction quality, with quantitative results in Sec. | definition/direction/unit from same section | p. 8 (5.2. Evaluation on Different Input Configurations) |
| Table 1. Point map Reconstruction on 7-Scenes, NRGBD, and DTU. We report the performance of WorldMirror under different input configurations. Best and second best ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Incorporating priors further improves results; using all priors yields 58.1% and 53.1% accuracy gains on 7-Scenes and NRGBD over our no-prior baseline, demonstrating effective ... | comparison identity and matched condition | p. 7 (5.1. Evaluation on Different Tasks) |
| As demonstrated, WorldMirror consistently outperforms both methods across most conditions. | comparison identity and matched condition | p. 8 (5.3. Comparison with Prior-guided Methods) |
| Compared to Pow3R, our method employs more multi-view-friendly embedding strategies that better preserve geometric consistency. | comparison identity and matched condition | p. 8 (5.3. Comparison with Prior-guided Methods) |
| Table 4. Multi-resolution novel view synthesis evaluation on DL3DV. ∗denotes using the pose-free optimization (Ye et al., 2024a) for fair comparison with non-pose-free baselines ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 4. Qualitative Comparisons of Novel View Synthesis. We compare with FLARE and AnySplat on RealEstate10K and DL3DV. The first four columns correspond to ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 10. Visual Comparisons on 7-Scenes, NRGBD, and DTU datasets. WorldMirror delivers superior reconstruction fidelity compared to VGGT, effectively capturing spatial relationships within scenes ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 6 reports ablation analysis on novel view synthesis: (1) We replace groundtruth camera parameters with predicted ones for 3DGS rendering to examine their importance. | component/input/data sensitivity | p. 8 (5.4. Ablation Study) |
| Figure 6. Geometric Priors Unlock Enhanced Scene Reconstruction of WorldMirror. (Top) Camera poses help the model to capture relative view positions accurately. (Middle) Calibrated ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| 1, our method without priors already surpasses VGGT and π3, with 10.4% and 17.8% accuracy gains on 7-Scenes and DTU. | component/input/data sensitivity | p. 7 (5.1. Evaluation on Different Tasks) |
| Table 6. Novel View Synthesis Ablation. Best and second best results are highlighted. | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 11. Two-view NVS comparison on RealEstate10K and DL3DV. WorldMirror demonstrates strong generalization ability, even without being trained specifically for the two-view NVS setting. | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Table 13. Ablation study comparing our decoupled training strategy against joint training. Lower is better for all error metrics (↓); higher is better for ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and ... | 3 shows substantial improvements over existing methods, demonstrating that multi-task learning with shared representations can outperform specialized single-task approaches. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.4. Ablation Study), p. 15 (Figure/Table caption), p. 17 (Figure/Table caption) |
| Primary metric/result | Incorporating priors further improves results; using all priors yields 58.1% and 53.1% accuracy gains on 7-Scenes and NRGBD over our no-prior baseline, demonstrating effective ... | numeric claim only at cited anchor | p. 7 (5.1. Evaluation on Different Tasks) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Model Training - extractive PDF cue:** Method Prior Condition Resolution DL3DV (8 Views) DL3DV (24 Views) DL3DV (64 Views) PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 12. Robustness evaluation of WorldMirror with noisy priors on 7-Scenes and DTU datasets. The model exhibits graceful degradation under various noise conditions. Prior ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Trained with dynamic resolutions, our model generalizes robustly across varying resolutions and consistently surpasses baselines. | p. 8 (5.1. Evaluation on Different Tasks) |
| body limitation/failure cue | Figure 11. Visual Comparisons of In-The-Wild Multi-View 3D Reconstruction. WorldMirror delivers superior reconstruction fidelity with in-the-wild images as input, generating more plausible results in ... | p. 23 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This enables flexible control over input modalities at inference time. | p. 4 (3.1. Multi-modal Tokenization) |
| 3.1), which encodes diverse input modalities, including camera intrinsics, poses, and depth maps, into a unified token sequence; and (2) Unified Spatial Prediction (Sec. | p. 3 (3. Method) |
| Additionally, Fi is processed by an MLP decoder to estimate camera parameters ˆEi. | p. 4 (3.2. Unified Spatial Prediction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 12. Robustness evaluation of WorldMirror with noisy priors on 7-Scenes and DTU datasets. The model exhibits graceful degradation under various noise conditions. Prior Type ...
- **p. 8 / 5.1. Evaluation on Different Tasks - extractive PDF cue:** Trained with dynamic resolutions, our model generalizes robustly across varying resolutions and consistently surpasses baselines.
- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 11. Visual Comparisons of In-The-Wild Multi-View 3D Reconstruction. WorldMirror delivers superior reconstruction fidelity with in-the-wild images as input, generating more plausible results in challenging ...

- **PDF anchors reviewed:** datasets p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5. Experiments), p. 8 (5.1. Evaluation on Different Tasks), p. 8 (5.1. Evaluation on Different Tasks), p. 6 (5. Experiments), metrics p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 17 (Figure/Table caption), p. 17 (Figure/Table caption), p. 6 (5. Experiments), p. 8 (5.3. Comparison with Prior-guided Methods), baselines p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.3. Comparison with Prior-guided Methods), p. 8 (5.3. Comparison with Prior-guided Methods), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 22 (Figure/Table caption), results p. 8 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 8 (5.4. Ablation Study), p. 15 (Figure/Table caption), p. 17 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
