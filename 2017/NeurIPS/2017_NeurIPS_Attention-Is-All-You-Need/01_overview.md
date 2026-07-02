# Attention Is All You Need

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_Attention-Is-All-You-Need/paper.pdf
- Code/Project: https://github.com/tensorflow/tensor2tensor
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction ...
- This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.
- The fundamental constraint of sequential computation, however, remains.

## Core Idea
- We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- The best performing models also connect the encoder and decoder through an attention mechanism.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 ...
- Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.
- 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- The best performing models also connect the encoder and decoder through an attention mechanism.
- We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## Abstract Cue
- The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.
