# Problem - MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=efDNv5XvVo; PDF retrieval source: https://openreview.net/pdf/804e98743d0bf960af90c596755d72e4736d2c39.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In-the-wild photo collections often contain limited volumes of imagery and exhibit multiple appearances, e.g., taken at different times of day or seasons, posing significant challenges ...
- **p. 1 / Abstract - extractive PDF cue:** Although recent adaptations of Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) have improved in these areas, they tend to oversmooth and are prone ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present MS-GS, a novel framework designed with Multi-appearance capabilities in Sparse-view scenarios using 3DGS.
- **p. 1 / Abstract - extractive PDF cue:** To address the lack of support due to sparse initializations, our approach is built on the geometric priors elicited from monocular depth estimations.
- **p. 1 / Abstract - extractive PDF cue:** The key lies in extracting and utilizing local semantic regions with a Structure-from-Motion (SfM) points anchored algorithm for reliable alignment and geometry cues.
- **p. 2 / 1 Introduction - extractive PDF cue:** A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity.
- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators [18, 19, 20] that ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | A key challenge is that monocular depth estimation is often incorrect at relative depth between objects due to single-view ambiguity. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages, monocular, depths | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | point, cloud, back-projected, given, training, view, corresponding, rendered | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages, monocular, depths | p. 3 (1 Introduction), p. 4 (3 Method), p. 6 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: summary, main, contributions, introduce, Semantic, Depth, Alignment, leverages | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: minimized, unclear, whether, regions, without, sufficient, constraints, dsfm | p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators [18, 19, 20] that ...
- **p. 1 / 1 Introduction - extractive PDF cue:** High-quality scene reconstruction and novel view synthesis from images is a long-standing research problem with wide-ranging applications in AR/VR, 3D site modeling, autonomous driving, robotics, ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method)): In summary, the main contributions of our work are: • We introduce a Semantic Depth Alignment approach, which leverages monocular depths in local semantic regions to construct a dense point ...

- **p. 2 / 1 Introduction - extractive PDF cue:** 1, they synthesize overly smooth regions, while our method recovers fine details.
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we present MS-GS, which improves the robustness of 3DGS in dealing with unconstrained images when limited viewpoints and varying appearances exist, which ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To this end, we introduce an unbounded drone dataset that features multi-view appearance.
- **p. 4 / 3 Method - extractive PDF cue:** To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Specific techniques have to be developed to solve these limitations, which we leave as future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We identify that one of the limitations of 3DGS-based methods in sparse-view synthesis is the sparse point cloud ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 5 Limitations First, MS-GS is not designed for handling transient objects, which is especially difficult under sparse views ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Jointly, MS-GS offers a robust solution under challenges of limited viewpoints and varying appearances that naturally arise in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1 Introduction), p. 4 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 3 (1 Introduction), p. 4 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction), objective p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
