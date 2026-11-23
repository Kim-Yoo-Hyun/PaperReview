# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Chang Guo, Yukun Xie, Bohan Tan, Zheng Chang, Zhaokai Yin, Qianli Ma, Yingqiao Wang, Chao Liang, Zhipeng Zhang
- Category: Benchmarks and Datasets
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-evaluation, Benchmark, policy-comparison
- Aliases:
- Official paper: https://arxiv.org/abs/2609.25636
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://github.com/AutoLab-SAI-SJTU/RoboFollow
- Code: https://github.com/AutoLab-SAI-SJTU/RoboFollow
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 공식 OpenReview 검색 API의 Conference venueid·CoRL 2026 Poster를 확인했다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RoboFollow는 한 장면에서 여러 행동이 가능하도록 설계해 로봇이 언어 지시를 실제로 따르는지 측정한다. [PDF 1쪽](https://arxiv.org/pdf/2609.25636v1#page=1)

## Core Idea and Contribution

- 관측만으로 과제를 유추하기 어렵게 만들고 지시된 의도를 선택한 단계와 그 행동을 실행한 단계의 점수를 분리했다. [PDF 2쪽](https://arxiv.org/pdf/2609.25636v1#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2609.25636v1#page=3)
- VLA와 세계 행동 모델을 비교해 단순 조건에서의 성공이 배치·의미가 달라진 조건에서의 지시 이행으로 이어지는지 검증했다. [PDF 1쪽](https://arxiv.org/pdf/2609.25636v1#page=1) · [PDF 8쪽](https://arxiv.org/pdf/2609.25636v1#page=8)

## Observation–State–Action Interface

Scene·다양한 instruction → policy rollout → intent/execution 판정.

## Evaluation Scope and Claim Boundary

Simulation benchmark와 제한된 실제 검증을 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=A9AQjk3dAt) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다.

## Verification Boundary

scene entropy, evaluator oracle, task infeasibility, real-robot coverage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
