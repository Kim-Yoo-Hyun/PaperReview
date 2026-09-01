# Problem - SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08870.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction)): Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** 3D mapping and reconstruction from multi-view images is crucial for a wide range of applications, such as virtual and augmented reality.
- **p. 1 / 1 Introduction - extractive PDF cue:** Given a set of unorganized images captured around an object, most pipelines proceed in two stages for obtaining the reconstruction.
- **p. 1 / 1 Introduction - extractive PDF cue:** 2 This work was done during the author's internship at Chohotech Co. ltd..
- **p. 2 / 1 Introduction - extractive PDF cue:** Dong et al. … NeuS BARF* Neuralangelo SCNeRF* Ours Images L2G-NeRF* Joint-TensoRF* Fig.
- **p. 2 / 1 Introduction - extractive PDF cue:** 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise.
- **p. 3 / 1 Introduction - extractive PDF cue:** Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures.
- **p. 3 / 1 Introduction - extractive PDF cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Specifically, for each scene, the input is a set of RGB images I = {I1, I2, ..., In}, and the output is ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Specifically, scene, input, RGB, images, output, surface, reconstruction, network, takes | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | node, corresponds, input, image, edge, between, nodes, indicates | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Specifically, scene, input, RGB, images, output, surface, reconstruction, network, takes | p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method) |
| Decision / output variable | path/waypoint/velocity; body terms: novel, framework, jointly, optimizes, neural, radiance, field, scene | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: IoU, loss, aims, maximize, intersection-over-union, between, MoGs, correspond | p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 7 (3 Method), p. 9 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (3 Method), p. 7 (3 Method), p. 5 (3 Method) |
| Success / guarantee | goal reach with collision-free execution | p. 14 (Figure/Table caption), p. 12 (4 Experiments), p. 14 (7.71 3.77†) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive PDF cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method)): In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.

- **p. 3 / 1 Introduction - extractive PDF cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our method works effectively and can produce high-quality 3D reconstructions. produce a sparse scene representation.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Scene Graph A scene graph G = (V, E) in SfM consists of a set of nodes V and edges E.
- **p. 5 / 3 Method - extractive PDF cue:** Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Even though our method can greatly refine the inlier poses, the improvement on outlier poses is moderate (whose ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Please also note that there are several failure cases from the competitors indicating completely incorrect reconstruction. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Most of these poses tend to come with a large angular deviation and cannot be rectified through local ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 9 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 9 (3 Method), objective p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 7 (3 Method), p. 9 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
