# Problem - BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve the issue.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) has demonstrated exceptional performance in reconstruction and novel view synthesis tasks.
- **p. 1 / Abstract - extractive body cue:** However, its reliance on Structure-from-Motion preprocessing may lead to degraded performance under sparse-view scenarios.
- **p. 1 / Abstract - extractive body cue:** Recent works attempt to address this limitation by leveraging pre-trained image matching models to generate Gaussian primitives but overlook the probabilistic uncertainty embedded in both ...
- **p. 1 / Abstract - extractive body cue:** This uncertainty can accumulate and degrade reconstruction fidelity.
- **p. 1 / Abstract - extractive body cue:** Hence, we propose BA-GS, a Bayesian framework that models both the global distribution and local uncertainty of Gaussian primitives.
- **p. 1 / 1. Introduction - extractive body cue:** Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve the issue.
- **p. 1 / 1. Introduction - extractive body cue:** Reconstructing real-world scenes from images is a fundamental problem in computer vision.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Although these approaches partially alleviate the challenges of sparse-view reconstruction such as rendering uncertainty and geometric inconsistency, they do not fundamentally resolve ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Noise Covriance Matrix Proposed Adaptive Kalman Filter Optimization Loop Step t-1 Step t Step t+1 Gradient Density Position Prior Propagate State Noisy ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Noise, Covriance, Matrix, Adaptive, Kalman, Filter, Optimization, Loop, Step, Gradient | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Since, amplitude, gradients, different, regions, reflects, complexity, image | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Noise, Covriance, Matrix, Adaptive, Kalman, Filter, Optimization, Loop, Step, Gradient | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising) |
| Decision / output variable | geometry/map/query r; body terms: Hence, introduce, variational, optimization, scheme, obtain, cleaner, more | p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: make, optimization, tractable, maximize, Evidence, Lower, Bound, ELBO | p. 5 (4.3. Kalman Filtering for Position Denoising), p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4.3. Kalman Filtering for Position Denoising), p. 4 (4.1. Variational Bayesian Initialization), p. 6 (4.3. Kalman Filtering for Position Denoising) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (5.3. Ablation Study), p. 7 (5.3. Ablation Study), p. 7 (5.2. Experiment Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Reconstructing real-world scenes from images is a fundamental problem in computer vision.

## What the Paper Changes

PDF body contribution framing (p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 1 (1. Introduction), p. 5 (4.2. Prior-Guided Adaptive Density Control)): Hence, we introduce a variational optimization scheme to obtain a cleaner and more structured initialization.

- **p. 4 / 4.1. Variational Bayesian Initialization - extractive body cue:** Since the exact posterior distribution is intractable for most mixture models, we introduce a variational distribution q, which is optimized to be as close as ...
- **p. 5 / 4.3. Kalman Filtering for Position Denoising - extractive body cue:** To stabilize this update, we introduce an Adaptive Kalman Filter that recursively fuses predicted positions with observed projections.
- **p. 1 / 1. Introduction - extractive body cue:** Recent advances such as Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS) [12, 20] have enabled high-quality novel view * Co-Corresponding authors. synthesis and ...
- **p. 5 / 4.2. Prior-Guided Adaptive Density Control - extractive body cue:** This allows the control mechanism to adapt to local geometric complexity rather than relying on a uniform hyperparameter.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Future works will explore richer priors, extending the Bayesian formulation to color and opacity estimation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 2. Overview of the global initialization Bayesian model (VB-GMM). The initial Gaussian primitives from MASt3R are refined ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | But the current formulation assumes Gaussian noise assumption and relies on density/gradient priors, which may not fully capture ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | When replacing the globally-aligned MASt3R initialization with VGGT, the deterministic optimization of InstantSplat degrades severely due to its ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 6 (4.3. Kalman Filtering for Position Denoising), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 1 (1. Introduction), objective p. 5 (4.3. Kalman Filtering for Position Denoising), p. 4 (4.1. Variational Bayesian Initialization), p. 4 (4.1. Variational Bayesian Initialization), p. 5 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising), p. 6 (4.3. Kalman Filtering for Position Denoising).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
