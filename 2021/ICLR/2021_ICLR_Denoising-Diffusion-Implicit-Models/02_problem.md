# Problem - Denoising Diffusion Implicit Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.02502; PDF retrieval source: https://arxiv.org/pdf/2010.02502. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs).

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps in ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In DDPMs, the generative process is defined as the reverse of a particular Markovian diffusion process.
- **p. 1 / ABSTRACT - extractive PDF cue:** We generalize DDPMs via a class of non-Markovian diffusion processes that lead to the same training objective.
- **p. 1 / ABSTRACT - extractive PDF cue:** These non-Markovian processes can correspond to generative processes that are deterministic, giving rise to implicit models that produce high quality samples much faster.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs).
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This becomes more problematic for larger images as sampling 50k images of size 256 × 256 could take nearly 1000 hours on the same GPU.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs). | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | We empirically demonstrate that DDIMs can produce high quality samples 10× to 50× faster in terms of wall-clock time compared to DDPMs, ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | empirically, demonstrate, DDIMs, produce, high, quality, samples, faster, terms, wall-clock | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | observation, DDPM, objective, form, only, depends, marginals2, xt/x0 | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: empirically, demonstrate, DDIMs, produce, high, quality, samples, faster, terms, wall-clock | p. 1 (ABSTRACT), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: close, efficiency, between, DDPMs, GANs, present, denoising, diffusion | p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: objective, optimized, instead, maximize, generation, performance, trained, model | p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION) |
| Success / guarantee | sample quality, diversity and latency | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This becomes more problematic for larger images as sampling 50k images of size 256 × 256 could take nearly 1000 hours on the same GPU.
- **p. 2 / 2 BACKGROUND - extractive PDF cue:** We call the latent variable model pθ(x0:T ), which is a Markov chain that samples from xT to x0, the generative process, since it approximates ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In Section 3, we generalize the forward diffusion process used by DDPMs, which is Markovian, to non-Markovian ones, for which we are still able to ...
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** From a trained model, x0 is sampled by first sampling xT from the prior pθ(xT ), and then sampling xt-1 from the generative processes iteratively.

## What the Paper Changes

PDF contribution framing (p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND)): To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs).

- **p. 1 / ABSTRACT - extractive PDF cue:** To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We show that the resulting variational training objectives have a shared surrogate objective, which is exactly the objective used to train DDPM.
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** In Appendix A, we show that the non-Markovian perspective also applies beyond the Gaussian case.
- **p. 4 / 2 BACKGROUND - extractive PDF cue:** However, Jσ is equivalent to Lγ for certain weights γ, as we show below.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | DDIMs can also be used to encode samples that reconstruct them from the latent code, which DDPMs cannot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The same cannot be said for DDPMs due to their stochastic nature. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | This allows DDIM to control the generated images on a high level directly through the latent variables, which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We also consider DDPM where the random noise has a larger standard deviation than σ(1), which we denote ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (ABSTRACT), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), interface p. 1 (ABSTRACT), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), objective p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
