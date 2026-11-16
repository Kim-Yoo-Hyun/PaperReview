# Enhancing Tactile-based Reinforcement Learning for Robotic Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

희소 이진 접촉·proprioception 표현을 self-supervised learning으로 학습하고 SSL memory와 on-policy memory의 분리를 검토한다.

## Observation–State–Action Interface

Binary contact·proprioception → 표현/memory → contact-rich control.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 센서 노이즈·빈도, sim contact의 현실성, 실물 센서 전이.

Source가 명시한 evaluation 범위: RoTO 시뮬레이션의 공 튀기기·Baoding 회전 등 dexterity를 평가한다. 실로봇 결과로 확대하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 제어기에서 contact 유무와 SSL memory 공유/분리를 교차 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) · [저자 project/code](https://elle-miller.github.io/tactile_rl/) · [공식 code](https://github.com/elle-miller/roto). 수식·세부 구현·코드 실행은 미검증이다.
