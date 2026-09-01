# Problem - Learning Transferable Visual Models From Natural Language Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.00020; PDF retrieval source: https://arxiv.org/pdf/2103.00020. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (1. Introduction and Motivating Work), p. 6 (3.1.1. MOTIVATION), p. 6 (3.1.1. MOTIVATION)): Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs.

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
| Target problem | Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs. | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | discussed, introduction, idea, however, terminology, describe, space, varied | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: development, text-to-text, standardized, input-output, interface, McCann, Radford, Raffel, enabled, taskagnostic | p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: Pre-training, methods, learn, directly, text, have, revolutionized, NLP | p. 1 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision), p. 3 (2.1. Natural Language Supervision) |
| Objective / loss / cost | paper-specific objective; cue terms: knowledge, batch, construction, technique, objective, first, introduced, area | p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training), p. 5 (2.4. Choosing and Scaling a Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (2.5. Training), p. 5 (2.5. Training), p. 3 (2.1. Natural Language Supervision) |
| Success / guarantee | source task metric; robot link not established | p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** In this work, we close this gap and study the behaviors of image classifiers trained with natural language supervision at large scale.
- **p. 3 / 1. Introduction and Motivating Work - extractive body cue:** Swapping the prediction objective for the contrastive objective of CLIP further improves efficiency another 4x. it can be competitive with prior task-specific supervised models.
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** We instead use the term in a broader sense and study generalization to unseen datasets.
- **p. 6 / 3.1.1. MOTIVATION - extractive body cue:** To our knowledge, Visual N-Grams (Li et al., 2017) first studied zero-shot transfer to existing image classification datasets in the manner described above.

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 1 (1. Introduction and Motivating Work)): Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years (Dai & Le, 2015; Peters et al., 2018; Howard & Ruder, 2018; Radford et ...

- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** Learning from natural language also has an important advantage over most unsupervised or self-supervised learning approaches in that it doesn't "just" learn a representation but ...
- **p. 3 / 2.1. Natural Language Supervision - extractive body cue:** At the core of our approach is the idea of learning perception from supervision contained in natural language.
- **p. 4 / 2.3. Selecting an Efficient Pre-Training Method - extractive body cue:** In Figure 2 we show that a 63 million parameter transformer language model, which already uses twice the compute of its ResNet-50 image encoder, learns ...
- **p. 1 / 1. Introduction and Motivating Work - extractive body cue:** The development of "text-to-text" as a standardized input-output interface (McCann et al., 2018; Radford et al., 2019; Raffel et al., 2019) has enabled taskagnostic architectures ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 25 | This process of characterization can help researchers increase the likelihood models are used beneficially by: • Identifying potentially ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Fine-tuning, because it adapts representations to each dataset during the fine-tuning phase, can compensate for and potentially mask ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | There are still many limitations to CLIP. | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Our methodology has several significant limitations. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (1. Introduction and Motivating Work), p. 6 (3.1.1. MOTIVATION), p. 6 (3.1.1. MOTIVATION), interface p. 1 (1. Introduction and Motivating Work), p. 2 (1. Introduction and Motivating Work), p. 3 (2.1. Natural Language Supervision), p. 4 (2.3. Selecting an Efficient Pre-Training Method), objective p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 4 (2.3. Selecting an Efficient Pre-Training Method), p. 5 (2.5. Training), p. 5 (2.4. Choosing and Scaling a Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
