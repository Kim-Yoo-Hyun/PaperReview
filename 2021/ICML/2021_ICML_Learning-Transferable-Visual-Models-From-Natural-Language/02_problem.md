# Problem - Learning Transferable Visual Models From Natural Language Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://proceedings.mlr.press/v139/radford21a.html)
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.00020; PDF retrieval source: https://arxiv.org/pdf/2103.00020. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

고정된 클래스 레이블로 학습한 분류기는 새로운 시각 개념에 적응하려면 추가 주석이 필요하다. [원문](https://proceedings.mlr.press/v139/radford21a.html)

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
- **p. 1 / Abstract - extractive body cue:** This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept.
- **p. 1 / Abstract - extractive body cue:** Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision.
- **p. 1 / Abstract - extractive body cue:** We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image ...
- **p. 1 / Abstract - extractive body cue:** After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks.
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs.
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** In this work, we close this gap and study the behaviors of image classifiers trained with natural language supervision at large scale.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs. | 자연 이미지와 설명 텍스트 | body wording is the source claim |
| Observation / input | The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF body |
| State / latent | development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | discussed, introduction, idea, however, terminology, describe, space, varied | 이미지–텍스트 유사도와 클래스별 예측 | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | zero-shot 시각 전이 성능 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic | p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: Learning, natural, language, important, advantage, over, most, unsupervised | p. 3 (2.1. Natural Language Supervision), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method) |
| Objective / loss / cost | paper-specific objective; cue terms: knowledge, batch, construction, technique, objective, first, introduced, area | p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training), p. 5 (2.4. Choosing and Scaling a Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (2.5. Training), p. 5 (2.5. Training), p. 3 (2.1. Natural Language Supervision) |
| Success / guarantee | source task metric; robot link not established | p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** In this work, we close this gap and study the behaviors of image classifiers trained with natural language supervision at large scale.
- **p. 3 / 1. Introduction and Motivating Work - extractive body cue:** Swapping the prediction objective for the contrastive objective of CLIP further improves efficiency another 4x. it can be competitive with prior task-specific supervised models.
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** We instead use the term in a broader sense and study generalization to unseen datasets.
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** To our knowledge, Visual N-Grams (Li et al., 2017) first studied zero-shot transfer to existing image classification datasets in the manner described above.

## What the Paper Changes

PDF body contribution framing (p. 3 (2.1. Natural Language Supervision), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 1 (1. Introduction and Motivating Work), p. 6 (3.1.1. MOTIVATION)): Learning from natural language also has an important advantage over most unsupervised or self-supervised learning approaches in that it doesn't "just" learn a representation but also connects that representation to ...

- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** At the core of our approach is the idea of learning perception from supervision contained in natural language.
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** In Figure 2 we show that a 63 million parameter transformer language model, which already uses twice the compute of its ResNet-50 image encoder, learns ...
- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has enabled taskagnostic architectures ...
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** However, many popular computer vision datasets were created by the research community primarily as benchmarks to guide the development of generic image classification methods rather ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 25 | This process of characterization can help researchers increase the likelihood models are used beneficially by: • Identifying potentially ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Fine-tuning, because it adapts representations to each dataset during the fine-tuning phase, can compensate for and potentially mask ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | There are still many limitations to CLIP. | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Our methodology has several significant limitations. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

후속 로봇 시스템에서는 이미지와 지시의 의미를 비교하는 지각 단계에 CLIP 표현을 활용할 수 있다. 원 논문의 출력은 이미지–텍스트 유사도이며 직접 측정한 성능은 시각 인식 지표다. [원문](https://proceedings.mlr.press/v139/radford21a.html)

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (1. Introduction and Motivating Work), p. 6 (3.1.1. MOTIVATION), p. 6 (3.1.1. MOTIVATION), interface p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method), objective p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training), p. 5 (2.4. Choosing and Scaling a Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs. (p. 2, 1. Introduction and Motivating Work).
- **Formulation-changing contribution:** At the core of our approach is the idea of learning perception from supervision contained in natural language. (p. 3, 2.1. Natural Language Supervision).
- **Assumption/failure evidence:** Linear classifiers, because of their limited flexibility, instead highlight these failures and provide clear feedback during development. (p. 11, 3.2. Representation Learning).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
