# Marginal Policy Gradients: A Unified Family of Estimators for Bounded Action Spaces with Applications

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

변환 후 같은 실행 행동이 되는 action sample의 gradient 분산을 줄인다.

## Bottleneck and Changed Formulation

Marginal policy gradient family로 angular/clipped estimator를 통합한다.

## System and Robotics Loop

Raw action distribution → execution transform → marginal score.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

transform measurability, discrete/continuous 차이, action-slot weighting.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RTS와 navigation task 및 variance 분석을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=HkgqFiAcFm). Exact objective, constraints, success definition은 본문 수동 확인 필요.
