# Method — Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, REINFORCE
- Official paper: https://doi.org/10.1007/BF00992696
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; estimator derivation remains UNVERIFIED.

## Pipeline

sampled action의 log-probability gradient에 return/reinforcement signal을 곱한 unbiased estimator를 사용한다.

## Interface

trajectory reward를 stochastic policy parameter update로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
