# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Temporal·spatial·object·procedural memory task와 여러 memory-augmented VLA를 비교한다.

## Observation–State–Action Interface

현재 관측·history representation → π0.5 기반 VLA → manipulation action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: task dictionary와 goal/evaluator, history cutoff, raw ID와 split.

Source가 명시한 evaluation 범위: 16 manipulation task와 14 memory variant를 보고하며 memory 효용은 task에 의존한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

먼저 3개 planned fixture의 native 관측·goal 일치를 확인한다. 기존 N3-A 계약 PASS는 native 재현이 아니다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/dai26c.html) · [저자 project/code](https://robomme.github.io/) · [공식 code](https://github.com/RoboMME/robomme_benchmark). 수식·세부 구현·코드 실행은 미검증이다.
