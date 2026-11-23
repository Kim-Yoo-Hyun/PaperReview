# LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

긴 항법 episode에서 단일 턴 학습은 시간적 credit assignment를 충분히 다루기 어렵다.

## Core Idea and Contribution

환경과의 multi-turn 상호작용 및 horizon을 반영한 advantage 추정으로 VLA를 학습한다.

## Observation–State–Action Interface

시각 관측·상호작용 이력 → 항법 의사결정 → 환경 피드백.

## Evaluation Scope and Claim Boundary

Object navigation과 실제 장기 항법의 zero-shot 평가를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p068.html) · [저자 project/code](https://github.com/UMich-CURLY/LongNav-R1). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

조작에서 설계한 VLA+RL 목적함수가 항법의 긴 시간축에도 유효한지 비교할 직접 선행이다.

## Verification Boundary

action 단위, episode 길이별 정규화, rollout 분모, 실제 로봇의 저수준 제어기을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
