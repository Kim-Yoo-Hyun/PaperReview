# Evaluation - Taming Video Diffusion Prior with Scene-Grounding Guidance for 3D Gaussian Splatting from Sparse Inputs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhong_Taming_Video_Diffusion_Prior_with_Scene-Grounding_Guidance_for_3D_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhong_Taming_Video_Diffusion_Prior_with_Scene-Grounding_Guidance_for_3D_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Comparisons), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Setups)): 1, our method achieves the highest performance on the Replica dataset, outperforming DNGaussian [18] and FSGS [64] by a significant margin of over 3.0 dB in PSNR.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setups - extractive body cue:** A 3DGS model optimized with these sequences renders images with black shadows, highlighted by red boxes, while our method solves this issue with the scene-grounding ...
- **p. 6 / 4.2. Comparisons - extractive body cue:** ScanNet++ is a dataset captured in realistic scenes, so it is more complicated and chal6138
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Comparisons with inpainting methods on the Replica dataset. ∗indicates the usage of our trajectory initialization.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** We analyze their effects on the Replica dataset.
- **p. 7 / 4.2. Comparisons - extractive body cue:** Qualitative comparisons on the Replica and ScanNet++ datasets.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Ablation experiments on the Replica dataset.
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For quantitative comparisons, we report PSNR, SSIM [47], and LPIPS [62] scores.
- **p. 8 / 4.4. Further Comparisons with Inpainting Methods - extractive body cue:** Our approach not only produces more plausible appearances around the inpainting regions but also predicts more consistent geometries in fine-grained local areas. inpainting on hole ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setups (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparisons | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, our method achieves the highest performance on the Replica dataset, outperforming DNGaussian [18] and FSGS [64] by a significant margin of over 3.0 ... | p. 6 (4.2. Comparisons) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. Comparisons with inpainting methods on the Replica dataset. ∗indicates the usage of our trajectory initialization. Trajectory Initialization Strategy. Tab. 2 (a) further ... | p. 8 (Figure/Table caption) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2 (a), while the full image metrics are enhanced due to slightly improved modeling at occluded regions, the visual quality degrades, as indicated by ... | p. 7 (4.3. Ablation Studies) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, our scene-grounding guidance ensures that the generated sequences remain consistent, significantly enhancing the modeling capability in regions outside the field of view ... | p. 7 (4.3. Ablation Studies) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | We empirically find that local sampling brings improvement in Sec. | p. 8 (4.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setups - extractive body cue:** A 3DGS model optimized with these sequences renders images with black shadows, highlighted by red boxes, while our method solves this issue with the scene-grounding ...
- **p. 6 / 4.2. Comparisons - extractive body cue:** ScanNet++ is a dataset captured in realistic scenes, so it is more complicated and chal6138
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Comparisons with inpainting methods on the Replica dataset. ∗indicates the usage of our trajectory initialization.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** We analyze their effects on the Replica dataset.
- **p. 7 / 4.2. Comparisons - extractive body cue:** Qualitative comparisons on the Replica and ScanNet++ datasets.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Ablation experiments on the Replica dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We tackle the critical issues of (a) extrapolation and (b) occlusion in sparse-input 3DGS by leveraging a video diffusion model. Vanilla generation often ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Framework overview of our proposed method. It consists of three parts: scene-grounding guidance, trajectory initialization, and optimization scheme with generated sequences. Initially, a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of the proposed trajectory initialization strat- egy. The yellow parts represent unobserved regions. For each input view, we sample a set of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Sequences from the vanilla generation suffer from incon- sistencies. A 3DGS model optimized with these sequences renders images with black shadows, highlighted by ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparisons on the Replica and ScanNet++ datasets. All 3DGS-based methods are optimized using the initialized point cloud from DUSt3R [46]. Our method ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on the Replica and ScanNet++ datasets. Including our approach, 3DGS-based methods marked with ↕are initialized with the point cloud from DUSt3R ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Our method not only effectively addresses extrapola- tion and occlusion (red boxes), improving the overall quality (blue boxes), but also predicts more plausible ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation experiments on the Replica dataset. (a) Effectiveness of the proposed scene-grounding guidance (Guide.) for generation, and the trajectory initialization strategy (Traj.). (Gen.) ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | A 3DGS model optimized with these sequences renders images with black shadows, highlighted by red boxes, while our method solves this issue with the ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setups), p. 6 (4.2. Comparisons) |
| Task/environment | ScanNet++ is a dataset captured in realistic scenes, so it is more complicated and chal6138 | reset, timeout, object/scene variation | p. 6 (4.2. Comparisons), p. 8 (4.3. Ablation Studies) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.2. Generation via Scene-Grounding Guidance), p. 5 (3.4. 3DGS Optimization with Generation) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (3.4. 3DGS Optimization with Generation), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For quantitative comparisons, we report PSNR, SSIM [47], and LPIPS [62] scores. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setups) |
| Our approach not only produces more plausible appearances around the inpainting regions but also predicts more consistent geometries in fine-grained local areas. inpainting on ... | definition/direction/unit from same section | p. 8 (4.4. Further Comparisons with Inpainting Methods) |
| The perceptual loss for generated views greatly increases the modeling capability at hole regions. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| 5 illustrates that our method effectively addresses occlusion and extrapolation, while other 3DGS-based methods struggle with these challenges. | definition/direction/unit from same section | p. 6 (4.2. Comparisons) |
| 1 demonstrate that our method has a clear advantage over current approaches, surpassing FSGS by more than 2.5 dB in PSNR. | definition/direction/unit from same section | p. 7 (4.2. Comparisons) |
| This degradation is attributed to inconsistencies within generated sequences, which can result in black shadows in rendered images as illustrated in Fig. | definition/direction/unit from same section | p. 7 (4.3. Ablation Studies) |
| Figure 1. We tackle the critical issues of (a) extrapolation and (b) occlusion in sparse-input 3DGS by leveraging a video diffusion model. Vanilla generation ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Framework overview of our proposed method. It consists of three parts: scene-grounding guidance, trajectory initialization, and optimization scheme with generated sequences. Initially, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We train a baseline 3DGS model initialized with the point cloud from DUSt3R [46], incorporating the gaussian unpooling in FSGS [64], which makes the ... | comparison identity and matched condition | p. 6 (4.1. Experimental Setups) |
| Furthermore, the comparisons in the third row highlight our method's superiority in preserving finer details compared to all other methods. | comparison identity and matched condition | p. 7 (4.2. Comparisons) |
| The model is denoted as ‘Baseline 3DGS' in the following. | comparison identity and matched condition | p. 6 (4.1. Experimental Setups) |
| Baseline 3DGS Ours Ground Truth Figure 6. | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| 3 show that our method outperforms these two methods by more than 1.0 dB in PSNR. | comparison identity and matched condition | p. 8 (4.4. Further Comparisons with Inpainting Methods) |
| (b) Effectiveness of the proposed scheme for 3DGS optimization. w/ Guided Genration&Traj. w/ Perceptual Loss Baseline 3DGS Figure 7. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Ablation experiments on the Replica dataset. (a) Effectiveness of the proposed scene-grounding guidance (Guide.) for generation, and the trajectory initialization strategy (Traj.). ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Our technical contributions consist of three key components. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as: • This paper is the first to explicitly address the challenges of extrapolation and occlusion in 3DGS modeling from ... | 1, our method achieves the highest performance on the Replica dataset, outperforming DNGaussian [18] and FSGS [64] by a significant margin of over 3.0 ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Comparisons), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Setups) |
| Primary metric/result | Table 3. Comparisons with inpainting methods on the Replica dataset. ∗indicates the usage of our trajectory initialization. Trajectory Initialization Strategy. Tab. 2 (a) further ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** A 3DGS model optimized with these sequences renders images with black shadows, highlighted by red boxes, while our method solves this issue with the scene-grounding ...
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For sequence generation, we employ the camera-controlled image-to-video diffusion model [57] which supports the generation of L = 25 frames.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6. Our method not only effectively addresses extrapola- tion and occlusion (red boxes), improving the overall quality (blue boxes), but also predicts more ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | FreeNeRF [52] exhibits severe artifacts because it cannot effectively utilize the strong prior from the DUSt3R point cloud. | p. 6 (4.2. Comparisons) |
| body limitation/failure cue | In this paper, we have explored to address the critical issues of extrapolation and occlusion in sparse-input 3DGS modeling. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. We tackle the critical issues of (a) extrapolation and (b) occlusion in sparse-input 3DGS by leveraging a video diffusion model. Vanilla generation ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Moreover, the ‘inside-out' viewing directions make occlusion common in this benchmark. | p. 6 (4.1. Experimental Setups) |
| body limitation/failure cue | Our method effectively addresses the issues of extrapolation and occlusion while preserving finer details and reducing artifacts. | p. 7 (4.2. Comparisons) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3: Given: Latent image-to-video diffusion model ϵθ, VAE decoder D, pre-defined βt, ¯αt and guidance scale γt. | p. 4 (3.2. Generation via Scene-Grounding Guidance) |
| The sampling is conducted by iterative denoising for T steps [56] as follows: \la b el {eq:ddp m } \se tle ngth { \ ... | p. 4 (3.1. Preliminary) |
| (4)) as: \la be l {eq : g u i d e_ l oss} \s e tlength {\a b o v ed i s ... | p. 5 (3.2. Generation via Scene-Grounding Guidance) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Our method not only effectively addresses extrapola- tion and occlusion (red boxes), improving the overall quality (blue boxes), but also predicts more plausible ...
- **p. 6 / 4.2. Comparisons - extractive body cue:** FreeNeRF [52] exhibits severe artifacts because it cannot effectively utilize the strong prior from the DUSt3R point cloud.
- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we have explored to address the critical issues of extrapolation and occlusion in sparse-input 3DGS modeling.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We tackle the critical issues of (a) extrapolation and (b) occlusion in sparse-input 3DGS by leveraging a video diffusion model. Vanilla generation often ...
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** Moreover, the ‘inside-out' viewing directions make occlusion common in this benchmark.
- **p. 7 / 4.2. Comparisons - extractive body cue:** Our method effectively addresses the issues of extrapolation and occlusion while preserving finer details and reducing artifacts.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setups), p. 6 (4.2. Comparisons), p. 8 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), p. 7 (4.2. Comparisons), p. 8 (4.3. Ablation Studies), metrics p. 6 (4.1. Experimental Setups), p. 8 (4.4. Further Comparisons with Inpainting Methods), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Comparisons), p. 7 (4.2. Comparisons), p. 7 (4.3. Ablation Studies), baselines p. 6 (4.1. Experimental Setups), p. 7 (4.2. Comparisons), p. 6 (4.1. Experimental Setups), p. 7 (4.3. Ablation Studies), p. 8 (4.4. Further Comparisons with Inpainting Methods), p. 8 (4.3. Ablation Studies), results p. 6 (4.2. Comparisons), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Setups).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
