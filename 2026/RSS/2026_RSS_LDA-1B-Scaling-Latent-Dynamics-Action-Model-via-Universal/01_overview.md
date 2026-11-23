# LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Jiangran Lyu, Kai Liu, Xuheng Zhang, Haoran Liao, Yusen Feng, Wenxuan Zhu, Tingrui Shen, Jiayi Chen, Jiazhao Zhang, Yifei Dong, Cui Wenbo, Senmao Qi, Shuo Wang, Yixin Zheng, Mi Yan, Xuesong Shi, Haoran Li, Dongbin Zhao, Ming-Yu Liu, Zhizheng Zhang, Li Yi, Yizhou Wang, He Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: generalist-policy, latent-dynamics, heterogeneous-data, world-model
- Aliases: LDA-1B
- Official paper: https://roboticsproceedings.org/rss22/p210.html
- Venue verification: https://roboticsproceedings.org/rss22/p210.html
- Code/Project: https://github.com/jiangranlv/LDA-1B
- Code: https://github.com/jiangranlv/LDA-1B
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

행동 모방만으로는 품질이 다양한 사람·로봇 데이터의 동역학 정보를 활용하기 어렵다.

## Core Idea and Contribution

구조화된 시각 latent에서 dynamics·policy·forecasting을 공동 학습하고 이질적 데이터를 통합한다.

## Observation–State–Action Interface

비동기 vision·action → multimodal diffusion transformer → 행동·미래 표현.

## Evaluation Scope and Claim Boundary

Simulation과 실제 contact-rich·dexterous·long-horizon 조작을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p210.html) · [저자 project/code](https://github.com/jiangranlv/LDA-1B). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 모델의 행동·세계 예측 공유를 새 기여로 제안하기 전에 비교할 핵심 구조다.

## Verification Boundary

저품질 데이터 정의, 데이터 역할별 objective, action/vision rate, 학습 데이터 중복을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
