# Problem - HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.14147; PDF retrieval source: https://arxiv.org/pdf/2501.14147. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for teams of heterogeneous robots that ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting offers expressive scene reconstruction and can model a broad range of visual, geometric, and semantic information.
- **p. 1 / Abstract - extractive body cue:** However, efficient real-time map reconstruction with data streamed from multiple robots and devices remains a challenge.
- **p. 1 / Abstract - extractive body cue:** To that end, we propose HAMMER, a server-based multi-robot Gaussian Splatting method that leverages ROS communication infrastructure to generate 3D, metric-semantic maps from asynchronous robot ...
- **p. 1 / Abstract - extractive body cue:** HAMMER consists of (i) a one-time frame alignment module that transforms local SLAM poses and image data into a global frame and requires no prior ...
- **p. 1 / Abstract - extractive body cue:** HAMMER handles mixed perception modes, adjusts automatically for variations in image pre-processing among different devices, and distills CLIP semantic codes into the 3D scene for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Alternatively, 3DGS is a promising representation for multi-robot mapping because of its scalability to large environments [8], modeling fidelity, and generalization to a broad range ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | During runtime, HAMMER rejects alignments where the localized SfM fails to estimate poses for all 2W input images or alignments that have ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | During, runtime, HAMMER, rejects, alignments, where, localized, SfM, fails, estimate | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Importantly, process, treats, onboard, localization, algorithms, black-boxes, only | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: During, runtime, HAMMER, rejects, alignments, where, localized, SfM, fails, estimate | p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Decision / output variable | geometry/map/query r; body terms: server-based, architecture, allows, existing, robot, edge, device, hardware | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Equation, optimizes, scaling, rotation, translation, between, frames, small | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Alternatively, 3DGS is a promising representation for multi-robot mapping because of its scalability to large environments [8], modeling fidelity, and generalization to a broad range ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Computing requirements for 3DGS training are currently beyond the on-board compute capabilities of most robots and wearables.
- **p. 2 / I. INTRODUCTION - extractive body cue:** HAMMER is designed to generalize to a wide range of robots and devices, combining the advantages of each device into a single map.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** HAMMER enables a server communicating with a team of robots to construct a joint 3DGS map of an unknown environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** A shared map enables these robots to have comprehensive spatial awareness compared to their own local maps.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | 3) Pose Refinement: Although the alignment module produces robust estimates of the local-to-world transforms, it cannot account for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), objective p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Multi-robot mapping is useful for rapidly exploring new environments, but when combined with traditional 3D reconstruction methods, can be difficult to scale efficiently, especially for teams of heterogeneous robots that ... (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. (p. 6, IV. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
