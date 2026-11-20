# CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kai Yang, Tianlin Zhang, Zhengbo Wang, Zedong Chu, Xiaolong Wu, Yang Cai, Mu Xu
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: cross-embodiment, local-navigation, flow-policy, reinforcement-learning
- Aliases: CE-Nav, VelFlow
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html
- Code/Project: https://github.com/amap-cvlab/CE-Nav
- Code: https://github.com/amap-cvlab/CE-Nav
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

로봇별 동역학 차이와 다봉 행동 분포 때문에 항법 정책 전이가 어렵다.

## Core Idea and Contribution

Planner 데이터로 embodiment-agnostic flow expert를 학습하고 이를 고정한 채 로봇별 경량 refiner를 online RL로 적응한다.

## Observation–State–Action Interface

기하 행동 prior → dynamics-aware refiner → 로봇 제어. 언어 VLA나 단일 공동 갱신 정책과 구분한다.

## Evaluation Scope and Claim Boundary

사족·이족·quadrotor 실험과 실제 배포를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html) · [저자 project/code](https://github.com/amap-cvlab/CE-Nav). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Cross-embodiment VLA-RL의 필요성을 검증할 기하 prior+동역학 적응 기준이다.

## Verification Boundary

planner 관측 접근, dynamics별 상호작용 분모, morphology별 평가 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
