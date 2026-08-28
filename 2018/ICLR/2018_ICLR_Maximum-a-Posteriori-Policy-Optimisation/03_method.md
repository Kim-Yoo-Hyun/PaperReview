# Method — Maximum a Posteriori Policy Optimisation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / ICLR
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning
- Official paper: https://openreview.net/forum?id=S1ANxQW0b
- Code/Project: not identified
- Source audit: official OpenReview abstract checked; derivation and experimental details remain UNVERIFIED.

## Pipeline

relative-entropy constrained E-step policy improvement와 supervised M-step projection을 번갈아 수행한다.

## Interface

replay trajectories와 critic estimates를 continuous stochastic policy update로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
