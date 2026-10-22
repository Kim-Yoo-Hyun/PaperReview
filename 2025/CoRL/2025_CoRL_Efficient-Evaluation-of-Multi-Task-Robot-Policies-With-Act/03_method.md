# Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

비용을 고려한 active experiment selection과 task/policy 정보를 활용한다.

## Observation–State–Action Interface

Policy·task·prior·관측 결과 → 다음 평가 선택.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: prior 언어 정보, 관측 noise, offline matrix와 실제 online 실행 차이.

Source가 명시한 evaluation 범위: 실제 및 simulated 평가 자료를 이용한 효율 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 task-policy matrix와 cost ledger로 uniform/active selection을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/anwar25a.html). 수식·세부 구현·코드 실행은 미검증이다.
