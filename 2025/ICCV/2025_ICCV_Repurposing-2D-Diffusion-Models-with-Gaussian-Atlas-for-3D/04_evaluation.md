# Evaluation - Repurposing 2D Diffusion Models with Gaussian Atlas for 3D Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (3. GaussianVerse), p. 5 (4. Formulating 3D Gaussians as 2D Atlas)): Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number of 3D Gaussians. sive details. In ...

## Evaluation Body Digest

- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** However, text-to-3D generation presents greater challenges due to two key reasons: (i) the scarcity of large-scale datasets with 3D models comparable to those in 2D, ...
- **p. 3 / 3. GaussianVerse - extractive PDF cue:** Statistics for the proposed GaussianVerse dataset.
- **p. 3 / 3. GaussianVerse - extractive PDF cue:** metal handle house model light box roof table stone character toy sword cube robot rock cartoon hat gun sphere hole Total number of 3DGS fittings ...
- **p. 4 / 3. GaussianVerse - extractive PDF cue:** This curated list results in a wide coverage of diverse objects.
- **p. 5 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** This consistency allows us to perform OT in the last stage only once and reuse the computed indices for all objects.
- **p. 5 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** In particular, since now M is a deterministic function, the mapping between {pi} and {qi} remains identical for all objects.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Additional qualitative results. Our method effectively repurposes 2D diffusion models for high-quality 3D contents. The generated Gaussian atlases are presented in the order ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number of ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 6. Experiments (p. 6); 6.1. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 7. User study results. Our method outperforms state-of- the-art methods [57, 60] in user preferences regarding generation quality and alignment with text prompts. ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 8. Finetuning from a pretrained 2D diffusion model leads to faster generalization. Top: 3D generations at different training checkpoints from finetuning (top row) ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. Previous 3D generators are either end-to-end 3D models [10, 57] or a combination of a multi-view 2D generator followed by a 2D-to-3D ... | p. 1 (Figure/Table caption) |
| 3. GaussianVerse | SYSTEM / EVALUATION SCOPE UNRESOLVED | Compared with several previous studies [10, 30, 57] which also fit per-object 3D Gaussians for training diffusion models, we achieve higherquality 3DGS fittings with ... | p. 4 (3. GaussianVerse) |

## Dataset / Benchmark Role

- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** However, text-to-3D generation presents greater challenges due to two key reasons: (i) the scarcity of large-scale datasets with 3D models comparable to those in 2D, ...
- **p. 3 / 3. GaussianVerse - extractive PDF cue:** Statistics for the proposed GaussianVerse dataset.
- **p. 3 / 3. GaussianVerse - extractive PDF cue:** metal handle house model light box roof table stone character toy sword cube robot rock cartoon hat gun sphere hole Total number of 3DGS fittings ...
- **p. 4 / 3. GaussianVerse - extractive PDF cue:** This curated list results in a wide coverage of diverse objects.
- **p. 5 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** This consistency allows us to perform OT in the last stage only once and reuse the computed indices for all objects.
- **p. 5 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** In particular, since now M is a deterministic function, the mapping between {pi} and {qi} remains identical for all objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Previous 3D generators are either end-to-end 3D models [10, 57] or a combination of a multi-view 2D generator followed by a 2D-to-3D lifting ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. (a) GaussianVerse offers high-quality 3DGS fittings for diverse 3D objects. (b) A word cloud and (c) a list of the most frequently occurring ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1. Statistics for the proposed GaussianVerse dataset. We report the average (with standard deviation) number of 3D Gaus- sians per fitting, the total number ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Representing 3D Gaussians as 2D Gaussian Atlas. For each fitting, 3D Gaussians are first translated to the surface of a standard sphere S ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Repurposing 2D diffusion models for 3D Gaussian generation. Our pipeline consists of two stages. In the 3DGS pre-fitting stage (section 3), we pre-fit ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative Comparisons. Our 3D generations exhibit the highest quality, minimal artifacts, and the best alignment with text prompts. In contrast, DreamGaussian [46], LGM ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Additional qualitative results. Our method effectively repurposes 2D diffusion models for high-quality 3D contents. The generated Gaussian atlases are presented in the order ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, text-to-3D generation presents greater challenges due to two key reasons: (i) the scarcity of large-scale datasets with 3D models comparable to those in ... | embodiment, simulator version and control stack | p. 4 (4. Formulating 3D Gaussians as 2D Atlas), p. 3 (3. GaussianVerse) |
| Task/environment | Statistics for the proposed GaussianVerse dataset. | reset, timeout, object/scene variation | p. 3 (3. GaussianVerse), p. 3 (3. GaussianVerse) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3. GaussianVerse) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (3. GaussianVerse), p. 4 (4. Formulating 3D Gaussians as 2D Atlas) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6. Additional qualitative results. Our method effectively repurposes 2D diffusion models for high-quality 3D contents. The generated Gaussian atlases are presented in the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 10. Log scale mean squared errors (smoothed) of per layer weights between different UNets. Finetuning from a pre-trained LD UNet leads to smaller ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 8. Finetuning from a pretrained 2D diffusion model leads to faster generalization. Top: 3D generations at different training checkpoints from finetuning (top row) ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We report the average (with standard deviation) number of 3D Gaussians per fitting, the total number of fitted objects, and the overall compute time ... | definition/direction/unit from same section | p. 3 (3. GaussianVerse) |
| We therefore standardize the 2D atlases using the pixelwise mean and standard deviation computed from the entire GaussianVerse. | definition/direction/unit from same section | p. 5 (5. 2D Diffusion for 3D Gaussian Generation) |
| Figure 1. Previous 3D generators are either end-to-end 3D models [10, 57] or a combination of a multi-view 2D generator followed by a 2D-to-3D ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The 3D covariance matrix !i can be represented as !i = risirT i . | definition/direction/unit from same section | p. 3 (3. GaussianVerse) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 7. User study results. Our method outperforms state-of- the-art methods [57, 60] in user preferences regarding generation quality and alignment with text prompts. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We build our fitting model upon the state-of-the-art, ScaffoldGS [24], along with non-trivial modifications. | comparison identity and matched condition | p. 3 (3. GaussianVerse) |
| Compared with several previous studies [10, 30, 57] which also fit per-object 3D Gaussians for training diffusion models, we achieve higherquality 3DGS fittings with ... | comparison identity and matched condition | p. 4 (3. GaussianVerse) |
| Figure 5. Qualitative Comparisons. Our 3D generations exhibit the highest quality, minimal artifacts, and the best alignment with text prompts. In contrast, DreamGaussian [46], ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. Previous 3D generators are either end-to-end 3D models [10, 57] or a combination of a multi-view 2D generator followed by a 2D-to-3D ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| First, we exclude view properties from the MLP predictors for attribute querying to enable more view-invariant applications. | component/input/data sensitivity | p. 3 (3. GaussianVerse) |
| The core components of LD include a Variational AutoEncoder (VAE) and a UNet F(·). | component/input/data sensitivity | p. 5 (5. 2D Diffusion for 3D Gaussian Generation) |
| The standard fine-tuning approach for LDs involves VAE-based encoding and decoding [14]. | component/input/data sensitivity | p. 5 (5. 2D Diffusion for 3D Gaussian Generation) |
| Figure 5. Qualitative Comparisons. Our 3D generations exhibit the highest quality, minimal artifacts, and the best alignment with text prompts. In contrast, DreamGaussian [46], ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our major contributions are three-fold: (i) We present a large-scale dataset, GaussianVerse, consisting of 205,737 high-quality 3D Gaussian fittings for diverse objects ... | Table 2. Qualitative comparisons. Our method achieves perfor- mance comparable to the state-of-the-art in terms of CLIP similar- ity scores, with the minimum number ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (3. GaussianVerse), p. 5 (4. Formulating 3D Gaussians as 2D Atlas) |
| Primary metric/result | Figure 7. User study results. Our method outperforms state-of- the-art methods [57, 60] in user preferences regarding generation quality and alignment with text prompts. ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 3 / 3. GaussianVerse - extractive PDF cue:** Red dotted lines indicate the 25%, 50%, and 75% percentile of the distribution. # Gaussians per fitting Total # fittings Compute time 10,435±4,453 205,737 >3.8 ...
- **p. 4 / 3. GaussianVerse - extractive PDF cue:** Each 3DGS fitting job converges at around 20,000 steps, translating to approximately 10 minutes of fitting time per object, with a total of over 3.8 ...
- **p. 3 / 3. GaussianVerse - extractive PDF cue:** Red dotted lines indicate the 25%, 50%, and 75% percentile of the distribution. # Gaussians per fitting Total # fittings Compute time 10,435±4,453 205,737 >3.8 ...
- **p. 4 / 3. GaussianVerse - extractive PDF cue:** Each 3DGS fitting job converges at around 20,000 steps, translating to approximately 10 minutes of fitting time per object, with a total of over 3.8 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, unstructured Gaussians in 3D space cannot be directly passed to 2D models, which require inputs X to have: (i) only 2 spatial dimensions; ... | p. 4 (4. Formulating 3D Gaussians as 2D Atlas) |
| body limitation/failure cue | Figure 5. Qualitative Comparisons. Our 3D generations exhibit the highest quality, minimal artifacts, and the best alignment with text prompts. In contrast, DreamGaussian [46], ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | As a result, diffusion models are not able to capture the irregular patterns and fail to generate meaningful contents. | p. 4 (4. Formulating 3D Gaussians as 2D Atlas) |
| body limitation/failure cue | By injecting Gaussian noise to the latents, F can be trained through self-supervised denoising via v-parameterization [39]: Ldiff = El0,z,t # ≃⇐ltz ↑⇐ltF(lt, t)≃2$ ... | p. 5 (5. 2D Diffusion for 3D Gaussian Generation) |
| body limitation/failure cue | In the diffusion model training stage (section 5), we leverage the transformed 2D Gaussian atlases to repurpose a pretrained latent diffusion model (the 2D ... | p. 5 (4. Formulating 3D Gaussians as 2D Atlas) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Red dotted lines indicate the 25%, 50%, and 75% percentile of the distribution. # Gaussians per fitting Total # fittings Compute time 10,435±4,453 205,737 ... | p. 3 (3. GaussianVerse) |
| Each 3DGS fitting job converges at around 20,000 steps, translating to approximately 10 minutes of fitting time per object, with a total of over ... | p. 4 (3. GaussianVerse) |
| We obtain Gaussian Atlas by reorganizing the flattened coordinates to pixels of a dense 2D square of size → N ↑ → N. loss ... | p. 4 (3. GaussianVerse) |
| We show that these Gaussian atlases facilitate transfer of the prior knowledge This ICCV paper is the Open Access version, provided by the Computer ... | p. 1 (1. Introduction) |
| In this work, we achieve 3D object generation by directly fine-tuning 2D generation models. previous studies that also pre-compute 3D Gaussian references, GaussianVerse provides ... | p. 1 (1. Introduction) |
| This pruning strategy differs from the original implementation [15], which only prunes completely invisible Gaussians. | p. 3 (3. GaussianVerse) |
| The core components of LD include a Variational AutoEncoder (VAE) and a UNet F(·). | p. 5 (5. 2D Diffusion for 3D Gaussian Generation) |
| The VAE decoder then upsamples the generated latent back to the original RGB space. | p. 5 (5. 2D Diffusion for 3D Gaussian Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** However, unstructured Gaussians in 3D space cannot be directly passed to 2D models, which require inputs X to have: (i) only 2 spatial dimensions; (ii) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative Comparisons. Our 3D generations exhibit the highest quality, minimal artifacts, and the best alignment with text prompts. In contrast, DreamGaussian [46], LGM ...
- **p. 4 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** As a result, diffusion models are not able to capture the irregular patterns and fail to generate meaningful contents.
- **p. 5 / 5. 2D Diffusion for 3D Gaussian Generation - extractive PDF cue:** By injecting Gaussian noise to the latents, F can be trained through self-supervised denoising via v-parameterization [39]: Ldiff = El0,z,t # ≃⇐ltz ↑⇐ltF(lt, t)≃2$ , ...
- **p. 5 / 4. Formulating 3D Gaussians as 2D Atlas - extractive PDF cue:** In the diffusion model training stage (section 5), we leverage the transformed 2D Gaussian atlases to repurpose a pretrained latent diffusion model (the 2D UNet ...

- **PDF anchors reviewed:** datasets p. 4 (4. Formulating 3D Gaussians as 2D Atlas), p. 3 (3. GaussianVerse), p. 3 (3. GaussianVerse), p. 4 (3. GaussianVerse), p. 5 (4. Formulating 3D Gaussians as 2D Atlas), p. 5 (4. Formulating 3D Gaussians as 2D Atlas), metrics p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 3 (3. GaussianVerse), p. 5 (5. 2D Diffusion for 3D Gaussian Generation), baselines p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 3 (3. GaussianVerse), p. 4 (3. GaussianVerse), p. 6 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (3. GaussianVerse), p. 5 (4. Formulating 3D Gaussians as 2D Atlas).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
