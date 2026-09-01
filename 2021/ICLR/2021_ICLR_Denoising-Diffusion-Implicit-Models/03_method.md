# Method - Denoising Diffusion Implicit Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.02502; PDF retrieval source: https://arxiv.org/pdf/2010.02502. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 6 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 1 (1 INTRODUCTION)): Unlike typical latent variable models (such as the variational autoencoder (Rezende et al., 2014)), DDPMs are learned with a fixed (rather than trainable) inference procedure q(x1:T /x0), and latent variables ...

## Method Body Digest

- **p. 2 / 2 BACKGROUND - extractive PDF cue:** Unlike typical latent variable models (such as the variational autoencoder (Rezende et al., 2014)), DDPMs are learned with a fixed (rather than trainable) inference procedure ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** From a trained model, x0 is sampled by first sampling xT from the prior pθ(xT ), and then sampling xt-1 from the generative processes iteratively.
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Intuitively, given a noisy observation xt, we first make a prediction4 of the corresponding x0, and then use it to obtain a sample xt-1 through ...
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** This suggests that unlike DDPM, we can use DDIM to obtain encodings of the observations (as the form of xT ), which might be useful ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Therefore, if parameters are not shared across t in the model ϵθ, then the L1 objective used by Ho et al.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, GANs require very specific choices in optimization and architectures in order to stabilize training (Arjovsky et al., 2017; Gulrajani et al., 2017; Karras et ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (2020), the objective with γ = 1 is optimized instead to maximize generation performance of the trained model; this is also the same objective used ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** The variational objective Lγ is special in the sense that if parameters θ of the models ϵ(t) θ are not shared across different t, then ...

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs).
- **p. 1 / ABSTRACT - extractive PDF cue:** To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We show that the resulting variational training objectives have a shared surrogate objective, which is exactly the objective used to train DDPM.

## Source Evidence Cues

- **p. 2 / 2 BACKGROUND - extractive PDF cue:** Unlike typical latent variable models (such as the variational autoencoder (Rezende et al., 2014)), DDPMs are learned with a fixed (rather than trainable) inference procedure ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** From a trained model, x0 is sampled by first sampling xT from the prior pθ(xT ), and then sampling xt-1 from the generative processes iteratively.
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Intuitively, given a noisy observation xt, we first make a prediction4 of the corresponding x0, and then use it to obtain a sample xt-1 through ...
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** This suggests that unlike DDPM, we can use DDIM to obtain encodings of the observations (as the form of xT ), which might be useful ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Therefore, if parameters are not shared across t in the model ϵθ, then the L1 objective used by Ho et al.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, GANs require very specific choices in optimization and architectures in order to stabilize training (Arjovsky et al., 2017; Gulrajani et al., 2017; Karras et ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (2020), the objective with γ = 1 is optimized instead to maximize generation performance of the trained model; this is also the same objective used ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Unlike typical latent variable models (such as the variational autoencoder (Rezende et al., 2014)), DDPMs are learned with a fixed (rather than ... | p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | From a trained model, x0 is sampled by first sampling xT from the prior pθ(xT ), and then sampling xt-1 from the ... | p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | Intuitively, given a noisy observation xt, we first make a prediction4 of the corresponding x0, and then use it to obtain a ... | p. 4 (2 BACKGROUND), p. 6 (2 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (2020), the objective with γ = 1 is optimized instead to maximize generation performance of the trained model; this is also the same objective used ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** The variational objective Lγ is special in the sense that if parameters θ of the models ϵ(t) θ are not shared across different t, then ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** We optimize θ via the following variational inference objective (which is a functional over ϵθ): Jσ(ϵθ) := Ex0:T ∼qσ(x0:T )[log qσ(x1:T /x0) -log pθ(x0:T )] ...
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** In a concurrent work, (Song et al., 2020) proposed a "probability flow ODE" that aims to recover the marginal densities of a stochastic differential equation ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We generalize DDPMs via a class of non-Markovian diffusion processes that lead to the same training objective.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** DDIMs are implicit probabilistic models (Mohamed & Lakshminarayanan, 2016) and are closely related to DDPMs, in the sense that they are trained with the same ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | empirically, demonstrate, DDIMs, produce, high, quality, samples, faster, terms, wall-clock, time, compared, DDPMs, allow | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | empirically, demonstrate, DDIMs, produce, high, quality, samples, faster, terms, wall-clock | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | close, efficiency, between, DDPMs, GANs, present, denoising, diffusion, implicit, models | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | objective, optimized, instead, maximize, generation, performance, trained, model, same, noise | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / ABSTRACT - extractive PDF cue:** We empirically demonstrate that DDIMs can produce high quality samples 10× to 50× faster in terms of wall-clock time compared to DDPMs, allow us to ...
- **p. 2 / 2 BACKGROUND - extractive PDF cue:** Intuitively, the forward process progressively adds noise to the observation x0, whereas the generative process progressively denoises a noisy observation (Figure 1, left).
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** Our key observation is that the DDPM objective in the form of Lγ only depends on the marginals2 q(xt/x0), but not directly on the joint ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** (4), one can then predict the denoised observation, which is a prediction of x0 given xt: f (t) θ (xt) := (xt - √ 1 ...
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** Intuitively, given a noisy observation xt, we first make a prediction4 of the corresponding x0, and then use it to obtain a sample xt-1 through ...
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** Here, we state that the our ODE is equivalent to a special case of theirs (which corresponds to a continuous-time analog of DDPM).
- **p. 6 / 2 BACKGROUND - extractive PDF cue:** This suggests that unlike DDPM, we can use DDIM to obtain encodings of the observations (as the form of xT ), which might be useful ...
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | 5.1 SAMPLE QUALITY AND EFFICIENCY In Table 1, we report the quality of the generated samples with models trained on CIFAR10 and ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | 10 20 50 100 1000 sample timesteps 10 100 sample timesteps 10 100 sample timesteps Figure 5: Samples from DDIM with the ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | 5.1 SAMPLE QUALITY AND EFFICIENCY In Table 1, we report the quality of the generated samples with models trained on CIFAR10 and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 2 BACKGROUND - extractive PDF cue:** Unlike typical latent variable models (such as the variational autoencoder (Rezende et al., 2014)), DDPMs are learned with a fixed (rather than trainable) inference procedure ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** From a trained model, x0 is sampled by first sampling xT from the prior pθ(xT ), and then sampling xt-1 from the generative processes iteratively.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, GANs require very specific choices in optimization and architectures in order to stabilize training (Arjovsky et al., 2017; Gulrajani et al., 2017; Karras et ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** (2020), the objective with γ = 1 is optimized instead to maximize generation performance of the trained model; this is also the same objective used ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Unlike, typical, latent, variable, models, variational, autoencoder, Rezende, DDPMs, learned, fixed, rather, trainable, inference, procedure, variables, relatively, high, dimensional, trained.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | For each dataset, we use the same trained model with T = 1000 and the objective being Lγ from Eq. | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Denoiser / vector field | In this section, we show that DDIMs outperform DDPMs in terms of image generation when fewer iterations are considered, giving speed ups ... | p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Sampling / downstream interface | Even though DDPM could also achieve reasonable sample quality with 100× steps, DDIM requires much fewer steps to achieve this; on CelebA, ... | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** DDIMs can also be used to encode samples that reconstruct them from the latent code, which DDPMs cannot do due to the stochastic sampling process.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** The same cannot be said for DDPMs due to their stochastic nature.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** This allows DDIM to control the generated images on a high level directly through the latent variables, which DDPMs cannot.
- **p. 6 / 5 EXPERIMENTS - extractive PDF cue:** We also consider DDPM where the random noise has a larger standard deviation than σ(1), which we denote as ˆσ: ˆστi = p 1 -ατi/ατi-1 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 6 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 1 (1 INTRODUCTION), objective p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 6 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), temporal p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
