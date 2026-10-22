# CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

계획과 action safety/recovery의 dual-loop 구조를 frozen VLA에 결합한다.

## Observation–State–Action Interface

사용자·scene context → 계획 → VLA·shield·recovery.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 메모리 입력, failure detector, recovery 비용, 공개 구현 범위.

Source가 명시한 evaluation 범위: Simulation과 실제 robot assistance 결과를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 policy·정보·도구에서 planner와 shield를 하나씩 제거해 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.21453) · [저자 project/code](https://vincent2311.github.io/Projects/CarryOn/). 수식·세부 구현·코드 실행은 미검증이다.
