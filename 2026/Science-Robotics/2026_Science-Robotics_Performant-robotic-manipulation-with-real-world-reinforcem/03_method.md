# Performant robotic manipulation with real-world reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Diffusion visuomotor policy의 imitation-to-RL 학습과 빠른 controller 실행을 연결하는 real-world RL framework를 제안한다.

## Observation–State–Action Interface

Visual observation → diffusion/flow visuomotor policy → robot action; offline/online 학습과 deployment 추론을 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Evaluation success denominator, human intervention, offline/online 단계 및 distillation 손실.

Source가 명시한 evaluation 범위: 저자 공식 repository와 저널 abstract는 pushing, pouring, cloth/long-horizon manipulation 등을 포함한 실제 robot 평가를 설명한다. 프로토콜별 수치는 본문 확인 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

하나의 manipulation task에서 BC, RL 후 policy, 가속 policy를 비교하고 success·cycle time·reset/intervention 비용을 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1126/scirobotics.aed6267) · [저자 project/code](https://github.com/Lei-Kun/RL-100). 수식·세부 구현·코드 실행은 미검증이다.
