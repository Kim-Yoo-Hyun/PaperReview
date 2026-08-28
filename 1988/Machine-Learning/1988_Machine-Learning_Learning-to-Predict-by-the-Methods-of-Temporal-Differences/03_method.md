# Method — Learning to Predict by the Methods of Temporal Differences

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1988 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, temporal difference, Value Learning
- Official paper: https://doi.org/10.1007/BF00115009
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; convergence arguments remain UNVERIFIED.

## Pipeline

현재 예측과 다음-step bootstrapped target의 temporal-difference error로 value estimate를 수정한다.

## Interface

state-transition-reward stream을 value prediction으로 변환하는 learning component다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
