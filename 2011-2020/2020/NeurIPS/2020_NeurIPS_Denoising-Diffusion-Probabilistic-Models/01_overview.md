# Denoising Diffusion Probabilistic Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://arxiv.org/html/2006.11239)
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2006.11239.
> PDF retrieval source: https://arxiv.org/pdf/2006.11239. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / NeurIPS
- Authors: Jonathan Ho, Ajay Jain, Pieter Abbeel
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Diffusion, Generation
- Official paper: https://arxiv.org/abs/2006.11239
- Full-text retrieval: https://arxiv.org/pdf/2006.11239
- Code/Project: https://github.com/hojonathanho/diffusion
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## 공개 자료

- **데이터** 저자 프로젝트의 예제 이미지와 보충 원고를 확인했다. Dropbox에서 생성 표본 묶음을 열거할 수 없어 논문 평가에 사용한 샘플 파일은 미확인이다. [검토 근거](https://hojonathanho.github.io/diffusion/)

## Why This Paper Is Here

DDPM은 잡음에서 자연 이미지를 복원하는 역확산 모델이다. 이 논문의 평가는 생성한 이미지의 품질과 분포에 초점을 둔다. [원문](https://arxiv.org/html/2006.11239)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 1 / Abstract - extractive body cue:** On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17.
- **p. 1 / Abstract - extractive body cue:** On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN.
- **p. 1 / 1 Introduction - extractive body cue:** Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities.
- **p. 3 / 2 Background - extractive body cue:** (5) are comparisons between Gaussians, so they can be calculated in a Rao-Blackwellized fashion with closed form expressions instead of high variance Monte Carlo estimates.
- **p. 5 / 2 Background - extractive body cue:** These terms train the network to denoise data with very small amounts of noise, so it is beneficial to down-weight them so that the network ...

## Core Idea

DDPM은 이미지에 단계별로 가우시안 잡음을 더하고, 시점별 잡음을 신경망으로 예측하도록 학습한다. 생성 시에는 잡음에서 시작해 역과정을 반복하여 이미지를 얻는다. [원문](https://arxiv.org/html/2006.11239)

## Observation, State, and Output Interface

학습 입력은 잡음을 더한 이미지와 확산 시점이며 신경망은 부가된 잡음을 예측한다. 역확산 체인의 최종 출력은 이미지다. [원문](https://arxiv.org/html/2006.11239)

## Main Claims and Actual Contribution

저자들은 확산 모델의 학습을 여러 잡음 수준에서의 denoising과 연결하고, CIFAR-10 등에서 생성한 이미지의 품질을 평가했다. [원문](https://arxiv.org/html/2006.11239)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Embodiment/environment | Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test set, the score is 5.24, which is still ... | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | 0 200 400 600 800 1,000 0 20 40 60 80 Reverse process steps (T -t) Distortion (RMSE) 0 200 400 600 800 1,000 0 0.5 1 1.5 Reverse process steps (T ... | role, split, size and leakage | p. 5 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Metric | 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. | definition, denominator, direction and uncertainty | p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Baseline/ablation | Prior work has shown that such reorderings introduce inductive biases that have an impact on sample quality [38], so we speculate that the Gaussian diffusion serves a similar purpose, perhaps to greater ... | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 2 Background - extractive body cue:** Blank entries were unstable to train and generated poor samples with out-ofrange scores.
- **p. 6 / 4 Experiments - extractive body cue:** We also see that learning reverse process variances (by incorporating a parameterized diagonal Σθ(xt) into the variational bound) leads to unstable training and poorer sample ...
- **p. 8 / 4 Experiments - extractive body cue:** We can therefore interpret the Gaussian diffusion model (2) as a kind of autoregressive model with a generalized bit ordering that cannot be expressed by ...
- **p. 4 / 2 Background - extractive body cue:** (It would be straightforward to instead incorporate a more powerful decoder like a conditional autoregressive model, but we leave that to future work.) Similar to ...
- **p. 5 / 2 Background - extractive body cue:** (LT does not appear because the forward process variances βt are fixed.) Algorithm 1 displays the complete training procedure with this simplified objective.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: The directed graphical model considered in this work. This paper presents progress in diffusion probabilistic models [53]. A diffusion probabilistic model (which we ...
- **p. 4 / 2 Background - extractive body cue:** At the end of sampling, we display µθ(x1, 1) noiselessly.

## Why Read It

후속 로봇 확산 정책을 읽을 때 원 DDPM의 이미지 생성 목적과 로봇 관측에 조건화한 행동 생성 목적을 구분하는 기준이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** (5) are comparisons between Gaussians, so they can be calculated in a Rao-Blackwellized fashion with closed form expressions instead of high variance Monte Carlo estimates. (p. 3, 2 Background).
- **Actual contribution:** DDPM은 이미지에 단계별로 가우시안 잡음을 더하고, 시점별 잡음을 신경망으로 예측하도록 학습한다. 생성 시에는 잡음에서 시작해 역과정을 반복하여 이미지를 얻는다. [원문](https://arxiv.org/html/2006.11239)
- **Evaluation boundary:** 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10. (p. 5, 4 Experiments).
- **Explicit failure boundary:** We fixed the noise for different values of λ so xt and x′ t remain the same. (p. 8, 4 Experiments).
