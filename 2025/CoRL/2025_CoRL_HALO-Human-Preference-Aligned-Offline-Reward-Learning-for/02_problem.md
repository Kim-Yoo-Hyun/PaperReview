# HALO : Human Preference Aligned Offline Reward Learning for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

항법 경로의 인간 선호를 단순 성공 보상으로 표현하기 어렵다.

## Bottleneck and Changed Formulation

Expert 행동 주변 후보의 선호 순위를 학습해 시각 reward를 구성한다.

## System and Robotics Loop

자아시점 영상·행동 후보 → 선호 보상 → offline 정책 또는 MPC.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

선호 query 생성·annotation 비용, 후보 sampling 분포, offline/online 데이터 경계.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 Clearpath Husky 항법에서 성공·경로 특성을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/seneviratne25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
