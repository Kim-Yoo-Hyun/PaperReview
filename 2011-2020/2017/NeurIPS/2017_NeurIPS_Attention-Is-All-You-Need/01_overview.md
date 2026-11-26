# Attention Is All You Need

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1706.03762.
> PDF retrieval source: https://arxiv.org/pdf/1706.03762. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / NeurIPS
- Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Transformer, attention, representation
- Official paper: https://arxiv.org/abs/1706.03762
- Full-text retrieval: https://arxiv.org/pdf/1706.03762
- Code/Project: https://github.com/tensorflow/tensor2tensor
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Transformer는 순환층 없이 어텐션을 사용해 입력 문장을 다른 언어의 문장으로 변환한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.
- **p. 1 / Abstract - extractive body cue:** The best performing models also connect the encoder and decoder through an attention mechanism.
- **p. 1 / Abstract - extractive body cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- **p. 1 / Abstract - extractive body cue:** Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.
- **p. 1 / Abstract - extractive body cue:** Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.
- **p. 2 / 2 Background - extractive body cue:** This makes it more difficult to learn dependencies between distant positions [12].
- **p. 2 / 1 Introduction - extractive body cue:** In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between ...
- **p. 1 / Abstract - extractive body cue:** We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- **p. 4 / 2 Background - extractive body cue:** The input consists of queries and keys of dimension dk, and values of dimension dv.
- **p. 4 / 2 Background - extractive body cue:** (right) Multi-Head Attention consists of several attention layers running in parallel. of the values, where the weight assigned to each value is computed by a ...
- **p. 5 / 2 Background - extractive body cue:** This consists of two linear transformations with a ReLU activation in between.
- **p. 2 / 2 Background - extractive body cue:** To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and ...
- **p. 3 / 2 Background - extractive body cue:** The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and ...
- **p. 5 / 2 Background - extractive body cue:** 3.2.3 Applications of Attention in our Model The Transformer uses multi-head attention in three different ways: • In "encoder-decoder attention" layers, the queries come from ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. | 논문이 명시한 observation과 task input | p. 2 (1 Introduction), p. 2 (2 Background) |
| State/latent | Transformer, model, architecture, eschewing, recurrence, instead, relying, entirely, attention, mechanism, draw, global | task state 또는 decision variable | p. 2 (1 Introduction), p. 2 (2 Background), p. 6 (2 Background) |
| Output/action | The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, ... | paper-specific output/action | p. 2 (2 Background), p. 6 (2 Background), p. 1 (Abstract) |
| Objective/outcome | On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training ... | primary task objective와 closed-loop behavior | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 인코더와 디코더에 다중 헤드 어텐션과 위치 정보를 사용한다.
- 두 기계번역 과제에서 품질과 학습 비용을 비교한다.

[저자 원문](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (6 Results), p. 8 (6 Results) |
| Embodiment/environment | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training cost of ... | hardware/simulator version and reset protocol | p. 8 (6 Results), p. 8 (6 Results) |
| Dataset/benchmark | This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input. | role, split, size and leakage | p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results), p. 9 (6 Results) |
| Metric | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training cost of ... | definition, denominator, direction and uncertainty | p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results) |
| Baseline/ablation | On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training cost of ... | fair input/data/compute/action matching | p. 8 (6 Results), p. 8 (6 Results), p. 9 (6 Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 2 Background - extractive body cue:** We plan to investigate this approach further in future work.
- **p. 7 / 2 Background - extractive body cue:** A single convolutional layer with kernel width k < n does not connect all pairs of input and output positions.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (2 Background), p. 2 (1 Introduction), p. 6 (2 Background), p. 7 (2 Background), p. 1 (Abstract)이다.
