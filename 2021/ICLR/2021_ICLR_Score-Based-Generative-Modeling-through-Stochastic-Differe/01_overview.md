# Score-Based Generative Modeling through Stochastic Differential Equations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2011.13456.
> PDF retrieval source: https://arxiv.org/pdf/2011.13456. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICLR
- Authors: Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, Ben Poole
- Primary track: Foundations: Generative Models
- Tier: REFERENCE
- Tags: Diffusion, score model, Generation
- Official paper: https://arxiv.org/abs/2011.13456
- Full-text retrieval: https://arxiv.org/pdf/2011.13456
- Code/Project: https://github.com/yang-song/score_sde
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

점수 기반 생성 모델과 확산 모델을 순방향 확률미분방정식과 시간별 스코어에 의존하는 역방향 과정으로 통합했다. [PDF 1쪽](https://arxiv.org/pdf/2011.13456v2#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Creating noise from data is easy; creating data from noise is generative modeling.
- **p. 1 / ABSTRACT - extractive body cue:** We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a ...
- **p. 1 / ABSTRACT - extractive body cue:** Crucially, the reverse-time SDE depends only on the time-dependent gradient field (a.k.a., score) of the perturbed data distribution.
- **p. 1 / ABSTRACT - extractive body cue:** By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples.
- **p. 1 / ABSTRACT - extractive body cue:** We show that this framework encapsulates previous approaches in score-based generative modeling and diffusion probabilistic modeling, allowing for new sampling procedures and new modeling capabilities.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The latter allows for fast adaptive sampling via black-box ODE solvers, flexible data manipulation via latent codes, a uniquely identifiable encoding, and notably, exact likelihood ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** In contrast, FID scores and NLL values in Table 2 are reported for the last training checkpoint, and samples are obtained with black-box ODE solvers.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** 5 CONTROLLABLE GENERATION The continuous structure of our framework allows us to not only produce data samples from p0, but also from p0pxp0q / yq ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, we introduce a predictor-corrector framework to correct errors in the evolution of the discretized reverse-time SDE.
- **p. 1 / ABSTRACT - extractive body cue:** We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Two successful classes of probabilistic generative models involve sequentially corrupting training data with slowly increasing noise, and then learning to reverse this corruption in order ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We can therefore approximate the reverse-time SDE by training a time-dependent neural network to estimate the scores, and then produce samples using numerical SDE solvers.
- **p. 5 / 2 BACKGROUND - extractive body cue:** 4 SOLVING THE REVERSE SDE After training a time-dependent score-based model sθ, we can use it to construct the reverse-time SDE and then simulate it ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with better architectures and new sampling algorithms allowed ... | conditioning observation와 noisy/intermediate sample | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | Although, DDPM, recently, reported, achieve, higher, sample, quality, SMLD, Song, Ermon, better | latent/noise variable와 conditional distribution | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND) |
| Output/action | For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale. | generated sample, action chunk 또는 trajectory | p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Objective/outcome | Song & Ermon (2019) propose to train a Noise Conditional Score Network (NCSN), denoted by sθpx, σq, with a weighted sum of denoising score matching (Vincent, 2011) objectives: θ˚ " arg min ... | distribution fit, multimodality, sample quality와 latency | p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- 교란된 데이터 분포의 스코어를 학습하고 역방향 수치 적분과 예측·보정 샘플링으로 새로운 표본을 생성한다. [PDF 3쪽](https://arxiv.org/pdf/2011.13456v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2011.13456v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2011.13456v2#page=5)
- 같은 주변 분포를 따르는 확률 흐름 ODE를 도출하고 영상 생성의 품질·우도와 역문제 적용을 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2011.13456v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2011.13456v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2011.13456v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2011.13456v2#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 1 (ABSTRACT), p. 6 (2 BACKGROUND) |
| Embodiment/environment | 3.1 PERTURBING DATA WITH SDES Our goal is to construct a diffusion process txptquT t"0 indexed by a continuous time variable t P r0, Ts, such that xp0q „ p0, for which ... | hardware/simulator version and reset protocol | p. 3 (2 BACKGROUND), p. 7 (2 BACKGROUND) |
| Dataset/benchmark | Since the forward SDE is tractable, we can easily create training data pxptq, yq for the time-dependent classifier by first sampling pxp0q, yq from a dataset, and then sampling xptq „ p0tpxptq ... | role, split, size and leakage | p. 3 (2 BACKGROUND), p. 7 (2 BACKGROUND), p. 9 (2 BACKGROUND), p. 1 (1 INTRODUCTION) |
| Metric | Table 1: Comparing different reverse-time SDE solvers on CIFAR-10. Shaded regions are obtained with the same computation (number of score function evaluations). Mean and standard deviation are reported over five sampling runs. ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 1 (ABSTRACT), p. 8 (Figure/Table caption) |
| Baseline/ablation | (7) (i.e., DDPM cont.), which further improves the likelihood; (iii) With sub-VP SDEs, we always get higher likelihoods compared to VP SDEs; (iv) With improved architecture (i.e., DDPM++ cont., details in Section ... | fair input/data/compute/action matching | p. 7 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 6 (2 BACKGROUND) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 CONCLUSION - extractive body cue:** Future work would benefit from improved methods to automatically select and tune these hyperparameters, as well as more extensive investigation on the merits and limitations ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This process progressively diffuses a data point into random noise, and is given by a prescribed SDE that does not depend on the data and ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** For ease of presentation we assume the diffusion coefficient is a scalar (instead of a d ˆ d matrix) and does not depend on x, ...
- **p. 1 / ABSTRACT - extractive body cue:** Creating noise from data is easy; creating data from noise is generative modeling.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale.
- **p. 2 / 2 BACKGROUND - extractive body cue:** Consider a sequence of positive noise scales σmin " σ1 ă σ2 ă ¨ ¨ ¨ ă σN " σmax.
- **p. 3 / 2 BACKGROUND - extractive body cue:** The noise scales are prescribed such that xN is approximately distributed according to Np0, Iq.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND), p. 3 (2 BACKGROUND)이다.
