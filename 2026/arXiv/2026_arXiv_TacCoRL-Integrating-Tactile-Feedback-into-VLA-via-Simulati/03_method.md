# TacCoRL: Integrating Tactile Feedback into VLA via Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

촉각 VLA를 sim-real co-training으로 초기화하고 simulation RL과 실환경 supervised anchor로 개선한다.

## Observation–State–Action Interface

영상·언어·촉각 → VLA 행동; 배포 시 privileged simulation state를 쓰지 않는다고 보고한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 촉각 합성 정합성, real anchor 비용, 물리 변화별 분할.

Source가 명시한 evaluation 범위: 실제 양팔 접촉 과제로 전이를 평가한다. 실제 로봇 online RL을 사용한 결과와 구별한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 초기화·접촉 관측의 motion-only RL과 joint motion/gain RL을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.11743) · [저자 project/code](https://tac-corl.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
