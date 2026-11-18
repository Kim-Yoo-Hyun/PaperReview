# Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

완성 shape에서 affordance 가설을 만들고 entropy 감소·실제 관측 검증을 함께 고려해 다음 시점을 정한다.

## Observation–State–Action Interface

부분 관측·task → affordance 후보 → 카메라 시점 → functional grasp로 연결한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Shape hallucination·hypothesis weighting·view feasibility·stop threshold.

Source가 명시한 evaluation 범위: Simulation과 실제 cluttered scene의 기능적 grasp 및 NBV step을 평가한다. 전체 pouring/insertion 성공과 구별한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 visibility·pose 정보·budget에서 affordance verification과 후보별 task success를 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.23504). 수식·세부 구현·코드 실행은 미검증이다.
