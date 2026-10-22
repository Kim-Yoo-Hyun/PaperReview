# Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

동적 환경에서 전체 task를 고려하며 mobile robot motion을 즉시 수정한다.

## Bottleneck and Changed Formulation

최적화 planner와 reactive geometric fabrics를 결합하고 대체 목표 pose를 탐색한다.

## System and Robotics Loop

Robot/환경 state → global guidance → reactive whole-body motion.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

object pose 가용성, collision geometry, 목표 pose 자유도, 계산 예산.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

다중 mobile manipulator의 simulation 및 실제 실험을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://doi.org/10.1109/LRA.2025.3562005) · [저자 project/code](https://autonomousrobots.nl/paper_websites/g3f). Exact objective, constraints, success definition은 본문 수동 확인 필요.
