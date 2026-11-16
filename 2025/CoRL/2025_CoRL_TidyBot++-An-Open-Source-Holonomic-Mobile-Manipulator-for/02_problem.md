# TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

가정용 mobile manipulation 시연을 수집할 유연하고 재사용 가능한 플랫폼이 필요하다.

## Bottleneck and Changed Formulation

Holonomic base와 휴대전화 teleoperation을 결합한 공개 mobile manipulator를 설계한다.

## System and Robotics Loop

사람 teleoperation → base/arm demonstration → mobile manipulation policy.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

arm 지원 범위와 실제 검증 조합, base/arm 제어 주기, 비용·teleoperation protocol.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실로봇 가정 과제에서 수집한 시연으로 학습한 정책을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/wu25a.html) · [저자 project/code](https://github.com/jimmyyhwu/tidybot2). Exact objective, constraints, success definition은 본문 수동 확인 필요.
