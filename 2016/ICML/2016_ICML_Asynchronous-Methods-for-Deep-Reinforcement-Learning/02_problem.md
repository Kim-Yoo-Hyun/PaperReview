# Problem — Asynchronous Methods for Deep Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2016 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, actor-critic, A3C
- Official paper: https://proceedings.mlr.press/v48/mniha16.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; implementation and result magnitudes remain UNVERIFIED.

## Target Problem and Assumptions

deep RL의 correlated data와 느린 training을 replay buffer 없이 완화한다.

## Closed-Loop Position

parallel environment trajectories를 shared actor-critic policy update로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
