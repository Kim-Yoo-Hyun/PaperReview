# Method — Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1999 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, actor-critic
- Official paper: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; theorem and experiment details remain UNVERIFIED.

## Pipeline

policy-gradient theorem과 compatible function approximation 조건을 제시하고 actor-critic update를 연결한다.

## Interface

state-action trajectories와 critic estimate를 policy parameter update로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
