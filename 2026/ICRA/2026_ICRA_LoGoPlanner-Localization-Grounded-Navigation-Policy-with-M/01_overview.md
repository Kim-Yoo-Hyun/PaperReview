# LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ICRA 2026 status는 저자 공식 자료 확인; IEEE proceedings 직접 검증 미완료.

## Problem and Importance

별도 localization/mapping module에 의존하는 navigation pipeline에서 latency와 오차 전파를 줄이는 문제다.

## Core Idea and Contribution

Visual geometry backbone을 metric scale에 맞추고 history 기반 geometry를 복원하여 navigation policy를 conditioning한다.

## Observation–State–Action Interface

Historical visual observation → metric geometry/implicit localization memory → local trajectory.

## Evaluation Scope and Claim Boundary

저자 abstract/project는 simulation과 real-world navigation, obstacle avoidance 및 embodiment/environment generalization 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.19629) · [저자 project/code](https://steinate.github.io/logoplanner.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / enabling 3D. Metric-aware geometry와 history 기반 state estimation을 trajectory planning에 연결한다. 일반 reconstruction보다 현재 navigation 목표에 직접적이다. Controller가 실제 사용하는 pose·calibration·simulator GT의 범위는 본문/배포 코드 확인이 필요하다.

## Verification Boundary

정책과 MPC가 각각 보는 pose, calibration, simulator GT 접근 및 metric scale supervision을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
