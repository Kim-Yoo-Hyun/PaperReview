# Evaluation - E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative evaluations), p. 6 (4.2. Quantitative evaluations), p. 7 (4.4. Ablation study), p. 7 (4.3. Qualitative evaluations), p. 5 (4.2. Quantitative evaluations)): Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine details such as dot patterns on the back ...

## Evaluation Body Digest

- **p. 6 / 4.3. Qualitative evaluations - extractive body cue:** IncEventGS† fails to reconstruct recognizable figurines and produces distorted scenes due to severe trajectory drift.
- **p. 5 / 4.1. Experiment settings - extractive body cue:** ESVO2 is evaluated only on real datasets.
- **p. 5 / 4.2. Quantitative evaluations - extractive body cue:** 1 shows reconstruction quality on synthetic scenes.
- **p. 6 / 4.3. Qualitative evaluations - extractive body cue:** 3 presents reconstruction results across Replica scenes.
- **p. 7 / 4.3. Qualitative evaluations - extractive body cue:** Qualitative results on Replica dataset.
- **p. 7 / 4.3. Qualitative evaluations - extractive body cue:** Impact of trajectory error on reconstruction quality.
- **p. 8 / 4.4. Ablation study - extractive body cue:** Excessive edge emphasis under-represents smooth surfaces, leading to incorrect trajectory estimation.
- **p. 8 / 4.4. Ablation study - extractive body cue:** Without edge initialization, the system experiences trajectory drift, leading to loss of details in 3D reconstruction.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiment settings (p. 5); 4.2. Quantitative evaluations (p. 5); 4.3. Qualitative evaluations (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine details such ... | p. 8 (Figure/Table caption) |
| 4.2. Quantitative evaluations | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves competitive performance solely using event data. | p. 6 (4.2. Quantitative evaluations) |
| 4.2. Quantitative evaluations | EMPIRICAL / SOURCE-REPORTED EVALUATION | On synthetic Replica scenes, our edge-guided approach achieves sub-millimeter accuracy across all scenes. | p. 6 (4.2. Quantitative evaluations) |
| 4.4. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3 shows the progressive improvement when adding our components to IncEventGS†. | p. 7 (4.4. Ablation study) |
| 4.3. Qualitative evaluations | EMPIRICAL / SOURCE-REPORTED EVALUATION | (d) Our method achieves accurate reconstruction with sharp textures and correct spatial alignment. | p. 7 (4.3. Qualitative evaluations) |

## Dataset / Benchmark Role

- **p. 6 / 4.3. Qualitative evaluations - extractive body cue:** IncEventGS† fails to reconstruct recognizable figurines and produces distorted scenes due to severe trajectory drift.
- **p. 5 / 4.1. Experiment settings - extractive body cue:** ESVO2 is evaluated only on real datasets.
- **p. 5 / 4.2. Quantitative evaluations - extractive body cue:** 1 shows reconstruction quality on synthetic scenes.
- **p. 6 / 4.3. Qualitative evaluations - extractive body cue:** 3 presents reconstruction results across Replica scenes.
- **p. 7 / 4.3. Qualitative evaluations - extractive body cue:** Qualitative results on Replica dataset.
- **p. 7 / 4.3. Qualitative evaluations - extractive body cue:** Impact of trajectory error on reconstruction quality.
- **p. 8 / 4.4. Ablation study - extractive body cue:** Excessive edge emphasis under-represents smooth surfaces, leading to incorrect trajectory estimation.
- **p. 8 / 4.4. Ablation study - extractive body cue:** Without edge initialization, the system experiences trajectory drift, leading to loss of details in 3D reconstruction.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Edge-guided reconstruction framework. Our pipeline extracts robust edges from consecutive event maps (Sec. 3.2), initializes edge-aware Gaussians (Sec. 3.3), and applies edge-guided losses ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. NVS performance on Replica dataset. Our method achieves superior reconstruction quality solely using event data. † denotes no depth supervision and ∗denotes that ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Absolute trajectory error (ATE). RMSE (cm) across synthetic Replica and real TUM-VIE sequences. Our method achieves competitive performance solely using event data.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. ATE with respect to the length of the sequence. unreliable gradient signals. In contrast, our edge-centric ap- proach focuses on structural boundaries where ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on edge components.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results on Replica dataset. Red boxes highlight regions of interest for comparison. Our method produces sharper boundaries and cleaner surfaces compared with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Impact of trajectory error on reconstruction quality. (a) Ground truth. (b) IncEventGS exhibits multiple failure modes: spatial misalignment causing viewpoint shifts and blurred ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on edge ratio (redge). Edge Ratio (redge) 0.0 0.1 0.3 0.5 0.7 1.0

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | IncEventGS† fails to reconstruct recognizable figurines and produces distorted scenes due to severe trajectory drift. | embodiment, simulator version and control stack | p. 6 (4.3. Qualitative evaluations), p. 5 (4.1. Experiment settings) |
| Task/environment | ESVO2 is evaluated only on real datasets. | reset, timeout, object/scene variation | p. 5 (4.1. Experiment settings), p. 5 (4.2. Quantitative evaluations) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 4 (3.2. Robust edge detection with patch-based tem) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 3 (3.1. Framework overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our edge-guided loss spatially weights reconstruction error by edge confidence, enabling rapid structure establishment and substantially clearer boundaries at convergence. | definition/direction/unit from same section | p. 7 (4.4. Ablation study) |
| 4 illustrates how pose accuracy influences the 3D reconstruction quality on the TUM-VIE dataset. | definition/direction/unit from same section | p. 6 (4.3. Qualitative evaluations) |
| Without edge guidance, photometric error from event noise uniformly affects 3D reconstruction, causing optimization process to receive 4926 | definition/direction/unit from same section | p. 5 (4.2. Quantitative evaluations) |
| For camera pose estimation, we use absolute trajectory error (ATE), which measures the root-mean-square error (RMSE) of the aligned trajectory after SE(3) alignment using ... | definition/direction/unit from same section | p. 5 (4.1. Experiment settings) |
| Impact of trajectory error on reconstruction. | definition/direction/unit from same section | p. 6 (4.3. Qualitative evaluations) |
| (c) IncEventGS† fails to reconstruct scenes due to severe trajectory errors. | definition/direction/unit from same section | p. 7 (4.3. Qualitative evaluations) |
| We find that redge ∈[0.1, 0.3] provides sufficient edge constraints, resulting in clear features in 3D reconstruction and low trajectory errors. | definition/direction/unit from same section | p. 8 (4.4. Ablation study) |
| While edges provide strong geometric constraints, the lack of information about smooth surfaces makes the difference between the rendered image and the input event ... | definition/direction/unit from same section | p. 8 (4.4. Ablation study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method produces sharper boundaries and cleaner surfaces compared with baselines. | comparison identity and matched condition | p. 7 (4.3. Qualitative evaluations) |
| Without requiring any depth supervision, our edge-guided approach outperforms DEVO [16] and IncEventGS† by substantial margins. | comparison identity and matched condition | p. 6 (4.2. Quantitative evaluations) |
| While baseline methods show significant performance variation across scenes, our method maintains more stable performance. | comparison identity and matched condition | p. 5 (4.2. Quantitative evaluations) |
| We compare our E2EGS with baselines to validate the effectiveness of our approach for both 3D reconstruction and trajectory estimation. | comparison identity and matched condition | p. 5 (4.1. Experiment settings) |
| Meanwhile, the baseline methods suffer from noisy photometric consistency that accumulates into geometric distortions. | comparison identity and matched condition | p. 6 (4.3. Qualitative evaluations) |
| Baseline (top) vs. ours with edge loss but random initialization (bottom) at early and final training stages. | comparison identity and matched condition | p. 8 (4.4. Ablation study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine details such ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| To validate the contribution of each proposed component, we conduct component-wise ablation experiments. | component/input/data sensitivity | p. 7 (4.4. Ablation study) |
| Without edge guidance, photometric error from event noise uniformly affects 3D reconstruction, causing optimization process to receive 4926 | component/input/data sensitivity | p. 5 (4.2. Quantitative evaluations) |
| Without requiring any depth supervision, our edge-guided approach outperforms DEVO [16] and IncEventGS† by substantial margins. | component/input/data sensitivity | p. 6 (4.2. Quantitative evaluations) |
| Ablation study on edge ratio (redge). | component/input/data sensitivity | p. 7 (4.3. Qualitative evaluations) |
| Without edge initialization, the system experiences trajectory drift, leading to loss of details in 3D reconstruction. | component/input/data sensitivity | p. 8 (4.4. Ablation study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To overcome these limitations, we propose event-toedge Gaussian splatting (E2EGS), a pose-free framework that leverages edge information derived solely from event streams. | Figure 6. Effect of edge ratio on reconstruction quality. Red boxes highlight comparison regions. (a) Ground truth. (b) Without edge guidance, fine details such ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative evaluations), p. 6 (4.2. Quantitative evaluations), p. 7 (4.4. Ablation study), p. 7 (4.3. Qualitative evaluations), p. 5 (4.2. Quantitative evaluations) |
| Primary metric/result | Our method achieves competitive performance solely using event data. | numeric claim only at cited anchor | p. 6 (4.2. Quantitative evaluations) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. Impact of trajectory error on reconstruction quality. (a) Ground truth. (b) IncEventGS exhibits multiple failure modes: spatial misalignment causing viewpoint shifts and ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Adaptive edge extraction methods that respond to local event statistics could address this limitation. | p. 8 (5. Conclusion) |
| body limitation/failure cue | On real-world TUM-VIE sequences, IncEventGS† suffers from catastrophic failure due to the lack of geometric constraints in random initialization, causing pose optimization to converge ... | p. 6 (4.2. Quantitative evaluations) |
| body limitation/failure cue | IncEventGS exhibits various failure modes in regions highlighted by red boxes, including wavelike artifacts in texture-less regions, missing fine details such as textures and ... | p. 6 (4.3. Qualitative evaluations) |
| body limitation/failure cue | IncEventGS shows failures including wave-like artifacts, missing details, and indistinct boundaries. | p. 7 (4.3. Qualitative evaluations) |
| body limitation/failure cue | Figure 1. Edge-guided reconstruction framework. Our pipeline extracts robust edges from consecutive event maps (Sec. 3.2), initializes edge-aware Gaussians (Sec. 3.3), and applies edge-guided ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We adopt the 3DGS implementation [13] and the tracking-mapping pipeline from IncEventGS [11] with standard hyperparameter settings. | p. 5 (4.1. Experiment settings) |
| All experiments are conducted on a server with an AMD Ryzen Threadripper PRO 3955WX processor and NVIDIA RTX A5000 GPU. | p. 5 (4.1. Experiment settings) |
| For each tile, we compute the standard deviation of the edge normal orientations. | p. 4 (3.3. Edge-guided Gaussian initialization) |
| The resulting edge map M ∈[0, 1]H×W encodes normalized edge confidence values at each pixel. | p. 4 (3.2. Robust edge detection with patch-based tem) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Impact of trajectory error on reconstruction quality. (a) Ground truth. (b) IncEventGS exhibits multiple failure modes: spatial misalignment causing viewpoint shifts and blurred ...
- **p. 8 / 5. Conclusion - extractive body cue:** Adaptive edge extraction methods that respond to local event statistics could address this limitation.
- **p. 6 / 4.2. Quantitative evaluations - extractive body cue:** On real-world TUM-VIE sequences, IncEventGS† suffers from catastrophic failure due to the lack of geometric constraints in random initialization, causing pose optimization to converge to ...
- **p. 6 / 4.3. Qualitative evaluations - extractive body cue:** IncEventGS exhibits various failure modes in regions highlighted by red boxes, including wavelike artifacts in texture-less regions, missing fine details such as textures and patterns, ...
- **p. 7 / 4.3. Qualitative evaluations - extractive body cue:** IncEventGS shows failures including wave-like artifacts, missing details, and indistinct boundaries.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Edge-guided reconstruction framework. Our pipeline extracts robust edges from consecutive event maps (Sec. 3.2), initializes edge-aware Gaussians (Sec. 3.3), and applies edge-guided losses ...

- **Evidence anchors reviewed:** datasets p. 6 (4.3. Qualitative evaluations), p. 5 (4.1. Experiment settings), p. 5 (4.2. Quantitative evaluations), p. 6 (4.3. Qualitative evaluations), p. 7 (4.3. Qualitative evaluations), p. 7 (4.3. Qualitative evaluations), metrics p. 7 (4.4. Ablation study), p. 6 (4.3. Qualitative evaluations), p. 5 (4.2. Quantitative evaluations), p. 5 (4.1. Experiment settings), p. 6 (4.3. Qualitative evaluations), p. 7 (4.3. Qualitative evaluations), baselines p. 7 (4.3. Qualitative evaluations), p. 6 (4.2. Quantitative evaluations), p. 5 (4.2. Quantitative evaluations), p. 5 (4.1. Experiment settings), p. 6 (4.3. Qualitative evaluations), p. 8 (4.4. Ablation study), results p. 8 (Figure/Table caption), p. 6 (4.2. Quantitative evaluations), p. 6 (4.2. Quantitative evaluations), p. 7 (4.4. Ablation study), p. 7 (4.3. Qualitative evaluations), p. 5 (4.2. Quantitative evaluations).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
