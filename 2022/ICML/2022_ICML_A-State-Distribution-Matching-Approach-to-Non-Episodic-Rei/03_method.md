# A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시연 state 분포를 맞추는 backward policy로 task-relevant reset을 학습한다.

## Observation–State–Action Interface

Demonstration states → reset policy → forward learner.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: demonstration 접근, forward/backward budget, independent evaluation.

Source가 명시한 evaluation 범위: EARL의 sparse-reward continuous control task를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Reset 분포별 learning curve와 고정 평가 분포의 checkpoint 성능을 함께 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v162/sharma22a.html). 수식·세부 구현·코드 실행은 미검증이다.
