# Problem - LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=MaN2x3O2Rk&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** With the attention gained by camera-only 3D object detection in autonomous driving, methods based on Bird-EyeView (BEV) representation especially derived from the forward view transformation ...
- **p. 1 / Abstract - extractive PDF cue:** The BEV representation formulated by the frustum based on depth distribution prediction is ideal for learning the road structure and scene layout from multi-view images.
- **p. 1 / Abstract - extractive PDF cue:** However, to retain computational efficiency, the compressed BEV representation such as in resolution and axis is inevitably weak in retaining the individual geometric details, undermining ...
- **p. 1 / Abstract - extractive PDF cue:** With this in mind, to compensate for the missing details and utilize multi-view geometry constraints, we propose LSSInst, a two-stage object detector incorporating BEV and ...
- **p. 1 / Abstract - extractive PDF cue:** The proposed detector exploits fine-grained pixel-level features that can be flexibly integrated into existing LSS-based BEV networks.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.
- **p. 2 / 1. Introduction - extractive PDF cue:** However, this collaboration also poses challenges, as the most straightforward solution of naively sharing the bounding box proposal is intuitively and experimentally failed 1.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | BEV, Branch, Looking, around, scene-level, representation, multi-view, sequential, images, previous | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | instance, branch, focuses, fine-grained, sparse, feature, extraction, geometric | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: BEV, Branch, Looking, around, scene-level, representation, multi-view, sequential, images, previous | p. 4 (3. Methodology), p. 4 (3. Methodology), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, concluded, follows, LSSInst, two-stage, framework, improves | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Lastly, model, makes, final, prediction, updated, output, briefly | p. 4 (3. Methodology), p. 4 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 13 (Figure/Table caption), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.4. Noise Resistance for Practical Robustness) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, this collaboration also poses challenges, as the most straightforward solution of naively sharing the bounding box proposal is intuitively and experimentally failed 1.
- **p. 2 / 1. Introduction - extractive PDF cue:** On the nuScenes dataset, our LSSInst method demonstrates strong generalization ability.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 5 (3. Methodology)): Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with instance representations; ii) We proposed ...

- **p. 2 / 1. Introduction - extractive PDF cue:** With this in mind, we propose the instance adaptor module to establish semantic coherence between the scene and instances and an instance branch for detection.
- **p. 3 / 3. Methodology - extractive PDF cue:** The overview of our framework is shown in Fig.
- **p. 3 / 3. Methodology - extractive PDF cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive PDF cue:** Then we introduce five separated linear projections {Ej l3}2 j=1 ∈R3×C, {Ej l2}2 j=1 ∈R2×C and Eg ∈RC×C for comprehensive encoding, of which the former ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | We can observe that on the one hand, relying solely on the potential queries cannot play a major ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The noise resistance results for robustness. | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3. Methodology), p. 4 (3. Methodology), p. 2 (1. Introduction), p. 3 (3. Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3. Methodology), p. 4 (3. Methodology), p. 2 (1. Introduction), p. 3 (3. Methodology), objective p. 4 (3. Methodology), p. 4 (3. Methodology), p. 5 (3. Methodology), p. 6 (3. Methodology).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
