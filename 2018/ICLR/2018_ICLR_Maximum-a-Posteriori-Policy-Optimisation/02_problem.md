# Problem — Maximum a Posteriori Policy Optimisation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / ICLR
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning
- Official paper: https://openreview.net/forum?id=S1ANxQW0b
- Code/Project: not identified
- Source audit: official OpenReview abstract checked; derivation and experimental details remain UNVERIFIED.

## Target Problem and Assumptions

sample-efficient off-policy learning에서 large policy update가 만드는 instability를 제한한다.

## Closed-Loop Position

replay trajectories와 critic estimates를 continuous stochastic policy update로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
