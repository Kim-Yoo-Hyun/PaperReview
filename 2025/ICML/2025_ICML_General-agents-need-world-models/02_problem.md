# General agents need world models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

다단계 목표 일반화에 환경 예측 모델이 필요한지 형식적으로 묻는다.

## Bottleneck and Changed Formulation

일반화 가능한 정책에서 예측 world model을 추출할 수 있음을 이론적으로 분석한다.

## System and Robotics Loop

다양한 목표를 수행하는 policy → 추출 가능한 환경 예측 model.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

일반화·목표 집합 정의, 추출 접근 권한, 정리 조건과 실제 로봇 적용 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract는 다단계 목표·성능과 모델 정확도의 이론적 관계를 제시한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v267/richens25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
