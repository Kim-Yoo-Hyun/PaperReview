# General Process Reward Modeling for Robotic Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Huajie Tan, Sixiang Chen, Yijie Xu, Zixiao Wang, Cheng Chi, Yuheng Ji, Yaoxu Lyu, Zhongxia Zhao, Xiansheng Chen, Peterson Co, Shaoxuan Xie, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: process-reward, multi-view, reward-shaping, robot-RL
- Aliases: Dopamine-Reward,  Dopamine-RL, Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation, Dopamine-RL
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html
- Code/Project: https://robo-dopamine.github.io/
- Code: https://github.com/FlagOpen/Robo-Dopamine
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. CVPR title은 General Process Reward Modeling; preprint Robo-Dopamine과 중복 등록하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Dopamine-Reward는 여러 시점의 영상에서 조작의 단계별 진행도를 추정하고 이를 로봇 강화학습의 보상으로 사용한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=2)

## Core Idea and Contribution

- 진행도를 단계별로 이산화하고 여러 카메라의 추정을 결합해 한 시점에서 가려진 동작도 평가하도록 보상 모델을 학습했다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=4)
- 잠재함수 기반 보상으로 학습한 실물 여덟 과제에서 최종 평균 성공률은 95.2%였고, 표 3은 그 성공률의 80%에 도달하기까지의 시행 수를 150회로 보고했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=5) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

다시점 관측·과제 진행 → dense reward → robot RL.

## Evaluation Scope and Claim Boundary

Simulation·실제 조작에서 reward 평가와 policy 학습을 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) · [저자 project/code](https://robo-dopamine.github.io/) · [공식 code](https://github.com/FlagOpen/Robo-Dopamine). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL 보상 설계와 HINDSIGHT의 대안 설명을 검토할 직접 선행이다.

## Verification Boundary

보존 정리의 가정, 종료 처리, multi-view 특권, task별 추가 시연을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
