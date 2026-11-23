# Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  CoRL 2024 event; PMLR volume 270 published 2025. Registry year uses event year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LiReN은 여러 로봇의 오프라인 주행 자료로 목표 조건부 정책을 사전학습한 뒤, 실제 배포 장소에서 자율적으로 수집한 경험으로 정책을 개선한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/stachowicz25a/stachowicz25a.pdf#page=1)

## Core Idea and Contribution

- 도달할 목표를 제안하고 충돌과 목표까지의 거리 변화를 보상에 반영하며 기존 자료와 새 주행을 혼합해 배포 중 학습한다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/stachowicz25a/stachowicz25a.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/stachowicz25a/stachowicz25a.pdf#page=6)
- 실제 사무실에서 목표 도달률과 탐색한 공간의 비율을 함께 측정해 좁은 구역에서 같은 성공을 반복하는 정책과 구분했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/stachowicz25a/stachowicz25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/stachowicz25a/stachowicz25a.pdf#page=8)

## Observation–State–Action Interface

시각 관측·항법 목표 → 정책 행동 → 실제 배포 데이터 → 정책 갱신.

## Evaluation Scope and Claim Boundary

실세계 open-world 항법 배포에서 자율 수집 데이터로 적응하는 시스템을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/stachowicz25a.html) · [저자 project/code](https://github.com/kylestach/lifelong-nav-rl). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL의 지속 학습을 manipulation에 한정하지 않고 실제 항법 운영 조건과 비교할 기준이다.

## Verification Boundary

목표 생성·reset·인간 개입의 범위, 정책 입력의 언어 여부, 이전 장소 회귀을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
