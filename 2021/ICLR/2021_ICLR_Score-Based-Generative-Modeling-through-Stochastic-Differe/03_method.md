# Method - Score-Based Generative Modeling through Stochastic Differential Equations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.13456; PDF retrieval source: https://arxiv.org/pdf/2011.13456. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 6 (2 BACKGROUND)): Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with better architectures and new sampling ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two successful classes of probabilistic generative models involve sequentially corrupting training data with slowly increasing noise, and then learning to reverse this corruption in order ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We can therefore approximate the reverse-time SDE by training a time-dependent neural network to estimate the scores, and then produce samples using numerical SDE solvers.
- **p. 5 / 2 BACKGROUND - extractive body cue:** 4 SOLVING THE REVERSE SDE After training a time-dependent score-based model sθ, we can use it to construct the reverse-time SDE and then simulate it ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 6 / 2 BACKGROUND - extractive body cue:** We test PC samplers on SMLD and DDPM models (see Algorithms 2 and 3 in Appendix G) trained with original discrete objectives given by Eqs.
- **p. 7 / 2 BACKGROUND - extractive body cue:** (2020), we obtain better bits/dim than ELBO, since our likelihoods are exact; (ii) Using the same architecture, we trained another DDPM model with the continuous ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** Song & Ermon (2019) propose to train a Noise Conditional Score Network (NCSN), denoted by sθpx, σq, with a weighted sum of denoising score matching ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** 5 CONTROLLABLE GENERATION The continuous structure of our framework allows us to not only produce data samples from p0, but also from p0pxp0q / yq ...

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two successful classes of probabilistic generative models involve sequentially corrupting training data with slowly increasing noise, and then learning to reverse this corruption in order ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We can therefore approximate the reverse-time SDE by training a time-dependent neural network to estimate the scores, and then produce samples using numerical SDE solvers.
- **p. 5 / 2 BACKGROUND - extractive body cue:** 4 SOLVING THE REVERSE SDE After training a time-dependent score-based model sθ, we can use it to construct the reverse-time SDE and then simulate it ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 6 / 2 BACKGROUND - extractive body cue:** We test PC samplers on SMLD and DDPM models (see Algorithms 2 and 3 in Appendix G) trained with original discrete objectives given by Eqs.
- **p. 7 / 2 BACKGROUND - extractive body cue:** (2020), we obtain better bits/dim than ELBO, since our likelihoods are exact; (ii) Using the same architecture, we trained another DDPM model with the continuous ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we ... | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Two successful classes of probabilistic generative models involve sequentially corrupting training data with slowly increasing noise, and then learning to reverse this ... | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | We can therefore approximate the reverse-time SDE by training a time-dependent neural network to estimate the scores, and then produce samples using ... | p. 2 (1 INTRODUCTION), p. 5 (2 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 BACKGROUND - extractive body cue:** Song & Ermon (2019) propose to train a Noise Conditional Score Network (NCSN), denoted by sθpx, σq, with a weighted sum of denoising score matching ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Score matching with Langevin dynamics (SMLD) (Song & Ermon, 2019) estimates the score (i.e., the gradient of the log probability density with respect to data) ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In addition, we propose two special methods not viable for general SDEs: (i) Predictor-Corrector (PC) samplers that combine numerical SDE solvers with score-based MCMC approaches, ...
- **p. 7 / 2 BACKGROUND - extractive body cue:** (2020), we obtain better bits/dim than ELBO, since our likelihoods are exact; (ii) Using the same architecture, we trained another DDPM model with the continuous ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** (deep, sub-VP), similarly doubles the network depth and achieves a log-likelihood of 2.99 bits/dim with the continuous objective in Eq.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Although, DDPM, recently, reported, achieve, higher, sample, quality, SMLD, Song, Ermon, better, architectures, sampling | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Although, DDPM, recently, reported, achieve, higher, sample, quality, SMLD, Song | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | addition, SDE, under, framework, achieves, likelihood, value, bits/dim, uniformly, dequantized | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Song, Ermon, train, Noise, Conditional, Score, Network, NCSN, denoted, weighted | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 4 / 2 BACKGROUND - extractive body cue:** The SDE has a unique strong solution as long as the coefficients are globally Lipschitz in both state and time (Øksendal, 2003).
- **p. 4 / 2 BACKGROUND - extractive body cue:** A remarkable result from Anderson (1982) states that the reverse of a diffusion process is also a diffusion process, running backwards in time and given ...
- **p. 7 / 2 BACKGROUND - extractive body cue:** This allows us to compute the exact likelihood on any input data (details in Appendix D.2).
- **p. 7 / 2 BACKGROUND - extractive body cue:** Uniquely identifiable encoding Unlike most current invertible models, our encoding is uniquely identifiable, meaning that with sufficient training data, model capacity, and optimization accuracy, the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | This SDE can be reversed if we know the score of the distribution at each intermediate time step, ∇x log ptpxq. et ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | (12) is always bounded by the VP SDE at every intermediate time step (proof in Appendix B). | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two successful classes of probabilistic generative models involve sequentially corrupting training data with slowly increasing noise, and then learning to reverse this corruption in order ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We can therefore approximate the reverse-time SDE by training a time-dependent neural network to estimate the scores, and then produce samples using numerical SDE solvers.
- **p. 5 / 2 BACKGROUND - extractive body cue:** 4 SOLVING THE REVERSE SDE After training a time-dependent score-based model sθ, we can use it to construct the reverse-time SDE and then simulate it ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 6 / 2 BACKGROUND - extractive body cue:** We test PC samplers on SMLD and DDPM models (see Algorithms 2 and 3 in Appendix G) trained with original discrete objectives given by Eqs.
- **p. 7 / 2 BACKGROUND - extractive body cue:** (2020), we obtain better bits/dim than ELBO, since our likelihoods are exact; (ii) Using the same architecture, we trained another DDPM model with the continuous ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Although, DDPM, recently, reported, achieve, higher, sample, quality, SMLD, Song, Ermon, better, architectures, sampling, algorithms, allowed, framework, latter, catch, up-it.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | 3.1 PERTURBING DATA WITH SDES Our goal is to construct a diffusion process txptquT t"0 indexed by a continuous time variable t ... | p. 3 (2 BACKGROUND), p. 7 (2 BACKGROUND) |
| Denoiser / vector field | (7) (i.e., DDPM cont.), which further improves the likelihood; (iii) With sub-VP SDEs, we always get higher likelihoods compared to VP SDEs; ... | p. 7 (2 BACKGROUND), p. 2 (1 INTRODUCTION) |
| Sampling / downstream interface | Combined with multiple architectural improvements, we achieve record-breaking performance for unconditional image generation on CIFAR-10 with an Inception score of 9.89 and ... | p. 1 (ABSTRACT), p. 6 (2 BACKGROUND) |

## Failure and Ablation Link

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This enables applications such as class-conditional generation, image inpainting, colorization and other inverse problems, all achievable using a single unconditional score-based model without re-training.
- **p. 3 / 2 BACKGROUND - extractive body cue:** A variational Markov chain in the reverse direction is parameterized with pθpxi´1/xiq " Npxi´1; 1 ?1´βi pxi`βisθpxi, iqq, βiIq, and trained with a re-weighted variant ...
- **p. 6 / 2 BACKGROUND - extractive body cue:** Moreover, it is typically better than doubling the number of predictor steps without adding a corrector (P2000), where we have to interpolate between noise scales ...
- **p. 7 / 2 BACKGROUND - extractive body cue:** (7) (i.e., DDPM cont.), which further improves the likelihood; (iii) With sub-VP SDEs, we always get higher likelihoods compared to VP SDEs; (iv) With improved ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** Surprisingly, we can achieve better FID than the previous best conditional generative model without requiring labeled data.
- **p. 8 / 2 BACKGROUND - extractive body cue:** With a larger error tolerance, the number of function evaluations can be reduced by over 90% without affecting the visual quality of samples (Fig.
- **p. 9 / 2 BACKGROUND - extractive body cue:** In Appendix I.4, we provide a broadly applicable method for obtaining such an estimate without the need of training auxiliary models.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 6 (2 BACKGROUND), objective p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 7 (2 BACKGROUND), p. 8 (2 BACKGROUND), p. 1 (1 INTRODUCTION), temporal p. 2 (1 INTRODUCTION), p. 5 (2 BACKGROUND), p. 6 (2 BACKGROUND), p. 9 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
