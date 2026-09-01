# Problem - EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): To bridge this gap, we formulate a new embodied 3D occupancy prediction task to evaluate the ability to progressively explore an unknown scene using only visual inputs.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** 3D occupancy prediction provides a comprehensive description of the surrounding scenes and has become an essential task for 3D perception.
- **p. 1 / Abstract - extractive PDF cue:** Most existing methods focus on offline perception from one or a few views and cannot be applied to embodied agents that demand to gradually perceive ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we formulate an embodied 3D occupancy prediction task to target this practical scenario and propose a Gaussian-based EmbodiedOcc framework to accomplish it.
- **p. 1 / Abstract - extractive PDF cue:** We initialize the global scene with uniform 3D semantic Gaussians and progressively update local regions observed by the embodied agent.
- **p. 1 / Abstract - extractive PDF cue:** For each update, we extract semantic and structural features from the observed image and efficiently incorporate them via deformable crossattention to refine the regional Gaussians.
- **p. 2 / 1. Introduction - extractive PDF cue:** To bridge this gap, we formulate a new embodied 3D occupancy prediction task to evaluate the ability to progressively explore an unknown scene using only ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To bridge this gap, we formulate a new embodied 3D occupancy prediction task to evaluate the ability to progressively explore an unknown ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Depth Aware Predicted Depth Map … … Input T-1 Input T … … … … Gaussian Memory T Gaussian Memory T-1 Occupancy ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Depth, Aware, Predicted, Map, Input, T-1, Gaussian, Memory, Occupancy, Load | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Recent, methods, begin, consider, endowing, models, same, competence | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Depth, Aware, Predicted, Map, Input, T-1, Gaussian, Memory, Occupancy, Load | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction) |
| Decision / output variable | geometry/map/query r; body terms: Specifically, structure-aware, local, refinement, module, update, relevant, Gaussians | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Embodied 3D Occupancy Prediction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Then, detach, updated, Gaussians, back, memory, Different, subscripts | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.4. Experimental Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 1 (1. Introduction)): Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum.

- **p. 2 / 1. Introduction - extractive PDF cue:** We propose an EmbodiedOcc framework based on Gaussian memories to accomplish this task, considering the explicity and structural nature of 3D Gaussians.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive PDF cue:** Motivated by this, we propose an embodied 3D occupancy prediction task in this paper.
- **p. 1 / 1. Introduction - extractive PDF cue:** With the rapid development of embodied intelligence and active agents [14, 17, 32], 3D scene perception [30, 34, 41, 42] has become a crucial task ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Due to space limitations, we will use a more diverse set of samples to further show the visual ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Besides, we replaced DepthAnything-V2 with IndoorDepth [6] in the last row to prove that our depth-aware branch does ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (1. Introduction), objective p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
