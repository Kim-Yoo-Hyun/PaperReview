# Problem - Flamingo: a Visual Language Model for Few-Shot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (54 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.14198; PDF retrieval source: https://arxiv.org/pdf/2204.14198. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning ...
- **p. 1 / Abstract - extractive PDF cue:** We introduce Flamingo, a family of Visual Language Models (VLM) with this ability.
- **p. 1 / Abstract - extractive PDF cue:** We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and ...
- **p. 1 / Abstract - extractive PDF cue:** Thanks to their flexibility, Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow ...
- **p. 1 / Abstract - extractive PDF cue:** We perform a thorough evaluation of our models, exploring and measuring their ability to rapidly adapt to a variety of image and video tasks.
- **p. 3 / 1 Introduction - extractive PDF cue:** They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual questionanswering.
- **p. 3 / 1 Introduction - extractive PDF cue:** We show that the same can be done for image and video understanding tasks such as classification, captioning, or question-answering: these can be cast as ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual ... | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | This section describes Flamingo: a visual language model that accepts text interleaved with images/videos as input and outputs free-form text. | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | section, describes, Flamingo, visual, language, model, accepts, text, interleaved, images/videos | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | takes, input, variable, number, image, video, features, vision | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: section, describes, Flamingo, visual, language, model, accepts, text, interleaved, images/videos | p. 4 (2 Approach), p. 3 (1 Introduction), p. 5 (2 Approach) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: summary, contributions, following, introduce, Flamingo, family, VLMs, perform | p. 4 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | paper-specific objective; cue terms: light, trade-off, maximize, number, added, layers, under, hardware | p. 5 (2 Approach), p. 8 (Method), p. 9 (Method), p. 6 (2 Approach), p. 6 (2 Approach), p. 9 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (Method), p. 6 (2 Approach), p. 6 (2 Approach) |
| Success / guarantee | source task metric; robot link not established | p. 31 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (3 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive PDF cue:** We show that the same can be done for image and video understanding tasks such as classification, captioning, or question-answering: these can be cast as ...
- **p. 4 / 1 Introduction - extractive PDF cue:** On 6 of these 16 tasks, Flamingo also outperforms the fine-tuned state of the art despite using only 32 task-specific examples, around 1000 times less ...

## What the Paper Changes

PDF contribution framing (p. 4 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (2 Approach), p. 6 (2 Approach)): In summary, our contributions are the following: (i) We introduce the Flamingo family of VLMs which can perform various multimodal tasks (such as captioning, visual dialogue, or visual question-answering) from ...

- **p. 3 / 1 Introduction - extractive PDF cue:** We introduce Flamingo, a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended ...
- **p. 3 / 1 Introduction - extractive PDF cue:** While initial progress has been made towards a similar capability in computer vision, the most widely used paradigm still consists of first pretraining on a ...
- **p. 6 / 2 Approach - extractive PDF cue:** We also collect a similar dataset but with videos instead of still images: VTP (Video & Text Pairs) consists of 27 million short videos (approximately ...
- **p. 6 / 2 Approach - extractive PDF cue:** To complement this dataset, we collect our own dataset of image and text pairs targeting better quality and longer descriptions: LTIP (Long Text & Image ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 42 | Figure 13: Hallucinations and ungrounded guesses in open-ended visual question answering. Left: The model occasionally hallucinates by producing ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We discuss the limitations of our work in more depth in Appendix D.1. | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Figure 9: Training datasets. Mixture of training datasets of different formats. 𝑁corresponds to the number of visual inputs ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 35 | Table 10. We ablate the size of our Resampler with three options: Small, Medium (default value for all ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (2 Approach), p. 3 (1 Introduction), p. 5 (2 Approach), p. 5 (2 Approach). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), interface p. 4 (2 Approach), p. 3 (1 Introduction), p. 5 (2 Approach), p. 5 (2 Approach), objective p. 5 (2 Approach), p. 8 (Method), p. 9 (Method), p. 6 (2 Approach), p. 6 (2 Approach), p. 9 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
