# How Should Vision-Language-Action Models Use Proprioceptive State?

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yiren Zhao, Ziyang Chen, Ziyang Rao, Pengteng Li, He Zhang, Weiyu Guo, Yandong Guo, Rushi Dai
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://arxiv.org/abs/2608.03052
- Venue verification: https://arxiv.org/abs/2608.03052
- Code/Project: https://arxiv.org/abs/2608.03052
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

VLA에 state를 어디에, 얼마나 긴 history로 넣어야 하는지 비교한다.

## Core Idea and Contribution

같은 flow-matching backbone에서 다섯 state interface와 history 길이를 통제한다.

## Observation–State–Action Interface

언어·영상·state/history → action chunk.

## Evaluation Scope and Claim Boundary

45 atomic 및 20 composite task 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.03052) · [저자 project/code](https://arxiv.org/abs/2608.03052). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1에서 state 사용과 history 효과를 먼저 입증할 NEXT prerequisite다.

## Verification Boundary

world-frame localization 포함 여부, native state 사용, checkpoint 공개을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
