# Problem - SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=o1sF4XaFdY; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247825. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES), p. 3 (1 INTRODUCTION)): Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Reconstructing 3D scenes from sparse images remains a challenging task due to the difficulty of recovering accurate geometry and texture without optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Recent approaches leverage generalizable models to generate 3D scenes using 3D Gaussian Splatting (3DGS) primitive.
- **p. 1 / ABSTRACT - extractive body cue:** However, they often fail to produce continuous surfaces and instead yield discrete, color-biased point clouds that appear plausible at normal resolution but reveal severe artifacts ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue, we present SurfSplat, a feedforward framework based on 2D Gaussian Splatting (2DGS) primitive, which provides stronger anisotropy and higher geometric precision.
- **p. 1 / ABSTRACT - extractive body cue:** By incorporating a surface continuity prior and a forced alpha blending strategy, SurfSplat reconstructs coherent geometry together with faithful textures.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, we observe that existing feedforward methods tend to generate degraded 3D scenes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Furthermore, most datasets lack out-of-distribution viewpoints for reliable assessment. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This behavior rapidly boosts image quality for near-input viewpoints, but under the alpha-blending rendering rule, occluded Gaussians contribute minimally to the output: ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | behavior, rapidly, boosts, image, quality, near-input, viewpoints, under, alpha-blending, rendering | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Given, sparse, input, images, dual-path, encoder, processes, them | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: behavior, rapidly, boosts, image, quality, near-input, viewpoints, under, alpha-blending, rendering | p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Decision / output variable | geometry/map/query r; body terms: summary, main, contributions, follows, SurfSplat, feedforward, network, reconstructs | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: fused, features, subsequently, construct, cost, volumes, Chen, When | p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE), p. 15 (A.1 ENCODER ARCHITECTURE) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, we observe that existing feedforward methods tend to generate degraded 3D scenes.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Without effective regularization, the generated 3D scenes often lack realistic and continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this limitation, we render each reconstructed scene at a higher resolution (e.g., 2× or 4× the original), resulting in an output ˆIHR.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Despite these advancements, prior feedforward methods primarily rely on 3DGS primitives.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES)): In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian surfels from sparse inputs.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our model leverages a surface continuity prior and forced alpha blending to significantly improve reconstruction quality. • We introduce HRRC, a high-resolution rendering-based metric that ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** 3.6 HIGH-RESOLUTION RENDERING CONSISTENCY (HRRC) To better evaluate the geometric fidelity of reconstructed 3D scenes, we propose a novel evaluation metric: High-Resolution Rendering Consistency (HRRC).
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | By introducing a surface continuity prior and a forced alpha blending strategy, our method addresses key limitations of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | These artifacts reveal the limitations of previous feedforward 3DGS 8 | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | This observation highlights a key limitation of conventional NVS metrics and underscores the value of our proposed HRRC ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (3.1 PRELIMINARIES), p. 3 (1 INTRODUCTION), interface p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), objective p. 4 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
