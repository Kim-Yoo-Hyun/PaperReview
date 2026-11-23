# Active 6D pose estimation for textureless objects using multi-view RGB frames

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IJRR
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 여러 RGB 시점에서 무늬 없는 물체의 위치와 방향을 추정하고, 남은 자세 모호성을 해소할 다음 카메라 위치를 고른다. [PDF 1쪽](https://arxiv.org/pdf/2503.03726v2#page=1)

## Core Idea and Contribution

- 먼저 삼차원 병진을 추정한 뒤 공통 크기의 형판과 비교해 회전을 구하며, 예상 자세 불확실성에 따라 추가 시점을 선택한다. [PDF 5쪽](https://arxiv.org/pdf/2503.03726v2#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2503.03726v2#page=7) · [PDF 10쪽](https://arxiv.org/pdf/2503.03726v2#page=10)
- ROBI·TOD와 투명 물체 T-ROBI에서 같은 시점의 추정 정확도를 비교하고, 목표 정확도에 도달하는 데 필요한 관측 수를 시점 선택 방식별로 평가했다. [PDF 15쪽](https://arxiv.org/pdf/2503.03726v2#page=15) · [PDF 18쪽](https://arxiv.org/pdf/2503.03726v2#page=18) · [PDF 19쪽](https://arxiv.org/pdf/2503.03726v2#page=19)

## Observation–State–Action Interface

다중 RGB·알려진 물체 geometry와 camera 관측에서 pose 및 다음 카메라 시점을 출력한다.

## Evaluation Scope and Claim Boundary

ROBI·TOD·T-ROBI에서 같은 view의 추정 성능과 적은 view로 얻는 정확도를 비교한다. VLA 행동 효과 평가로 확장하지 않는다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649251411922) · [저자 project/code](https://trailab.github.io/ActiveODPE/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Pose 정확도 중심 NBV와 task 성공 중심 관측 중단을 비교할 journal 기준이다.

## Verification Boundary

CAD·calibration 요구·transparent dataset 조건·실제 이동 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
