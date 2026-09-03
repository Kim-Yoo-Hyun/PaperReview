# Evaluation - ReconFusion: 3D Reconstruction with Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Comparison Results), p. 5 (4. Experiments), p. 5 (4. Experiments)): Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed views) to harder (novel views are ...

## Evaluation Body Digest

- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For the mip-NeRF 360 dataset, we retain its original test set and select the input views from the training set using a heuristic to encourage ...
- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For the real-world object-centric scenes from CO3D we evaluate on a subset of 20 scenes from 10 categories.
- **p. 6 / 4.2. Comparison Results - extractive body cue:** A visual comparison of rendered images and depth maps on scenes from the RealEstate10K [71], LLFF [31], DTU [23], CO3D [39], and mip-NeRF 360 [1] ...
- **p. 7 / 4.2. Comparison Results - extractive body cue:** However, they fall short on 360-degree scenes (e.g. the CO3D dataset), where a large portion of the scene is undersampled or even unobserved due to ...
- **p. 7 / 4.2. Comparison Results - extractive body cue:** Baselines that we additionally tuned for the task of few-view reconstruction are indicated with ∗. eRF and SimpleNeRF) are able to significantly improve the baseline ...
- **p. 8 / 4.4. Scaling to More Views - extractive body cue:** Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene from the mip-NeRF ...
- **p. 8 / 4.4. Scaling to More Views - extractive body cue:** Though most results in this paper focus on the challenging case of 3-9 input views, achieving a high-quality reconstruction of a real-world scene often requires ...
- **p. 6 / 4.2. Comparison Results - extractive body cue:** Both the appearance and geometry of our method are of higher quality than the baselines in these examples-typical failure modes exhibited by the baselines include ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 3.3. Implementation Details (p. 5); 4. Experiments (p. 5); 4.1. Experiment Setup (p. 5); 4.2. Comparison Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6. Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input ... | p. 1 (Figure/Table caption) |
| 4.2. Comparison Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method outperforms all baselines on both in-distribution and out-of-distribution datasets, achieving state-of-the-art performance for few-view NeRF reconstructions. | p. 7 (4.2. Comparison Results) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Finally, we demonstrate that our method improves NeRF reconstruction across a range of capture settings (Sec. | p. 5 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For the mip-NeRF 360 dataset, we retain its original test set and select the input views from the training set using a heuristic to encourage ...
- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For the real-world object-centric scenes from CO3D we evaluate on a subset of 20 scenes from 10 categories.
- **p. 6 / 4.2. Comparison Results - extractive body cue:** A visual comparison of rendered images and depth maps on scenes from the RealEstate10K [71], LLFF [31], DTU [23], CO3D [39], and mip-NeRF 360 [1] ...
- **p. 7 / 4.2. Comparison Results - extractive body cue:** However, they fall short on 360-degree scenes (e.g. the CO3D dataset), where a large portion of the scene is undersampled or even unobserved due to ...
- **p. 7 / 4.2. Comparison Results - extractive body cue:** Baselines that we additionally tuned for the task of few-view reconstruction are indicated with ∗. eRF and SimpleNeRF) are able to significantly improve the baseline ...
- **p. 8 / 4.4. Scaling to More Views - extractive body cue:** Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene from the mip-NeRF ...
- **p. 8 / 4.4. Scaling to More Views - extractive body cue:** Though most results in this paper focus on the challenging case of 3-9 input views, achieving a high-quality reconstruction of a real-world scene often requires ...
- **p. 6 / 4.2. Comparison Results - extractive body cue:** Both the appearance and geometry of our method are of higher quality than the baselines in these examples-typical failure modes exhibited by the baselines include ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input views. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) We optimize a NeRF to minimize a reconstruction loss Lrecon between renderings and a limited set of input images, alongside a sample ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. A visual comparison of rendered images and depth maps on scenes from the RealEstate10K [71], LLFF [31], DTU [23], CO3D [39], and mip-NeRF ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed views) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. We ablate two aspects of our model: pretrained dif- fusion weights (PT) and conditioning. For PT, we initialize the diffusion model weights from ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Ablation of diffusion model on 3-view reconstruc- tion. We show two samples from the diffusion model, and ren- derings from the reconstructed NeRFs ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Comparing diffusion losses for 3D reconstruction. Note the "blotchy" texture on the placemat and background chair when using SDS, and improved background detail ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene from ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the mip-NeRF 360 dataset, we retain its original test set and select the input views from the training set using a heuristic to ... | embodiment, simulator version and control stack | p. 5 (4.1. Experiment Setup), p. 5 (4.1. Experiment Setup) |
| Task/environment | For the real-world object-centric scenes from CO3D we evaluate on a subset of 20 scenes from 10 categories. | reset, timeout, object/scene variation | p. 5 (4.1. Experiment Setup), p. 6 (4.2. Comparison Results) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3.3. Implementation Details), p. 4 (3.2. 3D Reconstruction with Diffusion Priors) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate ReconFusion on five real-world datasets to demonstrate the performance and generalizability of our approach for few-view 3D reconstruction (Sec. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Figure 2. (a) We optimize a NeRF to minimize a reconstruction loss Lrecon between renderings and a limited set of input images, alongside a ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Finally, we demonstrate that our method improves NeRF reconstruction across a range of capture settings (Sec. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| 5, we ablate the choice of diffusion loss and find standard SDS results contain more artifacts, and the multistep diffusion loss effectively mitigates these ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Studies) |
| Our method outperforms all baselines on both in-distribution and out-of-distribution datasets, achieving state-of-the-art performance for few-view NeRF reconstructions. | definition/direction/unit from same section | p. 7 (4.2. Comparison Results) |
| The samples from nearby poses are inconsistent, but can be successfully reconciled into an underlying NeRF reconstruction. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Therefore, we set the weighting factor for our diffusion loss (Lsample) to be inversely proportional to the number of input views in this case. | definition/direction/unit from same section | p. 8 (4.4. Scaling to More Views) |
| Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms all baselines on both in-distribution and out-of-distribution datasets, achieving state-of-the-art performance for few-view NeRF reconstructions. | comparison identity and matched condition | p. 7 (4.2. Comparison Results) |
| Baselines For evaluation datasets, we compare against the state-of-the-art dense-view NeRF model Zip-NeRF [2] (which is also the reconstruction pipeline used in our model), ... | comparison identity and matched condition | p. 5 (4.1. Experiment Setup) |
| Despite this generality, we outperform all baselines across all domains. | comparison identity and matched condition | p. 7 (4.2. Comparison Results) |
| Please refer to the supplement for more details about baselines. | comparison identity and matched condition | p. 5 (4.1. Experiment Setup) |
| Both the appearance and geometry of our method are of higher quality than the baselines in these examples-typical failure modes exhibited by the baselines ... | comparison identity and matched condition | p. 6 (4.2. Comparison Results) |
| Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene from the ... | comparison identity and matched condition | p. 8 (4.4. Scaling to More Views) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. Ablation of diffusion model on 3-view reconstruc- tion. We show two samples from the diffusion model, and ren- derings from the reconstructed ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We also perform several ablations on the components of the diffusion model and the 3D reconstruction procedure (Sec. | component/input/data sensitivity | p. 5 (4. Experiments) |
| Both variants produce sampled images of lower quality, which subsequently degrades the NeRF reconstruction. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| 4, we ablate two aspects of our diffusion model: the use of pretrained diffusion model weights (PT) and conditioning signal. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| For PT, we initialize the diffusion model weights from a pretrained text-to-image model. pose uses a pose conditioning similar to ZeroNVS [45] while pixelnerf ... | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This enables our models to scale to large numbers of input images while selecting inputs that are most useful for the sampled novel view. | Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Comparison Results), p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Primary metric/result | Figure 6. Our learned diffusion prior improves performance over the Zip-NeRF baseline up to as many as 81 input views on the kitchenlego scene ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our base diffusion model is a re-implementation of the Latent Diffusion Model [43] that has been trained on an internal dataset of image-text pairs with ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** The encoder of our PixelNeRF is a small U-Net that takes as input an image of resolution 512×512 and outputs a feature map of resolution ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Regardless of t, we always sample the denoised image with k = 10 steps.
- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For Objaverse, we render each 3D asset from 16 randomly sampled views at resolution 512×512 and composite the rendering onto a randomly selected solid color ...
- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For training, we sample 3 frames of the same scene as input views and sample another frame as the target view.
- **p. 5 / 4.1. Experiment Setup - extractive body cue:** For the real-world object-centric scenes from CO3D we evaluate on a subset of 20 scenes from 10 categories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Many current limitations are evident: the heavyweight diffusion model is costly and slows down reconstruction significantly; our current results demonstrate only limited 3D outpainting ... | p. 8 (5. Discussion) |
| body limitation/failure cue | Both the appearance and geometry of our method are of higher quality than the baselines in these examples-typical failure modes exhibited by the baselines ... | p. 6 (4.2. Comparison Results) |
| body limitation/failure cue | However, they fall short on 360-degree scenes (e.g. the CO3D dataset), where a large portion of the scene is undersampled or even unobserved due ... | p. 7 (4.2. Comparison Results) |
| body limitation/failure cue | Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. (a) We optimize a NeRF to minimize a reconstruction loss Lrecon between renderings and a limited set of input images, alongside a ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We jointly train the PixelNeRF and finetune the denoising U-Net with batch size 256 and learning rate 10-4 for a total of 250k iterations. | p. 5 (3.3. Implementation Details) |
| However, unlike the original implementation, which masks out the foreground object and sidesteps the difficulty of recovering the background of the scene, we use ... | p. 5 (4.1. Experiment Setup) |
| To recover an image, the latents are passed through a VAE decoder D. | p. 3 (3.1. Diffusion Model for Novel View Synthesis) |
| LDMs encode input images to a latent representation using a pretrained variational auto-encoder (VAE) E. | p. 3 (3.1. Diffusion Model for Novel View Synthesis) |
| Specifically, we render an image x(ψ, π) from a sampled novel viewpoint π, and encode and perturb it to a noisy latent zt with ... | p. 4 (3.2. 3D Reconstruction with Diffusion Priors) |
| The trained diffusion model produces plausible single images for novel camera poses, but generated images are often inconsistent for different poses or random seeds. | p. 4 (3.2. 3D Reconstruction with Diffusion Priors) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Methods for reconstructing a 3D scene from images, such as Neural Radiance Fields (NeRF), often exhibit artifacts when trained with few input views. ...
- **p. 8 / 5. Discussion - extractive body cue:** Many current limitations are evident: the heavyweight diffusion model is costly and slows down reconstruction significantly; our current results demonstrate only limited 3D outpainting abilities ...
- **p. 6 / 4.2. Comparison Results - extractive body cue:** Both the appearance and geometry of our method are of higher quality than the baselines in these examples-typical failure modes exhibited by the baselines include ...
- **p. 7 / 4.2. Comparison Results - extractive body cue:** However, they fall short on 360-degree scenes (e.g. the CO3D dataset), where a large portion of the scene is undersampled or even unobserved due to ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of few-view 3D reconstruction methods. Datasets are ordered in terms of sparsity from easier (novel views are close to observed views) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) We optimize a NeRF to minimize a reconstruction loss Lrecon between renderings and a limited set of input images, alongside a sample ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experiment Setup), p. 5 (4.1. Experiment Setup), p. 6 (4.2. Comparison Results), p. 7 (4.2. Comparison Results), p. 7 (4.2. Comparison Results), p. 8 (4.4. Scaling to More Views), metrics p. 5 (4. Experiments), p. 3 (Figure/Table caption), p. 5 (4. Experiments), p. 7 (4.3. Ablation Studies), p. 7 (4.2. Comparison Results), p. 8 (4.3. Ablation Studies), baselines p. 7 (4.2. Comparison Results), p. 5 (4.1. Experiment Setup), p. 7 (4.2. Comparison Results), p. 5 (4.1. Experiment Setup), p. 6 (4.2. Comparison Results), p. 8 (4.4. Scaling to More Views), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.2. Comparison Results), p. 5 (4. Experiments), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
