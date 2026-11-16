# GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Gaussian radiance field와 differentiable dynamics를 이용한 학습에 VLM·mixture-of-experts를 결합한다.

## Observation–State–Action Interface

시각·언어 → VLA navigation/control; rendering과 dynamics gradient를 학습에 활용한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 언어 encoder·MoE 갱신 범위, dynamics model 오차, 이전 GRaD-Nav 대비 새 평가 범위.

Source가 명시한 evaluation 범위: Simulation과 실제 드론의 언어 조건부 navigation을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 scene·언어·action으로 differentiable learning과 model-free RL을 비교하고 실제 전이를 분리 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11297793/) · [저자 project/code](https://qianzhong-chen.github.io/gradnavpp.github.io/) · [공식 code](https://github.com/Qianzhong-Chen/grad_nav). 수식·세부 구현·코드 실행은 미검증이다.
