# Problem — Learning to Predict by the Methods of Temporal Differences

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1988 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, temporal difference, Value Learning
- Official paper: https://doi.org/10.1007/BF00115009
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; convergence arguments remain UNVERIFIED.

## Target Problem and Assumptions

완전한 episode return을 기다리지 않고 sequential prediction을 online으로 갱신한다.

## Closed-Loop Position

state-transition-reward stream을 value prediction으로 변환하는 learning component다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
