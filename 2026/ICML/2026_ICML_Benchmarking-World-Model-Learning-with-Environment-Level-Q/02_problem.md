# Benchmarking World-Model Learning with Environment-Level Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

단일 rollout의 예측이나 return만으로 환경 전반을 이해했는지 판단하기 어렵다.

## Bottleneck and Changed Formulation

도달 가능성·개입 결과 같은 environment-level query를 평가하는 WorldTest를 제안한다.

## System and Robotics Loop

환경 상호작용 → 학습된 model/belief → 여러 유형의 환경 질의.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

query 정답 접근, exploration budget, 환경 생성 분할, robot task로의 전이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

AutumnBench grid-world에서 사람과 학습 agent를 비교한다. 실로봇 평가는 아니다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/warrier26a.html) · [저자 project/code](https://zenodo.org/records/19498269). Exact objective, constraints, success definition은 본문 수동 확인 필요.
