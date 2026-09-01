# Evaluation - Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Scene Synthesis From a Single Image), p. 8 (4.3. Autoregressive Scene Synthesis), p. 6 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments), p. 8 (4.4. Ablation Studies), p. 5 (4. Experiments)): On RealEstate10K, our approach significantly improves image quality and 3D consistency over the baselines.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** Despite the similar name, ScanNet++ features different cameras and scenes from ScanNet, allowing us to assess the generalization of our method in real-world scenarios.
- **p. 5 / 4. Experiments - extractive PDF cue:** Our internal dataset contains around 95,000 synthetic indoor environments with smooth camera trajectories achieved through spline interpolation.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive PDF cue:** But ultimately, our goal is to generate high-quality 3D scenes.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive PDF cue:** Baseline Comparison Given Two Reference Images: We benchmark the approaches on RealEstate10K and evaluate generalization on ScanNet++.
- **p. 8 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** Autoregressive Scene Synthesis with GGS: By generating consistent views between the reference images and from additional viewpoints, GGS can augment the set of 5 reference ...
- **p. 7 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** 6, we show a reconstructed 3D scene from GGS using only 5 reference images.
- **p. 7 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** Next, we re-render the generated scene as condition for the next step, biasing the model towards 3D-consistent inpainting.
- **p. 8 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** For results on a longer trajectory, see Appendix E.3.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Scene Synthesis From a Single Image | EMPIRICAL / REAL-ROBOT OR HARDWARE | On RealEstate10K, our approach significantly improves image quality and 3D consistency over the baselines. | p. 6 (4.1. Scene Synthesis From a Single Image) |
| 4.3. Autoregressive Scene Synthesis | EMPIRICAL / REAL-ROBOT OR HARDWARE | With improved consistency, floating artifacts in the reconstructions are significantly reduced (see also Fig. | p. 8 (4.3. Autoregressive Scene Synthesis) |
| 4.2. Scene Synthesis From Two Images | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach achieves similar results on RealEstate10K but does not reach the same reconstruction quality on ScanNet++. | p. 6 (4.2. Scene Synthesis From Two Images) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our internal dataset contains around 95,000 synthetic indoor environments with smooth camera trajectories achieved through spline interpolation. | p. 5 (4. Experiments) |
| 4.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity. | p. 8 (4.4. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** Despite the similar name, ScanNet++ features different cameras and scenes from ScanNet, allowing us to assess the generalization of our method in real-world scenarios.
- **p. 5 / 4. Experiments - extractive PDF cue:** Our internal dataset contains around 95,000 synthetic indoor environments with smooth camera trajectories achieved through spline interpolation.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive PDF cue:** But ultimately, our goal is to generate high-quality 3D scenes.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive PDF cue:** Baseline Comparison Given Two Reference Images: We benchmark the approaches on RealEstate10K and evaluate generalization on ScanNet++.
- **p. 8 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** Autoregressive Scene Synthesis with GGS: By generating consistent views between the reference images and from additional viewpoints, GGS can augment the set of 5 reference ...
- **p. 7 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** 6, we show a reconstructed 3D scene from GGS using only 5 reference images.
- **p. 7 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** Next, we re-render the generated scene as condition for the next step, biasing the model towards 3D-consistent inpainting.
- **p. 8 / 4.3. Autoregressive Scene Synthesis - extractive PDF cue:** For results on a longer trajectory, see Appendix E.3.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview: Given one or more input images, GGS leverages a video diffusion prior to directly generate a 3D radiance field parameterized via 3D ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 3. To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships be- tween frames. Specifically, we integrate ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Model Architecture: Our approach, GGS, directly synthesizes a 3D representation, which is parameterized by a set of Gaussian splats {gm}, from a set ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Baseline Comparison Given One Reference Image: We benchmark the approaches on RealEstate10K and evaluate generalization ability on ScanNet++. The reported metrics are cal- ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Both, PixelSplat and LatentSplat perform well RE10K Scannet++ Interpolation Extrapolation Interpolation Extrapolation
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Baseline Comparison Given Two Reference Images: We benchmark the approaches on RealEstate10K and evaluate generalization on ScanNet++. We report PSNR, LPIPS and TSED ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. Similar to the single image results, ViewCrafter per- forms particularly well on ScanNet++ but lacks 3D con- sistency as indicated by a lower ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Baseline Comparison Given One Reference Image: We show results for the strongest baselines CameraCtrl [15] and ViewCrafter[76] together with our approach without (Ours-No3D) ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Despite the similar name, ScanNet++ features different cameras and scenes from ScanNet, allowing us to assess the generalization of our method in real-world scenarios. | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | Our internal dataset contains around 95,000 synthetic indoor environments with smooth camera trajectories achieved through spline interpolation. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4.2. Scene Synthesis From Two Images) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3. Method) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.2. Integrating 3D Constraints) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Single Image to 3D: FID and FVD scores for rendered views between the generated images at 576×320 pixels. sequence lead to clearly visible artifacts ... | definition/direction/unit from same section | p. 7 (4.2. Scene Synthesis From Two Images) |
| We report TSED scores with a threshold of 2.0. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Given two reference images, we evaluate performance separately on view interpolation and view extrapolation. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| But ultimately, our goal is to generate high-quality 3D scenes. | definition/direction/unit from same section | p. 6 (4.2. Scene Synthesis From Two Images) |
| For our method, we directly consider the generated 3D splats predicted by GGS. | definition/direction/unit from same section | p. 6 (4.2. Scene Synthesis From Two Images) |
| By improving 3D consistency of the generated images, 27516 | definition/direction/unit from same section | p. 7 (4.3. Autoregressive Scene Synthesis) |
| Without the loss on novel viewpoints (No Lnv), image quality (PSNR) and consistency (TSED) drop significantly. | definition/direction/unit from same section | p. 8 (4.4. Ablation Studies) |
| Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity. | definition/direction/unit from same section | p. 8 (4.4. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baseline Comparison Given One Reference Image: We show results for the strongest baselines CameraCtrl [15] and ViewCrafter[76] together with our approach without (Ours-No3D) and ... | comparison identity and matched condition | p. 7 (4.2. Scene Synthesis From Two Images) |
| Baseline Comparison Given Two Reference Images: We benchmark the approaches on RealEstate10K and evaluate generalization on ScanNet++. | comparison identity and matched condition | p. 6 (4.2. Scene Synthesis From Two Images) |
| Note that all of the baselines make use of pre-trained backbones. | comparison identity and matched condition | p. 5 (4. Experiments) |
| We evaluate these baselines by padding the output camera trajectory and subsequently subsampling the generated results. | comparison identity and matched condition | p. 5 (4. Experiments) |
| On RealEstate10K, our approach significantly improves image quality and 3D consistency over the baselines. | comparison identity and matched condition | p. 6 (4.1. Scene Synthesis From a Single Image) |
| Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity. | comparison identity and matched condition | p. 8 (4.4. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation Studies: We investigate the effectiveness of our design choices on RealEstate10K using two reference images. imation with a Gaussian distribution works better when ... | component/input/data sensitivity | p. 8 (4.4. Ablation Studies) |
| Following [68], we also use a variant of RealEstate10K with rescaled camera poses to be approximately metric. | component/input/data sensitivity | p. 5 (4. Experiments) |
| For a fair comparison of a model with and without an intermediate 3D representation, we train our own purely pose-conditional model (Ours-No3D) as described ... | component/input/data sensitivity | p. 5 (4. Experiments) |
| The ablation studies are reported after training the models for 75K iterations. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Additionally, we train a refined variant, for which we initialize Splatfacto with the generated splats and run it for 5,000 iterations per scene to ... | component/input/data sensitivity | p. 6 (4.2. Scene Synthesis From Two Images) |
| To extend our model from two to an arbitrary number of input views, we train a conditional variant to autoregressively generate a full scene ... | component/input/data sensitivity | p. 7 (4.3. Autoregressive Scene Synthesis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our main contributions as follows: • We propose an approach that directly integrates an explicit 3D representation with a pre-trained latent video ... | On RealEstate10K, our approach significantly improves image quality and 3D consistency over the baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Scene Synthesis From a Single Image), p. 8 (4.3. Autoregressive Scene Synthesis), p. 6 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments), p. 8 (4.4. Ablation Studies), p. 5 (4. Experiments) |
| Primary metric/result | With improved consistency, floating artifacts in the reconstructions are significantly reduced (see also Fig. | numeric claim only at cited anchor | p. 8 (4.3. Autoregressive Scene Synthesis) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive PDF cue:** RealEstate10K comprises sequences of approximately 30-100 frames from 10,000 real estate recordings, featuring smooth camera trajectories with minimal roll or pitch.
- **p. 5 / 4. Experiments - extractive PDF cue:** For the single-view setting, we subsample 8 frames for RealEstate10K with a stride of 10, similar to [68, 74], and use a stride of 4 ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We report results on 128 randomly selected scenes from the RealEstate10K testset and 50 scenes from ScanNet++.
- **p. 5 / 4. Experiments - extractive PDF cue:** For the two-view conditional model, we comply with the training strategy of PixelSplat [5] and sample 8 views randomly within a maximum gap of 80 ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Note that the video backbones of CameraCtrl[14] and ViewCrafter [76] require 14, and 25 frames, respectively, while we consider an 8-frame setting.
- **p. 6 / 4. Experiments - extractive PDF cue:** Inference is performed with a discrete Euler scheduler using 30 steps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 3. To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships be- tween frames. Specifically, we ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | However, PixelSplat does not support view extrapolation, which is our primary objective. | p. 6 (4.2. Scene Synthesis From Two Images) |
| body limitation/failure cue | Our approach achieves similar results on RealEstate10K but does not reach the same reconstruction quality on ScanNet++. | p. 6 (4.2. Scene Synthesis From Two Images) |
| body limitation/failure cue | Figure 2. Model Architecture: Our approach, GGS, directly synthesizes a 3D representation, which is parameterized by a set of Gaussian splats {gm}, from a ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Peak Signal-to-Noise Ratio and LPIPS [80] quantify reconstruction quality. | p. 5 (4. Experiments) |
| body limitation/failure cue | Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity. | p. 8 (4.4. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our models were trained on 8 Nvidia A100 80GB GPUs with a batch size of 1 per GPU, using the AdamW optimizer [31] with ... | p. 6 (4. Experiments) |
| For GGS, we report numbers on generated images using the 2D decoder. | p. 5 (4. Experiments) |
| We compare GGS to the strongest approaches that have code available. | p. 5 (4. Experiments) |
| Inference is performed with a discrete Euler scheduler using 30 steps. | p. 6 (4. Experiments) |
| For ViewCrafter, we use 15,000 optimization steps. | p. 8 (4.3. Autoregressive Scene Synthesis) |
| Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity. | p. 8 (4.4. Ablation Studies) |
| All images are encoded into latent space. | p. 3 (3.1. Pose-Conditional Image-To-Video Architecture) |
| To incorporate camera poses into the backbone, we adopt the approach from CameraCtrl [14], integrating the video model with a camera encoder P. | p. 3 (3.1. Pose-Conditional Image-To-Video Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 3. To address this limitation, we introduce a stronger bias in the model to learn correct spatial relationships be- tween frames. Specifically, we integrate ...
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive PDF cue:** However, PixelSplat does not support view extrapolation, which is our primary objective.
- **p. 6 / 4.2. Scene Synthesis From Two Images - extractive PDF cue:** Our approach achieves similar results on RealEstate10K but does not reach the same reconstruction quality on ScanNet++.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Model Architecture: Our approach, GGS, directly synthesizes a 3D representation, which is parameterized by a set of Gaussian splats {gm}, from a set ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Peak Signal-to-Noise Ratio and LPIPS [80] quantify reconstruction quality.
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** Compared to the 2D decoder (GGS), the 3D decoder improves 3D consistency but moderately degrades visual fidelity.

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.2. Scene Synthesis From Two Images), p. 6 (4.2. Scene Synthesis From Two Images), p. 8 (4.3. Autoregressive Scene Synthesis), p. 7 (4.3. Autoregressive Scene Synthesis), metrics p. 7 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.2. Scene Synthesis From Two Images), p. 6 (4.2. Scene Synthesis From Two Images), p. 7 (4.3. Autoregressive Scene Synthesis), baselines p. 7 (4.2. Scene Synthesis From Two Images), p. 6 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. Scene Synthesis From a Single Image), p. 8 (4.4. Ablation Studies), results p. 6 (4.1. Scene Synthesis From a Single Image), p. 8 (4.3. Autoregressive Scene Synthesis), p. 6 (4.2. Scene Synthesis From Two Images), p. 5 (4. Experiments), p. 8 (4.4. Ablation Studies), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
