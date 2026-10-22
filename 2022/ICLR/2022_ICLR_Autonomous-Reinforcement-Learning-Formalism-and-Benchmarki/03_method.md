# Autonomous Reinforcement Learning: Formalism and Benchmarking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Autonomous RL formalism과 최소 개입을 평가하는 EARL benchmark를 제안한다.

## Observation–State–Action Interface

연속 환경 상호작용·개입 budget → 학습 policy → 별도 평가.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: reset 정의, intervention 비용, 평가 rollout의 학습 유입, denominator.

Source가 명시한 evaluation 범위: 다양한 simulated task에서 reset 의존성과 기존 방법 한계를 분석한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 checkpoint를 continuing rollout과 독립 시작 분포에서 따로 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=nkaba3ND7B5). 수식·세부 구현·코드 실행은 미검증이다.
