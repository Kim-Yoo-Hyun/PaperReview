# Problem - Classifier-Free Diffusion Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2207.12598; PDF retrieval source: https://arxiv.org/pdf/2207.12598. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): (6) has no classifier gradient present, so taking a step in the ˜ϵθ direction cannot be interpreted as a gradient-based adversarial attack on an image classifier.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit ...
- **p. 1 / ABSTRACT - extractive body cue:** Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate ...
- **p. 1 / ABSTRACT - extractive body cue:** It also raises the question of whether guidance can be performed without a classifier.
- **p. 1 / ABSTRACT - extractive body cue:** We show that guidance can be indeed performed by a pure generative model without such a classifier: in what we call classifier-free guidance, we jointly ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Diffusion models have recently emerged as an expressive and flexible family of generative models, delivering competitive sample quality and likelihood scores on image and audio ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** (6) has no classifier gradient present, so taking a step in the ˜ϵθ direction cannot be interpreted as a gradient-based adversarial attack on an image ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** Furthermore, ˜ϵθ is constructed from score estimates that are non-conservative vector fields due to the use of unconstrained neural networks, so there in general cannot ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (6) has no classifier gradient present, so taking a step in the ˜ϵθ direction cannot be interpreted as a gradient-based adversarial attack ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | Classifier guidance instead mixes a diffusion model's score estimate with the input gradient of the log probability of a Figure 1: Classifier-free ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | Classifier, guidance, instead, mixes, diffusion, model, score, estimate, input, gradient | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | only, modification, model, reverse, process, function, approximator, receives | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: Classifier, guidance, instead, mixes, diffusion, model, score, estimate, input, gradient | p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: resolve, questions, present, classifier-free, guidance, avoids, classifier, entirely | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 5 (2 BACKGROUND) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Algorithm, Joint, training, diffusion, model, classifier-free, guidance, Require | p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 1 (ABSTRACT) |
| Success / guarantee | sample quality, diversity and latency | p. 2 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / 2 BACKGROUND - extractive body cue:** Furthermore, ˜ϵθ is constructed from score estimates that are non-conservative vector fields due to the use of unconstrained neural networks, so there in general cannot ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Prior to classifier guidance, it was not known how to generate "low temperature" samples from a diffusion model similar to those produced by truncated BigGAN ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** This objective is denoising score matching (Vincent, 2011; Hyv¨arinen & Dayan, 2005) over multiple noise scales (Song & Ermon, 2019), and when p(λ) is uniform, ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 5 (2 BACKGROUND)): To resolve these questions, we present classifier-free guidance, our guidance method which avoids any classifier entirely.

- **p. 1 / ABSTRACT - extractive body cue:** We show that guidance can be indeed performed by a pure generative model without such a classifier: in what we call classifier-free guidance, we jointly ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** Nevertheless, in Section 4, we show empirically that classifier-free guidance is able to trade off FID and IS in the same way as classifier guidance.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Therefore, our classifier-free guided sampler follows step directions that do not resemble classifier gradients at all and thus ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | It would be an interesting avenue of future work to try to boost sample quality while maintaining sample ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The 64 × 64 models used sampler noise interpolation coefficient v = 0.3 and were trained for 400 ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND), interface p. 1 (1 INTRODUCTION), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), objective p. 3 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
