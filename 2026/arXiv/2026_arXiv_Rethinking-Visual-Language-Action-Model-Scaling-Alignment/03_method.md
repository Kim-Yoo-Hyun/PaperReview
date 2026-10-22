# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

EEF-relative 정렬·embodiment mixture·regularization을 통제 비교하고 평가자 편향 통제를 제안한다.

## Observation–State–Action Interface

이종 robot demonstration → 정렬된 action 표현 → VLA.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: EEF frame, normalization, split, grouped blind protocol.

Source가 명시한 evaluation 범위: Simulation과 real-robot 평가에서 데이터 혼합과 negative transfer를 분석한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 sample 수·embodiment 비율·blind evaluation로 혼합 전후를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2602.09722). 수식·세부 구현·코드 실행은 미검증이다.
