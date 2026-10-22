# DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / Unverified
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, bimanual, reasoning, mixture-of-experts
- Aliases:
- Official paper: https://jjjenghi.github.io/dialogvla/
- Venue verification: https://jjjenghi.github.io/dialogvla/
- Code/Project: https://jjjenghi.github.io/dialogvla/
- Code: not_released
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. IROS 2026 저자 표기만 확인; 공식 발표 미확인.

## Problem and Importance

양팔 조작에서 skill phase와 arm role을 action에 연결한다.

## Core Idea and Contribution

Structured dialog와 parallel skill/arm MoE가 flow action expert를 조건화한다.

## Observation–State–Action Interface

Multi-view·언어·proprioception → 양팔 action.

## Evaluation Scope and Claim Boundary

저자 project는 RoboTwin, RoboCasa GR1 및 실제 양팔 평가를 제시한다.

근거: [공식 paper/abstract](https://jjjenghi.github.io/dialogvla/) · [저자 project/code](https://jjjenghi.github.io/dialogvla/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D3 양팔 role reasoning의 중복을 피할 REFERENCE다. IROS 2026은 저자 표기이며 공식 채택 미확인이다.

## Verification Boundary

공식 proceedings, 원문 공개, source version, code release을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
