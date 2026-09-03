# Problem - GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=VSG65wVNuL&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries)): The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D reconstruction from a single image is a long-standing problem in computer vision.
- **p. 1 / Abstract - extractive body cue:** Learning-based methods address its inherent scale ambiguity by leveraging increasingly large labeled and unlabeled datasets, to produce geometric priors capable of generating accurate predictions across ...
- **p. 1 / Abstract - extractive body cue:** As a result, state of the art approaches show impressive performance in zero-shot relative and metric depth estimation.
- **p. 1 / Abstract - extractive body cue:** Recently, diffusion models have exhibited remarkable scalability and generalizable properties in their learned representations.
- **p. 1 / Abstract - extractive body cue:** However, because these models repurpose tools originally designed for image generation, they can only operate on dense ground-truth, which is not available for most depth ...
- **p. 1 / 1. Introduction - extractive body cue:** The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1.
- **p. 1 / 1. Introduction - extractive body cue:** In order to fully leverage these geometric priors we turn to diffusion models [31], due to their scalability to large-scale diverse datasets and strong regression ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1. | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | (a) Latent tokens Zin read from input tokens Xin, are processed via a series of self-attention layers, and written back to output ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF body |
| State / latent | Latent, tokens, Zin, read, input, Xin, processed, series, self-attention, layers | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | Although, more, efficient, drawbacks, namely, loss, fine-grained, details | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: Latent, tokens, Zin, read, input, Xin, processed, series, self-attention, layers | p. 3 (3. Diffusion Preliminaries), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: summary, contributions, follows, introduce, GRIN, novel, diffusion-based, monocular | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: training, objective, loss, calculated, log-depth, scale, where, injected | p. 5 (4.4. Training Procedure) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.4. Training Procedure) |
| Success / guarantee | sample quality, diversity and latency | p. 7 (5.3. Zero-Shot Metric Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation), p. 8 (5.4. Zero-Shot Relative Depth Estimation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** In order to fully leverage these geometric priors we turn to diffusion models [31], due to their scalability to large-scale diverse datasets and strong regression ...
- **p. 2 / 1. Introduction - extractive body cue:** To mitigate these limitations, we instead propose to use a more flexible diffusion architecture that is efficient enough to operate at a pixel-level, and can ...
- **p. 2 / 1. Introduction - extractive body cue:** In particular, we build on RIN (Recurrent Interface Networks) [35], a novel diffusion architecture that decouples its core computation from input dimensionality, making it much ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** To circumvent these limitations, we instead adopt RIN [35], a recently introduced transformer-based architecture, shown in Figure 2.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries), p. 3 (3. Diffusion Preliminaries), p. 4 (4.1. Sparse Unstructured Training)): In summary, our contributions are as follows: • We introduce GRIN, a novel diffusion-based monocular depth estimation framework designed to (i) ingest sparse training data, enabling the use of larger ...

- **p. 2 / 1. Introduction - extractive body cue:** We propose several key modifications to this original framework to apply it to the task of depth estimation, including the use of 3D geometric positional ...
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** Capitalizing on these benefits, in the next section we introduce our approach for zero shot metric depth estimation with pixel-level diffusion.
- **p. 3 / 3. Diffusion Preliminaries - extractive body cue:** (b) A RIN model consists of B blocks, each receiving latent Zb and input Xb tokens from the previous block and returning updated Zb+1 and ...
- **p. 4 / 4.1. Sparse Unstructured Training - extractive body cue:** To address these limitations we propose a combination of local and global conditioning which promote training with unstructured sparse data while still maintaining dense scene-level ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Interestingly, these uncertainty maps also accurately detect failure cases of our model, such as the mirror on the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 1. Zero-shot metric monocular depth estimation results on various indoor and outdoor datasets. Numbers in italics indicate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | We then provide additional architecture details in Section C, and in Section D we discuss potential limitations of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 2. Recurrent Interface Networks (RIN) architecture. (a) Latent tokens Zin read from input tokens Xin, are processed ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Diffusion Preliminaries), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries), interface p. 3 (3. Diffusion Preliminaries), p. 2 (1. Introduction), p. 3 (3. Diffusion Preliminaries), p. 1 (1. Introduction), objective p. 5 (4.4. Training Procedure).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
