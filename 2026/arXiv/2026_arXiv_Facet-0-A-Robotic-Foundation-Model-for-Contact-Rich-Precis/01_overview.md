# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Haoyuan Deng, Haichao Liu, Wenkai Guo, Yuan Ling, Zaijia Yang, Yuanjiang Xue, Haosheng Sun, Liangzi Wang, Ziwei Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, wrench-prediction, reinforcement-learning, precision-assembly
- Aliases: Facet-0
- Official paper: https://arxiv.org/abs/2609.01596
- Venue verification: https://arxiv.org/abs/2609.01596
- Code/Project: https://pine-lab-ntu.github.io/facet-0/
- Code: https://github.com/PINE-Lab-NTU/FACET
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v1 abstract/project/code 공개 범위 확인. 전체 시스템을 단일 actor end-to-end RL로 요약하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Facet-0는 정밀 조립에서 각 후보 행동이 유발할 손목 힘·토크를 행동과 함께 예측하고 실제 접촉 결과로 정책을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2609.01596v1#page=1)

## Core Idea and Contribution

- 행동과 예상 힘·토크를 함께 평가하는 비평가를 학습하고, 고정한 표현 위에서 보정 범위가 제한된 정책을 실제 부품에 적응시킨다. [PDF 7쪽](https://arxiv.org/pdf/2609.01596v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2609.01596v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2609.01596v1#page=9)
- 실제 컴퓨터 부품 조립 다섯 과제에서 과제별로 적응한 시스템의 평균 성공률 82%와 논문이 비교한 가장 높은 기준선의 15%를 보고했다. [PDF 10쪽](https://arxiv.org/pdf/2609.01596v1#page=10) · [PDF 11쪽](https://arxiv.org/pdf/2609.01596v1#page=11)

## Observation–State–Action Interface

Causal wrench 이력·vision-language·kinematics → 동작과 예측 wrench; wrench는 명령이 아니다.

## Evaluation Scope and Claim Boundary

세 embodiment의 force-synchronized corpus와 정밀 컴퓨터 조립 과제를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.01596) · [저자 project/code](https://pine-lab-ntu.github.io/facet-0/) · [공식 code](https://github.com/PINE-Lab-NTU/FACET). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Action–wrench 예측·가치·RL 결합 자체의 중복을 점검할 직접 경쟁 선행이다.

## Verification Boundary

Frozen backbone/actor 경계, task adaptation 비용, 데이터 누출을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
