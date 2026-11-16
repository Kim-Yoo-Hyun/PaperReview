# Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

SO-101의 공간 지시 과제에서 익숙한 객체·개념·행동을 유지한 배치 변화와 직접 지시·표현·무행동 진단을 비교한다.

## Observation–State–Action Interface

실제 로봇의 관측·공간 언어 지시 → VLA 행동 → 목표별 채점. Counting과 no-action을 별도 진단으로 포함한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: ID/OOD support, 모델별 완료 범위와 trial 분모, 직접 지시의 정보량, 최종 수량·무행동 채점, 공개 data/코드의 실제 가용 범위.

Source가 명시한 evaluation 범위: 저자는 여섯 tabletop task와 여러 VLA의 실제 rollout을 보고한다. 전체 protocol을 수행한 모델과 부분 baseline이 다르므로 분모를 섞지 않는다. 공개 project의 model/data 링크는 확인했으나 독립 실행 code URL은 확인하지 못했다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

현재 SET의 D/R 설계와 Counting 평가 정의를 먼저 맞춘다. SO-101 결과를 VLABench simulator의 결과로 대체하지 않으며 실제 실행은 별도 조건을 따른다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.12696) · [저자 project/code](https://justintiensmith.github.io/Spa-Bench/). 수식·세부 구현·코드 실행은 미검증이다.
