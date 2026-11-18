# Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

시뮬레이터의 privileged state로 학습한 조작 정책을 영상 관측으로 실행하려면 추정 오차와 행동 오차를 함께 다뤄야 한다.

## Bottleneck and Changed Formulation

기존 미분 가능한 state-based expert를 고정하고, 상태 supervision과 expert를 통과하는 action-consistency loss로 시각 추정기를 학습한다. Expert의 행동 매핑을 다시 모방하는 비용을 줄이는 formulation이다.

## System and Robotics Loop

영상 → 추정된 물리 상태 → 고정 expert → 로봇 행동. 추정기만 학습하며 VLA나 언어 조건 정책을 전제로 한 방법은 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Expert의 미분 가능성·state/goal 정의·loss schedule·occlusion·held-out split·실제 로봇 trial 및 코드 release.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

초록은 goal-conditioned 조작 5개와 실제 Panda의 sim-to-real 평가를 보고한다. Trial 구성·각 조건별 성공 수·시연 분할은 이번 등록에서 확인하지 않았다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.34018). Exact objective, constraints, success definition은 본문 수동 확인 필요.
