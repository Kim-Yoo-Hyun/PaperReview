# Problem - ThermalGaussian: Thermal 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ybFRoGxZjs; PDF retrieval source: https://openreview.net/pdf/4daa89ce065b5e5cc408ac37b25bc7f3c49e924d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, these datasets suffer from problems such as lack of color images registered with thermal images, inconsistencies in thermal information from different views, and watermarked images.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Thermography is especially valuable for the military and other users of surveillance cameras.
- **p. 1 / ABSTRACT - extractive PDF cue:** Some recent methods based on Neural Radiance Fields (NeRF) are proposed to reconstruct the thermal scenes in 3D from a set of thermal and RGB ...
- **p. 1 / ABSTRACT - extractive PDF cue:** However, unlike NeRF, 3D Gaussian splatting (3DGS) prevails due to its rapid training and real-time rendering.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we propose ThermalGaussian, the first thermal 3DGS approach capable of rendering high-quality images in RGB and thermal modalities.
- **p. 1 / ABSTRACT - extractive PDF cue:** We first calibrate the RGB camera and the thermal camera to ensure that both modalities are accurately aligned.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, these datasets suffer from problems such as lack of color images registered with thermal images, inconsistencies in thermal information from different views, and watermarked ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, these methods not only fail to fully exploit thermal information but are also constrained by the limitations of traditional 3D reconstruction techniques, which impede ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these datasets suffer from problems such as lack of color images registered with thermal images, inconsistencies in thermal information from different ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Published as a conference paper at ICLR 2025 point clouds obtained from multimodal initialization as inputs. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Published, conference, ICLR, point, clouds, obtained, multimodal, initialization, inputs, capture | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Subsequently, rendered, images, modalities, compared, separately, ground, truth | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Published, conference, ICLR, point, clouds, obtained, multimodal, initialization, inputs, capture | p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Decision / output variable | geometry/map/query r; body terms: final, design, loss, LRGB, Lthermal, SELF-COLLECTED, THERAML, DATASET | p. 7 (3 METHOD), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: RGB, rendering, achieved, Formula, while, thermal, follows, equation | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 METHOD), p. 5 (3 METHOD), p. 7 (3 METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** However, these methods not only fail to fully exploit thermal information but are also constrained by the limitations of traditional 3D reconstruction techniques, which impede ...

## What the Paper Changes

PDF contribution framing (p. 7 (3 METHOD), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): The final design of this loss is: L = γLRGB + (1 -γ)Lthermal (12) 4 SELF-COLLECTED THERAML DATASET We introduce a new dataset, named RGBT-Scenes, which consists of aligned collections ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, the main contributions as follows: (1)We propose ThermalGaussian, the first multimodal 3DGS capable of simultaneously rendering photorealistic thermal and RGB images of a ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Published as a conference paper at ICLR 2025 (3)We introduce RGBT-Scenes, a new dataset designed for thermal 3D reconstruction and novelview synthesis.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In contrast, our method not only improves thermal rendering quality but also enhances RGB rendering quality by 1 dB.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** The dataset consists of paired RGB and thermal images captured from multiple viewpoints across 10 different scenes.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 2: Top: camera poses and point cloud generated by SfM. Bottom: input images for SfM. geometry methods ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Published as a conference paper at ICLR 2025 Table 2: Quantitative evaluation of thermal image using our method ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We then performed a comprehensive comparison across various dimensions, including rendering capability, the quality of rendered color and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our results demonstrate that, under multimodal constraints, when one modality fails, our approach leverages accurate information from the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 6 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), objective p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 7 (3 METHOD), p. 7 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
