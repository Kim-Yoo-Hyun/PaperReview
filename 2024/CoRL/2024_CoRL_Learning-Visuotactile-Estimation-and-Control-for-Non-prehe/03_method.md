# Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Simulation interaction으로 visuotactile estimator를 학습하고 불확실성을 정책에 연결한다.

## Observation–State–Action Interface

시각·촉각 → 추정 상태/불확실성 → uncertainty-aware control.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: privileged training input, tactile modality, occlusion 분포, estimator와 policy ablation.

Source가 명시한 evaluation 범위: 비파지 manipulation의 가림 조건과 실로봇 sim-to-real을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 estimator에서 uncertainty 입력만 제거하고 occlusion 조건별 제어 실패를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/ferrandis25a.html). 수식·세부 구현·코드 실행은 미검증이다.
