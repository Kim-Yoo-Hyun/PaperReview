# Flow Matching for Generative Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2023/poster/11309.
> PDF retrieval source: https://openreview.net/pdf?id=PqvMRDCJT9t. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Flow Matching, generative modeling, continuous normalizing flow, action generation
- Official paper: https://iclr.cc/virtual/2023/poster/11309
- Full-text retrieval: https://openreview.net/pdf?id=PqvMRDCJT9t
- Code/Project: https://openreview.net/forum?id=PqvMRDCJT9t
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 generative 문제를 이해하기 위해 읽는다. 본문은 (2018)) require expensive numerical ODE simulations, while existing simulation-free methods either involve intractable integrals (Rozen et al., 2021) or biased gradients (Ben-Hamu et al., 2022).를 문제로 두고, Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that generates a desired probability path.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, we present the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths.
- **p. 1 / ABSTRACT - extractive body cue:** Flow Matching is compatible with a general family of Gaussian probability paths for transforming between noise and data samples-which subsumes existing diffusion paths as specific ...
- **p. 1 / ABSTRACT - extractive body cue:** Interestingly, we find that employing FM with diffusion paths results in a more robust and stable alternative for training diffusion models.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, Flow Matching opens the door to training CNFs with other, non-diffusion probability paths.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2018)) require expensive numerical ODE simulations, while existing simulation-free methods either involve intractable integrals (Rozen et al., 2021) or biased gradients (Ben-Hamu et al., 2022).
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Flow Matching is a simple and attractive objective, but na¨ıvely on its own, it is intractable to use in practice since we have no prior ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a simpler objective, which surprisingly will result in the same optima as the original objective.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, we present the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our first key observation is this: The marginal vector field (equation 8) generates the marginal probability path (equation 6).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2022), is mostly facilitated by the scalable and relatively stable training of diffusion-based models Ho et al.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Upon reaching zero loss, the learned CNF model will generate pt(x).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our first key observation is this: The marginal vector field (equation 8) generates the marginal probability path (equation 6). | conditioning observation와 noisy/intermediate sample | p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| State/latent | first, observation, marginal, vector, field, equation, generates, probability, path, second, therefore, CFM | latent/noise variable와 conditional distribution | p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Output/action | Our second key observation is therefore: The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. θ. | generated sample, action chunk 또는 trajectory | p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Objective/outcome | Our second key observation is therefore: The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. θ. | distribution fit, multimodality, sample quality와 latency | p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Instead, we propose a simpler objective, which surprisingly will result in the same optima as the original objective.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, we present the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require ...
- **p. 7 / 6 EXPERIMENTS - extractive body cue:** We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** FM-OT achieves similar PSNR and SSIM values to (Saharia et al., 2022) while considerably improving on FID and IS, which as argued by (Saharia et ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Secondly, Figure 7 (right) shows how FID changes as a result of the computational cost, where we find FM with OT is able to achieve ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Embodiment/environment | We explore the empirical benefits of using Flow Matching on the image datasets of CIFAR10 (Krizhevsky et al., 2009) and ImageNet at resolutions 32, 64, and 128 (Chrabaszcz et al., 2017; Deng ... | hardware/simulator version and reset protocol | p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS) |
| Dataset/benchmark | We follow the evaluation procedure in (Saharia et al., 2022) and compute the FID of the upsampled validation images; baselines include reference (FID of original validation set), and regression. | role, split, size and leakage | p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Metric | Preprint 20 40 60 80 100 NFE 10 2 10 1 Error SM-Dif FM-Dif FM-OT 0 20 40 60 80 100 NFE 10 20 30 40 50 FID Euler Midpoint RK4 0 ... | definition, denominator, direction and uncertainty | p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 19 (Figure/Table caption) |
| Baseline/ablation | When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the most efficient sampler, regardless of ODE solver, as demonstrated next. | fair input/data/compute/action matching | p. 9 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6 EXPERIMENTS - extractive body cue:** The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Score Matching w/ Diffusion Flow Matching w/ Diffusion Flow Matching w/ OT Figure 6: Sample paths from the same initial noise with models trained on ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** In Figure 7 (left), we compare the per-pixel MSE of low NFE solutions compared with 1000 NFE solutions (we use 256 random noise seeds), and ...
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 16: Generated samples from the same initial noise, but with varying number of function evaluations (NFE). Flow matching with OT path trained on ImageNet-128. ...

## Why Read It

RL, IL, offline learning, and robot data의 generative 문제를 이해하기 위해 읽는다. 본문은 (2018)) require expensive numerical ODE simulations, while existing simulation-free methods either involve intractable integrals (Rozen et al., 2021) or biased gradients (Ben-Hamu et al., 2022).를 문제로 두고, Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that generates a desired probability path.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** (2018)) require expensive numerical ODE simulations, while existing simulation-free methods either involve intractable integrals (Rozen et al., 2021) or biased gradients (Ben-Hamu et al., 2022). (p. 1, 1 INTRODUCTION).
- **Actual contribution:** Preprint In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that generates a desired probability path. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Figure 7: Flow Matching, especially when using OT paths, allows us to use fewer evaluations for sampling while retaining similar numerical error (left) and sample quality (right). Results are shown ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** Another important observation is that, as these probability paths were previously derived as solutions of diffusion processes, they do not actually reach a true noise distribution in finite time. (p. 5, 1 INTRODUCTION).
