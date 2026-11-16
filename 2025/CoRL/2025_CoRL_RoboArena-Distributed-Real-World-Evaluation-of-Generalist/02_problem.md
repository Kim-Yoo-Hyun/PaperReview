# RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

기관마다 task·환경이 달라 generalist policy의 실로봇 순위를 비교하기 어렵다.

## Bottleneck and Changed Formulation

분산 평가자가 두 정책을 double-blind로 비교하고 선호 결과를 통합한다.

## System and Robotics Loop

같은 평가 상황의 두 정책 rollout → 선호 비교 → 전체 정책 순위.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

pairwise reset 조건, task 선택 편향, 선호 aggregation과 불확실성.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

DROID 플랫폼을 사용하는 여러 기관에서 generalist policy를 실로봇으로 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/atreya25a.html) · [저자 project/code](https://robo-arena.github.io/) · [공식 code](https://github.com/pranavatreya/roboarena_backend). Exact objective, constraints, success definition은 본문 수동 확인 필요.
