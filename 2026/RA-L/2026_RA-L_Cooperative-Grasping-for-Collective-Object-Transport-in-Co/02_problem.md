# Cooperative Grasping for Collective Object Transport in Constrained Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

두 로봇의 협동 운반에 적합한 grasp configuration을 고른다.

## Bottleneck and Changed Formulation

환경·물체 조건을 반영하는 conditional embedding과 negative sampling으로 feasible grasp를 학습한다.

## System and Robotics Loop

환경/물체·grasp 정보 → embedding → 운반 가능 grasp 선택.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

환경 표현, label 생성 planner, two-robot 제약, 일반화 split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 협동 object transport를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1109/LRA.2026.3653338). Exact objective, constraints, success definition은 본문 수동 확인 필요.
