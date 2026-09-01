# Problem - LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72OSO38a2z; PDF retrieval source: https://openreview.net/pdf/fadb73da860f028d2b7db1267acefa4519a291e3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): However, as there is no encoder, new objects cannot be mapped to latent space easily.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** This paper introduces a novel hierarchical autoencoder that maps 3D models into a highly compressed latent space.
- **p. 1 / ABSTRACT - extractive PDF cue:** The hierarchical autoencoder is specifically designed to tackle the challenges arising from large-scale datasets and generative modeling using diffusion.
- **p. 1 / ABSTRACT - extractive PDF cue:** Different from previous approaches that only work on a regular image or volume grid, our hierarchical autoencoder operates on unordered sets of vectors.
- **p. 1 / ABSTRACT - extractive PDF cue:** Each level of the autoencoder controls different geometric levels of detail.
- **p. 1 / ABSTRACT - extractive PDF cue:** We show that the model can be used to represent a wide range of 3D models while faithfully representing high-resolution geometry details.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, as there is no encoder, new objects cannot be mapped to latent space easily.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Because of the high reconstruction quality and compactness of the latent space, the method alleviates the difficulty of training 3D generative models.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, as there is no encoder, new objects cannot be mapped to latent space easily. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | The process first downsamples the 3D input point cloud PInput = {pi}i=1,...,N with furthest point sampling (FPS), P = FPS(PInput, r), where ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | process, first, downsamples, input, point, cloud, PInput, furthest, sampling, FPS | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | i-th, level, first, obtain, lower, resolution, point, clouds | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: process, first, downsamples, input, point, cloud, PInput, furthest, sampling, FPS | p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: summarize, contributions, follows, hierarchical, autoencoder, architecture, faster, training | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: need, explicit, loss, regularize, latent, space, Features, Latents | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Success / guarantee | sample quality, diversity and latency | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Because of the high reconstruction quality and compactness of the latent space, the method alleviates the difficulty of training 3D generative models.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** All the previous works VAE, NVAE, and VecSet apply KL divergence in the bottleneck to regularize the latent space, while in this work, we apply ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** This makes the training even more difficult because of the O(n3) complexity.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Both structures have the potential to represent highquality 3D models, but generating irregular structures explicitly is difficult for diffusion models.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHODOLOGY)): We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The latent space is composed of several levels. • The model is capable of training on large-scale datasets like objaverse. • We propose a cascaded ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** We proposed a U-Net-style transformer for the autoencoding.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** To train the generative diffusion models in the latent space, we propose the cascaded latent diffusion models.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Motivated by this, we propose a cascaded latent diffusion model.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Due to failures of modeling loading and conversion, we obtained around 600k watertight models for training. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Our method does not solve the high training cost problem of diffusion itself. | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
