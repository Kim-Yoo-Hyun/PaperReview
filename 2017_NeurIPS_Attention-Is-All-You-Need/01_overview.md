# Attention Is All You Need

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, representation
- Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez
- Paper: https://arxiv.org/abs/1706.03762
- PDF status: downloaded
- GitHub/Project: https://github.com/tensorflow/tensor2tensor

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 attention 기반 sequence modeling을 통해 장거리 의존성과 modality alignment를 scale-up 가능한 방식으로 학습하는 것이다.

## Paper-Specific Cues
- Topic cue: The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration.
- Method cue: We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- Result cue: Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to ...

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `sequence/representation learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- sequence/representation learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: LLM, Transformer, representation.
- 초록에서 확인되는 주요 cue: The, Transformer, Experiments, Our, BLEU, WMT, English-to-German, English-to-French.
