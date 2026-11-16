# VLA-R1: Enhancing Reasoning in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

CoT 데이터와 region alignment·trajectory consistency·format reward를 사용한 GRPO 후학습을 결합한다.

## Observation–State–Action Interface

시각·지시 → affordance region·trajectory와 reasoning → downstream robot control. 직접 joint action 최적화와 구분한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: annotation 접근, downstream controller의 역할, execution feedback 사용 범위.

Source가 명시한 evaluation 범위: In/out-of-domain, simulation과 실로봇 평가를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 supervision에서 SFT/RLVR를 비교하고 trajectory 지표와 실행 성공을 함께 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.01623) · [저자 project/code](https://gigaai-research.github.io/VLA-R1/) · [공식 code](https://github.com/GigaAI-research/VLA-R1). 수식·세부 구현·코드 실행은 미검증이다.
