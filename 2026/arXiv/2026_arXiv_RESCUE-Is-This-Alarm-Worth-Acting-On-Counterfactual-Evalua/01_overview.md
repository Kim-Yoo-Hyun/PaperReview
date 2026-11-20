# RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2610.13516
- Venue verification: https://arxiv.org/abs/2610.13516
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Failure alarm의 정확도만으로 실제 개입 가치를 알 수 없다.

## Core Idea and Contribution

Counterfactual continuation branch로 monitor의 intervention utility와 비용을 평가한다.

## Observation–State–Action Interface

동일 sim/policy state·alarm → 여러 continuation → outcome 비교.

## Evaluation Scope and Claim Boundary

LIBERO Spatial Plus와 VLA runtime monitor 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.13516). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C1/RP-2의 관측/개입 가치 진단에 대한 직접 evaluation 기준이다.

## Verification Boundary

state clone 완전성, policy memory, oracle 개입, 실환경 적용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
