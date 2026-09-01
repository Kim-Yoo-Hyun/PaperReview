# Evaluation - Score-Based Generative Modeling through Stochastic Differential Equations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.13456; PDF retrieval source: https://arxiv.org/pdf/2011.13456. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (ABSTRACT), p. 6 (2 BACKGROUND), p. 9 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND)): Combined with multiple architectural improvements, we achieve record-breaking performance for unconditional image generation on CIFAR-10 with an Inception score of 9.89 and FID of 2.20, a competitive likelihood of 2.99 ...

## Evaluation Body Digest

- **p. 3 / 2 BACKGROUND - extractive PDF cue:** 3.1 PERTURBING DATA WITH SDES Our goal is to construct a diffusion process txptquT t"0 indexed by a continuous time variable t P r0, Ts, ...
- **p. 7 / 2 BACKGROUND - extractive PDF cue:** As an example, we report negative log-likelihoods (NLLs) measured in bits/dim on the CIFAR-10 dataset in Table 2.
- **p. 9 / 2 BACKGROUND - extractive PDF cue:** Since the forward SDE is tractable, we can easily create training data pxptq, yq for the time-dependent classifier by first sampling pxp0q, yq from a ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (3) is also a weighted sum of denoising score matching objectives, which implies that the optimal model, sθ˚p˜x, iq, matches the score of the perturbed ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** (7) uses denoising score matching, but other score matching objectives, such as sliced 4
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** We test PC samplers on SMLD and DDPM models (see Algorithms 2 and 3 in Appendix G) trained with original discrete objectives given by Eqs.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| ABSTRACT | SYSTEM / EVALUATION SCOPE UNRESOLVED | Combined with multiple architectural improvements, we achieve record-breaking performance for unconditional image generation on CIFAR-10 with an Inception score of 9.89 and FID of ... | p. 1 (ABSTRACT) |
| 2 BACKGROUND | SYSTEM / EVALUATION SCOPE UNRESOLVED | We observe that our reverse diffusion sampler always outperform ancestral sampling, and corrector-only methods (C2000) perform worse than other competitors (P2000, PC1000) with the ... | p. 6 (2 BACKGROUND) |
| 2 BACKGROUND | SYSTEM / EVALUATION SCOPE UNRESOLVED | 4 (right) shows results for inpainting and colorization achieved with unconditional time-dependent score-based models. | p. 9 (2 BACKGROUND) |
| 1 INTRODUCTION | SYSTEM / EVALUATION SCOPE UNRESOLVED | The former unifies and improves over existing sampling methods for score-based models. | p. 2 (1 INTRODUCTION) |
| 1 INTRODUCTION | SYSTEM / EVALUATION SCOPE UNRESOLVED | Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that ... | p. 2 (1 INTRODUCTION) |

## Dataset / Benchmark Role

- **p. 3 / 2 BACKGROUND - extractive PDF cue:** 3.1 PERTURBING DATA WITH SDES Our goal is to construct a diffusion process txptquT t"0 indexed by a continuous time variable t P r0, Ts, ...
- **p. 7 / 2 BACKGROUND - extractive PDF cue:** As an example, we report negative log-likelihoods (NLLs) measured in bits/dim on the CIFAR-10 dataset in Table 2.
- **p. 9 / 2 BACKGROUND - extractive PDF cue:** Since the forward SDE is tractable, we can easily create training data pxptq, yq for the time-dependent classifier by first sampling pxp0q, yq from a ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (3) is also a weighted sum of denoising score matching objectives, which implies that the optimal model, sθ˚p˜x, iq, matches the score of the perturbed ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** (7) uses denoising score matching, but other score matching objectives, such as sliced 4
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** We test PC samplers on SMLD and DDPM models (see Algorithms 2 and 3 in Appendix G) trained with original discrete objectives given by Eqs.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Solving a reverse- time SDE yields a score-based generative model. Transform- ing data to a simple noise dis- tribution can be accomplished with ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of score-based generative modeling through SDEs. We can map data to a noise distribution (the prior) with an SDE (Section 3.1), and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Comparing different reverse-time SDE solvers on CIFAR-10. Shaded regions are obtained with the same computation (number of score function evaluations). Mean and standard ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: NLLs and FIDs (ODE) on CIFAR-10.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3: Probability flow ODE enables fast sampling with adaptive stepsizes as the numerical precision is varied (left), and reduces the number of score function ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 4: Left: Class-conditional samples on 32 ˆ 32 CIFAR-10. Top four rows are automobiles and bottom four rows are horses. Right: Inpainting (top two ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 5: Discrete-time perturbation kernels and our continuous generalizations match each other almost exactly. (a) compares the variance of perturbation kernels for SMLD and VE ...
- **p. 19 / Figure/Table caption - extractive PDF cue:** Fig. 7. In Fig. 8, we show the dimension-wise differences and correlation coefficients between latent encodings on a total of 16 CIFAR-10 images. Our results ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3.1 PERTURBING DATA WITH SDES Our goal is to construct a diffusion process txptquT t"0 indexed by a continuous time variable t P r0, ... | embodiment, simulator version and control stack | p. 3 (2 BACKGROUND), p. 7 (2 BACKGROUND) |
| Task/environment | As an example, we report negative log-likelihoods (NLLs) measured in bits/dim on the CIFAR-10 dataset in Table 2. | reset, timeout, object/scene variation | p. 7 (2 BACKGROUND), p. 9 (2 BACKGROUND) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Comparing different reverse-time SDE solvers on CIFAR-10. Shaded regions are obtained with the same computation (number of score function evaluations). Mean and ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Combined with multiple architectural improvements, we achieve record-breaking performance for unconditional image generation on CIFAR-10 with an Inception score of 9.89 and FID of ... | definition/direction/unit from same section | p. 1 (ABSTRACT) |
| Figure 3: Probability flow ODE enables fast sampling with adaptive stepsizes as the numerical precision is varied (left), and reduces the number of score ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples. | definition/direction/unit from same section | p. 1 (ABSTRACT) |
| 3 SCORE-BASED GENERATIVE MODELING WITH SDES Perturbing data with multiple noise scales is key to the success of previous methods. | definition/direction/unit from same section | p. 3 (2 BACKGROUND) |
| Figure 2: Overview of score-based generative modeling through SDEs. We can map data to a noise distribution (the prior) with an SDE (Section 3.1), ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| 4 SOLVING THE REVERSE SDE After training a time-dependent score-based model sθ, we can use it to construct the reverse-time SDE and then simulate ... | definition/direction/unit from same section | p. 5 (2 BACKGROUND) |
| Published as a conference paper at ICLR 2021 100 101 102 103 Evaluation number 0.0 0.5 1.0 Evaluation timepoint ODE Evaluation Points Precision 1e-1 ... | definition/direction/unit from same section | p. 8 (2 BACKGROUND) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (7) (i.e., DDPM cont.), which further improves the likelihood; (iii) With sub-VP SDEs, we always get higher likelihoods compared to VP SDEs; (iv) With ... | comparison identity and matched condition | p. 7 (2 BACKGROUND) |
| Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that ... | comparison identity and matched condition | p. 2 (1 INTRODUCTION) |
| We observe that our reverse diffusion sampler always outperform ancestral sampling, and corrector-only methods (C2000) perform worse than other competitors (P2000, PC1000) with the ... | comparison identity and matched condition | p. 6 (2 BACKGROUND) |
| Figure 8: Left: The dimension-wise difference between encodings obtained by Model A and B. As a baseline, we also report the difference between shuffled ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |
| This enables applications such as class-conditional generation, image inpainting, colorization and other inverse problems, all achievable using a single unconditional score-based model without re-training. | comparison identity and matched condition | p. 2 (1 INTRODUCTION) |
| 9 (Appendix G), we additionally provide qualitative comparison for 6 | comparison identity and matched condition | p. 6 (2 BACKGROUND) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This enables applications such as class-conditional generation, image inpainting, colorization and other inverse problems, all achievable using a single unconditional score-based model without re-training. | component/input/data sensitivity | p. 2 (1 INTRODUCTION) |
| A variational Markov chain in the reverse direction is parameterized with pθpxi´1/xiq " Npxi´1; 1 ?1´βi pxi`βisθpxi, iqq, βiIq, and trained with a re-weighted ... | component/input/data sensitivity | p. 3 (2 BACKGROUND) |
| Moreover, it is typically better than doubling the number of predictor steps without adding a corrector (P2000), where we have to interpolate between noise ... | component/input/data sensitivity | p. 6 (2 BACKGROUND) |
| (7) (i.e., DDPM cont.), which further improves the likelihood; (iii) With sub-VP SDEs, we always get higher likelihoods compared to VP SDEs; (iv) With ... | component/input/data sensitivity | p. 7 (2 BACKGROUND) |
| Surprisingly, we can achieve better FID than the previous best conditional generative model without requiring labeled data. | component/input/data sensitivity | p. 8 (2 BACKGROUND) |
| With a larger error tolerance, the number of function evaluations can be reduced by over 90% without affecting the visual quality of samples (Fig. | component/input/data sensitivity | p. 8 (2 BACKGROUND) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting ... | Combined with multiple architectural improvements, we achieve record-breaking performance for unconditional image generation on CIFAR-10 with an Inception score of 9.89 and FID of ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (ABSTRACT), p. 6 (2 BACKGROUND), p. 9 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND) |
| Primary metric/result | We observe that our reverse diffusion sampler always outperform ancestral sampling, and corrector-only methods (C2000) perform worse than other competitors (P2000, PC1000) with the ... | numeric claim only at cited anchor | p. 6 (2 BACKGROUND) |

- Numeric sentences retained from the body:
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** A variational Markov chain in the reverse direction is parameterized with pθpxi´1/xiq " Npxi´1; 1 ?1´βi pxi`βisθpxi, iqq, βiIq, and trained with a re-weighted variant ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (3), namely σ2 i and p1´αiq, are related to corresponding perturbation kernels in the same functional form: σ2 i 91{Er∥∇x log pσip˜x / xq∥2 2s ...
- **p. 5 / 2 BACKGROUND - extractive PDF cue:** In the limit of N Ñ 8, tσiuN i"1 becomes a function σptq, zi becomes zptq, and the Markov chain txiuN i"1 becomes a continuous ...
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** Mean and standard deviation are reported over five sampling runs. "P1000" or "P2000": predictor-only samplers using 1000 or 2000 steps. "C2000": corrector-only samplers using 2000 ...
- **p. 7 / 2 BACKGROUND - extractive PDF cue:** (deep, sub-VP) 2.99 2.92 Table 3: CIFAR-10 sample quality.
- **p. 9 / 2 BACKGROUND - extractive PDF cue:** We provide class-conditional CIFAR-10 samples in Fig.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work would benefit from improved methods to automatically select and tune these hyperparameters, as well as more extensive investigation on the merits and ... | p. 9 (6 CONCLUSION) |
| body limitation/failure cue | This process progressively diffuses a data point into random noise, and is given by a prescribed SDE that does not depend on the data ... | p. 2 (1 INTRODUCTION) |
| body limitation/failure cue | For ease of presentation we assume the diffusion coefficient is a scalar (instead of a d ˆ d matrix) and does not depend on ... | p. 4 (2 BACKGROUND) |
| body limitation/failure cue | Creating noise from data is easy; creating data from noise is generative modeling. | p. 1 (ABSTRACT) |
| body limitation/failure cue | For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale. | p. 1 (1 INTRODUCTION) |
| body limitation/failure cue | Consider a sequence of positive noise scales σmin " σ1 ă σ2 ă ¨ ¨ ¨ ă σN " σmax. | p. 2 (2 BACKGROUND) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For sampling, Song & Ermon (2019) run M steps of Langevin MCMC to get a sample for each pσipxq sequentially: xm i " xm´1 ... | p. 3 (2 BACKGROUND) |
| For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale. | p. 1 (1 INTRODUCTION) |
| The latter allows for fast adaptive sampling via black-box ODE solvers, flexible data manipulation via latent codes, a uniquely identifiable encoding, and notably, exact ... | p. 2 (1 INTRODUCTION) |
| Since VE, VP and sub-VP SDEs all have affine drift coefficients, their perturbation kernels p0tpxptq / xp0qq are all Gaussian and can be computed ... | p. 5 (2 BACKGROUND) |
| Please find pseudo-code and a complete description in Appendix G. | p. 6 (2 BACKGROUND) |
| Moreover, it is typically better than doubling the number of predictor steps without adding a corrector (P2000), where we have to interpolate between noise ... | p. 6 (2 BACKGROUND) |
| (13), we can encode any datapoint xp0q into a latent space xpTq. | p. 7 (2 BACKGROUND) |
| This allows us to compute the exact likelihood on any input data (details in Appendix D.2). | p. 7 (2 BACKGROUND) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 CONCLUSION - extractive PDF cue:** Future work would benefit from improved methods to automatically select and tune these hyperparameters, as well as more extensive investigation on the merits and limitations ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This process progressively diffuses a data point into random noise, and is given by a prescribed SDE that does not depend on the data and ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** For ease of presentation we assume the diffusion coefficient is a scalar (instead of a d ˆ d matrix) and does not depend on x, ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Creating noise from data is easy; creating data from noise is generative modeling.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 2 / 2 BACKGROUND - extractive PDF cue:** Consider a sequence of positive noise scales σmin " σ1 ă σ2 ă ¨ ¨ ¨ ă σN " σmax.

- **PDF anchors reviewed:** datasets p. 3 (2 BACKGROUND), p. 7 (2 BACKGROUND), p. 9 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), metrics p. 6 (Figure/Table caption), p. 1 (ABSTRACT), p. 8 (Figure/Table caption), p. 1 (ABSTRACT), p. 3 (2 BACKGROUND), p. 4 (Figure/Table caption), baselines p. 7 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 6 (2 BACKGROUND), p. 21 (Figure/Table caption), p. 2 (1 INTRODUCTION), p. 6 (2 BACKGROUND), results p. 1 (ABSTRACT), p. 6 (2 BACKGROUND), p. 9 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
