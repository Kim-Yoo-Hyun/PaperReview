# General agents need world models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

일반화 가능한 정책에서 예측 world model을 추출할 수 있음을 이론적으로 분석한다.

## Observation–State–Action Interface

다양한 목표를 수행하는 policy → 추출 가능한 환경 예측 model.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 일반화·목표 집합 정의, 추출 접근 권한, 정리 조건과 실제 로봇 적용 범위.

Source가 명시한 evaluation 범위: 공식 abstract는 다단계 목표·성능과 모델 정확도의 이론적 관계를 제시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

유한 환경에서 theorem 가정을 먼저 고정하고 policy-derived prediction과 별도 모델을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v267/richens25a.html). 수식·세부 구현·코드 실행은 미검증이다.
