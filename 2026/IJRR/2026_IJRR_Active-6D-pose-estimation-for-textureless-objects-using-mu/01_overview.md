# Active 6D pose estimation for textureless objects using multi-view RGB frames

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jun Yang, Wenjie Xue, Sahar Ghavidel, Steven L. Waslander
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: active perception, 6D pose, RGB, next-best-view
- Aliases: ActiveODPE
- Official paper: https://api.crossref.org/works/10.1177/02783649251411922
- Venue verification: https://journals.sagepub.com/doi/10.1177/02783649251411922
- Code/Project: https://trailab.github.io/ActiveODPE/
- Code: project_only
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인.

## Problem and Importance

무텍스처·대칭·가림 때문에 단일 RGB 관측만으로 물체 자세를 구별하기 어렵다.

## Core Idea and Contribution

Translation을 먼저 추정하고 canonical-scale template으로 orientation을 추정한 뒤 pose uncertainty를 줄일 다음 view를 선택한다.

## Observation–State–Action Interface

다중 RGB·알려진 물체 geometry와 camera 관측에서 pose 및 다음 카메라 시점을 출력한다.

## Evaluation Scope and Claim Boundary

ROBI·TOD·T-ROBI에서 같은 view의 추정 성능과 적은 view로 얻는 정확도를 비교한다. VLA 행동 효과 평가로 확장하지 않는다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649251411922) · [저자 project/code](https://trailab.github.io/ActiveODPE/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Pose 정확도 중심 NBV와 task 성공 중심 관측 중단을 비교할 journal 기준이다.

## Verification Boundary

CAD·calibration 요구·transparent dataset 조건·실제 이동 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
