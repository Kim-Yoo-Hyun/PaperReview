# Problem - Score-Based Generative Modeling through Stochastic Differential Equations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.13456; PDF retrieval source: https://arxiv.org/pdf/2011.13456. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND), p. 8 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): The latter allows for fast adaptive sampling via black-box ODE solvers, flexible data manipulation via latent codes, a uniquely identifiable encoding, and notably, exact likelihood computation.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Creating noise from data is easy; creating data from noise is generative modeling.
- **p. 1 / ABSTRACT - extractive body cue:** We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a ...
- **p. 1 / ABSTRACT - extractive body cue:** Crucially, the reverse-time SDE depends only on the time-dependent gradient field (a.k.a., score) of the perturbed data distribution.
- **p. 1 / ABSTRACT - extractive body cue:** By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples.
- **p. 1 / ABSTRACT - extractive body cue:** We show that this framework encapsulates previous approaches in score-based generative modeling and diffusion probabilistic modeling, allowing for new sampling procedures and new modeling capabilities.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The latter allows for fast adaptive sampling via black-box ODE solvers, flexible data manipulation via latent codes, a uniquely identifiable encoding, and notably, exact likelihood ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** In contrast, FID scores and NLL values in Table 2 are reported for the last training checkpoint, and samples are obtained with black-box ODE solvers.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The latter allows for fast adaptive sampling via black-box ODE solvers, flexible data manipulation via latent codes, a uniquely identifiable encoding, and ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | Although, DDPM, recently, reported, achieve, higher, sample, quality, SMLD, Song | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | SDE, unique, strong, solution, long, coefficients, globally, Lipschitz | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: Although, DDPM, recently, reported, achieve, higher, sample, quality, SMLD, Song | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: addition, SDE, under, framework, achieves, likelihood, value, bits/dim | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Song, Ermon, train, Noise, Conditional, Score, Network, NCSN | p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (2 BACKGROUND), p. 8 (2 BACKGROUND), p. 1 (1 INTRODUCTION) |
| Success / guarantee | sample quality, diversity and latency | p. 6 (Figure/Table caption), p. 1 (ABSTRACT), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 8 / 2 BACKGROUND - extractive body cue:** In contrast, FID scores and NLL values in Table 2 are reported for the last training checkpoint, and samples are obtained with black-box ODE solvers.
- **p. 8 / 2 BACKGROUND - extractive body cue:** Using a black-box ODE solver (Dormand & Prince, 1980) not only produces high quality samples (Table 2, details in Appendix D.4), but also allows us ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The former unifies and improves over existing sampling methods for score-based models.
- **p. 3 / 2 BACKGROUND - extractive body cue:** In other words, p0 is the data distribution and pT is the prior distribution.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (ABSTRACT)): In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a new record on this task.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although DDPM (Ho et al., 2020) was recently reported to achieve higher sample quality than SMLD (Song & Ermon, 2019; 2020), we show that with ...
- **p. 8 / 2 BACKGROUND - extractive body cue:** 5 CONTROLLABLE GENERATION The continuous structure of our framework allows us to not only produce data samples from p0, but also from p0pxp0q / yq ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, we introduce a predictor-corrector framework to correct errors in the evolution of the discretized reverse-time SDE.
- **p. 1 / ABSTRACT - extractive body cue:** We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Future work would benefit from improved methods to automatically select and tune these hyperparameters, as well as more ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | This process progressively diffuses a data point into random noise, and is given by a prescribed SDE that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | For ease of presentation we assume the diffusion coefficient is a scalar (instead of a d ˆ d ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Creating noise from data is easy; creating data from noise is generative modeling. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 8 (2 BACKGROUND), p. 8 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), interface p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), objective p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
