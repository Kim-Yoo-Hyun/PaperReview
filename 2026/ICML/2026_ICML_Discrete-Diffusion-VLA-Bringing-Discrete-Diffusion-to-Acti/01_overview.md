# Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Paper link: ./2026/ICML/2026_ICML_Discrete-Diffusion-VLA-Bringing-Discrete-Diffusion-to-Acti/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Continuous diffusion over action chunks (left) versus discrete token decoders: AR (sequential), BERT-style (parallel), and our discrete diffusion with re-masking.
- Diffusion AR Action Chunk Sequential BERT Discrete Iterative Diffusion Refine Parallel Action Chunk Gen.
- Current approaches fall into two paradigms: (1) an autoregressive (AR) approach, inspired by GPT-style transformers, that predicts discretized action tokens sequentially (e.g.

## Core Idea
- Instead, we present Discrete Diffusion VLA that discretizes action chunks and models them with discrete diffusion pattern retaining progressive refinement inside the unified transformer backbone.
- On out-of-distribution tests of LIBERO-Goal, our method exhibits only 0.8% language degradation versus 8.0% of parallel decoding, and 20.4% vision degradation versus 29.0% for continuous diffusion, demonstrating well ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method achieves an adaptive decoding order that resolves high-confidence action elements before harder ones and employs secondary re-masking to revisit uncertain predictions, enabling robust error correction.
- Discrete Diffusion VLA achieves 96.4% avg. success on LIBERO, 71.2% visual matching on SimplerEnv-Fractal, and 54.2% overall on SimplerEnv-Bridge.
- This design preserves pretrained vision-language priors, supports parallel decoding, and improves the efficiency.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Instead, we present Discrete Diffusion VLA that discretizes action chunks and models them with discrete diffusion pattern retaining progressive refinement inside the unified transformer backbone.
- On out-of-distribution tests of LIBERO-Goal, our method exhibits only 0.8% language degradation versus 8.0% of parallel decoding, and 20.4% vision degradation versus 29.0% for continuous diffusion, demonstrating well ...
- Our method achieves an adaptive decoding order that resolves high-confidence action elements before harder ones and employs secondary re-masking to revisit uncertain predictions, enabling robust error correction.

## Abstract Cue
- Iterative Refine Vision–Language–Action (VLA) models adapt large vision–language backbones to map images and instructions into robot actions.
