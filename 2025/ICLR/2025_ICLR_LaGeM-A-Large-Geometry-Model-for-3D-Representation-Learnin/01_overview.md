# LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=72OSO38a2z.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114810. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Diffusion, Generation, 3D Vision
- Official paper: https://openreview.net/forum?id=72OSO38a2z
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114810
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, as there is no encoder, new objects cannot be mapped to latent space easily.를 문제로 두고, We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** This paper introduces a novel hierarchical autoencoder that maps 3D models into a highly compressed latent space.
- **p. 1 / ABSTRACT - extractive body cue:** The hierarchical autoencoder is specifically designed to tackle the challenges arising from large-scale datasets and generative modeling using diffusion.
- **p. 1 / ABSTRACT - extractive body cue:** Different from previous approaches that only work on a regular image or volume grid, our hierarchical autoencoder operates on unordered sets of vectors.
- **p. 1 / ABSTRACT - extractive body cue:** Each level of the autoencoder controls different geometric levels of detail.
- **p. 1 / ABSTRACT - extractive body cue:** We show that the model can be used to represent a wide range of 3D models while faithfully representing high-resolution geometry details.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, as there is no encoder, new objects cannot be mapped to latent space easily.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Because of the high reconstruction quality and compactness of the latent space, the method alleviates the difficulty of training 3D generative models.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The latent space is composed of several levels. • The model is capable of training on large-scale datasets like objaverse. • We propose a cascaded ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We proposed a U-Net-style transformer for the autoencoding.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To train the generative diffusion models in the latent space, we propose the cascaded latent diffusion models.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Motivated by this, we propose a cascaded latent diffusion model.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** We use cross attention to compress the feature set CA(Pi, Pi-1) = Xi.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Each latent vector in Z is first converted back to feature space RC (Latent to Feature, or LtoF in short), LtoF(Z) = X ′ = ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Then PInput is converted to an unordered set with cross-attention CA(Q = PE(P), K = PE(PInput), V = PE(PInput)) = X = {x ∈RC}i=1,2,...,M, (1) ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The process first downsamples the 3D input point cloud PInput = {pi}i=1,...,N with furthest point sampling (FPS), P = FPS(PInput, r), where r is the down-sampling ratio, and P is a low-resolution ... | conditioning observation와 noisy/intermediate sample | p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| State/latent | process, first, downsamples, input, point, cloud, PInput, furthest, sampling, FPS, where, down-sampling | latent/noise variable와 conditional distribution | p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Output/action | For notational convenience, we denote the input point cloud as level 0. | generated sample, action chunk 또는 trajectory | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Objective/outcome | We do not need an explicit loss to regularize the latent space. | distribution fit, multimodality, sample quality와 latency | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The latent space is composed of several levels. • The model is capable of training on large-scale datasets like objaverse. • We propose a cascaded ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We proposed a U-Net-style transformer for the autoencoding.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To train the generative diffusion models in the latent space, we propose the cascaded latent diffusion models.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Motivated by this, we propose a cascaded latent diffusion model.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** While for LaGeM-Objaverse, there is a large improvement in both training cost and quantitative results.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The quantitative results show an improvement of almost 50 percent averaged across the complete dataset in terms of the metric Chamfer.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We show autoencoding results on ShapeNet.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | The objects from these datasets vary from daily objects, CAD models, human models, and synthetic objects. | hardware/simulator version and reset protocol | p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | Our trained model is capable of doing inference on several existing datasets. | role, split, size and leakage | p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | We use Chamfer distance and Fscore as the metrics. | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Baseline/ablation | Both models are compared against VecSet (Zhang et al., 2023). | fair input/data/compute/action matching | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Due to failures of modeling loading and conversion, we obtained around 600k watertight models for training.
- **p. 10 / 5 CONCLUSION - extractive body cue:** Our method does not solve the high training cost problem of diffusion itself.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Latent with red color Z means it is replaced by Gaussian noise. Latent with blue color Z means it is generated with the ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, as there is no encoder, new objects cannot be mapped to latent space easily.를 문제로 두고, We summarize our contributions as follows: • We propose a hierarchical autoencoder architecture with faster training time and low memory consumption.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
