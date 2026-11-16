# Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Adaptive conformal prediction의 불확실성을 관측에 넣고 constrained RL로 행동을 조절한다.

## Observation–State–Action Interface

Pedestrian 예측·uncertainty → navigation policy → 이동 행동.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 보장의 단위, reactive crowd, calibration update와 intervention 비용.

Source가 명시한 evaluation 범위: 속도·행동 정책·집단 변화 및 실로봇 군중 navigation을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 scene에서 보정 유무를 비교하고 collision·진행·coverage를 함께 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/yao25a.html). 수식·세부 구현·코드 실행은 미검증이다.
