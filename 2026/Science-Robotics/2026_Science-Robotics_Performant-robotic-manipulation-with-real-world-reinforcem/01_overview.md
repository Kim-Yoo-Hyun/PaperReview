# Performant robotic manipulation with real-world reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / Science Robotics
- Authors: Kun Lei, Huanyu Li, Dongjie Yu, Zhenyu Wei, Lingxiao Guo, Zhennan Jiang, Ziyu Wang, Shiyu Liang, Huazhe Xu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: real-robot-RL, diffusion-policy, deployment
- Aliases: RL-100
- Official paper: https://api.crossref.org/works/10.1126/scirobotics.aed6267
- Venue verification: https://lei-kun.github.io/
- Code/Project: https://github.com/Lei-Kun/RL-100
- Code: https://github.com/Lei-Kun/RL-100
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.
- 대조 판본: Science Robotics 게재 논문의 요약·기여는 저자 원고 RL-100 v4의 쪽수를 따른다. [원문](https://arxiv.org/pdf/2510.14830v4)

## Problem and Importance

RL-100은 확산 기반 조작 정책에 오프라인·온라인 강화학습과 단일 단계 증류를 적용하고 실제 로봇의 성공률과 완료 시간을 평가했다. [PDF 1쪽](https://arxiv.org/pdf/2510.14830v4#page=1)

## Core Idea and Contribution

- 디노이징 단계에 같은 clipped PPO 목적을 적용해 정책을 갱신하고 일관성 증류로 여러 번의 추론을 한 단계로 줄였다. [PDF 18쪽](https://arxiv.org/pdf/2510.14830v4#page=18) · [PDF 20쪽](https://arxiv.org/pdf/2510.14830v4#page=20)
- 정해진 여덟 실물 과제의 평가 시행에서 1,000회 중 1,000회 성공을 기록했다. 환경이나 동역학을 바꾼 검증은 따로 보고했다. [PDF 1쪽](https://arxiv.org/pdf/2510.14830v4#page=1) · [PDF 14쪽](https://arxiv.org/pdf/2510.14830v4#page=14)

## Observation–State–Action Interface

Visual observation → diffusion/flow visuomotor policy → robot action; offline/online 학습과 deployment 추론을 구분한다.

## Evaluation Scope and Claim Boundary

저자 공식 repository와 저널 abstract는 pushing, pouring, cloth/long-horizon manipulation 등을 포함한 실제 robot 평가를 설명한다. 프로토콜별 수치는 본문 확인 필요.

근거: [공식 paper/abstract](https://doi.org/10.1126/scirobotics.aed6267) · [저자 project/code](https://github.com/Lei-Kun/RL-100). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / real-robot system. Diffusion policy에서 imitation→offline/online RL과 빠른 실행을 연결한다. HIL-SERL/DPPO와 비교해 실제 interaction 비용·latency·복구를 읽을 가치가 크다. 제목/이름의 “100”을 모든 환경에서의 무실패 보장으로 해석하지 않는다.

## Verification Boundary

Evaluation success denominator, human intervention, offline/online 단계 및 distillation 손실을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
