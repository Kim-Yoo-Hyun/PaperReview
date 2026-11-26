# PROSPECT: Unified Streaming Vision-Language Navigation via Semantic–Spatial Fusion and Latent Predictive Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

CUT3R 공간 표현과 SigLIP 의미 표현을 융합하고 학습 중 미래 2D·3D latent prediction을 보조 목표로 사용한다.

## Observation–State–Action Interface

단안 RGB 프레임과 언어 지시로 전진·회전·정지 행동을 예측한다. 미래 표현 예측 분기는 훈련 시에만 사용한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 미래 target 접근, inference 비용 산정, map/history memory 조건.

Source가 명시한 evaluation 범위: VLN-CE와 실제 항법을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 navigation backbone에서 fusion·prediction·RL을 구분한 ablation을 수행한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11673313/) · [저자 project/code](https://github.com/Debactor/PROSPECT). 수식·세부 구현·코드 실행은 미검증이다.
