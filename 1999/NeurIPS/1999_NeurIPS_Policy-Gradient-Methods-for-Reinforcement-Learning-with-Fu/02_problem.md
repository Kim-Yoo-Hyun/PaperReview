# Problem — Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1999 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, actor-critic
- Official paper: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; theorem and experiment details remain UNVERIFIED.

## Target Problem and Assumptions

parameterized stochastic policy의 average performance gradient를 value approximation과 함께 계산한다.

## Closed-Loop Position

state-action trajectories와 critic estimate를 policy parameter update로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
