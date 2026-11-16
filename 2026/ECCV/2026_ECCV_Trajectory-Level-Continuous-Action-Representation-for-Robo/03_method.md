# Trajectory-Level Continuous Action Representation for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

고정된 실제 시간 구간의 궤적을 continuous latent token으로 압축하고 주파수를 고려한 위치 표현을 사용한다.

## Observation–State–Action Interface

시간 구간의 행동 궤적·control frequency ↔ 연속 latent token ↔ 실행 행동.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 시간 구간·normalizer·주파수 학습 노출·동일 episode 내 변경 평가 유무.

Source가 명시한 evaluation 범위: LIBERO·MimicGen·실제 장시간 조작에서 backbone과 control frequency를 바꿔 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

정상 주기와 episode 중간 주기 변경을 구별하고 동일 시간·경로에서 행동 오차와 성공을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24). 수식·세부 구현·코드 실행은 미검증이다.
