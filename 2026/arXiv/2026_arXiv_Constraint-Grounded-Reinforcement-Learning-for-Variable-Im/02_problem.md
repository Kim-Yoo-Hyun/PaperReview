# Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

삽입의 force limit과 controller gain이 달라질 때 수동 재조정이 필요하다.

## Bottleneck and Changed Formulation

Force-limit 조건부 RL이 motion·insertion rate·gain을 요청하고 controller가 gain 범위로 투영한다.

## System and Robotics Loop

접촉 feedback·force limit → residual motion·속도·요청 gain.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Projection과 actor 범위, force constraint의 경험적/형식적 보장 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulated oblique insertion을 평가한다. Gain 범위 보장과 force-limit 경험적 만족은 구별한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.13516). Exact objective, constraints, success definition은 본문 수동 확인 필요.
