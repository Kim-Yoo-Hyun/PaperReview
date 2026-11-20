# Performant robotic manipulation with real-world reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. Science Robotics 2026 status는 저자 공식 발표/code로 확인; publisher 직접 열기 실패.

## Problem and Importance

실제 manipulation에서 imitation policy의 성공률·속도·강건성을 실용적인 RL 학습으로 개선하는 문제다.

## Core Idea and Contribution

Diffusion visuomotor policy의 imitation-to-RL 학습과 빠른 controller 실행을 연결하는 real-world RL framework를 제안한다.

## Observation–State–Action Interface

Visual observation → diffusion/flow visuomotor policy → robot action; offline/online 학습과 deployment 추론을 구분한다.

## Evaluation Scope and Claim Boundary

저자 공식 repository와 저널 abstract는 pushing, pouring, cloth/long-horizon manipulation 등을 포함한 실제 robot 평가를 설명한다. 프로토콜별 수치는 본문 확인 필요.

근거: [공식 paper/abstract](https://doi.org/10.1126/scirobotics.aed6267) · [저자 project/code](https://github.com/Lei-Kun/RL-100). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / real-robot system. Diffusion policy에서 imitation→offline/online RL과 빠른 실행을 연결한다. HIL-SERL/DPPO와 비교해 실제 interaction 비용·latency·복구를 읽을 가치가 크다. 제목/이름의 “100”을 모든 환경에서의 무실패 보장으로 해석하지 않는다.

## Verification Boundary

Evaluation success denominator, human intervention, offline/online 단계 및 distillation 손실을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
