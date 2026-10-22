# Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

이질적인 속도·길이의 행동을 고정 시간격자에 표현하는 한계를 다룬다.

## Bottleneck and Changed Formulation

연속 spline action curve와 적응 길이 표현을 사용한다.

## System and Robotics Loop

관측·지시 → action curve → 실행 시 sampling.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

spline fitting, horizon-matched 학습, controller tracking, code 공개 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation benchmark와 실제 long-horizon manipulation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.05230) · [저자 project/code](https://clementine24.github.io/Vela/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
