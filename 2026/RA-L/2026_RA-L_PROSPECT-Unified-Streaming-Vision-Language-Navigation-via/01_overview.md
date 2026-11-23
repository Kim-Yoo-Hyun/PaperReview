# PROSPECT: Unified Streaming Vision-Language Navigation via Semantic–Spatial Fusion and Latent Predictive Representation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RA-L
- Authors: Zehua Fan, Wenqi Lyu, Wenxuan Song, Linge Zhao, Yifei Yang, Xi Wang, Junjie He, Lida Huang, Haiyan Liu, Bingchuan Sun, Guangjun Bao, Xuanyao Mao, Liang Xu, Yan Wang, Feng Gao
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: vision-language-navigation, spatial-representation, predictive-learning
- Aliases: PROSPECT, PROSPECT: Unified Streaming Vision-Language Navigation via Semantic--Spatial Fusion and Latent Predictive Representation
- Official paper: https://api.crossref.org/works/10.1109/LRA.2026.3729462
- Venue verification: https://ieeexplore.ieee.org/document/11673313/
- Code/Project: https://github.com/Debactor/PROSPECT
- Code: https://github.com/Debactor/PROSPECT
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. RA-L 11(11), 13071–13078, November 2026; first online 2026-08-31. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Streaming VLN에서 의미 정보와 공간 정보를 함께 이용하고 미래 상태를 학습할 필요가 있다.

## Core Idea and Contribution

CUT3R 공간 표현과 SigLIP 의미 표현을 융합하고 학습 중 미래 2D·3D latent prediction을 보조 목표로 사용한다.

## Observation–State–Action Interface

영상 stream·언어 → semantic-spatial state → navigation action; predictive branch는 학습 보조다.

## Evaluation Scope and Claim Boundary

VLN-CE와 실제 항법을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11673313/) · [저자 project/code](https://github.com/Debactor/PROSPECT). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

정책 내부 표현·미래 예측이 항법에 주는 효과를 RL 기여와 분리할 기준이다.

## Verification Boundary

미래 target 접근, inference 비용 산정, map/history memory 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
