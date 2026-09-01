# Problem - iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=W7vOFBCGPm&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminary)): Reconstructing objects from sparse views poses a significant challenge yet holds paramount importance for various applications, including 3D content creation, augmented reality, virtual reality, and robotics.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.
- **p. 1 / Abstract - extractive PDF cue:** While single-view reconstruction yields visually appealing results, it can deviate significantly from the actual object, especially on unseen sides.
- **p. 1 / Abstract - extractive PDF cue:** Additional views improve reconstruction fidelity but necessitate known camera poses.
- **p. 1 / Abstract - extractive PDF cue:** However, assuming the availability of pose may be unrealistic, and existing pose estimators fail in sparseview scenarios.
- **p. 1 / Abstract - extractive PDF cue:** To address this, we harness a pre-trained novel view synthesis diffusion model, which embeds implicit knowledge about the geometry and appearance of diverse objects.
- **p. 1 / 1. Introduction - extractive PDF cue:** Reconstructing objects from sparse views poses a significant challenge yet holds paramount importance for various applications, including 3D content creation, augmented reality, virtual reality, and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** A generic framework for pose-free, sparse-view 3D reconstruction is still lacking, posing a significant obstacle to real-world applications with casually captured photos.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Reconstructing objects from sparse views poses a significant challenge yet holds paramount importance for various applications, including 3D content creation, augmented reality, ... | high-dimensional data 또는 robot action-trajectory distribution | body wording is the source claim |
| Observation / input | (a) Given as few as two pose-free images (xr, xq), we estimate the pose ˆTr→q from T0 to optimally reconstruct the input ... | conditioning observation와 noisy/intermediate sample | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, pose-free, images, estimate, pose, optimally, reconstruct, input, view, through | latent/noise variable와 conditional distribution | notation and tensor shape require body check |
| Output / action | Moreover, optionally, take, conditional, inputs, texts, bounding, layouts | generated sample, action chunk 또는 trajectory | exact unit/frame/decoder require body check |
| Target outcome | sample quality, diversity and latency | distribution fit, multimodality, sample quality와 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | data x₀, noisy state x_t, condition c; body terms: Given, pose-free, images, estimate, pose, optimally, reconstruct, input, view, through | p. 4 (3.1. Diffusion as a Pose Estimator), p. 2 (1. Introduction), p. 3 (2. Preliminary) |
| Decision / output variable | sample/action x̂ or trajectory; body terms: introduce, iFusion, novel, framework, reconstructs, diverse, objects, sparse | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. From Single-View to Multi-View) |
| Objective / loss / cost | distribution/denoising/flow objective; cue terms: ensure, estimated, pose, continue, manifold, during, gradientbased, optimization | p. 3 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 5 (3.3. From Sparse Views to 3D Reconstruction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 4 (3.1. Diffusion as a Pose Estimator) |
| Success / guarantee | sample quality, diversity and latency | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 7 (4.3. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** A generic framework for pose-free, sparse-view 3D reconstruction is still lacking, posing a significant obstacle to real-world applications with casually captured photos.
- **p. 2 / 1. Introduction - extractive PDF cue:** This indicates that the model has learned rich prior knowledge about the geometry and appearance of diverse objects.
- **p. 3 / 2. Preliminary - extractive PDF cue:** 3D Reconstruction via Score Distillation Sampling Recent studies [18, 39, 47, 67] indicated that large-scale pretrained 2D vision models [50, 52, 54] implicitly encapsulate rich ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. From Single-View to Multi-View), p. 3 (2. Preliminary), p. 3 (3. Method)): To this end, we introduce iFusion, a novel framework that reconstructs diverse 3D objects with sparse, pose-free views.

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose a novel camera pose estimator that significantly outperforms existing methods in terms of both accuracy and required number of input views, while being ...
- **p. 4 / 3.2. From Single-View to Multi-View - extractive PDF cue:** We propose to close the gap by further fine-tuning the DM with the given views and estimated poses.
- **p. 3 / 2. Preliminary - extractive PDF cue:** For instance, the standalone SD takes texts as the condition c and enables textto-image generation (T2I).
- **p. 3 / 3. Method - extractive PDF cue:** Next, the registered views are leveraged to customized the novel view synthesis model for the target object as in Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Notably, COLMAP [55] cannot serve as a baseline in our evaluation due to the structural limitations of Structure-from-Motion, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We found that by leveraging the diffusion model [31], iFusion excels at handling diverse objects thanks to its ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Row (c) highlights the substantial improvement from the stochastic re-sampling of multiview conditions at each timestep, providing more ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Figure 8. More qualitative results on pose estimation. The predicted poses (thin) and their corresponding ground truth (bold), ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

generative writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.1. Diffusion as a Pose Estimator), p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 3 (3.1. Diffusion as a Pose Estimator). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminary), interface p. 4 (3.1. Diffusion as a Pose Estimator), p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 3 (3.1. Diffusion as a Pose Estimator), objective p. 3 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction), p. 5 (3.3. From Sparse Views to 3D Reconstruction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
