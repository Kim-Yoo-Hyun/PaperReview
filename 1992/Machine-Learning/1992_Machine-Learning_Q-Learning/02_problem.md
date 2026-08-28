# Problem — Q-Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Q-learning, Value Learning
- Official paper: https://doi.org/10.1007/BF00992698
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof conditions remain UNVERIFIED.

## Target Problem and Assumptions

transition model 없이 trial-and-error data로 optimal action policy를 학습한다.

## Closed-Loop Position

state-action-reward-next-state samples를 discrete action selection용 Q-value로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
