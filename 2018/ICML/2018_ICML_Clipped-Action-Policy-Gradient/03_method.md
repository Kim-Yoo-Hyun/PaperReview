# Clipped Action Policy Gradient

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

실행 action이 clipping되는 사실을 이용한 unbiased estimator를 제안한다.

## Observation–State–Action Interface

Unbounded policy sample → clip → bounded executed action·gradient.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: clipping preimage, policy family, gradient unbiasedness 조건.

Source가 명시한 evaluation 범위: Continuous control의 이론·실험 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 reward·action sample에서 raw/clipped score variance를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v80/fujita18a.html) · [저자 project/code](https://github.com/pfnet-research/capg). 수식·세부 구현·코드 실행은 미검증이다.
