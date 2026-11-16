# Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, state estimation, occlusion, non-prehensile
- Aliases:
- Official paper: https://proceedings.mlr.press/v270/ferrandis25a.html
- Venue verification: https://proceedings.mlr.press/v270/ferrandis25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025.

## Problem and Importance

비파지 조작에서 가려진 물체의 상태와 접촉 불확실성을 함께 다뤄야 한다.

## Core Idea and Contribution

Simulation interaction으로 visuotactile estimator를 학습하고 불확실성을 정책에 연결한다.

## Observation–State–Action Interface

시각·촉각 → 추정 상태/불확실성 → uncertainty-aware control.

## Evaluation Scope and Claim Boundary

비파지 manipulation의 가림 조건과 실로봇 sim-to-real을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/ferrandis25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

접촉 VLA의 센서 이득과 상태 추정·feedback controller 이득을 분리할 직접 대안이다.

## Verification Boundary

privileged training input, tactile modality, occlusion 분포, estimator와 policy ablation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
