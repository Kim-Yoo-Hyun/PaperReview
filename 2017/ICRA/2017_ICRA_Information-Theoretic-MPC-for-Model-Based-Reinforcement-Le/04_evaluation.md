# Evaluation — Information Theoretic MPC for Model-Based Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2017 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, model predictive control, model-based RL, Planning
- Official paper: https://ieeexplore.ieee.org/document/7989202/
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; objective derivation and result magnitudes remain UNVERIFIED.

## Protocol

aggressive autonomous driving/control 사례가 보고되며 hardware와 sampling 설정은 원문에서 확인한다.

## Limitations and Reproducibility

model bias, sample budget와 horizon에 민감하며 partial observability는 별도 estimator가 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
