# FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

가중치·feature·gradient norm을 제한하고 병렬 데이터와 replay coverage를 확대한다.

## Observation–State–Action Interface

상태 또는 시각 관측 → SAC 행동; replay 기반 가치 학습.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 상태/vision별 계산량, update-to-data 비율, 실제 로봇 전이 범위.

Source가 명시한 evaluation 범위: 여러 simulator의 제어 과제와 실제 humanoid sim-to-real을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

하나의 조작 환경에서 replay coverage와 norm 제한을 분리하고 sample·wall-clock 비용을 함께 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p099.html) · [저자 project/code](https://github.com/Holiday-Robot/FlashSAC). 수식·세부 구현·코드 실행은 미검증이다.
