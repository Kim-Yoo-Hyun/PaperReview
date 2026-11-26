# ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://referit3d.github.io/.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / ECCV
- Authors: Panos Achlioptas, Ahmed Abdelreheem, Fei Xia, Mohamed Elhoseiny, Leonidas Guibas
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D visual grounding, language, scene, point cloud
- Official paper: https://referit3d.github.io/
- Full-text retrieval: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf
- Code/Project: https://github.com/referit3d/referit3d
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf)

## Why This Paper Is Here

ReferIt3D는 한 장면에 같은 세부 범주의 물체가 여럿 있을 때 언어 설명이 가리키는 인스턴스를 골라내는 문제를 다룬다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=1) · [PDF 2쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=2)

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

- 공간 관계 템플릿으로 만든 Sr3D와 두 사람이 물체를 설명하고 맞히는 게임으로 수집한 Nr3D를 제공하고 사람의 식별 정확도를 측정했다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=5) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=7) · [PDF 8쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=8)
- 점군에서 각 물체를 인코딩하고 물체 사이의 관계를 언어와 결합하는 모델로 방해 물체의 수와 시점 의존성이 식별에 미치는 영향을 평가했다. [PDF 10쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=12)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (body section not recovered), p. 1 (1 Introduction), p. 3 (1 Introduction)이다.

## 검색 태그 근거

ReferIt3D의 모델은 색이 붙은 후보 물체 점군과 설명을 받아 같은 범주의 인스턴스 중 하나를 고른다. 실내 스캔으로 만든 Nr3D와 Sr3D를 사용해 구별 정확도를 검사했다. [원문 3쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=3) · [원문 11쪽](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf#page=11)
