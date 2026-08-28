# Evaluation — A Generalist Agent

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, Generalist Agent, Transformer, Multimodal Learning, Google DeepMind
- Official paper: https://arxiv.org/abs/2205.06175
- Code/Project: https://deepmind.google/discover/blog/a-generalist-agent/
- Source audit: arXiv abstract and official DeepMind article checked; dataset and result details remain UNVERIFIED.

## Protocol

Atari, language, vision, simulated/real robot control 등 다수 domain을 하나의 모델로 평가한다.

## Limitations and Reproducibility

specialist 대비 성능, context/action tokenization, data mixture와 real-time closed-loop control 제약이 남는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
