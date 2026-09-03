# Evaluation - SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7idCpuEAiR; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/113436. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 19 (Figure/Table caption), p. 9 (5 EXPERIMENTS)): When trained with pose perturbation, our full model, incorporating both camera model and pose optimization, consistently achieves improvement in both training and test view synthesis.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We evaluated SG-OmniGS against several SOTA models on datasets of 360-degree images, including eight real-world multi-room scenes from 360Roam dataset (Huang et al., 2022) each ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 5.3 EVALUATION ON MULTI-ROOM REAL-WORLD DATASET In real-world scenarios, we studied three situations of SC-OmniGS and reported the average metric scores across scenes in Table ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.2 EVALUATION ON SINGLE-ROOM SYNTHETIC DATASET We conducted experiments on three synthetic scenes from OmniBlender (Choi et al., 2023), namely Barbershop, Classroom, and Flat.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Real-world omnidirectional images captured by 360-degree cameras inherit the distortion from each lens and result in a complex distortion pattern.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Our method is able to effectively optimize the scene representation, displaying a low sensitivity to initial values.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In Figure 5, we visualize the performance trend depicting the impact of increasing noise scales on the synthetic scene Barbershop and the realworld scene Lab.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** To validate the effectiveness of our camera calibration, we conducted ablation studies on a real scene Center, with and without perturbation to training cameras.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); C EXPERIMENT DETAILS (p. 14); C.2 DATASETS (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | When trained with pose perturbation, our full model, incorporating both camera model and pose optimization, consistently achieves improvement in both training and test view ... | p. 10 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite a slight decrease in rendering quality, the results demonstrate that our method still exhibits significant performance improvements compared to baseline methods. | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our results outperform in both rendering quality and camera accuracy. † indicates training from scratch. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | After modifying ray sampling functions, we can effectively improve NeRF-based methods' performance, proving the necessity of properly treating omnidirectional images as a whole. | p. 8 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Depth visualization of 360-degree views rendered by calibration methods equipped with omnidirectional sampling. Our results outperform in geometry accuracy and details. † ... | p. 19 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We evaluated SG-OmniGS against several SOTA models on datasets of 360-degree images, including eight real-world multi-room scenes from 360Roam dataset (Huang et al., 2022) each ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 5.3 EVALUATION ON MULTI-ROOM REAL-WORLD DATASET In real-world scenarios, we studied three situations of SC-OmniGS and reported the average metric scores across scenes in Table ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.2 EVALUATION ON SINGLE-ROOM SYNTHETIC DATASET We conducted experiments on three synthetic scenes from OmniBlender (Choi et al., 2023), namely Barbershop, Classroom, and Flat.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Real-world omnidirectional images captured by 360-degree cameras inherit the distortion from each lens and result in a complex distortion pattern.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Our method is able to effectively optimize the scene representation, displaying a low sensitivity to initial values.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In Figure 5, we visualize the performance trend depicting the impact of increasing noise scales on the synthetic scene Barbershop and the realworld scene Lab.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** To validate the effectiveness of our camera calibration, we conducted ablation studies on a real scene Center, with and without perturbation to training cameras.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: SC-OmniGS jointly optimizes the omnidirectional camera model, poses, and 3D Gaus- sians using a differentiable omnidirectional rasterizer. It can achieve rapid radiance field ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: A schematic overview of SC-OmniGS optimization flow. 3 PRELIMINARY: 3D GAUSSIAN SPLATTING 3D Gaussian splatting (3D-GS) (Kerbl et al., 2023) represents the scene ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Differentiable omnidirectional camera model. Part 2: ∂ro 2D ∂T′ , the gradient of 2D Gaussian w.r.t. pose [q/t]. Camera pose gets involved in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. For model initialization, we create a spherical grid S ∈RH×W ×3 and set the correspond- ing angle distortion coefficients D with the same ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparisons on synthetic dataset OmniBlender. Checked "Perturb" indicates perturbed training camera poses for training, † indicates training from scratch. 3D-GS based meth- ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparisons of 360-degree novel views among calibration methods. Our results outperform in both rendering quality and camera accuracy. † indicates training from ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Quantitative comparisons on real-world dataset 360Roam. "Point Init" indicates the way of point cloud initialization for 3D-GS based methods, checked "Perturb" indicates perturbed ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Performance with different camera perturbations (PSNR↑). Zoom in for details.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluated SG-OmniGS against several SOTA models on datasets of 360-degree images, including eight real-world multi-room scenes from 360Roam dataset (Huang et al., 2022) ... | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Task/environment | 5.3 EVALUATION ON MULTI-ROOM REAL-WORLD DATASET In real-world scenarios, we studied three situations of SC-OmniGS and reported the average metric scores across scenes in ... | reset, timeout, object/scene variation | p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 6: Ablation study of weighted spherical photometric loss Lwsp. Without using Lwsp, the estimated poses of some cameras suffer obvious errors leading to ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| 5.3 EVALUATION ON MULTI-ROOM REAL-WORLD DATASET In real-world scenarios, we studied three situations of SC-OmniGS and reported the average metric scores across scenes in ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Our results outperform in both rendering quality and camera accuracy. † indicates training from scratch. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Additionally, since point cloud initialization is demanded by 3D-GS based methods, we conducted experiments using different initialization strategies to further verify our system's robustness ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| In comparison to all baselines, our SC-OmniGS demonstrates stable and excellent performance. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Under the situation of camera perturbation, SC-OmniGS demonstrates consistent performance across both training and test views, no matter how 3D Gaussians are initialized. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| To further assess the robustness of our method against varying levels of camera perturbation, we conducted experiments using the same learning rate with increasing ... | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Furthermore, when compared to other calibration baselines (see Barbershop in Table 1), SC-OmniGS consistently outperforms them with most increased rotation noise scales. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Despite a slight decrease in rendering quality, the results demonstrate that our method still exhibits significant performance improvements compared to baseline methods. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Figure 7: Qualitative comparisons of 360-degree novel views among calibration methods equipped with omnidirectional sampling. Our results outperform in both rendering quality and camera ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| For comparison, we select BARF (Lin et al., 2021), L2G-NeRF (Chen et al., 2023a) and CamP (Park et al., 2023) as SOTA radiance field ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| For reference, we also run 3D-GS (Kerbl et al., 2023) and OmniGS (Li et al., 2024) as non-calibration SOTA baselines. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| In comparison to all baselines, our SC-OmniGS demonstrates stable and excellent performance. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of our camera calibration, we conducted ablation studies on a real scene Center, with and without perturbation to training cameras. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Our method is able to effectively optimize the scene representation, displaying a low sensitivity to initial values. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Figure 6: Ablation study of weighted spherical photometric loss Lwsp. Without using Lwsp, the estimated poses of some cameras suffer obvious errors leading to ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Table 5: Ablation study. "Re-init" indicates re-initialization of 3D Gaussians; w/o Lwsp means we disable the spherical weight and calculate classical photometric loss for ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Additionally, we initialized all training cameras at the origin, enabling training the models from scratch without pose priors. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| When the input camera poses are estimated by SfM without perturbation, we can slightly increase the quality of radiance field reconstruction by camera pose ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D ... | When trained with pose perturbation, our full model, incorporating both camera model and pose optimization, consistently achieves improvement in both training and test view ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 19 (Figure/Table caption), p. 9 (5 EXPERIMENTS) |
| Primary metric/result | Despite a slight decrease in rendering quality, the results demonstrate that our method still exhibits significant performance improvements compared to baseline methods. | numeric claim only at cited anchor | p. 8 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The initial learning rates for each camera quaternion q and translation t are set to 0.01, with exponential decay to 1.6e-4 and 6e-3, respectively, in ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** All methods were run on a desktop computer with an RTX 3090 GPU.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Existing methods for recovering 3D information from 360-degree images, including structure-from-motion (SfM) systems (Moulon et al., 2013; Huang & Yeung, 2022), rely on an idealized ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, we cannot apply a similar modification to 3D-GS based methods. | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | With the differentiable omnidirectional camera model and Gaussian splatting procedure, our approach jointly optimizes 3D Gaussians, omnidirectional camera poses and camera model, leading to ... | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors. | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | OmniBlender dataset provides noise-free camera poses and depth maps. | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | Additionally, since point cloud initialization is demanded by 3D-GS based methods, we conducted experiments using different initialization strategies to further verify our system's robustness ... | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | To verify SC-OmniGS flexibility and robustness, we utilized an omnidirectional monocular depth estimation method, e.g. | p. 8 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All methods were run on a desktop computer with an RTX 3090 GPU. | p. 7 (5 EXPERIMENTS) |
| The initial learning rates for each camera quaternion q and translation t are set to 0.01, with exponential decay to 1.6e-4 and 6e-3, respectively, ... | p. 7 (5 EXPERIMENTS) |
| To further assess the robustness of our method against varying levels of camera perturbation, we conducted experiments using the same learning rate with increasing ... | p. 10 (5 EXPERIMENTS) |
| Finally, rather than using the rendered or estimated geometry as the starting point, we randomly sampled 300k points with random colors and positions as ... | p. 8 (5 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** However, we cannot apply a similar modification to 3D-GS based methods.
- **p. 10 / 6 CONCLUSION - extractive body cue:** With the differentiable omnidirectional camera model and Gaussian splatting procedure, our approach jointly optimizes 3D Gaussians, omnidirectional camera poses and camera model, leading to robust ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our camera calibration demonstrates greater robustness to translation errors with only minor degradation compared to rotation errors.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** OmniBlender dataset provides noise-free camera poses and depth maps.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Additionally, since point cloud initialization is demanded by 3D-GS based methods, we conducted experiments using different initialization strategies to further verify our system's robustness and ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** To verify SC-OmniGS flexibility and robustness, we utilized an omnidirectional monocular depth estimation method, e.g.

- **Evidence anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), metrics p. 10 (5 EXPERIMENTS), p. 16 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), baselines p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 19 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), results p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 19 (Figure/Table caption), p. 9 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
