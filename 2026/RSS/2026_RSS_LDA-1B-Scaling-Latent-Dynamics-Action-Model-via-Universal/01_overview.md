# LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LDA-1B는 사람과 로봇 궤적을 함께 사용해 잠재 동역학·정책·시각 예측을 학습하는 로봇 기반 모델이다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p210.pdf#page=1)

## Core Idea and Contribution

- 표준화한 EI-30k 자료를 학습 신호별로 나누고 DINO 잠재 공간과 멀티모달 확산 트랜스포머로 서로 다른 시점의 시각·행동을 모델링한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p210.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p210.pdf#page=4)
- 접촉·손 조작·긴 과제에서 정책을 비교하고 품질이 낮은 궤적을 따로 활용하는 미세조정이 성능에 미치는 영향을 평가했다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p210.pdf#page=5) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p210.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p210.pdf#page=8)

## Observation–State–Action Interface

비동기 vision·action → multimodal diffusion transformer → 행동·미래 표현.

## Evaluation Scope and Claim Boundary

Simulation과 실제 contact-rich·dexterous·long-horizon 조작을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p210.html) · [저자 project/code](https://github.com/jiangranlv/LDA-1B). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단일 모델의 행동·세계 예측 공유를 새 기여로 제안하기 전에 비교할 핵심 구조다.

## Verification Boundary

저품질 데이터 정의, 데이터 역할별 objective, action/vision rate, 학습 데이터 중복을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
