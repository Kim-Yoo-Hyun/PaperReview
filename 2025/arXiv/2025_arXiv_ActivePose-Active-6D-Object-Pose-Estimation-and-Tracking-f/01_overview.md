# ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Sheng Liu, Zhe Li, Weiheng Wang, Han Sun, Heng Zhang, Hongpeng Chen, Yusen Qin, Arash Ajoudani, Yizhao Wang
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: active perception, 6D pose, VLM, next-best-view
- Aliases: ActivePose
- Official paper: https://arxiv.org/abs/2509.11364
- Venue verification: https://arxiv.org/abs/2509.11364
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 현재 abstract는 2026-03-07 v2; 최초 공개 연도 2025 유지. 이전 N1의 v1 지정 절 검토와 같은 본문으로 취급하지 않는다. 공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지.

## Problem and Importance

고정 카메라와 pose ambiguity가 물체 이동·가림 상황의 추정과 추적을 불안정하게 한다.

## Core Idea and Contribution

CAD virtual view와 FoundationPose 기반 정보로 VLM이 모호성을 평가하고 다음 camera view를 선택한다.

## Observation–State–Action Interface

RGB 관측·CAD 기반 가상 시점 → ambiguity score·NBV·pose tracking으로 이어진다.

## Evaluation Scope and Claim Boundary

공식 초록은 로봇 조작을 위한 active pose estimation/tracking을 다룬다. Task별 성공률과 camera 이동 비용은 본문 확인 필요다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.11364). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Pose estimation+active perception 조합이 이미 구현됐음을 보여 주는 직접 선행이다.

## Verification Boundary

VLM score calibration·CAD render 조건·물리 camera 비용·task success 기준을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
