# LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

센서·actuation·controller·기하 변화 축을 분리한 benchmark를 제안한다.

## Observation–State–Action Interface

Native VLA observation/action interface에 setup perturbation을 주입한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: native state 소비, fault axis와 onset, 공개 trial-level logs.

Source가 명시한 evaluation 범위: LIBERO 기반 여러 VLA와 hardware severity 조건을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 초기 상태에서 두 injection 경로를 독립 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.18843) · [저자 project/code](https://arxiv.org/abs/2610.18843). 수식·세부 구현·코드 실행은 미검증이다.
