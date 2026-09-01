# Problem - Attention Is All You Need

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1706.03762; PDF retrieval source: https://arxiv.org/pdf/1706.03762. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (2 Background), p. 2 (1 Introduction), p. 6 (2 Background), p. 6 (2 Background), p. 7 (2 Background)): This makes it more difficult to learn dependencies between distant positions [12].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.
- **p. 1 / Abstract - extractive PDF cue:** The best performing models also connect the encoder and decoder through an attention mechanism.
- **p. 1 / Abstract - extractive PDF cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- **p. 1 / Abstract - extractive PDF cue:** Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.
- **p. 1 / Abstract - extractive PDF cue:** Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.
- **p. 2 / 2 Background - extractive PDF cue:** This makes it more difficult to learn dependencies between distant positions [12].
- **p. 2 / 1 Introduction - extractive PDF cue:** In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This makes it more difficult to learn dependencies between distant positions [12]. | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF |
| State / latent | Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely, attention, mechanism | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | Hence, compare, maximum, path, length, between, input, output | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely, attention, mechanism | p. 2 (1 Introduction), p. 2 (2 Background), p. 6 (2 Background) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | paper-specific objective; cue terms: WMT, English-to-French, translation, task, model, establishes, single-model, state-of-the-art | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (2 Background), p. 5 (2 Background), p. 7 (2 Background) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2 Background), p. 5 (2 Background), p. 8 (2 Background) |
| Success / guarantee | source task metric; robot link not established | p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network.
- **p. 6 / 2 Background - extractive PDF cue:** Learning long-range dependencies is a key challenge in many sequence transduction tasks.
- **p. 6 / 2 Background - extractive PDF cue:** Layer Type Complexity per Layer Sequential Maximum Path Length Operations Self-Attention O(n2 · d) O(1) O(1) Recurrent O(n · d2) O(n) O(n) Convolutional O(k · ...
- **p. 7 / 2 Background - extractive PDF cue:** Convolutional layers are generally more expensive than recurrent layers, by a factor of k.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 4 (2 Background), p. 4 (2 Background)): In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output.

- **p. 1 / Abstract - extractive PDF cue:** We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. ...
- **p. 1 / Abstract - extractive PDF cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- **p. 4 / 2 Background - extractive PDF cue:** The input consists of queries and keys of dimension dk, and values of dimension dv.
- **p. 4 / 2 Background - extractive PDF cue:** (right) Multi-Head Attention consists of several attention layers running in parallel. of the values, where the weight assigned to each value is computed by a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | We plan to investigate this approach further in future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | A single convolutional layer with kernel width k < n does not connect all pairs of input and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 2 (2 Background), p. 6 (2 Background), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (2 Background), p. 2 (1 Introduction), p. 6 (2 Background), p. 6 (2 Background), p. 7 (2 Background), interface p. 2 (1 Introduction), p. 2 (2 Background), p. 6 (2 Background), p. 1 (Abstract), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (2 Background), p. 5 (2 Background), p. 7 (2 Background).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
