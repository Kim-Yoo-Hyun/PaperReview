# SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Zihan Zhou, Animesh Garg, Dieter Fox, Caelan Reed Garrett, Ajay Mandlekar
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: TAMP, imitation-learning, reinforcement-learning, long-horizon
- Aliases: SPIRE
- Official paper: https://proceedings.mlr.press/v270/zhou25a.html
- Venue verification: https://proceedings.mlr.press/v270/zhou25a.html
- Code/Project: https://sites.google.com/view/spire-corl-2024
- Code: project_only
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  CoRL 2024 event; PMLR volume 270 published 2025. Registry year uses event year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

장기 접촉 조작 전체를 시연이나 RL만으로 학습하면 탐색과 시연 비용이 커진다.

## Core Idea and Contribution

TAMP로 작은 학습 문제를 만들고 planning context에 맞춘 IL·RL 학습을 결합한다.

## Observation–State–Action Interface

상위 task/motion plan → 학습 하위 정책 → 접촉 조작; 계층형 경계를 유지한다.

## Evaluation Scope and Claim Boundary

장기·접촉 중심 조작 문제 집합에서 planning·IL·RL 결합 시스템들을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25a.html) · [저자 project/code](https://sites.google.com/view/spire-corl-2024). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 VLA 내부 RL이 계층형 분해보다 어떤 비용·일반화 이점을 주는지 비교하는 시스템 대안이다.

## Verification Boundary

planner의 상태·기하 접근, 하위 문제 성공 분포, 실로봇 평가 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
