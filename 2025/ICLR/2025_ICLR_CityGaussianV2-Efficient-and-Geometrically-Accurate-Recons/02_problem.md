# Problem - CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=a3ptUbuzbW; PDF retrieval source: https://openreview.net/pdf/602b5d6d17415fb9e6df86e7df8a1fe5990406d7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION)): On the one hand, existing methods face significant challenges related to scalability and generalization ability.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, manifesting efficient and high-fidelity novel view synthesis.
- **p. 1 / ABSTRACT - extractive PDF cue:** However, accurately representing surfaces, especially in large and complex scenarios, remains a significant challenge due to the unstructured nature of 3DGS.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this paper, we present CityGaussianV2, a novel approach for large-scale scene reconstruction that addresses critical challenges related to geometric accuracy and efficiency.
- **p. 1 / ABSTRACT - extractive PDF cue:** Building on the favorable generalization capabilities of 2D Gaussian Splatting (2DGS), we address its convergence and scalability issues.
- **p. 1 / ABSTRACT - extractive PDF cue:** Specifically, we implement a decomposed-gradient-based densification and depth regression technique to eliminate blurry artifacts and accelerate convergence.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** On the one hand, existing methods face significant challenges related to scalability and generalization ability.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In response to these challenges, we introduce CityGaussianV2, a geometrically accurate yet efficient strategy for large-scale scene reconstruction.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | On the one hand, existing methods face significant challenges related to scalability and generalization ability. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | begin, initializing, DGS, field, ground-truth, point, cloud, then, traverse, training | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | derived, outputs, loss, calculation, light, observation, implement, straightforward | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: begin, initializing, DGS, field, ground-truth, point, cloud, then, traverse, training | p. 7 (3 METHOD), p. 17 (C MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, four-fold, novel, optimization, strategy, DGS, accelerates | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: alleviate, problem, prioritize, gradient, SSIM, loss, introduce, Decomposed-Gradient-based | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 1 (Figure/Table caption), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In response to these challenges, we introduce CityGaussianV2, a geometrically accurate yet efficient strategy for large-scale scene reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Though these algorithms have been proven to be successful on small scenes or single objects, the challenges behind scaling up, including performance degradation, densification stability, ...
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Despite these advances, the issue of geometry accuracy has been largely overlooked due to the lack of reliable benchmarks.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Our work addresses this gap, proposing a reliable benchmark along with a novel algorithm for both economical training, high fidelity, and accurate geometry.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be scaled up to high capacity ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Furthermore, our contribution-based vectree quantization enables a tenfold reduction in storage requirements for large-scale 2DGS.
- **p. 6 / 3 METHOD - extractive PDF cue:** To resolve these issues, we propose a novel pipeline, as shown in Fig.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** TrimGS (Fan et al., 2024) further provides a novel per-Gaussian contribution definition to remove inaccurate geometry.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** One of the most seminal contributions to this field is Neural Radiance Fields (NeRF) (Mildenhall et al., 2021), which implicitly models target scenes using multi-layer ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Published as a conference paper at ICLR 2025 Ours Ground-truth CityGS SuGaR GOF 2DGS Modern Russian Aerial Convergence ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Furthermore, GOF fails to complete training or extract meaningful meshes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Table 1: Comparison with SOTA reconstruction methods. "NaN" means no results due to NaN error. "FAIL" means the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 7 (3 METHOD), p. 17 (C MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 5 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), interface p. 7 (3 METHOD), p. 17 (C MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 5 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
