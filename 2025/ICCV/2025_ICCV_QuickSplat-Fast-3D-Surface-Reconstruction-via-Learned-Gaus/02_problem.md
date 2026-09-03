# Problem - QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Surface reconstruction is fundamental to computer vision and graphics, enabling applications in 3D modeling, mixed reality, robotics, and more.
- **p. 1 / Abstract - extractive body cue:** Existing approaches based on volumetric rendering obtain promising results, but optimize on a per-scene basis, resulting in a slow optimization that can struggle to model ...
- **p. 1 / Abstract - extractive body cue:** We introduce QuickSplat, which learns datadriven priors to generate dense initializations for 2D gaussian splatting optimization of large-scale indoor scenes.
- **p. 1 / Abstract - extractive body cue:** This provides a strong starting point for the reconstruction, which accelerates the convergence of the optimization and improves the geometry of flat wall structures.
- **p. 1 / Abstract - extractive body cue:** We further learn to jointly estimate the densification and update of the scene parameters during each iteration; our proposed densifier network predicts new Gaussians based ...
- **p. 1 / 1. Introduction - extractive body cue:** In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem.
- **p. 2 / 1. Introduction - extractive body cue:** Our priors also guide the optimization towards high-quality indoor-scene geometry and thus overcome limitations stemming from insufficient observations or textureless regions (e.g., floating artifacts or ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In particular, achieving both high fidelity as well as efficient and fast reconstruction for large scenes remains a difficult problem. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Our method reconstructs the surface of large-scale indoor scenes from posed images as input. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | reconstructs, surface, large-scale, indoor, scenes, posed, images, input, learn, several | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | SfM, points, input, multi-view, images, initializer, network, predicts | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: reconstructs, surface, large-scale, indoor, scenes, posed, images, input, learn, several | p. 2 (3. Method), p. 2 (1. Introduction), p. 3 (3. Method) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, learned, generalized, initializer, network, leverages, scene | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Initialization Prior) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Initializer, SfM, points, New, Densifier, Optimizer, Gradients, Rendering | p. 3 (3. Method), p. 4 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 3 (3. Method), p. 4 (3.2. Initialization Prior) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Surface Representation), p. 4 (3.2. Initialization Prior), p. 5 (3.3. Iterative Gaussian Optimization) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Our priors also guide the optimization towards high-quality indoor-scene geometry and thus overcome limitations stemming from insufficient observations or textureless regions (e.g., floating artifacts or ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel generalized prior for 3D surface reconstruction.
- **p. 1 / 1. Introduction - extractive body cue:** Surface reconstruction of large, real-world scenes is a key problem in computer vision and graphics.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Initialization Prior), p. 3 (3.1. Surface Representation), p. 4 (3.3. Iterative Gaussian Optimization)): To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more efficient and accurate 3D surface reconstruction ...

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel generalized prior for 3D surface reconstruction.
- **p. 3 / 3.2. Initialization Prior - extractive body cue:** The first step in our method is to create an initialization of all Gaussians G.
- **p. 3 / 3.1. Surface Representation - extractive body cue:** We propose to predict G with neural networks instead of optimizing the primitives directly with gradient descent.
- **p. 4 / 3.3. Iterative Gaussian Optimization - extractive body cue:** To this end, we introduce another learnable component, the densifier network θD, that predicts additional voxel features in free space.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Second, we assume static environments and therefore cannot reconstruct dynamic scenes (e.g., people walking inside of a room). | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Lastly, even though we significantly reduce optimization runtime, our method does not yet reconstruct in real-time, but could ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (3. Method), p. 2 (1. Introduction), p. 3 (3. Method), p. 5 (3.3. Iterative Gaussian Optimization). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (3. Method), p. 2 (1. Introduction), p. 3 (3. Method), p. 5 (3.3. Iterative Gaussian Optimization), objective p. 3 (3. Method), p. 4 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 5 (3.3. Iterative Gaussian Optimization), p. 3 (3. Method), p. 4 (3.2. Initialization Prior).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
