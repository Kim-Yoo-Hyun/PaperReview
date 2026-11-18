# Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

물체 관계·task geometry의 알려진 제약을 shared-control template으로 표현해 RL이 탐색하는 차원을 줄인다.

## Observation–State–Action Interface

Template가 제한한 state/action 공간에서 unknown task knowledge를 학습한다. 단일 VLA 내부의 learned exploration은 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 수동 task constraint·phase 전환·안전 보증 전제·reward 정보.

Source가 명시한 evaluation 범위: 7-DoF 실제 로봇의 pouring·grid-clamp placement를 다룬다. 논문의 안전 주장 조건을 보편적 보증으로 일반화하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

고정 제약 template과 learned weighting에 동일 관계 정보·action budget을 제공한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/article/10.1007/s10514-024-10164-6). 수식·세부 구현·코드 실행은 미검증이다.
