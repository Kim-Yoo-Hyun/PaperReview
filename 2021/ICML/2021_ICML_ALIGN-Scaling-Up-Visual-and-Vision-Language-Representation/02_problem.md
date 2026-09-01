# Problem - ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2102.05918; PDF retrieval source: https://arxiv.org/pdf/2102.05918. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Pre-trained representations are becoming crucial for many NLP and perception tasks.
- **p. 1 / Abstract - extractive PDF cue:** While representation learning in NLP has transitioned to training on raw text without human annotations, visual and vision-language representations still rely heavily on curated training ...
- **p. 1 / Abstract - extractive PDF cue:** For vision applications, representations are mostly learned using datasets with explicit class labels such as ImageNet or OpenImages.
- **p. 1 / Abstract - extractive PDF cue:** For vision-language, popular datasets like Conceptual Captions, MSCOCO, or CLIP all involve a non-trivial data collection (and cleaning) process.
- **p. 1 / Abstract - extractive PDF cue:** This costly curation process limits the size of datasets and hence hinders the scaling of trained models.
- **p. 1 / 1. Introduction - extractive PDF cue:** Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale.
- **p. 1 / 1. Introduction - extractive PDF cue:** In the existing literature, visual and vision-language representation learning are mostly studied separately with different training data sources.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale. | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | The aligned image and text representations are naturally suited for cross-modality matching/retrieval tasks and achieve state-of-the-art (SOTA) results in corresponding benchmarks. | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | aligned, image, text, representations, naturally, suited, cross-modality, matching/retrieval, tasks, achieve | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | However, vision-language, pre-training, datasets, Conceptual, Captions, Sharma, Visual | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: aligned, image, text, representations, naturally, suited, cross-modality, matching/retrieval, tasks, achieve | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: Moreover, cross-modality, matching, naturally, enables, zero-shot, image, classification | p. 2 (1. Introduction), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 4 (4.3. Transferring to Visual Classification) |
| Objective / loss / cost | paper-specific objective; cue terms: minimize, losses, image-to-text, classification, Li2t, other, text-to-image, Lt2i | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 9 (8. Multilingual ALIGN Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 9 (8. Multilingual ALIGN Model), p. 9 (8. Multilingual ALIGN Model) |
| Success / guarantee | source task metric; robot link not established | p. 5 (5.2. Zero-shot Visual Classification), p. 5 (5.2. Zero-shot Visual Classification), p. 6 (5.2. Zero-shot Visual Classification) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** In the existing literature, visual and vision-language representation learning are mostly studied separately with different training data sources.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 4 (4.3. Transferring to Visual Classification), p. 9 (8. Multilingual ALIGN Model), p. 1 (1. Introduction)): Moreover, such cross-modality matching naturally enables zero-shot image classification when feeding the classnames into the text encoder, achieving 76.4% top-1 accuracy in ImageNet without using any of its training samples.

- **p. 3 / 4.1. Pre-training on Noisy Image-Text Pairs - extractive PDF cue:** The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top.
- **p. 4 / 4.3. Transferring to Visual Classification - extractive PDF cue:** (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering ...
- **p. 9 / 8. Multilingual ALIGN Model - extractive PDF cue:** The dataset consists of 31,783 images with 5 captions per image in English and German and 1 caption per image in French and Czech.
- **p. 1 / 1. Introduction - extractive PDF cue:** We show that visual and visionlanguage representations pre-trained on our exascale dataset achieve very strong performance on a wide range of tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | We show that linear relationships between + "red" + "forest" + "desert" + "orange" + "blue" + "purple" ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Similar to CLIP, ALIGN shows great robustness on classification tasks with different image distributions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 3 (4.1. Pre-training on Noisy Image-Text Pairs), p. 9 (8. Multilingual ALIGN Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
