# Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Yurou Yang, Muyuan Lin, Roberto Martin-Martin, Martin Labrie, Shreekant Gayaka, Cheng-Hao Kuo, Luca Carlone
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, 3D reconstruction, geometry fusion, representation probing
- Aliases: Geometry Impact Analysis
- Official paper: https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2
- Venue verification: https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-18: arXiv 초록·공식 publication/project를 확인한 등록. Abstract 기반 — 본문 수동 확인 필요. 연구 dossier의 지정 절 검토와 paper별 5-note의 evidence를 구별하며 사용자 읽기 상태는 변경하지 않음. Springer ECCV2026 chapter DOI 10.1007/978-3-032-37271-0_2와 2026-09-11 출판일 확인. 본문 전체는 별도 검토이며 code는 not identified. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 GR00T-N1.5의 표현이 기하 정보를 얼마나 담는지, 그리고 VGGT의 기하를 제공하는 방식이 조작 행동을 어떻게 바꾸는지 비교한다. [PDF 1쪽](https://arxiv.org/pdf/2605.24642v1#page=1)

## Core Idea and Contribution

- 선형 탐침으로 정책과 기하 모델의 특징에서 깊이 등을 예측한 뒤, 동일한 기반 정책에 기하 특징을 결합하는 세 구조를 통제된 조건에서 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2605.24642v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2605.24642v1#page=8)
- RoboCasa와 실제 Unitree G1에서 구조별 성능을 비교하고 카메라 수·자료 구성·재구성 품질 등 구조 외 조건에 따라 결과가 달라짐을 조사했다. [PDF 11쪽](https://arxiv.org/pdf/2605.24642v1#page=11) · [PDF 13쪽](https://arxiv.org/pdf/2605.24642v1#page=13)

## Observation–State–Action Interface

영상/언어 기반 VLA에 geometric foundation model의 정보를 결합한다. 정책 입력·학습 방식·카메라 수의 차이를 비교 변수로 구별한다.

## Evaluation Scope and Claim Boundary

공식 초록은 특정 VLA/GFM 조합의 표현 probing, 결합 구조 세 가지, 데이터·카메라 수·재구성 품질의 영향을 비교한다. 모든 VLA에 대한 보편 결론이나 동일 상태 오류 개입 실험을 뜻하지 않는다.

근거: [공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

단순 geometry 오차–성공률 상관도 이미 분석됐음을 확인할 직접 NEXT다. 신규 후보는 동일 상태 개입·단순 대안 이후의 차이를 보여야 한다.

## Verification Boundary

Probe 용량 차이·architecture별 파라미터/학습량·재구성 품질의 측정 단위·task/data split·real-robot 범위를 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
