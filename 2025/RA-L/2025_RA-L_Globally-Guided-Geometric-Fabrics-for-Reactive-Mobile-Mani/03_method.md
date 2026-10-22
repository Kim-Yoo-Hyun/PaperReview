# Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

최적화 planner와 reactive geometric fabrics를 결합하고 대체 목표 pose를 탐색한다.

## Observation–State–Action Interface

Robot/환경 state → global guidance → reactive whole-body motion.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: object pose 가용성, collision geometry, 목표 pose 자유도, 계산 예산.

Source가 명시한 evaluation 범위: 다중 mobile manipulator의 simulation 및 실제 실험을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

장애물로 기존 grasp가 막힌 한 task에서 대체 pose planner와 VLA 선택을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1109/LRA.2025.3562005) · [저자 project/code](https://autonomousrobots.nl/paper_websites/g3f). 수식·세부 구현·코드 실행은 미검증이다.
