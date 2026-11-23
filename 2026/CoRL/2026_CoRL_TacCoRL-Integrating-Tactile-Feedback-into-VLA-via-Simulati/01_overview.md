# TacCoRL: Integrating Tactile Feedback into VLA via Simulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CoRL
- Authors: Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su, Yixin Zhu, Yin Yang, Chenfanfu Jiang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, tactile, sim-to-real, reinforcement-learning
- Aliases: TacCoRL
- Official paper: https://arxiv.org/abs/2606.11743
- Venue verification: https://www.corl.org/program/accepted-papers
- Code/Project: https://tac-corl.github.io/
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 저자 project는 CoRL 2026을 표기하지만 공식 proceedings/forum은 이번 검색에서 확인하지 못했다. arXiv 유지. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

TacCoRL은 실물·시뮬레이션 시연으로 촉각을 쓰는 VLA를 초기화하고, 시뮬레이션 접촉 경험을 이용해 실제 양팔 조작을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2606.11743v1#page=1)

## Core Idea and Contribution

- 시뮬레이션에서는 검증 가능한 과제 보상으로 정책을 갱신하면서 실물 궤적의 행동을 모방하는 손실을 함께 적용한다. [PDF 4쪽](https://arxiv.org/pdf/2606.11743v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2606.11743v1#page=5)
- 실물 양팔 네 과제에서 시뮬레이션 강화학습을 거친 시각 전용 정책의 평균 성공률은 50.0%, 촉각도 입력한 정책은 72.5%였다. [PDF 7쪽](https://arxiv.org/pdf/2606.11743v1#page=7)

## Observation–State–Action Interface

영상·언어·촉각 → VLA 행동; 배포 시 privileged simulation state를 쓰지 않는다고 보고한다.

## Evaluation Scope and Claim Boundary

실제 양팔 접촉 과제로 전이를 평가한다. 실제 로봇 online RL을 사용한 결과와 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.11743) · [저자 project/code](https://tac-corl.github.io/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

촉각 추가와 단일 VLA RL 자체가 이미 선행임을 확인할 직접 비교다.

## Verification Boundary

촉각 합성 정합성, real anchor 비용, 물리 변화별 분할을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
