# CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Jiange Yang, Yansong Shi, Haoyi Zhu, Mingyu Liu, Kaijing Ma, Yating Wang, Gangshan Wu, Tong He, Limin Wang
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: latent-motion, human-video, representation-learning, robot-data
- Aliases: CoMo
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html
- Code/Project: https://github.com/MCG-NJU/CoMo
- Code: https://github.com/MCG-NJU/CoMo
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

CoMo는 행동 라벨이 없는 인터넷 영상에서 연속적인 잠재 움직임을 학습해 로봇 정책의 추가 훈련 신호로 사용한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.pdf#page=1)

## Core Idea and Contribution

- 초기 단계에서 프레임 차이를 취하고 가까운 미래와 시간을 반전한 영상을 대조해 정적인 배경에 의존하는 표현을 억제한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.pdf#page=4)
- 학습된 표현으로 보지 못한 영상에 의사 행동을 붙여 로봇 자료와 공동학습하고 시뮬레이션 및 실물에서 확산·자기회귀 정책을 비교했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.pdf#page=8)

## Observation–State–Action Interface

인터넷 영상 → motion pseudo-label → robot policy 공동 학습.

## Evaluation Scope and Claim Boundary

Diffusion·autoregressive 정책의 simulation·실제 조작을 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html) · [저자 project/code](https://github.com/MCG-NJU/CoMo). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

행동 공간의 통합이 discrete/continuous 선택 자체의 효과인지 분리할 비교다.

## Verification Boundary

정적 배경 shortcut, reverse-video negative의 유효성, action-label 없이 가능한 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
