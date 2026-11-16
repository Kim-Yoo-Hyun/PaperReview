# RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

분산 평가자가 두 정책을 double-blind로 비교하고 선호 결과를 통합한다.

## Observation–State–Action Interface

같은 평가 상황의 두 정책 rollout → 선호 비교 → 전체 정책 순위.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: pairwise reset 조건, task 선택 편향, 선호 aggregation과 불확실성.

Source가 명시한 evaluation 범위: DROID 플랫폼을 사용하는 여러 기관에서 generalist policy를 실로봇으로 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

정책과 예산을 고정하고 기관/과제별 순위 및 leave-one-site-out 안정성을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/atreya25a.html) · [저자 project/code](https://robo-arena.github.io/) · [공식 code](https://github.com/pranavatreya/roboarena_backend). 수식·세부 구현·코드 실행은 미검증이다.
