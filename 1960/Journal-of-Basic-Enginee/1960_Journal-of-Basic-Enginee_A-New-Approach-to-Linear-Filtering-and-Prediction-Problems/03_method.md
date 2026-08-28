# Method — A New Approach to Linear Filtering and Prediction Problems

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1960 / Journal of Basic Engineering
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, state estimation, Kalman Filter, Control
- Official paper: https://doi.org/10.1115/1.3662552
- Code/Project: not identified
- Source audit: publisher metadata and accessible paper summary checked; derivations remain UNVERIFIED.

## Pipeline

상태와 공분산의 prediction/update recursion으로 새 측정을 이전 추정과 결합한다.

## Interface

control/transition model과 sensor observation을 belief mean·covariance로 변환하는 state-estimation 계층이다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
