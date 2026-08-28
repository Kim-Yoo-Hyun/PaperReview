# Problem — Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, REINFORCE
- Official paper: https://doi.org/10.1007/BF00992696
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; estimator derivation remains UNVERIFIED.

## Target Problem and Assumptions

differentiable environment model 없이 stochastic policy parameter를 expected reward 방향으로 갱신한다.

## Closed-Loop Position

trajectory reward를 stochastic policy parameter update로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
