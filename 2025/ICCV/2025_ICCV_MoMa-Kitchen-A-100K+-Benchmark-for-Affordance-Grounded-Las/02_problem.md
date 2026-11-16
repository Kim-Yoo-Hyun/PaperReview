# MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

물체 근처까지 항법에 성공해도 팔이 조작 가능한 자세에 도달한 것은 아니다.

## Bottleneck and Changed Formulation

조작 가능 최종 base 위치를 라벨링한 주방 데이터와 affordance baseline을 제공한다.

## System and Robotics Loop

RGB-D 관측·로봇 형상 → 조작 가능한 바닥 위치 → 항법 종료.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

형상별 split, oracle grasp label 생성, navigability와 reachability 정의, 실환경 전이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

여러 팔·platform 높이를 포함한 simulated kitchen affordance 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html) · [저자 project/code](https://momakitchen.github.io/) · [공식 code](https://github.com/MoMaKitchen/MoMaKitchen). Exact objective, constraints, success definition은 본문 수동 확인 필요.
