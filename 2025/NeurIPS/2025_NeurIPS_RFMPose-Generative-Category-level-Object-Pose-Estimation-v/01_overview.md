# RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Wenzhe Ouyang, Jinghua Wang, Zenglin Xu, Jiming Chen, Qi Ye
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 6D pose, Flow Matching, multi-hypothesis, symmetry
- Aliases: RFMPose
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html
- Code/Project: https://github.com/shabiouyang/RMFPose
- Code: https://github.com/shabiouyang/RMFPose
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 공식 repository 철자는 RMFPose다. 논문의 likelihood 제안과 이전 코드 감사의 특정 aggregation 경로를 구별한다.

## Problem and Importance

Category-level pose의 대칭과 다중 가능한 해를 한 점 추정만으로 표현하기 어렵다.

## Core Idea and Contribution

Riemannian flow와 geodesic 경로·optimal transport를 사용하며 likelihood 추정 경로를 제안한다.

## Observation–State–Action Interface

물체 관측의 category-level 6D pose 후보를 생성한다. Generative likelihood는 task 성공 확률과 별개다.

## Evaluation Scope and Claim Boundary

Omni6DPose의 pose metric과 sim-to-real/추적 확장을 보고한다. 이번 등록에서는 정책 제어 trial을 추정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) · [저자 project/code](https://github.com/shabiouyang/RMFPose). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

유한 pose 가설 생성과 score 해석을 비교하는 직접 NEXT다.

## Verification Boundary

Likelihood 구현·symmetry convention·공개 checkpoint·tracking 평가 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
