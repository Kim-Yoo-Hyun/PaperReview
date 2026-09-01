# Evaluation - SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9NfHbWKqMF; PDF retrieval source: https://openreview.net/pdf/b05fcaaffbc6f81e70f605c033bb30f44fe43513.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 2 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS)): While our method still faces challenges with high-frequency texture details, it outperforms previous approaches in terms of fidelity and consistency in out-of-distribution views, which is also supported by the clear ...

## Evaluation Body Digest

- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** SplatFormer trained on Objaverse successfully mitigates artifacts in OOD views in the GSO (Downs et al., 2022) dataset and our real-world object-centric captures.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** Even on the real-world dataset, despite being trained exclusively on synthetic data, SplatFormer reduces artifacts.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We select common objects and scenes with meaningful topdown views, such as city streets and buildings, avoiding those with large cavities that are invisible from ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Next, we present the results on OOD-NVS, crossdataset generalization, and ablation studies.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** H.1 using the MVImgNet dataset (Yu et al., 2023), and outline both the potential and challenges.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive PDF cue:** Since object-centric scenes often possess concentrated spatial distribution, our current SplatFormer can be quite efficient for large-scale 3DGS during inference.
- **p. 16 / B IMPLEMENTATION DETAILS - extractive PDF cue:** It takes 2 days to generate each training dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 8); A EVALUATION DATASETS (p. 15); B IMPLEMENTATION DETAILS (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While our method still faces challenges with high-frequency texture details, it outperforms previous approaches in terms of fidelity and consistency in out-of-distribution views, which ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Published as a conference paper at ICLR 2025 On the GSO-OOD evaluation set, SplatFormer achieves substantial improvements in both metrics and visual quality. | p. 10 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3, while 2D denoising methods improve the original 3DGS, they significantly underperform compared to SplatFormer and fail to recover geometric details. | p. 10 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: We investigate the out-of-distribution (OOD) novel view synthesis (NVS), where test views significantly differ from input views. This scenario contrasts with prior ... | p. 2 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While 3DGS performance degrades significantly as the viewing angle deviates from the input views, our method provides more robust synthesis for target views in ... | p. 9 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** SplatFormer trained on Objaverse successfully mitigates artifacts in OOD views in the GSO (Downs et al., 2022) dataset and our real-world object-centric captures.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** Even on the real-world dataset, despite being trained exclusively on synthetic data, SplatFormer reduces artifacts.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We select common objects and scenes with meaningful topdown views, such as city streets and buildings, avoiding those with large cavities that are invisible from ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Next, we present the results on OOD-NVS, crossdataset generalization, and ablation studies.
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** H.1 using the MVImgNet dataset (Yu et al., 2023), and outline both the potential and challenges.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive PDF cue:** Since object-centric scenes often possess concentrated spatial distribution, our current SplatFormer can be quite efficient for large-scale 3DGS during inference.
- **p. 16 / B IMPLEMENTATION DETAILS - extractive PDF cue:** It takes 2 days to generate each training dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: We investigate the out-of-distribution (OOD) novel view synthesis (NVS), where test views significantly differ from input views. This scenario contrasts with prior in-distribution ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via 3DGS significantly deteriorates as the test camera ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Method Overview. We introduce SplatFormer, a generalizable 3D point transformer network designed for feed-forward refinement of Gaussian splats, enabling robust out-of-distribution novel-view synthesis ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: OOD-NVS. Comparisons on the ShapeNet-OOD and Objaverse-OOD evaluation sets. The metric is evaluated on OOD test views with elevation ϕood ≥70◦; colors indicate ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Novel View Synthesis under Out-of-Distribution Camera Angles. The first column shows 4 out of 32 input views. Here, we compare our method with ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Cross-dataset Generalization. SplatFormer trained on Objaverse successfully mitigates artifacts in OOD views in the GSO (Downs et al., 2022) dataset and our real-world ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Cross-dataset Generalization Methods GSO-OOD RealWorld-OOD PSNR SSIM LPIPS PSNR SSIM LPIPS Nerfbusters 15.95 0.678 0.300 23.93 0.893 0.114 2DGS
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 3: SplatFormer vs 2D Denoising ShapeNet-OOD

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes. | embodiment, simulator version and control stack | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Task/environment | SplatFormer trained on Objaverse successfully mitigates artifacts in OOD views in the GSO (Downs et al., 2022) dataset and our real-world object-centric captures. | reset, timeout, object/scene variation | p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 16 (B IMPLEMENTATION DETAILS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To demonstrate this, we evaluate NVS with elevations ϕ ∈[10◦, 90◦] in Objaverse-OOD scenes and compare SplatFormer to 3DGS (Fig. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| SplatFormer trained on Objaverse successfully mitigates artifacts in OOD views in the GSO (Downs et al., 2022) dataset and our real-world object-centric captures. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| An alternative strategy for refining OOD-NVS renderings is to use 2D image restoration methods. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Additionally, to validate the effectiveness of the residual prediction strategy outlined in Sec. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 3: Method Overview. We introduce SplatFormer, a generalizable 3D point transformer network designed for feed-forward refinement of Gaussian splats, enabling robust out-of-distribution novel-view ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 1: We investigate the out-of-distribution (OOD) novel view synthesis (NVS), where test views significantly differ from input views. This scenario contrasts with prior ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via 3DGS significantly deteriorates as the test ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and ... | definition/direction/unit from same section | p. 15 (B IMPLEMENTATION DETAILS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method also outperforms MipNeRF360 and 2DGS, the best-performing baselines in Objaverse-OOD (Tab. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| First, despite outperforming all the considered baselines, it still struggles to reconstruct fine-grained details and complex texture. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| We begin by outlining our experimental setup, followed by a description of the evaluation protocol and the baseline methods used for comparison. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| For LaRa, which is limited to four input views due to memory constraints, we chose four large-baseline views to maximize scene coverage. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| While our method still faces challenges with high-frequency texture details, it outperforms previous approaches in terms of fidelity and consistency in out-of-distribution views, which ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Figure 1: We investigate the out-of-distribution (OOD) novel view synthesis (NVS), where test views significantly differ from input views. This scenario contrasts with prior ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Next, we examine regularized 3DGS variants without external priors, including 2DGS (Huang et al., 2024a) and SplatFields (Mihajlovic et al., 2024). | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| These improvements are reflected in the SSIM and LPIPS metrics, though we observed rather minimal improvements in PSNR, which we attribute to the pixelwise ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| 4, we train a variant that directly predicts the full 3DGS attributes (direct component). | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Next, we present the results on OOD-NVS, crossdataset generalization, and ablation studies. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods ... | While our method still faces challenges with high-frequency texture details, it outperforms previous approaches in terms of fidelity and consistency in out-of-distribution views, which ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 2 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Primary metric/result | Published as a conference paper at ICLR 2025 On the GSO-OOD evaluation set, SplatFormer achieves substantial improvements in both metrics and visual quality. | numeric claim only at cited anchor | p. 10 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** As visualized in Fig 1, for a centered object, we simulate an input camera capturing 360degree azimuths at low elevations.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We use Blender to render 20 objects from ShapeNet (Chang et al., 2015) and Objaverse-v1 (Deitke et al., 2023) each.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive PDF cue:** Regarding SplatFormer's inference efficiency, most input splats in our object-centric test sets contain 70k-100k gaussians, requiring only 900MB of GPU memory for one feed-forward inference ...
- **p. 17 / B IMPLEMENTATION DETAILS - extractive PDF cue:** We find that an RTX 4090 GPU can accommodate up to 4 million Gaussians.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive PDF cue:** Regarding SplatFormer's inference efficiency, most input splats in our object-centric test sets contain 70k-100k gaussians, requiring only 900MB of GPU memory for one feed-forward inference ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using ... | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | Our method has several limitations that provide directions for future work. | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via 3DGS significantly deteriorates as the test ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Finally, we discuss the limitations of our approach and potential directions for future research. | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | Figure 3: Method Overview. We introduce SplatFormer, a generalizable 3D point transformer network designed for feed-forward refinement of Gaussian splats, enabling robust out-of-distribution novel-view ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | While 3DGS performance degrades significantly as the viewing angle deviates from the input views, our method provides more robust synthesis for target views in ... | p. 9 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Regarding SplatFormer's inference efficiency, most input splats in our object-centric test sets contain 70k-100k gaussians, requiring only 900MB of GPU memory for one feed-forward ... | p. 17 (B IMPLEMENTATION DETAILS) |
| For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train ... | p. 16 (B IMPLEMENTATION DETAILS) |
| We use Adam optimizer with a constant learning rate of 3e-5. | p. 16 (B IMPLEMENTATION DETAILS) |
| The point transformer encoder begins with an MLP embedding layer, followed by five down-pooling and four up-pooling stages, ultimately producing features with a dimensionality ... | p. 15 (B IMPLEMENTATION DETAILS) |
| The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and ... | p. 15 (B IMPLEMENTATION DETAILS) |
| We find that an RTX 4090 GPU can accommodate up to 4 million Gaussians. | p. 17 (B IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 CONCLUSION - extractive PDF cue:** In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** Our method has several limitations that provide directions for future work.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via 3DGS significantly deteriorates as the test camera ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Finally, we discuss the limitations of our approach and potential directions for future research.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Method Overview. We introduce SplatFormer, a generalizable 3D point transformer network designed for feed-forward refinement of Gaussian splats, enabling robust out-of-distribution novel-view synthesis ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** While 3DGS performance degrades significantly as the viewing angle deviates from the input views, our method provides more robust synthesis for target views in the ...

- **PDF anchors reviewed:** datasets p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), metrics p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 2 (Figure/Table caption), results p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 2 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
