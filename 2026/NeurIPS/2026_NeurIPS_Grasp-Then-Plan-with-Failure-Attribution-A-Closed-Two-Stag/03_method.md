# Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Grasp-then-plan 두 단계와 failure attribution을 연결한다.

## Observation–State–Action Interface

Grasp 후보 → 실행 계획 → 실패 원인 → 두 단계 개선.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: failure label 출처, planner 성공과 policy 성공 구분, code 공개.

Source가 명시한 evaluation 범위: Simulation과 실제 manipulation 및 여러 정책 계열 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 grasp 후보로 geometry-only ranking과 execution-outcome ranking을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.03385) · [저자 project/code](https://sites.google.com/view/gtp-fa/). 수식·세부 구현·코드 실행은 미검증이다.
