# Denoising Diffusion Implicit Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2010.02502.
> PDF retrieval source: https://arxiv.org/pdf/2010.02502. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICLR
- Authors: Jiaming Song, Chenlin Meng, Stefano Ermon
- Primary track: Foundations: Generative Models
- Tier: REFERENCE
- Tags: Diffusion, sampling, Generation
- Official paper: https://arxiv.org/abs/2010.02502
- Full-text retrieval: https://arxiv.org/pdf/2010.02502
- Code/Project: https://github.com/ermongroup/ddim
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

DDIM은 DDPM과 같은 학습 목적을 쓰면서 더 적은 역방향 단계로 이미지를 생성하는 확산 모형이다. [PDF 1쪽](https://arxiv.org/pdf/2010.02502v4#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps in ...
- **p. 1 / ABSTRACT - extractive body cue:** To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as ...
- **p. 1 / ABSTRACT - extractive body cue:** In DDPMs, the generative process is defined as the reverse of a particular Markovian diffusion process.
- **p. 1 / ABSTRACT - extractive body cue:** We generalize DDPMs via a class of non-Markovian diffusion processes that lead to the same training objective.
- **p. 1 / ABSTRACT - extractive body cue:** These non-Markovian processes can correspond to generative processes that are deterministic, giving rise to implicit models that produce high quality samples much faster.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** This becomes more problematic for larger images as sampling 50k images of size 256 × 256 could take nearly 1000 hours on the same GPU.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To close this efficiency gap between DDPMs and GANs, we present denoising diffusion implicit models (DDIMs).
- **p. 1 / ABSTRACT - extractive body cue:** To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We show that the resulting variational training objectives have a shared surrogate objective, which is exactly the objective used to train DDPM.
- **p. 3 / 2 BACKGROUND - extractive body cue:** In Appendix A, we show that the non-Markovian perspective also applies beyond the Gaussian case.
- **p. 4 / 2 BACKGROUND - extractive body cue:** However, Jσ is equivalent to Lγ for certain weights γ, as we show below.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Unlike typical latent variable models (such as the variational autoencoder (Rezende et al., 2014)), DDPMs are learned with a fixed (rather than trainable) inference procedure ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** From a trained model, x0 is sampled by first sampling xT from the prior pθ(xT ), and then sampling xt-1 from the generative processes iteratively.
- **p. 4 / 2 BACKGROUND - extractive body cue:** Intuitively, given a noisy observation xt, we first make a prediction4 of the corresponding x0, and then use it to obtain a sample xt-1 through ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We empirically demonstrate that DDIMs can produce high quality samples 10× to 50× faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, perform ... | conditioning observation와 noisy/intermediate sample | p. 1 (ABSTRACT), p. 2 (2 BACKGROUND) |
| State/latent | empirically, demonstrate, DDIMs, produce, high, quality, samples, faster, terms, wall-clock, time, compared | latent/noise variable와 conditional distribution | p. 1 (ABSTRACT), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Output/action | Intuitively, the forward process progressively adds noise to the observation x0, whereas the generative process progressively denoises a noisy observation (Figure 1, left). | generated sample, action chunk 또는 trajectory | p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Objective/outcome | (2020), the objective with γ = 1 is optimized instead to maximize generation performance of the trained model; this is also the same objective used in noise conditional score networks (Song & ... | distribution fit, multimodality, sample quality와 latency | p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND) |

## Main Claims and Actual Contribution

- 비마르코프 순방향 과정에서 결정론적 역방향 갱신을 유도해 학습한 잡음 예측기를 재사용한다. [PDF 4쪽](https://arxiv.org/pdf/2010.02502v4#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2010.02502v4#page=5)
- 단계 수를 줄였을 때 CIFAR-10·CelebA의 FID와 실제 생성 시간이 어떻게 달라지는지 비교한다. [PDF 7쪽](https://arxiv.org/pdf/2010.02502v4#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2010.02502v4#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Embodiment/environment | For each dataset, we use the same trained model with T = 1000 and the objective being Lγ from Eq. | hardware/simulator version and reset protocol | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Dataset/benchmark | We consider encoding and decoding on the CIFAR-10 test set with the CIFAR-10 model with S steps for both encoding and decoding; we report the per-dimension mean squared error (scaled to [0, ... | role, split, size and leakage | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Metric | For the case of ˆσ, the generated images seem to have more noisy perturbations under short trajectories; this explains why the FID scores are much worse than other methods, as FID is ... | definition, denominator, direction and uncertainty | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | In this section, we show that DDIMs outperform DDPMs in terms of image generation when fewer iterations are considered, giving speed ups of 10× to 100× over the original DDPM generation process. | fair input/data/compute/action matching | p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** DDIMs can also be used to encode samples that reconstruct them from the latent code, which DDPMs cannot do due to the stochastic sampling process.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The same cannot be said for DDPMs due to their stochastic nature.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This allows DDIM to control the generated images on a high level directly through the latent variables, which DDPMs cannot.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** We also consider DDPM where the random noise has a larger standard deviation than σ(1), which we denote as ˆσ: ˆστi = p 1 -ατi/ατi-1 ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND)이다.
