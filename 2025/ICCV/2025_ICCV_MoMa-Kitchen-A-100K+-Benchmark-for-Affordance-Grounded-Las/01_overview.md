# MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

물체 근처까지 항법에 성공해도 팔이 조작 가능한 자세에 도달한 것은 아니다.

## Core Idea and Contribution

조작 가능 최종 base 위치를 라벨링한 주방 데이터와 affordance baseline을 제공한다.

## Observation–State–Action Interface

RGB-D 관측·로봇 형상 → 조작 가능한 바닥 위치 → 항법 종료.

## Evaluation Scope and Claim Boundary

여러 팔·platform 높이를 포함한 simulated kitchen affordance 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html) · [저자 project/code](https://momakitchen.github.io/) · [공식 code](https://github.com/MoMaKitchen/MoMaKitchen). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL을 manipulation과 navigation에 통합할 때 성공 조건을 구체화하는 benchmark다.

## Verification Boundary

형상별 split, oracle grasp label 생성, navigability와 reachability 정의, 실환경 전이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
