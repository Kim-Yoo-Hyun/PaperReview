# General Process Reward Modeling for Robotic Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: process-reward, multi-view, reward-shaping, robot-RL
- Aliases: Dopamine-Reward,  Dopamine-RL, Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation, Dopamine-RL
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html
- Code/Project: https://robo-dopamine.github.io/
- Code: https://github.com/FlagOpen/Robo-Dopamine
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. CVPR title은 General Process Reward Modeling; preprint Robo-Dopamine과 중복 등록하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

진행 보상이 단계·시점을 잘못 판단하면 정책이 보상만 높이는 행동을 배울 수 있다.

## Core Idea and Contribution

다시점 step-aware 보상 모델과 policy-invariant reward shaping을 제안한다.

## Observation–State–Action Interface

다시점 관측·과제 진행 → dense reward → robot RL.

## Evaluation Scope and Claim Boundary

Simulation·실제 조작에서 reward 평가와 policy 학습을 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) · [저자 project/code](https://robo-dopamine.github.io/) · [공식 code](https://github.com/FlagOpen/Robo-Dopamine). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL 보상 설계와 HINDSIGHT의 대안 설명을 검토할 직접 선행이다.

## Verification Boundary

보존 정리의 가정, 종료 처리, multi-view 특권, task별 추가 시연을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
