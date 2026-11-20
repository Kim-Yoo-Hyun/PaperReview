# VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yanjiang Guo, Tony Lee, Lucy Xiaoyang Shi, Jianyu Chen, Percy Liang, Chelsea Finn
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: world-model, online-interaction, failure-data
- Aliases: VLAW
- Official paper: https://proceedings.mlr.press/v306/guo26i.html
- Venue verification: https://proceedings.mlr.press/v306/guo26i.html
- Code/Project: https://sites.google.com/view/vla-w
- Code: https://github.com/Robert-gyj/Ctrl-World
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Demonstration 중심으로 학습한 world model은 실패 interaction과 작은 contact detail을 충분히 표현하지 못해 policy improvement에 제약이 생긴다.

## Core Idea and Contribution

실제 rollout으로 action-conditioned video world model을 개선하고 그 synthetic rollout으로 VLA를 개선하는 반복 학습을 제안한다.

## Observation–State–Action Interface

VLA action-conditioned video model → synthetic rollout; real rollout → world-model update → policy update.

## Evaluation Scope and Claim Boundary

ICML abstract는 실제 robot의 여러 downstream task에서 base policy 및 synthetic-rollout 학습 효과를 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/guo26i.html) · [저자 project/code](https://sites.google.com/view/vla-w). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. 실제 rollout으로 world model의 failure coverage를 개선하고 synthetic rollout으로 policy를 개선하는 반복 구조다. 이미 등록된 Ctrl-World/WMPO와 연결해 model bias와 real-data budget을 비교한다. Abstract만으로 특정 RL optimizer를 단정하지 않는다.

## Verification Boundary

Policy update objective, 실패 data 구성, synthetic/real 혼합비와 evaluation leakage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
