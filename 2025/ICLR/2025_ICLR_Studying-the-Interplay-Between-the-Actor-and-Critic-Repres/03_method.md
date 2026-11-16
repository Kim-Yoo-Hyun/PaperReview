# Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

공유/분리 표현과 각 역할의 전문화를 비교한다. 별도 critic은 탐색과 수집 데이터에도 영향을 준다고 보고한다.

## Observation–State–Action Interface

고차원 관측 → actor 행동·critic 가치 추정의 on-policy 학습.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 환경별 capacity·optimizer·data collection 통제, VLA에 그대로 적용 가능한 결론의 범위.

Source가 명시한 evaluation 범위: 공식 abstract의 표현·downstream 성능 비교까지 확인. 세부 환경·seed·수치·모델 용량 통제는 본문 대조 필요.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 초기 정책·고정 old log-prob/return/advantage의 단일 update 진단과 각 조건의 on-policy 학습을 별도로 평가한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) · [저자 project/code](https://github.com/francelico/deac-rep). 수식·세부 구현·코드 실행은 미검증이다.
