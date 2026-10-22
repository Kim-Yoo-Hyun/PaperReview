# Measuring the Stability Assumption Behind Action Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Open-loop/closed-loop branch의 finite-horizon divergence를 비교한다.

## Observation–State–Action Interface

같은 초기 상태·action perturbation → rollout → divergence slope.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: norm 단위, perturbation 크기, branch 동치, 전역 안정성과의 차이.

Source가 명시한 evaluation 범위: GR00T manipulation task에서 chunk 안정성 가정의 차이를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Held-out perturbation·horizon에서 divergence와 success를 별도 검증한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.01626) · [저자 project/code](https://aryangoyal7.github.io/publication/2026-stability-action-chunking). 수식·세부 구현·코드 실행은 미검증이다.
