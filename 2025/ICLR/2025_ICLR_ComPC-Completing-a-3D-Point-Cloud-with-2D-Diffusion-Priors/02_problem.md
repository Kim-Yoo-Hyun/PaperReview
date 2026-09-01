# Problem - ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SoUwcVplq4; PDF retrieval source: https://openreview.net/pdf/07e0e163b5ab2a3918ebbccd045080a0decea42e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): However, they face challenges in handling data that differs from what they were trained on, such as unseen object categories or real-world scans.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** 3D point clouds directly collected from objects through sensors are often incomplete due to self-occlusion.
- **p. 1 / ABSTRACT - extractive PDF cue:** Conventional methods for completing these partial point clouds rely on manually organized training sets and are usually limited to object categories seen during training.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we propose a test-time framework for completing partial point clouds across unseen categories without any requirement for training.
- **p. 1 / ABSTRACT - extractive PDF cue:** Leveraging point rendering via Gaussian Splatting, we develop techniques of Partial Gaussian Initialization, Zero-shot Fractal Completion, and Point Cloud Extraction that utilize priors from pre-trained ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Experimental results on both synthetic and real-world scanned point clouds demonstrate that our approach outperforms existing methods in completing a variety of objects.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, they face challenges in handling data that differs from what they were trained on, such as unseen object categories or real-world scans.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, a notable limitation of the method proposed by SDS-complete (Kasten et al., 2024) is its dependency on manually created text prompts for each point ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, they face challenges in handling data that differs from what they were trained on, such as unseen object categories or real-world ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | main, contributions, summarized, below, Partial, Gaussian, Initialization, generate, reference, image | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | Published, conference, ICLR, SDS, Virtual, Camera, Froze, parameters | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: main, contributions, summarized, below, Partial, Gaussian, Initialization, generate, reference, image | p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: main, contributions, summarized, below, Partial, Gaussian, Initialization, generate | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: Given, centers, Gin, anchored, Pin, estimate, minimizing, Depth | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Success / guarantee | sample quality, diversity and latency | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, a notable limitation of the method proposed by SDS-complete (Kasten et al., 2024) is its dependency on manually created text prompts for each point ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This approach also allows us to incorporate 2D diffusion priors into the process of modifying 3D geometry.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To achieve robust and generalizable 3D generation, researchers propose to lift 2D priors for 3D generation (Poole et al., 2022; Wang et al., 2023; Mohammad ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** This insight presents an opportunity to apply 2D diffusion priors to tasks related to 3D point clouds, such as point cloud completion.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which is observed from an estimated reference ...

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** In view of the above-mentioned issues, we propose a novel test-time point cloud completion framework that eliminates the need for any extra manually provided information ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Inspired by the capability of novel view synthetic diffusion model, e.g., Zero 1-to-3 (Liu et al., 2023), we propose to use the reference image as ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In this study, we propose to leverage 3D Gaussian Splatting (GS) (Kerbl et al., 2023) to bridge point clouds with priors from 2D diffusion models.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Due to the efficient rendering from 3D GS, and stronger priors from Zero 1-to-3, our method can achieve much higher optimization efficiency than SDS-Complete (Kasten ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | LIMITATION Our method shares similar limitations as claimed by SDS-complete (Kasten et al., 2024). | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Figure 12: Some failure cases. AdaPoinTr SVDFormer Ours Input GT 0.0 0.001 | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Published as a conference paper at ICLR 2025 Output Ground Truth Partial Reference Image Figure 12: Some failure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | As a test-time completion method, although our method does not require any training, the optimization on the test ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), objective p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
