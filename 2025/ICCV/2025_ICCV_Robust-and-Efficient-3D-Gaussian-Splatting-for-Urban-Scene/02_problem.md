# Problem - Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, its *Corresponding author explicit representation introduces scalability challenges, as spatial complexity increases with scene size.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present a framework that enables fast reconstruction and real-time rendering of urban-scale scenes while maintaining robustness against appearance variations across multi-view captures.
- **p. 1 / Abstract - extractive PDF cue:** Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency.
- **p. 1 / Abstract - extractive PDF cue:** A controllable level-of-detail (LOD) strategy explicitly regulates Gaussian density under a user-defined budget, enabling efficient training and rendering while maintaining high visual fidelity.
- **p. 1 / Abstract - extractive PDF cue:** The appearance transformation module mitigates the negative effects of appearance inconsistencies across images while enabling flexible adjustments.
- **p. 1 / Abstract - extractive PDF cue:** Additionally, we utilize enhancement modules, such as depth regularization, scale regularization, and antialiasing, to improve reconstruction fidelity.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, its *Corresponding author explicit representation introduces scalability challenges, as spatial complexity increases with scene size.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, its *Corresponding author explicit representation introduces scalability challenges, as spatial complexity increases with scene size. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | For an unselected image Ii, the 3D point cloud of the scene is projected onto its image plane, and compute its convex ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | unselected, image, point, cloud, scene, projected, onto, plane, compute, convex | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Section, proposes, appearance, transform, module, ensure, robust, adaptation | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: unselected, image, point, cloud, scene, projected, onto, plane, compute, convex | p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail), p. 4 (3.5. Quality Enhancements) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, follows, novel, visibility-based, data, division | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: optimizing, attributes, Gaussians, carrying, densification, minimize, loss, DGS | p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.2. Scale Regularization), p. 3 (3.3. In-Partition Prioritized Densification), p. 3 (3.4. Controllable Level-of-detail), p. 4 (3.4. Controllable Level-of-detail), p. 5 (3.5.1. Appearance Transform Module) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.3. In-Partition Prioritized Densification), p. 4 (3.4. Controllable Level-of-detail), p. 5 (3.5.1. Appearance Transform Module) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.3. LOD Generation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- **p. 2 / 1. Introduction - extractive PDF cue:** Experimental results demonstrate that our method outperform existing methods in terms of reconstruction quality, resource efficiency, and rendering speed, enabling the reconstruction of arbitrarily large ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.3. In-Partition Prioritized Densification), p. 4 (3.4.1. Controllable Detail Level Generation)): The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale scene reconstruction. • A controllable ...

- **p. 1 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- **p. 2 / 1. Introduction - extractive PDF cue:** Experimental results demonstrate that our method outperform existing methods in terms of reconstruction quality, resource efficiency, and rendering speed, enabling the reconstruction of arbitrarily large ...
- **p. 3 / 3.3. In-Partition Prioritized Densification - extractive PDF cue:** To solve this problem, as shown in Figure 2 we propose a distance-related threshold for each Gaussian: τi = ˆτmin
- **p. 4 / 3.4.1. Controllable Detail Level Generation - extractive PDF cue:** Experiments show that our method achieves higher quality than compression-based method while enabling faster completion by utilizing low-resolution images and a smaller budget for lower ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Future work could explore incremental switching mechanisms for smoother transitions and improved resource efficiency. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Enhancing robustness to pose inaccuracies is thus an important future direction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Meanwhile, the FPS does not experience a significant decline and consistently ranks as either the best or second-best, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail), p. 4 (3.5. Quality Enhancements), p. 5 (3.5.1. Appearance Transform Module). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail), p. 4 (3.5. Quality Enhancements), p. 5 (3.5.1. Appearance Transform Module), objective p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.2. Scale Regularization), p. 3 (3.3. In-Partition Prioritized Densification), p. 3 (3.4. Controllable Level-of-detail), p. 4 (3.4. Controllable Level-of-detail), p. 5 (3.5.1. Appearance Transform Module).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
