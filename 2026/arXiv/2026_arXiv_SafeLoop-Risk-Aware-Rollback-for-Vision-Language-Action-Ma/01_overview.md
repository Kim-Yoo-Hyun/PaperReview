# SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2609.26313
- Venue verification: https://arxiv.org/abs/2609.26313
- Code/Project: https://github.com/Loule0-0/SafeLoop/tree/release/safeloop
- Code: https://github.com/Loule0-0/SafeLoop/tree/release/safeloop
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. IROS 저자 표기만으로 venue를 승격하지 않음; 공식 acceptance 미확인.

## Problem and Importance

위험한 VLA 실행을 감지해 rollback으로 복구한다.

## Core Idea and Contribution

시각·proprioception 기반 위험 예측과 no-op/rollback 개입을 결합한다.

## Observation–State–Action Interface

관측·시간 context → risk → 실행 중단/역행.

## Evaluation Scope and Claim Boundary

LIBERO 및 실제 manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.26313) · [저자 project/code](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D3에서 rollback이 세계 상태를 되돌린다는 잘못된 가정을 피할 직접 비교군이다.

## Verification Boundary

joint history와 world state 구분, detector labels, collision 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
