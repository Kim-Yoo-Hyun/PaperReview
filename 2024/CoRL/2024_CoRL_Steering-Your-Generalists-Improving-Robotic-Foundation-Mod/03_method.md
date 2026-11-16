# Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Offline RL로 학습한 value를 사용하여 범용 정책이 생성한 행동 후보를 추론 시 선택한다.

## Observation–State–Action Interface

고정 정책의 action samples → 학습 value scoring → 실행 행동. 정책 가중치 갱신과 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 후보 수와 latency, value 데이터 범위, 정책별 action normalization.

Source가 명시한 evaluation 범위: 서로 다른 다섯 정책과 여러 실제 로봇·조작 과제에서 value guidance를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 데이터·critic·추론 계산량에서 고정 actor+reranking과 RL actor update를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/nakamoto25a.html) · [저자 project/code](https://nakamotoo.github.io/V-GPS) · [공식 code](https://github.com/nakamotoo/V-GPS). 수식·세부 구현·코드 실행은 미검증이다.
