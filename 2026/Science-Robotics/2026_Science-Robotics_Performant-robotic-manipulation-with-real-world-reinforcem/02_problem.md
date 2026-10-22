# Performant robotic manipulation with real-world reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실제 manipulation에서 imitation policy의 성공률·속도·강건성을 실용적인 RL 학습으로 개선하는 문제다.

## Bottleneck and Changed Formulation

Diffusion visuomotor policy의 imitation-to-RL 학습과 빠른 controller 실행을 연결하는 real-world RL framework를 제안한다.

## System and Robotics Loop

Visual observation → diffusion/flow visuomotor policy → robot action; offline/online 학습과 deployment 추론을 구분한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Evaluation success denominator, human intervention, offline/online 단계 및 distillation 손실.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 공식 repository와 저널 abstract는 pushing, pouring, cloth/long-horizon manipulation 등을 포함한 실제 robot 평가를 설명한다. 프로토콜별 수치는 본문 확인 필요.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1126/scirobotics.aed6267) · [저자 project/code](https://github.com/Lei-Kun/RL-100). Exact objective, constraints, success definition은 본문 수동 확인 필요.
