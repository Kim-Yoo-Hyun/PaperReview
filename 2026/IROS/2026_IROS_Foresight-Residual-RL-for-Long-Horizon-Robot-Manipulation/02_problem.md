# Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

각 subtask의 국소 성공이 후속 task 성공으로 이어지지 않을 수 있다.

## Bottleneck and Changed Formulation

Downstream rollout의 성공 예측을 terminal-state 평가에 사용해 residual RL을 연결한다.

## System and Robotics Loop

VLA 행동·종료 state → 미래 성공 예측 → residual policy 학습.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

stage 경계, privileged state, backward training 순서, 실제 robot 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation의 여러 단계 manipulation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2607.16506) · 저자 프로젝트·코드 주소 미확인. Exact objective, constraints, success definition은 본문 수동 확인 필요.
