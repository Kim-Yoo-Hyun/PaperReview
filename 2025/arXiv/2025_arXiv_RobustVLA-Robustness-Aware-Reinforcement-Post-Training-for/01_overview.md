# RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue
- Authors: Hongyin Zhang, Shuo Zhang, Junxi Jin, Qixin Zeng, Runze Li, Donglin Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, RL, robustness, regularization
- Official paper: https://arxiv.org/abs/2511.01331
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-05: v2 §4.2–4.3, Algorithm 1; §5 범위. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

Reward 중심 후학습이 관측·실행 교란에 대한 강건성을 충분히 다루지 못하는 문제.

PPO에 observation log-probability Jacobian penalty와 이전 reference 정책 대비 mean-action deviation penalty를 더하고 교란 강도를 조절한다.

## Scope and Limitation

ICLR under-review PDF는 확인했으나 채택을 확인하지 못해 arXiv로 등록한다. 2510.00037의 동명 Multi-Modal Perturbations 논문과 별개다.

## Why This Paper Is Here — Researcher Interpretation

FEEDBACK에서 단순 Jacobian 억제·강건 RL을 새 방법으로 제안하지 않도록 하는 직접 비교.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2511.01331v2), v2 §4.2–4.3, Algorithm 1; §5 범위.
