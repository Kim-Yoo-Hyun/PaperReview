# Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Denis Shcherba, Adrian Abel, Eckart Cobo-Briesewitz, Paul Mattes, Wojciech Samek, Marc Toussaint
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: state estimation, visuomotor control, policy distillation, manipulation
- Aliases: EDI, Estimate, Don't Imitate
- Official paper: https://arxiv.org/abs/2609.34018
- Venue verification: https://arxiv.org/abs/2609.34018
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: arXiv 초록·공식 publication/project를 확인한 등록. Abstract 기반 — 본문 수동 확인 필요. 연구 dossier의 지정 절 검토와 paper별 5-note의 evidence를 구별하며 사용자 읽기 상태는 변경하지 않음. 저자 dataset card의 ICRA2026 표기는 공식 proceedings 확인이 없어 채택하지 않음. 연결된 HHI-Robot-Learning/26-DistillingSGRL은 404이며 미공개 이유를 추정하지 않음.

## Problem and Importance

시뮬레이터의 privileged state로 학습한 조작 정책을 영상 관측으로 실행하려면 추정 오차와 행동 오차를 함께 다뤄야 한다.

## Core Idea and Contribution

기존 미분 가능한 state-based expert를 고정하고, 상태 supervision과 expert를 통과하는 action-consistency loss로 시각 추정기를 학습한다. Expert의 행동 매핑을 다시 모방하는 비용을 줄이는 formulation이다.

## Observation–State–Action Interface

영상 → 추정된 물리 상태 → 고정 expert → 로봇 행동. 추정기만 학습하며 VLA나 언어 조건 정책을 전제로 한 방법은 아니다.

## Evaluation Scope and Claim Boundary

초록은 goal-conditioned 조작 5개와 실제 Panda의 sim-to-real 평가를 보고한다. Trial 구성·각 조건별 성공 수·시연 분할은 이번 등록에서 확인하지 않았다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.34018). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 geometry 후보의 action-consistency 대조를 정하는 직접 NEXT다. 행동에 중요한 추정 오차를 학습한다는 원리를 신규성에서 제외하게 한다.

## Verification Boundary

Expert의 미분 가능성·state/goal 정의·loss schedule·occlusion·held-out split·실제 로봇 trial 및 코드 release를 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
