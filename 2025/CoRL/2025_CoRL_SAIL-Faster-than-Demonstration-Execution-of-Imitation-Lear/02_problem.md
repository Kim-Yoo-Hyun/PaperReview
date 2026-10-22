# SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Imitation policy를 시연 속도보다 빠르게 실행하면서 성능을 유지한다.

## Bottleneck and Changed Formulation

일관성·tracking·speed modulation·latency scheduling을 결합한다.

## System and Robotics Loop

시연 motion target → policy → tracking/speed 제어.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

target/command/torque 주기, motion 재표현, component ablation.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation task와 실제 robot 플랫폼의 빠른 실행을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/arachchige25a.html) · [저자 project/code](https://nadunranawaka1.github.io/sail-policy). Exact objective, constraints, success definition은 본문 수동 확인 필요.
