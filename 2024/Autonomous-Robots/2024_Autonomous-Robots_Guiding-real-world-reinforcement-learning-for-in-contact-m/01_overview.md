# Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / Autonomous Robots
- Authors: Abhishek Padalkar, Gabriel Quere, Antonin Raffin, João Silvério, Freek Stulp
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: real-world RL, contact, constraints, shared control
- Aliases: RL-SCT
- Official paper: https://link.springer.com/article/10.1007/s10514-024-10164-6
- Venue verification: https://link.springer.com/article/10.1007/s10514-024-10164-6
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. Autonomous Robots journal로 기록하며 top-tier conference 논문으로 묶지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 기하와 물체 접촉에서 이미 아는 제약을 제어 템플릿에 맡기고 남은 자유도만 강화학습으로 탐색해 실물 학습 부담을 줄인다. [PDF 1쪽](https://link.springer.com/content/pdf/10.1007/s10514-024-10164-6.pdf#page=1)

## Core Idea and Contribution

- 공유 제어 템플릿으로 허용되는 움직임을 정해 행동·상태 공간을 줄이고, 미지의 작업 변수에 대해서만 로봇이 경험에서 학습하게 한다. [PDF 7쪽](https://link.springer.com/content/pdf/10.1007/s10514-024-10164-6.pdf#page=7) · [PDF 8쪽](https://link.springer.com/content/pdf/10.1007/s10514-024-10164-6.pdf#page=8)
- 실제 7자유도 팔의 붓기 과제는 65회 약 16분, 격자 클램프 삽입은 75회 약 17분의 학습을 보고하고 삽입 때 접촉력도 평가했다. [PDF 1쪽](https://link.springer.com/content/pdf/10.1007/s10514-024-10164-6.pdf#page=1) · [PDF 10쪽](https://link.springer.com/content/pdf/10.1007/s10514-024-10164-6.pdf#page=10) · [PDF 13쪽](https://link.springer.com/content/pdf/10.1007/s10514-024-10164-6.pdf#page=13)

## Observation–State–Action Interface

Template가 제한한 state/action 공간에서 unknown task knowledge를 학습한다. 단일 VLA 내부의 learned exploration은 아니다.

## Evaluation Scope and Claim Boundary

7-DoF 실제 로봇의 pouring·grid-clamp placement를 다룬다. 논문의 안전 주장 조건을 보편적 보증으로 일반화하지 않는다.

근거: [공식 paper/abstract](https://link.springer.com/article/10.1007/s10514-024-10164-6). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

관계/geometry로 탐색을 제한한다는 원리를 이미 제시한 직접 선행이다.

## Verification Boundary

수동 task constraint·phase 전환·안전 보증 전제·reward 정보을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
