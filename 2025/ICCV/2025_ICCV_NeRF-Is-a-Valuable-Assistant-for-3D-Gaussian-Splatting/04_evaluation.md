# Evaluation - NeRF Is a Valuable Assistant for 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (5.2. Comparison), p. 5 (5.2. Comparison), p. 8 (5.4. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (5.2. Comparison), p. 8 (5.4. Ablation Studies)): Notably, compared to other methods that incorporate NeRF-like concepts, such as VDGS and Hash-GS, NeRF-GS achieves even more substantial improvements.

## Evaluation Body Digest

- **p. 5 / 5.1. Implementation Details - extractive body cue:** We report experimental results on real-world datasets, including Mip-NeRF360 (all 9 scenes) [5], Tanks&Temples [29] DeepBlending [23], and the Blender dataset [41].
- **p. 5 / 5.1. Implementation Details - extractive body cue:** Joint training iterates 30k for full-view datasets and 8k for sparse-view scenes.
- **p. 6 / 5.2. Comparison - extractive body cue:** Qualitative comparison on real-world datasets.
- **p. 6 / 5.2. Comparison - extractive body cue:** Additionally, the collaborative optimization between NeRF and GS branches, facilitated by this shared information, creates mutual constraints and regularization effects, mitigating overfitting, which is crucial ...
- **p. 7 / 5.2. Comparison - extractive body cue:** Qualitative comparison under 12 input views on the Blender dataset.
- **p. 7 / 5.2. Comparison - extractive body cue:** Impact of feature share and joint optimization on sparse view scenes.
- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive body cue:** Ablation of different components in NeRF-GS on Tank&Temples and DeepBlending datasets.
- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive body cue:** For example, on the DeepBlending dataset, vanilla 3DGS uses 2,461,023 Gaussians, while ours uses only 1,926,336.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, compared to other methods that incorporate NeRF-like concepts, such as VDGS and Hash-GS, NeRF-GS achieves even more substantial improvements. | p. 5 (5.2. Comparison) |
| 5.2. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Comparative results are shown in Table 1, where our approach significantly outperforms the vanilla 3DGS model and other state-of-the-art methods across PSNR, SSIM, and ... | p. 5 (5.2. Comparison) |
| 5.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | The ablation results in Table 4 indicate that our proposed initialization significantly outperforms the alternatives. | p. 8 (5.4. Ablation Studies) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. NeRF-GS establishes a bridge of communication be- tween NeRF and 3DGS, leveraging information sharing, modeling of distinct characteristics, and joint optimization to ... | p. 1 (Figure/Table caption) |
| 5.2. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Remarkably, NeRF-GS achieves performance comparable to or even surpassing the SplatField method, which is specifically designed for sparse-view set26235 | p. 6 (5.2. Comparison) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Implementation Details - extractive body cue:** We report experimental results on real-world datasets, including Mip-NeRF360 (all 9 scenes) [5], Tanks&Temples [29] DeepBlending [23], and the Blender dataset [41].
- **p. 5 / 5.1. Implementation Details - extractive body cue:** Joint training iterates 30k for full-view datasets and 8k for sparse-view scenes.
- **p. 6 / 5.2. Comparison - extractive body cue:** Qualitative comparison on real-world datasets.
- **p. 6 / 5.2. Comparison - extractive body cue:** Additionally, the collaborative optimization between NeRF and GS branches, facilitated by this shared information, creates mutual constraints and regularization effects, mitigating overfitting, which is crucial ...
- **p. 7 / 5.2. Comparison - extractive body cue:** Qualitative comparison under 12 input views on the Blender dataset.
- **p. 7 / 5.2. Comparison - extractive body cue:** Impact of feature share and joint optimization on sparse view scenes.
- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive body cue:** Ablation of different components in NeRF-GS on Tank&Temples and DeepBlending datasets.
- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive body cue:** For example, on the DeepBlending dataset, vanilla 3DGS uses 2,461,023 Gaussians, while ours uses only 1,926,336.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. NeRF-GS establishes a bridge of communication be- tween NeRF and 3DGS, leveraging information sharing, modeling of distinct characteristics, and joint optimization to enable ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of NeRF-GS. (a) We first pretrain a Hash-based NeRF network to acquire continuous spatial encoding capabilities and implicit scene representation. (b) Utilizing ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison on real-world datasets. Colors denote the 1st , 2nd , and 3rd best-performing model.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison on real-world datasets. The numbers indicate the PSNR. Our method demonstrates a significant advantage over 3DGS and its variants, achieving a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparison under 12 input views on the Blender dataset. The numbers indicate the PSNR.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison of using different numbers of input views on Blender dataset. Our NeRF-GS maintains high performance when the scene input views are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Impact of feature share and joint optimization on sparse view scenes. These two key designs enable mutual regular- ization constraints between NeRF and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Comparison of model efficiency with 3DGS. We report the FPS, model size (MB), training time (minutes) and PSNR. The 3DGSL denotes longer iterative ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We report experimental results on real-world datasets, including Mip-NeRF360 (all 9 scenes) [5], Tanks&Temples [29] DeepBlending [23], and the Blender dataset [41]. | embodiment, simulator version and control stack | p. 5 (5.1. Implementation Details), p. 5 (5.1. Implementation Details) |
| Task/environment | Joint training iterates 30k for full-view datasets and 8k for sparse-view scenes. | reset, timeout, object/scene variation | p. 5 (5.1. Implementation Details), p. 6 (5.2. Comparison) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (4.3. Joint Optimization in Dual-branch) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Errors introduced during NeRF pre-training and inherent disparities between NeRF and 3DGS can impede the GS branch's ability to effectively model a 3D scene ... | definition/direction/unit from same section | p. 7 (5.3. Qualitative Analysis of NeRF-GS) |
| In contrast, previous methods such as Scaffold-GS, Hash-GS and VDGS that merely incorporate NeRF characteristics overlooked this distinction, thereby offering limited performance improvement. | definition/direction/unit from same section | p. 8 (5.4. Ablation Studies) |
| Joint training iterates 30k for full-view datasets and 8k for sparse-view scenes. | definition/direction/unit from same section | p. 5 (5.1. Implementation Details) |
| Notably, compared to other methods that incorporate NeRF-like concepts, such as VDGS and Hash-GS, NeRF-GS achieves even more substantial improvements. | definition/direction/unit from same section | p. 5 (5.2. Comparison) |
| Remarkably, NeRF-GS achieves performance comparable to or even surpassing the SplatField method, which is specifically designed for sparse-view set26235 | definition/direction/unit from same section | p. 6 (5.2. Comparison) |
| Our method demonstrates a significant advantage over 3DGS and its variants, achieving a more faithful representation of scene details. validating NeRF-GS as a robust ... | definition/direction/unit from same section | p. 6 (5.2. Comparison) |
| Our NeRF-GS maintains high performance when the scene input views are reduced. | definition/direction/unit from same section | p. 7 (5.2. Comparison) |
| Impact of Joint Optimization Strategy. | definition/direction/unit from same section | p. 8 (5.4. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparative results are shown in Table 1, where our approach significantly outperforms the vanilla 3DGS model and other state-of-the-art methods across PSNR, SSIM, and ... | comparison identity and matched condition | p. 5 (5.2. Comparison) |
| We conduct extensive quantitative and qualitative comparisons with state-of-the-art methods on both full and sparse datasets. | comparison identity and matched condition | p. 5 (5.2. Comparison) |
| To validate this, we perform sparse-view comparisons with baseline methods, as shown in Table 2. | comparison identity and matched condition | p. 6 (5.2. Comparison) |
| The ablation results in Table 4 indicate that our proposed initialization significantly outperforms the alternatives. | comparison identity and matched condition | p. 8 (5.4. Ablation Studies) |
| Across various sparsity levels, NeRF-GS consistently surpasses corresponding baselines. | comparison identity and matched condition | p. 6 (5.2. Comparison) |
| Furthermore, it can be observed that the performance gap between NeRF-GS and baseline methods in sparse views is more pronounced than in full views, ... | comparison identity and matched condition | p. 7 (5.2. Comparison) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation of different components in NeRF-GS on Tank&Temples and DeepBlending datasets. | component/input/data sensitivity | p. 8 (5.3. Qualitative Analysis of NeRF-GS) |
| Moreover, to examine the effect of feature sharing, we directly train the GS branch with learnable feature parameters, remarked as ‘w/o Feature Share'. | component/input/data sensitivity | p. 8 (5.4. Ablation Studies) |
| Our method is focused on enhancing GS branch performance, so we primarily compare it with 3DGS [27] and its variants, including C3DGS [44], Scaffold-GS ... | component/input/data sensitivity | p. 5 (5.1. Implementation Details) |
| Our method demonstrates a significant advantage over 3DGS and its variants, achieving a more faithful representation of scene details. validating NeRF-GS as a robust ... | component/input/data sensitivity | p. 6 (5.2. Comparison) |
| When associations between two branches are directly removed, such as feature sharing, loss constraints during joint training, etc., the NeRF-GS shows large visual quality ... | component/input/data sensitivity | p. 7 (5.3. Qualitative Analysis of NeRF-GS) |
| Figure 2. Overview of NeRF-GS. (a) We first pretrain a Hash-based NeRF network to acquire continuous spatial encoding capabilities and implicit scene representation. (b) ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF ... | Notably, compared to other methods that incorporate NeRF-like concepts, such as VDGS and Hash-GS, NeRF-GS achieves even more substantial improvements. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (5.2. Comparison), p. 5 (5.2. Comparison), p. 8 (5.4. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (5.2. Comparison), p. 8 (5.4. Ablation Studies) |
| Primary metric/result | Comparative results are shown in Table 1, where our approach significantly outperforms the vanilla 3DGS model and other state-of-the-art methods across PSNR, SSIM, and ... | numeric claim only at cited anchor | p. 5 (5.2. Comparison) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Implementation Details - extractive body cue:** During the NeRF branch pre-training, each batch contains 8,192 rays and is trained for 10 epochs.
- **p. 5 / 5.1. Implementation Details - extractive body cue:** For real-world datasets, we initialize using 1,000,000 points sampled at an 8:2 ratio from edge rays and random rays, while Blender datasets are initialized with ...
- **p. 5 / 5.1. Implementation Details - extractive body cue:** We report experimental results on real-world datasets, including Mip-NeRF360 (all 9 scenes) [5], Tanks&Temples [29] DeepBlending [23], and the Blender dataset [41].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These strategies effectively address several limitations of 3DGS, including initialization dependency, limited spatial awareness, insufficient Gaussian sphere correlation, and overfitting in sparse-view scenes. | p. 8 (7. Conclusion) |
| body limitation/failure cue | Our method demonstrates a significant advantage over 3DGS and its variants, achieving a more faithful representation of scene details. validating NeRF-GS as a robust ... | p. 6 (5.2. Comparison) |
| body limitation/failure cue | When associations between two branches are directly removed, such as feature sharing, loss constraints during joint training, etc., the NeRF-GS shows large visual quality ... | p. 7 (5.3. Qualitative Analysis of NeRF-GS) |
| body limitation/failure cue | Removing mutual constraints between branch outputs leads to performance degradation. | p. 8 (5.4. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additionally, we compare metrics for training time (minutes), storage size (MB), and rendering speed (FPS) to assess the model's compactness and efficiency. | p. 5 (5.1. Implementation Details) |
| We report the FPS, model size (MB), training time (minutes) and PSNR. | p. 7 (5.2. Comparison) |
| This suggests that integrating the NeRF branch is a worthwhile trade-off despite the increase in training time. | p. 8 (5.3. Qualitative Analysis of NeRF-GS) |
| We also compare it with an extendedtraining version of 3DGSL, showing NeRF-GS outperforms 3DGS even with similar training time. | p. 8 (5.3. Qualitative Analysis of NeRF-GS) |
| All experiments are conducted on an NVIDIA A100 GPU. | p. 5 (5.1. Implementation Details) |
| Through shared spatial positions and corresponding encoded features, different branches within NeRF-GS can more comprehensively perceive and learn from limited 3D scene information. | p. 6 (5.2. Comparison) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7. Conclusion - extractive body cue:** These strategies effectively address several limitations of 3DGS, including initialization dependency, limited spatial awareness, insufficient Gaussian sphere correlation, and overfitting in sparse-view scenes.
- **p. 6 / 5.2. Comparison - extractive body cue:** Our method demonstrates a significant advantage over 3DGS and its variants, achieving a more faithful representation of scene details. validating NeRF-GS as a robust framework ...
- **p. 7 / 5.3. Qualitative Analysis of NeRF-GS - extractive body cue:** When associations between two branches are directly removed, such as feature sharing, loss constraints during joint training, etc., the NeRF-GS shows large visual quality degradation.
- **p. 8 / 5.4. Ablation Studies - extractive body cue:** Removing mutual constraints between branch outputs leads to performance degradation.

- **Evidence anchors reviewed:** datasets p. 5 (5.1. Implementation Details), p. 5 (5.1. Implementation Details), p. 6 (5.2. Comparison), p. 6 (5.2. Comparison), p. 7 (5.2. Comparison), p. 7 (5.2. Comparison), metrics p. 7 (5.3. Qualitative Analysis of NeRF-GS), p. 8 (5.4. Ablation Studies), p. 5 (5.1. Implementation Details), p. 5 (5.2. Comparison), p. 6 (5.2. Comparison), p. 6 (5.2. Comparison), baselines p. 5 (5.2. Comparison), p. 5 (5.2. Comparison), p. 6 (5.2. Comparison), p. 8 (5.4. Ablation Studies), p. 6 (5.2. Comparison), p. 7 (5.2. Comparison), results p. 5 (5.2. Comparison), p. 5 (5.2. Comparison), p. 8 (5.4. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (5.2. Comparison), p. 8 (5.4. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
