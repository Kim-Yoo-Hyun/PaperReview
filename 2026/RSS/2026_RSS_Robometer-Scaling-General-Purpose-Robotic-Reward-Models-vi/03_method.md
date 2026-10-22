# Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Progress supervision과 trajectory comparison을 결합한다.

## Observation–State–Action Interface

영상 trajectory·비교 정보 → progress/reward.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: policy version chronology, failure labels, reward training 중복, calibration.

Source가 명시한 evaluation 범위: 대규모 multi-robot 자료와 downstream 실제 robot RL을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 frozen policy rollout에서 progress/reward와 독립 outcome을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p140.html) · [저자 project/code](https://robometer.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
