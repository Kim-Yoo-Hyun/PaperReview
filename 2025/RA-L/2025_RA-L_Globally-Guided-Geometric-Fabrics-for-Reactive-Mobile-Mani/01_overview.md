# Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Tomas Merva, Saray Bakker, Max Spahn, Danning Zhao, Ivan Virgala, Javier Alonso-Mora
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: mobile-manipulation, motion-planning, grasping
- Aliases: G3F
- Official paper: https://api.crossref.org/works/10.1109/LRA.2025.3562005
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3562005
- Code/Project: https://autonomousrobots.nl/paper_websites/g3f
- Code: https://github.com/TomasMerva/g3f_planner
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. IEEE DOI deposit와 저자 연구실 abstract를 함께 확인했다.

## Problem and Importance

동적 환경에서 전체 task를 고려하며 mobile robot motion을 즉시 수정한다.

## Core Idea and Contribution

최적화 planner와 reactive geometric fabrics를 결합하고 대체 목표 pose를 탐색한다.

## Observation–State–Action Interface

Robot/환경 state → global guidance → reactive whole-body motion.

## Evaluation Scope and Claim Boundary

다중 mobile manipulator의 simulation 및 실제 실험을 보고한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/LRA.2025.3562005) · [저자 project/code](https://autonomousrobots.nl/paper_websites/g3f). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D2에서 grasp/place 변경과 전체 경로 reasoning의 기하학 baseline이다.

## Verification Boundary

object pose 가용성, collision geometry, 목표 pose 자유도, 계산 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
