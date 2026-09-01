# Problem - G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction)): We argue that this limitation stems from how current VLMs acquire their physical world knowledge.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Vision-Language Models (VLMs) still lack robustness in spatial intelligence, demonstrating poor performance on spatial understanding and reasoning tasks.
- **p. 1 / Abstract - extractive PDF cue:** We attribute this gap to the absence of a visual geometry learning process capable of reconstructing 3D space from 2D images.
- **p. 1 / Abstract - extractive PDF cue:** We present G2VLM, a geometry grounded vision-language model that bridges two fundamental aspects of spatial intelligence: spatial 3D reconstruction and spatial understanding.
- **p. 1 / Abstract - extractive PDF cue:** G2VLM natively leverages learned 3D visual geometry features to directly predict 3D attributes and enhance spatial reasoning tasks via in-context learning and interleaved reasoning.
- **p. 1 / Abstract - extractive PDF cue:** Our unified design is highly scalable for spatial understanding: it trains on abundant multiview image and video data, while simultaneously leveraging the benefits of 3D ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We argue that this limitation stems from how current VLMs acquire their physical world knowledge.
- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We argue that this limitation stems from how current VLMs acquire their physical world knowledge. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (1) where Ti ∈SE(3) ⊂R4×4 is the camera pose, Xi ∈ RH×W ×3 is the associated pixel-aligned 3D point map represented in ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | where, camera, pose, associated, pixel-aligned, point, represented, coordinate, system, corresponding | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Except, incorporating, priors, specific, D-VLMs, general, VLMs, simply | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: where, camera, pose, associated, pixel-aligned, point, represented, coordinate, system, corresponding | p. 4 (3.1. Model Architecture), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, introduce, G2VLM, first, unified, model | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: explore, three, distinct, joint-training, strategies, where, semantic, perception | p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive PDF cue:** Then turn right, go straight pass the boxes to get to the black monitor.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3. Unified Spatial Vision-Language Model), p. 4 (3.1. Model Architecture)): Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in a single vision-language model.

- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive PDF cue:** We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and ...
- **p. 4 / 3. Unified Spatial Vision-Language Model - extractive PDF cue:** We introduce G2VLM, a unified geometry-grounded VLM that integrates spatial 3D reconstruction and spatial understanding.
- **p. 4 / 3.1. Model Architecture - extractive PDF cue:** Our model's input is a sequence (Ii)N i=1 of N RGB images Ii ∈R3×H×W , we present the detailed design for each expert as follows.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We leave the scaling of our model to future work, as this is a promising direction to unlock ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.1. Model Architecture), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Model Architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), interface p. 4 (3.1. Model Architecture), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Model Architecture), objective p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
