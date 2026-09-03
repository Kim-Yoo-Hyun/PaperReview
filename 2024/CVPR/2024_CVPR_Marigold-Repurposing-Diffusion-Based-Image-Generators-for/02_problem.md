# Problem - Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.02145; PDF retrieval source: https://arxiv.org/pdf/2312.02145. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Empowered by the underlying diffusion prior of natural images, Marigold exhibits excellent zero-shot generalization: Without ever having seen real depth maps, it attains state-ofthe-art performance on several real datasets.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Monocular depth estimation is a fundamental computer vision task.
- **p. 1 / Abstract - extractive body cue:** Recovering 3D depth from a single image is geometrically ill-posed and requires scene understanding, so it is not surprising that the rise of deep learning ...
- **p. 1 / Abstract - extractive body cue:** The impressive progress of monocular depth estimators has mirrored the growth in model capacity, from relatively modest CNNs to large Transformer architectures.
- **p. 1 / Abstract - extractive body cue:** Still, monocular depth estimators tend to struggle when presented with images with unfamiliar content and layout, since their knowledge of the visual world is restricted ...
- **p. 1 / Abstract - extractive body cue:** This motivates us to explore whether the extensive priors captured in recent generative diffusion models can enable better, more generalizable depth estimation.
- **p. 2 / 1. Introduction - extractive body cue:** Empowered by the underlying diffusion prior of natural images, Marigold exhibits excellent zero-shot generalization: Without ever having seen real depth maps, it attains state-ofthe-art performance ...
- **p. 1 / 1. Introduction - extractive body cue:** Clearly, undoing the projection from the 3D world to a 2D image is a geometrically ill-posed problem and can 1.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Empowered by the underlying diffusion prior of natural images, Marigold exhibits excellent zero-shot generalization: Without ever having seen real depth maps, it ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given that the encoder, which is designed for 3-channel (RGB) inputs, receives a single-channel depth map, we replicate the depth map into ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, encoder, designed, channel, RGB, inputs, receives, single-channel, depth, replicate | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | multi-resolution, noise, composed, superimposing, several, random, Gaussian, images | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, encoder, designed, channel, RGB, inputs, receives, single-channel, depth, replicate | p. 4 (3.2. Network Architecture), p. 4 (3.2. Network Architecture), p. 5 (3.3. Fine-Tuning Protocol) |
| Decision / output variable | geometry/map/query r; body terms: Capitalizing, following, test-time, ensembling, scheme, capable, combining, multiple | p. 5 (3.4. Inference), p. 2 (1. Introduction), p. 5 (3.4. Inference) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: training, time, parameters, updated, taking, data, pair, noising | p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference), p. 5 (3.3. Fine-Tuning Protocol), p. 3 (3.1. Generative Formulation), p. 4 (3.3. Fine-Tuning Protocol), p. 4 (3.1. Generative Formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Fine-Tuning Protocol), p. 3 (3.1. Generative Formulation), p. 4 (3.3. Fine-Tuning Protocol) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Implementation), p. 6 (4.2. Evaluation), p. 8 (4.3. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Clearly, undoing the projection from the 3D world to a 2D image is a geometrically ill-posed problem and can 1.
- **p. 2 / 1. Introduction - extractive body cue:** only be solved with the help of prior knowledge, such as typical object shapes and sizes, likely scene layouts, occlusion patterns, etc.

## What the Paper Changes

PDF body contribution framing (p. 5 (3.4. Inference), p. 2 (1. Introduction), p. 5 (3.4. Inference), p. 2 (1. Introduction), p. 4 (3.3. Fine-Tuning Protocol)): Capitalizing on that, we propose the following test-time ensembling scheme, capable of combining multiple inference passes over the same input.

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are: 1.
- **p. 5 / 3.4. Inference - extractive body cue:** This scheme enables a flexible trade-off between computation efficiency and prediction quality by choosing N accordingly.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we set out to explore this option and develop Marigold, a latent diffusion model (LDM) based on Stable Diffusion [38], along with ...
- **p. 4 / 3.3. Fine-Tuning Protocol - extractive body cue:** This normalization allows Marigold to focus on pure affine-invariant depth estimation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Future research directions to overcome current limitations include improving inference efficiency, ensuring that similar inputs yield consistent outputs ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | During training, we apply the DDPM noise scheduler [20] with 1000 diffusion steps. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | For the final prediction, we aggregate results from 10 inference runs with varying starting noise. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We investigate the impact of three types of noise during the training phase. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2. Network Architecture), p. 4 (3.2. Network Architecture), p. 5 (3.3. Fine-Tuning Protocol), p. 5 (3.4. Inference). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Network Architecture), p. 4 (3.2. Network Architecture), p. 5 (3.3. Fine-Tuning Protocol), p. 5 (3.4. Inference), objective p. 3 (3.1. Generative Formulation), p. 5 (3.4. Inference), p. 5 (3.3. Fine-Tuning Protocol), p. 3 (3.1. Generative Formulation), p. 4 (3.3. Fine-Tuning Protocol), p. 4 (3.1. Generative Formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
