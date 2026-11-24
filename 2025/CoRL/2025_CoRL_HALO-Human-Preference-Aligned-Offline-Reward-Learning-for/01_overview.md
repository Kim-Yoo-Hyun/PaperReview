# HALO : Human Preference Aligned Offline Reward Learning for Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / CoRL
- Authors: Gershom Seneviratne, Jianyu An, Sahire Ellahy, Kasun Weerakoon, Mohamed Bashir Elnoor, Jonathan Deepak Kannan, Amogha Thalihalla Sunil, Dinesh Manocha
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reward-learning, human-preference, Navigation, offline-RL
- Aliases: HALO
- Official paper: https://proceedings.mlr.press/v305/seneviratne25a.html
- Venue verification: https://proceedings.mlr.press/v305/seneviratne25a.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

HALO는 로봇의 주행 시연과 이진 주행 피드백에서 시각 보상을 학습해, 같은 보상을 오프라인 정책과 모델 예측 제어에 활용한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf#page=3)

## Core Idea and Contribution

- 참조 행동 주위에서 뽑은 행동에 선호 순위를 부여하고 Plackett–Luce 손실로 영상 조건부 보상 모델을 학습한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf#page=4) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf#page=6)
- Clearpath Husky의 실물 주행에서 학습 보상을 사용한 정책 및 계획기를 비교하고, 목표 도달과 전문가 경로에 대한 궤적 유사성을 평가했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/seneviratne25a/seneviratne25a.pdf#page=8)

## Observation–State–Action Interface

자아시점 영상·행동 후보 → 선호 보상 → offline 정책 또는 MPC.

## Evaluation Scope and Claim Boundary

실제 Clearpath Husky 항법에서 성공·경로 특성을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/seneviratne25a.html).

## Why This Paper Is Here — Researcher Interpretation

항법 VLA-RL에 인간 선호 보상을 붙일 때 참고할 구체적 reward-learning 대안이다.

## Verification Boundary

선호 query 생성·annotation 비용, 후보 sampling 분포, offline/online 데이터 경계을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
