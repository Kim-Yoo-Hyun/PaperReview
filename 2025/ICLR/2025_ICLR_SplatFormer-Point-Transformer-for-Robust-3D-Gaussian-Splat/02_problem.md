# Problem - SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9NfHbWKqMF; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/111734. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): 1, existing NVS methods perform poorly on the OOD views when restricted to low-elevation inputs, highlighting the need for a novel approach to address this problem.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** 3D Gaussian Splatting (3DGS) has recently transformed photorealistic reconstruction, achieving high visual fidelity and real-time performance.
- **p. 1 / ABSTRACT - extractive body cue:** However, rendering quality significantly deteriorates when test views deviate from the camera angles used during training, posing a major challenge for applications in immersive free-viewpoint ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we conduct a comprehensive evaluation of 3DGS and related novel view synthesis methods under out-ofdistribution (OOD) test camera scenarios.
- **p. 1 / ABSTRACT - extractive body cue:** By creating diverse test cases with synthetic and real-world datasets, we demonstrate that most existing methods, including those incorporating various regularization techniques and data-driven priors, ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this limitation, we introduce SplatFormer, the first point transformer model specifically designed to operate on Gaussian splats.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 1, existing NVS methods perform poorly on the OOD views when restricted to low-elevation inputs, highlighting the need for a novel approach to address this ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 1, existing NVS methods perform poorly on the OOD views when restricted to low-elevation inputs, highlighting the need for a novel approach ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | It outputs residuals that are added to the input Gaussian attributes. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | outputs, residuals, added, input, Gaussian, attributes, While, initial, representation, effectively | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Additionally, some, feed-forward, models, predict, primitives, input, views | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: outputs, residuals, added, input, Gaussian, attributes, While, initial, representation, effectively | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: summary, make, following, contributions, introduce, OOD-NVS, experimental, protocol | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: reduce, computational, costs, terminate, optimization, early, steps, where | p. 16 (B IMPLEMENTATION DETAILS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 16 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results demonstrate that existing methods struggle to generalize under the OOD-NVS protocol; • We propose SplatFormer, a novel learning-based model that refines flawed 3D ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Traditionally, this problem has been approached using a standard novel view interpolation protocol, where test views are sampled at fixed intervals along the trajectory of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** A related research problem is 3D reconstruction from sparse input views, where methods often hallucinate unseen content (Liu et al., 2023a; Chan et al., 2023; ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 15 (B IMPLEMENTATION DETAILS)): In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods when rendering 3D scenes from novel ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To meet these needs, we propose SplatFormer, a novel learning-based feed-forward 3D transformer designed to operate on Gaussian splats.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results demonstrate that existing methods struggle to generalize under the OOD-NVS protocol; • We propose SplatFormer, a novel learning-based model that refines flawed 3D ...
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** Each MLP branch consists of four linear layers, with hidden dimensions of 512 and ReLU activations for all but the last layer.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Our method has several limitations that provide directions for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Finally, we discuss the limitations of our approach and potential directions for future research. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (B IMPLEMENTATION DETAILS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (B IMPLEMENTATION DETAILS), objective p. 16 (B IMPLEMENTATION DETAILS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
