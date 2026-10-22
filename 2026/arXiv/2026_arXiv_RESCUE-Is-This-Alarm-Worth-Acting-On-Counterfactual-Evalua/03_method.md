# RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Counterfactual continuation branch로 monitor의 intervention utility와 비용을 평가한다.

## Observation–State–Action Interface

동일 sim/policy state·alarm → 여러 continuation → outcome 비교.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: state clone 완전성, policy memory, oracle 개입, 실환경 적용 범위.

Source가 명시한 evaluation 범위: LIBERO Spatial Plus와 VLA runtime monitor 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 failure onset에서 continue/hold/개입을 branch해 비용 포함 outcome을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.13516). 수식·세부 구현·코드 실행은 미검증이다.
