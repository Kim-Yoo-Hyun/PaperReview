# CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / ICLR
- Authors: Kai Yang, Tianlin Zhang, Zhengbo Wang, Zedong Chu, Xiaolong Wu, Yang Cai, Mu Xu
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: cross-embodiment, local-navigation, flow-policy, reinforcement-learning, imitation-learning, LiDAR
- Aliases: CE-Nav, VelFlow
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html
- Code/Project: https://github.com/amap-cvlab/CE-Nav
- Code: https://github.com/amap-cvlab/CE-Nav
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

CE-Nav는 여러 로봇에 공통인 국소 경로 선택을 먼저 학습하고, 기종별 동역학 차이는 고정된 전문가에 붙인 보정 정책으로 학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=1) · [PDF 2쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=2)

## Core Idea and Contribution

- VelFlow는 고전 계획기가 생성한 자료에서 여러 가능한 속도 명령의 분포를 모방하고, 온라인 강화학습은 기종별 동역학 보정기를 훈련한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=5)
- 여러 이동 형태에서 장애물 회피와 적응을 비교하고, 실물 배포는 Unitree Go2와 MagicDog에서 확인했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=6) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

기하 행동 prior → dynamics-aware refiner → 로봇 제어. 언어 VLA나 단일 공동 갱신 정책과 구분한다.

## Evaluation Scope and Claim Boundary

사족·이족·쿼드로터의 국소 항법은 시뮬레이션에서 비교했다. 실물 배포 대상은 Unitree Go2와 MagicDog다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html) · [저자 project/code](https://github.com/amap-cvlab/CE-Nav).

## 검색 태그 근거

DWA가 생성한 속도 명령을 모방해 VelFlow를 훈련한다. 기체별 PPO 정책은 동결한 VelFlow의 참조 속도와 2D LiDAR·로봇 상태를 받아 실행 속도를 정한다. 사족·이족·쿼드로터 비교는 시뮬레이션에서, 실물 항법은 Go2와 MagicDog에서 수행했다. [원문 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=5) · [원문 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=6) · [원문 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/514bdfb12b318ad02c6f28dc68f2feea-Paper-Conference.pdf#page=9)

## Why This Paper Is Here — Researcher Interpretation

Cross-embodiment VLA-RL의 필요성을 검증할 기하 prior+동역학 적응 기준이다.

## Verification Boundary

planner 관측 접근, dynamics별 상호작용 분모, morphology별 평가 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
