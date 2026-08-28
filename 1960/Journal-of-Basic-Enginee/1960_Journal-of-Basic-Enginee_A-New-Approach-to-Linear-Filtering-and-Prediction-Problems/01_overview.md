# A New Approach to Linear Filtering and Prediction Problems

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1960 / Journal of Basic Engineering
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, state estimation, Kalman Filter, Control
- Official paper: https://doi.org/10.1115/1.3662552
- Code/Project: not identified
- Source audit: publisher metadata and accessible paper summary checked; derivations remain UNVERIFIED.

## Why This Paper Is Here

부분 관측 하의 recursive state estimation을 이해하는 핵심 기반으로, SLAM·tracking·model-based control의 공통 prerequisite다.

## Problem

선형 동역학과 noisy observation에서 latent state의 최소분산 추정과 예측을 순차적으로 갱신하는 문제를 다룬다.

## Core Idea

상태와 공분산의 prediction/update recursion으로 새 측정을 이전 추정과 결합한다.

## Interface

control/transition model과 sensor observation을 belief mean·covariance로 변환하는 state-estimation 계층이다.

## Evaluation Scope

수학적 유도와 예시가 중심이며 현대 robotics task의 downstream control 평가는 없다.
