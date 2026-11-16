# Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시각 verifier가 후보 행동을 선택하고 검증된 rollout을 후속 정책 학습에 사용한다.

## Observation–State–Action Interface

기존 정책의 행동 후보 → gradient-free 시각 검증 → 실행·재학습 데이터.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: verifier 오류와 성공 판정의 독립성, fine-tuning objective, 인간 개입의 집계 범위.

Source가 명시한 evaluation 범위: SIMPLER와 실제 DROID setup에서 steering 및 offline 개선을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

후보 수·verifier 비용·수집 예산을 맞춰 원 정책, 선택만, 선택 데이터 모방, RL을 대조한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p079.html). 수식·세부 구현·코드 실행은 미검증이다.
