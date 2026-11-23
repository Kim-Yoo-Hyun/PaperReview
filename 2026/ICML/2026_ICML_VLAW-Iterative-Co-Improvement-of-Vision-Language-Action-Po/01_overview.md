# VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
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
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

VLAW는 실제 정책 실행으로 행동 조건부 영상 세계 모델을 개선하고, 개선된 모델이 생성한 궤적을 다시 VLA 학습에 사용한다. [PDF 1쪽](https://arxiv.org/pdf/2602.12063v2#page=1)

## Core Idea and Contribution

- 성공 시연에서 잘 보이지 않았던 실패·접촉 상태를 실물 실행으로 수집해 세계 모델을 갱신한 뒤 정책 학습용 합성 경험을 추가한다. [PDF 3쪽](https://arxiv.org/pdf/2602.12063v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2602.12063v2#page=4)
- 실물 조작에서 기본 정책의 성능과 합성 궤적 추가 효과를 나눠 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2602.12063v2#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2602.12063v2#page=7)

## Observation–State–Action Interface

VLA action-conditioned video model → synthetic rollout; real rollout → world-model update → policy update.

## Evaluation Scope and Claim Boundary

ICML abstract는 실제 robot의 여러 downstream task에서 base policy 및 synthetic-rollout 학습 효과를 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/guo26i.html) · [저자 project/code](https://sites.google.com/view/vla-w). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. 실제 rollout으로 world model의 failure coverage를 개선하고 synthetic rollout으로 policy를 개선하는 반복 구조다. 이미 등록된 Ctrl-World/WMPO와 연결해 model bias와 real-data budget을 비교한다. Abstract만으로 특정 RL optimizer를 단정하지 않는다.

## Verification Boundary

Policy update objective, 실패 data 구성, synthetic/real 혼합비와 evaluation leakage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
