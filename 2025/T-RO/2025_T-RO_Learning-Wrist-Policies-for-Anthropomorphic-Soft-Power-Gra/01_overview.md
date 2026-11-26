# Learning Wrist Policies for Anthropomorphic Soft Power Grasping in Handle and Door Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / T-RO
- Authors: Florian Voigt, Abdeljalil Naceri, Sami Haddadin
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: force control, Impedance Control, door opening, dexterous manipulation, sim-to-real
- Aliases: Learning Wrist Policies
- Official paper: https://portal.fis.tum.de/en/publications/learning-wrist-policies-for-anthropomorphic-soft-power-grasping-i/
- Venue verification: https://api.crossref.org/works/10.1109/tro.2025.3576950
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-26 서지와 T-RO 인쇄 초록과 TUM 서지(인쇄 저자는 Abdeljalil, TUM·기탁 서지는 Abdeldjallil 표기) 대조. 본문 검토 범위는 제한적이다.

## Problem and Importance

손잡이의 위치와 방향이 불확실할 때 순응하는 손목을 이용해 접촉을 유지하는 문제다.

## Core Idea and Contribution

손·팔을 하나의 임피던스 제어기로 다루며, 손목 임피던스와 손바닥·손가락 힘을 함께 조절하는 정책을 학습한다.

## Observation–State–Action Interface

손과 팔 기구의 제어 설정을 하나의 정책에서 정해 손잡이 잡기와 회전에 사용한다.

## Evaluation Scope and Claim Boundary

시뮬레이션에서 학습하고 완전 구동 손과 부족 구동 손을 장착한 서비스 휴머노이드에서 손잡이·문 조작을 검증했다.

근거: [공식 paper/abstract](https://portal.fis.tum.de/en/publications/learning-wrist-policies-for-anthropomorphic-soft-power-grasping-i/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

걸쇠와 손잡이 실험에서 재학습 없는 순응 제어 기준을 제공한다.

## Verification Boundary

손의 구동 형태와 문 유형별 시험 조건 및 힘·속도 제어 기준선을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
