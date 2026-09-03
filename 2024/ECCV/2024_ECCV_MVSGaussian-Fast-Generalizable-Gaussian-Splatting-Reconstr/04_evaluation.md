# Evaluation - MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2662_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02662.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (Figure/Table caption), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 2 (Figure/Table caption), p. 11 (5 Experiments), p. 14 (5 Experiments)): Fig. 5: Qualitative comparison of rendering quality with state-of-the-art methods [6, 19, 22] after per-scene optimization. by the generalizable model and the effective aggregation strategy, we achieve op- timal performance ...

## Evaluation Body Digest

- **p. 11 / 5 Experiments - extractive body cue:** Additionally, it focuses on natural scenes with image pairs as input, and its performance significantly decreases when applied to object-centric datasets [1,29].
- **p. 10 / 5 Experiments - extractive body cue:** Following MVSNeRF [6], we train the generalizable model on the DTU training set [1] and evaluate it on the DTU test set.
- **p. 10 / 5 Experiments - extractive body cue:** Subsequently, we conduct further evaluations on the Real Forward-facing [28], NeRF Synthetic [29], and Tanks and Temples [21] datasets.
- **p. 11 / 5 Experiments - extractive body cue:** MVSGaussian 11 Table 2: Quantitative results of generalization on Real Forward-facing [28], NeRF Synthetic [29], and Tanks and Temples [21] datasets.
- **p. 12 / 5 Experiments - extractive body cue:** PSNRdtu, PSNRllff, PSNRnerf, and PSNRtnt are the PSNR metrics for different datasets [1,21,28,29].
- **p. 13 / 5 Experiments - extractive body cue:** Especially on the Real Forward-facing dataset, our method achieves superior performance with only 45 seconds of optimization, compared to 10 minutes for 3D-GS and 10 ...
- **p. 13 / 5 Experiments - extractive body cue:** Regarding color representation, we directly decode RGB values instead of spherical harmonic (SH) coefficients (No.5), as decoding coefficients may result in a degradation of generalization, ...
- **p. 14 / 5 Experiments - extractive body cue:** We report the quantitative results obtained with different strategies on the Real Forward-facing dataset [28].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Qualitative comparison of rendering quality with state-of-the-art methods [6, 19, 22] after per-scene optimization. by the generalizable model and the effective aggregation ... | p. 13 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | When optimizing the entire pipeline, our method can achieve better performance with faster inference speeds compared to previous generalizable NeRF methods, and results comparable ... | p. 12 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, optimizing only the Gaussians can significantly improve optimization and rendering speed because it eliminates the time-consuming feed-forward neural network. | p. 12 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1: Comparison with existing methods. (a) We present the generalizable re- sults on the Real Forward-facing dataset [28]. Compared with other competitors, our ... | p. 2 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Due to the MVS-based pixel-aligned Gaussian representation and the efficient hybrid Gaussian rendering, our method achieves optimal performance at a fast inference speed. | p. 11 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 11 / 5 Experiments - extractive body cue:** Additionally, it focuses on natural scenes with image pairs as input, and its performance significantly decreases when applied to object-centric datasets [1,29].
- **p. 10 / 5 Experiments - extractive body cue:** Following MVSNeRF [6], we train the generalizable model on the DTU training set [1] and evaluate it on the DTU test set.
- **p. 10 / 5 Experiments - extractive body cue:** Subsequently, we conduct further evaluations on the Real Forward-facing [28], NeRF Synthetic [29], and Tanks and Temples [21] datasets.
- **p. 11 / 5 Experiments - extractive body cue:** MVSGaussian 11 Table 2: Quantitative results of generalization on Real Forward-facing [28], NeRF Synthetic [29], and Tanks and Temples [21] datasets.
- **p. 12 / 5 Experiments - extractive body cue:** PSNRdtu, PSNRllff, PSNRnerf, and PSNRtnt are the PSNR metrics for different datasets [1,21,28,29].
- **p. 13 / 5 Experiments - extractive body cue:** Especially on the Real Forward-facing dataset, our method achieves superior performance with only 45 seconds of optimization, compared to 10 minutes for 3D-GS and 10 ...
- **p. 13 / 5 Experiments - extractive body cue:** Regarding color representation, we directly decode RGB values instead of spherical harmonic (SH) coefficients (No.5), as decoding coefficients may result in a degradation of generalization, ...
- **p. 14 / 5 Experiments - extractive body cue:** We report the quantitative results obtained with different strategies on the Real Forward-facing dataset [28].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Comparison with existing methods. (a) We present the generalizable re- sults on the Real Forward-facing dataset [28]. Compared with other competitors, our method ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of MVSGaussian. We first extract features {fi}N i=1 from input source views {Ii}N i=1 using FPN. These features are then aggregated into ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3: Consistent aggregation. With depth maps and point clouds produced by the generalizable model, we first conduct geometric consistency checks on depths to derive ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Quantitative results of generalization on the DTU test set [1]. FPS and Mem are measured under a 3-view input, while FPS∗and Mem∗are measured ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Quantitative results of generalization on Real Forward-facing [28], NeRF Synthetic [29], and Tanks and Temples [21] datasets. Due to the signif- icant memory ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Quantitative results after per-scene optimization. Timeft represents the time for fine-tuning. The best result is in bold, and second-best one is in underlined.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative comparison of rendering quality under generalization and 3-view settings with state-of-the-art methods [6, 9, 22].
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Ablation studies. The terms "gs" and "vr" represent Gaussian Splatting and volume rendering, respectively. PSNRdtu, PSNRllff, PSNRnerf, and PSNRtnt are the PSNR metrics ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Additionally, it focuses on natural scenes with image pairs as input, and its performance significantly decreases when applied to object-centric datasets [1,29]. | embodiment, simulator version and control stack | p. 11 (5 Experiments), p. 10 (5 Experiments) |
| Task/environment | Following MVSNeRF [6], we train the generalizable model on the DTU training set [1] and evaluate it on the DTU test set. | reset, timeout, object/scene variation | p. 10 (5 Experiments), p. 10 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (body section not recovered), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 5: Qualitative comparison of rendering quality with state-of-the-art methods [6, 19, 22] after per-scene optimization. by the generalizable model and the effective aggregation strategy, ... | definition/direction/unit from same section | p. 13 (5 Experiments) |
| Employing the consistency check strategy can further boost performance, as it filters out noisy points while preserving valid points. | definition/direction/unit from same section | p. 14 (5 Experiments) |
| Fig. 1: Comparison with existing methods. (a) We present the generalizable re- sults on the Real Forward-facing dataset [28]. Compared with other competitors, our ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| During the per-scene optimization stage, for fair comparison, our optimization strategy and hyperparameters settings remain consistent with the vanilla 3DGS [19], except for the ... | definition/direction/unit from same section | p. 10 (5 Experiments) |
| Additionally, it focuses on natural scenes with image pairs as input, and its performance significantly decreases when applied to object-centric datasets [1,29]. | definition/direction/unit from same section | p. 11 (5 Experiments) |
| For NeRF-based methods, ENeRF [22] enjoys promising speeds by sampling only 2 points per ray, however, its performance is limited and consumes higher memory ... | definition/direction/unit from same section | p. 11 (5 Experiments) |
| Moreover, performance can benefit from the adaptive density control module described in Sec. | definition/direction/unit from same section | p. 12 (5 Experiments) |
| For per-scene optimization, one strategy is to optimize the entire pipeline, similar to NeRF-based methods. | definition/direction/unit from same section | p. 12 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Qualitative comparison of rendering quality with state-of-the-art methods [6, 19, 22] after per-scene optimization. by the generalizable model and the effective aggregation ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| 4: Qualitative comparison of rendering quality under generalization and 3-view settings with state-of-the-art methods [6, 9, 22]. | comparison identity and matched condition | p. 12 (5 Experiments) |
| Fig. 1: Comparison with existing methods. (a) We present the generalizable re- sults on the Real Forward-facing dataset [28]. Compared with other competitors, our ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| We compare our method with state-of-the-art generalizable NeRF methods [6,9,22,40,54], as well as the recent generalizable Gaussian method [4]. | comparison identity and matched condition | p. 10 (5 Experiments) |
| When optimizing the entire pipeline, our method can achieve better performance with faster inference speeds compared to previous generalizable NeRF methods, and results comparable ... | comparison identity and matched condition | p. 12 (5 Experiments) |
| Additionally, adopting the hybrid Gaussian rendering approach (No.4) notably enhances performance compared to utilizing splatting (No.2) or volume rendering (No.3) alone. | comparison identity and matched condition | p. 13 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| As shown in Table 4, we conduct ablation studies to evaluate the effectiveness of our designs. | component/input/data sensitivity | p. 13 (5 Experiments) |
| 5.4 Ablations and Analysis Ablation studies. | component/input/data sensitivity | p. 13 (5 Experiments) |
| Table 4: Ablation studies. The terms "gs" and "vr" represent Gaussian Splatting and volume rendering, respectively. PSNRdtu, PSNRllff, PSNRnerf, and PSNRtnt are the PSNR ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Timeft represents the time for fine-tuning. | component/input/data sensitivity | p. 11 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Liu et al. - We present MVSGaussian, a generalizable Gaussian Splatting method derived from Multi-View Stereo and a pixel-aligned Gaussian representation. - We further ... | Fig. 5: Qualitative comparison of rendering quality with state-of-the-art methods [6, 19, 22] after per-scene optimization. by the generalizable model and the effective aggregation ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (Figure/Table caption), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 2 (Figure/Table caption), p. 11 (5 Experiments), p. 14 (5 Experiments) |
| Primary metric/result | When optimizing the entire pipeline, our method can achieve better performance with faster inference speeds compared to previous generalizable NeRF methods, and results comparable ... | numeric claim only at cited anchor | p. 12 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 5 Experiments - extractive body cue:** The generalizable model is trained using the Adam optimizer [20] on four RTX 3090 GPUs.
- **p. 11 / 5 Experiments - extractive body cue:** For NeRF-based methods, ENeRF [22] enjoys promising speeds by sampling only 2 points per ray, however, its performance is limited and consumes higher memory overhead.
- **p. 13 / 5 Experiments - extractive body cue:** Especially on the Real Forward-facing dataset, our method achieves superior performance with only 45 seconds of optimization, compared to 10 minutes for 3D-GS and 10 ...
- **p. 14 / 5 Experiments - extractive body cue:** Aggregation PSNR ↑ SSIM ↑ LPIPS ↓ Timeft ↓ FPS ↑ direct concatenation 26.18 0.901 0.122 90s 220 downsampling 26.72 0.909 0.121 60s 340 consistency ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo Tianqi Liu1 , Guangcong Wang2,3 , Shoukang Hu2 , Liao Shen1 , Xinyi Ye1 , Yuhang ...
- **p. 2 / 1 Introduction - extractive body cue:** 0 0.5 10 20 21 22 23 24 25 PSNR ↑ IBRNet (0.1, 21.79) MVSNeRF (0.2, 21.93) MatchNeRF (0.5, 22.43) ENeRF (11.7, 23.63) Ours (14.1, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As our method relies on MVS for depth estimation, it inherits limitations from MVS, such as decreased depth accuracy in areas with weak textures ... | p. 14 (6 Conclusion) |
| body limitation/failure cue | The remaining methods render images by sampling rays due to their high memory consumption, as they cannot process the entire image at once. | p. 11 (5 Experiments) |
| body limitation/failure cue | When optimizing the entire pipeline, our method can achieve better performance with faster inference speeds compared to previous generalizable NeRF methods, and results comparable ... | p. 12 (5 Experiments) |
| body limitation/failure cue | Regarding color representation, we directly decode RGB values instead of spherical harmonic (SH) coefficients (No.5), as decoding coefficients may result in a degradation of ... | p. 13 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For [22] and [4], we evaluate them using their officially released code and pre-trained models. | p. 10 (5 Experiments) |
| During the per-scene optimization stage, for fair comparison, our optimization strategy and hyperparameters settings remain consistent with the vanilla 3DGS [19], except for the ... | p. 10 (5 Experiments) |
| Regarding color representation, we directly decode RGB values instead of spherical harmonic (SH) coefficients (No.5), as decoding coefficients may result in a degradation of ... | p. 13 (5 Experiments) |
| Specifically, 1) we leverage MVS to encode geometry-aware Gaussian representations and decode them into Gaussian parameters. | p. 1 (body section not recovered) |
| PixelSplat [4] leverages an epipolar Transformer [37] to address scale ambiguity and encode features. | p. 2 (1 Introduction) |
| Second, with the encoded point-wise features, we can decode them into Gaussian parameters through an MLP. | p. 3 (1 Introduction) |
| On a single RTX 3090 GPU, compared with the vanilla 3D-GS, our proposed method achieves better novel view synthesis with similar rendering speed (300+ ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 6 Conclusion - extractive body cue:** As our method relies on MVS for depth estimation, it inherits limitations from MVS, such as decreased depth accuracy in areas with weak textures or ...
- **p. 11 / 5 Experiments - extractive body cue:** The remaining methods render images by sampling rays due to their high memory consumption, as they cannot process the entire image at once.
- **p. 12 / 5 Experiments - extractive body cue:** When optimizing the entire pipeline, our method can achieve better performance with faster inference speeds compared to previous generalizable NeRF methods, and results comparable to ...
- **p. 13 / 5 Experiments - extractive body cue:** Regarding color representation, we directly decode RGB values instead of spherical harmonic (SH) coefficients (No.5), as decoding coefficients may result in a degradation of generalization, ...

- **Evidence anchors reviewed:** datasets p. 11 (5 Experiments), p. 10 (5 Experiments), p. 10 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 13 (5 Experiments), metrics p. 13 (5 Experiments), p. 14 (5 Experiments), p. 2 (Figure/Table caption), p. 10 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), baselines p. 13 (Figure/Table caption), p. 12 (5 Experiments), p. 2 (Figure/Table caption), p. 10 (5 Experiments), p. 12 (5 Experiments), p. 13 (5 Experiments), results p. 13 (Figure/Table caption), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 2 (Figure/Table caption), p. 11 (5 Experiments), p. 14 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
