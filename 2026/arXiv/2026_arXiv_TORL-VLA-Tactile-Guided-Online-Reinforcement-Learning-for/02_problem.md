# TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉 조건이 변하면 offline tactile VLA가 적응하지 못하는 문제를 다룬다.

## Bottleneck and Changed Formulation

Wrench-aware VLA의 reference를 online RL 모듈로 보정하고 human intervention 경계를 critic 학습에 반영한다.

## System and Robotics Loop

촉각 유래 wrench·상태 → reference action/future wrench → 실행 행동 보정.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

개입 전후 critic mask, latency, base/보정 정책 학습 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

실제 latch·컵·달걀 조작의 부분/전체 과제와 시간 제한 효율을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2606.09337) · [저자 project/code](https://torl-vla.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
