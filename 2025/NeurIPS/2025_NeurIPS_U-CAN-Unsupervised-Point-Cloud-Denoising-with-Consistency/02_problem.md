# Problem - U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=hVFtXE19Me; PDF retrieval source: https://arxiv.org/pdf/2510.25210. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): However, the current unsupervised approaches still struggle to predict

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Point clouds captured by scanning sensors are often perturbed by noise, which have a highly negative impact on downstream tasks (e.g. surface reconstruction and shape ...
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- **p. 1 / Abstract - extractive body cue:** Specifically, we leverage a neural network to infer a multi-step denoising path for each point of a shape or scene with a noise to noise ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / 1 Introduction - extractive body cue:** However, the current unsupervised approaches still struggle to predict
- **p. 2 / 1 Introduction - extractive body cue:** precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the current unsupervised approaches still struggle to predict | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | evaluations, under, widely, benchmarks, point, cloud, denoising, upsampling | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, follows, introduce, U-CAN, novel, framework | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: main, contributions, summarized, follows, introduce, U-CAN, novel, framework | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.
- **p. 2 / 1 Introduction - extractive body cue:** Another challenge in predicting robust denoising arises from the unknown location of true surfaces when only noisy observations are available.
- **p. 1 / 1 Introduction - extractive body cue:** The subsequent approaches, such as TotalDenoising [14], therefore turn to explore unsupervised point cloud denoising by leveraging a spatial prior term for total-level denoising.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)): Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising ...

- **p. 2 / 1 Introduction - extractive body cue:** In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For unsupervised denoising, the TTD [14] fails to produce high-fidelity local geometries with only the global constraints. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Note that U-CAN does not require (1) sparse-to-dense point cloud pairs and (2) clean point clouds, where the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 1: Overview of our method. (a) We design a multi-step denoising framework to gradually filter the noisy ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), objective p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
