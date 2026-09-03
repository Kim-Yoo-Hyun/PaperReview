# Problem - Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p034.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p034.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION)): Estimating geometry through contact-rich interactions is not a trivial problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce Vysies, a vision-and-physies frame- ‘work for a robot to build an expressive geometry and dynamics model of a single rigid body, using a ...
- **p. 1 / Abstract - extractive body cue:** While the computer vision comhas built powerful visual 3D perception algorithms, cat tered environments with heavy occlusions can limit the visibility of objects of interest.
- **p. 1 / Abstract - extractive body cue:** However, observed motion of partially occluded objects can imply physical interactions took place, sueh as contact with a robot or the environment.
- **p. 1 / Abstract - extractive body cue:** These inferred contacts can supplement the visible geometry with "physible geomet which best explains the observed object motion through physics. ‘Vysies uses a vision-based tracking ...
- **p. 1 / Abstract - extractive body cue:** into optimizing a signed distance object shape.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Estimating geometry through contact-rich interactions is not a trivial problem.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** While some might be recognized from an existing database, others will require physical interaction to be newly understood on the spot.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Estimating geometry through contact-rich interactions is not a trivial problem. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | portions of its geometry, and observations of the object's state evolution can inject more geometric information when contact, | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | portions, geometry, observations, object, state, evolution, inject, more, geometric, information | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Referring, labeled, arrows, Figure, obtain, object, trajectory, initial | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: portions, geometry, observations, object, state, evolution, inject, more, geometric, information | p. 1 (1. INTRODUCTION), p. 2 (A. Vision-Based Geometry Reconstruction and Completion), p. 4 (IV. APPROACH) |
| Decision / output variable | geometry/map/query r; body terms: Fusing, vision, contact, rich, physics, recovers, occluded, geometry | p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: While, avoids, problematic, gradients, contactrch, scenarios, gradient-free, search | p. 3 (C. Simultaneous Tracking and Shape Reconstruction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (C. Simultaneous Tracking and Shape Reconstruction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. INTRODUCTION - extractive body cue:** While some might be recognized from an existing database, others will require physical interaction to be newly understood on the spot.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH), p. 8 (A. Geometry Reconstruction), p. 8 (200.0 BundlesDF)): Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction,

- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 8 / 200.0 BundlesDF - extractive body cue:** Our method recovers the occluded geometry through physics-based reasoning over the observed trajectories, substantially and consistently improving the geometric accuracy in both metrics.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. INTRODUCTION), p. 2 (A. Vision-Based Geometry Reconstruction and Completion), p. 4 (IV. APPROACH), p. 2 (A. Vision-Based Geometry Reconstruction and Completion). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), interface p. 1 (1. INTRODUCTION), p. 2 (A. Vision-Based Geometry Reconstruction and Completion), p. 4 (IV. APPROACH), p. 2 (A. Vision-Based Geometry Reconstruction and Completion), objective p. 3 (C. Simultaneous Tracking and Shape Reconstruction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Estimating geometry through contact-rich interactions is not a trivial problem. (p. 1, 1. INTRODUCTION).
- **Formulation-changing contribution:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction, (p. 1, 1. INTRODUCTION).
- **Assumption/failure evidence:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory. (p. 6, V. EXPERIMENTAL SETUP).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
