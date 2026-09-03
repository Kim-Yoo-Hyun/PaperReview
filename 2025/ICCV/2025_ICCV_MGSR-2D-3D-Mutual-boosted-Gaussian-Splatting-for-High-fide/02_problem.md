# Problem - MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, 2DGS still cannot effectively model surfaces when ambient lighting changes.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Novel view synthesis (NVS) and surface reconstruction (SR) are essential tasks in 3D Gaussian Splatting (3DGS).
- **p. 1 / Abstract - extractive body cue:** Despite recent progress, these tasks are often addressed independently, with GS-based rendering methods struggling under diverse light conditions and failing to produce accurate surfaces, while ...
- **p. 1 / Abstract - extractive body cue:** This raises a central question: must rendering and reconstruction always involve a trade-off?
- **p. 1 / Abstract - extractive body cue:** To address this, we propose MGSR, a 2D/3D Mutual-boosted Gaussian Splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy.
- **p. 1 / Abstract - extractive body cue:** MGSR introduces two branches-one based on 2DGS and the other on 3DGS.
- **p. 1 / 1. Introduction - extractive body cue:** However, 2DGS still cannot effectively model surfaces when ambient lighting changes.
- **p. 1 / 1. Introduction - extractive body cue:** However, despite the effectiveness of illumination decomposition in rendering, these methods are time-consuming and still struggle to achieve meaningful mesh extraction due to inherent limitations ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, 2DGS still cannot effectively model surfaces when ambient lighting changes. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 2D Gaussians Normals Images Depths 2D-GS Branch Ref-images Ref-map × + Trans-images 3D Gaussians 3D-GS Branch Depths Mutual-boosted Supervision NVS SR Inputs ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Gaussians, Normals, Images, Depths, D-GS, Branch, Ref-images, Ref-map, Trans-images, Mutual-boosted | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | encourage, alternating, optimization, focus, foreground, part, input, images | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Gaussians, Normals, Images, Depths, D-GS, Branch, Ref-images, Ref-map, Trans-images, Mutual-boosted | p. 4 (3.2. Illumination decomposition with 3DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians) |
| Decision / output variable | geometry/map/query r; body terms: solve, contradictions, MGSR, D/3D, Mutual-boosted, Gaussian, splatting, Surface | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: total, loss, Ltotal, alternating, optimization, w2DL2D, w3DL3D, wdepth-mutualLZ | p. 5 (3.3. Surface reconstruction with 2DGS), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 3 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. Datasets and evaluation metrics), p. 8 (4.2. Results), p. 7 (4.2. Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, despite the effectiveness of illumination decomposition in rendering, these methods are time-consuming and still struggle to achieve meaningful mesh extraction due to inherent limitations ...
- **p. 2 / 1. Introduction - extractive body cue:** Prior to alternating optimization, the two modules undergo an independent warm-up stage, and an autostop strategy is introduced to reduce unnecessary computational burdens.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.3. Surface reconstruction with 2DGS)): To solve these contradictions, we propose MGSR, a 2D/3D Mutual-boosted Gaussian splatting for Surface Reconstruction that enhances both rendering quality and 3D reconstruction accuracy (Figure 1c).

- **p. 2 / 1. Introduction - extractive body cue:** The input consists of multi-view images captured from various camera positions and angles, under significantly varying light conditions.
- **p. 3 / 3.1. Overview - extractive body cue:** MGSR is a 2D/3D mutual-boosted framework that consists of two branches: improved 3DGS branch (Section 3.2) and 2DGS branch (Section 3.3).
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we introduce a geometry-guided illumination decomposition module, which leverages depth information from the 2DGS branch to enhance rendering performance under diverse ...
- **p. 5 / 3.3. Surface reconstruction with 2DGS - extractive body cue:** The overall loss of the 2DGS branch consists of a weighted combination: L2D = Lrender + λ3(γLn + λ4Ln-TV) + λ5Ld-TV, (11) where λ3, λ4, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | To address this issue, NC is introduced as an evaluation metric for reconstruction, overcoming the limitations of CDs, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | A possible way for addressing this issue is to incorporate exposure compensation for input images, which we will ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Due to the limitation of CD, we mainly focus on NC metric, which aligns better 27300 | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Previous GS-based methods fail to effectively reconstruct glass or mirror surfaces, resulting in damaged and inaccurate surfaces. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2. Illumination decomposition with 3DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Illumination decomposition with 3DGS), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 2 (1. Introduction), objective p. 5 (3.3. Surface reconstruction with 2DGS), p. 5 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 6 (3.4. Alternating optimization of 2D & 3D Gaussians), p. 3 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS), p. 4 (3.2. Illumination decomposition with 3DGS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
