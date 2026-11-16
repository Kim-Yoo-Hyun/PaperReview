# Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Offline RL 사전학습과 지속적인 자율 운영·online 적응을 하나의 항법 학습 시스템으로 구성한다.

## Observation–State–Action Interface

시각 관측·항법 목표 → 정책 행동 → 실제 배포 데이터 → 정책 갱신.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 목표 생성·reset·인간 개입의 범위, 정책 입력의 언어 여부, 이전 장소 회귀.

Source가 명시한 evaluation 범위: 실세계 open-world 항법 배포에서 자율 수집 데이터로 적응하는 시스템을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 사전학습 정책에서 offline 고정·최근 데이터 모방·online RL을 비교하고 이전 장소를 재평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/stachowicz25a.html) · [저자 project/code](https://github.com/kylestach/lifelong-nav-rl). 수식·세부 구현·코드 실행은 미검증이다.
