# Problem — A New Approach to Linear Filtering and Prediction Problems

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1960 / Journal of Basic Engineering
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, state estimation, Kalman Filter, Control
- Official paper: https://doi.org/10.1115/1.3662552
- Code/Project: not identified
- Source audit: publisher metadata and accessible paper summary checked; derivations remain UNVERIFIED.

## Target Problem and Assumptions

선형 동역학과 noisy observation에서 latent state의 최소분산 추정과 예측을 순차적으로 갱신하는 문제를 다룬다.

## Closed-Loop Position

control/transition model과 sensor observation을 belief mean·covariance로 변환하는 state-estimation 계층이다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
