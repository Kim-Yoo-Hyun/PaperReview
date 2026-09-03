# Problem - LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2406.08009v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): To address this limitation, some works [11], [12] have proposed instance-oriented open-vocabulary mapping methods.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In recent years, there has been a surge of interest in open-vocabulary 3D scene reconstruction facilitated by visual language models (VLMs), which showcase remarkable capabilities ...
- **p. 1 / Abstract - extractive body cue:** However, existing methods face some limitations: they either focus on learning point-wise features, resulting in blurry semantic understanding, or solely tackle object-level reconstruction, thereby overlooking ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce OpenObj, an innovative approach to build openvocabulary object-level Neural Radiance Fields (NeRF) with fine-grained understanding.
- **p. 1 / Abstract - extractive body cue:** In essence, OpenObj establishes a robust framework for efficient and watertight scene modeling and comprehension at the object-level.
- **p. 1 / Abstract - extractive body cue:** Moreover, we incorporate part-level features into the neural fields, enabling a nuanced representation of object interiors.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this limitation, some works [11], [12] have proposed instance-oriented open-vocabulary mapping methods.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these semantics are limited to a closed-set of labels predefined during the training phase [3], making it challenging to generalize to new scenes or ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address this limitation, some works [11], [12] have proposed instance-oriented open-vocabulary mapping methods. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Based on this, we can render the occupancy, depth, color, and feature as: ˆO(r[u,v]) = X m Tm, ˆD(r[u,v]) = X m ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | render, occupancy, depth, color, feature, Tmdm, Tmcm, Tmfm, Loss, Function | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Finally, NeRF, Rendering, Training, module, vectorizes, NeRFs, objects | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: render, occupancy, depth, color, feature, Tmdm, Tmcm, Tmfm, Loss, Function | p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, summarized, follows, present, OpenObj, open-vocabulary, object-level | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: overall, loss, function, obtained, summing, losses, objects, depth | p. 5 (III. OPENOBJ), p. 5 (III. OPENOBJ) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (2) Are OpenObj's open-vocabulary object-level and part), p. 4 (III. OPENOBJ), p. 3 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these semantics are limited to a closed-set of labels predefined during the training phase [3], making it challenging to generalize to new scenes or ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In addressing this challenge, we are inspired by how humans cognitively process their environment.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 4 (III. OPENOBJ)): In summary, Our contributions are summarized as follows: • We present OpenObj, the open-vocabulary object-level neural radiance fields with fine-grained understanding, supporting downstream tasks at multiple scales. • We propose ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** Following this inspiration, we proposed OpenObj, an innovative approach to build open-vocabulary objectlevel neural radiance fields with fine-grained understanding.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce OpenObj, an innovative approach to build openvocabulary object-level Neural Radiance Fields (NeRF) with fine-grained understanding.
- **p. 4 / III. OPENOBJ - extractive body cue:** To address this problem, we propose considering all frames together and devising a two-stage approach as shown in Fig.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | This approach helps to mitigate the effects of outliers caused by poor observation viewpoints or model failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: We introduce OpenObj, a framework of open-vocabulary object-level neural radiance fields with fine-grained understanding. OpenObj facilitates ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Additionally, we apply another method to compensate for the limitations of VLM features f clip t,i in semantic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Since this method does not distinguish between the sources of the masks, it can effectively correlate masks across ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 4 (III. OPENOBJ). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 5 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 3 (III. OPENOBJ), p. 4 (III. OPENOBJ), objective p. 5 (III. OPENOBJ), p. 5 (III. OPENOBJ).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
