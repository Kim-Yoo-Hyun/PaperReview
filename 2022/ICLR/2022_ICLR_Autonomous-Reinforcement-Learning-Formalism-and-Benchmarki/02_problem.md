# Autonomous Reinforcement Learning: Formalism and Benchmarking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Human reset에 의존하는 episodic RL을 연속적으로 변하는 환경의 자율 학습으로 확장한다.

## Bottleneck and Changed Formulation

Autonomous RL formalism과 최소 개입을 평가하는 EARL benchmark를 제안한다.

## System and Robotics Loop

연속 환경 상호작용·개입 budget → 학습 policy → 별도 평가.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

reset 정의, intervention 비용, 평가 rollout의 학습 유입, denominator.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

다양한 simulated task에서 reset 의존성과 기존 방법 한계를 분석한다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=nkaba3ND7B5). Exact objective, constraints, success definition은 본문 수동 확인 필요.
