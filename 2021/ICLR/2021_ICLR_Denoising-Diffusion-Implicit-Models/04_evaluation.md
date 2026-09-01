# Evaluation - Denoising Diffusion Implicit Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.02502; PDF retrieval source: https://arxiv.org/pdf/2010.02502. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 18 (Figure/Table caption)): Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, the FID score of the 100 step DDPM ...

## Evaluation Body Digest

- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** For each dataset, we use the same trained model with T = 1000 and the objective being Lγ from Eq.
- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** (2020) only to obtain the CIFAR10 samples, but not samples of the other datasets.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2021 Table 2: Reconstruction error with DDIM on CIFAR-10 test set, rounded to 10-4.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** We consider encoding and decoding on the CIFAR-10 test set with the CIFAR-10 model with S steps for both encoding and decoding; we report the ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** For the DDPM, the sample quality deteriorates rapidly when the sampling trajectory has 10 steps.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** In Figure 4, we show that the amount of time needed to produce a sample scales linearly with the length of the sample trajectory.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** For the case of ˆσ, the generated images seem to have more noisy perturbations under short trajectories; this explains why the FID scores are much ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, the FID score ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, the FID ... | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In this section, we show that DDIMs outperform DDPMs in terms of image generation when fewer iterations are considered, giving speed ups of 10× ... | p. 6 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The only changes that we make is how we produce samples from the model; we achieve this by controlling τ (which controls how fast ... | p. 6 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | DDIM, on the other hand, achieves high sample quality much more consistently. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our results show that DDIMs have lower reconstruction error for larger S values and have properties similar to Neural ODEs and normalizing flows. | p. 9 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** For each dataset, we use the same trained model with T = 1000 and the objective being Lγ from Eq.
- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** (2020) only to obtain the CIFAR10 samples, but not samples of the other datasets.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2021 Table 2: Reconstruction error with DDIM on CIFAR-10 test set, rounded to 10-4.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** We consider encoding and decoding on the CIFAR-10 test set with the CIFAR-10 model with S steps for both encoding and decoding; we report the ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** For the DDPM, the sample quality deteriorates rapidly when the sampling trajectory has 10 steps.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** In Figure 4, we show that the amount of time needed to produce a sample scales linearly with the length of the sample trajectory.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Graphical models for diffusion (left) and non-Markovian (right) inference models. In Section 3, we generalize the forward diffusion process used by DDPMs, which ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Graphical model for accelerated generation, where τ = [1, 3]. 4.1 DENOISING DIFFUSION IMPLICIT MODELS From pθ(x1:T ) in Eq. (10), one can ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: CIFAR10 and CelebA image generation measured in FID. η = 1.0 and ˆσ are cases of DDPM (although Ho et al. (2020) only ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: CIFAR10 and CelebA samples with dim(τ) = 10 and dim(τ) = 100. 5.1 SAMPLE QUALITY AND EFFICIENCY In Table 1, we report the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Hours to sample 50k images with one Nvidia 2080 Ti GPU and samples at different steps. 10 20 50 100 1000 sample timesteps ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Samples from DDIM with the same random xT and different number of steps. quality are encoded in the parameters, as longer sample trajectories ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Interpolation of samples from DDIM with dim(τ) = 50. Since the high level features of the DDIM sample is encoded by xT , ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Reconstruction error with DDIM on CIFAR-10 test set, rounded to 10-4. S 10 20 50 100 200 500

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For each dataset, we use the same trained model with T = 1000 and the objective being Lγ from Eq. | embodiment, simulator version and control stack | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Task/environment | (2020) only to obtain the CIFAR10 samples, but not samples of the other datasets. | reset, timeout, object/scene variation | p. 6 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 1 (ABSTRACT), p. 2 (2 BACKGROUND) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the case of ˆσ, the generated images seem to have more noisy perturbations under short trajectories; this explains why the FID scores are ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, the FID ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Published as a conference paper at ICLR 2021 Table 2: Reconstruction error with DDIM on CIFAR-10 test set, rounded to 10-4. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| S 10 20 50 100 200 500 1000 Error 0.014 0.0065 0.0023 0.0009 0.0004 0.0001 0.0001 bilistic models, such as GANs (Goodfellow et al., ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| We also consider DDPM where the random noise has a larger standard deviation than σ(1), which we denote as ˆσ: ˆστi = p 1 ... | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| We consider different sub-sequences τ of [1, . . . , T] and different variance hyperparameters σ indexed by elements of τ. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| Figure 2: Graphical model for accelerated generation, where τ = [1, 3]. 4.1 DENOISING DIFFUSION IMPLICIT MODELS From pθ(x1:T ) in Eq. (10), one ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In this section, we show that DDIMs outperform DDPMs in terms of image generation when fewer iterations are considered, giving speed ups of 10× ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| Notably, DDIM is able to produce samples with quality comparable to 1000 step models within 20 to 100 steps, which is a 10× to ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| We observe that DDIM (η = 0) achieves the best sample quality when dim(τ) is small, and DDPM (η = 1 and ˆσ) typically ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| To simplify comparisons, we consider σ with the form: στi(η) = η q (1 -ατi-1)/(1 -ατi) q 1 -ατi/ατi-1, (16) where η ∈R≥0 is ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs). | Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, the FID ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 18 (Figure/Table caption) |
| Primary metric/result | In this section, we show that DDIMs outperform DDPMs in terms of image generation when fewer iterations are considered, giving speed ups of 10× ... | numeric claim only at cited anchor | p. 6 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** (2020) only considered T = 1000 steps, and S < T can be seen as simulating DDPMs trained with S steps), and η = 0.0 ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.1 SAMPLE QUALITY AND EFFICIENCY In Table 1, we report the quality of the generated samples with models trained on CIFAR10 and CelebA, as measured ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** For the DDPM, the sample quality deteriorates rapidly when the sampling trajectory has 10 steps.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Notably, DDIM is able to produce samples with quality comparable to 1000 step models within 20 to 100 steps, which is a 10× to 50× ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, the FID score ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.2 SAMPLE CONSISTENCY IN DDIMS For DDIM, the generative process is deterministic, and x0 would depend only on the initial state xT .

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | DDIMs can also be used to encode samples that reconstruct them from the latent code, which DDPMs cannot do due to the stochastic sampling ... | p. 6 (5 EXPERIMENTS) |
| body limitation/failure cue | The same cannot be said for DDPMs due to their stochastic nature. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | This allows DDIM to control the generated images on a high level directly through the latent variables, which DDPMs cannot. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | We also consider DDPM where the random noise has a larger standard deviation than σ(1), which we denote as ˆσ: ˆστi = p 1 ... | p. 6 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Published as a conference paper at ICLR 2021 10 30 100 300 1000 # steps 0.2 0.5 2 5 20 Hours CIFAR10 10 30 ... | p. 8 (5 EXPERIMENTS) |
| 10 20 50 100 1000 sample timesteps 10 100 sample timesteps 10 100 sample timesteps Figure 5: Samples from DDIM with the same random ... | p. 8 (5 EXPERIMENTS) |
| This is used by the implementation in Ho et al. | p. 6 (5 EXPERIMENTS) |
| We consider different sub-sequences τ of [1, . . . , T] and different variance hyperparameters σ indexed by elements of τ. | p. 6 (5 EXPERIMENTS) |
| For the DDPM, the sample quality deteriorates rapidly when the sampling trajectory has 10 steps. | p. 7 (5 EXPERIMENTS) |
| In Figure 3, we show CIFAR10 and CelebA samples with the same number of sampling steps and varying σ. | p. 7 (5 EXPERIMENTS) |
| 5.4 RECONSTRUCTION FROM LATENT SPACE As DDIM is the Euler integration for a particular ODE, it would be interesting to see whether it can ... | p. 9 (5 EXPERIMENTS) |
| We consider encoding and decoding on the CIFAR-10 test set with the CIFAR-10 model with S steps for both encoding and decoding; we report ... | p. 9 (5 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** DDIMs can also be used to encode samples that reconstruct them from the latent code, which DDPMs cannot do due to the stochastic sampling process.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** The same cannot be said for DDPMs due to their stochastic nature.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** This allows DDIM to control the generated images on a high level directly through the latent variables, which DDPMs cannot.
- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** We also consider DDPM where the random noise has a larger standard deviation than σ(1), which we denote as ˆσ: ˆστi = p 1 -ατi/ατi-1 ...

- **PDF anchors reviewed:** datasets p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), metrics p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), baselines p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), results p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 18 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
