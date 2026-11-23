# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Ziyi Chen, Yingnan Guo, Zedong Chu, Minghua Luo, Yanfen Shen, Mingchao Sun, Junjun Hu, Shichao Xie, Yang Kuan, Pei Shi, Zhining Gu, Lu Liu, Honglin Han, Xiaolong Wu, Mu Xu, Yu Zhang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: social-navigation, flow-policy, RL
- Aliases: SocialNav
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html
- Code/Project: https://amap-eai.github.io/SocialNav/
- Code: https://github.com/AMAP-EAI/SocialNav
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

SocialNav는 보행자 주변에서 사회적 규범을 추론하는 상위 모델과 실제 주행 궤적을 만드는 하위 모델을 함께 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 사회적 판단 예시와 전문가 궤적으로 모방학습한 뒤 사회 규범 준수에 보상을 주는 SAFE-GRPO로 흐름 기반 정책을 개선한다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf#page=5)
- 전용 SocNav 벤치마크와 실제 로봇에서 목표 도달과 사회적 규범 준수를 나누어 평가했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

Visual/semantic context → social reasoning/traversability → flow trajectory policy → navigation.

## Evaluation Scope and Claim Boundary

CVF abstract는 SocNav dataset, navigation success와 social compliance 평가를 보고한다. 정확한 metric 정의와 실제 robot trial은 확인 필요.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) · [저자 project/code](https://amap-eai.github.io/SocialNav/). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / dataset. Semantic reasoning과 trajectory generation에 socially compliant reward를 연결한다. NaVILA/VLFM의 task success 중심 비교에 행동 제약을 더한다. 기존 **SocialNav-SUB는 별도 benchmark**다.

## Verification Boundary

Social label/reward 정의, 지역/환경별 규범 변화, reward hacking 및 evaluation split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
