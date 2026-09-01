# Evaluation - Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=MCu8SOjPad; PDF retrieval source: https://openreview.net/pdf/ed47436b3c090baac63dc92adf3fafca0e15cc01.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results), p. 7 (4.1. Main Results), p. 8 (4.1. Main Results), p. 6 (4. Experiments), p. 13 (Figure/Table caption)): The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in the scene, achieving a performance improvement ...

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive PDF cue:** Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Following (Ding et al., 2023; Zhai et al., 2025; Wu et al., 2025), we conduct experiments on the real-world View-of-Delft (VoD) dataset (Palffy et al., ...
- **p. 7 / 4.1. Main Results - extractive PDF cue:** Note that fully-supervised methods are trained with the radar scene flow ground truth derived from the annotated 3D tracking boxes provided by the dataset, and ...
- **p. 7 / 4.1. Main Results - extractive PDF cue:** Qualitative Results on VoD validation dataset.
- **p. 8 / 4.1. Main Results - extractive PDF cue:** Lsc is the soft chamfer loss without instance-aware guidance and Lss is the KNN-based spatial smoothness loss; both are from RaFlow (Ding et al., 2022). ...
- **p. 8 / 4.1. Main Results - extractive PDF cue:** Ablation Study on Loss Terms on VoD validation set.
- **p. 8 / 4.2. Ablation Studies - extractive PDF cue:** The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in the ...
- **p. 7 / 4.1. Main Results - extractive PDF cue:** IterFlow also brings a 39.2% error reduction on the SRNE metric and achieves the best performance on the MRNE metric, generating more accurate flow estimation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Main Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in ... | p. 8 (4.2. Ablation Studies) |
| 4.1. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | When compared to LiDAR-based approaches, our method even surpasses the best fully supervised model, PVRAFT (Wei et al., 2021), achieving performance improvements across all ... | p. 7 (4.1. Main Results) |
| 4.1. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In particular, IterFlow yields a 34.7% performance improvement on the EPE metric, while increasing AccS and AccR by 13.6% and 21.4%, respectively. | p. 7 (4.1. Main Results) |
| 4.1. Main Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, when replacing the original loss combinations in (Wu et al., 2020) and (Ding et al., 2022) with our proposed ones (rows 2 and ... | p. 8 (4.1. Main Results) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition, for the cross-modal supervised CMFlow (Ding et al., 2023), we generate extra required optical flow labels and pseudo scene flow labels by ... | p. 6 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive PDF cue:** Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Following (Ding et al., 2023; Zhai et al., 2025; Wu et al., 2025), we conduct experiments on the real-world View-of-Delft (VoD) dataset (Palffy et al., ...
- **p. 7 / 4.1. Main Results - extractive PDF cue:** Note that fully-supervised methods are trained with the radar scene flow ground truth derived from the annotated 3D tracking boxes provided by the dataset, and ...
- **p. 7 / 4.1. Main Results - extractive PDF cue:** Qualitative Results on VoD validation dataset.
- **p. 8 / 4.1. Main Results - extractive PDF cue:** Lsc is the soft chamfer loss without instance-aware guidance and Lss is the KNN-based spatial smoothness loss; both are from RaFlow (Ding et al., 2022). ...
- **p. 8 / 4.1. Main Results - extractive PDF cue:** Ablation Study on Loss Terms on VoD validation set.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Comparison between existing self-supervised (SSF) and cross-modal supervised (CMS) radar scene flow estimation settings and our weakly supervised cross-modal learning setting. SF , ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overall architecture of our proposed method. The process of the kth scene flow iteration is depicted on the left and the detailed loss ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. An example of mismached chamfer pairs. The top and bottom rows show two consecutive frames at time t and time t + 1, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. An example of wrong KNN-based spatial flow smooth- ing. The figure shows the bird's-eye view of a cyclist (green bounding box). Foreground radar ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative Evaluation and Model Complexity Comparison on VoD validation set. In the Category (Cat.) column, existing methods are classified depending on the input ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative Evaluation on Network Architecture and Loss Scalability on VoD validation set. Lc, Ls, Lg denote the official chamfer loss, local flow smoothness ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative Results on VoD validation dataset. The first row and the third row display two separate traffic scenes; while the second row and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation Study on Loss Terms on VoD validation set. Lsc is the soft chamfer loss without instance-aware guidance and Lss is the KNN-based ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Task/environment | Following (Ding et al., 2023; Zhai et al., 2025; Wu et al., 2025), we conduct experiments on the real-world View-of-Delft (VoD) dataset (Palffy et ... | reset, timeout, object/scene variation | p. 6 (4. Experiments), p. 7 (4.1. Main Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.1. IterFlow), p. 6 (3.3. Rigid Static Loss) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in ... | definition/direction/unit from same section | p. 8 (4.2. Ablation Studies) |
| IterFlow also brings a 39.2% error reduction on the SRNE metric and achieves the best performance on the MRNE metric, generating more accurate flow ... | definition/direction/unit from same section | p. 7 (4.1. Main Results) |
| Following (Ding et al., 2022; 2023; Zhai et al., 2025; Wu et al., 2025), we use standard metrics for evaluation: 1) EPE: average 3D ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| When compared to LiDAR-based approaches, our method even surpasses the best fully supervised model, PVRAFT (Wei et al., 2021), achieving performance improvements across all ... | definition/direction/unit from same section | p. 7 (4.1. Main Results) |
| This analysis underscores the necessity and effectiveness of our loss designs for radar scene flow learning. | definition/direction/unit from same section | p. 8 (4.1. Main Results) |
| EPE < 0.05/0.1m or the relative error <5%/10%; 3) RNE: resolutionnormalized EPE by dividing EPE by the ratio of 4D radar and LiDAR resolution, ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Figure 8. Visualization of failure cases on VoD validation set. Each row displays a driving scenario and regions with large scene flow estimation errors ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Figure 1. Comparison between existing self-supervised (SSF) and cross-modal supervised (CMS) radar scene flow estimation settings and our weakly supervised cross-modal learning setting. SF ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For a fair comparison with the baselines, we use their official loss configuration and hyperparameter settings for network retraining on the VoD radar scene ... | comparison identity and matched condition | p. 6 (4. Experiments) |
| We compare our method with state-of-the-art scene flow estimation models 6 | comparison identity and matched condition | p. 6 (4.1. Main Results) |
| Compared to the best radar-based CMFlow (Ding et al., 2023), IterFlow has ∼40× fewer parameters and ∼30× lower GFLOPs while achieving better performance. | comparison identity and matched condition | p. 7 (4.1. Main Results) |
| When compared to LiDAR-based approaches, our method even surpasses the best fully supervised model, PVRAFT (Wei et al., 2021), achieving performance improvements across all ... | comparison identity and matched condition | p. 7 (4.1. Main Results) |
| As shown in the last section of Table 2, when replacing the backbone of PointPWC and RaFlow with IterFlow while keeping their respective loss ... | comparison identity and matched condition | p. 8 (4.1. Main Results) |
| Ablation Study on Loss Terms on VoD validation set. | comparison identity and matched condition | p. 8 (4.1. Main Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablation Study on Loss Terms on VoD validation set. Lsc is the soft chamfer loss without instance-aware guidance and Lss is the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Note that fully-supervised methods are trained with the radar scene flow ground truth derived from the annotated 3D tracking boxes provided by the dataset, ... | component/input/data sensitivity | p. 7 (4.1. Main Results) |
| B.2 in the appendix for hyperparameter sensitivity analysis of L, R and K. officially released YOLO11-l (Khanam & Hussain, 2024) model and the huge ... | component/input/data sensitivity | p. 6 (4. Experiments) |
| Second, we examine the effectiveness of Lis by removing it from total loss. | component/input/data sensitivity | p. 8 (4.2. Ablation Studies) |
| Figure 7. Ablation on iteration steps K and ball query hyperparameters L and R. When L varies, R = 1m; when R varies, L ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| In addition, for the cross-modal supervised CMFlow (Ding et al., 2023), we generate extra required optical flow labels and pseudo scene flow labels by ... | component/input/data sensitivity | p. 6 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Given the high cost of high-performance LiDAR sensors, we propose a novel setting, weakly supervised cross-modal learning for 4D radar scene flow, that relies ... | The experimental results in Table 3 illustrate that the addition of Lis successfully improves the prediction accuracy in both dynamic and static areas in ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results), p. 7 (4.1. Main Results), p. 8 (4.1. Main Results), p. 6 (4. Experiments), p. 13 (Figure/Table caption) |
| Primary metric/result | When compared to LiDAR-based approaches, our method even surpasses the best fully supervised model, PVRAFT (Wei et al., 2021), achieving performance improvements across all ... | numeric claim only at cited anchor | p. 7 (4.1. Main Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive PDF cue:** Following (Ding et al., 2023; Zhai et al., 2025; Wu et al., 2025), we conduct experiments on the real-world View-of-Delft (VoD) dataset (Palffy et al., ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from ...
- **p. 6 / 4. Experiments - extractive PDF cue:** IterFlow is implemented in PyTorch (Paszke et al., 2019) and trained for 150 epochs with a batch size of 8.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 8. Visualization of failure cases on VoD validation set. Each row displays a driving scenario and regions with large scene flow estimation errors ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | The advantage of Lic over Lsc is twofold: on one hand, Lic only calculates the chamfer distance between points within the same instance across ... | p. 8 (4.2. Ablation Studies) |
| body limitation/failure cue | Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels ... | p. 6 (4. Experiments) |
| body limitation/failure cue | The resulting enforced consistency between incorrect point pairs can significantly degrade network performance. | p. 5 (3.2. Instance-aware Loss Functions) |
| body limitation/failure cue | This result highlights that our ball query-based correlation operation is more robust in sparse radar scenarios than the KNN-based and voxelbased correlation modules used ... | p. 7 (4.1. Main Results) |
| body limitation/failure cue | Finally, comparing rows 5 and 7, we find that using LiDARbased losses in (Wu et al., 2020) to train our IterFlow results in dramatic ... | p. 8 (4.1. Main Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| IterFlow is implemented in PyTorch (Paszke et al., 2019) and trained for 150 epochs with a batch size of 8. | p. 6 (4. Experiments) |
| The Adam optimizer with an initial learning rate of 0.001 is used. | p. 6 (4. Experiments) |
| During training, the consecutive radar point clouds Pt and Pt+1 are fed into IterFlow to generate the final scene flow prediction FK ∈RN1×3 after ... | p. 3 (3. Method) |
| Here φ(·) represents the multi-scale encoder. | p. 4 (3.1. IterFlow) |
| Meanwhile, the coarse flow vector Fk-1 is also encoded via an MLP. | p. 4 (3.1. IterFlow) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 8. Visualization of failure cases on VoD validation set. Each row displays a driving scenario and regions with large scene flow estimation errors are ...
- **p. 8 / 4.2. Ablation Studies - extractive PDF cue:** The advantage of Lic over Lsc is twofold: on one hand, Lic only calculates the chamfer distance between points within the same instance across frames, ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Since the VoD dataset does not provide ready-made scene flow ground truth, we adopt the commonly used preprocessing methods to generate scene flow labels from ...
- **p. 5 / 3.2. Instance-aware Loss Functions - extractive PDF cue:** The resulting enforced consistency between incorrect point pairs can significantly degrade network performance.
- **p. 7 / 4.1. Main Results - extractive PDF cue:** This result highlights that our ball query-based correlation operation is more robust in sparse radar scenarios than the KNN-based and voxelbased correlation modules used in ...
- **p. 8 / 4.1. Main Results - extractive PDF cue:** Finally, comparing rows 5 and 7, we find that using LiDARbased losses in (Wu et al., 2020) to train our IterFlow results in dramatic performance ...

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Main Results), p. 7 (4.1. Main Results), p. 8 (4.1. Main Results), p. 8 (4.1. Main Results), metrics p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results), p. 6 (4. Experiments), p. 7 (4.1. Main Results), p. 8 (4.1. Main Results), p. 6 (4. Experiments), baselines p. 6 (4. Experiments), p. 6 (4.1. Main Results), p. 7 (4.1. Main Results), p. 7 (4.1. Main Results), p. 8 (4.1. Main Results), p. 8 (4.1. Main Results), results p. 8 (4.2. Ablation Studies), p. 7 (4.1. Main Results), p. 7 (4.1. Main Results), p. 8 (4.1. Main Results), p. 6 (4. Experiments), p. 13 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
