# Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kyle Stachowicz, Lydia Ignatova, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Navigation, offline-to-online-RL, continual-learning
- Aliases: LiReN
- Official paper: https://proceedings.mlr.press/v270/stachowicz25a.html
- Venue verification: https://proceedings.mlr.press/v270/stachowicz25a.html
- Code/Project: https://github.com/kylestach/lifelong-nav-rl
- Code: https://github.com/kylestach/lifelong-nav-rl
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  CoRL 2024 event; PMLR volume 270 published 2025. Registry year uses event year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

시연으로만 학습한 항법 foundation policy는 배포 경험으로 자율 개선하기 어렵다.

## Core Idea and Contribution

Offline RL 사전학습과 지속적인 자율 운영·online 적응을 하나의 항법 학습 시스템으로 구성한다.

## Observation–State–Action Interface

시각 관측·항법 목표 → 정책 행동 → 실제 배포 데이터 → 정책 갱신.

## Evaluation Scope and Claim Boundary

실세계 open-world 항법 배포에서 자율 수집 데이터로 적응하는 시스템을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/stachowicz25a.html) · [저자 project/code](https://github.com/kylestach/lifelong-nav-rl). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL의 지속 학습을 manipulation에 한정하지 않고 실제 항법 운영 조건과 비교할 기준이다.

## Verification Boundary

목표 생성·reset·인간 개입의 범위, 정책 입력의 언어 여부, 이전 장소 회귀을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
