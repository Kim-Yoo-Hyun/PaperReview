# Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

파지 실패와 후속 실행 실패를 구분해 manipulation을 개선한다.

## Bottleneck and Changed Formulation

Grasp-then-plan 두 단계와 failure attribution을 연결한다.

## System and Robotics Loop

Grasp 후보 → 실행 계획 → 실패 원인 → 두 단계 개선.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

failure label 출처, planner 성공과 policy 성공 구분, code 공개.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 manipulation 및 여러 정책 계열 비교를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.03385) · [저자 project/code](https://sites.google.com/view/gtp-fa/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
