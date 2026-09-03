# ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://referit3d.github.io/.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D visual grounding, language, scene
- Official paper: https://referit3d.github.io/
- Full-text retrieval: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf
- Code/Project: https://github.com/referit3d/referit3d
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied question answering [21], visual- and language-based navigation ...를 문제로 두고, For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** The progress on connecting language and vision in the past decade has rekindled interest in tasks like visual question answering (e.g., [12,54]), image captioning (e.g., ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent works have enhanced the accessibility of visual content through language via grounding (e.g., [49,48]), showing strong results in locating linguistically described visual elements in ...
- **p. 1 / 1 Introduction - extractive body cue:** However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view ...
- **p. 1 / 1 Introduction - extractive body cue:** Even in embodied AI most works (e.g., embodied QA [21], or embodied visual recognition [69]), fine-grained 3D object identification is not explicitly modeled.
- **p. 1 / 1 Introduction - extractive body cue:** Fine-grained 3D understanding however
- **p. 2 / 1 Introduction - extractive body cue:** Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied ...
- **p. 2 / 1 Introduction - extractive body cue:** The use of a specific contrasting context inside a scene (as delineated by the bounding boxes surrounding all and only those objects of the same ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.
- **p. 3 / 1 Introduction - extractive body cue:** Fine-Grained ReferIt3D task: We introduce the task of language-based identification of specific 3D object instances, where fine-grained object-centric and multi-object understanding is necessary for its ...
- **p. 2 / 1 Introduction - extractive body cue:** This flexibility enables us also to bypass camera view dependency (e.g., having access to parts of a scene occluded by a fixed camera) when we ...
- **p. 1 / body section not recovered - extractive body cue:** Our key technical contribution is designing an approach for combining linguistic and geometric information (in the form of 3D point clouds) and creating multi-modal (3D) ...
- **p. 1 / 1 Introduction - extractive body cue:** However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view ...
- **p. 1 / body section not recovered - extractive body cue:** We also show that architectures which promote object-to-object communication via graph neural networks outperform less context-aware alternatives, and that fine-grained object classification is a bottleneck ...
- **p. 1 / 1 Introduction - extractive body cue:** Even in embodied AI most works (e.g., embodied QA [21], or embodied visual recognition [69]), fine-grained 3D object identification is not explicitly modeled.
- **p. 2 / 1 Introduction - extractive body cue:** Despite this, developing datasets and methods with characteristics that enable machine learning models to perform well on this 3D reference task is far from straightforward; ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied question answering [21], visual- and language-based navigation ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | Solving, reference, problem, directly, space, without, camera, view, dependency, benefit, many, downstream | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view of our 3D reality. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | The progress on connecting language and vision in the past decade has rekindled interest in tasks like visual question answering (e.g., [12,54]), image captioning (e.g., [28,63,68,41,6]), and sentence-to-image similarity (e.g., [28,31]). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.
- **p. 3 / 1 Introduction - extractive body cue:** Fine-Grained ReferIt3D task: We introduce the task of language-based identification of specific 3D object instances, where fine-grained object-centric and multi-object understanding is necessary for its ...
- **p. 2 / 1 Introduction - extractive body cue:** This flexibility enables us also to bypass camera view dependency (e.g., having access to parts of a scene occluded by a fixed camera) when we ...
- **p. 1 / body section not recovered - extractive body cue:** Our key technical contribution is designing an approach for combining linguistic and geometric information (in the form of 3D point clouds) and creating multi-modal (3D) ...
- **p. 1 / 1 Introduction - extractive body cue:** However, most of these works focus on developing better models that connect vision to language in images, which express after all only a 2D view ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2. ReferIt3DNet performance on Nr3D with/out Sr3D. The first row contains the achieved accuracy on the Nr3D testing data for a listener trained solely ...
- **p. 12 / VI SD - extractive body cue:** We observe the following main trends5: i) using the visual and linguistic auxiliary classification losses improves performance; ii) Simplified language (Sr3D) makes identification easier; iii) ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4. ScanRefer performance with/out Sr3D. MeanIoU improvements when combining Sr3D data with ScanRefer's data during training.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 12 (Figure/Table caption), p. 12 (VI SD) |
| Embodiment/environment | This demonstrates the contribution of adding a synthetically generated dataset to a human one. | hardware/simulator version and reset protocol | p. 13 (VI SD), p. 13 (VI SD) |
| Dataset/benchmark | Scene-Discoverable (SD): does the utterance explicitly refer to the target's object class (or a synonym), hence permitting object-identification among all objects of the scene? | role, split, size and leakage | p. 13 (VI SD), p. 13 (VI SD), p. 11 (VI SD), p. 12 (VI SD) |
| Metric | 5 Experiments and Analysis We explore different listening architectures 4 and report the listening accuracy; each test utterance receives a binary score (1 if the correct object is predicted as target and ... | definition, denominator, direction and uncertainty | p. 11 (VI SD), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Baseline/ablation | Decoupled approach: This is a baseline listener consisting of a text classifier and an (FG) object classifier that are trained separately. | fair input/data/compute/action matching | p. 11 (VI SD), p. 11 (VI SD), p. 12 (VI SD) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 6 Conclusion - extractive body cue:** Success cases are in the top four images and Failure in the bottom two.
- **p. 13 / VI SD - extractive body cue:** Finally, the last row shows two challenging failure cases of our model.
- **p. 13 / VI SD - extractive body cue:** This does not come as a surprise, since the network has naturally more work to do to comprehend nuances related to viewing the scene w.r.t. ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Solving such a reference problem directly in 3D space - i.e., without a camera view dependency - can benefit many downstream robotics applications, including embodied question answering [21], visual- and language-based navigation ...를 문제로 두고, For Sr3D we propose a simple but effective methodology for building template-based and spatially-oriented object referential language in 3D scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (body section not recovered), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
