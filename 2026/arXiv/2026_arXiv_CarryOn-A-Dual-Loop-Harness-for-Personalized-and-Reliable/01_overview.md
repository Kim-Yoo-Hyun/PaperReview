# CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2610.21453
- Venue verification: https://arxiv.org/abs/2610.21453
- Code/Project: https://vincent2311.github.io/Projects/CarryOn/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

개인화된 robot assistance에서 고수준 의도와 실행 신뢰성을 연결한다.

## Core Idea and Contribution

계획과 action safety/recovery의 dual-loop 구조를 frozen VLA에 결합한다.

## Observation–State–Action Interface

사용자·scene context → 계획 → VLA·shield·recovery.

## Evaluation Scope and Claim Boundary

Simulation과 실제 robot assistance 결과를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.21453) · [저자 project/code](https://vincent2311.github.io/Projects/CarryOn/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2/D3에서 persistent planning·shield 결합의 신규성 경계를 정한다.

## Verification Boundary

메모리 입력, failure detector, recovery 비용, 공개 구현 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
