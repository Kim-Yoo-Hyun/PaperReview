# Method — Q-Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Q-learning, Value Learning
- Official paper: https://doi.org/10.1007/BF00992698
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof conditions remain UNVERIFIED.

## Pipeline

reward와 다음 상태의 최대 action value를 이용한 TD update로 action-value function을 갱신한다.

## Interface

state-action-reward-next-state samples를 discrete action selection용 Q-value로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
