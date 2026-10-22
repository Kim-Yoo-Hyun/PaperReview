# Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Action entropy를 이용해 추론 중 실행할 chunk 길이를 조정한다.

## Observation–State–Action Interface

VLA 예측 sample → uncertainty cue → 실행 길이 → 다음 관측.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: entropy 추정 sample 수, 최소 이동량, sensor/inference timing.

Source가 명시한 evaluation 범위: Simulation과 real-robot manipulation 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

고정/적응 horizon을 동일 wall-clock·관측 예산·controller에서 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2604.04161) · [저자 project/code](https://lance-lot.github.io/adaptive-chunking.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
