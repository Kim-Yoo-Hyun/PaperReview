# Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

ManiSkill 기반 다중 morphology task로 in/out-of-domain policy 평가를 구성한다.

## Observation–State–Action Interface

Task·robot morphology·분포 변화 → ACT/π0.5 등 policy → task 성능.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: morphology별 action/control 정렬, task split과 simulator-real 대응.

Source가 명시한 evaluation 범위: 28 task·두 robot morphology와 simulation/real-world 지표 상관을 abstract에서 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 task pair에서 morphology와 시각 perturbation을 분리해 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2605.27759). 수식·세부 구현·코드 실행은 미검증이다.
