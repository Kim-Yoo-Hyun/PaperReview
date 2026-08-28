# Method — Human-level control through deep reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / Nature
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Deep Q-Network, Value Learning
- Official paper: https://doi.org/10.1038/nature14236
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; architecture and result details remain UNVERIFIED.

## Pipeline

convolutional Q-network에 experience replay와 target network를 결합해 학습 안정성을 높인다.

## Interface

image frame history를 discrete action Q-values로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
