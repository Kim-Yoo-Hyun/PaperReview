# Trajectory-Level Continuous Action Representation for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

제어 주기에 묶인 행동 표현은 높은 샘플링 빈도에서 길어지고 시간적 일관성을 잃기 쉽다.

## Bottleneck and Changed Formulation

고정된 실제 시간 구간의 궤적을 continuous latent token으로 압축하고 주파수를 고려한 위치 표현을 사용한다.

## System and Robotics Loop

시간 구간의 행동 궤적·control frequency ↔ 연속 latent token ↔ 실행 행동.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

시간 구간·normalizer·주파수 학습 노출·동일 episode 내 변경 평가 유무.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO·MimicGen·실제 장시간 조작에서 backbone과 control frequency를 바꿔 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24). Exact objective, constraints, success definition은 본문 수동 확인 필요.
