# SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실행 도중 새 지시로 바뀔 때 적절히 task를 전환한다.

## Bottleneck and Changed Formulation

Contact phase와 behavior-conditioned trajectory를 이용해 switching을 학습한다.

## System and Robotics Loop

언어·관측·execution state → forward/rollback/advance action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

contact label, rollback 가정, 정식 venue status.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실행 중 task switching 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2506.03574) · [저자 project/code](https://switchvla.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
