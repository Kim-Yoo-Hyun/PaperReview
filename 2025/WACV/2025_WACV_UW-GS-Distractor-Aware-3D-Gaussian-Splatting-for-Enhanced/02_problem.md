# Problem - UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation), p. 1 (1. Introduction)): However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3DGS) offers the capability to achieve real-time high quality 3D scene rendering.
- **p. 1 / Abstract - extractive body cue:** However, 3DGS assumes that the scene is in a clear medium environment and struggles to generate satisfactory representations in underwater scenes, where light absorption and ...
- **p. 1 / Abstract - extractive body cue:** To overcome these, we introduce a novel Gaussian Splatting-based method, UW-GS, designed specifically for underwater applications.
- **p. 1 / Abstract - extractive body cue:** It introduces a color appearance that models distance-dependent color variation, employs a new physics-based density control strategy to enhance clarity for distant objects, and uses ...
- **p. 1 / Abstract - extractive body cue:** Optimized with a well-designed loss function supporting for scattering media and strengthened by pseudo-depth maps, UW-GS outperforms existing methods with PSNR gains up to 1.26dB.
- **p. 1 / 1. Introduction - extractive body cue:** However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs.
- **p. 2 / 1. Introduction - extractive body cue:** Finally, given the scarcity of underwater datasets, we collected a new dataset featuring four expansive areas of shallow underwater scenes, each presenting unique challenges compared ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The 3D Gaussians with modified color will be sent to do 2D projection and then generate pixel color in rasterization module to ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Gaussians, modified, color, will, sent, projection, then, generate, pixel, rasterization | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Lca, imposes, restrictions, closely, related, depth, DGS, render | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Gaussians, modified, color, will, sent, projection, then, generate, pixel, rasterization | p. 4 (3.2. Overview of UW-GS), p. 4 (3.3. Color Appearance Model), p. 6 (3.6. Loss Function) |
| Decision / output variable | geometry/map/query r; body terms: address, issue, novel, color, appearance, formation, aforementioned, issues | p. 4 (3.3. Color Appearance Model), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: However, underwater, scenes, Equation, suggests, LRec, color, calculated | p. 4 (3.4. Physical-based Density Control), p. 6 (3.6. Loss Function), p. 3 (3.1. Problem formulation), p. 3 (3.1. Problem formulation), p. 4 (3.4. Physical-based Density Control), p. 5 (3.4. Physical-based Density Control) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Physical-based Density Control), p. 3 (3.1. Problem formulation), p. 3 (3.1. Problem formulation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 2 (Figure/Table caption), p. 7 (5. Results and Discussion), p. 6 (4. Experiment Configuration) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Finally, given the scarcity of underwater datasets, we collected a new dataset featuring four expansive areas of shallow underwater scenes, each presenting unique challenges compared ...
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Moreover, moving objects such as fish and floating particles pose challenges to underwater 3D reconstruction.
- **p. 4 / 3.1. Problem formulation - extractive body cue:** In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a pixel-level mask, named ...
- **p. 1 / 1. Introduction - extractive body cue:** Unfortunately, the existing methods [26, 39] do not address this issue.

## What the Paper Changes

PDF body contribution framing (p. 4 (3.3. Color Appearance Model), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem formulation), p. 4 (3.3. Color Appearance Model)): To address this issue, we propose a novel approach for color appearance formation.

- **p. 1 / 1. Introduction - extractive body cue:** To address the aforementioned issues, we propose a new Gaussian Splatting (GS)-based method, UW-GS, specifically for underwater scenes.
- **p. 2 / 1. Introduction - extractive body cue:** We also incorporated pseudo-depth maps generated from DepthAnything [47], trained with more general scenes, to enhance the robustness of our method.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** The left panel of Figure 2 illustrates the workflow of our method.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. The diagram of our proposed UW-GS approach, combining a novel color appearance model, physical-based density control ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2. Overview of UW-GS), p. 4 (3.3. Color Appearance Model), p. 6 (3.6. Loss Function), p. 6 (3.6. Loss Function). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation), p. 1 (1. Introduction), interface p. 4 (3.2. Overview of UW-GS), p. 4 (3.3. Color Appearance Model), p. 6 (3.6. Loss Function), p. 6 (3.6. Loss Function), objective p. 4 (3.4. Physical-based Density Control), p. 6 (3.6. Loss Function), p. 3 (3.1. Problem formulation), p. 3 (3.1. Problem formulation), p. 4 (3.4. Physical-based Density Control), p. 5 (3.4. Physical-based Density Control).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
