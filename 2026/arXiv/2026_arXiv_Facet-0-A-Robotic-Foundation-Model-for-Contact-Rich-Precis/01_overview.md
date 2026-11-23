# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v1 abstract/project/code 공개 범위 확인. 전체 시스템을 단일 actor end-to-end RL로 요약하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

정밀 조립에서 행동의 접촉 결과를 예측하고 실패에 적응해야 한다.

## Core Idea and Contribution

Joint action–wrench proposal과 distributional critic으로 접촉 결과를 학습하며 bounded actor가 현장 적응한다.

## Observation–State–Action Interface

Causal wrench 이력·vision-language·kinematics → 동작과 예측 wrench; wrench는 명령이 아니다.

## Evaluation Scope and Claim Boundary

세 embodiment의 force-synchronized corpus와 정밀 컴퓨터 조립 과제를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.01596) · [저자 project/code](https://pine-lab-ntu.github.io/facet-0/) · [공식 code](https://github.com/PINE-Lab-NTU/FACET). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Action–wrench 예측·가치·RL 결합 자체의 중복을 점검할 직접 경쟁 선행이다.

## Verification Boundary

Frozen backbone/actor 경계, task adaptation 비용, 데이터 누출을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
