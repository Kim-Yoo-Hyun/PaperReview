# RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2025 / arXiv
- Authors: Hongyin Zhang, Shuo Zhang, Junxi Jin, Qixin Zeng, Runze Li, Donglin Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, RL, robustness, regularization
- Official paper: https://arxiv.org/abs/2511.01331
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-05: v2 §4.2–4.3, Algorithm 1; §5 범위. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RobustVLA는 관측과 제어의 작은 교란에 VLA가 과도하게 반응하는 것을 줄이도록 강화학습 후처리의 목적함수를 설계한다. [PDF 1쪽](https://arxiv.org/pdf/2511.01331v2#page=1)

## Core Idea and Contribution

- 관측에 대한 정책의 로그확률 야코비안을 제약하고 같은 관측에서 현재 정책과 직전 기준 정책이 내는 평균 행동의 차이에 벌점을 준다. [PDF 5쪽](https://arxiv.org/pdf/2511.01331v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2511.01331v2#page=6)
- LIBERO의 시각 및 실행 교란 조건에서 기준 정책과 비교하고 두 정규화 항이 강건성과 행동에 주는 효과를 따로 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2511.01331v2#page=6) · [PDF 9쪽](https://arxiv.org/pdf/2511.01331v2#page=9)

## Scope and Limitation

ICLR under-review PDF는 확인했으나 채택을 확인하지 못해 arXiv로 등록한다. 2510.00037의 동명 Multi-Modal Perturbations 논문과 별개다.

## Why This Paper Is Here — Researcher Interpretation

FEEDBACK에서 단순 Jacobian 억제·강건 RL을 새 방법으로 제안하지 않도록 하는 직접 비교.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2511.01331v2), v2 §4.2–4.3, Algorithm 1; §5 범위.
