# Is Value Learning Really the Main Bottleneck in Offline RL?

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / NeurIPS
- Authors: Seohong Park, Kevin Frans, Sergey Levine, Aviral Kumar
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, policy-extraction, generalization, diagnosis
- Aliases: Offline RL bottlenecks
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

Offline RL이 BC보다 낮을 때 원인이 항상 value 오차인지 묻는다.

## Core Idea and Contribution

Value learning·policy extraction·test-state 일반화를 분리해 비교하고 policy 개선 대안을 분석한다.

## Observation–State–Action Interface

같은 offline data·가치함수 → 서로 다른 policy extraction → ID/OOD 상태 행동.

## Evaluation Scope and Claim Boundary

Offline RL의 extraction 선택과 데이터 coverage·test-time 정책 개선을 실증 비교한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다.

## Verification Boundary

본문에서 확인할 항목: critic 고정·extraction 예산·평가 state coverage·test-time 최적화 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
