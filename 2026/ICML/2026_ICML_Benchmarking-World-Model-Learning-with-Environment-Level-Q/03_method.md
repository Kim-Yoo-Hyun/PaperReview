# Benchmarking World-Model Learning with Environment-Level Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

도달 가능성·개입 결과 같은 environment-level query를 평가하는 WorldTest를 제안한다.

## Observation–State–Action Interface

환경 상호작용 → 학습된 model/belief → 여러 유형의 환경 질의.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: query 정답 접근, exploration budget, 환경 생성 분할, robot task로의 전이.

Source가 명시한 evaluation 범위: AutumnBench grid-world에서 사람과 학습 agent를 비교한다. 실로봇 평가는 아니다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

공유 rollout으로 구별 불가능한 환경 쌍을 만들고 추가 관측·query별 식별성을 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/warrier26a.html) · [저자 project/code](https://zenodo.org/records/19498269). 수식·세부 구현·코드 실행은 미검증이다.
