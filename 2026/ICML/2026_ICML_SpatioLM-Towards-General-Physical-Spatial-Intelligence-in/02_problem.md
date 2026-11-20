# Problem - SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/virtual/2026/oral/71166; PDF retrieval source: https://openreview.net/pdf/04fc204cb3233c6ac9f5867e72c861a9e835bc65.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): The aforementioned analysis highlights an unresolved core challenge: how to enhance the spatial intelligence of VLMs without extra 3D prior inputs or third-party spatial encoders, while preserving their general-purpose capabilities.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning.
- **p. 1 / Abstract - extractive body cue:** Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs' general-purpose capabilities after spatial fine-tuning.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a parameter-efficient Spatio-vision Language Models (SpatioLM), that enhances spa
- **p. 1 / Abstract - extractive body cue:** Concretely, we design a plug-and-play and non-invasive spatiovision module that elicits the spatial knowledge inherent in VLMs.
- **p. 1 / Abstract - extractive body cue:** Furthermore, we innovatively leverage pseudo depth and camera information as supervision to guide the model in learning physically coherent representations.
- **p. 2 / 1. Introduction - extractive body cue:** The aforementioned analysis highlights an unresolved core challenge: how to enhance the spatial intelligence of VLMs without extra 3D prior inputs or third-party spatial encoders, ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle this core challenge, this work proposes a Spatiovision Language Model (SpatioLM), whose overall architecture is illustrated in Fig.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The aforementioned analysis highlights an unresolved core challenge: how to enhance the spatial intelligence of VLMs without extra 3D prior inputs or ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 원문 대조: 모델 입력은 visual sequence X^v와 textual instruction X^t의 쌍이다. X^v는 T×H×W×3 RGB 입력이며 T=1은 image, T>1은 video를 뜻한다. Depth와 camera ray map은 뒤의 학습 supervision으로 구분된다. ([PDF p. 3](https://arxiv.org/pdf/2608.01899#page=3), §3.1 Problem definition and notation, Eq. (1)) | RGB image/video + text | Depth/ray map은 supervision; Eq. (1) 입력과 구분 |
| State / latent | input, sequence, model, defined, following, tuple, format, where, denotes, visual | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | main, contributions, summarized, follows, SpatioLM, purely, vision-language, framework | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: input, sequence, model, defined, following, tuple, format, where, denotes, visual | p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: main, contributions, summarized, follows, SpatioLM, purely, vision-language, framework | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: overall, training, objective, weighted, language, modeling, loss, mixed | p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design), p. 6 (3.4. Unified Task Formulation), p. 6 (3.3. Loss Design) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Loss Design), p. 6 (3.4. Unified Task Formulation), p. 6 (3.4. Unified Task Formulation) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4.2.2. SPATIAL UNDERSTANDING), p. 7 (4.2.1. SPATIAL PERCEPTION), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To tackle this core challenge, this work proposes a Spatiovision Language Model (SpatioLM), whose overall architecture is illustrated in Fig.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 2 (1. Introduction), p. 4 (3.2. Spatio-Vision Module)): Our main contributions are summarized as follows: • We propose SpatioLM, a purely 2D vision-language framework that elicits implicit 3D geometric structure from pretrained VLM vision tokens, eliminating reliance on ...

- **p. 3 / 3. Method - extractive body cue:** We propose SpatioLM, a unified framework that enhances VLMs with general physical spatial intelligence.
- **p. 3 / 3. Method - extractive body cue:** 3, SpatioLM freezes a pretrained VLM backbone and introduces a parameter-efficient runtime plugand-play Spatio-Vision Module (SV-Module, which consists of stacked Spatio-Vision Blocks) to elicit the ...
- **p. 2 / 1. Introduction - extractive body cue:** Without modifying the core structure of the base VLM, SpatioLM enables flexible activation or deactivation during the inference phase, thereby enhancing the base VLM with ...
- **p. 4 / 3.2. Spatio-Vision Module - extractive body cue:** This mechanism allows the model to separately model fine-grained geometry within each frame and global geometric relationships across frames.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Despite the effectiveness of SpatioLM, several limitations remain. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Impact Statement Addressing the critical limitation of multimodal large models in visual spatial reasoning, this work proposes SpatioLM, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 21 | Table 15. Failure consistency analysis on VSI-Bench. Consistency denotes the ratio of shared failures over SpatioLM failures. Task ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Results indicate that, despite large-scale training targeted at spatial intelligence, the performance degradation of SpatioLM on general tasks ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 2 (1. Introduction), p. 3 (3.1. Problem definition and notation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Problem definition and notation), p. 4 (3.2. Spatio-Vision Module), p. 2 (1. Introduction), p. 3 (3.1. Problem definition and notation), objective p. 5 (3.3. Loss Design), p. 5 (3.3. Loss Design), p. 6 (3.4. Unified Task Formulation), p. 6 (3.3. Loss Design).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
