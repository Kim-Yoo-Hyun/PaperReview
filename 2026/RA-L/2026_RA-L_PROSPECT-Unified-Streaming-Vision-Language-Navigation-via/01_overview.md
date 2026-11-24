# PROSPECT: Unified Streaming Vision-Language Navigation via Semantic–Spatial Fusion and Latent Predictive Representation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

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
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

PROSPECT는 연속 관측의 3차원 공간 특징과 영상 의미 특징을 결합하고, 다음 시점의 두 특징을 예측하도록 학습한 언어 지시 내비게이션 정책이다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=3)

## Core Idea and Contribution

- CUT3R 공간 특징과 SigLIP 시각 특징을 교차 주의로 결합하고, 훈련 중 동결한 교사의 다음 잠재 표현을 예측하는 보조 목표를 사용한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=4)
- VLN-CE 벤치마크와 실물 주행에서 평가하고 조명 변화와 긴 경로에서의 행동을 분석했다. 배포 시에는 보조 예측 분기를 실행하지 않는다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11673313#page=7)

## Observation–State–Action Interface

영상 stream·언어 → semantic-spatial state → navigation action; predictive branch는 학습 보조다.

## Evaluation Scope and Claim Boundary

VLN-CE와 실제 항법을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11673313/) · [저자 project/code](https://github.com/Debactor/PROSPECT).

## Why This Paper Is Here — Researcher Interpretation

정책 내부 표현·미래 예측이 항법에 주는 효과를 RL 기여와 분리할 기준이다.

## Verification Boundary

미래 target 접근, inference 비용 산정, map/history memory 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
