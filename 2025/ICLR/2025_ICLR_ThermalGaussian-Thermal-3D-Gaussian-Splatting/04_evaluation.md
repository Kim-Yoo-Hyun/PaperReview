# Evaluation - ThermalGaussian: Thermal 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ybFRoGxZjs; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114610. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS)): We not only achieve simultaneous rendering of thermal and RGB images but also significantly improve the rendering quality of both color and thermal images.

## Evaluation Body Digest

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** As shown in Table 2, even in scenes with pronounced thermal variations, specifically targeting lowtexture thermal characteristics, direct application of thermal data proves challenging for ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Our three thermal Gaussian methods outperform 3DGS+MI across all scenes in PSNR, SSIM, and LPIPS.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our multimodal thermal Gaussian models, MSMG and OMMG, not only render both thermal and RGB images simultaneously but also improve rendering quality for both modalities ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In Fig.7 a, we compare our multimodal regularization γ with manually adjusting the thermal constraint coefficients in a truck scene.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** In very few successful cases, inadequate precision in thermal camera positioning has compromised the quality of thermal reconstructions.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 3DGS+MI denotes training the original 3DGS using thermal images instead of RGB images after obtaining accurate thermal poses through our multimodal initialization.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Additionally, as depicted in the bottom of Fig.6, the assistance from thermal images enables accurate color rendering in low-light scenes for the RGB modality.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We not only achieve simultaneous rendering of thermal and RGB images but also significantly improve the rendering quality of both color and thermal images. | p. 10 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5.3 RGB VIEW SYNTHESIS Our method not only achieves high-quality thermal image rendering but also significantly enhances RGB image rendering quality. | p. 9 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: Compared to NeRF-based methods (Hassan et al., 2024) and methods that directly use thermal images for training 3DGS, our approach not only ... | p. 1 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5.1 IMPLEMENTATION DETAILS Our method is an improvement upon the 3DGS framework, with all experimental settings (e.g., λ) remaining consistent with the reference 3DGS. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to 3DGS, 3DGS+MI adapts to a wider range of scenarios and achieves higher reconstruction quality. | p. 8 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** As shown in Table 2, even in scenes with pronounced thermal variations, specifically targeting lowtexture thermal characteristics, direct application of thermal data proves challenging for ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Our three thermal Gaussian methods outperform 3DGS+MI across all scenes in PSNR, SSIM, and LPIPS.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our multimodal thermal Gaussian models, MSMG and OMMG, not only render both thermal and RGB images simultaneously but also improve rendering quality for both modalities ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In Fig.7 a, we compare our multimodal regularization γ with manually adjusting the thermal constraint coefficients in a truck scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Compared to NeRF-based methods (Hassan et al., 2024) and methods that directly use thermal images for training 3DGS, our approach not only improves ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: ThermalGaussian Overview. We simultaneously construct Gaussians for RGB and ther- mal modalities using the point cloud obtained from multimodal initialization. Each modality's Gaus- ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Different calibration boards for thermal Cameras. 3.2 MULTIMODAL INITIALIZATION Previously, methods for calibration RGB and thermal images (Zhang et al., 2023) often involve ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of our collected dataset with others.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative evaluation of thermal image using our method compared to previous work from test views. "×" indicates a failure to localize using only ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: We present qualitative thermal image comparisons between our method, previous ap- proaches (Hassan et al., 2024; Kerbl et al., 2023), and the corresponding ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Quantitative evaluation of RGB image using our method compared to 3DGS. Metric

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As shown in Table 2, even in scenes with pronounced thermal variations, specifically targeting lowtexture thermal characteristics, direct application of thermal data proves challenging ... | embodiment, simulator version and control stack | p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Task/environment | Our three thermal Gaussian methods outperform 3DGS+MI across all scenes in PSNR, SSIM, and LPIPS. | reset, timeout, object/scene variation | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In very few successful cases, inadequate precision in thermal camera positioning has compromised the quality of thermal reconstructions. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| 3DGS+MI denotes training the original 3DGS using thermal images instead of RGB images after obtaining accurate thermal poses through our multimodal initialization. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Additionally, as depicted in the bottom of Fig.6, the assistance from thermal images enables accurate color rendering in low-light scenes for the RGB modality. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| 5.4 ABLATION STUDY We separate different contributions and algorithm choices to test their effectiveness. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 3: ThermalGaussian Overview. We simultaneously construct Gaussians for RGB and ther- mal modalities using the point cloud obtained from multimodal initialization. Each modality's ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We conducted ablation experiments by gradually adding each component to the baseline 3DGS model. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Compared to 3DGS, 3DGS+MI adapts to a wider range of scenarios and achieves higher reconstruction quality. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Our three thermal Gaussian methods outperform 3DGS+MI across all scenes in PSNR, SSIM, and LPIPS. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| As shown quantitatively in Table 4, our multimodal constraints improve RGB rendering quality in nearly all scenarios, with an average PSNR improvement of 1.1 ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Our method requires only 8% ( 9+9 159+65 = 0.08) of the storage space compared to directly using 3DGS. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Figure 1: Compared to NeRF-based methods (Hassan et al., 2024) and methods that directly use thermal images for training 3DGS, our approach not only ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 5.4 ABLATION STUDY We separate different contributions and algorithm choices to test their effectiveness. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| We conducted ablation experiments by gradually adding each component to the baseline 3DGS model. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named ... | We not only achieve simultaneous rendering of thermal and RGB images but also significantly improve the rendering quality of both color and thermal images. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Primary metric/result | 5.3 RGB VIEW SYNTHESIS Our method not only achieves high-quality thermal image rendering but also significantly enhances RGB image rendering quality. | numeric claim only at cited anchor | p. 9 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** All experiments are conducted on a single NVIDIA 3090 GPU.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The resolution of the rendered RGB images and thermal images is 640×480.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** T / RGB PSNR SSIM LPIPS PSNR SSIM LPIPS 3DGS ✓/ - × × × - - - × × × - / ✓ - ...
- **p. 7 / 3 METHOD - extractive body cue:** The basic specifications of this camera include a resolution of 240×180, a field of view of 33°×25°, a temperature range from -20°C to 550°C, and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Table 2: Quantitative evaluation of thermal image using our method compared to previous work from test views. "×" indicates a failure to localize using ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, model memory ... | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | Our results demonstrate that, under multimodal constraints, when one modality fails, our approach leverages accurate information from the other modality to enhance the model's ... | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | In the appendix, we discuss the limitations of this work and potential directions for future research. | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent. | p. 9 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, model memory ... | p. 10 (5 EXPERIMENTS) |
| The specific hyperparameter λsmooth is set to 0.6. | p. 7 (5 EXPERIMENTS) |
| All experiments are conducted on a single NVIDIA 3090 GPU. | p. 7 (5 EXPERIMENTS) |
| Using the calibrated intrinsic parameters KRGB for the color camera, KTh for the thermal camera, and the rotation R and translation t from the ... | p. 5 (3 METHOD) |
| Then, we provide a detailed description of our method's specific implementation details, including multimodal initialization, three types of multimodal thermal Gaussians, thermal loss, and ... | p. 4 (3 METHOD) |
| The calibration relies on the temperature difference between the board and the background to compute thermal features, enabling calibration. | p. 5 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods (Newcombe et al., 2011) are used to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative evaluation of thermal image using our method compared to previous work from test views. "×" indicates a failure to localize using only ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and thermal images, training time, model memory usage, ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Our results demonstrate that, under multimodal constraints, when one modality fails, our approach leverages accurate information from the other modality to enhance the model's understanding ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In the appendix, we discuss the limitations of this work and potential directions for future research.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This enables our method to advance 3D reconstruction in low-light scenes and enhances the robustness of 3D reconstruction techniques to some extent.

- **Evidence anchors reviewed:** datasets p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), metrics p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 2 (Figure/Table caption), baselines p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 1 (Figure/Table caption), results p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
