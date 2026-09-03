# Problem - BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.04805; PDF retrieval source: https://arxiv.org/pdf/1810.04805. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 1 / Abstract - extractive body cue:** Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by ...
- **p. 1 / Abstract - extractive body cue:** As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of ...
- **p. 1 / Abstract - extractive body cue:** BERT is conceptually simple and empirically powerful.
- **p. 1 / Abstract - extractive body cue:** It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to ...
- **p. 1 / 1 Introduction - extractive body cue:** The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- **p. 1 / 1 Introduction - extractive body cue:** We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during ... | 논문이 정의한 robot/embodied environment | body wording is the source claim |
| Observation / input | As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a ... | 논문이 명시한 observation과 task input | exact sensor/frame/preprocessing from PDF body |
| State / latent | result, pre-trained, BERT, model, finetuned, just, additional, output, layer, create | task state 또는 decision variable | notation and tensor shape require body check |
| Output / action | task, simply, plug, taskspecific, inputs, outputs, BERT, finetune | paper-specific output/action | exact unit/frame/decoder require body check |
| Target outcome | source task metric; robot link not established | primary task objective와 closed-loop behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | source-defined input o; body terms: result, pre-trained, BERT, model, finetuned, just, additional, output, layer, create | p. 1 (Abstract), p. 4 (C T1), p. 5 (C T1) |
| Decision / output variable | prediction/embedding/sample ŷ; body terms: Unlike, left-toright, language, model, pre-training, MLM, objective, enables | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | paper-specific objective; cue terms: BERT, alleviates, previously, mentioned, unidirectionality, constraint, masked, language | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (C T1), p. 4 (C T1), p. 5 (C T1) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (C T1), p. 5 (C T1) |
| Success / guarantee | source task metric; robot link not established | p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (C T1), p. 3 (C T1)): Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer.

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper are as follows: • We demonstrate the importance of bidirectional pre-training for language representations.
- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 3 / C T1 - extractive body cue:** There are two steps in our framework: pre-training and fine-tuning.
- **p. 3 / C T1 - extractive body cue:** 3 BERT We introduce BERT and its detailed implementation in this section.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Given a question and a passage from 9The GLUE data set distribution does not include the Test labels, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

upstream writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 4 (C T1), p. 5 (C T1), p. 5 (C T1). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 1 (Abstract), p. 4 (C T1), p. 5 (C T1), p. 5 (C T1), objective p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (C T1), p. 4 (C T1), p. 5 (C T1).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
