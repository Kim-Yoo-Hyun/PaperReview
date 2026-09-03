# Problem - Vision Transformers for Dense Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.13413; PDF retrieval source: https://arxiv.org/pdf/2103.13413. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): While these techniques can significantly improve prediction quality, the networks are still bottlenecked by their fundamental building block: the convolution.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce dense vision transformers, an architecture that leverages vision transformers in place of convolutional networks as a backbone for dense prediction tasks.
- **p. 1 / Abstract - extractive body cue:** We assemble tokens from various stages of the vision transformer into image-like representations at various resolutions and progressively combine them into full-resolution predictions using a ...
- **p. 1 / Abstract - extractive body cue:** The transformer backbone processes representations at a constant and relatively high resolution and has a global receptive field at every stage.
- **p. 1 / Abstract - extractive body cue:** These properties allow the dense vision transformer to provide finer-grained and more globally coherent predictions when compared to fully-convolutional networks.
- **p. 1 / Abstract - extractive body cue:** Our experiments show that this architecture yields substantial improvements on dense prediction tasks, especially when a large amount of training data is available.
- **p. 1 / 1. Introduction - extractive body cue:** While these techniques can significantly improve prediction quality, the networks are still bottlenecked by their fundamental building block: the convolution.
- **p. 1 / 1. Introduction - extractive body cue:** Virtually all existing architectures for dense prediction are based on convolutional networks [6, 31, 34, 42, 49, 50, 53].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While these techniques can significantly improve prediction quality, the networks are still bottlenecked by their fundamental building block: the convolution. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | simple, three-stage, Reassemble, operation, recover, image-like, representations, output, tokens, arbitrary | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Convolutional, backbones, progressively, downsample, input, image, extract, features | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: simple, three-stage, Reassemble, operation, recover, image-like, representations, output, tokens, arbitrary | p. 3 (3. Architecture), p. 3 (3. Architecture), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: introduce, dense, prediction, transformer, DPT, Downsampling, enables, progressive | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Architecture) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: stark, contrast, convolutional, networks, progressively, increase, receptive, field | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Architecture), p. 3 (3. Architecture), p. 4 (3. Architecture) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 4 (4. Experiments), p. 5 (4.1. Monocular Depth Estimation), p. 6 (4.2. Semantic Segmentation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Virtually all existing architectures for dense prediction are based on convolutional networks [6, 31, 34, 42, 49, 50, 53].
- **p. 2 / 1. Introduction - extractive body cue:** Downsampling the intermediate representations is necessary to keep memory consumption at levels that are feasible with existing computer architectures.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Architecture), p. 2 (1. Introduction)): In this work, we introduce the dense prediction transformer (DPT).

- **p. 1 / 1. Introduction - extractive body cue:** Downsampling enables a progressive increase of the receptive field, the grouping of low-level features into abstract highlevel features, and simultaneously ensures that memory and computational ...
- **p. 3 / 3. Architecture - extractive body cue:** We propose a simple three-stage Reassemble operation to recover image-like representations from the output tokens of arbitrary layers of the transformer encoder: Reassemble ˆ D ...
- **p. 2 / 1. Introduction - extractive body cue:** We show that these properties are especially advantageous for dense prediction tasks as they naturally lead to fine-grained and globally coherent predictions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | We thus first align predictions of the initial network to each training sample using the robust alignment procedure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We observe that the performance of DPT variants indeed degrades more gracefully as inference resolution increases. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Architecture), p. 3 (3. Architecture), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3. Architecture), p. 3 (3. Architecture), p. 1 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
