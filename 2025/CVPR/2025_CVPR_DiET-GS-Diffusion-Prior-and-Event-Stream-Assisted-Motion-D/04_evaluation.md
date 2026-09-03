# Evaluation - DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons), p. 8 (Figure/Table caption), p. 6 (Dataset), p. 6 (Dataset)): Furthermore, our DiET-GS++ shows significant improvement in MUSIQ and CLIP-IQA metrics, achieving the best results but showing a slight drop in PSNR and SSIM metrics.

## Evaluation Body Digest

- **p. 6 / 5.2. Datasets - extractive body cue:** The EvDeblur-CDAVIS Dataset contains five real-world scenes, each with 11 to 18 blurry training images paired with corresponding event streams.
- **p. 6 / 5.2. Datasets - extractive body cue:** Both synthetic and real-world datasets include five ground-truth (GT) sharp images captured from both seen and unseen viewpoints for each scene.
- **p. 7 / 5.3. Experiment Settings - extractive body cue:** Qualitative comparisons on both synthetic (1st-2nd rows) and real-world (3rd-4th rows) datasets.
- **p. 7 / 5.4. Quantitative Comparisons - extractive body cue:** Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world datasets, showing the effectiveness of our framework to leverage ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on both synthetic and real-world dataset. The results are the average of every scenes within the dataset. The best results are ...
- **p. 6 / 5.1. Implementation Details - extractive body cue:** Throughout Stage 1, we set the loss weights λblur = λedi = λrsd = 1.0 and λev = 0.1, and execute 100,000 iterations of training.
- **p. 7 / 5.3. Experiment Settings - extractive body cue:** DiET-GS shows cleaner texture with more accurate details compared to the event-based baselines while DiET-GS++ further enhances these features with sharper definition, achieving the best ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall framework of our DiET-GS. Stage 1 (DiET-GS) optimizes the deblurring 3DGS with the event streams and diffusion prior. To preserve accurate color ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** Dataset (p. 6); 5. Experiments (p. 6); 5.1. Implementation Details (p. 6); 5.2. Datasets (p. 6); 5.3. Experiment Settings (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.4. Quantitative Comparisons | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, our DiET-GS++ shows significant improvement in MUSIQ and CLIP-IQA metrics, achieving the best results but showing a slight drop in PSNR and SSIM ... | p. 7 (5.4. Quantitative Comparisons) |
| 5.4. Quantitative Comparisons | EMPIRICAL / REAL-ROBOT OR HARDWARE | Nonetheless, DiET-GS++ still substantially improves the visual quality as shown in NR-IQA metrics. | p. 7 (5.4. Quantitative Comparisons) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6. Ablation on Ledi simul (1st row) and Lrsd (S1) (2nd row). adding EDI simulation Ledi simul further aids fine-grained deblurring as shown ... | p. 8 (Figure/Table caption) |
| Dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | The best results are in bold while the second best results are underscored. | p. 6 (Dataset) |
| Dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results are the average of every scenes within the dataset. | p. 6 (Dataset) |

## Dataset / Benchmark Role

- **p. 6 / 5.2. Datasets - extractive body cue:** The EvDeblur-CDAVIS Dataset contains five real-world scenes, each with 11 to 18 blurry training images paired with corresponding event streams.
- **p. 6 / 5.2. Datasets - extractive body cue:** Both synthetic and real-world datasets include five ground-truth (GT) sharp images captured from both seen and unseen viewpoints for each scene.
- **p. 7 / 5.3. Experiment Settings - extractive body cue:** Qualitative comparisons on both synthetic (1st-2nd rows) and real-world (3rd-4th rows) datasets.
- **p. 7 / 5.4. Quantitative Comparisons - extractive body cue:** Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world datasets, showing the effectiveness of our framework to leverage ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Given a set of blurry images and corresponding event streams, we propose a novel framework to construct deblurring 3DGS by jointly leveraging the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall framework of our DiET-GS. Stage 1 (DiET-GS) optimizes the deblurring 3DGS with the event streams and diffusion prior. To preserve accurate color ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Cycle consistency among the objective terms. Ledi simul follows the formulation of Ledi gray except for substi- tuting CB to simulated blurry image ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on both synthetic and real-world dataset. The results are the average of every scenes within the dataset. The best results are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparisons on both synthetic (1st-2nd rows) and real-world (3rd-4th rows) datasets. DiET-GS shows cleaner texture with more accurate details compared to the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Ablation study on Ledi gray and Ledi color samples compared to DiET-GS which is supervised by real- captured data. Nonetheless, DiET-GS++ still substantially ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation study on DiET-GS and DiET-GS++ 3DGS. 2) We find that our DiET-GS is capable of restor- ing cleaner textures and clearer edges ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Ablation on Ledi simul (1st row) and Lrsd (S1) (2nd row). adding EDI simulation Ledi simul further aids fine-grained deblurring as shown in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The EvDeblur-CDAVIS Dataset contains five real-world scenes, each with 11 to 18 blurry training images paired with corresponding event streams. | embodiment, simulator version and control stack | p. 6 (5.2. Datasets), p. 6 (5.2. Datasets) |
| Task/environment | Both synthetic and real-world datasets include five ground-truth (GT) sharp images captured from both seen and unseen viewpoints for each scene. | reset, timeout, object/scene variation | p. 6 (5.2. Datasets), p. 7 (5.3. Experiment Settings) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (4. Our Method), p. 5 (4. Our Method) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (4. Our Method), p. 4 (4. Our Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1. Quantitative comparisons on both synthetic and real-world dataset. The results are the average of every scenes within the dataset. The best results ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Throughout Stage 1, we set the loss weights λblur = λedi = λrsd = 1.0 and λev = 0.1, and execute 100,000 iterations of ... | definition/direction/unit from same section | p. 6 (5.1. Implementation Details) |
| DiET-GS shows cleaner texture with more accurate details compared to the event-based baselines while DiET-GS++ further enhances these features with sharper definition, achieving the ... | definition/direction/unit from same section | p. 7 (5.3. Experiment Settings) |
| Figure 2. Overall framework of our DiET-GS. Stage 1 (DiET-GS) optimizes the deblurring 3DGS with the event streams and diffusion prior. To preserve accurate ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Table 2. Ablation study on DiET-GS and DiET-GS++ 3DGS. 2) We find that our DiET-GS is capable of restor- ing cleaner textures and clearer ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our DiETGS largely outperforms all baselines in PSNR, SSIM, and LPIPS on both synthetic and real-world datasets, showing the effectiveness of our framework to ... | comparison identity and matched condition | p. 7 (5.4. Quantitative Comparisons) |
| DiET-GS shows cleaner texture with more accurate details compared to the event-based baselines while DiET-GS++ further enhances these features with sharper definition, achieving the ... | comparison identity and matched condition | p. 7 (5.3. Experiment Settings) |
| Table 2. Ablation study on DiET-GS and DiET-GS++ 3DGS. 2) We find that our DiET-GS is capable of restor- ing cleaner textures and clearer ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Our baselines are divided into three categories. | comparison identity and matched condition | p. 6 (5.3. Experiment Settings) |
| Specifically, an image deblurring method MPRNet [63], and event-based deblurring methods EDI [33] and EFNet [48] are adopted as baselines. | comparison identity and matched condition | p. 6 (5.3. Experiment Settings) |
| Figure 6. Ablation on Ledi simul (1st row) and Lrsd (S1) (2nd row). adding EDI simulation Ledi simul further aids fine-grained deblurring as shown ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on Ledi gray and Ledi color samples compared to DiET-GS which is supervised by realcaptured data. | component/input/data sensitivity | p. 7 (5.4. Quantitative Comparisons) |
| Figure 2. Overall framework of our DiET-GS. Stage 1 (DiET-GS) optimizes the deblurring 3DGS with the event streams and diffusion prior. To preserve accurate ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 2. Ablation study on DiET-GS and DiET-GS++ 3DGS. 2) We find that our DiET-GS is capable of restor- ing cleaner textures and clearer ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. Ablation on Ledi simul (1st row) and Lrsd (S1) (2nd row). adding EDI simulation Ledi simul further aids fine-grained deblurring as shown ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| As already discussed in [20, 62], since DiET-GS++ is solely guided by a pretrained generative model, the resulting images may contain more variation with ... | component/input/data sensitivity | p. 7 (5.4. Quantitative Comparisons) |
| Specifically, ˜C = D(z′ 0) = D(f2D +E( ˆC)), where D is pretrained VAE decoder (cf. | component/input/data sensitivity | p. 6 (Dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Once optimized, our method is capable of recovering well-defined details with accurate color from the input blurry images. • Qualitative and quantitative results show ... | Furthermore, our DiET-GS++ shows significant improvement in MUSIQ and CLIP-IQA metrics, achieving the best results but showing a slight drop in PSNR and SSIM ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons), p. 8 (Figure/Table caption), p. 6 (Dataset), p. 6 (Dataset) |
| Primary metric/result | Nonetheless, DiET-GS++ still substantially improves the visual quality as shown in NR-IQA metrics. | numeric claim only at cited anchor | p. 7 (5.4. Quantitative Comparisons) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Implementation Details - extractive body cue:** All experiments are conducted using a single NVIDIA RTX 6000 GPU.
- **p. 6 / 5.2. Datasets - extractive body cue:** Motion blur is produced during a 40ms exposure time with a single fast continuous motion by averaging a set of images rendered at 1000 FPS ...
- **p. 6 / 5.2. Datasets - extractive body cue:** A 1000ms exposure time is given to produce motion blur.
- **p. 4 / 4. Our Method - extractive body cue:** 3 into: ˆCB i = 1 n n-1 X j=0 gθ(pij), (5) where gθ(·) is the 3DGS with rendering function and ˆCB is the estimated ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1. | p. 6 (Dataset) |
| body limitation/failure cue | Finally, given ˆC as conditional input, the UNet backbone of pretrained diffusion model predicts the noise residual of z′t to derive the denoised latent ... | p. 6 (Dataset) |
| body limitation/failure cue | We employ three standard metrics: Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and VGG-based Learned Perceptual Image Patch Similarity (LPIPS) [65] to ... | p. 7 (5.3. Experiment Settings) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All experiments are conducted using a single NVIDIA RTX 6000 GPU. | p. 6 (5.1. Implementation Details) |
| We build our framework based on the official code of 3DGS [15] and DiSR-NeRF [20]. | p. 6 (5.1. Implementation Details) |
| We select E2NeRF [36] and Ev-DeblurNeRF [3] as the most recent works in this category with publicly available code. | p. 7 (5.3. Experiment Settings) |
| We obtain a set of latent images for each training view by warping the recovered latent image I to each of the n timesteps ... | p. 4 (4. Our Method) |
| 2, we randomly sample two timesteps tα and tβ = tα + ∆t along the camera trajectory and approximate the camera poses corresponding to ... | p. 4 (4. Our Method) |
| 3, and encode it to a latent z0 = E( ˆCB) via a pretrained VAE encoder E. | p. 5 (4. Our Method) |
| Subsequently, we apply the forward process of the diffusion model by introducing noise at timesteps t and t -1 based on a predetermined noising ... | p. 5 (4. Our Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Dataset - extractive body cue:** Gaussian noise samples at timesteps t and t -1 are then introduced to z′0 to get noised latents z′t and z′t-1.
- **p. 6 / Dataset - extractive body cue:** Finally, given ˆC as conditional input, the UNet backbone of pretrained diffusion model predicts the noise residual of z′t to derive the denoised latent ˆz′ ...
- **p. 7 / 5.3. Experiment Settings - extractive body cue:** We employ three standard metrics: Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and VGG-based Learned Perceptual Image Patch Similarity (LPIPS) [65] to evaluate ...

- **Evidence anchors reviewed:** datasets p. 6 (5.2. Datasets), p. 6 (5.2. Datasets), p. 7 (5.3. Experiment Settings), p. 7 (5.4. Quantitative Comparisons), metrics p. 6 (Figure/Table caption), p. 6 (5.1. Implementation Details), p. 7 (5.3. Experiment Settings), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 7 (5.4. Quantitative Comparisons), p. 7 (5.3. Experiment Settings), p. 8 (Figure/Table caption), p. 6 (5.3. Experiment Settings), p. 6 (5.3. Experiment Settings), p. 8 (Figure/Table caption), results p. 7 (5.4. Quantitative Comparisons), p. 7 (5.4. Quantitative Comparisons), p. 8 (Figure/Table caption), p. 6 (Dataset), p. 6 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
