# SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시각·proprioception 기반 위험 예측과 no-op/rollback 개입을 결합한다.

## Observation–State–Action Interface

관측·시간 context → risk → 실행 중단/역행.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: joint history와 world state 구분, detector labels, collision 비용.

Source가 명시한 evaluation 범위: LIBERO 및 실제 manipulation을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 event 이후 continue·hold·rollback의 실제 object/task 상태를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.26313) · [저자 project/code](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop). 수식·세부 구현·코드 실행은 미검증이다.
