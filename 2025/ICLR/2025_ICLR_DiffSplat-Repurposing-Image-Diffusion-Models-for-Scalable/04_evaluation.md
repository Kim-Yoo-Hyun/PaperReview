# Evaluation - DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eajZpoQkGK; PDF retrieval source: https://openreview.net/pdf/b34ae6f6d924f7fa749267cf44d0839eaad40dba.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS)): Freezing the original image VAE or its encoder results in poor performance, as Gaussian splat properties differ significantly from natural images.

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** For both reconstruction and image-conditioned generation task, 300 objects from the unseen GSO (Downs et al., 2022) dataset are randomly selected and rendered to serve ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Original Object Input Control A steampunk robot with brass gears and steam pipes A cute cartoon robot ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Results and Comparisions Single image-conditioned generation performance on the GSO dataset is assessed in Table 2, and qualitative results on in-the-wild images are presented in ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Rendering loss plays a crucial role in auto-encoding by ensuring that the VAE is supervised by real datasets rather than being limited by the lightweight ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Decoded splat latents from the image VAE can be interpreted as the original objects in a "special style" or illuminated in a "special environment light", ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Captions of these 3D objects are provided by Cap3D (Luo et al., 2023; 2024).
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** DIFFSPLAT GVGEN LN3Diff DIRECT-3D 3DTopia LGM† GRM† Single Object ↑CLIP Sim.% 30.95 23.66 24.36 24.80 25.55 29.96 28.19 ↑CLIP R-Prec.% 81.00 23.25 27.25 30.75 34.50 ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Training Objectives DIFFSPLAT can perform well with merely the regular diffusion loss by setting λrender = 0 given high-quality splat latents.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A IMPLEMENTATION DETAILS (p. 17); B MORE VISUALIZATION RESULTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Freezing the original image VAE or its encoder results in poor performance, as Gaussian splat properties differ significantly from natural images. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | VAEs from SD1.5 and SDXL (Podell et al., 2024) have a similar performance with the same dimension (d = 4) of latent space, while ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results and Comparisions Single image-conditioned generation performance on the GSO dataset is assessed in Table 2, and qualitative results on in-the-wild images are presented ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | More visualization results are provided in Appendix Figure 9, 10 and 11. | p. 6 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results and Comparisions As demonstrated in Table 1 and Figure 3, DIFFSPLAT exhibits the best prompt alignment and visual quality among cutting-edge text-conditioned 3D ... | p. 6 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** For both reconstruction and image-conditioned generation task, 300 objects from the unseen GSO (Downs et al., 2022) dataset are randomly selected and rendered to serve ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Original Object Input Control A steampunk robot with brass gears and steam pipes A cute cartoon robot ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Results and Comparisions Single image-conditioned generation performance on the GSO dataset is assessed in Table 2, and qualitative results on in-the-wild images are presented in ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Rendering loss plays a crucial role in auto-encoding by ensuring that the VAE is supervised by real datasets rather than being limited by the lightweight ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Decoded splat latents from the image VAE can be interpreted as the original objects in a "special style" or illuminated in a "special environment light", ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Captions of these 3D objects are provided by Cap3D (Luo et al., 2023; 2024).
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** DIFFSPLAT GVGEN LN3Diff DIRECT-3D 3DTopia LGM† GRM† Single Object ↑CLIP Sim.% 30.95 23.66 24.36 24.80 25.55 29.96 28.19 ↑CLIP R-Prec.% 81.00 23.25 27.25 30.75 34.50 ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Training Objectives DIFFSPLAT can perform well with merely the regular diffusion loss by setting λrender = 0 given high-quality splat latents.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison with Previous 3D Diffusion Generative Models. (1) Native 3D methods and (2) rendering-based methods encounter challenges in training 3D diffusion models from ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Method Overview. (1) A lightweight reconstruction model provides high-quality struc- tured representation for "pseudo" dataset curation. (2) Image VAE is fine-tuned to encode ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative Results and Comparisons on Text-conditioned 3D Generation. More visualizations of DIFFSPLAT results are provided in Appendix Figure 9, 10 and 11.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitive evaluations on T3Bench prompts for text-conditioned generation. † indicates reconstruction-based methods that require additional text-conditioned multi-view generative models. DIFFSPLAT GVGEN LN3Diff DIRECT-3D ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative Results and Comparisons on Image-conditioned 3D Generation. More visualizations of DIFFSPLAT results are provided in Appendix Figure 12, 13 and 14.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative evaluations on GSO for image-conditioned generation. † indicates reconstruc- tion methods that require additional image generation models for single image-to-3D generation. DIFFSPLAT ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Controllable Generation. ControlNet can seamlessly adapt to DIFFSPLAT for control- lable text-to-3D generation in various formats, such as normal and depth maps, and ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation study of inputs for structured splat reconstruction. ↑PSNR ↑SSIM ↓LPIPS #Param. LGM 26.48

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For both reconstruction and image-conditioned generation task, 300 objects from the unseen GSO (Downs et al., 2022) dataset are randomly selected and rendered to ... | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Task/environment | Published as a conference paper at ICLR 2025 Original Object Input Control A steampunk robot with brass gears and steam pipes A cute cartoon ... | reset, timeout, object/scene variation | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3 METHOD), p. 5 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| CLIP similarity score (Radford et al., 2021) and CLIP R-Precision (Park et al., 2021) based on ViT-B/32 are used to measure the alignment of ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| DIFFSPLAT GVGEN LN3Diff DIRECT-3D 3DTopia LGM† GRM† Single Object ↑CLIP Sim.% 30.95 23.66 24.36 24.80 25.55 29.96 28.19 ↑CLIP R-Prec.% 81.00 23.25 27.25 30.75 ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Figure 2: Method Overview. (1) A lightweight reconstruction model provides high-quality struc- tured representation for "pseudo" dataset curation. (2) Image VAE is fine-tuned to ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| However, as shown in Table 5 and Figure 6, the proposed 3D rendering loss Lrender can further boost both the aesthetic quality and geometric ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| 29.87 0.961 0.028 42M Ours 30.09 0.963 0.027 42M Table 4: Ablation study for Gaussian splat property auto-encoding strategies. ↑PSNR ↑SSIM ↓LPIPS Frozen VAE ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Table 5: Ablation study of DIFFSPLAT design choices. T3Bench-300 GSO-300 ↑CLIP Sim.% ↑CLIP R-Prec.% ↑ImageReward ↑PSNR ↑SSIM | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 1: Comparison with Previous 3D Diffusion Generative Models. (1) Native 3D methods and (2) rendering-based methods encounter challenges in training 3D diffusion models ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Results and Comparisions As demonstrated in Table 1 and Figure 3, DIFFSPLAT exhibits the best prompt alignment and visual quality among cutting-edge text-conditioned 3D ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.3 IMAGE-CONDITIONED GENERATION Baselines Two up-to-date native 3D models that support image-conditioned generation are compared here: the concurrent work 3DTopia-XL (Chen et al., 2024d) ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| 4.2 TEXT-CONDITIONED GENERATION Baselines Four state-of-the-art open-sourced methods that support native text-to-3D generation are evaluated, where GVGEN (He et al., 2024) uses Gaussian volume ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| DIFFSPLAT delivers accurate 3D content aligned with input images while maintaining strong geometric fidelity compared to other state-of-the-art methods. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Ablation studies are conducted based on Stable Diffusion V1.5 (SD1.5) (Rombach et al., 2022) unless otherwise specified. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Gaussian Splatting-based large reconstruction model LGM (Tang et al., 2024) and GRM (Xu et al., 2024c) are also evaluated with sparse-view RGB images for ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2025 Input Image InstantMesh LGM DiffSplat (Ours) LN3Diff 3DTopia-XL Figure 4: Qualitative Results and Comparisons on Image-conditioned ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation studies are conducted based on Stable Diffusion V1.5 (SD1.5) (Rombach et al., 2022) unless otherwise specified. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| 4.5 ABLATION AND ANALYSIS We carefully investigate each design choice for splat latent reconstruction and DIFFSPLAT 3D generation in this subsection. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| With the advancements in base models, DIFFSPLAT consistently benefits in both text- and image-conditioned tasks, indicating that the proposed method effectively leverages priors from ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| 29.87 0.961 0.028 42M Ours 30.09 0.963 0.027 42M Table 4: Ablation study for Gaussian splat property auto-encoding strategies. ↑PSNR ↑SSIM ↓LPIPS Frozen VAE ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2025 Table 5: Ablation study of DIFFSPLAT design choices. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Figure 1: Comparison with Previous 3D Diffusion Generative Models. (1) Native 3D methods and (2) rendering-based methods encounter challenges in training 3D diffusion models ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To overcome the drawbacks of previous works, we present DIFFSPLAT, a novel 3D generative framework that exhibits multi-view consistency and effectively leverages generative priors ... | Freezing the original image VAE or its encoder results in poor performance, as Gaussian splat properties differ significantly from natural images. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | VAEs from SD1.5 and SDXL (Podell et al., 2024) have a similar performance with the same dimension (d = 4) of latent space, while ... | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** For both reconstruction and image-conditioned generation task, 300 objects from the unseen GSO (Downs et al., 2022) dataset are randomly selected and rendered to serve ...
- **p. 17 / A IMPLEMENTATION DETAILS - extractive PDF cue:** The flowbased model, i.e., SD3 (Esser et al., 2024) uses the original flow matching Euler ODE solver (Lipman et al., 2023) with 28 steps, consistent ...
- **p. 17 / A IMPLEMENTATION DETAILS - extractive PDF cue:** The flowbased model, i.e., SD3 (Esser et al., 2024) uses the original flow matching Euler ODE solver (Lipman et al., 2023) with 28 steps, consistent ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and Future Work Although DIFFSPLAT delivers decent results, the conversion of its 3DGS representation to high-quality mesh remains an unsolved problem. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Moreover, we only utilize rendered multi-view datasets in this work, which does not fully exploit the scalability potential of the proposed method. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Moreover, while most previous reconstruction methods cannot incorporate text understanding, the flexible conditioning design allows DIFFSPLAT to perform text-guided reconstruction from single-view ambiguous images, ... | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | However, the training process becomes unstable and slow to converge, and gets over-saturated results. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Base Text-to-image Diffusion Models Various popular open-source large text-to-image diffusion models are investigated in this work, including SD1.5 (Rombach et al., 2022), SDXL (Podell ... | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For diffusion models, the batch size and peak learning rate are 128 and 1e-4 respectively. | p. 17 (A IMPLEMENTATION DETAILS) |
| Training batch size for reconstruction and auto-encoding is 64 in total across up to 16 A100 GPUs with gradient accumulation and the peak learning ... | p. 17 (A IMPLEMENTATION DETAILS) |
| Implementation details are provided in Appendix A. | p. 6 (4 EXPERIMENTS) |
| Image generative models for these reconstruction methods are selected following their original implementations. | p. 7 (4 EXPERIMENTS) |
| Freezing the original image VAE or its encoder results in poor performance, as Gaussian splat properties differ significantly from natural images. | p. 8 (4 EXPERIMENTS) |
| Rendering loss plays a crucial role in auto-encoding by ensuring that the VAE is supervised by real datasets rather than being limited by the ... | p. 8 (4 EXPERIMENTS) |
| Splat latents encoded by a fine-tuned VAE are decoded by the original image VAE. | p. 9 (4 EXPERIMENTS) |
| As shown in Figure 7, auto-encoded Gaussian splat properties are presented as RGB or grayscale images. | p. 9 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Limitations and Future Work Although DIFFSPLAT delivers decent results, the conversion of its 3DGS representation to high-quality mesh remains an unsolved problem.
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Moreover, we only utilize rendered multi-view datasets in this work, which does not fully exploit the scalability potential of the proposed method.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Moreover, while most previous reconstruction methods cannot incorporate text understanding, the flexible conditioning design allows DIFFSPLAT to perform text-guided reconstruction from single-view ambiguous images, as ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** However, the training process becomes unstable and slow to converge, and gets over-saturated results.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Base Text-to-image Diffusion Models Various popular open-source large text-to-image diffusion models are investigated in this work, including SD1.5 (Rombach et al., 2022), SDXL (Podell et ...

- **PDF anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), metrics p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 4 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (Figure/Table caption), baselines p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), results p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
