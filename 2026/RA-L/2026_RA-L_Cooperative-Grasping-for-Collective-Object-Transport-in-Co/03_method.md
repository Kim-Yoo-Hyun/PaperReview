# Cooperative Grasping for Collective Object Transport in Constrained Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

환경·물체 조건을 반영하는 conditional embedding과 negative sampling으로 feasible grasp를 학습한다.

## Observation–State–Action Interface

환경/물체·grasp 정보 → embedding → 운반 가능 grasp 선택.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 환경 표현, label 생성 planner, two-robot 제약, 일반화 split.

Source가 명시한 evaluation 범위: Simulation과 실제 협동 object transport를 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Grasp 후보를 고정하고 transport feasibility selector와 nearest/simple planner 기준을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1109/LRA.2026.3653338). 수식·세부 구현·코드 실행은 미검증이다.
