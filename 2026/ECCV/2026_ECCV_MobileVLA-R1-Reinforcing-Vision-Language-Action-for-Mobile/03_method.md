# MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

구조화 CoT alignment 뒤 GRPO RL로 추론·제어 일관성을 학습한다.

## Observation–State–Action Interface

영상·지시 → reasoning과 navigation command/control output → quadruped execution. 출력 형식을 low-level motor torque와 혼동하지 않는다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 속도·이산 행동 output 형식, low-level controller 고정 여부, 2.0 코드와 원 논문 차이.

Source가 명시한 evaluation 범위: VLN·VLA benchmark와 실제 사족 로봇 배포를 보고한다. MobileVLA-R1 2.0의 추가 주장은 포함하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 navigation 경로에서 CoT-only, RL, reasoning 제거 대조를 수행한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2511.17889) · [저자 project/code](https://aigeeksgroup.github.io/MobileVLA-R1/) · [공식 code](https://github.com/AIGeeksGroup/MobileVLA-R1). 수식·세부 구현·코드 실행은 미검증이다.
