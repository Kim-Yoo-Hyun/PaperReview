# StructRL: Structured Action-Space Exploration for Flow-Based VLAs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Flow 중간에 넣은 구조적 탐색 noise가 남은 denoising 과정에서 약해질 수 있다.

## Bottleneck and Changed Formulation

Deterministic ODE decoder 뒤 실행 action space에 구조적 noise를 넣고 last-step replay로 정책 갱신 신호를 구성한다.

## System and Robotics Loop

VLA flow decoder와 실행 행동의 stochasticity를 분리한다. 조건부 양팔 관계 학습의 선행 경계를 정한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Last-step likelihood 의미·noise covariance·중간 flow dilution 분석·코드 호환.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

초록은 로봇 조작의 online RL 탐색을 대상으로 한다. 이번 등록에서는 task별 수치·동일 compute 여부를 확정하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.15139). Exact objective, constraints, success definition은 본문 수동 확인 필요.
