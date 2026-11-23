# TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Code: not identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. 최신 v3 abstract 확인; N1 본문 대조는 v1이다. Project는 TORL code Coming Soon이며 연결된 RLT 재현 코드는 TORL 구현으로 간주하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

접촉 조건이 변하면 offline tactile VLA가 적응하지 못하는 문제를 다룬다.

## Core Idea and Contribution

Wrench-aware VLA의 reference를 online RL 모듈로 보정하고 human intervention 경계를 critic 학습에 반영한다.

## Observation–State–Action Interface

촉각 유래 wrench·상태 → reference action/future wrench → 실행 행동 보정.

## Evaluation Scope and Claim Boundary

실제 latch·컵·달걀 조작의 부분/전체 과제와 시간 제한 효율을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.09337) · [저자 project/code](https://torl-vla.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

접촉 VLA의 online RL과 사람 개입 credit 처리가 이미 다뤄졌음을 확인할 비교다.

## Verification Boundary

개입 전후 critic mask, latency, base/보정 정책 학습 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
