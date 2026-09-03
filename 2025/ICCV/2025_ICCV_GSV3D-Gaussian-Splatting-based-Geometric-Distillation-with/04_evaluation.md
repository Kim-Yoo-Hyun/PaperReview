# Evaluation - GSV3D: Gaussian Splatting-based Geometric Distillation with Stable Video Diffusion for Single-Image 3D Object Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Tao_GSV3D_Gaussian_Splatting-based_Geometric_Distillation_with_Stable_Video_Diffusion_for_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Tao_GSV3D_Gaussian_Splatting-based_Geometric_Distillation_with_Stable_Video_Diffusion_for_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Ablation Studies), p. 7 (4.2. Evalutaion on 3D Generation), p. 7 (4.2. Evalutaion on 3D Generation), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Settings), p. 6 (4.2. Evalutaion on 3D Generation)): The results in Table 2 demonstrate that the setting N = 16 outperforms the other settings in terms of overall performance.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For evaluation, we select a standardized subset of 100 randomly chosen models from the Google Scanned Objects (GSO) [8] dataset.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For training, we collect P = 1 × 105 highquality 3D models from Objaverse [6] dataset.
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** Quantitative comparisons on GSO dataset [8].
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** Our GSV3D achieves the best performance on the GSO dataset. herent in 2D-to-3D indirect representations.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** All experiments are conducted on the GSO dataset.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For the geometry evaluation, we extract meshes from the generated 3D representations and then sample points from these meshes to compute the Chamfer Distance (CD), ...
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** Type Method Appearance Quality Geometry Quality User Study PSNR↑ SSIM↑ LPIPS↓ FID↓ KID↓ CLIP-IQA↑ CD↓ IoU ↑ F-Score↑ App.
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** Score↑ 3D GA [15] 15.201 0.834 0.039 95.47 1.17 0.805 0.197 0.502 0.303 3.154 5.000 TGS [39] 18.874 0.872 0.032 85.25 1.28 0.812 0.272 0.415 ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results in Table 2 demonstrate that the setting N = 16 outperforms the other settings in terms of overall performance. | p. 8 (4.3. Ablation Studies) |
| 4.2. Evalutaion on 3D Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our GSV3D achieves the best performance on the GSO dataset. herent in 2D-to-3D indirect representations. | p. 7 (4.2. Evalutaion on 3D Generation) |
| 4.2. Evalutaion on 3D Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method, constrained by explicit 3D representations, achieves better geometric quality. | p. 7 (4.2. Evalutaion on 3D Generation) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | This improvement can be attributed to the higher number of overlapping regions between frames in the setting N = 16, which helps maintain consistency ... | p. 8 (4.3. Ablation Studies) |
| 4.1. Experimental Settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the geometry evaluation, we extract meshes from the generated 3D representations and then sample points from these meshes to compute the Chamfer Distance ... | p. 6 (4.1. Experimental Settings) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For evaluation, we select a standardized subset of 100 randomly chosen models from the Google Scanned Objects (GSO) [8] dataset.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For training, we collect P = 1 × 105 highquality 3D models from Objaverse [6] dataset.
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** Quantitative comparisons on GSO dataset [8].
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** Our GSV3D achieves the best performance on the GSO dataset. herent in 2D-to-3D indirect representations.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** All experiments are conducted on the GSO dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GSV3D utilizes Stable Video Diffusion and Gaussian Splatting decoder to generate 3D model from a single image. Meanwhile, the Gaussian Splatting-based geometric distillation ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of GSV3D Training and Inference Pipeline. During inference, given an initialized noise latent zT , an input image R and its corresponding ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Overview of the Gaussian Splatting Decoder pipeline. During both geometric distillation and GSV3D inference, the conditioning image R is first processed by a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Performance comparison between our GSV3D and other state-of-art methods. GA and TGS are abbreviations for GaussianAny- thing and TriplaneGaussian, respectively. For each example, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on GSO dataset [8]. GA and TGS are abbreviations for GaussianAnything and TriplaneGaussian, respectively. GaussianAnything and TriplaneGaussians are 3D methods, while ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Examples of using GSV3D for text-to-image-to-3D gen- eration.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Visual comparison for the number of frames N in the multi-view latents generated by denoising UNet ϵθ. Reducing the number of frames weakens ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation studies on the losses used in geometric distil- lation, the number of frames N in the multi-view latents gener- ated by multi-view ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For evaluation, we select a standardized subset of 100 randomly chosen models from the Google Scanned Objects (GSO) [8] dataset. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Task/environment | For training, we collect P = 1 × 105 highquality 3D models from Objaverse [6] dataset. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Settings), p. 7 (4.2. Evalutaion on 3D Generation) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3.4.1. Training Gaussian Splatting Decoder), p. 4 (3.2. Multi-view Diffusion Model for 3D Generation) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (3.4.1. Training Gaussian Splatting Decoder), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the geometry evaluation, we extract meshes from the generated 3D representations and then sample points from these meshes to compute the Chamfer Distance ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Type Method Appearance Quality Geometry Quality User Study PSNR↑ SSIM↑ LPIPS↓ FID↓ KID↓ CLIP-IQA↑ CD↓ IoU ↑ F-Score↑ App. | definition/direction/unit from same section | p. 7 (4.2. Evalutaion on 3D Generation) |
| Score↑ 3D GA [15] 15.201 0.834 0.039 95.47 1.17 0.805 0.197 0.502 0.303 3.154 5.000 TGS [39] 18.874 0.872 0.032 85.25 1.28 0.812 0.272 ... | definition/direction/unit from same section | p. 7 (4.2. Evalutaion on 3D Generation) |
| We collect results from 40 volunteers and get 2800 valid scores in total. | definition/direction/unit from same section | p. 8 (4.2. Evalutaion on 3D Generation) |
| This underscores the essential role of the DINO encoder in the overall framework. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| In contrast, 2D methods [17, 28, 30, 31] demonstrate superior performance in terms of appearance generation. | definition/direction/unit from same section | p. 6 (4.2. Evalutaion on 3D Generation) |
| Figure 2. Overview of GSV3D Training and Inference Pipeline. During inference, given an initialized noise latent zT , an input image R and its ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 1. GSV3D utilizes Stable Video Diffusion and Gaussian Splatting decoder to generate 3D model from a single image. Meanwhile, the Gaussian Splatting-based geometric ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare our model against the following state-of-the-art methods: GaussianAnything [15] (GA), TriplaneGaussian [39] (TGS), LGM [30], Zero123Plus [28], Era3D [17], and SV3D [31]. | comparison identity and matched condition | p. 6 (4.1. Experimental Settings) |
| The results in Table 2 demonstrate that the setting N = 16 outperforms the other settings in terms of overall performance. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| They generate 3D representations without the intermediate step of estimating 2D images and are trained from scratch on 3D datasets. | comparison identity and matched condition | p. 6 (4.1. Experimental Settings) |
| Quantitative comparisons on GSO dataset [8]. | comparison identity and matched condition | p. 7 (4.2. Evalutaion on 3D Generation) |
| Performance comparison between our GSV3D and other state-of-art methods. | comparison identity and matched condition | p. 7 (4.2. Evalutaion on 3D Generation) |
| Visual comparison for the number of frames N in the multi-view latents generated by denoising UNet ϵθ. | comparison identity and matched condition | p. 8 (4.2. Evalutaion on 3D Generation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Ablation studies on the losses used in geometric distil- lation, the number of frames N in the multi-view latents gener- ated by ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Effect of DINO encoder in Gaussian Splatting Decoder. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| They generate 3D representations without the intermediate step of estimating 2D images and are trained from scratch on 3D datasets. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| These methods are typically based on strong pretrained 2D Diffusion models to help construct 3D representations. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We propose a latent decoder trained to extract 3D Gaussian Splatting representations directly from multi-view latents ... | The results in Table 2 demonstrate that the setting N = 16 outperforms the other settings in terms of overall performance. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Ablation Studies), p. 7 (4.2. Evalutaion on 3D Generation), p. 7 (4.2. Evalutaion on 3D Generation), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Settings), p. 6 (4.2. Evalutaion on 3D Generation) |
| Primary metric/result | Our GSV3D achieves the best performance on the GSO dataset. herent in 2D-to-3D indirect representations. | numeric claim only at cited anchor | p. 7 (4.2. Evalutaion on 3D Generation) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** While the elevation angle is fixed for each individual object, it is randomly sampled between -5 and 30 degrees across different objects.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** From these 84 images, we select N = 16 images at regular intervals to serve as the training input.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For each model, we render 21 RGB images with a fixed elevation angle, which is randomly chosen between -5 and 30 degrees, and azimuth angles ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Also, we sample 4,096 points from the mesh of each object to facilitate 3D evaluation.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** This stage is trained for 80,000 steps with a batch size of 128. • Stage Two: We integrate the Gaussian Splatting Decoder into the multi-view ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** This stage is trained for 40,000 steps with a reduced batch size of 32.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While 2D diffusion models offer diversity but lack geometric consistency, and 3D diffusion models face data limitations, our hybrid approach bridges this gap. | p. 8 (5. Conclusion) |
| body limitation/failure cue | This limitation stems from the restricted diversity of the training data, which hinders the model's ability to generalize well to unseen or complex scenarios. | p. 7 (4.2. Evalutaion on 3D Generation) |
| body limitation/failure cue | Figure 2. Overview of GSV3D Training and Inference Pipeline. During inference, given an initialized noise latent zT , an input image R and its ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | However, due to poor image consistency, the reconstructed results of these images suffer from blurry and ghosting artifacts, which degrade the evaluation metrics, as ... | p. 6 (4.2. Evalutaion on 3D Generation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This stage is trained for 80,000 steps with a batch size of 128. • Stage Two: We integrate the Gaussian Splatting Decoder into the ... | p. 6 (4.1. Experimental Settings) |
| In both stages, we use AdamW [21] with a learning rate of 1 × 10-5 to optimize the model. | p. 6 (4.1. Experimental Settings) |
| Notably, we render both the input views and the novel views to ensure a comprehensive optimization of the performance of the decoder across different ... | p. 5 (3.4.1. Training Gaussian Splatting Decoder) |
| In order to train the Gaussian Splatting Decoder, we render Q images for each of the P objects in the training set, with these ... | p. 5 (3.4.1. Training Gaussian Splatting Decoder) |
| Effect of DINO encoder in Gaussian Splatting Decoder. | p. 8 (4.3. Ablation Studies) |
| This underscores the essential role of the DINO encoder in the overall framework. | p. 8 (4.3. Ablation Studies) |
| This decoder provides a learnable 3D representation, better capturing the underlying geometry. | p. 3 (3.1. Overview) |
| To address this, we introduce a Gaussian Splatting Decoder, which transforms the multi-view latents into an explicit 3D structure (Section 3.3). | p. 3 (3.1. Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** While 2D diffusion models offer diversity but lack geometric consistency, and 3D diffusion models face data limitations, our hybrid approach bridges this gap.
- **p. 7 / 4.2. Evalutaion on 3D Generation - extractive body cue:** This limitation stems from the restricted diversity of the training data, which hinders the model's ability to generalize well to unseen or complex scenarios.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of GSV3D Training and Inference Pipeline. During inference, given an initialized noise latent zT , an input image R and its corresponding ...
- **p. 6 / 4.2. Evalutaion on 3D Generation - extractive body cue:** However, due to poor image consistency, the reconstructed results of these images suffer from blurry and ghosting artifacts, which degrade the evaluation metrics, as shown ...

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Evalutaion on 3D Generation), p. 7 (4.2. Evalutaion on 3D Generation), p. 8 (4.3. Ablation Studies), metrics p. 6 (4.1. Experimental Settings), p. 7 (4.2. Evalutaion on 3D Generation), p. 7 (4.2. Evalutaion on 3D Generation), p. 8 (4.2. Evalutaion on 3D Generation), p. 8 (4.3. Ablation Studies), p. 6 (4.2. Evalutaion on 3D Generation), baselines p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Evalutaion on 3D Generation), p. 7 (4.2. Evalutaion on 3D Generation), p. 8 (4.2. Evalutaion on 3D Generation), results p. 8 (4.3. Ablation Studies), p. 7 (4.2. Evalutaion on 3D Generation), p. 7 (4.2. Evalutaion on 3D Generation), p. 8 (4.3. Ablation Studies), p. 6 (4.1. Experimental Settings), p. 6 (4.2. Evalutaion on 3D Generation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
