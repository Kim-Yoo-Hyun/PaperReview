# Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yuhan Liu, Xinyu Zhang, Litao Liu, Abdeslam Boularias
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: robot-learning, imitation-learning, Control
- Aliases:
- Official paper: https://arxiv.org/abs/2607.16506
- Venue verification: https://2026.ieee-iros.org/program/contributed_talks/#8d1ad5:4421
- Code/Project: not identified
- Code: not identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. IROS 저자 표기만으로 venue를 승격하지 않음; 공식 acceptance 미확인.

## Problem and Importance

각 subtask의 국소 성공이 후속 task 성공으로 이어지지 않을 수 있다.

## Core Idea and Contribution

Downstream rollout의 성공 예측을 terminal-state 평가에 사용해 residual RL을 연결한다.

## Observation–State–Action Interface

VLA 행동·종료 state → 미래 성공 예측 → residual policy 학습.

## Evaluation Scope and Claim Boundary

Simulation의 여러 단계 manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.16506) · [저자 project/code](https://jaysparrow.github.io/foresight-residual-rl). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2에서 후속 실행 가능성을 reward에 넣는 좁은 RL 주장도 제한한다.

## Verification Boundary

stage 경계, privileged state, backward training 순서, 실제 robot 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
