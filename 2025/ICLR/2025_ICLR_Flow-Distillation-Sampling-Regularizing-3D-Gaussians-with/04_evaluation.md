# Evaluation - Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=BzsjHiBfLk; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/113507. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 7 (4 EXPERIMENTS)): We found that Sea Raft (Wang et al., 2024) outperforms Raft (Teed and Deng, 2020) on FDS, indicating that a better optical flow model can lead to more significant improvements.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.1.2 DATASETS AND METRICS We evaluate our method for 3D reconstruction and novel view synthesis tasks on Mushroom (Ren et al., 2024), ScanNet (v2) (Dai ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We select 5 scenes from the ScanNet (V2) 7
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 3D Reconstruction and novel view synthesis results on ScanNet dataset.
- **p. 8 / 4.2 RESULTS - extractive body cue:** The qualitative comparisons on the Mushroom and ScanNet dataset are illustrated in Fig.
- **p. 9 / 4.2 RESULTS - extractive body cue:** The comparison results on Mushroom dataset are shown in Tab.
- **p. 9 / 4.2 RESULTS - extractive body cue:** Ablation study on FDS: In this section, we present the design of our FDS method through an ablation study on the Mushroom dataset to validate ...
- **p. 10 / 4.2 RESULTS - extractive body cue:** (5) utilizing ground truth depth in dataset.
- **p. 10 / 4.2 RESULTS - extractive body cue:** We apply our method to the 3DGS-based framework, and the geometry is enhanced on the Mushroom, ScanNet, and Replica datasets.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); 4.2 RESULTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We found that Sea Raft (Wang et al., 2024) outperforms Raft (Teed and Deng, 2020) on FDS, indicating that a better optical flow model ... | p. 8 (4.2 RESULTS) |
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | From the results, it can be seen that depth order information provided by monocular depth improves reconstruction accuracy. | p. 9 (4.2 RESULTS) |
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Meanwhile, our FDS achieves the best performance among all the priors, and by integrating all three components, we obtained the optimal results. | p. 9 (4.2 RESULTS) |
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | By incorporating the matching prior through FDS, the quality of the rendered depth is significantly improved. | p. 8 (4.2 RESULTS) |
| 4.2 RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5 CONCLUSIONS In this paper, we propose Flow Distillation Sampling (FDS), which leverages the matching prior between input views and sampled unobserved views from ... | p. 10 (4.2 RESULTS) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.1.2 DATASETS AND METRICS We evaluate our method for 3D reconstruction and novel view synthesis tasks on Mushroom (Ren et al., 2024), ScanNet (v2) (Dai ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We select 5 scenes from the ScanNet (V2) 7
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 3D Reconstruction and novel view synthesis results on ScanNet dataset.
- **p. 8 / 4.2 RESULTS - extractive body cue:** The qualitative comparisons on the Mushroom and ScanNet dataset are illustrated in Fig.
- **p. 9 / 4.2 RESULTS - extractive body cue:** The comparison results on Mushroom dataset are shown in Tab.
- **p. 9 / 4.2 RESULTS - extractive body cue:** Ablation study on FDS: In this section, we present the design of our FDS method through an ablation study on the Mushroom dataset to validate ...
- **p. 10 / 4.2 RESULTS - extractive body cue:** (5) utilizing ground truth depth in dataset.
- **p. 10 / 4.2 RESULTS - extractive body cue:** We apply our method to the 3DGS-based framework, and the geometry is enhanced on the Mushroom, ScanNet, and Replica datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Pipeline of the proposed FDS. For each input view, we apply the FDS camera sampling scheme to generate corresponding unobserved sampled view. We ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Explanation of depth-adaptive translation radius. A fixed-radius camera sampling scheme may result in significantly different flow values (Flow 1 and Flow 2) in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Comparison of depth reconstruction on Mushroom and ScanNet datasets. The original 3DGS or 2DGS model equipped with FDS can remove unwanted floaters and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. 3D Reconstruction and novel view synthesis results on Mushroom dataset. * Represents that FDS uses the Raft model.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. 3D Reconstruction and novel view synthesis results on ScanNet dataset.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on geometry priors.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4. The error map of Radiance Flow and Prior Flow. RF: Radiance Flow, PF: Prior Flow, * means that there is no FDS loss ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on FDS strategies. Mθ(X, Cs) Loss Metric X = Ci X = Ii Next Input view Sampled view

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1.2 DATASETS AND METRICS We evaluate our method for 3D reconstruction and novel view synthesis tasks on Mushroom (Ren et al., 2024), ScanNet (v2) ... | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Task/environment | We select 5 scenes from the ScanNet (V2) 7 | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 4 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Additionally, for mesh evaluation, we use metrics including Accuracy, Completion, Chamfer-L1 distance, Normal Consistency, and F-scores. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| The error map of Radiance Flow and Prior Flow. | definition/direction/unit from same section | p. 9 (4.2 RESULTS) |
| Mθ(X, Cs) Loss Metric X = Ci X = Ii Next Input view Sampled view Fixed Sampled view Abs Rel ↓ F-score ↑ NC ... | definition/direction/unit from same section | p. 10 (4.2 RESULTS) |
| Method Acc ↓ Comp ↓ C-L1 ↓ NC ↑ F-Score ↑ Abs Rel ↓ PSNR ↑ SSIM ↑ LPIPS ↓ GOF 1.8671 0.0805 0.9738 ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| From the results, it can be seen that depth order information provided by monocular depth improves reconstruction accuracy. | definition/direction/unit from same section | p. 9 (4.2 RESULTS) |
| Thus, we incorporate normal prior supervision on the rendered normals in ScanNet (V2) dataset by default. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| We removed the depth distortion loss in 2DGS because we found that it degrades its results in indoor scenes. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| We also experiment with modifying the FDS loss. | definition/direction/unit from same section | p. 10 (4.2 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| With the integration of FDS, the mesh quality is significantly enhanced compared to the baseline, featuring fewer floaters and more well-defined shapes. | comparison identity and matched condition | p. 9 (4.2 RESULTS) |
| On the Mushroom dataset, adding the FDS loss increases the training time by half an hour, which maintains the same level as baseline. | comparison identity and matched condition | p. 8 (4.2 RESULTS) |
| We found that Sea Raft (Wang et al., 2024) outperforms Raft (Teed and Deng, 2020) on FDS, indicating that a better optical flow model ... | comparison identity and matched condition | p. 8 (4.2 RESULTS) |
| The comparison results on Mushroom dataset are shown in Tab. | comparison identity and matched condition | p. 9 (4.2 RESULTS) |
| Figure 3. Comparison of depth reconstruction on Mushroom and ScanNet datasets. The original 3DGS or 2DGS model equipped with FDS can remove unwanted floaters ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4. Ablation study on FDS strategies. Mθ(X, Cs) Loss Metric X = Ci X = Ii Next Input view Sampled view | comparison identity and matched condition | p. 10 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on FDS: In this section, we present the design of our FDS method through an ablation study on the Mushroom dataset to ... | component/input/data sensitivity | p. 9 (4.2 RESULTS) |
| We removed the depth distortion loss in 2DGS because we found that it degrades its results in indoor scenes. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Using Ii instead of Ci help us to remove the 9 | component/input/data sensitivity | p. 9 (4.2 RESULTS) |
| Figure 3. Comparison of depth reconstruction on Mushroom and ScanNet datasets. The original 3DGS or 2DGS model equipped with FDS can remove unwanted floaters ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 4. Ablation study on FDS strategies. Mθ(X, Cs) Loss Metric X = Ci X = Ii Next Input view Sampled view | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| For example, in the third row, we use the next training input view as the sampling view, and replace the render result of next ... | component/input/data sensitivity | p. 10 (4.2 RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce Flow Distillation Sampling (FDS), an online method for distilling matching prior from a pre-trained optical flow model into the ... | We found that Sea Raft (Wang et al., 2024) outperforms Raft (Teed and Deng, 2020) on FDS, indicating that a better optical flow model ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | From the results, it can be seen that depth order information provided by monocular depth improves reconstruction accuracy. | numeric claim only at cited anchor | p. 9 (4.2 RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We select 5 scenes from the ScanNet (V2) 7

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to the significant movement between images, the Prior Flow fails to accurately match the pixel between them, leading to a further degradation in ... | p. 10 (4.2 RESULTS) |
| body limitation/failure cue | The multi-view depth prior, hindered by the limited feature overlap between input views, fails to offer reliable geometric information. | p. 9 (4.2 RESULTS) |
| body limitation/failure cue | 4.4 LIMITATION AND FURTHER WORK Firstly, our FDS faces challenges in scenes with significant lighting variations between different views, as shown in the lamp ... | p. 10 (4.2 RESULTS) |
| body limitation/failure cue | We removed the depth distortion loss in 2DGS because we found that it degrades its results in indoor scenes. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | This demonstrates the robustness and effectiveness of the FDS method across different datasets. | p. 8 (4.2 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| On the Mushroom dataset, adding the FDS loss increases the training time by half an hour, which maintains the same level as baseline. | p. 8 (4.2 RESULTS) |
| The entire framework is implemented in PyTorch (Paszke et al., 2019), and all experiments are conducted on a single NVIDIA 4090D GPU. | p. 7 (4 EXPERIMENTS) |
| 4.1 SETUPS 4.1.1 IMPLEMENTATION DETAILS We apply our FDS method to two types of 3DGS: the original 3DGS, and 2DGS (Huang et al., 2024). | p. 7 (4 EXPERIMENTS) |
| Interpretive Experiments: To demonstrate the mutual refinement of two flows in our FDS, for each view, we sample the unobserved views multiple times to ... | p. 10 (4.2 RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4.2 RESULTS - extractive body cue:** Due to the significant movement between images, the Prior Flow fails to accurately match the pixel between them, leading to a further degradation in geometric ...
- **p. 9 / 4.2 RESULTS - extractive body cue:** The multi-view depth prior, hindered by the limited feature overlap between input views, fails to offer reliable geometric information.
- **p. 10 / 4.2 RESULTS - extractive body cue:** 4.4 LIMITATION AND FURTHER WORK Firstly, our FDS faces challenges in scenes with significant lighting variations between different views, as shown in the lamp of ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We removed the depth distortion loss in 2DGS because we found that it degrades its results in indoor scenes.
- **p. 8 / 4.2 RESULTS - extractive body cue:** This demonstrates the robustness and effectiveness of the FDS method across different datasets.

- **Evidence anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS), metrics p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 7 (4 EXPERIMENTS), baselines p. 9 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption), results p. 8 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 8 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
