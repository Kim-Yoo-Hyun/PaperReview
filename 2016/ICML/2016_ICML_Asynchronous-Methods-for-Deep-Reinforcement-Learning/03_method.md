# Method — Asynchronous Methods for Deep Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2016 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, actor-critic, A3C
- Official paper: https://proceedings.mlr.press/v48/mniha16.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; implementation and result magnitudes remain UNVERIFIED.

## Pipeline

여러 asynchronous actor-learners가 shared parameters에 policy/value gradients를 적용한다.

## Interface

parallel environment trajectories를 shared actor-critic policy update로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
