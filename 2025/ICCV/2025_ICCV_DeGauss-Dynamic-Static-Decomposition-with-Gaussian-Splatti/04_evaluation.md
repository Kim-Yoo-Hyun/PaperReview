# Evaluation - DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.3. Results), p. 6 (4.3. Results)): Notably, our method consistently achieves significantly better LPIPS scores over the previous SOTA method SpotlessSplats [24].

## Evaluation Body Digest

- **p. 5 / 4.2. Datasets - extractive PDF cue:** HyperNeRF Dataset [21] features real-world activities captured with smooth trajectories.
- **p. 7 / 4.3. Results - extractive PDF cue:** Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene metrics ...
- **p. 6 / 4.3. Results - extractive PDF cue:** Distractor free scene reconstruction on NeRF On-the-go Dataset[22].The best , second best , and third best are highlighted. ‡: ±0.005 SSIM and LPIPS due to ...
- **p. 5 / 4.2. Datasets - extractive PDF cue:** Therefore, we focus primarily on qualitative visualizations for this dataset.
- **p. 7 / 4.3. Results - extractive PDF cue:** Comparison dynamic modeling on Neu3D Dataset [13].
- **p. 8 / 4.3. Results - extractive PDF cue:** Qualitative comparison with 4DGS [36] on the Neu3D [13] dataset.
- **p. 6 / 4.3. Results - extractive PDF cue:** Qualitative comparison of baseline methods [10, 24, 31] for distractor-free scene reconstruction on the Aria and EPIC-Field sequences.
- **p. 7 / 4.3. Results - extractive PDF cue:** 2, where our methods achieve consistently better LPIPS scores.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Implementation Details (p. 5); 4.2. Datasets (p. 5); 4.3. Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, our method consistently achieves significantly better LPIPS scores over the previous SOTA method SpotlessSplats [24]. | p. 7 (4.3. Results) |
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, where our methods achieve consistently better LPIPS scores. | p. 7 (4.3. Results) |
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | To assess the performance of our method for the distractorfree scene reconstruction task in the presence of noisy inputs, we conduct evaluations on both ... | p. 5 (4.3. Results) |
| 4.3. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method shows generally superior performance over state-of-the-art methods. | p. 6 (4.3. Results) |

## Dataset / Benchmark Role

- **p. 5 / 4.2. Datasets - extractive PDF cue:** HyperNeRF Dataset [21] features real-world activities captured with smooth trajectories.
- **p. 7 / 4.3. Results - extractive PDF cue:** Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene metrics ...
- **p. 6 / 4.3. Results - extractive PDF cue:** Distractor free scene reconstruction on NeRF On-the-go Dataset[22].The best , second best , and third best are highlighted. ‡: ±0.005 SSIM and LPIPS due to ...
- **p. 5 / 4.2. Datasets - extractive PDF cue:** Therefore, we focus primarily on qualitative visualizations for this dataset.
- **p. 7 / 4.3. Results - extractive PDF cue:** Comparison dynamic modeling on Neu3D Dataset [13].
- **p. 8 / 4.3. Results - extractive PDF cue:** Qualitative comparison with 4DGS [36] on the Neu3D [13] dataset.
- **p. 6 / 4.3. Results - extractive PDF cue:** Qualitative comparison of baseline methods [10, 24, 31] for distractor-free scene reconstruction on the Aria and EPIC-Field sequences.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. With self-supervised foreground-background gaussian splats modeling and accurate decomposition, DeGauss simultaneously enables (a): SOTA distractor-free static scene reconstruction for casual captures (no dynamic ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Our method simultaneously reconstructs the 3D scene and learns an unsupervised decomposition into decoupled static background and dynamic foreground branches, where the update ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers signifi- cantly greater robustness in handling local ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparison of baseline methods [10, 24, 31] for distractor-free scene reconstruction on the Aria and EPIC-Field sequences. Left of the dashed line: ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Distractor free scene reconstruction on NeRF On-the-go Dataset[22].The best , second best , and third best are highlighted. ‡: ±0.005 SSIM and LPIPS ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Occlusion handling on the NeRF-on-the-Go dataset [22]. Compared to SpotlessSplats [24], our method better preserves fine details in the training views (please consider ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison dynamic modeling on Neu3D Dataset [13]. The best , second best , and third best are highlighted. Noticeably, our method shows a ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Our method robustly handles various challenges, preserv- ing clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | HyperNeRF Dataset [21] features real-world activities captured with smooth trajectories. | embodiment, simulator version and control stack | p. 5 (4.2. Datasets), p. 7 (4.3. Results) |
| Task/environment | Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene ... | reset, timeout, object/scene variation | p. 7 (4.3. Results), p. 6 (4.3. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.4. Background Brightness Control) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 5 (3.6. Unsupervised scene decomposition) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2, where our methods achieve consistently better LPIPS scores. | definition/direction/unit from same section | p. 7 (4.3. Results) |
| Noticeably, our method shows a consistently better LPIPS score compared to baseline methods. | definition/direction/unit from same section | p. 7 (4.3. Results) |
| However, as noted in [8], the camera poses are considerably inaccurate. | definition/direction/unit from same section | p. 5 (4.2. Datasets) |
| The foreground Gaussians are initialized from randomly generated points distributed within this scene boundary. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| Our method shows generally superior performance over state-of-the-art methods. | definition/direction/unit from same section | p. 6 (4.3. Results) |
| Compared to baseline methods [10, 24, 31], our method models high-quality distractor-free static background with accurate foreground separation. | definition/direction/unit from same section | p. 6 (4.3. Results) |
| Figure 1. With self-supervised foreground-background gaussian splats modeling and accurate decomposition, DeGauss simultaneously enables (a): SOTA distractor-free static scene reconstruction for casual captures (no ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Our method simultaneously reconstructs the 3D scene and learns an unsupervised decomposition into decoupled static background and dynamic foreground branches, where the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to baseline methods [10, 24, 31], our method models high-quality distractor-free static background with accurate foreground separation. | comparison identity and matched condition | p. 6 (4.3. Results) |
| Noticeably, our method shows a consistently better LPIPS score compared to baseline methods. | comparison identity and matched condition | p. 7 (4.3. Results) |
| Qualitative comparison of baseline methods [10, 24, 31] for distractor-free scene reconstruction on the Aria and EPIC-Field sequences. | comparison identity and matched condition | p. 6 (4.3. Results) |
| We take one sequence from ADT [20], AEA [16], Hot3D [2], and Epic-Field [32] dataset, respectively, ranging from 28005000 frames, to evaluate our method ... | comparison identity and matched condition | p. 5 (4.2. Datasets) |
| Our methods generalize to image collections and achieve state-of-the-art results. | comparison identity and matched condition | p. 7 (4.3. Results) |
| Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers signifi- cantly greater robustness in handling ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Left of the dashed line: composed render comparisons; right: static reconstruction comparison(without camera masks). | component/input/data sensitivity | p. 6 (4.3. Results) |
| Figure 9. Ablation Study on AEA [16] dataset. w/o Ldepth Ours | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 10. Ablation Study on Neu3D dataet [13] cut beef scene. | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • We propose DeGauss, a decoupled foregroundbackground design which leverages dynamic-static Gaussian splatting for robust and generalizable dynamicstatic decomposition. ... | Notably, our method consistently achieves significantly better LPIPS scores over the previous SOTA method SpotlessSplats [24]. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.3. Results), p. 6 (4.3. Results) |
| Primary metric/result | 2, where our methods achieve consistently better LPIPS scores. | numeric claim only at cited anchor | p. 7 (4.3. Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2. Datasets - extractive PDF cue:** We take one sequence from ADT [20], AEA [16], Hot3D [2], and Epic-Field [32] dataset, respectively, ranging from 28005000 frames, to evaluate our method against ...
- **p. 5 / 4.2. Datasets - extractive PDF cue:** For each sequence, every 1 out of 5 frames is held out during training.
- **p. 5 / 4.2. Datasets - extractive PDF cue:** Neu3D Dataset [13] was captured using 15 to 20 static cameras recording relatively simple activities over 300 frames.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting. | p. 8 (6. Conclusion) |
| body limitation/failure cue | We show our method robustly handles occlusion and reconstructs fine static details compared to SpotlessSplats [24]in Fig. | p. 7 (4.3. Results) |
| body limitation/failure cue | Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene ... | p. 7 (4.3. Results) |
| body limitation/failure cue | Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers signifi- cantly greater robustness in handling ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The decoder D comprises: D = {ϕx, ϕr, ϕs ϕσ, ϕc, ϕmf , ϕmb, ϕb}. | p. 3 (3.2. Foreground deformable gaussian) |
| The final color \protect \mathbf {C} at each pixel is then computed by blending the contribution of all Gaussians, sorted by their depth: | p. 3 (3.1. 3D Gaussian Splatting) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** This paper proposes DeGauss to robust decompose dynamicstatic elements in the scene with gaussian splatting.
- **p. 7 / 4.3. Results - extractive PDF cue:** We show our method robustly handles occlusion and reconstructs fine static details compared to SpotlessSplats [24]in Fig.
- **p. 7 / 4.3. Results - extractive PDF cue:** Our method robustly handles various challenges, preserving clean and high quality static background. dataset Nerf-on-the-go[22] with clean reference test views, we report detailed per-scene metrics ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Compared to SpotlessSplats [24], which is constrained by initialization and overfit to floaters. Our method offers signifi- cantly greater robustness in handling local ...

- **PDF anchors reviewed:** datasets p. 5 (4.2. Datasets), p. 7 (4.3. Results), p. 6 (4.3. Results), p. 5 (4.2. Datasets), p. 7 (4.3. Results), p. 8 (4.3. Results), metrics p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.2. Datasets), p. 5 (4.1. Implementation Details), p. 6 (4.3. Results), p. 6 (4.3. Results), baselines p. 6 (4.3. Results), p. 7 (4.3. Results), p. 6 (4.3. Results), p. 5 (4.2. Datasets), p. 7 (4.3. Results), p. 5 (Figure/Table caption), results p. 7 (4.3. Results), p. 7 (4.3. Results), p. 5 (4.3. Results), p. 6 (4.3. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
