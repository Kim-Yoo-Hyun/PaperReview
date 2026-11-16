# SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

장기 접촉 조작 전체를 시연이나 RL만으로 학습하면 탐색과 시연 비용이 커진다.

## Bottleneck and Changed Formulation

TAMP로 작은 학습 문제를 만들고 planning context에 맞춘 IL·RL 학습을 결합한다.

## System and Robotics Loop

상위 task/motion plan → 학습 하위 정책 → 접촉 조작; 계층형 경계를 유지한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

planner의 상태·기하 접근, 하위 문제 성공 분포, 실로봇 평가 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

장기·접촉 중심 조작 문제 집합에서 planning·IL·RL 결합 시스템들을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25a.html) · [저자 project/code](https://sites.google.com/view/spire-corl-2024). Exact objective, constraints, success definition은 본문 수동 확인 필요.
