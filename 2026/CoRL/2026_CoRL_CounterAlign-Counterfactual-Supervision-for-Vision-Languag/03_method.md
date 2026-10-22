# CounterAlign: Counterfactual Supervision for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Instruction mismatch를 counterfactual supervision으로 사용해 reward/정책을 정렬한다.

## Observation–State–Action Interface

관측·지시·mismatch negative → 학습 신호 → action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: negative validity, reward leakage, scene overlap, constraint label 범위.

Source가 명시한 evaluation 범위: LIBERO 계열 instruction 평가와 실제 robot 결과를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Object/task 지시와 execution constraint를 분리한 held-out 평가를 수행한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=AY4totylcx). 수식·세부 구현·코드 실행은 미검증이다.
