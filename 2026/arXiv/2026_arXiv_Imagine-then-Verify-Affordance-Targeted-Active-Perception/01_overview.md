# Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jingzhi Cui, Xuefeng Liu, Feng Han, Xinyu Liu, Wei Chen, Jianwei Niu
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: active perception, affordance, grasping, shape completion
- Aliases: ATAP
- Official paper: https://arxiv.org/abs/2609.23504
- Venue verification: https://arxiv.org/abs/2609.23504
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인.  공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지.

## Problem and Importance

가려진 기능 영역을 찾는 grasp에서 물체 전체를 스캔하면 관측 budget을 낭비할 수 있다.

## Core Idea and Contribution

완성 shape에서 affordance 가설을 만들고 entropy 감소·실제 관측 검증을 함께 고려해 다음 시점을 정한다.

## Observation–State–Action Interface

부분 관측·task → affordance 후보 → 카메라 시점 → functional grasp로 연결한다.

## Evaluation Scope and Claim Boundary

Simulation과 실제 cluttered scene의 기능적 grasp 및 NBV step을 평가한다. 전체 pouring/insertion 성공과 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.23504). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Task-aware NBV와 verification 기반 중단이 이미 있는 점을 반영할 직접 비교다.

## Verification Boundary

Shape hallucination·hypothesis weighting·view feasibility·stop threshold을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
