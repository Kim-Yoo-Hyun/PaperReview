# Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Jacky Kwok, Xilun Zhang, Mengdi Xu, Yuejiang Liu, Azalia Mirhoseini, Chelsea Finn, Marco Pavone
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: test-time-scaling, verification, instruction-following
- Aliases: CoVer, CoVer-VLA
- Official paper: https://arxiv.org/abs/2602.12281
- Venue verification: https://api.crossref.org/works/10.1007/978-3-032-37016-7_3
- Code/Project: https://cover-vla.github.io/
- Code: https://github.com/cover-vla/cover-vla
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

VLA의 생성 행동이 지시 의도와 어긋나며 후보 다양성만 늘려도 선택 문제가 남는다.

## Core Idea and Contribution

지시 재표현과 action sample을 함께 확장하고 contrastive verifier로 prompt·action을 선택한다.

## Observation–State–Action Interface

VLM instruction rephrasing → VLA action candidates → verifier selection; 계층형 test-time pipeline.

## Evaluation Scope and Claim Boundary

SIMPLER·PolaRiS와 실로봇의 in/out-of-distribution 지시 실행을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.12281) · [저자 project/code](https://cover-vla.github.io/) · [공식 code](https://github.com/cover-vla/cover-vla). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

정책 RL 갱신의 필요성을 검증할 강한 추론 계산량·검증 대안이다.

## Verification Boundary

재표현의 의미 보존, verifier 감독량, rollout-independent evaluation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
