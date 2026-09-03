# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1810.04805.
> PDF retrieval source: https://arxiv.org/pdf/1810.04805. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / NAACL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: LLM, Transformer, pretraining
- Official paper: https://arxiv.org/abs/1810.04805
- Full-text retrieval: https://arxiv.org/pdf/1810.04805
- Code/Project: https://github.com/google-research/bert
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.를 문제로 두고, Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 1 / Abstract - extractive body cue:** Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by ...
- **p. 1 / Abstract - extractive body cue:** As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of ...
- **p. 1 / Abstract - extractive body cue:** BERT is conceptually simple and empirically powerful.
- **p. 1 / Abstract - extractive body cue:** It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to ...
- **p. 1 / 1 Introduction - extractive body cue:** The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.
- **p. 1 / 1 Introduction - extractive body cue:** We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper are as follows: • We demonstrate the importance of bidirectional pre-training for language representations.
- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 3 / C T1 - extractive body cue:** There are two steps in our framework: pre-training and fine-tuning.
- **p. 3 / C T1 - extractive body cue:** 3 BERT We introduce BERT and its detailed implementation in this section.
- **p. 2 / 1 Introduction - extractive body cue:** BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming many task-specific architectures. ...
- **p. 5 / C T1 - extractive body cue:** 3.2 Fine-tuning BERT Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream taskswhether they involve single text or ...
- **p. 1 / 1 Introduction - extractive body cue:** The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language ... | 논문이 명시한 observation과 task input | p. 1 (Abstract), p. 4 (C T1) |
| State/latent | result, pre-trained, BERT, model, finetuned, just, additional, output, layer, create, state-of-the-art, models | task state 또는 decision variable | p. 1 (Abstract), p. 4 (C T1), p. 5 (C T1) |
| Output/action | Input/Output Representations To make BERT handle a variety of down-stream tasks, our input representation is able to unambiguously represent both a single sentence and a pair of sentences (e.g., ⟨Question, Answer ⟩) ... | paper-specific output/action | p. 4 (C T1), p. 5 (C T1), p. 5 (C T1) |
| Objective/outcome | BERT alleviates the previously mentioned unidirectionality constraint by using a "masked language model" (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). | primary task objective와 closed-loop behavior | p. 1 (1 Introduction), p. 4 (C T1), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a ...
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper are as follows: • We demonstrate the importance of bidirectional pre-training for language representations.
- **p. 1 / Abstract - extractive body cue:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
- **p. 3 / C T1 - extractive body cue:** There are two steps in our framework: pre-training and fine-tuning.
- **p. 3 / C T1 - extractive body cue:** 3 BERT We introduce BERT and its detailed implementation in this section.
- **p. 6 / 4 Experiments - extractive body cue:** Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior ...
- **p. 8 / 4 Experiments - extractive body cue:** This does significantly improve results on SQuAD, but the results are still far worse than those of the pretrained bidirectional models.
- **p. 8 / 4 Experiments - extractive body cue:** It is also perhaps surprising that we are able to achieve such significant improvements on top of models which are already quite large relative to ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | 4.1 GLUE The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | Detailed descriptions of GLUE datasets are included in Appendix B.1. | role, split, size and leakage | p. 5 (4 Experiments), p. 8 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Metric | F1 scores are reported for QQP and MRPC, Spearman correlations are reported for STS-B, and accuracy scores are reported for the other tasks. | definition, denominator, direction and uncertainty | p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Baseline/ablation | BERTLARGE outperforms the authors' baseline ESIM+ELMo system by +27.1% and OpenAI GPT by 8.3%. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 Experiments - extractive body cue:** Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on ...
- **p. 6 / 4 Experiments - extractive body cue:** Given a question and a passage from 9The GLUE data set distribution does not include the Test labels, and we only made a single GLUE ...
- **p. 8 / 4 Experiments - extractive body cue:** The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training.를 문제로 두고, Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (C T1) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
