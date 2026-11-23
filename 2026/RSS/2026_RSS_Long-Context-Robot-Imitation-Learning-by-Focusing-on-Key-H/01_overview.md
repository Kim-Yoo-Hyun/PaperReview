# Long-Context Robot Imitation Learning by Focusing on Key History Frames

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Big Picture Policies는 전체 관측 이력에 우연히 나타난 단서에 모방 정책이 의존하는 문제를 줄이기 위해 중요한 사건의 프레임만 기억한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=1)

## Core Idea and Contribution

- 시각언어 모델이 과제 진행과 관련된 핵심 프레임을 탐지해 서로 다른 관측 이력을 간결한 사건 표현으로 바꾼다. [PDF 4쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=5) · [PDF 6쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=6)
- 과거 관측이 필요한 실제 네 과제와 시뮬레이션 세 과제에서 전체 이력·제한된 이력·핵심 프레임 조건의 일반화를 비교했다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=5) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p201.pdf#page=8)

## Observation–State–Action Interface

관측 이력 → 의미 keyframe → history-conditioned 로봇 행동.

## Evaluation Scope and Claim Boundary

기억이 필요한 실제 조작과 simulation 과제를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p201.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA memory를 늘리는 것과 필요한 정보만 남기는 것의 차이를 검증할 직접 선행이다.

## Verification Boundary

VLM 호출 비용, event 검출의 미래 정보 누출, history 길이별 평가을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
