# Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

가려진 기능 영역을 찾는 grasp에서 물체 전체를 스캔하면 관측 budget을 낭비할 수 있다.

## Bottleneck and Changed Formulation

완성 shape에서 affordance 가설을 만들고 entropy 감소·실제 관측 검증을 함께 고려해 다음 시점을 정한다.

## System and Robotics Loop

부분 관측·task → affordance 후보 → 카메라 시점 → functional grasp로 연결한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Shape hallucination·hypothesis weighting·view feasibility·stop threshold.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation과 실제 cluttered scene의 기능적 grasp 및 NBV step을 평가한다. 전체 pouring/insertion 성공과 구별한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.23504). Exact objective, constraints, success definition은 본문 수동 확인 필요.
