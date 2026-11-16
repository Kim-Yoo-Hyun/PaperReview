# General Process Reward Modeling for Robotic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

다시점 step-aware 보상 모델과 policy-invariant reward shaping을 제안한다.

## Observation–State–Action Interface

다시점 관측·과제 진행 → dense reward → robot RL.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 보존 정리의 가정, 종료 처리, multi-view 특권, task별 추가 시연.

Source가 명시한 evaluation 범위: Simulation·실제 조작에서 reward 평가와 policy 학습을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

보상 오류를 독립 측정하고 sparse-only, 직접 dense, invariant shaping을 같은 rollout budget으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) · [저자 project/code](https://robo-dopamine.github.io/) · [공식 code](https://github.com/FlagOpen/Robo-Dopamine). 수식·세부 구현·코드 실행은 미검증이다.
