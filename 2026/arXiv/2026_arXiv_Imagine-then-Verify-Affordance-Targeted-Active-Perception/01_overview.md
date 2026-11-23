# Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인.  공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ATAP는 가려진 물체 전체를 스캔하는 데 쓰이는 관측 횟수를 줄이기 위해 지시한 용도에 맞는 파지 부위를 확인할 다음 시점을 고른다. [PDF 1쪽](https://arxiv.org/pdf/2609.23504v1#page=1)

## Core Idea and Contribution

- 부분 관측을 완성한 물체 형상에서 가능한 기능 부위들을 추정하고, 예상 엔트로피 감소와 실제 관측으로 부위를 확인할 이득을 함께 평가한다. [PDF 3쪽](https://arxiv.org/pdf/2609.23504v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2609.23504v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.23504v1#page=5)
- 가려진 시뮬레이션·실물 장면에서 단순 파지와 기능 부위 파지의 성공률을 구분하고 고정 시점·복원 중심 탐색과 관측 횟수를 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2609.23504v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2609.23504v1#page=7)

## Observation–State–Action Interface

부분 관측·task → affordance 후보 → 카메라 시점 → functional grasp로 연결한다.

## Evaluation Scope and Claim Boundary

Simulation과 실제 cluttered scene의 기능적 grasp 및 NBV step을 평가한다. 전체 pouring/insertion 성공과 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.23504). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Task-aware NBV와 verification 기반 중단이 이미 있는 점을 반영할 직접 비교다.

## Verification Boundary

Shape hallucination·hypothesis weighting·view feasibility·stop threshold을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
