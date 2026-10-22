# VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

로봇의 동시 보고·듣기·말하기·행동과 사용자 interruption을 연결한다.

## Bottleneck and Changed Formulation

Active/Standby dual-model과 system command token을 사용한다.

## System and Robotics Loop

시각·음성·지시 → 발화와 system/action command.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

명령 token timing, rollback 범위, ICLR acceptance 미확인.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Humanoid platform의 동시 interaction을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2510.21817) · [저자 project/code](https://lxysl.github.io/VITA-E/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
