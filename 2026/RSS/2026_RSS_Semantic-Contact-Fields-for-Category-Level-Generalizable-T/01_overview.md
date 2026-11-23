# Semantic Contact Fields for Category-Level Generalizable Tool Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Kevin Yuchen Ma, Heng Zhang, Weisi Lin, Mike Zheng Shou, Yan Wu
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: contact, manipulation, representation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p004.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p004.html
- Code/Project: https://github.com/Kevinskwk/SCFields
- Code: https://github.com/Kevinskwk/SCFields
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

새 도구 형상에서 semantic 목표와 접촉 제어를 함께 일반화한다.

## Core Idea and Contribution

3D semantic-contact field를 sim pretraining과 real pseudo-label 조정으로 학습한다.

## Observation–State–Action Interface

시각 의미·접촉 추정 → 3D field → diffusion policy.

## Evaluation Scope and Claim Boundary

서로 다른 도구를 사용하는 contact-rich 작업 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p004.html) · [저자 project/code](https://github.com/Kevinskwk/SCFields). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2의 도구·접촉 표현을 비교할 REFERENCE다. End-to-end VLA로 분류하지 않는다.

## Verification Boundary

촉각 입력 종류, pseudo-label 정확도, unseen-tool split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
