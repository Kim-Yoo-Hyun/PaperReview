# SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Meng Li, Zhen Zhao, Zhengping Che, Fei Liao, Kun Wu, Zhiyuan Xu, Pei Ren, Zhao Jin, Ning Liu, Jian Tang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, task-switching, contact-phase, imitation-learning
- Aliases:
- Official paper: https://arxiv.org/abs/2506.03574
- Full-text retrieval: https://arxiv.org/pdf/2506.03574v1
- Venue verification: https://arxiv.org/abs/2506.03574
- Code/Project: https://switchvla.github.io/
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

SwitchVLA는 작업 도중 지시가 바뀌면 현재 접촉 단계와 새 지시를 이용해 로봇의 행동을 전환한다. [PDF 1쪽](https://arxiv.org/pdf/2506.03574v1#page=1)

## Core Idea and Contribution

- 시연의 접촉 사건에서 진행 단계를 추출해 별도의 전환 전용 시연 없이 실행 상태에 따른 행동열을 학습한다. [PDF 4쪽](https://arxiv.org/pdf/2506.03574v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2506.03574v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2506.03574v1#page=6)
- 같은 지시를 유지하거나 실행 중 바꾸는 조건을 구분해 시뮬레이션과 실제 로봇에서 전환 성공을 평가했다. [PDF 7쪽](https://arxiv.org/pdf/2506.03574v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2506.03574v1#page=8)

## Observation–State–Action Interface

언어·관측·execution state → forward/rollback/advance action.

## Evaluation Scope and Claim Boundary

실행 중 task switching 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2506.03574) · [저자 project/code](https://switchvla.github.io/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

시연 영상에서 VLM으로 그리퍼 접촉 구간을 표시해 보조 감독으로 쓴다. 정책은 시각·로봇 상태에서 실행 단계를 추정해 지시 유지·전환에 필요한 행동을 예측한다. 접촉 표시는 힘이나 촉각 센서 측정값과 구분된다. [원문 5쪽](https://arxiv.org/pdf/2506.03574v1#page=5) · [원문 6쪽](https://arxiv.org/pdf/2506.03574v1#page=6)

## Why This Paper Is Here — Researcher Interpretation

D3의 일반 task interruption 주장을 제한하는 REFERENCE다.

## Verification Boundary

접촉 라벨의 오차율, 되돌리기가 가능한 접촉 조건, 정식 게재 여부를 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
