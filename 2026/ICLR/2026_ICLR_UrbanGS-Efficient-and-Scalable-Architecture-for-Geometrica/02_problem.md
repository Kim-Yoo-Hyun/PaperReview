# Problem - UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=L3utaw6SD9; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248058. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES)): However, due to the unstructured nature of 3DGS, accurately representing surfaces-especially in large-scale complex scenes-remains a significant challenge.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** While 3D Gaussian Splatting (3DGS) enables high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments gives rise to critical challenges in terms ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these issues, we present UrbanGS, a scalable reconstruction framework that effectively tackles these challenges for city-scale applications.
- **p. 1 / ABSTRACT - extractive body cue:** First, we propose a Depth-Consistent D-Normal Regularization module.
- **p. 1 / ABSTRACT - extractive body cue:** Unlike existing approaches that rely solely on monocular normal estimators, which can effectively update rotation parameters yet struggle to update position parameters, our method integrates ...
- **p. 1 / ABSTRACT - extractive body cue:** This allows for comprehensive updates of all geometric parameters.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, due to the unstructured nature of 3DGS, accurately representing surfaces-especially in large-scale complex scenes-remains a significant challenge.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These limitations underscore the urgent need for a unified framework that balances geometric precision, memory efficiency, and seamless scalability.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to the unstructured nature of 3DGS, accurately representing surfaces-especially in large-scale complex scenes-remains a significant challenge. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | First, the rendered depth map is back-projected into point clouds{dk(n, p)}, using the camera intrinsic matrix. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | First, rendered, depth, back-projected, point, clouds, camera, intrinsic, matrix, ensures | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | reconstruct, scene, surfaces, enforce, normal, priors, predicted, pretrained | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: First, rendered, depth, back-projected, point, clouds, camera, intrinsic, matrix, ensures | p. 5 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, below, Depth-Consistent, D-Normal, Regularizer, enables | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: formulation, minimizes, relative, depth, errors, pixel, while, enhancing | p. 4 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** These limitations underscore the urgent need for a unified framework that balances geometric precision, memory efficiency, and seamless scalability.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** In urban-scale scenes, D-Normal regularization optimizes geometry through normal-depth associations but lacks explicit cross-view depth constraints, frequently causing building misalignment and street distortion-especially in distant/co ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** To overcome these limitations, we propose a unified, spatially adaptive pruning framework.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3.1 PRELIMINARIES)): Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the limitation of incomplete geometric upda ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To overcome this limitation, we introduce a Depth-Consistent D-Normal Regularization framework.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose UrbanGS, a strategy that achieves high geometric accuracy, fidelity, and efficiency in large-scale scene reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To meet the memory and computational demands of urban-scale reconstruction, we propose a Spatially Adaptive Gaussian Pruning (SAGP) method.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** (4) In our method, the depth map is rendered by performing a weighted sum of depths (Bae & Davison, 2024; Chen et al., 2024b; Yu ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Table 2: Detailed geometry evaluation on the GauU-Scene dataset (Xiong et al., 2024). "NaN" indicates that the method ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 25 | Qualitative results in Figure F show that rendered views remain visually consistent across different weight combinations, with no ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1: We propose UrbanGS, a scalable framework for high-fidelity large-scale scene reconstruc- tion. Left: It reconstructs complex ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | This discrepancy highlights a limitation of current geometry optimization objectives when applied to background regions lacking clear geometric ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), interface p. 5 (3.1 PRELIMINARIES), p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), objective p. 4 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
