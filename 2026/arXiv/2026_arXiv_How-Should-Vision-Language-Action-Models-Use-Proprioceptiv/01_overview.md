# How Should Vision-Language-Action Models Use Proprioceptive State?

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Yiren Zhao, Ziyang Chen, Ziyang Rao, Pengteng Li, He Zhang, Weiyu Guo, Yandong Guo, Rushi Dai
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://arxiv.org/abs/2608.03052
- Venue verification: https://arxiv.org/abs/2608.03052
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 같은 VLA에서 로봇 상태를 어디에 넣고 어느 길이의 이력을 사용할 때 폐루프 조작이 개선되는지 비교했다. [PDF 1쪽](https://arxiv.org/pdf/2608.03052v1#page=1)

## Core Idea and Contribution

- 백본·학습 데이터·행동 표현을 고정하고 상태를 텍스트나 시각언어 입력에 넣는 방식과 행동 생성기에 직접 주는 방식을 비교했다. [PDF 3쪽](https://arxiv.org/pdf/2608.03052v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2608.03052v1#page=4)
- 실제 과거 상태를 넣은 경우와 현재 상태를 같은 개수만큼 반복한 경우를 비교해 시간 변화 자체가 복합 과제에 주는 이득을 분리했다. [PDF 6쪽](https://arxiv.org/pdf/2608.03052v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2608.03052v1#page=7)

## Observation–State–Action Interface

언어·영상·state/history → action chunk.

## Evaluation Scope and Claim Boundary

45 atomic 및 20 composite task 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.03052) · 저자 프로젝트·코드 주소 미확인. 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

D1에서 state 사용과 history 효과를 먼저 입증할 NEXT prerequisite다.

## Verification Boundary

world-frame localization 포함 여부, native state 사용, checkpoint 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
