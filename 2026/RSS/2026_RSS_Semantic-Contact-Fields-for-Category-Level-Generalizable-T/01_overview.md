# Semantic Contact Fields for Category-Level Generalizable Tool Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Kevin Yuchen Ma, Heng Zhang, Weisi Lin, Mike Zheng Shou, Yan Wu
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: contact, manipulation, representation
- Aliases: Semantic-Contact Fields for Category-Level Generalizable Tactile Tool Manipulation
- 게재 PDF에는 “Semantic-Contact Fields for Category-Level Generalizable Tactile Tool Manipulation”라는 제목이 실렸다. [표제면](https://www.roboticsproceedings.org/rss22/p004.pdf#page=1) · [학회 서지](https://www.roboticsproceedings.org/rss22/p004.html)
- Official paper: https://www.roboticsproceedings.org/rss22/p004.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss22/p004.pdf
- Venue verification: https://www.roboticsproceedings.org/rss22/p004.html
- DOI: 10.15607/rss.2026.xxii.004
- Code/Project: https://github.com/Kevinskwk/SCFields
- Code: https://github.com/Kevinskwk/SCFields
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

SCFields는 도구 표면의 접촉 가능성·힘과 시각적 의미를 3차원에 함께 표현해 여러 형상의 도구 조작에 사용한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=1)

## Core Idea and Contribution

- 시뮬레이션에서 도구 전반의 접촉장을 사전학습하고 실물 센서 관측으로 정렬해 접촉 추정을 조작 정책에 제공한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=5)
- 실제 도구의 접촉 예측을 확인하고 긁개·크레용·껍질 벗기기 과제에서 도구가 바뀔 때 정책 성능을 비교했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=6) · [PDF 7쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p004.pdf#page=9)

## Observation–State–Action Interface

시각 의미·접촉 추정 → 3D field → diffusion policy.

## Evaluation Scope and Claim Boundary

서로 다른 도구를 사용하는 contact-rich 작업 평가를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p004.html) · [저자 project/code](https://github.com/Kevinskwk/SCFields). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

D2의 도구·접촉 표현을 비교할 REFERENCE다. End-to-end VLA로 분류하지 않는다.

## Verification Boundary

촉각 입력 종류, pseudo-label 정확도, unseen-tool split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
