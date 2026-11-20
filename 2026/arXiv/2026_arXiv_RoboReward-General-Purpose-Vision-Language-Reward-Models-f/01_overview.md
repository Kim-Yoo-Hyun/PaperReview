# RoboReward: General-Purpose Vision-Language Reward Models for Robotics

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Tony Lee, Andrew Wagenmaker, Karl Pertsch, Percy Liang, Sergey Levine, Chelsea Finn
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: reward-learning, robot-learning, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2601.00675
- Venue verification: https://arxiv.org/abs/2601.00675
- Code/Project: https://crfm.stanford.edu/helm/robo-reward-bench/
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.
- Metadata refresh: 2026-10-25 arXiv v2와 저자가 연결한 HELM project URL 확인. 목적지 HTML은 client-rendered shell이며 code/data/checkpoint 공개 범위는 검증하지 않았다. OpenReview challenge로 정식 acceptance를 확인하지 못해 arXiv 유지.

## Problem and Importance

범용 robot task 성공도를 평가할 VLM reward 모델과 기준을 만든다.

## Core Idea and Contribution

Robot 자료와 counterfactual negative를 사용해 reward 모델·benchmark를 구성한다.

## Observation–State–Action Interface

지시·trajectory → task completion reward.

## Evaluation Scope and Claim Boundary

공개 robot 자료의 reward 평가와 실제 robot RL을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.00675). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다.

## Verification Boundary

counterfactual label 검증, temporal clipping, policy shift, benchmark leakage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
