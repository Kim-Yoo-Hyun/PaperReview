# Denoising Diffusion Probabilistic Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2006.11239.
> PDF retrieval source: https://arxiv.org/pdf/2006.11239. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Diffusion, Generation
- Official paper: https://arxiv.org/abs/2006.11239
- Full-text retrieval: https://arxiv.org/pdf/2006.11239
- Code/Project: https://github.com/hojonathanho/diffusion
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 generative 문제를 이해하기 위해 읽는다. 본문은 (5) are comparisons between Gaussians, so they can be calculated in a Rao-Blackwellized fashion with closed form expressions instead of high variance Monte Carlo estimates.를 문제로 두고, We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models is a type of progressive decoding that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 1 / Abstract - extractive body cue:** On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17.
- **p. 1 / Abstract - extractive body cue:** On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN.
- **p. 1 / 1 Introduction - extractive body cue:** Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities.
- **p. 3 / 2 Background - extractive body cue:** (5) are comparisons between Gaussians, so they can be calculated in a Rao-Blackwellized fashion with closed form expressions instead of high variance Monte Carlo estimates.
- **p. 5 / 2 Background - extractive body cue:** These terms train the network to denoise data with very small amounts of noise, so it is beneficial to down-weight them so that the network ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models ...
- **p. 2 / 1 Introduction - extractive body cue:** When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for ...
- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 3 / 2 Background - extractive body cue:** Second, to represent the mean µθ(xt, t), we propose a specific parameterization motivated by the following analysis of Lt.
- **p. 4 / 2 Background - extractive body cue:** 3.3 Data scaling, reverse process decoder, and L0 We assume that image data consists of integers in {0, 1, . . . , 255} scaled ...
- **p. 1 / Abstract - extractive body cue:** Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score ...
- **p. 5 / 2 Background - extractive body cue:** Model IS FID NLL Test (Train) Conditional EBM [11] 8.30 37.9 JEM [17] 8.76 38.4 BigGAN [3] 9.22 14.73 StyleGAN2 + ADA (v1) [29] 10.06 ...
- **p. 2 / 1 Introduction - extractive body cue:** In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. | conditioning observation와 noisy/intermediate sample | p. 1 (Abstract), p. 4 (2 Background) |
| State/latent | unconditional, CIFAR10, dataset, obtain, Inception, score, state-of-the-art, FID, ensures, neural, network, reverse | latent/noise variable와 conditional distribution | p. 1 (Abstract), p. 4 (2 Background), p. 4 (2 Background) |
| Output/action | This ensures that the neural network reverse process operates on consistently scaled inputs starting from the standard normal prior p(xT ). | generated sample, action chunk 또는 trajectory | p. 4 (2 Background), p. 4 (2 Background), p. 1 (Abstract) |
| Objective/outcome | In particular, our diffusion process setup in Section 4 causes the simplified objective to down-weight loss terms corresponding to small t. | distribution fit, multimodality, sample quality와 latency | p. 5 (2 Background), p. 1 (Abstract), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models ...
- **p. 2 / 1 Introduction - extractive body cue:** When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for ...
- **p. 1 / Abstract - extractive body cue:** We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- **p. 3 / 2 Background - extractive body cue:** Second, to represent the mean µθ(xt, t), we propose a specific parameterization motivated by the following analysis of Lt.
- **p. 4 / 2 Background - extractive body cue:** 3.3 Data scaling, reverse process decoder, and L0 We assume that image data consists of integers in {0, 1, . . . , 255} scaled ...
- **p. 5 / 4 Experiments - extractive body cue:** With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models.
- **p. 5 / 4 Experiments - extractive body cue:** 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10.
- **p. 6 / 4 Experiments - extractive body cue:** Still, while our lossless codelengths are better than the large estimates reported for energy based models and score matching using annealed importance sampling [11], they ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

RL, IL, offline learning, and robot data의 generative 문제를 이해하기 위해 읽는다. 본문은 (5) are comparisons between Gaussians, so they can be calculated in a Rao-Blackwellized fashion with closed form expressions instead of high variance Monte Carlo estimates.를 문제로 두고, We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models is a type of progressive decoding that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (2 Background), p. 5 (2 Background), p. 2 (1 Introduction), p. 4 (2 Background), p. 1 (Abstract), p. 5 (2 Background) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
