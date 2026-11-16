# Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Force-limit 조건부 RL이 motion·insertion rate·gain을 요청하고 controller가 gain 범위로 투영한다.

## Observation–State–Action Interface

접촉 feedback·force limit → residual motion·속도·요청 gain.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Projection과 actor 범위, force constraint의 경험적/형식적 보장 차이.

Source가 명시한 evaluation 범위: Simulated oblique insertion을 평가한다. Gain 범위 보장과 force-limit 경험적 만족은 구별한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 controller projection에서 비-VLA와 VLA actor의 조건 전이를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.13516). 수식·세부 구현·코드 실행은 미검증이다.
