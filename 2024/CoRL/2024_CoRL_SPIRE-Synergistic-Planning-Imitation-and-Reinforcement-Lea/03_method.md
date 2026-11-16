# SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

TAMP로 작은 학습 문제를 만들고 planning context에 맞춘 IL·RL 학습을 결합한다.

## Observation–State–Action Interface

상위 task/motion plan → 학습 하위 정책 → 접촉 조작; 계층형 경계를 유지한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: planner의 상태·기하 접근, 하위 문제 성공 분포, 실로봇 평가 범위.

Source가 명시한 evaluation 범위: 장기·접촉 중심 조작 문제 집합에서 planning·IL·RL 결합 시스템들을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 과제·reset·데모 예산으로 planning scaffold의 유무를 대조하고 전체 성공과 개입 비용을 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25a.html) · [저자 project/code](https://sites.google.com/view/spire-corl-2024). 수식·세부 구현·코드 실행은 미검증이다.
