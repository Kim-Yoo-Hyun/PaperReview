# Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Trajectory history를 instrumental variable로 이용하는 conditional moment 기반 DML-IL을 제안한다.

## Observation–State–Action Interface

expert trajectory history → instrumental-variable regression → imitation policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: instrument relevance/exclusion, 시간적 confounding, history 접근, imitation-gap 가정.

Source가 명시한 evaluation 범위: MuJoCo를 포함한 연속 상태·행동 환경에서 causal IL baseline과 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

History의 instrument 유효성만 바꾼 환경에서 BC·memory BC·DML-IL을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html). 수식·세부 구현·코드 실행은 미검증이다.
