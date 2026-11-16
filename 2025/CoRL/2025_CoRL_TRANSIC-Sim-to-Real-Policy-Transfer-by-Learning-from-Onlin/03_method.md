# TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

사람의 online correction으로 residual policy를 학습해 simulation 정책과 결합한다.

## Observation–State–Action Interface

point-cloud 기반 base policy + 인간 correction으로 학습한 residual → 실행 action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 개입 시점/시간 비용, residual 제어 권한, correction과 평가 분할.

Source가 명시한 evaluation 범위: 가구 조립 등 실로봇 접촉 조작의 sim-to-real 전이를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

base policy·개입 횟수·관측을 고정하고 residual과 단순 finetuning을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/jiang25a.html) · [저자 project/code](https://transic-robot.github.io/) · [공식 code](https://github.com/transic-robot/transic). 수식·세부 구현·코드 실행은 미검증이다.
