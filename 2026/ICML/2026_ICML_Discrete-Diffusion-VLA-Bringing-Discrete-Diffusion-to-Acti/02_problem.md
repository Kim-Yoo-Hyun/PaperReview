# Problem

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Paper link: ./2026/ICML/2026_ICML_Discrete-Diffusion-VLA-Bringing-Discrete-Diffusion-to-Acti/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Continuous diffusion over action chunks (left) versus discrete token decoders: AR (sequential), BERT-style (parallel), and our discrete diffusion with re-masking.
- Diffusion AR Action Chunk Sequential BERT Discrete Iterative Diffusion Refine Parallel Action Chunk Gen.
- Current approaches fall into two paradigms: (1) an autoregressive (AR) approach, inspired by GPT-style transformers, that predicts discretized action tokens sequentially (e.g.

## 해결하려는 문제
- Instead, we present Discrete Diffusion VLA that discretizes action chunks and models them with discrete diffusion pattern retaining progressive refinement inside the unified transformer backbone.
- On out-of-distribution tests of LIBERO-Goal, our method exhibits only 0.8% language degradation versus 8.0% of parallel decoding, and 20.4% vision degradation versus 29.0% for continuous diffusion, demonstrating well ...
- Our method achieves an adaptive decoding order that resolves high-confidence action elements before harder ones and employs secondary re-masking to revisit uncertain predictions, enabling robust error correction.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
