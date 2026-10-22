# RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Failure alarm의 정확도만으로 실제 개입 가치를 알 수 없다.

## Bottleneck and Changed Formulation

Counterfactual continuation branch로 monitor의 intervention utility와 비용을 평가한다.

## System and Robotics Loop

동일 sim/policy state·alarm → 여러 continuation → outcome 비교.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

state clone 완전성, policy memory, oracle 개입, 실환경 적용 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO Spatial Plus와 VLA runtime monitor 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.13516). Exact objective, constraints, success definition은 본문 수동 확인 필요.
