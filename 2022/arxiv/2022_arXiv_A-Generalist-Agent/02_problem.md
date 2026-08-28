# Problem — A Generalist Agent

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, Generalist Agent, Transformer, Multimodal Learning, Google DeepMind
- Official paper: https://arxiv.org/abs/2205.06175
- Code/Project: https://deepmind.google/discover/blog/a-generalist-agent/
- Source audit: arXiv abstract and official DeepMind article checked; dataset and result details remain UNVERIFIED.

## Target Problem and Assumptions

서로 다른 modality, embodiment와 task를 각각 별도 모델이 아닌 하나의 policy로 수행한다.

## Closed-Loop Position

text/image/state history를 task별 discrete/continuous action token으로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
