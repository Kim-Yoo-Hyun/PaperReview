# LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
- Authors: Jiaqi Peng, Wenzhe Cai, Yuqiang Yang, Tai Wang, Yuan Shen, Jiangmiao Pang
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: metric-geometry, spatial-memory, Navigation
- Aliases: LoGoPlanner, NavDP--
- Official paper: https://arxiv.org/abs/2512.19629
- Venue verification: https://steinate.github.io/publications/
- Code/Project: https://steinate.github.io/logoplanner.github.io/
- Code: https://github.com/InternRobotics/NavDP
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ICRA 2026 status는 저자 공식 자료 확인; IEEE proceedings 직접 검증 미완료. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LoGoPlanner는 과거 영상에서 실제 거리 척도와 주변 기하를 추정해 이동 로봇의 궤적을 계획한다. [PDF 1쪽](https://arxiv.org/pdf/2512.19629v2#page=1)

## Core Idea and Contribution

- 시각 기하 백본에 위치 추정과 장면 복원을 함께 학습시켜 누적된 관측의 기하 정보를 정책에 전달한다. [PDF 3쪽](https://arxiv.org/pdf/2512.19629v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2512.19629v2#page=4)
- 시뮬레이션과 실제 주행에서 장애물 회피와 계획의 일관성을 평가하고 별도 위치 추정값을 받는 기준선과 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2512.19629v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2512.19629v2#page=6)

## Observation–State–Action Interface

Historical visual observation → metric geometry/implicit localization memory → local trajectory.

## Evaluation Scope and Claim Boundary

저자 abstract/project는 simulation과 real-world navigation, obstacle avoidance 및 embodiment/environment generalization 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.19629) · [저자 project/code](https://steinate.github.io/logoplanner.github.io/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / enabling 3D. Metric-aware geometry와 history 기반 state estimation을 trajectory planning에 연결한다. 일반 reconstruction보다 현재 navigation 목표에 직접적이다. Controller가 실제 사용하는 pose·calibration·simulator GT의 범위는 본문/배포 코드 확인이 필요하다.

## Verification Boundary

정책과 MPC가 각각 보는 pose, calibration, simulator GT 접근 및 metric scale supervision을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
