# Problem - Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5197_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05197.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (X. Peng et al), p. 2 (X. Peng et al), p. 3 (X. Peng et al)): In this way, the detection model fails to detect objects not belonging to the training object classes.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** As a basic function of machine perception, object detection has attracted much attention within computer vision communities.
- **p. 1 / 1 Introduction - extractive body cue:** The traditional training pipeline for the detection model relies on elaborately labeled data, resulting in a limited number of classes that can be collected and ...
- **p. 1 / 1 Introduction - extractive body cue:** In this way, the detection model fails to detect objects not belonging to the training object classes.
- **p. 2 / X. Peng et al - extractive body cue:** Compared to open-vocabulary detection for 2D RGB images, lidar-based open-vocabulary detection suffers from more difficulties.
- **p. 2 / X. Peng et al - extractive body cue:** However, the dominant paradigm of current state-of-the-art lidar-based OVD methods only focuses on object-level features and neglects the importance of
- **p. 3 / X. Peng et al - extractive body cue:** 1a, the current paradigm determines the class of an object by comparing the object-level features and the text features of class names.
- **p. 3 / X. Peng et al - extractive body cue:** In summary, our contributions are as follows. - We propose a lidar-based open-vocabulary detection method, GLIS, which is the first work to explore the interactions ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this way, the detection model fails to detect objects not belonging to the training object classes. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Due to noises within the point cloud, the detector may confuse foreground objects with the background and outputs false object proposals. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Due, noises, within, point, cloud, detector, confuse, foreground, objects, background | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | However, dominant, paradigm, current, state-of-the-art, lidar-based, OVD, methods | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Due, noises, within, point, cloud, detector, confuse, foreground, objects, background | p. 7 (X. Peng et al), p. 3 (X. Peng et al), p. 2 (X. Peng et al) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, follows, lidar-based, open-vocabulary, detection, GLIS, first | p. 3 (X. Peng et al), p. 1 (body section not recovered), p. 1 (body section not recovered) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Firstly, point, clouds, have, lower, resolutions, compared, RGB | p. 2 (X. Peng et al), p. 6 (X. Peng et al), p. 8 (X. Peng et al) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (X. Peng et al), p. 6 (X. Peng et al), p. 8 (X. Peng et al) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 11 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / X. Peng et al - extractive body cue:** Compared to open-vocabulary detection for 2D RGB images, lidar-based open-vocabulary detection suffers from more difficulties.
- **p. 2 / X. Peng et al - extractive body cue:** However, the dominant paradigm of current state-of-the-art lidar-based OVD methods only focuses on object-level features and neglects the importance of
- **p. 3 / X. Peng et al - extractive body cue:** 1a, the current paradigm determines the class of an object by comparing the object-level features and the text features of class names.

## What the Paper Changes

PDF body contribution framing (p. 3 (X. Peng et al), p. 1 (body section not recovered), p. 1 (body section not recovered), p. 2 (X. Peng et al), p. 3 (X. Peng et al)): In summary, our contributions are as follows. - We propose a lidar-based open-vocabulary detection method, GLIS, which is the first work to explore the interactions of the global scene-level information ...

- **p. 1 / body section not recovered - extractive body cue:** Extensive experiments on ScanNetV2 and SUN RGB-D demonstrate the superiority of our methods.
- **p. 1 / body section not recovered - extractive body cue:** In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result ...
- **p. 2 / X. Peng et al - extractive body cue:** (b) In contrast, we propose a Global-Local Collaborative Inference Scheme (GLIS) for 3D OVD, considering both the scene-level/global information and the object-level/local information.
- **p. 3 / X. Peng et al - extractive body cue:** Superior performance on ScanNetV2 [7] and SUN RGB-D [38] demonstrates the effectiveness of our methods.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | These limitations could inspire our future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | The limitation of GLIS exists due to the noises within the point cloud and the false pseudo labels ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | This proves that BAOL can overcome the disturbance of noises in point clouds, resulting in better localization for ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 7 (X. Peng et al), p. 3 (X. Peng et al), p. 2 (X. Peng et al), p. 2 (X. Peng et al). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (X. Peng et al), p. 2 (X. Peng et al), p. 3 (X. Peng et al), interface p. 7 (X. Peng et al), p. 3 (X. Peng et al), p. 2 (X. Peng et al), p. 2 (X. Peng et al), objective p. 2 (X. Peng et al), p. 6 (X. Peng et al), p. 8 (X. Peng et al).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
