# Learning Human Objectives by Evaluating Hypothetical Behavior

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Siddharth Reddy, Anca Dragan, Sergey Levine, Shane Legg, Jan Leike
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reward-learning, robot-learning, evaluation
- Aliases: ReQueST
- Official paper: https://proceedings.mlr.press/v119/reddy20a.html
- Venue verification: https://proceedings.mlr.press/v119/reddy20a.html
- Code/Project: https://github.com/rddy/ReQueST
- Code: https://github.com/rddy/ReQueST
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

적은 human feedback으로 reward를 학습한다.

## Core Idea and Contribution

가상 행동을 생성하고 평가를 받아 human objective를 추정한다.

## Observation–State–Action Interface

모델이 만든 hypothetical trajectory → expert feedback → reward model.

## Evaluation Scope and Claim Boundary

Navigation·driving 성격의 simulated task를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v119/reddy20a.html) · [저자 project/code](https://github.com/rddy/ReQueST). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C4에서 query 선택·reward refinement의 오래된 직접 선행이다.

## Verification Boundary

가상 trajectory 실현 가능성, feedback 형태, model bias을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
