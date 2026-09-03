# Problem - Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ycPVp0577R; PDF retrieval source: https://arxiv.org/pdf/2503.22204.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot be directly applied to dynamic scenes.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary querying in 3D space is crucial for enabling more intelligent perception in applications such as robotics, autonomous systems, and augmented reality.
- **p. 1 / Abstract - extractive body cue:** However, most existing methods rely on 2D pixel-level parsing, leading to multi-view inconsistencies and poor 3D object retrieval.
- **p. 1 / Abstract - extractive body cue:** Moreover, they are limited to static scenes and struggle with dynamic scenes due to the complexities of motion modeling.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Segment then Splat, a 3D-aware open vocabulary segmentation approach for both static and dynamic scenes based on Gaussian Splatting.
- **p. 1 / Abstract - extractive body cue:** Segment then Splat reverses the long established approach of "segmentation after reconstruction" by dividing Gaussians into distinct object sets before reconstruction.
- **p. 2 / 1 Introduction - extractive body cue:** However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot be directly applied ...
- **p. 1 / 1 Introduction - extractive body cue:** 2) Failure to capture true 3D object information, complicating 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these approaches require a predefined number of objects for clustering [13] or are limited to foreground segmentation [14], and also cannot ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | "Chopsticks" Initialized Objectspecific Gaussians Reconstruction Rasterize Object Query Result Trained Objectspecific Gaussians "Chopsticks" Gaussians CLIP Rasterize Rendered Image & 2D Feature Map ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Chopsticks, Initialized, Objectspecific, Gaussians, Reconstruction, Rasterize, Object, Query, Result, Trained | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Robust, Object, Tracking, Given, input, images, goal, extract | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Chopsticks, Initialized, Objectspecific, Gaussians, Reconstruction, Rasterize, Object, Query, Result, Trained | p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, include, Segment, then, Splat, novel, paradigm | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Given, input, text, prompt, perform, open, vocabulary, query | p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 6 (3 Method), p. 4 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (4 Experiments), p. 2 (Figure/Table caption), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** 2) Failure to capture true 3D object information, complicating 39th Conference on Neural Information Processing Systems (NeurIPS 2025).
- **p. 1 / 1 Introduction - extractive body cue:** While 3DGS has demonstrated remarkable performance in scene reconstruction and novel view synthesis, it lacks inherent semantic understandings, limiting its applicability in tasks that require ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike existing methods that adopt a "splat then segment" approach, our method reverses the process by first initializing each object with a specific set of ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method)): In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction.

- **p. 2 / 1 Introduction - extractive body cue:** This enables unified static/dynamic open-vocabulary segmentation, eliminates auxiliary language fields, and significantly reduces training complexity. • Our framework features a robust object tracking module that ...
- **p. 4 / 3 Method - extractive body cue:** We introduce Segment then Splat, a unified approach for 3D open-vocabulary segmentation based on Gaussian Splatting, as illustrated in Fig.
- **p. 5 / 3 Method - extractive body cue:** Specifically, we introduce an additional object-level loss term, 5
- **p. 5 / 3 Method - extractive body cue:** To capture newly appearing objects, we introduce a detection mechanism at fixed intervals of ∆t.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | However, this minor failure does not affect the final reconstruction, as sufficient information is retained from other views. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Moreover, because DGD does not directly supervise the language embeddings of each Gaussian, Gaussians located far apart may ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2: Demonstration of Segment then Splat pipeline. We first extracts multi-view masks for each object through a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction), objective p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
