# JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

미분 가능한 soft-body 모델·EKF 추정과 정보 이득/안전 비용을 고려한 능동 조작을 결합한다.

## Observation–State–Action Interface

Stereo 관측·조작 → attachment 추정 → sensing action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 재료 모델과 attachment 가정, 안전 비용 정의.

Source가 명시한 evaluation 범위: 실제 동물 조직의 부착점과 cutting/suturing 변화 실험을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

정보 이득 probe와 단순 displacement probe를 task outcome으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss20/p007.html). 수식·세부 구현·코드 실행은 미검증이다.
