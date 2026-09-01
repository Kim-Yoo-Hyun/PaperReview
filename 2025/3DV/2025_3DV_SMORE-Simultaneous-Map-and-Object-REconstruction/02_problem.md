# Problem - SMORE: Simultaneous Map and Object REconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=1NhnG9BvQB&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction)): However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed by the existing research.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present a method for dynamic surface reconstruction of large-scale urban scenes from LiDAR.
- **p. 1 / Abstract - extractive PDF cue:** Depth-based reconstructions tend to focus on small-scale objects or largescale SLAM reconstructions that treat moving objects as outliers.
- **p. 1 / Abstract - extractive PDF cue:** We take a holistic perspective and optimize a compositional model of a dynamic scene that decomposes the world into rigidly-moving objects and the background.
- **p. 1 / Abstract - extractive PDF cue:** To achieve this, we take inspiration from recent novel view synthesis methods and frame the reconstruction problem as a global optimization over neural surfaces, ego ...
- **p. 1 / Abstract - extractive PDF cue:** In contrast to view synthesis methods, which typically minimize 2D errors with gradient descent, we minimize a 3D point-to-surface error by coordinate descent, which we ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed ...
- **p. 1 / 1. Introduction - extractive PDF cue:** This problem has been widely studied in the context of handheld RGB-D sensors capturing humanscale scenes [23, 29, 44, 48].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | In *Equal Contribution the context of depth sensors, this problem is posed as dynamic surface reconstruction, where the goal is to produce ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Equal, Contribution, context, depth, sensors, problem, posed, dynamic, surface, reconstruction | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Since, compositional, model, scene, will, need, coordinate, frame | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Equal, Contribution, context, depth, sensors, problem, posed, dynamic, surface, reconstruction | p. 1 (1. Introduction), p. 3 (3. Problem Statement), p. 3 (3. Problem Statement) |
| Decision / output variable | geometry/map/query r; body terms: example, depth, maps, produced, Fig, introduce, global, optimization | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Decomposition) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: following, sections, derive, appropriate, surface, pose, optimization, steps | p. 4 (4. Objective), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (6. Qualitative Results), p. 8 (Figure/Table caption), p. 6 (5.1. Lidar Novel View Synthesis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** This problem has been widely studied in the context of handheld RGB-D sensors capturing humanscale scenes [23, 29, 44, 48].
- **p. 2 / 1. Introduction - extractive PDF cue:** Our main contributions are (1) posing the classic dynamic surface reconstruction problem in the context of
- **p. 2 / 1. Introduction - extractive PDF cue:** Labeling in-the-wild data is extremely costly, and as a result, many autonomous driving tasks rely on reprocessing existing data of varying quality.
- **p. 3 / 1. Introduction - extractive PDF cue:** LiDAR-based urban scenes, (2) combining insights from actor decomposition of radiance fields and continuous-time SLAM to produce high-quality reconstructions that reduce error by 10X over ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Decomposition), p. 1 (1. Introduction), p. 4 (4. Objective)): An example of the depth maps produced by our method is shown in Fig.

- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce a global optimization that refines both ego and object poses so as to minimize a scan-to-surface reconstruction error, dramatically improving results (right).
- **p. 4 / 4.1. Decomposition - extractive PDF cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In *Equal Contribution the context of depth sensors, this problem is posed as dynamic surface reconstruction, where the goal is to produce a time-varying surface ...
- **p. 4 / 4. Objective - extractive PDF cue:** Our method aims to find the surfaces and object motions that best explain the LiDAR measurements.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For testing, however, the reference implementation does not support optimizing new poses that were not present at train ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 3 (3. Problem Statement), p. 3 (3. Problem Statement), p. 5 (4.4. What is a LiDAR sweep?). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), interface p. 1 (1. Introduction), p. 3 (3. Problem Statement), p. 3 (3. Problem Statement), p. 5 (4.4. What is a LiDAR sweep?), objective p. 4 (4. Objective), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
