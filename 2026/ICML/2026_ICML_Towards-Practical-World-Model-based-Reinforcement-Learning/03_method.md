# Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Unified multimodal model 기반 dynamics, interleaved multi-view decoding 및 chunk-level branched rollout을 결합한다.

## Observation–State–Action Interface

Multi-view observation + VLA action chunk → imagined next observation/reward → RL update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Multi-view conditioning, rollout branching state 분포, reward model과 실제 transfer 검증.

Source가 명시한 evaluation 범위: 공식 ICML abstract는 simulation과 real-world task에서 policy 성능 및 sample efficiency 평가를 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 world model과 policy에서 long rollout과 chunk-level branched rollout을 비교해 model error·real success·interaction 비용을 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26ez.html) · [저자 project/code](https://github.com/LAMDA-RL/VLA-MBPO). 수식·세부 구현·코드 실행은 미검증이다.
