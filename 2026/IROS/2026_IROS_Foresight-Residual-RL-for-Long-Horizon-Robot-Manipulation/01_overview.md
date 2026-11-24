# Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IROS
- Authors: Yuhan Liu, Xinyu Zhang, Litao Liu, Abdeslam Boularias
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: robot-learning, imitation-learning, Control
- Aliases:
- Official paper: https://arxiv.org/abs/2607.16506
- Full-text retrieval: https://arxiv.org/pdf/2607.16506v1
- Venue verification: https://2026.ieee-iros.org/program/contributed_talks/#8d1ad5:4421
- Code/Project: not identified
- Code: not identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다. 평가 노트의 측정 조건도 해당 표·절에서 확인했다.

## Problem and Importance

Foresight Residual RL은 조립의 한 단계를 마친 상태에서 다음 단계가 성공할 가능성을 추정해 고정된 VLA 위의 잔차 정책을 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2607.16506v1#page=1)

## Core Idea and Contribution

- 다음 단계 시행에서 얻은 결과로 마지막 상태 영상의 가치를 학습하고 뒤 단계부터 앞 단계로 성공 보상을 조정한다. [PDF 3쪽](https://arxiv.org/pdf/2607.16506v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2607.16506v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2607.16506v1#page=5)
- Isaac Gym의 렌치 조립 과제에서 단계별 성공과 전체 조립 성공을 따로 비교해 단계 사이 인계 상태의 영향을 측정했다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2607.16506v1#page=8)

## Observation–State–Action Interface

VLA 행동·종료 state → 미래 성공 예측 → residual policy 학습.

## Evaluation Scope and Claim Boundary

표 II의 각 단계는 전문가 상태에서 시작하고 전체 작업은 처음부터 실행한다. Isaac Gym의 전체 조립 성공률은 기본 잔차 정책 54.5%, 다음 단계 성공 가능성을 보상에 반영한 정책 85.6%다. [PDF 6쪽](https://arxiv.org/pdf/2607.16506v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2607.16506v1#page=7)

## Why This Paper Is Here — Researcher Interpretation

D2에서 후속 실행 가능성을 reward에 넣는 좁은 RL 주장도 제한한다.

## Verification Boundary

stage 경계, privileged state, backward training 순서, 실제 robot 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
