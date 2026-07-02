# Problem

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_Attention-Is-All-You-Need/paper.pdf
- Code/Project: https://github.com/tensorflow/tensor2tensor
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction ...
- This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.
- The fundamental constraint of sequential computation, however, remains.

## 해결하려는 문제
- We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- The best performing models also connect the encoder and decoder through an attention mechanism.
- We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## 선행 연구 / 배경 단서
- In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output.
- Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction ...
- This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.
