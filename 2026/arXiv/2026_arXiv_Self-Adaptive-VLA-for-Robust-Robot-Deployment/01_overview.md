# Self-Adaptive VLA for Robust Robot Deployment

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Hongxin Zhang, Chunru Lin, Tsun-Hsuan Wang, Zhenjia Xu, Chuang Gan
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://arxiv.org/abs/2609.30092
- Venue verification: https://arxiv.org/abs/2609.30092
- Code/Project: https://icefoxzhx.github.io/self-adaptive-vla/
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Self-Adaptive VLA는 배포 중 관측한 로봇의 동작 이력을 이용해 구동 편향과 관절 센서 오프셋에 적응한다. [PDF 1쪽](https://arxiv.org/pdf/2609.30092v1#page=1)

## Core Idea and Contribution

- 알려진 하드웨어 편차를 보상하도록 전문가 행동을 변환하고, 실행 이력을 압축한 토큰으로 정책의 층 정규화를 조절한다. [PDF 3쪽](https://arxiv.org/pdf/2609.30092v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2609.30092v1#page=4)
- 정밀 양팔·다지 조작에서 하드웨어 편차로 잃은 성능을 얼마나 회복하는지 측정하고 새 작업대에도 배포했다. [PDF 5쪽](https://arxiv.org/pdf/2609.30092v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.30092v1#page=6)

## Observation–State–Action Interface

영상·proprioception·action history → context-conditioned action.

## Evaluation Scope and Claim Boundary

정밀 bimanual·dexterous 작업의 actuation bias와 encoder offset 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.30092) · [저자 project/code](https://icefoxzhx.github.io/self-adaptive-vla/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

D1의 hardware-cause adaptation과 가장 가까운 NEXT 비교군이다.

## Verification Boundary

episode/trial 간 offset 유지, encoder 모델, expert action 보상을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
