# PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

여러 시간 granularity의 표현과 router로 적응형 temporal quantization을 구성한다.

## Observation–State–Action Interface

관측 → temporal 선택·action decoding → robot tracking.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: v2 controller 설정, router 비용, task별 gain, success/time denominator.

Source가 명시한 evaluation 범위: Simulation과 실제 manipulation에서 실행 효율·성능을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 controller gain·물리 시간 예산에서 고정/적응 granularity를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.25961) · [저자 project/code](https://pacevla.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
