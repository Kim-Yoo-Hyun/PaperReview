# TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Huaihang Zheng, Yi Yang, Kai Ma, Shenglin Xu, Tian Xie, Guozheng Li, Xiangyu Wang, Yiren Ma, Si Liu, Yinian Mao, Baoxu Liu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, tactile, online-RL, intervention
- Aliases: TORL-VLA
- Official paper: https://arxiv.org/abs/2606.09337
- Venue verification: https://arxiv.org/abs/2606.09337
- Code/Project: https://torl-vla.github.io/
- Code: not_released
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 최신 v3 abstract 확인; N1 본문 대조는 v1이다. Project는 TORL code Coming Soon이며 연결된 RLT 재현 코드는 TORL 구현으로 간주하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

TORL-VLA는 촉각에서 추정한 힘·토크로 VLA의 기준 동작을 만들고 온라인 강화학습을 통해 실제 접촉 상태에 맞춰 동작을 수정한다. [PDF 1쪽](https://arxiv.org/pdf/2606.09337v3#page=1)

## Core Idea and Contribution

- 기준 모형이 행동과 미래 힘·토크를 예측하고, 사람의 개입 이후 발생한 성공을 직전 정책 행동의 공적으로 돌리지 않도록 비평가를 학습한다. [PDF 4쪽](https://arxiv.org/pdf/2606.09337v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2606.09337v3#page=5)
- 실제 걸쇠 조작·컵 배치·달걀 다루기에서 하위 과제와 전체 과제 성공을 구분해 측정하고 힘 정보와 개입 처리가 성능에 미치는 영향을 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2606.09337v3#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2606.09337v3#page=8)

## Observation–State–Action Interface

촉각 유래 wrench·상태 → reference action/future wrench → 실행 행동 보정.

## Evaluation Scope and Claim Boundary

실제 latch·컵·달걀 조작의 부분/전체 과제와 시간 제한 효율을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.09337) · [저자 project/code](https://torl-vla.github.io/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

접촉 VLA의 online RL과 사람 개입 credit 처리가 이미 다뤄졌음을 확인할 비교다.

## Verification Boundary

개입 전후 critic mask, latency, base/보정 정책 학습 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · 저자는 TORL-VLA 코드를 공개 예정으로 표시한다. 별도 링크는 RLT 기준선의 재구현이다. [저자 공개 안내](https://torl-vla.github.io/)
