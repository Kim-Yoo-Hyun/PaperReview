# Problem - CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03580.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): Traditional visual SLAM systems [24] have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, and surfel) demonstrate limitations in facilitating highly free ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Traditional visual SLAM systems [24] have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, and surfel) demonstrate ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Inspired by the Neural Radiance Field (NeRF) [29] in surface reconstruction and view rendering, some novel NeRF-based SLAM methods [17,28,37,61] have ∗Jiarui Hu and Xianhao ...
- **p. 2 / 1 Introduction - extractive PDF cue:** FPS ≈15 Hz Mean PSNR: 33.27 dB Mean PSNR: 34.60 dB Acc: 1.10 cm RMSE: 0.29 cm Acc: 1.28 cm RMSE: 0.31 cm Fig.
- **p. 2 / 1 Introduction - extractive PDF cue:** 1: CG-SLAM, which adopts a well-designed 3D Gaussian field, can simultaneously achieve state-of-the-art performance in localization, reconstruction and rendering.
- **p. 2 / 1 Introduction - extractive PDF cue:** At the same time, we observed that solely employing alpha-blending depth cannot
- **p. 2 / 1 Introduction - extractive PDF cue:** As a photorealistic view synthesis technique, the 3D Gaussian field is prone to overfitting the input images due to strong anisotropy and the lack of ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Traditional visual SLAM systems [24] have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Hence, uncertainty, model, suitable, RGB-D, observations, perspectives, rendering, images, Gaussian | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Jiarui, Xianhao, Chen, determined, difference, between, depth, observations | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Hence, uncertainty, model, suitable, RGB-D, observations, perspectives, rendering, images, Gaussian | p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method) |
| Decision / output variable | path/waypoint/velocity; body terms: Overall, contributions, summarized, follows, present, GPU-accelerated, framework, real-time | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 7 (3 Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Finally, minimizing, re-rendering, loss, low-uncertainty, primitives, build, real-time | p. 9 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |
| Success / guarantee | goal reach with collision-free execution | p. 14 (56.50 MB), p. 10 (4 Experiments), p. 10 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** At the same time, we observed that solely employing alpha-blending depth cannot
- **p. 2 / 1 Introduction - extractive PDF cue:** As a photorealistic view synthesis technique, the 3D Gaussian field is prone to overfitting the input images due to strong anisotropy and the lack of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Furthermore, in order to further improve the system's accuracy and efficiency, we design a novel depth uncertainty model to guide our Gaussian-based SLAM to focus ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 7 (3 Method), p. 7 (3 Method), p. 6 (3 Method)): Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough theoretical analysis of camera pose derivatives ...

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we introduce a real-time Gaussian splatting SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and ...
- **p. 7 / 3 Method - extractive PDF cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.
- **p. 7 / 3 Method - extractive PDF cue:** Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives.
- **p. 6 / 3 Method - extractive PDF cue:** Fast Gaussian splatting rasterizer enables efficient pixel-by-pixel parallel rendering, and is fully differentiable, which provides a useful GPU-accelerated framework.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | Considerable memory usage is one limitation of the Gaussianbased system. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other methods on average. "-" indicates failure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure situation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Due to the inherent limitation of 3D Gaussian representation, our method is slightly worse in completion. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), objective p. 9 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
