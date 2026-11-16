# Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

지시 재표현과 action sample을 함께 확장하고 contrastive verifier로 prompt·action을 선택한다.

## Observation–State–Action Interface

VLM instruction rephrasing → VLA action candidates → verifier selection; 계층형 test-time pipeline.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 재표현의 의미 보존, verifier 감독량, rollout-independent evaluation.

Source가 명시한 evaluation 범위: SIMPLER·PolaRiS와 실로봇의 in/out-of-distribution 지시 실행을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 backbone·데이터에 candidate 수와 verifier 비용을 포함한 성능/latency 곡선을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2602.12281) · [저자 project/code](https://cover-vla.github.io/) · [공식 code](https://github.com/cover-vla/cover-vla). 수식·세부 구현·코드 실행은 미검증이다.
