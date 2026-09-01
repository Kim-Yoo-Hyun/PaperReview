# Problem - 3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Preliminary)): In addressing the above challenges, one common strategy is to represent the dynamic scenes as a combination of a static canonical field and a deformation model [11, 16, 17, 27, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose a 3D geometry-aware deformable Gaussian Splatting method for dynamic view synthesis.
- **p. 1 / Abstract - extractive PDF cue:** Existing neural radiance fields (NeRF) based solutions learn the deformation in an implicit manner, which cannot incorporate 3D scene geometry.
- **p. 1 / Abstract - extractive PDF cue:** Therefore, the learned deformation is not necessarily geometrically coherent, which results in unsatisfactory dynamic view synthesis and 3D dynamic reconstruction.
- **p. 1 / Abstract - extractive PDF cue:** Recently, 3D Gaussian Splatting provides a new representation of the 3D scene, building upon which the 3D geometry could be exploited in learning the complex ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, the scenes are represented as a collection of 3D Gaussian, where each 3D Gaussian is optimized to move and rotate over time to model ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In addressing the above challenges, one common strategy is to represent the dynamic scenes as a combination of a static canonical field and a deformation ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, this strategy has a limited cover range of local areas and cannot work at a later training stage.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In addressing the above challenges, one common strategy is to represent the dynamic scenes as a combination of a static canonical field ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Taking V as input, we perform sparse 3D U-Net to aggregate local features (dubbed as Fv ∈RM×C) of the point clouds. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Taking, input, perform, sparse, U-Net, aggregate, local, features, dubbed, point | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Due, inherent, motion/shape, ambiguity, monocular, dynamic, representation, scene | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Taking, input, perform, sparse, U-Net, aggregate, local, features, dubbed, point | p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, geometry-aware, feature, extraction, network, Gaussian | p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Gaussian Canonical Field) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Gaussian, Canonical, Field, Deformation, RGB, Gradient, Transformation, Inverse | p. 5 (3.4. Rasterization), p. 3 (3. Method), p. 5 (3.5. Optimization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Rasterization), p. 5 (3.5. Optimization), p. 3 (3. Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.5. Ablation Study), p. 6 (4.2. Implementation Details), p. 7 (4.4. Visualization Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, this strategy has a limited cover range of local areas and cannot work at a later training stage.
- **p. 1 / 1. Introduction - extractive PDF cue:** This is mainly due to the difficulty in modeling and representing the scene deformation.
- **p. 2 / 1. Introduction - extractive PDF cue:** Since point-level MLP has a limited receptive field, which cannot capture the local geometric features of point clouds.
- **p. 4 / 3.1. Preliminary - extractive PDF cue:** This ensures that the covariance matrix is positive semi-definite, while reducing the learning difficulty of 3D Gaussians: \mathbf {\Sigma }=\mathbf {R}\mathbf {S}\mathbf {S}^{\top }\mathbf {R}^{\top ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Gaussian Canonical Field), p. 1 (1. Introduction), p. 2 (1. Introduction)): Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric information. • We propose to use ...

- **p. 3 / 3. Method - extractive PDF cue:** Our method mainly consists of two core components: the Gaussian canonical field is used to learn the reconstruction of static scenes, while the deformation field ...
- **p. 4 / 3.2. Gaussian Canonical Field - extractive PDF cue:** Then, we propose a geometric branch, which enables geometry feature learning of the 3D Gaussian distributions for the subsequent deformation field.
- **p. 1 / 1. Introduction - extractive PDF cue:** Geometric information exploited by different methods. a) Early dynamic NeRF methods such as DNeRF[37] directly encode the coordinate p of the sample point as input ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The Gaussian canonical field consists of 3D Gaussian distributions and a geometry-aware feature learning network.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We addressed the limitations of existing approaches from two perspectives: 1) we introduced 3D sparse convolution to extract ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Since 3D-DS cannot model dynamic scenes, the quality of the point cloud is poor. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Since it inherently cannot model the deformation of the dynamic scene, 3D-GS performs poorly in dynamic view synthesis. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In Table 4, canonical DC shows a performance drop, as the canonical 3D Gaussian alone cannot reflect the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Preliminary), interface p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction), objective p. 5 (3.4. Rasterization), p. 3 (3. Method), p. 5 (3.5. Optimization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
