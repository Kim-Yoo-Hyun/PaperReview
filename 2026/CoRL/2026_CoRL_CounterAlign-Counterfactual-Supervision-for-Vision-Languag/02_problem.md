# CounterAlign: Counterfactual Supervision for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA가 언어 지시 대신 시각적 shortcut을 따르는 문제를 다룬다.

## Bottleneck and Changed Formulation

Instruction mismatch를 counterfactual supervision으로 사용해 reward/정책을 정렬한다.

## System and Robotics Loop

관측·지시·mismatch negative → 학습 신호 → action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

negative validity, reward leakage, scene overlap, constraint label 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO 계열 instruction 평가와 실제 robot 결과를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=AY4totylcx). Exact objective, constraints, success definition은 본문 수동 확인 필요.
