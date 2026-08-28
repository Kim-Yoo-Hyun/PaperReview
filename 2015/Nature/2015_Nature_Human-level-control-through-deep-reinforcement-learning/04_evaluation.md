# Evaluation — Human-level control through deep reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / Nature
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Deep Q-Network, Value Learning
- Official paper: https://doi.org/10.1038/nature14236
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; architecture and result details remain UNVERIFIED.

## Protocol

Atari game suite에서 단일 알고리즘의 성능을 비교하며 robotics embodiment는 직접 다루지 않는다.

## Limitations and Reproducibility

discrete actions, 높은 sample cost, reward specification과 safety 문제를 해결하지 않는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
