# JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / RSS
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, evaluation, manipulation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss20/p007.html
- Venue verification: https://www.roboticsproceedings.org/rss20/p007.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

가려진 deformable tissue의 부착 조건을 손상 없이 알아내야 한다.

## Core Idea and Contribution

미분 가능한 soft-body 모델·EKF 추정과 정보 이득/안전 비용을 고려한 능동 조작을 결합한다.

## Observation–State–Action Interface

Stereo 관측·조작 → attachment 추정 → sensing action.

## Evaluation Scope and Claim Boundary

실제 동물 조직의 부착점과 cutting/suturing 변화 실험을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss20/p007.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

물성·boundary 식별과 task-oriented probing을 구별하는 GAP-DE의 직접 선행이다.

## Verification Boundary

재료 모델과 attachment 가정, 안전 비용 정의을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
