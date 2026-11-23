# MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICCV
- Authors: Pingrui Zhang, Xianqiang Gao, Yuhan Wu, Kehui Liu, Dong Wang, Zhigang Wang, Bin Zhao, Yan Ding, Xuelong Li
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: mobile-manipulation, affordance, Navigation, Benchmark
- Aliases: MoMa-Kitchen
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html
- Code/Project: https://momakitchen.github.io/
- Code: https://github.com/MoMaKitchen/MoMaKitchen
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

MoMa-Kitchen은 이동 로봇이 물체에 접근한 뒤 실제로 팔을 뻗어 잡을 수 있는 마지막 정차 위치를 예측하는 벤치마크다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.pdf#page=1)

## Core Idea and Contribution

- 여러 주방과 로봇팔에서 후보 바닥 위치의 파지를 시뮬레이션해 가능 여부를 기록하고 이를 로봇 시점의 RGB-D 관측과 짝지었다. [PDF 2쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.pdf#page=2) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.pdf#page=3)
- NavAff가 예측한 위치별 조작 가능성을 기준 레이블과 비교해, 팔의 종류와 베이스 높이가 달라졌을 때의 예측 성능을 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.pdf#page=6)

## Observation–State–Action Interface

RGB-D 관측·로봇 형상 → 조작 가능한 바닥 위치 → 항법 종료.

## Evaluation Scope and Claim Boundary

여러 팔·platform 높이를 포함한 simulated kitchen affordance 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html) · [저자 project/code](https://momakitchen.github.io/) · [공식 code](https://github.com/MoMaKitchen/MoMaKitchen). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL을 manipulation과 navigation에 통합할 때 성공 조건을 구체화하는 benchmark다.

## Verification Boundary

형상별 split, oracle grasp label 생성, navigability와 reachability 정의, 실환경 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
