# Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

범용 정책의 혼합 품질 시연에는 더 나은 행동을 선별할 가치 정보가 부족하다.

## Bottleneck and Changed Formulation

Offline RL로 학습한 value를 사용하여 범용 정책이 생성한 행동 후보를 추론 시 선택한다.

## System and Robotics Loop

고정 정책의 action samples → 학습 value scoring → 실행 행동. 정책 가중치 갱신과 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

후보 수와 latency, value 데이터 범위, 정책별 action normalization.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

서로 다른 다섯 정책과 여러 실제 로봇·조작 과제에서 value guidance를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/nakamoto25a.html) · [저자 project/code](https://nakamotoo.github.io/V-GPS) · [공식 code](https://github.com/nakamotoo/V-GPS). Exact objective, constraints, success definition은 본문 수동 확인 필요.
