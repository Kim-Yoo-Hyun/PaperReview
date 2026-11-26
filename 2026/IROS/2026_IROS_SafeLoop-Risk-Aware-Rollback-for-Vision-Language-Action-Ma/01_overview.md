# SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IROS
- Authors: Zeyu Lou, Tianran Zhang, Xinquan Yue, Ya Jing, Chenyang Si
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation, VLA, failure recovery, Reinforcement Learning
- Aliases:
- Official paper: https://arxiv.org/abs/2609.26313
- Full-text retrieval: https://arxiv.org/pdf/2609.26313v1
- Venue verification: https://2026.ieee-iros.org/program/contributed_talks/#d6dc87:1051
- Code/Project: https://github.com/Loule0-0/SafeLoop/tree/release/safeloop
- Code: https://github.com/Loule0-0/SafeLoop/tree/release/safeloop
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다. 평가 노트의 측정 조건도 해당 표·절에서 확인했다.

## Problem and Importance

SafeLoop는 영상과 고유수용감각에서 충돌·물체 실패의 확률과 남은 시간을 예측해 고정된 VLA의 행동을 계속하거나 안전한 관절 자세로 후퇴시킨다. [PDF 1쪽](https://arxiv.org/pdf/2609.26313v1#page=1)

## Core Idea and Contribution

- 위험 유형별 예측을 이용해 계속 실행, 안전 자세 저장, 후퇴 중 하나를 고르고 되돌아간 뒤 정책에 다시 질의한다. [PDF 3쪽](https://arxiv.org/pdf/2609.26313v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2609.26313v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5)
- LIBERO 조작과 실물 과제에서 충돌·물체 실패와 작업 성공을 함께 측정해 후퇴 전략을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## Observation–State–Action Interface

관측·시간 context → risk → 실행 중단/역행.

## Evaluation Scope and Claim Boundary

시뮬레이션은 LIBERO 24개 과제에 시드 16개씩을 사용해 방법별 384회 시행했다. 실물 검증은 세 과제를 각각 25회 수행해 위해 사건과 작업 성공을 기록했다. [PDF 5쪽](https://arxiv.org/pdf/2609.26313v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.26313v1#page=7)

## 검색 태그 근거

시각·상태 이력, 지시와 예정 행동으로 위험을 예측하고, 비대칭 강화학습으로 계속 실행·체크포인트 저장·되돌리기 중 하나를 고른다. 학습용 critic의 특권 정보와 실행 시 감독 정책의 관측을 구분했다. [원문 4쪽](https://arxiv.org/pdf/2609.26313v1#page=4) · [원문 6쪽](https://arxiv.org/pdf/2609.26313v1#page=6)

## Why This Paper Is Here — Researcher Interpretation

D3에서 rollback이 세계 상태를 되돌린다는 잘못된 가정을 피할 직접 비교군이다.

## Verification Boundary

joint history와 world state 구분, detector labels, collision 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
