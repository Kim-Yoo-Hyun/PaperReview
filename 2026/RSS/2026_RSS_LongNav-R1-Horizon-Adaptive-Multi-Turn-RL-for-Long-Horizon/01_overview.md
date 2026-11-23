# LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Yue Hu, Avery Xi, Qixin Xiao, Seth Isaacson, Henry X. Liu, Ram Vasudevan, Maani Ghaffari
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, online-RL, Navigation, credit-assignment
- Aliases: LongNav-R1
- Official paper: https://roboticsproceedings.org/rss22/p068.html
- Venue verification: https://roboticsproceedings.org/rss22/p068.html
- Code/Project: https://github.com/UMich-CURLY/LongNav-R1
- Code: https://github.com/UMich-CURLY/LongNav-R1
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LongNav-R1은 긴 물체 탐색을 로봇과 환경의 연속적인 상호작용으로 학습하며 궤적 길이에 따라 행동의 기여도를 추정한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p068.pdf#page=1)

## Core Idea and Contribution

- 여러 차례의 관측·행동을 유지하는 온라인 강화학습에서 길이가 다른 탐색 궤적에 맞춘 어드밴티지 추정 방식을 제안했다. [PDF 4쪽](https://roboticsproceedings.org/rss22/p068.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p068.pdf#page=5)
- 객체 목표 내비게이션에서 4천 개 실행 궤적으로 Qwen3-VL-2B의 성공률이 64.3%에서 73.0%로 변했음을 보고하고 길이 보정의 영향을 분석했다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p068.pdf#page=1) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p068.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p068.pdf#page=8)

## Observation–State–Action Interface

시각 관측·상호작용 이력 → 항법 의사결정 → 환경 피드백.

## Evaluation Scope and Claim Boundary

Object navigation과 실제 장기 항법의 zero-shot 평가를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p068.html) · [저자 project/code](https://github.com/UMich-CURLY/LongNav-R1). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

조작에서 설계한 VLA+RL 목적함수가 항법의 긴 시간축에도 유효한지 비교할 직접 선행이다.

## Verification Boundary

action 단위, episode 길이별 정규화, rollout 분모, 실제 로봇의 저수준 제어기을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
