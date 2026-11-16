# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

짧은 실환경 스캔으로 시뮬레이터를 만들고 simulation co-training으로 잔여 차이를 줄인다.

## Observation–State–Action Interface

실환경 영상 → 재구성 환경 → generalist 정책 평가.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 평가 전에 허용된 co-training 데이터, 독립 실환경 trial, 장면 선택 편향.

Source가 명시한 evaluation 범위: 실제·시뮬레이션의 짝지은 rollout으로 정책 순위 상관을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 checkpoint들을 동일 task의 실환경·재구성 환경에서 비교하고 co-training 전후 순위를 별도로 계산한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p062.html) · [저자 project/code](https://polaris-evals.github.io/) · [공식 code](https://github.com/arhanjain/PolaRiS). 수식·세부 구현·코드 실행은 미검증이다.
