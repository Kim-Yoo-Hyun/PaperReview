# ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-interface, cross-embodiment
- Aliases: ExecVLA, KineVLA
- Official paper: https://arxiv.org/abs/2603.17524
- Venue verification: https://arxiv.org/abs/2603.17524
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. KineVLA→ExecVLA 동일 arXiv의 title revision이며 별도 논문이 아니다. ICLR 2027 submission은 acceptance가 아니다.

## Problem and Importance

목표 달성 외에 세부 수행 방식 제약을 따르게 한다.

## Core Idea and Contribution

목표/실행 수준의 action representation과 reasoning 신호를 분리한다.

## Observation–State–Action Interface

관측·실행 제약 지시 → bi-level representation → robot action.

## Evaluation Scope and Claim Boundary

LIBERO와 Realman robot의 execution-constraint 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.17524). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C2의 수행 방식 지시 주장이 겹치는 직접 선행이며 KineVLA와 동일 identity다.

## Verification Boundary

constraint label, evaluator geometry, KineVLA→ExecVLA version, 공개 checkpoint을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
