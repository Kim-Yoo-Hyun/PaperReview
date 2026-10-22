# WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2610.01083
- Venue verification: https://arxiv.org/abs/2610.01083
- Code/Project: https://samuelzhen.com/projects/wbag
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

VLA action의 안전성을 robot whole-body와 잡은 물체까지 고려한다.

## Core Idea and Contribution

Attached geometry와 whole-body 제약을 반영하는 safety filtering을 제안한다.

## Observation–State–Action Interface

Robot·attached object geometry와 VLA action → 수정 action.

## Evaluation Scope and Claim Boundary

SafeLIBERO 기반 안전성 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.01083) · [저자 project/code](https://samuelzhen.com/projects/wbag). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2의 파지 후 geometry 고려라는 넓은 기여와 직접 충돌한다.

## Verification Boundary

geometry/oracle 접근, attachment 갱신, infeasible 제약, real-robot 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
