# Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Zhilong Zhang, Haoxiang Ren, Yihao Sun, Yifei Sheng, Haonan Wang, Zhichao Wu, Haoxin Lin, Pierre-Luc Bacon, Yang Yu
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: model-based-RL, multi-view, branched-rollout
- Aliases: VLA-MBPO
- Official paper: https://proceedings.mlr.press/v306/zhang26ez.html
- Venue verification: https://proceedings.mlr.press/v306/zhang26ez.html
- Code/Project: https://github.com/LAMDA-RL/VLA-MBPO
- Code: https://github.com/LAMDA-RL/VLA-MBPO
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Pixel-level interactive world model에서 VLA RL을 수행할 때 multi-view 불일치와 rollout 오차 누적이 발생한다.

## Core Idea and Contribution

Unified multimodal model 기반 dynamics, interleaved multi-view decoding 및 chunk-level branched rollout을 결합한다.

## Observation–State–Action Interface

Multi-view observation + VLA action chunk → imagined next observation/reward → RL update.

## Evaluation Scope and Claim Boundary

공식 ICML abstract는 simulation과 real-world task에서 policy 성능 및 sample efficiency 평가를 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26ez.html) · [저자 project/code](https://github.com/LAMDA-RL/VLA-MBPO). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Multi-view consistency와 chunk-level branched rollout으로 world-model RL의 오차 누적을 다룬다. WMPO/WorldGym을 읽을 때 직접 비교해야 할 누락 논문이다.

## Verification Boundary

Multi-view conditioning, rollout branching state 분포, reward model과 실제 transfer 검증을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
