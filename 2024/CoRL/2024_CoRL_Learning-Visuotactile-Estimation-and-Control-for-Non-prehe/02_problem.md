# Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

비파지 조작에서 가려진 물체의 상태와 접촉 불확실성을 함께 다뤄야 한다.

## Bottleneck and Changed Formulation

Simulation interaction으로 visuotactile estimator를 학습하고 불확실성을 정책에 연결한다.

## System and Robotics Loop

시각·촉각 → 추정 상태/불확실성 → uncertainty-aware control.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

privileged training input, tactile modality, occlusion 분포, estimator와 policy ablation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

비파지 manipulation의 가림 조건과 실로봇 sim-to-real을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/ferrandis25a.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
