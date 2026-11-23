# Cooperative Grasping for Collective Object Transport in Constrained Environments

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: David Alvear, George Turkiyyah, Shinkyu Park
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: mobile-manipulation, motion-planning, grasping
- Aliases:
- Official paper: https://api.crossref.org/works/10.1109/LRA.2026.3653338
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2026.3653338
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

두 로봇의 협동 운반에 적합한 grasp configuration을 고른다.

## Core Idea and Contribution

환경·물체 조건을 반영하는 conditional embedding과 negative sampling으로 feasible grasp를 학습한다.

## Observation–State–Action Interface

환경/물체·grasp 정보 → embedding → 운반 가능 grasp 선택.

## Evaluation Scope and Claim Boundary

Simulation과 실제 협동 object transport를 평가한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/LRA.2026.3653338). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2의 운반 결과를 고려한 파지 주장이 이미 다뤄졌음을 보여준다.

## Verification Boundary

환경 표현, label 생성 planner, two-robot 제약, 일반화 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
