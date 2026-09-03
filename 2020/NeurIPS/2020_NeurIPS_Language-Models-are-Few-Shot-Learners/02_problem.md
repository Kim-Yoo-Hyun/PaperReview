# Problem - Language Models are Few-Shot Learners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (75 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.14165; PDF retrieval source: https://arxiv.org/pdf/2005.14165. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction)): However, a major limitation to this approach is that while the architecture is task-agnostic, there is still a need for task-specific datasets and task-specific fine-tuning: to achieve strong performance on ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a ...
- **p. 1 / Abstract - extractive body cue:** While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples.
- **p. 1 / Abstract - extractive body cue:** By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems ...
- **p. 1 / Abstract - extractive body cue:** Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches.
- **p. 1 / Abstract - extractive body cue:** Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in ...
- **p. 4 / 1 Introduction - extractive body cue:** Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages - it allows humans to seamlessly mix together ...
- **p. 5 / 1 Introduction - extractive body cue:** We also show that in the few-shot setting, GPT-3 can generate synthetic news articles which human evaluators have difficulty distinguishing from human-generated articles.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a major limitation to this approach is that while the architecture is task-agnostic, there is still a need for task-specific datasets ... | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | Recent work [RWC+19] attempts to do this via what we call "in-context learning", using the text input of a pretrained language model ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF body |
| State / latent | Recent, RWC, attempts, what, call, in-context, learning, text, input, pretrained | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | main, disadvantage, have, been, much, worse, state-of-the-art, fine-tuned | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: Recent, RWC, attempts, what, call, in-context, learning, text, input, pretrained | p. 4 (1 Introduction), p. 7 (2 Approach), p. 6 (2 Approach) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: panels, above, four, methods, performing, task, language, model | p. 7 (2 Approach), p. 5 (1 Introduction), p. 5 (1 Introduction) |
| Objective / loss / cost | paper-specific objective; cue terms: Data, sampled, without, replacement, during, training, until, epoch | p. 8 (2 Approach), p. 8 (2 Approach), p. 9 (2 Approach), p. 43 (B Details of Model Training), p. 57 (Model), p. 58 (Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (2 Approach), p. 9 (2 Approach), p. 9 (2 Approach) |
| Success / guarantee | source task metric; robot link not established | p. 18 (3 Results), p. 10 (2.4 Evaluation), p. 12 (3 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 4 / 1 Introduction - extractive body cue:** Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages - it allows humans to seamlessly mix together ...
- **p. 5 / 1 Introduction - extractive body cue:** We also show that in the few-shot setting, GPT-3 can generate synthetic news articles which human evaluators have difficulty distinguishing from human-generated articles.
- **p. 3 / 1 Introduction - extractive body cue:** Removing this limitation would be desirable, for several reasons.
- **p. 5 / 1 Introduction - extractive body cue:** By presenting a broad characterization of GPT-3's strengths and weaknesses, including these limitations, we hope to stimulate study of few-shot learning in language models and ...

## What the Paper Changes

PDF body contribution framing (p. 7 (2 Approach), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction)): The panels above show four methods for performing a task with a language model - fine-tuning is the traditional method, whereas zero-, one-, and few-shot, which we study in this ...

- **p. 5 / 1 Introduction - extractive body cue:** Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to ...
- **p. 5 / 1 Introduction - extractive body cue:** GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning, which include unscrambling words, performing arithmetic, and using ...
- **p. 4 / 1 Introduction - extractive body cue:** We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with and without a natural ...
- **p. 6 / 1 Introduction - extractive body cue:** In Section 2, we describe our approach and methods for training GPT-3 and evaluating it.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 33 | An important limitation of our contamination analysis is that we cannot be sure that the clean subset is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 41 | Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | 21 4 Measuring and Preventing Memorization Of Benchmarks 29 5 Limitations 33 6 Broader Impacts 34 6.1 Misuse ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 1.2: Larger models make increasingly efficient use of in-context information. We show in-context learning performance on a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (1 Introduction), p. 7 (2 Approach), p. 6 (2 Approach), p. 7 (2 Approach). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), interface p. 4 (1 Introduction), p. 7 (2 Approach), p. 6 (2 Approach), p. 7 (2 Approach), objective p. 8 (2 Approach), p. 8 (2 Approach), p. 9 (2 Approach), p. 43 (B Details of Model Training), p. 57 (Model), p. 58 (Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
