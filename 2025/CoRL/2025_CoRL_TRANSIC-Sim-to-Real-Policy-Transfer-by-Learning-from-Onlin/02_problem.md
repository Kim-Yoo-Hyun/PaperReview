# TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Simulation 정책은 모델에 없는 실환경 차이를 모두 다루기 어렵다.

## Bottleneck and Changed Formulation

사람의 online correction으로 residual policy를 학습해 simulation 정책과 결합한다.

## System and Robotics Loop

point-cloud 기반 base policy + 인간 correction으로 학습한 residual → 실행 action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

개입 시점/시간 비용, residual 제어 권한, correction과 평가 분할.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

가구 조립 등 실로봇 접촉 조작의 sim-to-real 전이를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/jiang25a.html) · [저자 project/code](https://transic-robot.github.io/) · [공식 code](https://github.com/transic-robot/transic). Exact objective, constraints, success definition은 본문 수동 확인 필요.
