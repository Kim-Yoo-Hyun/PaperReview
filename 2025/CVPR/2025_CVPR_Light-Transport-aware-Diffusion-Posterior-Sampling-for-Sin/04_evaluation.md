# Evaluation - Light Transport-aware Diffusion Posterior Sampling for Single-View Reconstruction of 3D Volumes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Leonard_Light_Transport-aware_Diffusion_Posterior_Sampling_for_Single-View_Reconstruction_of_3D_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Leonard_Light_Transport-aware_Diffusion_Posterior_Sampling_for_Single-View_Reconstruction_of_3D_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.6. Recovering Light Conditions), p. 7 (5.5. Comparative Evaluation), p. 6 (5.2. Monoplanar Representation), p. 6 (5.1. Diffusion Posterior Sampling), p. 7 (5.2. Monoplanar Representation), p. 8 (5.6. Recovering Light Conditions)): Experimental results demonstrate that our approach provides robust generalization and achieves quality and performance that significantly exceed existing methods.

## Evaluation Body Digest

- **p. 4 / 4.1. Cloudy - a 3D Clouds Dataset - extractive body cue:** First, we create a dataset consisting of 1,000 synthetic clouds using the JangaFX fluid simulator [21].
- **p. 6 / 5.1. Diffusion Posterior Sampling - extractive body cue:** 5 demonstrates this with a cloud from the Cloudy dataset, which is rendered with an environmental sky model Figure 5.
- **p. 8 / 5.5. Comparative Evaluation - extractive body cue:** The table shows average values over 32 test cases, each constructed using clouds, materials, cameras, and environment settings sampled from 16 unseen clouds, 3 distinct ...
- **p. 4 / 4.1. Cloudy - a 3D Clouds Dataset - extractive body cue:** The simulator is configured to emulate the evolution and dynamics of gaseous substances, capturing realistic buoyancy, turbulence, and diffusion essential for producing the lifelike flow ...
- **p. 7 / 5.5. Comparative Evaluation - extractive body cue:** The reconstructions using DRT and SPS show that while both techniques can overfit to a single view, they struggle to constrain unseen parts of the ...
- **p. 8 / 5.5. Comparative Evaluation - extractive body cue:** Bottom: Evolution of the recovered background (top) and environment (bottom).
- **p. 8 / 5.6. Recovering Light Conditions - extractive body cue:** Experimental results demonstrate that our approach provides robust generalization and achieves quality and performance that significantly exceed existing methods.
- **p. 6 / 5. Results - extractive body cue:** In this section, we demonstrate the effectiveness of our method for different use cases.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4.1. Cloudy - a 3D Clouds Dataset (p. 4); 5. Results (p. 6); 5.5. Comparative Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.6. Recovering Light Conditions | EMPIRICAL / SIMULATION | Experimental results demonstrate that our approach provides robust generalization and achieves quality and performance that significantly exceed existing methods. | p. 8 (5.6. Recovering Light Conditions) |
| 5.5. Comparative Evaluation | EMPIRICAL / SIMULATION | Since both DRT and SPS require multiple views to achieve accurate results, we tested with one and three images for the reconstructions. | p. 7 (5.5. Comparative Evaluation) |
| 5.2. Monoplanar Representation | EMPIRICAL / SIMULATION | To assess the quality that is achieved with the proposed monoplanar latent representation, we perform a series of experiments with the monoplanar, triplanar and ... | p. 6 (5.2. Monoplanar Representation) |
| 5.1. Diffusion Posterior Sampling | EMPIRICAL / SIMULATION | While an exact match with the given observation cannot be achieved - since the denoiser cannot perfectly reproduce the corresponding 3D cloud - the ... | p. 6 (5.1. Diffusion Posterior Sampling) |
| 5.2. Monoplanar Representation | EMPIRICAL / SIMULATION | Our proposed monoplanar representation quantitatively outperforms the other state-of-the-art representations in terms of reconstruction fidelity. | p. 7 (5.2. Monoplanar Representation) |

## Dataset / Benchmark Role

- **p. 4 / 4.1. Cloudy - a 3D Clouds Dataset - extractive body cue:** First, we create a dataset consisting of 1,000 synthetic clouds using the JangaFX fluid simulator [21].
- **p. 6 / 5.1. Diffusion Posterior Sampling - extractive body cue:** 5 demonstrates this with a cloud from the Cloudy dataset, which is rendered with an environmental sky model Figure 5.
- **p. 8 / 5.5. Comparative Evaluation - extractive body cue:** The table shows average values over 32 test cases, each constructed using clouds, materials, cameras, and environment settings sampled from 16 unseen clouds, 3 distinct ...
- **p. 4 / 4.1. Cloudy - a 3D Clouds Dataset - extractive body cue:** The simulator is configured to emulate the evolution and dynamics of gaseous substances, capturing realistic buoyancy, turbulence, and diffusion essential for producing the lifelike flow ...
- **p. 7 / 5.5. Comparative Evaluation - extractive body cue:** The reconstructions using DRT and SPS show that while both techniques can overfit to a single view, they struggle to constrain unseen parts of the ...
- **p. 8 / 5.5. Comparative Evaluation - extractive body cue:** Bottom: Evolution of the recovered background (top) and environment (bottom).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Given a single view (y) of a volume (V ), we reconstruct a volume ( ˆV ) from its latent representation (θ) that ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Top images: Cloudy Dataset - Photorealistic renderings of randomly selected clouds from our dataset, illustrating natural variations and details. Bottom images: Diffusion-based cloud ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Implicit monoplanar representation. which are rendered under different lighting conditions. The density fields are numerically simulated on regular 3D grids at a resolution ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Diffusion Sampling. First column: A cloud from the Cloudy dataset. Subsequent columns show clouds generated by our diffusion model. First row shows the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Diffusion Posterior Sampling. Given an observation and a differentiable process (differentiable volume rendering in our application), the denoising process is guided step-by-step to- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quality metrics for different latent representations. 16168
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative comparison. Left: Cross-sections of a cloud and its reconstructions using different latent representations are shown. Right: Convergence graphs of the reconstruction loss ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Cloud Super-Resolution. From a cloud on a 32×16×32 grid (center), the diffuser reconstructs a density distribution on a 256 × 128 × 256 ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | First, we create a dataset consisting of 1,000 synthetic clouds using the JangaFX fluid simulator [21]. | embodiment, simulator version and control stack | p. 4 (4.1. Cloudy - a 3D Clouds Dataset), p. 6 (5.1. Diffusion Posterior Sampling) |
| Task/environment | 5 demonstrates this with a cloud from the Cloudy dataset, which is rendered with an environmental sky model Figure 5. | reset, timeout, object/scene variation | p. 6 (5.1. Diffusion Posterior Sampling), p. 8 (5.5. Comparative Evaluation) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.2. Diffusion Posterior Sampling), p. 3 (3.3. Differentiable Rendering with a Diffusion Prior) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (4.4. Parameterized Posterior Sampling), p. 4 (4. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Experimental results demonstrate that our approach provides robust generalization and achieves quality and performance that significantly exceed existing methods. | definition/direction/unit from same section | p. 8 (5.6. Recovering Light Conditions) |
| In this section, we demonstrate the effectiveness of our method for different use cases. | definition/direction/unit from same section | p. 6 (5. Results) |
| 5 demonstrates this with a cloud from the Cloudy dataset, which is rendered with an environmental sky model Figure 5. | definition/direction/unit from same section | p. 6 (5.1. Diffusion Posterior Sampling) |
| Right: Convergence graphs of the reconstruction loss over 50,000 steps, measured at 128K uniform sampled positions. | definition/direction/unit from same section | p. 7 (5.2. Monoplanar Representation) |
| Since both DRT and SPS require multiple views to achieve accurate results, we tested with one and three images for the reconstructions. | definition/direction/unit from same section | p. 7 (5.5. Comparative Evaluation) |
| With the availability of a few additional views, even more accurate reconstruction can be achieved. | definition/direction/unit from same section | p. 8 (5.6. Recovering Light Conditions) |
| Figure 2. Top images: Cloudy Dataset - Photorealistic renderings of randomly selected clouds from our dataset, illustrating natural variations and details. Bottom images: Diffusion-based ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 4. Diffusion Sampling. First column: A cloud from the Cloudy dataset. Subsequent columns show clouds generated by our diffusion model. First row shows ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our proposed monoplanar representation quantitatively outperforms the other state-of-the-art representations in terms of reconstruction fidelity. | comparison identity and matched condition | p. 7 (5.2. Monoplanar Representation) |
| Quality comparison of DRT, SPS and DPS (ours) using one and three views for reconstruction. | comparison identity and matched condition | p. 8 (5.5. Comparative Evaluation) |
| This could lead to incorrect reconstructions, as certain parts of the cloud may be explained without actually being recovered. | comparison identity and matched condition | p. 8 (5.6. Recovering Light Conditions) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This could lead to incorrect reconstructions, as certain parts of the cloud may be explained without actually being recovered. | component/input/data sensitivity | p. 8 (5.6. Recovering Light Conditions) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce our novel monoplanar latent representation to effectively compress the cloud database (see Section 4.2), and we demonstrate how to prevent overfitting by ... | Experimental results demonstrate that our approach provides robust generalization and achieves quality and performance that significantly exceed existing methods. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.6. Recovering Light Conditions), p. 7 (5.5. Comparative Evaluation), p. 6 (5.2. Monoplanar Representation), p. 6 (5.1. Diffusion Posterior Sampling), p. 7 (5.2. Monoplanar Representation), p. 8 (5.6. Recovering Light Conditions) |
| Primary metric/result | Since both DRT and SPS require multiple views to achieve accurate results, we tested with one and three images for the reconstructions. | numeric claim only at cited anchor | p. 7 (5.5. Comparative Evaluation) |

- Numeric sentences retained from the body:
- **p. 6 / 5.2. Monoplanar Representation - extractive body cue:** All representations use the same number of parameters for the latent, i.e.: Monoplanar 128 × 128 × 32, Triplanar 3×128×128×11, and Grid 32×32×32×16.
- **p. 7 / 5.2. Monoplanar Representation - extractive body cue:** Right: Convergence graphs of the reconstruction loss over 50,000 steps, measured at 128K uniform sampled positions.
- **p. 7 / 5.2. Monoplanar Representation - extractive body cue:** While PSNR, RMSE, and MAE consider the full volume at 256×128×256 resolution, SSIM [71] considers the center slice.
- **p. 7 / 5.4. Cloud Recovery from Transmittance Measures - extractive body cue:** From a cloud on a 32×16×32 grid (center), the diffuser reconstructs a density distribution on a 256 × 128 × 256 grid (right).
- **p. 8 / 5.5. Comparative Evaluation - extractive body cue:** Target+ Target+ Target Test View DRT1 0.0275 30 min 11 s 0.3918 DRT3 0.0247 47 min 33 s 0.1361 SPS1 0.0132 30 min 24 s ...
- **p. 8 / 5.5. Comparative Evaluation - extractive body cue:** Target Test View Background 0.0323 11 min 57 s 0.1131 Environment 0.0342 27 min 2 s 0.1740 Figure 10.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While an exact match with the given observation cannot be achieved - since the denoiser cannot perfectly reproduce the corresponding 3D cloud - the ... | p. 6 (5.1. Diffusion Posterior Sampling) |
| body limitation/failure cue | A notable limitation is the ambiguity between what is represented by θ and ϕ. | p. 8 (5.6. Recovering Light Conditions) |
| body limitation/failure cue | If no proper regularization for ϕ is applied, the interleaved optimization of θ and ϕ may fall into local minima. | p. 8 (5.6. Recovering Light Conditions) |
| body limitation/failure cue | To add natural randomness and represent diverse distributions of warm columns to the clouds, we apply Perlin noise functions and varied particle emission shapes. | p. 4 (4.1. Cloudy - a 3D Clouds Dataset) |
| body limitation/failure cue | The result shows how the denoiser is guided by the cloud's appearance, which is considered by the differentiable renderer, rather than performing unconditional denoising ... | p. 6 (5.1. Diffusion Posterior Sampling) |
| body limitation/failure cue | The last setting aligns with diffuse-denoise strategies, progressively adjusting the initial noise toward the observed data to improve guidance stability. | p. 7 (5.5. Comparative Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Here, ζ is a hyperparameter that balances prior enforcement with observation fidelity by accounting for normalization and the noise level of the measurement (see ... | p. 3 (3.2. Diffusion Posterior Sampling) |
| Additionally, it provides a method to compute how the gradients of a loss function with respect to the rendered image, ∇RL, propagate through all ... | p. 3 (3.3. Differentiable Rendering with a Diffusion Prior) |
| The final latent code is about 2MB. | p. 4 (4.2. Volume Latent Encoding) |
| The monoplanar representation model is trained jointly on a subset of the clouds from the Cloudy dataset, sharing the parameters for the upsampler and ... | p. 4 (4.2. Volume Latent Encoding) |
| Gradients of the grid can be backpropagated through the model after they are computed. | p. 5 (4.2. Volume Latent Encoding) |
| A grid only requires trilinear interpolation on the GPU, making it easier to integrate and evaluate in a differentiable renderer. | p. 5 (4.2. Volume Latent Encoding) |
| on refining other aspects of the rendering, such as finer details and complex scene parameters, in the subsequent steps. | p. 6 (4.5. Optimization) |
| In practice we applied it a few steps around the middle of the process, to avoid early local minima in the beginning and artifacts ... | p. 6 (4.5. Optimization) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.1. Diffusion Posterior Sampling - extractive body cue:** While an exact match with the given observation cannot be achieved - since the denoiser cannot perfectly reproduce the corresponding 3D cloud - the reconstruction ...
- **p. 8 / 5.6. Recovering Light Conditions - extractive body cue:** A notable limitation is the ambiguity between what is represented by θ and ϕ.
- **p. 8 / 5.6. Recovering Light Conditions - extractive body cue:** If no proper regularization for ϕ is applied, the interleaved optimization of θ and ϕ may fall into local minima.
- **p. 4 / 4.1. Cloudy - a 3D Clouds Dataset - extractive body cue:** To add natural randomness and represent diverse distributions of warm columns to the clouds, we apply Perlin noise functions and varied particle emission shapes.
- **p. 6 / 5.1. Diffusion Posterior Sampling - extractive body cue:** The result shows how the denoiser is guided by the cloud's appearance, which is considered by the differentiable renderer, rather than performing unconditional denoising based ...
- **p. 7 / 5.5. Comparative Evaluation - extractive body cue:** The last setting aligns with diffuse-denoise strategies, progressively adjusting the initial noise toward the observed data to improve guidance stability.

- **Evidence anchors reviewed:** datasets p. 4 (4.1. Cloudy - a 3D Clouds Dataset), p. 6 (5.1. Diffusion Posterior Sampling), p. 8 (5.5. Comparative Evaluation), p. 4 (4.1. Cloudy - a 3D Clouds Dataset), p. 7 (5.5. Comparative Evaluation), p. 8 (5.5. Comparative Evaluation), metrics p. 8 (5.6. Recovering Light Conditions), p. 6 (5. Results), p. 6 (5.1. Diffusion Posterior Sampling), p. 7 (5.2. Monoplanar Representation), p. 7 (5.5. Comparative Evaluation), p. 8 (5.6. Recovering Light Conditions), baselines p. 7 (5.2. Monoplanar Representation), p. 8 (5.5. Comparative Evaluation), p. 8 (5.6. Recovering Light Conditions), results p. 8 (5.6. Recovering Light Conditions), p. 7 (5.5. Comparative Evaluation), p. 6 (5.2. Monoplanar Representation), p. 6 (5.1. Diffusion Posterior Sampling), p. 7 (5.2. Monoplanar Representation), p. 8 (5.6. Recovering Light Conditions).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
