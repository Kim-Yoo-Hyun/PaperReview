# Problem - SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation)): This prevents leveraging large-scale cross-scene data to learn 3D-specific SR priors and to train a generalized 3DSR model, thereby inherently limiting reconstruction fidelity, cross-scene generalization, and real-time usage.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D super-resolution (3DSR) aims to reconstruct highresolution (HR) 3D scenes from low-resolution (LR) multiview images.
- **p. 1 / Abstract - extractive PDF cue:** Existing methods rely on dense LR inputs and per-scene optimization, which restricts the highfrequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited ...
- **p. 1 / Abstract - extractive PDF cue:** This severely limits reconstruction fidelity, cross-scene generalization, and real-time usability.
- **p. 1 / Abstract - extractive PDF cue:** We propose to reformulate 3DSR as a direct feedforward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific ...
- **p. 1 / Abstract - extractive PDF cue:** This fundamentally changes how 3DSR acquires high-frequency knowledge and enables robust generalization to unseen scenes.
- **p. 2 / 1. Introduction - extractive PDF cue:** Although this strategy injects high-frequency cues into the HR 3DGS reconstruction, it suffers from several fundamental limitations.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This prevents leveraging large-scale cross-scene data to learn 3D-specific SR priors and to train a generalized 3DSR model, thereby inherently limiting reconstruction ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | This task has become increasingly critical because state-of-the-art 3D Gaussian Splatting (3DGS)-based reconstruction methods [14, 25] typically require dense and high-resolution input ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | task, become, increasingly, critical, because, state-of-the-art, Gaussian, Splatting, DGS, reconstruction | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Formally, given, input, views, camera, intrinsics, goal, learn | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: task, become, increasingly, critical, because, state-of-the-art, Gaussian, Splatting, DGS, reconstruction | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, follows, novel, formulation, DSR, SR3R, feed-forward | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Following, adopt, combination, pixel-wise, reconstruction, loss, MSE, perceptual | p. 6 (3.6. Training Objective) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3.6. Training Objective), p. 3 (3.1. Problem Formulation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.4. Ablation Study), p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Although this strategy injects high-frequency cues into the HR 3DGS reconstruction, it suffers from several fundamental limitations.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** We reformulate 3DGS-based 3DSR as a feed-forward mapping problem from LR multi-view images to an HR 3DGS representation.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Overall Framework), p. 4 (3.4. LR Image to HR 3DGS Mapping)): The main contributions are as follows. • A novel formulation of 3DSR.

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose SR3R, a feed-forward framework that directly reconstructs HR 3DGS from as few as two LR views through a learned mapping network.
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.
- **p. 4 / 3.2. Overall Framework - extractive PDF cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive PDF cue:** To correct these unreliable 2D features, we introduce a feature refinement module that aligns the encoder tokens ten ∈RN×C with geometry-aware tokens tpre ∈RN×C extracted ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | These improvements hold for both 3DGS backbones, confirming that our offsetbased refinement and cross-view fusion effectively restore 3D-specific ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Applying 2D upsampling reduces excessive softness but still fails to recover reliable high-frequency structures, often introducing ambiguous or ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Notably, even Bilinear interpolation already surpasses all feed-forward baselines (Table 1), indicating that SR3R does not depend on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results highlight the advantage of learning Gaussian offsets over direct parameter regression, enabling more accurate high-frequency recovery ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.4. LR Image to HR 3DGS Mapping). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), interface p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.4. LR Image to HR 3DGS Mapping), objective p. 6 (3.6. Training Objective).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
