# Problem — Information Theoretic MPC for Model-Based Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2017 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, model predictive control, model-based RL, Planning
- Official paper: https://ieeexplore.ieee.org/document/7989202/
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; objective derivation and result magnitudes remain UNVERIFIED.

## Target Problem and Assumptions

비선형·비convex control 문제에서 dynamics model을 이용해 실시간 action sequence를 최적화한다.

## Closed-Loop Position

current state와 dynamics model을 짧은 horizon action sequence와 첫 control action으로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
