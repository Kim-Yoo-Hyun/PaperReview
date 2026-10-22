# Memory Anchors for Continual Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

겹치는 latent representation에서 요구 action이 충돌하는 memory를 replay anchor로 사용한다.

## Observation–State–Action Interface

현재/과거 sample의 representation·action → replay 선택 → policy update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: latent layer, action normalization, task order, replay step scaling.

Source가 명시한 evaluation 범위: LIBERO와 real-robot continual learning 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 replay budget에서 uniform·MIR·anchor selection의 old/new task 성능을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=dSbtHPqFj9) · [저자 project/code](https://robot-adaptation.github.io/MemoryAnchors). 수식·세부 구현·코드 실행은 미검증이다.
