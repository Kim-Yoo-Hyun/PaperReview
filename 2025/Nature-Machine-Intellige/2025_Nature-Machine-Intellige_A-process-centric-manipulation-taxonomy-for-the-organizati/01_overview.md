# A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / Nature Machine Intelligence
- Authors: Lars Johannsmeier, Samuel Schneider, Yanan Li, Etienne Burdet, Sami Haddadin
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, tactile sensing, skill-composition, process-specification
- Aliases: TMS
- Official paper: https://www.nature.com/articles/s42256-025-01045-3
- Venue verification: https://www.nature.com/articles/s42256-025-01045-3
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. Nature 공식 검색 인덱스의 abstract·서지정보 확인. 직접 HTML 접근은 인증 redirect로 제한; 본문 정독·code 확인으로 표시하지 않는다.

## Problem and Importance

복잡한 접촉 작업을 재사용 가능한 tactile skill로 조직할 표현이 필요하다.

## Core Idea and Contribution

전문가의 process specification을 taxonomy와 parametric tactile skill로 연결한다.

## Observation–State–Action Interface

공정 요구 → skill specification → policy/controller → 접촉 feedback.

## Evaluation Scope and Claim Boundary

산업 응용의 여러 tactile skill과 목표 pose 교란을 실로봇에서 평가한다.

근거: [공식 paper/abstract](https://www.nature.com/articles/s42256-025-01045-3). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

언어 기반 skill 조합과 전문가가 명시한 물리적 요구·종료 조건을 비교할 참조다.

## Verification Boundary

전문가 specification 비용, grasp/접촉 가정, skill 선택과 저수준 controller 기여을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
