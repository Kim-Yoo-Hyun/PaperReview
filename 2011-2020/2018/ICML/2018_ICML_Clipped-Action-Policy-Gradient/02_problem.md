# Clipped Action Policy Gradient

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Action clipping을 무시한 policy gradient의 불필요한 분산을 줄인다.

## Bottleneck and Changed Formulation

실행 action이 clipping되는 사실을 이용한 unbiased estimator를 제안한다.

## System and Robotics Loop

Unbounded policy sample → clip → bounded executed action·gradient.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

clipping preimage, policy family, gradient unbiasedness 조건.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Continuous control의 이론·실험 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v80/fujita18a.html) · [저자 project/code](https://github.com/pfnet-research/capg). Exact objective, constraints, success definition은 본문 수동 확인 필요.
