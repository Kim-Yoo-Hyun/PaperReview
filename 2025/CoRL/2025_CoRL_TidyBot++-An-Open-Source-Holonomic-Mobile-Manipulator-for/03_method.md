# TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Holonomic base와 휴대전화 teleoperation을 결합한 공개 mobile manipulator를 설계한다.

## Observation–State–Action Interface

사람 teleoperation → base/arm demonstration → mobile manipulation policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: arm 지원 범위와 실제 검증 조합, base/arm 제어 주기, 비용·teleoperation protocol.

Source가 명시한 evaluation 범위: 실로봇 가정 과제에서 수집한 시연으로 학습한 정책을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

base/arm command와 demonstration 비용을 기록하고 base 동작 필요성별 task를 구분한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/wu25a.html) · [저자 project/code](https://github.com/jimmyyhwu/tidybot2). 수식·세부 구현·코드 실행은 미검증이다.
