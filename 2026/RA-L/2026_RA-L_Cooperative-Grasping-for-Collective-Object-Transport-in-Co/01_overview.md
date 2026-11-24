# Cooperative Grasping for Collective Object Transport in Constrained Environments

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: David Alvear, George Turkiyyah, Shinkyu Park
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: mobile-manipulation, motion-planning, grasping
- Aliases:
- Official paper: https://api.crossref.org/works/10.1109/LRA.2026.3653338
- Full-text retrieval: https://arxiv.org/pdf/2509.03638v1
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2026.3653338
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

이 연구는 두 로봇이 제한된 공간에서 물체를 함께 운반할 수 있는 파지 조합을 물체 형상과 환경 배치에서 예측한다. [PDF 1쪽](https://arxiv.org/pdf/2509.03638v1#page=1)

## Core Idea and Contribution

- 운반 가능한 파지 조합과 불가능한 조합을 구별하도록 조건부 임베딩을 지도학습하고 후보 쌍을 점수화한다. [PDF 3쪽](https://arxiv.org/pdf/2509.03638v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2509.03638v1#page=4)
- 여러 물체와 통로에서 시뮬레이션 운반 성공률을 비교하고 두 대의 실물 모바일 로봇으로 협동 운반을 시험했다. [PDF 5쪽](https://arxiv.org/pdf/2509.03638v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2509.03638v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2509.03638v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2509.03638v1#page=8)

## Observation–State–Action Interface

환경/물체·grasp 정보 → embedding → 운반 가능 grasp 선택.

## Evaluation Scope and Claim Boundary

Simulation과 실제 협동 object transport를 평가한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/LRA.2026.3653338). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

D2의 운반 결과를 고려한 파지 주장이 이미 다뤄졌음을 보여준다.

## Verification Boundary

환경 표현, label 생성 planner, two-robot 제약, 일반화 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
