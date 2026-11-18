# Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

기존 미분 가능한 state-based expert를 고정하고, 상태 supervision과 expert를 통과하는 action-consistency loss로 시각 추정기를 학습한다. Expert의 행동 매핑을 다시 모방하는 비용을 줄이는 formulation이다.

## Observation–State–Action Interface

영상 → 추정된 물리 상태 → 고정 expert → 로봇 행동. 추정기만 학습하며 VLA나 언어 조건 정책을 전제로 한 방법은 아니다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Expert의 미분 가능성·state/goal 정의·loss schedule·occlusion·held-out split·실제 로봇 trial 및 코드 release.

Source가 명시한 evaluation 범위: 초록은 goal-conditioned 조작 5개와 실제 Panda의 sim-to-real 평가를 보고한다. Trial 구성·각 조건별 성공 수·시연 분할은 이번 등록에서 확인하지 않았다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 estimator·expert·시연에서 state-only, action-consistency 혼합, task outcome supervision을 비교한다. 이는 제안이며 원 논문 결과가 아니다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.34018). 수식·세부 구현·코드 실행은 미검증이다.
