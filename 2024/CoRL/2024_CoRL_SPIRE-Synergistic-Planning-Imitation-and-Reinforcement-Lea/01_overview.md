# SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2024 / CoRL
- Authors: Zihan Zhou, Animesh Garg, Dieter Fox, Caelan Reed Garrett, Ajay Mandlekar
- 저자 판본: 학회 서지와 표기가 다른 저자의 인쇄명은 Caelan Garrett이다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=1) · [학회 서지](https://proceedings.mlr.press/v270/zhou25a.html)
- Category: Planning and Long-Horizon Reasoning
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: TAMP, imitation-learning, reinforcement-learning, long-horizon
- Aliases: SPIRE, SPIRE: Synergistic Planning, Imitation, and Reinforcement for Long-Horizon Manipulation
- 게재본 표제: SPIRE: Synergistic Planning, Imitation, and Reinforcement for Long-Horizon Manipulation [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=1) · [학회 서지](https://proceedings.mlr.press/v270/zhou25a.html)
- Official paper: https://proceedings.mlr.press/v270/zhou25a.html
- Venue verification: https://proceedings.mlr.press/v270/zhou25a.html
- Code/Project: https://sites.google.com/view/spire-corl-2024
- Code: project_only
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

SPIRE는 과제·동작 계획으로 긴 조작을 분해한 뒤, 접촉이 까다로운 하위 동작을 시연으로 초기화하고 강화학습으로 개선한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=1) · [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=2)

## Core Idea and Contribution

- 계획기가 처리할 구간과 정책이 맡을 구간을 나누고, 정책이 실제 계획 안에서 만나는 상태를 이용해 하위 동작의 학습을 구성한다. [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=2) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=5)
- 조립·커피 준비·도구 걸기 등에서 성공률과 성공한 에피소드의 길이를 비교하고, 필요한 시연 수와 표본 선택 방식도 분석했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhou25a/zhou25a.pdf#page=8)

## Observation–State–Action Interface

상위 task/motion plan → 학습 하위 정책 → 접촉 조작; 계층형 경계를 유지한다.

## Evaluation Scope and Claim Boundary

장기·접촉 중심 조작 문제 집합에서 planning·IL·RL 결합 시스템들을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25a.html) · [저자 project/code](https://sites.google.com/view/spire-corl-2024).

## Why This Paper Is Here — Researcher Interpretation

단일 VLA 내부 RL이 계층형 분해보다 어떤 비용·일반화 이점을 주는지 비교하는 시스템 대안이다.

## Verification Boundary

planner의 상태·기하 접근, 하위 문제 성공 분포, 실로봇 평가 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
