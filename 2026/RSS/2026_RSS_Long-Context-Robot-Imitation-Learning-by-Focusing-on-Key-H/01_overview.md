# Long-Context Robot Imitation Learning by Focusing on Key History Frames

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Max Sobol Mark, Maria Attarian, Chuyuan Fu, Debidatta Dwibedi, Jacky Liang, Dhruv Shah, Aviral Kumar
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Imitation Learning, memory, distribution-shift, keyframes
- Aliases: BPP, BPP: Long-Context Robot Imitation Learning by Focusing on Key History Frames
- Official paper: https://roboticsproceedings.org/rss22/p201.html
- Venue verification: https://roboticsproceedings.org/rss22/p201.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

긴 관측 이력은 학습에 없던 history에서 잘못된 상관에 의존할 수 있다.

## Core Idea and Contribution

VLM이 선택한 소수의 의미 있는 keyframe으로 정책 history를 압축한다.

## Observation–State–Action Interface

관측 이력 → 의미 keyframe → history-conditioned 로봇 행동.

## Evaluation Scope and Claim Boundary

기억이 필요한 실제 조작과 simulation 과제를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p201.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA memory를 늘리는 것과 필요한 정보만 남기는 것의 차이를 검증할 직접 선행이다.

## Verification Boundary

VLM 호출 비용, event 검출의 미래 정보 누출, history 길이별 평가을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
