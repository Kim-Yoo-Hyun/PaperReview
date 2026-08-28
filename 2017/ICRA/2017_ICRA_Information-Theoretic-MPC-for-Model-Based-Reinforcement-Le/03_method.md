# Method — Information Theoretic MPC for Model-Based Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2017 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, model predictive control, model-based RL, Planning
- Official paper: https://ieeexplore.ieee.org/document/7989202/
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; objective derivation and result magnitudes remain UNVERIFIED.

## Pipeline

path-integral/information-theoretic 관점의 sampled trajectory weighting으로 receding-horizon control sequence를 갱신한다.

## Interface

current state와 dynamics model을 짧은 horizon action sequence와 첫 control action으로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
