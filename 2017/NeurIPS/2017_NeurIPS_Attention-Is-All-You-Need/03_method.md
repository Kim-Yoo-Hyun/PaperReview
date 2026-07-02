# Method

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_Attention-Is-All-You-Need/paper.pdf
- Code/Project: https://github.com/tensorflow/tensor2tensor
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- The best performing models also connect the encoder and decoder through an attention mechanism.
- The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder.

## 원리적 동기
- Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction ...
- This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.
- We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.

## 핵심 방법론
- Most competitive neural sequence transduction models have an encoder-decoder structure .
- Here, the encoder maps an input sequence of symbol representations (x1 , ..., xn ) to a sequence of continuous representations z = (z1 , ..., zn ).
- Given z, the decoder then generates an output sequence (y1 , ..., ym ) of symbols one element at a time.
