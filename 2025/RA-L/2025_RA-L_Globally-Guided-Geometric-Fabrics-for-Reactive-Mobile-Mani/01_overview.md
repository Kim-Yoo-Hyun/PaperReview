# Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / RA-L
- Authors: Tomas Merva, Saray Bakker, Max Spahn, Danning Zhao, Ivan Virgala, Javier Alonso-Mora
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: mobile-manipulation, motion-planning, grasping
- Aliases: G3F
- Official paper: https://api.crossref.org/works/10.1109/LRA.2025.3562005
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245
- Venue verification: https://api.crossref.org/works/10.1109/LRA.2025.3562005
- Code/Project: https://autonomousrobots.nl/paper_websites/g3f
- Code: https://github.com/TomasMerva/g3f_planner
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

G3F는 전체 과제 구간을 고려하는 최적화 계획기와 빠른 국소 제어기를 결합해 이동형 로봇팔이 동적 장애물에 반응하게 한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=1)

## Core Idea and Contribution

- 전역 경로와 허용 가능한 목표 자세를 갱신하면서 로봇 전신의 충돌·물리 제약을 반영하는 기하 기반 운동을 생성한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=5)
- 장애물과 목표가 움직이는 조건에서 기준 방법의 과제 수행을 비교하고 실제 로봇의 이동 조작을 평가했다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=10967245#page=8)

## Observation–State–Action Interface

Robot/환경 state → global guidance → reactive whole-body motion.

## Evaluation Scope and Claim Boundary

다중 mobile manipulator의 simulation 및 실제 실험을 보고한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/LRA.2025.3562005) · [저자 project/code](https://autonomousrobots.nl/paper_websites/g3f). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

D2에서 grasp/place 변경과 전체 경로 reasoning의 기하학 baseline이다.

## Verification Boundary

object pose 가용성, collision geometry, 목표 pose 자유도, 계산 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
