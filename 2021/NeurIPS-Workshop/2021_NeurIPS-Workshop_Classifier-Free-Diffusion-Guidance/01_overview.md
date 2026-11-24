# Classifier-Free Diffusion Guidance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2207.12598.
> PDF retrieval source: https://arxiv.org/pdf/2207.12598. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / NeurIPS Workshop
- Authors: Jonathan Ho, Tim Salimans
- Primary track: Foundations: Generative Models
- Tier: REFERENCE
- Tags: Diffusion, guidance, Generation
- Official paper: https://arxiv.org/abs/2207.12598
- Venue verification: https://openreview.net/pdf/ea628d03c92a49b54bc2d757d209e024e7885980.pdf
- Full-text retrieval: https://arxiv.org/pdf/2207.12598
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

분류기 없는 확산 유도는 조건부와 무조건부의 두 점수 추정값을 결합해 생성 표본의 충실도와 다양성을 조절한다. [PDF 1쪽](https://arxiv.org/pdf/2207.12598v1#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit ...
- **p. 1 / ABSTRACT - extractive body cue:** Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate ...
- **p. 1 / ABSTRACT - extractive body cue:** It also raises the question of whether guidance can be performed without a classifier.
- **p. 1 / ABSTRACT - extractive body cue:** We show that guidance can be indeed performed by a pure generative model without such a classifier: in what we call classifier-free guidance, we jointly ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Diffusion models have recently emerged as an expressive and flexible family of generative models, delivering competitive sample quality and likelihood scores on image and audio ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** (6) has no classifier gradient present, so taking a step in the ˜ϵθ direction cannot be interpreted as a gradient-based adversarial attack on an image ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** Furthermore, ˜ϵθ is constructed from score estimates that are non-conservative vector fields due to the use of unconstrained neural networks, so there in general cannot ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To resolve these questions, we present classifier-free guidance, our guidance method which avoids any classifier entirely.
- **p. 1 / ABSTRACT - extractive body cue:** We show that guidance can be indeed performed by a pure generative model without such a classifier: in what we call classifier-free guidance, we jointly ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** Nevertheless, in Section 4, we show empirically that classifier-free guidance is able to trade off FID and IS in the same way as classifier guidance.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Because the loss for ϵθ(zλ) is denoising score matching for all λ, the score ϵθ(zλ) learned by our model estimates the gradient of the log-density ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** If the model xθ is correct, then as T →∞, we obtain samples from an SDE whose sample paths are distributed as p(z) (Song et ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** We use a single neural network to parameterize both models, where for the unconditional model we can simply input a null token ∅for the class ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** Algorithm 1 Joint training a diffusion model with classifier-free guidance Require: puncond: probability of unconditional training 1: repeat 2: (x, c) ∼p(x, c) ▷Sample data ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** (It would certainly be possible to train separate models instead of jointly training them together, but we choose joint training because it is extremely simple ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Classifier guidance instead mixes a diffusion model's score estimate with the input gradient of the log probability of a Figure 1: Classifier-free guidance on the malamute class for a 64x64 ImageNet diffusion ... | conditioning observation와 noisy/intermediate sample | p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND) |
| State/latent | Classifier, guidance, instead, mixes, diffusion, model, score, estimate, input, gradient, probability, Figure | latent/noise variable와 conditional distribution | p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Output/action | 3.2 CLASSIFIER-FREE GUIDANCE While classifier guidance successfully trades off IS and FID as expected from truncation or low temperature sampling, it is nonetheless reliant on gradients from an image classifier and we ... | generated sample, action chunk 또는 trajectory | p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Objective/outcome | Algorithm 1 Joint training a diffusion model with classifier-free guidance Require: puncond: probability of unconditional training 1: repeat 2: (x, c) ∼p(x, c) ▷Sample data with conditioning from the dataset 3: c ... | distribution fit, multimodality, sample quality와 latency | p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |

## Main Claims and Actual Contribution

- 학습 중 조건 정보를 일정 확률로 지워 같은 네트워크가 두 추정값을 모두 학습하게 한다. [PDF 4쪽](https://arxiv.org/pdf/2207.12598v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2207.12598v1#page=5)
- ImageNet의 두 해상도에서 유도 강도를 바꾸며 FID와 Inception Score의 변화를 측정한다. [PDF 7쪽](https://arxiv.org/pdf/2207.12598v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2207.12598v1#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Embodiment/environment | We obtain the best FID results with a small amount of guidance (w = 0.1 or w = 0.3, depending on the dataset) and the best IS result with strong guidance (w ... | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | We obtain the best FID results with a small amount of guidance (w = 0.1 or w = 0.3, depending on the dataset) and the best IS result with strong guidance (w ... | role, split, size and leakage | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Metric | Figure 2: The effect of guidance on a mixture of three Gaussians, each mixture component represent- ing data conditioned on a class. The leftmost plot is the non-guided marginal density. Left to ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | Nevertheless, our classifier-free guided models still produce competitive sample quality metrics and sometimes outperform prior work, as can be seen in the following sections. | fair input/data/compute/action matching | p. 6 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 DISCUSSION - extractive body cue:** Therefore, our classifier-free guided sampler follows step directions that do not resemble classifier gradients at all and thus cannot be interpreted as a gradient-based adversarial ...
- **p. 9 / 5 DISCUSSION - extractive body cue:** It would be an interesting avenue of future work to try to boost sample quality while maintaining sample diversity.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The 64 × 64 models used sampler noise interpolation coefficient v = 0.3 and were trained for 400 thousand steps; the 128 × 128 models ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND)이다.
