# TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Wrench-aware VLA의 reference를 online RL 모듈로 보정하고 human intervention 경계를 critic 학습에 반영한다.

## Observation–State–Action Interface

촉각 유래 wrench·상태 → reference action/future wrench → 실행 행동 보정.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 개입 전후 critic mask, latency, base/보정 정책 학습 범위.

Source가 명시한 evaluation 범위: 실제 latch·컵·달걀 조작의 부분/전체 과제와 시간 제한 효율을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 접촉 관측에서 단일 actor와 frozen-prior 보정을 비교하고 개입 비용을 별도 집계한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.09337) · [저자 project/code](https://torl-vla.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
