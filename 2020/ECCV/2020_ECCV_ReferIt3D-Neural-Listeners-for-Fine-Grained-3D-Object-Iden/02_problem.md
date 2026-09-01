# Problem - ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://referit3d.github.io/; PDF retrieval source: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied question answering [21], visual- and ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** The progress on connecting language and vision in the past decade has rekindled interest in tasks like visual question answering (e.g., [12,54]), image captioning (e.g., ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Recent works have enhanced the accessibility of visual content through language via grounding (e.g., [49,48]), showing strong results in locating linguistically described visual elements in ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Even in embodied AI most works (e.g., embodied QA [21], or embodied visual recognition [69]), fine-grained 3D object identification is not explicitly modeled.
- **p. 1 / 1 Introduction - extractive PDF cue:** Fine-grained 3D understanding however
- **p. 2 / 1 Introduction - extractive PDF cue:** Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The use of a specific contrasting context inside a scene (as delineated by the bounding boxes surrounding all and only those objects of the same ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Solving, reference, problem, directly, space, without, camera, view, dependency, benefit | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Recent, works, have, enhanced, accessibility, visual, content, through | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Solving, reference, problem, directly, space, without, camera, view, dependency, benefit | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: Sr3D, simple, effective, methodology, building, template-based, spatially-oriented, object | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: progress, connecting, language, vision, past, decade, rekindled, interest | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 11 (VI SD), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** The use of a specific contrasting context inside a scene (as delineated by the bounding boxes surrounding all and only those objects of the same ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (2 King Abdullah University of Science and Technology), p. 1 (1 Introduction)): For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.

- **p. 3 / 1 Introduction - extractive PDF cue:** Fine-Grained ReferIt3D task: We introduce the task of language-based identification of specific 3D object instances, where fine-grained object-centric and multi-object understanding is necessary for its ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This flexibility enables us also to bypass camera view dependency (e.g., having access to parts of a scene occluded by a fixed camera) when we ...
- **p. 1 / 2 King Abdullah University of Science and Technology - extractive PDF cue:** Our key technical contribution is designing an approach for combining linguistic and geometric information (in the form of 3D point clouds) and creating multi-modal (3D) ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | Success cases are in the top four images and Failure in the bottom two. | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Finally, the last row shows two challenging failure cases of our model. | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | This does not come as a surprise, since the network has naturally more work to do to comprehend ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
