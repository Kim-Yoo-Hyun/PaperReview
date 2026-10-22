# SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

위험한 VLA 실행을 감지해 rollback으로 복구한다.

## Bottleneck and Changed Formulation

시각·proprioception 기반 위험 예측과 no-op/rollback 개입을 결합한다.

## System and Robotics Loop

관측·시간 context → risk → 실행 중단/역행.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

joint history와 world state 구분, detector labels, collision 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO 및 실제 manipulation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.26313) · [저자 project/code](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop). Exact objective, constraints, success definition은 본문 수동 확인 필요.
