# Mechanistic Interpretability for Steering Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

VLA 내부 표현을 이해하고 실행 중 행동을 조절하는 수단이 부족하다.

## Bottleneck and Changed Formulation

Transformer activation의 semantic 방향을 찾고 inference 때 activation steering으로 행동을 조절한다.

## System and Robotics Loop

VLA 내부 activation·semantic 방향 → 개입된 action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

방향 추출 데이터, 개입 강도, 속도와 성공의 trade-off.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Pi0·OpenVLA를 LIBERO 및 UR5에서 평가한다고 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/haon25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
