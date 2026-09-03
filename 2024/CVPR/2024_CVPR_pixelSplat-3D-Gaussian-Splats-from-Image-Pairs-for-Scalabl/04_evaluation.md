# Evaluation - pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Results), p. 8 (5.3. Ablations and Analysis), p. 6 (Figure/Table caption), p. 8 (5.3. Ablations and Analysis)): Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS).

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** Both datasets include camera poses computed by SfM software, necessitating the scale-aware design discussed in Section 4.1.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To present a fair comparison, we retrained these baselines by combining their publicly available codebases with our datasets and our method's data loaders.
- **p. 7 / 5.2. Results - extractive body cue:** Qualitative comparison of novel views on the RealEstate10k (top) and ACID (bottom) test sets.
- **p. 8 / 5.3. Ablations and Analysis - extractive body cue:** This highlights that beyond simply detecting correspondence, our encoder uses the scene-scale encoded depths it triangulates to resolve scale ambiguity.
- **p. 8 / 5.3. Ablations and Analysis - extractive body cue:** In Figure 6, we visualize epipolar attention scores, demonstrating that our epipolar transformer successfully discovers cross-view correspondences.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We train our model to minimize a combination of MSE and LPIPS losses using the Adam optimizer [20].
- **p. 6 / 5.2. Results - extractive body cue:** Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS).
- **p. 7 / 5.2. Results - extractive body cue:** Compared to the baselines, our approach not only produces more accurate and perceptually appealing images, but also generalizes better to out-of-distribution examples like the creek ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS). | p. 6 (5.2. Results) |
| 5.3. Ablations and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Qualitatively, this produces ghosting and motion blur artifacts that are evidence of incorrect depth predictions; quantitatively, performance drops significantly. | p. 8 (5.3. Ablations and Analysis) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Quantitative comparisons. We outperform all baseline methods in terms PSNR, LPIPS, and SSIM for novel view synthesis on the real-world RealEstate10k and ... | p. 6 (Figure/Table caption) |
| 5.3. Ablations and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Figure 6, we visualize epipolar attention scores, demonstrating that our epipolar transformer successfully discovers cross-view correspondences. | p. 8 (5.3. Ablations and Analysis) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** Both datasets include camera poses computed by SfM software, necessitating the scale-aware design discussed in Section 4.1.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To present a fair comparison, we retrained these baselines by combining their publicly available codebases with our datasets and our method's data loaders.
- **p. 7 / 5.2. Results - extractive body cue:** Qualitative comparison of novel views on the RealEstate10k (top) and ACID (bottom) test sets.
- **p. 8 / 5.3. Ablations and Analysis - extractive body cue:** This highlights that beyond simply detecting correspondence, our encoder uses the scene-scale encoded depths it triangulates to resolve scale ambiguity.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview. Given a pair of input images, pixelSplat recon- structs a 3D radiance field parameterized via 3D Gaussian primi- tives. This yields an ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Scale ambiguity. SfM does not reconstruct camera poses in real-world, metric scale-poses are scaled by an arbitrary scale factor that is different for ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Proposed probabilistic prediction of pixel-aligned Gaussians. For every pixel feature F[u] in the input feature map, a neural network f predicts Gaussian primitive ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. 3D Gaussians (top) and corresponding depth maps (bottom) predicted by our method. In contrast to light field rendering methods like GPNR [47] and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons. We outperform all baseline methods in terms PSNR, LPIPS, and SSIM for novel view synthesis on the real-world RealEstate10k and ACID ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparison of novel views on the RealEstate10k (top) and ACID (bottom) test sets. Compared to the baselines, our approach not only produces ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Attention visualization. We visualize the epipolar cross- attention weights between the rays on the left and the corresponding epipolar lines on the right ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. Ablating epipolar encoding (Q1a). To measure our epipolar encoding scheme's importance, we compare pixelSplat to a variant (No Epipolar Encoder) that eschews epipolar ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Both datasets include camera poses computed by SfM software, necessitating the scale-aware design discussed in Section 4.1. | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |
| Task/environment | To present a fair comparison, we retrained these baselines by combining their publicly available codebases with our datasets and our method's data loaders. | reset, timeout, object/scene variation | p. 6 (5.1. Experimental Setup), p. 7 (5.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4.1. Resolving Scale Ambiguity), p. 3 (4.1. Resolving Scale Ambiguity) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Figure 6, we visualize epipolar attention scores, demonstrating that our epipolar transformer successfully discovers cross-view correspondences. | definition/direction/unit from same section | p. 8 (5.3. Ablations and Analysis) |
| We train our model to minimize a combination of MSE and LPIPS losses using the Adam optimizer [20]. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS). | definition/direction/unit from same section | p. 6 (5.2. Results) |
| Compared to the baselines, our approach not only produces more accurate and perceptually appealing images, but also generalizes better to out-of-distribution examples like the ... | definition/direction/unit from same section | p. 7 (5.2. Results) |
| This leads to a performance drop of ≈1dB PSNR. | definition/direction/unit from same section | p. 8 (5.3. Ablations and Analysis) |
| Figure 2. Scale ambiguity. SfM does not reconstruct camera poses in real-world, metric scale-poses are scaled by an arbitrary scale factor that is different ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Proposed probabilistic prediction of pixel-aligned Gaussians. For every pixel feature F[u] in the input feature map, a neural network f predicts Gaussian ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Because the prior state-of-the-art wide-baseline novel view synthesis model by Du et al. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS). | comparison identity and matched condition | p. 6 (5.2. Results) |
| Compared to the baselines, our approach not only produces more accurate and perceptually appealing images, but also generalizes better to out-of-distribution examples like the ... | comparison identity and matched condition | p. 7 (5.2. Results) |
| Figure 2. Scale ambiguity. SfM does not reconstruct camera poses in real-world, metric scale-poses are scaled by an arbitrary scale factor that is different ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Qualitative comparison of novel views on the RealEstate10k (top) and ACID (bottom) test sets. | comparison identity and matched condition | p. 7 (5.2. Results) |
| To investigate whether predicting the depth of a Gaussian probabilistically is necessary, we perform an ablation (No Probabilistic Prediction) which directly regresses the depth, ... | comparison identity and matched condition | p. 8 (5.3. Ablations and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 7. Ablations. Without the epipolar transformer, our model is unable to resolve scale ambiguity, leading to ghosting artifacts. Without our sampling approach, our ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| For the "Plus Depth Regularization" ablation, we regularize depth maps by fine-tuning with 50,000 steps of edge-aware total variation regularization. | component/input/data sensitivity | p. 6 (5.1. Experimental Setup) |
| In this section, we describe our experimental setup, evaluate our method on wide-baseline novel view synthesis from image pairs, and perform ablations to validate ... | component/input/data sensitivity | p. 6 (5. Experiments) |
| We perform ablations on RealEstate10k to answer the following questions: • Question 1a: Is our epipolar encoder responsible for our model's ability to handle ... | component/input/data sensitivity | p. 7 (5.3. Ablations and Analysis) |
| To measure our epipolar encoding scheme's importance, we compare pixelSplat to a variant (No Epipolar Encoder) that eschews epipolar encoding. | component/input/data sensitivity | p. 8 (5.3. Ablations and Analysis) |
| We visualize point clouds using the version of our model that has been fine-tuned with a depth regularizer. | component/input/data sensitivity | p. 7 (5.2. Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module. | Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS). | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Results), p. 8 (5.3. Ablations and Analysis), p. 6 (Figure/Table caption), p. 8 (5.3. Ablations and Analysis) |
| Primary metric/result | Qualitatively, this produces ghosting and motion blur artifacts that are evidence of incorrect depth predictions; quantitatively, performance drops significantly. | numeric claim only at cited anchor | p. 8 (5.3. Ablations and Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For the "Plus Depth Regularization" ablation, we regularize depth maps by fine-tuning with 50,000 steps of edge-aware total variation regularization.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Without our sampling approach, our model falls into local minima that manifest themselves as speckling artifacts. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Note that while the resulting Gaussians facilitate high-fidelity novel-view synthesis for in-distribution camera poses, they suffer from the same failure modes as 3D Gaussians ... | p. 7 (5.2. Results) |
| body limitation/failure cue | An exciting avenue for future work is to leverage our model for generative modeling by combining it with diffusion models [48, 51] or to ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 2. Scale ambiguity. SfM does not reconstruct camera poses in real-world, metric scale-poses are scaled by an arbitrary scale factor that is different ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | To evaluate visual fidelity, we compare each method's rendered images to the corresponding ground-truth frames by computing a peak signal-to-noise ratio (PSNR), structural similarity ... | p. 6 (5.1. Experimental Setup) |
| body limitation/failure cue | Specifically, reflective surfaces are often transparent, and Gaussians appear billboard-like when viewed from out-of-distribution views. | p. 7 (5.2. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our method also uses significantly less memory per ray at training time. | p. 6 (5.2. Results) |
| ACID RealEstate10k Inference Time (s) Memory (GB) PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Encode ↓ Render ↓ Training ... | p. 6 (4.2. Gaussian Parameter Prediction) |
| We perform ablations on RealEstate10k to answer the following questions: • Question 1a: Is our epipolar encoder responsible for our model's ability to handle ... | p. 7 (5.3. Ablations and Analysis) |
| To measure our epipolar encoding scheme's importance, we compare pixelSplat to a variant (No Epipolar Encoder) that eschews epipolar encoding. | p. 8 (5.3. Ablations and Analysis) |
| This highlights that beyond simply detecting correspondence, our encoder uses the scene-scale encoded depths it triangulates to resolve scale ambiguity. | p. 8 (5.3. Ablations and Analysis) |
| Note that these depth values are computed from I and ˜I's camera poses, and thus encode the scene's scale si. | p. 3 (4.1. Resolving Scale Ambiguity) |
| Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time. | p. 1 (Abstract) |
| In each forward pass, we sample This CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (1. Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** Without our sampling approach, our model falls into local minima that manifest themselves as speckling artifacts.
- **p. 7 / 5.2. Results - extractive body cue:** Note that while the resulting Gaussians facilitate high-fidelity novel-view synthesis for in-distribution camera poses, they suffer from the same failure modes as 3D Gaussians optimized ...
- **p. 8 / 6. Conclusion - extractive body cue:** An exciting avenue for future work is to leverage our model for generative modeling by combining it with diffusion models [48, 51] or to remove ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Scale ambiguity. SfM does not reconstruct camera poses in real-world, metric scale-poses are scaled by an arbitrary scale factor that is different for ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To evaluate visual fidelity, we compare each method's rendered images to the corresponding ground-truth frames by computing a peak signal-to-noise ratio (PSNR), structural similarity index ...
- **p. 7 / 5.2. Results - extractive body cue:** Specifically, reflective surfaces are often transparent, and Gaussians appear billboard-like when viewed from out-of-distribution views.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 7 (5.2. Results), p. 8 (5.3. Ablations and Analysis), metrics p. 8 (5.3. Ablations and Analysis), p. 6 (5.1. Experimental Setup), p. 6 (5.2. Results), p. 7 (5.2. Results), p. 8 (5.3. Ablations and Analysis), p. 3 (Figure/Table caption), baselines p. 6 (5.1. Experimental Setup), p. 6 (5.2. Results), p. 7 (5.2. Results), p. 3 (Figure/Table caption), p. 7 (5.2. Results), p. 8 (5.3. Ablations and Analysis), results p. 6 (5.2. Results), p. 8 (5.3. Ablations and Analysis), p. 6 (Figure/Table caption), p. 8 (5.3. Ablations and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
