# Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. Autonomous Robots journal로 기록하며 top-tier conference 논문으로 묶지 않는다.

## Problem and Importance

접촉 과제의 자유로운 RL 탐색은 많은 실제 상호작용과 위험한 동작을 요구한다.

## Core Idea and Contribution

물체 관계·task geometry의 알려진 제약을 shared-control template으로 표현해 RL이 탐색하는 차원을 줄인다.

## Observation–State–Action Interface

Template가 제한한 state/action 공간에서 unknown task knowledge를 학습한다. 단일 VLA 내부의 learned exploration은 아니다.

## Evaluation Scope and Claim Boundary

7-DoF 실제 로봇의 pouring·grid-clamp placement를 다룬다. 논문의 안전 주장 조건을 보편적 보증으로 일반화하지 않는다.

근거: [공식 paper/abstract](https://link.springer.com/article/10.1007/s10514-024-10164-6). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

관계/geometry로 탐색을 제한한다는 원리를 이미 제시한 직접 선행이다.

## Verification Boundary

수동 task constraint·phase 전환·안전 보증 전제·reward 정보을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
