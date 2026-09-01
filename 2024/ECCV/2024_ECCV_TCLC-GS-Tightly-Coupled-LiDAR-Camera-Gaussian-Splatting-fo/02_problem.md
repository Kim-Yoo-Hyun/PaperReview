# Problem - TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7983_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07983.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, these methods face significant limitations due to their slow training and rendering speeds, which are further compounded by the critical requirement in real-time applications.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Urban-level reconstruction and rendering present significant challenges due to the vast scale of the unbounded environments and the sparse nature of the captured data.
- **p. 1 / 1 Introduction - extractive PDF cue:** Fortunately, in autonomous vehicle settings, data from various modalities captured by multiple sensors are typically available.
- **p. 1 / 1 Introduction - extractive PDF cue:** However, fully ⋆Equally contributed as co-first author.
- **p. 2 / 1 Introduction - extractive PDF cue:** 1: Left: Original 3D-GS [11] based methods directly initialize 3D Gaussians by 3D LiDAR points; Right: Our TCLC-GS enriches the geometry and appearance attributes of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Neural Radiance Fields (NeRF) [17] based solutions are effective in reconstructing urban environments when a sufficient number of images captured from diverse viewpoints are available.
- **p. 2 / 1 Introduction - extractive PDF cue:** However, these methods face significant limitations due to their slow training and rendering speeds, which are further compounded by the critical requirement in real-time applications.
- **p. 3 / 1 Introduction - extractive PDF cue:** However, this approach faces challenges in unbounded urban scenes within autonomous driving contexts, particularly when viewpoints are sparse.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these methods face significant limitations due to their slow training and rendering speeds, which are further compounded by the critical requirement ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Problem Definition: In an urban street scene, given a sequence of surrounding images and LiDAR data collected from a vehicle-mounted system, our ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Problem, Definition, urban, street, scene, given, sequence, surrounding, images, LiDAR | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Different, sparse, depth, supervision, derived, LiDAR, dense, rendered | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Problem, Definition, urban, street, scene, given, sequence, surrounding, images, LiDAR | p. 4 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology) |
| Decision / output variable | geometry/map/query r; body terms: present, visualization, examples, colorized, mesh, dense, depths, generated | p. 7 (3 Methodology), p. 3 (1 Introduction), p. 13 (13 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: train, binary, cross, entropy, BCE, loss, Lbce, math | p. 6 (3 Methodology), p. 6 (3 Methodology), p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive PDF cue:** However, this approach faces challenges in unbounded urban scenes within autonomous driving contexts, particularly when viewpoints are sparse.
- **p. 1 / 1 Introduction - extractive PDF cue:** Urban-level reconstruction and rendering present significant challenges due to the vast scale of the unbounded environments and the sparse nature of the captured data.
- **p. 2 / 1 Introduction - extractive PDF cue:** In addition, a significant limitation of these methods is their dependence on intensive volumetric sampling in free space, leading to excessive consumption of computational resources ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To facilitate better 3D Gaussian initialization, pioneering research [5,28,31] has introduced LiDAR priors into the 3D-GS process, enabling more accurate geometries and ensuring rendering consistency ...

## What the Paper Changes

PDF contribution framing (p. 7 (3 Methodology), p. 3 (1 Introduction), p. 13 (13 Method), p. 7 (3 Methodology), p. 13 (13 Method)): We present visualization examples of the colorized 3D mesh and dense depths generated by our method in Fig.

- **p. 3 / 1 Introduction - extractive PDF cue:** In this paper, we proposed a novel Tightly Coupled LiDAR-Camera Gaussian Splatting (TCLC-GS) for accurate modeling and real-time rendering in surrounding autonomous driving scenes.
- **p. 13 / 13 Method - extractive PDF cue:** According to Table 3, our method outperforms 3D-GS in the metrics of PSNR, SSIM, and LPIPS for novel image synthesis.
- **p. 7 / 3 Methodology - extractive PDF cue:** Different from directly initializing Gaussian by LiDAR points, our method initials 3D Gaussians GS on the 3D mesh M.
- **p. 13 / 13 Method - extractive PDF cue:** The lower depth performance of our method observed on the nuScenes dataset, compared to the Waymo dataset, is due to the nuScenes dataset's reliance on ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Fig. 3: Visualization of our colorized 3D mesh and dense depths. Row 1: rendered dense surrounding depth images ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Metrics: Following the previous research [5,15,20,28,31], our image synthesis evaluation employs three widely-used benchmark metrics, i.e., peak signal-tonoise ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | The significant improvement in depth synthesis performance can be attributed to the robust supervision provided by the rendered ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (3 Methodology), p. 7 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), objective p. 6 (3 Methodology), p. 6 (3 Methodology), p. 8 (3 Methodology), p. 8 (3 Methodology).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
