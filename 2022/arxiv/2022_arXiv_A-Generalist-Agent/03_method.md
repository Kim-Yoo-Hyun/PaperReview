# Method — A Generalist Agent

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, Generalist Agent, Transformer, Multimodal Learning, Google DeepMind
- Official paper: https://arxiv.org/abs/2205.06175
- Code/Project: https://deepmind.google/discover/blog/a-generalist-agent/
- Source audit: arXiv abstract and official DeepMind article checked; dataset and result details remain UNVERIFIED.

## Pipeline

observations와 actions를 공통 token sequence로 직렬화해 autoregressive transformer를 multi-domain data에 학습한다.

## Interface

text/image/state history를 task별 discrete/continuous action token으로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
