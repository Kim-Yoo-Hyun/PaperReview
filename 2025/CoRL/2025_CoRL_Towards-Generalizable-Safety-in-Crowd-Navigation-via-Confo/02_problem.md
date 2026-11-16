# Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

군중 행동 분포가 바뀌면 학습된 navigation policy 안전성이 저하될 수 있다.

## Bottleneck and Changed Formulation

Adaptive conformal prediction의 불확실성을 관측에 넣고 constrained RL로 행동을 조절한다.

## System and Robotics Loop

Pedestrian 예측·uncertainty → navigation policy → 이동 행동.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

보장의 단위, reactive crowd, calibration update와 intervention 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

속도·행동 정책·집단 변화 및 실로봇 군중 navigation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/yao25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
