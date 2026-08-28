# Problem — Human-level control through deep reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / Nature
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Deep Q-Network, Value Learning
- Official paper: https://doi.org/10.1038/nature14236
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; architecture and result details remain UNVERIFIED.

## Target Problem and Assumptions

고차원 pixel observation에서 직접 action-value policy를 학습한다.

## Closed-Loop Position

image frame history를 discrete action Q-values로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
