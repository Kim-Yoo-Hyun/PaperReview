# CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, variable-impedance, contact, flow-matching
- Aliases: CompVLA
- Official paper: https://arxiv.org/abs/2609.23614
- Venue verification: https://arxiv.org/abs/2609.23614
- Code/Project: https://compvla.github.io/
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 최신 v2(2026-11-06) abstract 확인. 기존 N1 본문 대조는 v1이며 v2 본문을 확인한 것으로 승격하지 않는다. 저자 CoRL 2026 표기는 공식 승인 근거 미확인. Code 링크 404. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

기하 동작만 출력하는 VLA의 접촉 순응성 부족을 다룬다.

## Core Idea and Contribution

Compliance Expert가 동작·강성·virtual displacement를 생성하고 geometric impedance로 실행한다.

## Observation–State–Action Interface

RGB·언어 → 동작과 시변 강성 행렬.

## Evaluation Scope and Claim Boundary

접촉 과제에서 vanilla/compliance-aware VLA 및 구성요소 ablation을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.23614) · [저자 project/code](https://compvla.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

강성 출력을 VLA에 추가하는 것 자체의 신규성을 배제할 직접 선행이다.

## Verification Boundary

강성–displacement 식별성, force 입력 유무, 데이터·controller 공정성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
